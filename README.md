# daily-intelligence-skill

AI 情报引擎 skill 仓库，包含两条独立演进线：

| 分支 | 版本 | 定位 | 结构 |
|---|---|---|---|
| `v3`（当前开发线） | **3.2** | **AI Signal Intelligence** — 采集 + 评分 + 分析 + 决策 | 8 层信息源 → Signal Score 七维加权 → 三维影响分析 → Action Recommendation → Top 5 Action Items / Tomorrow Watchlist |
| `master` | 1.6.0 | 早期聚合器版本 — 46+ 源聚合 | X 68 账号直拉、Reddit、CoinDesk、主题筛选脚本 |

## 用法（v3 分支）

```bash
git clone -b v3 https://github.com/aiedwardai/daily-intelligence-skill
# 复制到 Hermes skill 目录
cp -r SKILL.md references scripts ~/.hermes/skills/news/ai-signal-intelligence/
```

## 差异说明

- `v3.x` 是引擎式设计：每条事件必须经过 Signal Score（0-100，7 维加权）、Confidence、Business/Technical/Market 三维影响、Action Recommendation，未评分不进入日报。
- `v1.x` 是聚合器式设计：以广覆盖采集 + 主题分区为主，不做强制评分。
- 两版结构不兼容，不要混用 prompt。
