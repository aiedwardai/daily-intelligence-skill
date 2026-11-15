---
name: daily-intelligence-v3.0
description: AI Native Daily Intelligence System — 覆盖 8 层信息源，S/A/B/C 四级信号评分，旧版 v3.0
version: 3.0
author: Edward Dai
---

# Hermes AI Daily Intelligence v3.0

> 目标不是收集新闻，而是发现真正重要的行业信号。

---

## 输出原则

Daily Intelligence 每天只输出真正值得看的内容。不是"今天发生了 100 条新闻"，而是"今天真正改变 AI 行业的事情"。

**优先级：**
- ✅ 最新
- ✅ 官方
- ✅ 原始来源
- ✅ 高可信度
- ✅ 高影响力

**避免：**
- ❌ 重复转载
- ❌ 媒体二次解读
- ❌ 营销文章
- ❌ 低价值新闻

---

## 信号评分体系（Signal Priority）

所有信息按影响力评分：

| 等级 | 标签 | 含义 | 示例 |
|:----:|:----:|------|------|
| ★★★★★ | **S** | 改变行业方向 | OpenAI/Anthropic/Google 新模型、DeepSeek、重大融资、重大政策 |
| ★★★★ | **A** | 值得所有 AI 从业者关注 | Agent Framework、重要论文、GitHub Trending、API 更新 |
| ★★★ | **B** | 行业动态 | 产品升级、版本更新、企业合作 |
| ★★ | **C** | 普通新闻 | — |
| ★ | **忽略** | 低价值 | — |

**Daily Brief 默认仅输出 S/A/B 三级内容。**

---

## 八大信息层

### Layer 1: Top People（核心人物追踪）

每日追踪以下 X（Twitter）账号，发现行业趋势、技术方向、未来信号：

```
@elonmusk            — 马斯克（xAI/Tesla/SpaceX）
@sama                — Sam Altman（OpenAI CEO）
@demishassabis       — Demis Hassabis（Google DeepMind CEO）
@karpathy            — Andrej Karpathy
@ylecun              — Yann LeCun（Meta AI 首席）
@JeffDean            — Jeff Dean（Google DeepMind）
@darioamodei         — Dario Amodei（Anthropic CEO）
@gdb                 — Greg Brockman（OpenAI 联合创始人）
@natfriedman         — Nat Friedman（GitHub 前 CEO）
@eladgil             — Elad Gil（AI 投资人）
@AndrewYNg           — Andrew Ng（DeepLearning.AI）
@emollick            — Ethan Mollick（AI 研究）
```

### Layer 2: AI Labs（AI 实验室追踪）

每日追踪实验室官方账号，重点关注：模型发布、API 更新、Benchmark、Pricing、Context Window、Agent、Reasoning、Coding、Multimodal：

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

每日追踪开源项目动态，重点关注：Agent、Framework、Inference、MCP、RAG、Tool Calling、Workflow：

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

每日扫描 GitHub Trending，重点分析以下方向：

- AI / LLM / Agent / MCP / Coding Agent
- RAG / Workflow / Browser Use
- OpenManus / Claude Code / Codex
- OpenAI SDK / Anthropic SDK

**关注指标：** New Release、Trending Repo、Star 增长最快、Issue 热度、PR 热度、Breaking Project

**采集方式：**
```
web_search "GitHub trending AI open source project today"
web_search "GitHub 热门开源项目 2026"
web_search "GitHub trending agent MCP framework"
```

### Layer 5: Research（学术研究追踪）

每日扫描 arXiv、Papers with Code、Semantic Scholar，关键词：

```
LLM / Agent / Reasoning / Inference / Multimodal
RL / Diffusion / Memory / Evaluation / Tool Use
```

**关注指标：** 论文质量、GitHub 配套、Twitter 热度、引用增长、商业价值

### Layer 6: Official Blogs（官方博客追踪）

每日扫描以下官方博客，重点关注：官方发布、Roadmap、Documentation、Research、API：

```
OpenAI Blog        — https://openai.com/blog
Anthropic Blog     — https://anthropic.com/blog
Google DeepMind    — https://deepmind.google/blog
Meta AI Blog       — https://ai.meta.com/blog
Microsoft Research — https://www.microsoft.com/en-us/research
NVIDIA Blog        — https://blogs.nvidia.com
AWS AI             — https://aws.amazon.com/blogs/machine-learning
Azure AI           — https://azure.microsoft.com/en-us/blog
Cloudflare Blog    — https://blog.cloudflare.com
```

### Layer 7: Policy（政策法规追踪）

每日扫描以下监管机构，重点关注：AI Regulation、AI Safety、Data Security、Model Governance、Export Control、GPU：

**美国：** White House / NIST / FCC / SEC
**欧盟：** EU AI Office
**中国：** 国家数据局 / 工信部 / 网信办

### Layer 8: Capital（资本流向追踪）

每日扫描以下投资机构，重点关注：融资、IPO、AI 投资、AI 并购、独角兽、行业趋势：

**VC：** a16z / Sequoia / Benchmark / Accel / Lightspeed / Y Combinator
**投行/研究：** ARK Invest / Morgan Stanley / Goldman Sachs

---

## 信号融合（Signal Fusion）

不要简单罗列新闻。必须进行：

1. **去重** — 同一事件多个来源只保留一个
2. **聚类** — 相关事件分组整合
3. **交叉验证** — 同一事件在 Twitter + GitHub + Blog + Paper 同时出现 → 判定为重大行业事件
4. **可信度评估** — 优先官方/原始来源
5. **影响力评分** — 按 S/A/B/C 分级

---

## 日报输出格式

```
# Hermes AI Daily Intelligence
日期：YYYY-MM-DD

---

## Today Top 10
今天最重要的十件事。

---

## S Level
真正改变行业的事件。

---

## A Level
值得重点关注。

---

## B Level
行业动态。

---

## AI Labs
OpenAI / Anthropic / Google / DeepSeek / xAI / Qwen ...

---

## Open Source
GitHub Trending / New Release / New Framework

---

## Research
今日论文 / 重要突破

---

## Capital
融资 / IPO / VC

---

## Policy
法规 / 监管 / 出口限制 / AI 法案

---

## Trend Summary
总结：今天 AI 行业真正发生了什么？
哪些趋势正在形成？
未来一周值得重点关注什么？
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

**Step 2: 信号处理**

1. 去重 — 合并多源同一事件
2. 聚类 — 按主题分组
3. 交叉验证 — 跨层验证重大事件
4. 影响力评分 — 标注 S/A/B/C

**Step 3: 生成日报**

按输出格式生成完整日报，每条内容必带来源链接。

**格式规范：**
```markdown
**[S/A/B] 标题**
摘要内容（含关键数据/判断）
🔗 [来源名称](原始链接)
```

**来源链接格式：**
- Twitter/X: `https://x.com/{screenName}/status/{id}`
- GitHub: `https://github.com/{owner}/{repo}`
- arXiv: `https://arxiv.org/abs/{id}`
- Blog: 原始 URL
- 政策: 官方公告 URL

**Step 4: 存档**

将完整日报（不含数据源状态）保存到 `~/wiki/20 queries/intel/daily-intelligence-YYYY-MM-DD.md`（YAML frontmatter + 正文），执行 `git commit/push`。

**Step 5: 交付**

日报全文作为最终响应 deliver 给用户，末尾附上文件路径确认。