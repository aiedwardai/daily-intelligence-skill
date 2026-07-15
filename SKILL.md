---
name: daily-intelligence
description: 每日情报筛选系统。整合 news-aggregator-skill(44+源), aihot, ai-daily-news, tencent-news, Web3/区块链数据, Twitter/X关注人物，按主题（AI·Web3·区块链·比特币·科技·融资·金融·股票）筛选并生成日报。
version: 1.5.1
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [news, daily, intelligence, filter, ai, web3]
    related_skills: [aihot, news-aggregator-skill, ai-daily-news, tencent-news, second-brain]
---

# 每日情报筛选系统（Daily Intelligence）

## 数据源全景

本 Skill 整合以下 News Skill：**aihot**（AI 中文资讯）、**ai-daily-news**（全球 AI 新闻）、**news-aggregator-skill**（44+ 源全能聚合器）、**tencent-news**（腾讯新闻 7×24 资讯），外加 Web3/区块链专有数据源。

此外，本 Skill 可委托 `source-gathering` skill 执行多维度新闻素材收集（web_search 采集 → 原始池 → 压缩精选 → 推荐主线），以获得更结构化的素材池。

### 一、聚合新闻源（整合 news-aggregator-skill + aihot + ai-daily-news + tencent-news）

| 类别 | 源名 | 来源 Skill | 是否关注 |
|------|------|-----------|---------|
| **Global** | Hacker News | news-aggregator-skill | ✅ |
| | 36氪 | news-aggregator-skill | ✅ |
| | 华尔街见闻 WallStreetCN | news-aggregator-skill | ✅ |
| | 腾讯新闻 | tencent-news + news-aggregator-skill | ⚠️ 仅需科技相关 |
| | 微博热搜 | news-aggregator-skill | ⚠️ 仅需科技/Web3 |
| | V2EX | news-aggregator-skill | ✅ |
| | Product Hunt | news-aggregator-skill | ✅ |
| | GitHub Trending | news-aggregator-skill | ✅ |
| **AI Curated** | AIHOT (aihot.virxact.com) | aihot | ✅ |
| | TLDR AI (英文日刊) | news-aggregator-skill | ✅ |
| | Import AI (Jack Clark 周刊) | news-aggregator-skill | ✅ |
| | AI Daily News 远程数据集 | ai-daily-news | ✅ |
| **AI/Tech** | Hugging Face Papers | news-aggregator-skill | ✅ |
| | arXiv (cs.AI/cs.CL/cs.LG) | news-aggregator-skill | ✅ |
| | Ben's Bites | news-aggregator-skill | ✅ |
| | Interconnects | news-aggregator-skill | ✅ |
| | One Useful Thing | news-aggregator-skill | ✅ |
| | ChinAI | news-aggregator-skill | ✅ |
| | Memia | news-aggregator-skill | ✅ |
| | AI to ROI | news-aggregator-skill | ✅ |
| | KDnuggets | news-aggregator-skill | ✅ |
| **Tech** | Lobsters | news-aggregator-skill | ✅ |
| | Dev.to | news-aggregator-skill | ✅ |
| **Chinese** | 少数派 sspai | news-aggregator-skill | ✅ |
| | InfoQ 中文 | news-aggregator-skill | ✅ |
| **International** | BBC / Guardian / Al Jazeera / France 24 / Reuters | news-aggregator-skill | ⚠️ 仅需科技/AI |

### 二、AI Daily News（远程API）
来自 `ai-daily-news` skill 的远程数据集，覆盖全球AI新闻。

### 三、Web3/区块链专属数据源（来自 Web3 PDF）
| 源名 | 用途 | 类别 |
|------|------|------|
| Coinglass | BTC现货ETF资金流 | 区块链/比特币 |
| CoinGecko | 加密货币实时报价 | 区块链/比特币 |
| CoinMarketCap | 交易所交易量排名 | 区块链/金融 |
| Foresight News | Web3/区块链新闻 | Web3/区块链 |
| Whale Alert | 巨鲸链上转账监控 | 区块链/比特币 |
| Grayscale GBTC | 灰度BTC持仓 | 区块链/比特币 |
| iShares IBIT | BTC ETF持仓 | 区块链/比特币 |
| Fidelity FBTC | BTC ETF持仓 | 区块链/比特币 |
| VanEck HODL | BTC ETF持仓 | 区块链/比特币 |
| Hey Apollo | BTC ETF数据 | 区块链/比特币 |

