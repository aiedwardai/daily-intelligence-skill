# 公众号推送转换（剑闻）—— 详细参考

## 架构

```
 ┌─────────────────────────────────────────────┐
 │ Cron Job cd4758415298                        │
 │ 每日 18:00 CST                               │
 │ 9数据源 → 每日智能情报筛选                    │
 └──────────────┬──────────────────────────────┘
                │ 输出完整对话（skill指令 + 正文）
                ▼
 ┌─────────────────────────────────────────────┐
 │ Cron Output File                             │
 │ ~/.hermes/cron/output/cd4758415298/          │
 │     YYYY-MM-DD_hh-mm-ss.md                   │
 │ 结构: ## Prompt → 200+行skill全文 →          │
 │       ## Response → report                   │
 └──────────────┬──────────────────────────────┘
                │ cron_to_jianwen.py
                ▼
 ┌─────────────────────────────────────────────┐
 │ Jianwen HTML                                 │
 │ /tmp/jianwen-YYYY-MM-DD.html                 │
 │ 公众号兼容格式，inline styles                │
 │ 标题: 剑闻 | 热点 · 日期                     │
 └──────────────┬──────────────────────────────┘
                │ 手动：打开 → 全选复制 → 粘贴到
                │ 或 # 自动推送到公众号草稿箱
                ▼
 ┌─────────────────────────────────────────────┐
 │ 公众号「剑胆琴新」后台                        │
 │ 新建图文 → 粘贴HTML → 定时 7:00 发布         │
 └─────────────────────────────────────────────┘
```

### 自动化推送（无需手动粘贴）

使用 `publish_jianwen.py` 脚本一键完成全部三步：生成 HTML → 生成封面图 → 推送草稿。

#### 全自动发布脚本

**位置：** `~/.hermes/scripts/publish_jianwen.py`

**手动运行：**
```bash
source ~/.md2wechat/.env.jdqx && python3 ~/.hermes/scripts/publish_jianwen.py
```

**脚本包含三步：**
1. **Step 1** — 调用 `cron_to_jianwen.py`，读取最新 cron 输出，生成公众号 HTML
2. **Step 2** — 从 HTML 解析标题和日期，用 Pillow 绘制封面图（900×383，深色背景 `#1a1a2e`，文泉驿正黑字体）
3. **Step 3** — 用 npm md2wechat CLI 的 `sync-html` 推送草稿到公众号

**成功输出：**
```
Step 1: Running cron_to_jianwen.py...
HTML ready: /tmp/jianwen-2026-06-15.html
Title: 剑闻 | 热点 · 日期
Cover saved: /tmp/jianwen-cover-2026-06-15.png
Step 4: Pushing draft to WeChat...
✅ DRAFT CREATED SUCCESSFULLY
```

#### ⚠️ 自动发布限制（适用所有账号类型）

草稿推送成功，但**无法自动发布**。微信公众号 API `cgi-bin/freepublish/submit` 对非认证订阅号返回 `48001 api unauthorized`。

