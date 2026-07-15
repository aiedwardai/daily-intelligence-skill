# 数据源爬取技术与注意事项

本文件记录从各数据源抓取内容时发现的技术细节和踩坑经验。

## AIHOT API

URL: `https://aihot.virxact.com/api/public/`
- 匿名访问，无需 token
- 限流 600 req/min/IP
- 所有请求必须带浏览器 UA 头，否则 403
- `mode=selected` 精选模式，`mode=all` 全量模式
- `since` 参数为 ISO 8601 UTC 时间戳
- `category` 取值：ai-models, ai-products, industry, paper, tip
- 关键词搜索：`?q=xxx` 在 title + summary 三列匹配
- 默认 `since=now-7d`（服务端硬上限）
- 翻页：response.nextCursor → 塞入下次请求的 `cursor` 参数

## CoinGecko 加密货币行情

公开 API，无需 Key：

```bash
curl -s "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd&include_24hr_change=true"
```

返回：`{"bitcoin":{"usd":61742,"usd_24h_change":0.065}}`

## Alternative.me 恐慌与贪婪指数

公开 API，无需 Key：

```bash
curl -s "https://api.alternative.me/fng/?limit=1"
```

返回：`{"data":[{"value":"9","value_classification":"Extreme Fear",...}]}`

取值 0-100：0-24 = Extreme Fear, 25-44 = Fear, 45-54 = Neutral, 55-74 = Greed, 75-100 = Extreme Greed

## BTC ETF 数据源

### Coinglass
- BTC ETF 资金流: `https://www.coinglass.com/etf/bitcoin`
- 灰度持仓: `https://www.coinglass.com/etf/bitcoin/GBTC`
- 有反爬限制，优先用 web_search 或 CoinDesk 替代

### Farside Investors (推荐)
- `https://farside.co.uk/btc/` — BTC ETF 净流入流出数据
- 或通过 web_search 搜索 "bitcoin etf flows farside YYYY" 获取

### CoinDesk
- 用于 BTC ETF 深度分析和市场评论
- 搜索 "bitcoin etf" site:coindesk.com

## Foresight News

- URL: https://foresightnews.pro/
- 网页有反爬限制（Access Restricted），无法直接 browser 或 curl 抓取
- **优先用 web_search** 替代直接抓取
- 搜索模式：`site:foresightnews.pro 区块链 2026`
- 英文版：https://global.foresightnews.pro/

## 喷嚏图卦 (dapenti.com)

> 内容保留，去除结尾总结/评论部分。通过 fetch_dapenti.py 脚本自动获取。

### 使用方法
```bash
python3 ~/.hermes/scripts/fetch_dapenti.py
# 输出: 【N】编号的新闻条目（已剔除结尾的"@泰伯"等编辑评论）
```

### 技术实现
脚本 `~/.hermes/scripts/fetch_dapenti.py` 自动：
1. 抓取列表页 `blog.asp?name=xilei&subjectid=70`
2. 提取最新喷嚏图卦的文章链接
3. 抓取文章全文
4. 解析编号条目 【1】~【N】，自动丢弃条目后的编辑评论部分
5. 输出干净的 Markdown 格式内容

### 编码
- 列表页和文章页均使用 gb2312/gbk 编码
- Python 中需 `decode("gbk", errors="replace")`

## 泰伯早报 (taibo.cn) — 已恢复

> 内容保留（仅新闻条目，无编辑评论）。通过 fetch_taibo.py 脚本自动获取。

### 最新一期 URL 获取
```python
# 浏览器方案
browser_navigate("https://www.taibo.cn/")
# 提取早报链接 href
### 最新一期 URL 获取
最新早报地址：`https://www.taibo.cn/info/zaobao`（也可能是 `/p/{数字ID}`）

### 内容提取
泰伯早报内容存在于静态 HTML 中（**非 JS 渲染**），`class="article-content"` 即可提取完整的板块内容（商业航天/低空经济/时空智能/企业出海）。

```bash
curl -sL --max-time 15 -H "User-Agent: ..." "https://www.taibo.cn/p/{ID}" \
  | python3 -c "
import re, sys
html = sys.stdin.read()
m = re.search(r'<div[^>]*class=\"article-content\"[^>]*>(.*?)</div>', html, re.DOTALL)
if m:
    text = re.sub(r'<[^>]+>', '', m.group(1))
    print(text.strip())
"
```
备用方案（当 curl 因 JS 动态加载失败时）：使用 browser_navigate 后从 DOM 提取。

### URL 模式
`https://www.taibo.cn/p/{数字ID}`（ID 每日递增）

### 爬取注意事项
- 首页 SSR 渲染，可稳定获取链接
- UA 必须带浏览器标识，否则 403
- 文章正文包含多个板块：商业航天、低空经济、时空智能、企业出海

## Twitter/X Cookie 配置

### 配置流程
1. 用户在浏览器登录 x.com
2. 安装 Cookie-Editor Chrome 插件
3. 点击插件 → Export → Header String
4. 将字符串发给 Agent
5. Agent 执行：

```bash
agent-reach configure twitter-cookies "header-string-copied-from-browser"
```

### 环境变量持久化
`agent-reach configure` 将认证令牌存到 `~/.agent-reach/config.yaml`：
```yaml
twitter_auth_token: "..."
twitter_ct0: "..."
```

要让 `twitter-cli` 在 Hermes 中生效，还需将环境变量写入 `~/.hermes/.env`：
```bash
echo 'TWITTER_AUTH_TOKEN=*** >> ~/.hermes/.env
echo "TWITTER_CT0=<ct0-value>" >> ~/.hermes/.env
```