### 三、用户自定义源
| 源名 | 类型 | 可获取性 |
|------|------|----------|
| @elonmusk (马斯克) | Twitter/X | ✅ 已配置 |
| @realDonaldTrump (特朗普) | Twitter/X | ✅ 已配置 |
| @sama (Sam Altman) | Twitter/X | ✅ 已配置 |
| Dario Amodei (Anthropic CEO) | Twitter/X | ✅ 已配置 |
| @nvidia (NVIDIA官方) | Twitter/X | ✅ 已配置 |
| @aleabitoreddit (白毛股神 Serenity) | Twitter/X | ✅ 已配置 — AI/半导体供应链分析 |
| Reddit (AI/科技/金融子版块) | rdt-cli | ✅ 已登录 ActivityCorrect2434 |
| 雪球 (热帖/行情) | agent-reach | ✅ 已配置 Cookie |
| 喷嚏网/喷嚏图卦 | 喷嚏网公开网页 | ✅ fetch_dapenti.py（已去除结尾评论） |
| 泰伯网/泰伯早报 | taibo.cn | ✅ fetch_taibo.py（商业航天/低空经济/时空智能/出海） |
| 自动驾驶/智能网联合规动态 | 主管部门政策文件 | ✅ web_search（法规/标准/监管动态） |
| 猫笔刀（公众号） | 财经/股市 | ❌ 微信封闭生态 |
| 孟岩的区块链思考（公众号） | 区块链 | ❌ 微信封闭生态 |
| 金岩石（抖音） | 财经观点 | ❌ 抖音封闭生态 |
| 李孔越（抖音） | 财经观点 | ❌ 抖音封闭生态 |

## 主题筛选规则

只保留以下主题的内容，其他一概过滤：

| 主题 | 关键词（用于过滤） |
|------|-------------------|
| **AI** | AI, 人工智能, LLM, GPT, Claude, OpenAI, Anthropic, DeepSeek, 大模型, 机器学习, Agent, 智能体, 推理, RAG, 神经网络, GenAI, 生成式AI, Sam Altman, Dario Amodei |
| **Web3** | Web3, 去中心化, DeFi, NFT, 元宇宙, DAO, 公链, Layer2, 跨链 |
| **区块链** | 区块链, 链上, 智能合约, 矿工, 挖矿, 哈希, 节点, EVM, 共识机制, PoS, PoW |
| **比特币** | 比特币, BTC, 比特币ETF, 比特币现货ETF, GBTC, 减半, 比特币价格, 比特币挖矿, Satoshi, Ordinals, 铭文 |
| **科技（大类）** | 科技, 技术, 创新, 创业, 开源, 代码, 编程, 芯片, GPU, NVIDIA, 半导体, 数据中心, 云计算, 5G/6G, 卫星, 航天, 低空经济, SpaceX, 机器人, 自动驾驶 |
| **融资** | 融资, 投资, 融资轮, 天使轮, A轮, B轮, VC, 风投, 募资, 众筹, 资本, 估值, IPO, 并购, 收购 |
| **金融** | 金融, 银行, 证券, 基金, 债券, 利率, 美联储, 通胀, 货币政策, 监管, 合规, 央行 |
| **股票** | 股票, 股市, 港股, 美股, A股, 大盘, 指数, Nvidia, 特斯拉, 苹果, Microsoft, Google, 财报, 股息, 回购 |

## 工作流

### 每日情报汇总执行流程

1. **拉取所有数据源**
   - aihot API → 过去24h AI精选
   - news-aggregator-skill fetch_news.py → 选关键源
   - Twitter/X → `twitter user-posts @handle --json`（注意：`twitter user` 只返回资料不含推文）
   - Reddit → `rdt search \"AI\" -n 3 --json` 搜索 AI/科技/股票主题
   - 雪球 → Python `XueqiuChannel.get_hot_posts(limit=5)` 获取热帖
   - tencent-news → `tencent-news-cli hot`
   - CoinGecko → curl 公开 API

2. **主题筛选**
   对每条内容，按上述「主题关键词」规则匹配。一条内容可能匹配多个主题。

