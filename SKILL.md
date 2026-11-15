---
name: ai-signal-intelligence
description: AI信号情报引擎：8层信源采集、7维信号评分、三重影响分析与行动建议，生成可决策日报。
aliases: [daily-intelligence]
version: 3.2
author: Edward Dai
tags: [ai, signal, intelligence, analysis, actionable, trend, research]
related_skills: [aihot, second-brain, source-gathering, arxiv, wordpress-publish]
---

# AI Signal Intelligence v3.2 — 信号情报引擎

> 不是新闻聚合器，而是企业级 AI Signal Intelligence Engine。
>
> 目标：Signal → Insight → Decision → Action

---

## Core Principle

不要输出"今天发生了什么"。
而要输出"今天哪些事情会改变未来"。

每条情报必须经过以下 8 步处理流水线，**任何新闻未经评分，不允许直接进入日报**：

```
Source Collection
      │
      ▼
Deduplication
      │
      ▼
Topic Clustering
      │
      ▼
Cross Verification
      │
      ▼
Signal Scoring
      │
      ▼
Business Impact
      │
      ▼
Action Recommendation
      │
      ▼
Daily Intelligence
```

---

## 八大信息层

### Layer 1: Top People（核心人物追踪）

每日追踪以下 X（Twitter）账号，发现行业趋势、技术方向、未来信号：

```
@elonmusk             — 马斯克（xAI/Tesla/SpaceX）
@sama                 — Sam Altman（OpenAI CEO）
@demishassabis        — Demis Hassabis（Google DeepMind CEO）
@karpathy             — Andrej Karpathy
@ylecun               — Yann LeCun（Meta AI 首席）
@JeffDean             — Jeff Dean（Google DeepMind）
@darioamodei          — Dario Amodei（Anthropic CEO）
@gdb                  — Greg Brockman（OpenAI 联合创始人）
@natfriedman          — Nat Friedman（GitHub 前 CEO）
@eladgil              — Elad Gil（AI 投资人）
@AndrewYNg            — Andrew Ng（DeepLearning.AI）
@emollick             — Ethan Mollick（AI 研究）
```

### Layer 2: AI Labs（AI 实验室追踪）

每日追踪实验室官方账号：

```
@OpenAI            — OpenAI
@AnthropicAI       — Anthropic
@GoogleDeepMind    — Google DeepMind
@xAI               — xAI（马斯克）
@nvidia            — NVIDIA
@deepseek_ai       — DeepSeek
@Alibaba_Qwen      — 阿里通义千问
@MoonshotAI        — 月之暗面
@MiniMax__AI       — MiniMax
@ZhipuAI           — 智谱AI
@MistralAI         — Mistral
@Cohere            — Cohere
```

### Layer 3: Open Source（开源生态追踪）

```
@huggingface      — Hugging Face
@LangChainAI      — LangChain
@llama_index      — LlamaIndex
@ollama           — Ollama
@vllm_project     — vLLM
@modal_labs       — Modal
@replicate        — Replicate
```

### Layer 4: GitHub（GitHub 深度分析）

每日扫描 GitHub Trending，重点分析：AI/LLM/Agent/MCP/Coding Agent/RAG/Workflow/Browser Use/OpenManus/Claude Code/Codex/OpenAI SDK/Anthropic SDK

关注：New Release、Trending Repo、Star 增长最快、Issue 热度、PR 热度、Breaking Project

### Layer 5: Research（学术研究追踪）

每日扫描 arXiv、Papers with Code、Semantic Scholar
关键词：LLM/Agent/Reasoning/Inference/Multimodal/RL/Diffusion/Memory/Evaluation/Tool Use

### Layer 6: Official Blogs（官方博客追踪）

OpenAI Blog / Anthropic Blog / Google DeepMind Blog / Meta AI Blog / Microsoft Research / NVIDIA Blog / AWS AI / Azure AI / Cloudflare Blog

### Layer 7: Policy（政策法规追踪）

美国：White House / NIST / FCC / SEC
欧盟：EU AI Office
中国：国家数据局 / 工信部 / 网信办

### Layer 8: Capital（资本流向追踪）

VC：a16z / Sequoia / Benchmark / Accel / Lightspeed / Y Combinator
投行：ARK Invest / Morgan Stanley / Goldman Sachs

---

## Signal Score 评分体系

### 评分公式

每条事件必须计算 Signal Score（0-100）：

```
Signal Score = Importance × 25%
            + Credibility × 20%
            + Business Impact × 20%
            + Technical Impact × 15%
            + Novelty × 10%
            + Market Impact × 5%
            + Propagation × 5%
```

### Signal Level

