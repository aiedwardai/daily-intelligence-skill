# Cron 故障手动回退流程

> 当 LLM 驱动型 cron job（每日情报、arXiv、SPCX）因模型 provider 超时或审批拦截失败时的恢复流程。

## 快速诊断

```bash
# 1. 查 cron 列表，看 last_status
cronjob(action='list')

# 2. 查错误日志
tail -100 ~/.hermes/logs/errors.log
grep -i "524\|timeout\|pending_approval\|APIConnectionError" ~/.hermes/logs/errors.log | tail -20

# 3. 确认 provider 状态
curl -sI --connect-timeout 5 "https://api.bjlab.tk/v1/models" 2>&1 | head -5

# 4. 查 cron 配置是否拦截终端命令
grep "cron_mode" ~/.hermes/config.yaml
```

## 常见失败模式

| 症状 | 根因 | 对策 |
|------|------|------|
| last_status=error, 日志有 `HTTP 524` | 模型 API 源站超时（Cloudflare 代理 120s 上限） | 手动回退执行 |
| 日志有 `pending_approval` | `cron_mode: deny` 拦截终端命令 | 手动回退或改配置 |
| 日志有 `stream expired` / `no chunks for Ns` | 模型流式响应超时 | 手动回退，或改为更短的 prompt |
| 日志有 `APIConnectionError` | API 完全不可连 | 换 provider 或等恢复 |
| 执行报 `config drifted since this job was created` | 全局 provider/model 变更后旧 job 未固定 | 更新 job 时显式指定 provider+model 参数锁定 |

## 手动回退执行（以每日情报为例）

### 推荐方案：并行 delegate_task（最快，3-5 分钟）

数据源按"独立无依赖"分组，用 3-4 个 delegate_task 并行拉取：

```text
批次 A: CoinGecko + AIHOT → 纯终端 curl
批次 B: 腾讯新闻 → news-aggregator-skill fetch_news.py --source tencent
批次 C: Twitter/X → web_search 广泛搜索账号名
批次 D: 喷嚏图卦 + 泰伯早报 → fetch_dapenti.py + fetch_taibo.py
```

1. 先拉批次 A + B（纯 API，最快返回）
2. 同时拉批次 C（web_search 密集，需 15-30+ 次搜索）
3. 同时拉批次 D（本地脚本，秒回）

### 编译日报

收集所有子代理输出后：
1. 按 8 大主题（AI·Web3·区块链·比特币·科技·融资·金融·股票）分组筛选
2. 每条带来源链接
3. 用 `write_file` 写入 `~/wiki/queries/daily-intelligence-YYYY-MM-DD.md`
4. 末尾附数据源状态表
5. `cd ~/wiki && git add && git commit && git push`

### 之后通知用户

直接 deliver 完整日报到当前会话。

## 注意事项

- **子代理可能被安全拒绝**：向子代理请求搜索喷嚏图卦、Reddit 等中文政治/社交媒体内容时，model 可能安全拒绝（"无法给到相关内容"）。此时退出 delegate_task，改在主会话中直接用 terminal/web_search 查询
- **GitHub raw 文件获取慢**：raw.githubusercontent.com 在国内可能超时。改用 `api.github.com/repos/<user>/<repo>/contents/` 拿文件列表
- **不要编造数据**：所有价格、新闻必须有真实搜索来源支撑。标明"本日未获取"的源