3. **按主题分组输出，每条内容必带来源链接**
   ```markdown
   🤖 AI · ⛓️ Web3/区块链 · ₿ 比特币 · 🔬 科技 · 💰 融资 · 📊 金融 · 📈 股票
   ```
   **每条新闻的格式规范：**
   ```markdown
   **标题**
   摘要内容...
   🔗 [来源名称](原始链接)
   ```
   - tencent-news 搜出来的每条自带链接，直接保留
   - 泰伯早报源头链接统一为 `https://www.taibo.cn/p/{id}`，每条附注 `（来源：泰伯网）`
   - 喷嚏图卦源头链接统一为喷嚏图卦页面 URL，每条附注 `（来源：喷嚏网）`
   - Twitter/X 推文链接格式 `https://x.com/{screenName}/status/{id}`
   - Reddit 帖子链接格式 `https://reddit.com/r/{subreddit}/comments/{id}`
   - 雪球热帖：使用雪球页面 URL，附注 `（来源：雪球）`

4. **生成日报**，只展示匹配主题的内容，确保**每条都有可点击的来源链接**

### 源状态追踪

每次日报末尾附上所有数据源的状态：
```
✅ 正常 · ⚠️ 待配置 · ❌ 不可用
```

## 工具脚本

### filter_topics.py
本 skill 目录 `scripts/filter_topics.py`
按8大主题关键词过滤新闻JSON，输出分组markdown

### 使用 filter_topics.py
```bash
# 配合 AIHOT API 使用
UA=\"Mozilla/5.0 ...\"
SINCE=$(date -u -d '24 hours ago' +%Y-%m-%dT%H:%M:%SZ)
curl -sH \"User-Agent: $UA\" \\
  \"https://aihot.virxact.com/api/public/items?mode=selected&since=$SINCE&take=50\" \\
  | python3 ~/.hermes/skills/news/daily-intelligence/scripts/filter_topics.py

# 只看统计
python3 ~/.hermes/skills/news/daily-intelligence/scripts/filter_topics.py --format stats
```

## 用户偏好：数据源操作原则

用户对数据源的修改请求（添加/移除/调整）遵循「保留内容，去除冗余」的默认原则：

- **不要整体移除一个数据源**，除非用户明确说「完全删除/永不使用」
- 当用户说「移除/删除一个数据源」时，应**先澄清**：是要完全删除，还是保留内容但要剔除某些部分（结尾评论、总结摘要、作者署名等）
- 再执行删除前，先看能否通过脚本/过滤规则保留内容、仅剔除用户不想要的部分
- 🔥 **历史教训（两次踩坑）**：
  1. **喷嚏图卦** — 用户说「删除喷嚏图卦」，实际是「保留内容，但不要结尾的泰伯评论/总结部分」 → 写 `fetch_dapenti.py` 过滤结尾而非删源
  2. **泰伯早报** — 因为\"泰伯\"出现在喷嚏图卦结尾，误以为用户也要删除泰伯早报整体 → 写 `fetch_taibo.py` 恢复。注意：**\"删除A中的X部分\" ≠ \"删除整个X源\"**
  3. **主题为空的排查**：如果发现融资/金融/股票等板块在日报中出现为空，可考虑：①适当放宽关键词（如增加“融资”、“投资”、“并购”等通用词）；②使用 `source-gathering` skill 进行补充采集；③检查数据源是否有财经类内容（如腾讯财经、雪球等）是否被误过滤。

## 爬取注意事项（踩坑记录）

### CoinGecko 行情
- 公开 API，无需 Key
- `GET https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd&include_24hr_change=true`

### AIHOT
- 所有 API 调用必须带浏览器 UA，否则 403
- 公开 API，无 token 要求
- 限流 600 req/min/IP

### Foresight News
- 网页有反爬限制，优先用 web_search 替代直接抓取

### 雪球 — WAF 保护（重要限制）

雪球全站受**阿里云WAF**保护。即使配置了有效Cookie，直接调用API端点（`v4/statuses/user_timeline.json`）仍返回JavaScript验证挑战。此限制对境外服务器尤为明显。

**可用功能：**
- `XueqiuChannel.get_hot_posts()` — ✅ 热帖获取正常
- web_search 缓存 — ⚠️ 偶尔可用（取决于网络）