| Signal Score | 等级 | 标签 | 含义 |
|:-----------:|:----:|:----:|------|
| 90-100 | ★★★★★ | **S+** | 行业拐点，必须立即阅读 |
| 80-89 | ★★★★★ | **S** | 重大行业事件 |
| 70-79 | ★★★★☆ | **A** | 重点关注 |
| 60-69 | ★★★☆☆ | **B** | 值得了解 |
| 40-59 | ★★☆☆☆ | **C** | 一般信息 |
| 0-39 | ★☆☆☆☆ | Ignore | 日报默认忽略 |

---

## Confidence Score（可信度评分）

每条事件必须计算可信度（0-100）：

| 分数 | 条件 |
|:----:|------|
| 95+ | 官方确认（官方 Blog/Documentation/Release） |
| 80+ | 多个可信来源交叉验证 |
| 60+ | 单一可信来源 |
| 40- | 传闻/未证实 |

**判定依据：**
- 是否来自官方
- 是否来自多个来源
- 是否存在 GitHub 项目
- 是否存在 Blog 文章
- 是否存在论文
- 是否存在 Documentation

---

## Business Impact（业务影响分析）

每条事件必须分析：

**哪些企业受到影响？**
**哪些行业受到影响？**
**哪些岗位受到影响？**

**是否影响：**
企业 AI / Agent / 云计算 / 芯片 / SaaS / 办公 / 金融 / 制造 / 汽车 / 医疗 / 教育

**影响等级：**
Critical / High / Medium / Low / None

---

## Technical Impact（技术影响分析）

分析是否影响以下技术领域（可多选）：

```
LLM / Reasoning / Context / Inference / Memory
Tool Calling / Agent / MCP / Coding / RAG
Browser Use / Multimodal / Evaluation / Fine-tuning
```

---

## Market Impact（市场影响分析）

分析是否影响以下公司/市场（可多选）：

```
GPU / Cloud / OpenAI / Anthropic / Google / Meta
NVIDIA / AMD / TSMC / Microsoft / Amazon / Apple / Tesla
AI 创业公司
```

若影响上市公司，列出公司名称。

---

## Action Recommendation（行动建议）

每条 S/A 级事件必须输出 Action Recommendation：

| 建议 | 含义 |
|:----:|------|
| **Monitor** | 继续观察，无需立即行动 |
| **Research** | 值得深入研究 |
| **Experiment** | 建议团队测试/试用 |
| **Upgrade** | 建议升级现有方案 |
| **Prepare** | 建议提前准备/布局 |
| **Ignore** | 无需投入时间 |

**示例：**
- OpenAI 发布新 API → **Experiment / Upgrade**
- Karpathy 发布 Agent 新框架 → **Research / Experiment**
- White House 发布 AI 法案 → **Prepare / Review Compliance**

---

## Trend Detection（趋势检测）

不仅分析单条新闻，还必须分析最近 7 天 / 30 天 / 90 天是否形成趋势。

**示例：** 如果 OpenAI + Anthropic + Google 都在强化 Reasoning，则输出：
> **Trend：** Reasoning 已进入行业竞争核心。

而不是仅展示三条独立新闻。

---

## Event Correlation（事件关联）

自动关联多源同一事件。如果 Twitter + GitHub + Paper + Blog + Documentation + Release + Funding + Policy 同时讨论同一事件，合并为**一个事件**，不要重复输出。

---

## Actionable Intelligence（可执行情报）

日报不是 Information，而是 Actionable Intelligence。

每天必须输出 **Top 5 Action Items**，例如：
- 建议立即体验某模型
- 建议关注某 GitHub 项目
- 建议阅读某论文
- 建议关注某法规
- 建议准备企业升级

---

## Daily Output（日报格式）

```
# Hermes AI Daily Intelligence
Date: YYYY-MM-DD

---

## Executive Summary
今日核心判断（2-3 句话）

---

## Today's Top 10
1. [S+] 事件标题 — Signal Score
2. [S] 事件标题 — Signal Score
...

---

## S Level
真正改变行业的事件，每条含：
- Signal Score / Confidence Score
- Business Impact / Technical Impact / Market Impact
- Action Recommendation
- 来源链接

---

## A Level
值得重点关注，每条含：
- Signal Score / Action Recommendation
- 来源链接

---

## B Level
行业动态

---

## Trend Analysis
7 天 / 30 天 / 90 天趋势识别

---

## Business Impact
今日哪些企业/行业/岗位受影响最大？

---

## Technical Impact
今日哪些技术领域出现突破或变化？

---

## Market Impact
今日资本市场/上市公司值得关注的变化？

---

## Policy Update
法规/监管动态

---

## Open Source Update
GitHub Trending / 新发布 / 新框架

---

## Research Update
今日论文 / 重要突破

---

## Top GitHub
今日最值得关注的 3 个开源项目

---

## Top Papers
今日最值得阅读的 3 篇论文

---

## Top 5 Action Items
1. [Action] 事项描述
2. [Action] 事项描述
...

---

## Tomorrow Watchlist
预测未来 24 小时 / 72 小时 / 一周最值得关注的事件：
- 明天：
- 本周：
- 提前布局：
```

