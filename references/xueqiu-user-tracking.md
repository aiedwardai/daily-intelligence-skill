# 雪球大V用户追踪

雪球受阿里云WAF深度保护（Aliyun Web Application Firewall），从境外服务器直接调用API「不可行」——即使带有有效的登录Cookie，API端点（如 `v4/statuses/user_timeline.json`）仍返回JS验证挑战而非JSON数据。

## 可用的替代数据获取路径

| 方法 | 效果 | 备注 |
|:----|:----|:-----|
| `XueqiuChannel.get_hot_posts()` | ✅ 可用 | agent-reach 内置，适用于热帖而非特定用户 |
| web_search 雪球用户缓存 | ⚠️ 偶尔可用 | 跨境网络不稳定时可能超时 |
| RSSHub 镜像 | ❌ 不可用 | rsshub.app 被WAF同样阻挡 |
| 直接 curl API | ❌ 不可用 | 返回 Aliyun WAF JS挑战页面 |

## 已收录大V用户信息

所有13位用户的雪球ID已查全并硬编码在脚本中：

| 用户 | ID | 方向 |
|:----|:--:|:----|
| 超级鹿鼎公 | 8790885129 | 资源+高股息 |
| 六亿居士 | 9391624441 | 指数基金定投 |
| 管我财 | 9650668145 | 低估逆向价值 |
| qzy69 | 1205946512 | 低估值高股息 |
| HIS1963 | 1760673340 | 高股息/周期 |
| 郑qq | 7106659159 | 地产/低估值 |
| 二鸟说 | 3502863673 | 基金投资 |
| 张翼轸 | 3559889031 | ETF/量化 |
| 饕餮海 | 1314783718 | 可转债 |
| 山行 | 4111857140 | 可转债/低风险 |
| 小卡叔 | 6854054227 | 可转债 |
| 优美 | 5091457148 | 低风险投资 |
| 大道无形我有型 | slowisquick | 价值投资（段永平） |

## 脚本位置

- **数据脚本**: `~/.hermes/scripts/xueqiu_tracker.py`
- **包装器**: `~/.hermes/scripts/xueqiu_wrapper.sh`（tee stdout + 存入wiki + git push）
- **Cron ID**: `4b78f05e7441`，每天 07:00，no_agent 模式
- **Wiki路径**: `~/wiki/queries/xueqiu-tracker-YYYY-MM-DD.md`

## 未来解决方案（如需稳定抓取）

1. **RSSHub 自建实例** — 在境内服务器部署绕过WAF
2. **浏览器自动化** — Puppeteer/Playwright 在境内节点渲染JS