**不可用功能：**
- 直接curl API — ❌ WAF阻挡
- RSSHub镜像 — ❌ 同样被阻挡
- 特定用户时间线 — ❌ 无法直接获取

**雪球大V用户追踪方案详见 `references/xueqiu-user-tracking.md`**（13位大V的ID、脚本、cron均已配置）。

### 凤凰FM（小爱晚报）
- 通过 JSONP API 获取，无需 Cookie
- 必须带移动端 UA（Android Chrome）
- 接口文档详见 `references/fenghuang-fm-api.md`
- 返回格式：`j({...})`（注意是 `j` 不是 `BackData`）需去掉回调包装
- **音频转文字**：下载 mp3 → faster-whisper base 模型转写 → 纳入日报\"国内新闻\"板块
- **第二大脑存档**：转写结果保存到 `~/wiki/queries/fenghuang-xiaoi-YYYY-MM-DD.md`
- 已集成到每日情报 cron（每天 18:00 自动执行）
- **独立 Skill 已创建**：`fenghuang-fm`（含一键脚本 `scripts/fenghuang_fm_transcribe.sh`），完整工作流已发布至 GitHub
  - 发布版：https://github.com/aiedwardai/fenghuang-fm-skill
  - Skills 合集：https://github.com/aiedwardai/hermes-skills
- 用户偏好：当用户要求某期小爱晚报\"全文\"时，输出完整转写文字，不做任何总结或压缩
- 相关 skill：`audio-to-text`（通用音频转文字流程）
- ⚠️ **JSONP 解析**：两个接口都返回 JSONP（`j({...})` 或 `BackData({...})`），必须先去掉回调包装再 `json.loads`。直接用 `json.load()` 会报 `JSONDecodeError: Expecting value`

### 自动驾驶/智能网联汽车合规动态（数据源 #11）
- **独立 cron 任务**（非 fenghuang-fm 的一部分），每天自动执行
- **获取方式**：`web_search` 按 **6 个独立关键词** 分别搜索（limit=10）：
  - `\"自动驾驶 合规\"`
  - `\"智能网联 数据安全\"`
  - `\"高精地图 审图\"`
  - `\"车联网 数据安全\"`
  - `\"汽车数据安全管理\"`
- **主管部门聚焦**：自然资源部（地图/测绘/地理信息）、工信部（网络安全/数据安全）、交通运输部（道路运输/车辆安全）、国家网信办、公安部
- **来源筛选标准**（严格按此过滤，仅保留以下 5 类）：
  1. 政策文件发布/修订
  2. 行业标准征求意见/发布
  3. 监管部门的通知/问答/工作会议
  4. 企业合规处罚/整改案例
  5. 图商/地图审图相关动态
- **输出格式**：按主题分类（🔬 科技 / 📊 金融），每条含标题+摘要+🔗 来源链接，末尾附本期重点关注矩阵
- **存档路径**：`~/wiki/queries/automotive-compliance-daily-YYYY-MM-DD.md`（YAML frontmatter + 正文），然后 `git commit/push`
- **背景知识库**：`~/wiki/queries/automotive-compliance-solution.md`
  - 包含完整法规体系（11项核心法规）、合规架构、技术标准、工具链、客户案例
  - 来源：宏图创展 PPT《自动驾驶合规解决方案（通用）》(2025/10/20)
- **完整工作流**：详见 `references/automotive-compliance-daily-workflow.md`