---

## 工作流

### 每日情报汇总执行流程

**执行时间：** 每天 18:00（cron: `0 18 * * *`）

**Step 1: 并行拉取 8 层数据源**

| 批次 | 层 | 采集方式 | 预估耗时 |
|:----:|:---|---------|:--------:|
| A | Layer 1-2: Top People + AI Labs | web_search 各账号最新推文 | 15s |
| B | Layer 3: Open Source | web_search 各项目动态 | 10s |
| C | Layer 4: GitHub | web_search GitHub Trending (中英文) | 10s |
| D | Layer 5: Research | web_search arXiv + Papers with Code | 10s |
| E | Layer 6: Official Blogs | web_search 定向搜索各博客 | 10s |
| F | Layer 7: Policy | web_search 政策法规关键词 | 10s |
| G | Layer 8: Capital | web_search 融资/IPO 动态 | 8s |
| H | 补充源 | AIHOT API / CoinGecko / 喷嚏图卦 / 泰伯早报 | 15s |

**Step 2: 信号处理流水线**

1. **去重** — 合并多源同一事件
2. **聚类** — 按主题分组
3. **交叉验证** — 跨层验证重大事件 → 计算 Confidence Score
4. **Signal Scoring** — 按 7 维公式计算 Signal Score（0-100）
5. **Business Impact** — 分析影响的企业/行业/岗位
6. **Technical Impact** — 标记受影响的 technical domains
7. **Market Impact** — 标记受影响的公司/市场
8. **Action Recommendation** — 给出行动建议
9. **Trend Detection** — 与近 7/30/90 天数据对比

**Step 3: 生成日报**

按输出格式生成完整日报，每条内容必带来源链接。

**来源链接格式：**
- Twitter/X: `https://x.com/{screenName}/status/{id}`
- GitHub: `https://github.com/{owner}/{repo}`
- arXiv: `https://arxiv.org/abs/{id}`
- Blog: 原始 URL
- 政策: 官方公告 URL

**Step 4: 存档**

将完整日报保存到 `~/wiki/20 queries/intel/daily-intelligence-YYYY-MM-DD.md`（YAML frontmatter + 正文），执行 `git commit/push`。

**Step 5: 交付**

日报全文作为最终响应 deliver 给用户，末尾附上文件路径确认。

---

## 数据源操作原则

- **不要整体移除一个数据源**，除非用户明确说「完全删除/永不使用」
- 当用户说「移除/删除一个数据源」时，应**先澄清**：是要完全删除，还是保留内容但要剔除某些部分
- 🔥 **历史教训：** 喷嚏图卦（删除结尾评论而非删源）、泰伯早报（误删后恢复）

---

## 爬取注意事项

### AIHOT
- 所有 API 调用必须带浏览器 UA，否则 403
- 公开 API，无 token 要求，限流 600 req/min/IP

### CoinGecko
- 公开 API，无需 Key
- `GET https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd&include_24hr_change=true`

### 雪球 — WAF 保护
- 雪球全站受阿里云 WAF 保护，直接 curl API 被阻挡
- 可用功能：`XueqiuChannel.get_hot_posts()` ✅

### 凤凰FM（小爱晚报）
- 通过 JSONP API 获取，需移动端 UA
- 详见独立 skill `fenghuang-fm`

### 公众号/抖音
- ❌ 猫笔刀、孟岩的区块链思考 — 微信封闭生态
- ❌ 金岩石、李孔越 — 抖音封闭生态

---

## 排版规范（md2wechat 秋色 autumn-warm）

日报对外发布统一使用 md2wechat-lite 的 **autumn-warm（秋日暖橙）** AI 排版，这是唯一允许的视觉风格，不再使用红蓝配色。

### 配色表

| 元素 | 色值 |
|---|---|
| 页面底色 | `#FDF6EC` |
| 主卡片底 | `#FFFDF9` |
| 正文 | `#4A413D` |
| 标题 / h2 / 强调 | `#D97758` |
| h3 / 次强调 | `#C06B4D` |
| 分隔线 / 表格边框 | `#EADFD2`（th 底 `#FAF3EA`） |
| 次要文字 | `#A8988A` / `#B9AAA0` |

