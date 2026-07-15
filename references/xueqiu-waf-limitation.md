## 雪球 WAF 限制补充（2026-06-16）

### 核心限制

雪球全站受阿里云WAF保护，从境外服务器调用**任何API端点**均返回JS验证页面而非数据：

```bash
# 即使是带有效Cookie的请求
curl -s "https://xueqiu.com/v4/statuses/user_timeline.json?user_id=8790885129"
# → 返回 <textarea id="renderData"> 含 _waf_bd8ce2ce37 加密token
# → 以及 80KB+ 混淆JS挑战，不是JSON数据
```

WAF特征：
- 响应中包含 `<meta name="aliyun_waf_aa">`、`aliyunwaf_6a6f5ea8` 等标记
- Cookie中的 `acw_tc` 参数是WAF挑战ID
- 即使 `xq_a_token` 和 `xq_r_token` 有效，WAF层仍然拦截
- 需要浏览器环境执行JS才能通过挑战

### 影响范围

| 功能 | 状态 |
|:----|:----|
| `XueqiuChannel.get_hot_posts()` | ✅ 正常（agent-reach内置了WAF绕过） |
| 直接 curl API | ❌ 被WAF拦截 |
| browser_navigate 到xueqiu.com | ❌ 超时（WAF + 跨境） |
| RSSHub xueqiu 路由 | ❌ 同样被阻挡 |
| web_search 缓存 | ⚠️ 有时能搜到 |

### 大V用户追踪脚本

已配置的追踪脚本位于 `~/.hermes/scripts/xueqiu_tracker.py`，通过多渠道尝试获取：
1. RSSHub镜像（可能被挡）
2. web_search缓存（不稳定）
3. 直接API（被WAF挡）

详见 `references/xueqiu-user-tracking.md`。