### 主题过滤器（Python伪代码）
```python
TOPICS = {
    \"AI\": [\"ai\", \"人工智能\",\"llm\",\"gpt\",\"claude\",\"openai\",\"anthropic\",\"deepseek\",\"大模型\",\"机器学习\",\"agent\",\"智能体\",\"sam altman\",\"dario amodei\"],\n    \"Web3\": [\"web3\",\"去中心化\",\"defi\",\"nft\",\"元宇宙\",\"dao\",\"公链\",\"layer2\"],\n    \"区块链\": [\"区块链\",\"链上\",\"智能合约\",\"矿工\",\"挖矿\",\"evm\",\"共识\"],\n    \"比特币\": [\"比特币\",\"btc\",\"比特币etf\",\"gbtc\",\"减半\",\"ordinals\",\"铭文\"],\n    \"科技\": [\"科技\",\"芯片\",\"gpu\",\"nvidia\",\"半导体\",\"云计算\",\"卫星\",\"航天\",\"spacex\",\"机器人\",\"自动驾驶\",\"开源\"],\n    \"融资\": [\"融资\",\"投资\",\"vc\",\"风投\",\"估值\",\"ipo\",\"并购\",\"收购\",\"天使轮\"],\n    \"金融\": [\"金融\",\"银行\",\"证券\",\"基金\",\"美联储\",\"通胀\",\"货币政策\",\"监管\"],\n    \"股票\": [\"股票\",\"股市\",\"美股\",\"a股\",\"大盘\",\"指数\",\"财报\",\"回购\"],\n}
\ndef filter_by_topic(items, topics=TOPICS):\n    for item in items:\n        text = (item.get(\"title\",\"\") + \" \" + item.get(\"summary\",\"\") + \" \" + item.get(\"content\",\"\")).lower()\n        matched = [t for t, keywords in topics.items() \n                   if any(kw in text for kw in keywords)]\n        if matched:\n            yield (item, matched)
```

## 公众号推送转换（剑闻）

Cron 日报产出后，可自动转换为微信公众号「剑胆琴新」可用的 HTML 文章。

### 工作流

```
Cron Job 18:00 → 原始日报送达飞书
        ↓
python3 ~/.hermes/scripts/cron_to_jianwen.py
        ↓
/tmp/jianwen-YYYY-MM-DD.html  ← 打开后全选复制，
                                  公众号后台新建图文 → 粘贴 → 设 7:00 定时发布
```

### 标题格式

自动生成：**剑闻 | {热点词1} · {热点词2} · {日期}**

热点词从日报内容中自动提取，取匹配度最高的 1-2 个。**规则顺序即优先级**：时间敏感的重大事件优先，宽泛关键词排在后面。

| 日报内容示例 | 自动标题 |
|-------------|---------|
| 苹果起诉OpenAI + Grok安全事件 | 剑闻 | 苹果起诉OpenAI · Grok安全事件 · 2026-07-13 |
| 英伟达季度营收+GPT-5.6发布 | 剑闻 | GPT-5.6 · 英伟达 · 2026-07-11 |
| 美联储决议 + BTC 暴跌 | 剑闻 | 美联储 · BTC · 2026-07-16 |

**⚠️ 重要规则**：
- 热点词前3条为时间敏感重大事件（苹果起诉、GPT-5.6、Grok安全事件），优先匹配
- \"AI竞赛\"仅在明确竞争语境（超越/对决/军备）时触发，避免因OpenAI+Anthropic日常共现而每天重复出现
- 取匹配的前2个不重复的热点词；如果只有1个匹配，则只用1个

### 转换处理

脚本执行 3 步转换：
1. **萃取正文** — 跳过 cron 输出中的 skill 指令前缀和 agent 思考过程，从 `## Response` 后的真实内容起始（跳过 '数据充足'、'现在汇编' 等 preamble）
2. **删除数据源状态** — 移除末尾的 `## 📊 数据源状态` 章节
3. **HTML 格式化** — 公众号兼容内联样式（红色标题栏 `#c0392b`、链接 `#2980b9` 新标签打开、多级标题、表格列表适配）

### ⚠️ 核心原则：内容忠实

- **不要手动重新编辑日报内容** — 公众号版本必须基于 cron 原始输出自动转换，保持内容与原情报一致
- 历史教训：手动重新拉数据和编辑导致公众号版本与情报原文**内容完全不同**（不同数据切片、不同的选题编辑）
- `cron_to_jianwen.py` 只做**格式转换 + 标题组装 + 数据源状态删除**，不修改任何正文内容

### 脚本位置

**转换脚本：** `~/.hermes/scripts/cron_to_jianwen.py`
**全自动发布脚本：** `~/.hermes/scripts/publish_jianwen.py`

详见 `references/wechat-publishing.md`。

### 自动发布流水线