### Twitter CLI 命令速查

⚠️ **关键区别：`twitter user` vs `twitter user-posts`**
- `twitter user @handle --json` → 返回**用户资料**（bio、粉丝数、推文数），**不含推文内容**
- `twitter user-posts @handle --json` → 返回**用户的实际推文列表**（文本、指标、媒体）

```bash
# 检查认证状态
twitter status

# 查看用户资料（不含推文）
twitter user @elonmusk --json

# 获取用户实际推文 ✅ 这是日报数据源的正确命令
twitter user-posts @elonmusk --json

# 搜索用户推文（替代方案）
twitter search --from elonmusk --json

# 获取首页 feed
twitter feed --json

# 获取指定用户的喜欢
twitter likes @username

# 保存 JSON 输出到文件（方便后续分析）
twitter user-posts @elonmusk --json > /tmp/musk.json
```

#### 在日报工作流中的正确用法

```bash
# 拉取5位关注人物的最新推文（日报数据源步骤）
twitter user-posts @elonmusk --json
twitter user-posts @sama --json
twitter user-posts @realDonaldTrump --json
twitter user-posts @nvidia --json
twitter search "from:@DarioAmodei" --json   # Dario 的搜索语法略有不同
```

### 已知问题
- Cookie 可能因服务器 IP 与签发 IP 不一致而 401 过期
- 过期后需要用户重新导出 Cookie
- 从中国大陆服务器访问可能较慢（需要长 timeout）

## Reddit (rdt-cli)

### 安装

```bash
agent-reach install --channels reddit
# pipx install rdt-cli (fallback)
```

### 认证方式

⚠️ Reddit 2024 年起要求登录认证。服务器上无浏览器，需手动注入 Cookie：

1. 用户在浏览器登录 reddit.com
2. Cookie-Editor 插件 → Export → Header String
3. Agent 解析 Cookie 字符串并写入 credential.json

**手动创建 credential.json**（`rdt login` 不支持 `--cookies` 参数）：

```python
# /home/admin/.config/rdt-cli/credential.json
{
  "cookies": {
    "token_v2": "...",
    "reddit_session": "...",
    "csrf_token": "...",
    ...
  },
  "source": "manual",
  "username": null,
  "modhash": null,
  "saved_at": 1781178404.0,
  "last_verified_at": 1781178404.0
}
```

### 验证状态

```bash
rdt status --json
# 返回 {"data": {"authenticated": true, "username": "..."}}
```

### 命令速查

```bash
# 搜索帖子
rdt search "AI agents" -n 3 --json           # 指定条数 + JSON
rdt search "AI agents" -n 3 --json -o /tmp/out.json  # 保存到文件
rdt search "AI agents" -s top -t week -n 5    # 按热度·周榜排序

# 浏览子版块
rdt sub python -n 10                          # r/Python 最新
rdt sub "artificial" -s top -t month          # 月榜排序

# 热帖
rdt popular -n 10
rdt all -n 5

# 阅读帖子内容
rdt read <post-id>                            # 读取帖子+评论
rdt read <post-id> -c                         # 紧凑模式

# 用户信息
rdt user <username>
```

### 已知问题
- `rdt login` 仅支持从本地浏览器提取 Cookie，服务器上需手动创建 credential.json
- credential 有效期 7 天，过期后需要重新导入
- 贴子 ID 是 Reddit 提供的 `t3_xxx` 格式，使用 `rdt read` 时去掉前缀

## 雪球 (agent-reach 内置模块)

### 安装

```bash
agent-reach install --channels xueqiu
```

### 认证方式

⚠️ 雪球股票 API 需要登录 Cookie（`xq_a_token`）。服务器上无浏览器，需手动配置：

1. 用户在浏览器登录 xueqiu.com
2. Cookie-Editor 插件 → Export → Header String
3. Agent 写入 `~/.agent-reach/config.yaml`

**注意：`agent-reach configure` 没有 `xueqiu-cookies` 参数，需直接写配置文件**：

```python
import yaml, os
config_file = os.path.expanduser("~/.agent-reach/config.yaml")
data = {}
if os.path.exists(config_file):
    with open(config_file) as f:
        data = yaml.safe_load(f) or {}
data["xueqiu_cookie"] = "xq_a_token=xxx; xq_r_token=xxx; ..."
with open(config_file, "w") as f:
    yaml.dump(data, f)
os.chmod(config_file, 0o600)
```

### 验证状态

```python
from agent_reach.channels.xueqiu import XueqiuChannel
ch = XueqiuChannel()
status, msg = ch.check()
# 返回 ("ok", "公开 API 可用（行情、搜索、热帖、热股）")
```

### 数据获取 API

**热帖**（最常用于日报）：
```python
ch = XueqiuChannel()
posts = ch.get_hot_posts(limit=5)
for p in posts:
    print(p.get("title", ""))
```

### 已知问题
- `agent-reach configure` CLI 不支持 `xueqiu-cookies` 子命令，必须直接写 YAML
- 需要 `xq_a_token` 和 `xq_r_token` 两个关键 Cookie 才能正常工作
- 雪球 Cookie 有效期较长，暂无 TTL 限制

## 公众号 / 抖音

微信和抖音均为封闭生态，无法从服务器端直接抓取内容。每次日报末尾提示：
```
❌ 公众号（猫笔刀、孟岩的区块链思考）：不可用
❌ 抖音（金岩石、李孔越）：不可用
```