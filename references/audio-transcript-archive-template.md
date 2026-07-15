# 音频转文字存档模板（第二大脑）

## 用途
适用于音频新闻节目（如凤凰FM小爱晚报）转写后的存档到第二大脑 Wiki。

## 模板格式
```markdown
---
date: YYYY-MM-DD
title: {节目名} {日期}
tags: [{节目标签}, news, audio-transcript]
source: {来源标识}
audio_url: {音频直链URL}
transscribed: YYYY-MM-DD
---

# 📻 {节目名} | {日期}

> 节目：{节目名}（pid={pid}）
> 时长：X分X秒
> 出品：{出品方}
> 转写：faster-whisper (base)

---

## 头条要闻

**{标题1}**
{摘要}

## {板块2}

...

---

## 完整转写文本

{原始转写全文，分段保留}
```

## 字段说明
- `transcribed`: 转写完成日期（非节目播出日期）
- `audio_url`: /mp3 直链，方便回听
- 板块按节目实际结构分组（头条、财经、体育、社会、生活贴士等）
- **完整转写文本**必须保留在存档中，不可省略

## 注意事项
- 存档路径：`~/wiki/queries/{slug}-{YYYY-MM-DD}.md`
- 存档后必须 `git add` + `git commit` + `git push`
- 结构化摘要用于快速浏览，完整全文用于深度检索