每天 07:00 cron job `9abc671907ae`（no_agent 模式）自动执行 `publish_jianwen.py`，完成三步：
1. **生成 HTML** — 调用 `cron_to_jianwen.py`，输出 `/tmp/jianwen-YYYY-MM-DD.html`
2. **生成封面图** — Pillow 绘制 900×383 深色封面，带 剑闻 文字 + 热点词 + 日期
3. **推送草稿** — `npm md2wechat sync-html` 将 HTML+封面推送到公众号草稿箱，deliver=\"origin\" 通知用户

```bash
# 手动模拟一次：
source ~/.md2wechat/.env.jdqx && python3 ~/.hermes/scripts/publish_jianwen.py
```

### ⚠️ 自动发布限制

草稿推送成功，但**无法自动发布** — 公众号为个人订阅号，API `freepublish/submit` 返回 `48001 api unauthorized`。用户需手动打开公众号后台 → 草稿箱 → 找到\"剑闻\" → 点击发布/设定时发布。

### 已实现的优化

- ✅ **日报自动存入第二大脑 Wiki** — Cron job 18:00 的 prompt 末尾包含 wiki 存档指令：生成日报后将完整内容（不含数据源状态）保存到 `~/wiki/queries/daily-intelligence-YYYY-MM-DD.md`（YAML frontmatter + 正文），并执行 git commit/push

### Cron 故障恢复

LLM 驱动型 cron job（每日情报、arXiv、SPCX）可能因模型 provider 超时或 `cron_mode: deny` 审批拦截而失败。此时按 `references/cron-manual-fallback.md` 中的并行 delegate_task 流程手动执行：

```text
批次 A: CoinGecko + AIHOT (curl)
批次 B: Tencent News (tencent-news-cli)
批次 C: Twitter/X (web_search)
批次 D: 喷嚏图卦 + 泰伯早报 (fetch_*.py)
```

详见 `references/cron-manual-fallback.md`。

### 未来优化方向
- 增加更多 Twitter/X 关注账号
- 日报自动存入第二大脑 Wikidata

## 重要限制

- ❌ 公众号（猫笔刀、孟岩的区块链思考）：微信封闭生态，无法获取
- ❌ 抖音（金岩石、李孔越）：抖音封闭生态，无法获取
- ⚠️ 国际新闻仅在重大科技/AI事件时关注

## 数据源配置审计

当用户问「还有哪些需要配置/需要Cookie/需要API Key」时，执行以下审计流程，输出完整状态总表：

### 审计步骤

1. **Agent Reach 渠道状态** — `agent-reach doctor` 查看所有渠道的可用性
2. **各 Skill API/Key 需求** — 对 daily-intelligence 集成的每个子 skill，grep 其 SKILL.md 中 api.key/api_key/API_KEY 等关键字。公开 API（CoinGecko、AIHOT）标注为无需 Key
3. **环境变量检查** — `cat ~/.hermes/.env` 查看已配置的 token/key
4. **Agent Reach 可选渠道检查** — `agent-reach install --channels <name> --dry-run` 查看安装方式和代理需求

### 输出格式

按三级分类呈现给用户：

| 状态 | 含义 |
|------|------|
| ✅ 已就绪 | 无需任何配置，直接可用 |
| ⚠️ 可加装 | 可选渠道，知道安装命令和配置需求 |
| ❌ 不可用 | 平台封闭（公众号/抖音）或无此 skill |

### Agent Reach 可选渠道配置需求速查
| references/wechat-publishing.md — 剑闻生成 HTML 并推送公众号的完整工作流 |
| references/ppt-to-markdown-extraction.md — PPT/PPTX 全文提取为 Markdown 的工作流 |
- `references/fenghuang-fm-api.md` — 凤凰FM API 接口文档（小爱晚报节目，pid=456498）
- `references/channel-cookie-setup.md` — 各渠道无浏览器 Cookie 配置脚本

| 渠道 | 安装 | Cookie/Key | 代理 |
|------|------|-----------|------|
| Reddit | `agent-reach install --channels reddit` | 无 | 无需 |
| 雪球 | `agent-reach install --channels xueqiu` | 无 | 无需 |
| 小红书 | `agent-reach install --channels xiaohongshu` | xhs-cookies | 无需 |
| 小宇宙 | `agent-reach install --channels xiaoyuzhou` | 无 | 无需 |
| B站 | `agent-reach install --channels bilibili` | 无 | 需代理 |
| LinkedIn | `agent-reach install --channels linkedin` | 需要登录 | 无需 |