### 硬性要求

1. **纯内联样式**，禁止 `<style>` 标签（微信公众号会丢弃）
2. 外层必须用 `<section>` 或 `<div>` 主容器包裹（微信丢弃 body 样式）
3. **每个 `<p>` 显式 `color:#4a413d`**（微信会重置 p 颜色）
4. 标题层级：h1 全文一次（`#4A413D`）→ h2 章节（`#D97758`，居中）→ h3 条目（`#C06B4D` + 左侧 `#E8C4A8` 竖线）
5. 表格：th 底 `#FAF3EA`、边框 `#EADFD2`、td 文字 `#4A413D`
6. 封面 900×383 PNG，秋色（底 `#FDF6EC`、主色 `#D97758`、字 `#4A413D`）

### 落地方式

- **WordPress（token2x.com）**：post content 必须直接提交这份秋色 HTML，不能提交裸 markdown 转出的无样式 HTML
- **公众号（剑胆琴新）**：`cron_to_jianwen.py` 的 STYLES 已内置同一套秋色；也可走 md2wechat-lite 的 `draft/add`

### 发布前自检

```bash
grep -c '<style' out.html          # 必须为 0
grep -c 'color:#4a413d' out.html   # 应接近 <p> 数量
grep -c '#d97758' out.html         # 应 > 0
```

---

## 公众号推送转换（剑闻）

详见 `references/wechat-publishing.md`。

### 自动发布流水线

每天 20:30 cron job `9abc671907ae`（no_agent 模式）自动执行 `publish_jianwen.py`：
1. 生成 HTML — 调用 `cron_to_jianwen.py`
2. 生成封面图 — Pillow 绘制 900×383
3. 推送草稿 — `npm md2wechat sync-html` 推送到剑胆琴新
4. WordPress 同步发布到 token2x.com（JianNews 分类）

### 已实现的优化

- ✅ 日报自动存入第二大脑 Wiki：`~/wiki/20 queries/intel/daily-intelligence-YYYY-MM-DD.md`
- ✅ WordPress 自动发布：token2x.com → JianNews 分类
- ✅ 剑胆琴新公众号草稿推送
- ✅ 剑闻格式自动转换：cron_to_jianwen.py → 热点词标题 + 公众号兼容 HTML

---

## Cron 配置

```bash
hermes cron add \
  --name "每日全球AI科技实时追踪" \
  --schedule "0 18 * * *" \
  --skills "ai-signal-intelligence,aihot" \
  --prompt "执行每日 AI Intelligence 情报汇编，使用 ai-signal-intelligence v3.2 skill，按 Signal Score 评分 + 7 维分析 + Action Recommendation 输出日报。" \
  --deliver origin
```

## 历史版本与提示词恢复

用户问「v1.5.1 / v3.0 的提示词或版本」时不要凭记忆拼：

- **当前 cron 提示词**：读 `~/.hermes/cron/jobs.json` 里对应 job 的 `prompt` 字段。
- **历史 cron 提示词**：`~/.hermes/state-snapshots/*/cron/jobs.json`（升级前自动快照，保留当时的原样 prompt；v1.5.1 提示词即由此取得）。
- **历史 skill 全文**：`~/.hermes/skills/.curator_backups/*/skills.tar.gz`（按日期取旧版）+ `references/daily-intelligence-v3.0.md`（v3.0 存档）。
- **GitHub 归档**：`aiedwardai/daily-intelligence-skill`（GitHub 独立演进线 v1.6.0，与本地 v3.x 结构不同）。
- 注意 cron prompt 可能滞后于 skill 版本（prompt 仍写 v3.0、实际加载 v3.1）：回答时区分「提示词文本」与「实际加载的 skill」。

## 更新日志

- v3.2 (2026-11-10): skill 更名为 **ai-signal-intelligence**（原名 daily-intelligence 保留为 alias），明确定位为「采集 + 分析 + 决策」引擎而非日报聚合器。
- v3.1 (2026-07-30): 升级为 Signal Intelligence Engine。新增 Signal Score 0-100 评分公式、Confidence Score、Business/Technical/Market Impact 分析、Action Recommendation、Trend Detection、Event Correlation、Top 5 Action Items、Tomorrow Watchlist。
- v3.0 (2026-07-29): 全面升级为 AI Native Daily Intelligence System。8 层信息源，S/A/B/C 信号评分体系。
- v1.5.1 (2026-07-24): 修复 wiki 写入路径
- v1.0.0 (2026-06-09): 初始版本