**手动发布步骤（每天早上必做）：**
1. 打开 [mp.weixin.qq.com](https://mp.weixin.qq.com)
2. 左侧 → 草稿箱
3. 找到标题为「剑闻 | ...」的文章
4. 点击「发布」或「定时发布」→ 设 7:00 或立即发布

#### 封面图生成（Pillow 自动）

脚本内置封面生成逻辑，无需手动执行。如果需要单独生成封面：

```python
from PIL import Image, ImageDraw, ImageFont
W, H = 900, 383
img = Image.new('RGB', (W, H), '#1a1a2e')
draw = ImageDraw.Draw(img)
font_large = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc', 88)
font_small = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc', 28)
# ... 绘制 剑闻 大标题 + 热点子标题 + 日期 ...
img.save('/tmp/jianwen-cover.png')
```

CJK 字体路径：`/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc`（文泉驿正黑）

#### 凭证获取模式

`publish_jianwen.py` 使用 bash subprocess 模式获取凭证，而非 Python 正则解析：

```python
# ✅ 正确做法 — bash source 自动解析变量引用
bash_cmd = f"source {ENV_FILE} && echo WECHAT_APP_ID=$WECHAT_APP_ID && echo WECHAT_APP_SECRET=$WECHAT_APP_SECRET"
result = subprocess.run(['bash', '-c', bash_cmd], capture_output=True, text=True)
# 解析 stdout 中的 VAR=VALUE 行

# ❌ 错误做法 — Python regex 无法解析 $VAR 引用
# with open(env_file) as f:
#     for line in f:
#         m = re.match(r'export (\w+)=["\']?(.*?)["\']?', line)  # 失败！
```

`.env.jdqx` 中的 `WECHAT_APP_ID="$WECHAT_APPID_JDQX"` 是 bash 变量引用，Python 直接读取得到的是字面字符串 `$WECHAT_APPID_JDQX` 而非其值。

#### cron 自动运行

每天 07:00 cron job `9abc671907ae`（name="剑闻自动发布"）自动运行 `publish_jianwen.py`。
- 模式：`no_agent=True`（直接执行脚本，不经过 LLM）
- 交付：`deliver="origin"`（执行结果发送到飞书）
- 输出：用户早上收到「✅ DRAFT CREATED SUCCESSFULLY」通知

```bash
# 当前 cron 配置（通过 Hermes CLI 查看）
hermes cron list
# → 剑闻自动发布 | 0 7 * * * | publish_jianwen.py | no_agent | enabled
```

## 脚本细节

### cron_to_jianwen.py

**位置:** `~/.hermes/scripts/cron_to_jianwen.py`

**执行:** `python3 ~/.hermes/scripts/cron_to_jianwen.py`
（不传参，自动找最新 cron 输出）

**输出路径:** `/tmp/jianwen-YYYY-MM-DD.html`

### 提取报告体

cron 输出文件结构复杂，脚本按以下步骤萃取真实报告：

1. 定位 `## Response` 标记 — 之后的内容是 agent 的输出
2. 跳过 preamble（"数据充足，现在汇编..." 等思考过程文本）
3. 第一个真实内容标记（`---`、`##`、`#`、`📡`、`**标题**`）开始作为报告起点
4. 遇到 `## 📊 数据源状态` 或 `## 数据源` 标记后全部删除

### 标题自动生成

**规则:** `剑闻 | {热点词1} · {热点词2} · {日期}`

**热点词优先级（源码 HOT_TOPIC_SIGNALS 数组，按权重降序排列）:**

| 优先级 | 识别模式 | 输出标签 |
|--------|---------|---------|
| 1 | `\bSpaceX\b` | SpaceX IPO |
| 2 | `马斯克.*万亿` / `万亿.*马斯克` | 万亿马斯克 |
| 3 | `美联储.*降息` / `fed.*rate` | 美联储 |
| 4 | `黄金.*[跌涨]` / `金价.*[跌涨]` | 黄金 |
| 5 | `比特币.*[跌涨]` / `BTC.*price` | BTC |
| 6 | `\bGPT-5\b` / `\bGPT5\b` | GPT-5 |
| 7 | `Anthropic.*IPO` / `Anthropic.*估值` | Anthropic |
| 8 | `DeepSeek.*[Rr]2` | DeepSeek |
| 9 | `\bDiffusionGemma\b` / `\bGemma\b` | Google Gemma |
| 10 | `Midjourney\s+V?\d` | Midjourney |
| 11 | `NVIDIA.*Next` / `GB\d+` | NVIDIA |
| 12 | `华为.*芯片` / `华为.*AI` | 华为 |
| 13 | `BTC.*ETF.*[流资]` | BTC ETF |

取匹配度最高的前 1-2 个。如果没有任何高优先级匹配，fallback 到章节标题 emoji（₿=AI, 🤖=AI, 🔬=科技, 💰=融资, 📈=金融等）。

日期从 cron 输出内容中的 `YYYY-MM-DD` 模式提取，fallback 到文件名中的日期或执行日期。

### HTML 样式

微信公众号编辑器对 HTML 支持有限，所有样式均用内联 style：

| 元素 | 样式 |
|------|------|
| 整体 | 680px max-width, 白色背景, 10px阴影 |
| 文章标题 `<h1>` | 26px, 红色 `#c0392b`, 字间距 2px |
| 日期行 | 13px, 灰色 `#999` |
| 节标题 `<h2>` | 20px, 深灰 `#2c3e50`, 居中 |
| 子标题 `<h3>` | 17px, 红色 `#c0392b`, 左边框 4px `#c0392b` |
| cron内标题 `<h4>` | 15px, 灰色 `#555`, 居中（保留 cron 内部标题但不突出） |
| 正文 `<p>` | 16px, 行高 1.8 |
| 链接 `<a>` | 蓝色 `#2980b9`, `target="_blank"` |
| 表格 | 1px 边框 `#ddd`, 表头灰色背景 |
| 分割线 | 1px 灰色实线, 上下 20px |
| 页脚 | 11px, 浅灰 `#bbb` |

### 内容处理规则

| 输入元素 | 输出 |
|----------|------|
| `---` | 分割线 `<section>` |
| `## 标题` | `<h2>` (章节标题) |
| `### 标题` | `<h3>` (子标题，左边框) |
| `# 标题` | `<h4>` (cron 内部标题，小字) |
| `**加粗**` | `<strong>` |
| `[文字](url)` | `<a href="url" target="_blank">` |
| `| col1 \| col2 \|` | `<table>` (首行自动为 `<th>`) |
| `- 列表项` | `<ul><li>` |
| **数据源状态章节** | **已删除** |

### 关键注意事项

1. **不要重新拉数据** — 永远基于 cron 原始输出，不要再调 API/search 重新获取
2. **不要改正文** — 只做格式转换 + 标题 + 删除数据源状态
3. **不要加个人评论** — 保留原文的语气和事实性
4. 如果当天 cron 输出中没有内容（空日报），脚本输出的 HTML 也会是空的——这是正确的，不要自行填充内容