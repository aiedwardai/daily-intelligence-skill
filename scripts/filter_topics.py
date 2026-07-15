#!/usr/bin/env python3
"""
每日情报主题过滤器。
从 stdin 接收 JSON 格式的 items，按主题关键词过滤并输出分组结果。

用法：
  curl -s ...items | python3 filter_topics.py
  cat items.json | python3 filter_topics.py --format grouped

输入格式（每行一个JSON或整体JSON数组）：
  {"items": [{"title": "...", "summary": "...", "source": "...", "publishedAt": "..."}]}

输出格式（--format grouped）：
  按主题分组的 markdown 列表
"""
import sys, json, datetime, re

TOPICS = {
    "AI": ["ai","人工智能","llm","gpt","claude","openai","anthropic","deepseek",
           "大模型","机器学习","agent","智能体","sam altman","dario amodei",
           "推理","rag","神经网络","genai","生成式"],
    "WEB3": ["web3","去中心化","defi","nft","元宇宙","dao","公链","layer2","跨链"],
    "BLOCKCHAIN": ["区块链","链上","智能合约","矿工","挖矿","evm","共识机制"],
    "BTC": ["比特币","btc","比特币etf","gbtc","减半","ordinals","铭文"],
    "TECH": ["科技","芯片","gpu","nvidia","半导体","数据中心","云计算",
             "卫星","航天","spacex","机器人","自动驾驶","开源","5g"],
    "FINANCE": ["融资","投资","vc","风投","估值","ipo","并购","收购",
                "金融","银行","股票","股市","美股","大盘","指数","财报",
                "天使轮","a轮","b轮","募资","回购"],
}

CAT_LABELS = {
    "AI": "🤖 AI",
    "WEB3": "⛓️ Web3",
    "BLOCKCHAIN": "⛓️ 区块链",
    "BTC": "₿ 比特币",
    "TECH": "🔬 科技",
    "FINANCE": "💰 融资·金融·股票",
}

CAT_ORDER = ["AI", "WEB3", "BLOCKCHAIN", "BTC", "TECH", "FINANCE"]

def time_to_str(pub):
    """Convert ISO UTC to Beijing relative time"""
    if not pub:
        return ""
    dt = datetime.datetime.fromisoformat(pub.replace("Z", "+00:00"))
    bj = dt + datetime.timedelta(hours=8)
    now_bj = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=8)
    diff = (now_bj - bj).total_seconds()
    if diff < 60:
        return "刚刚"
    elif diff < 3600:
        return f"{int(diff//60)}分钟前"
    elif diff < 86400:
        return f"{int(diff//3600)}小时前"
    else:
        return bj.strftime("%m/%d %H:%M")

def filter_items(items):
    """Filter items by topic keywords, return dict of {category: [items]}"""
    result = {cat: [] for cat in TOPICS}
    for item in items:
        text = (item.get("title", "") + " " + item.get("summary", "")).lower()
        matched = False
        for cat, keywords in TOPICS.items():
            if any(kw in text for kw in keywords):
                result[cat].append(item)
                matched = True
                break
    return result

def format_grouped(filtered):
    """Output markdown grouped by category"""
    parts = []
    for cat in CAT_ORDER:
        items = filtered.get(cat, [])
        if not items:
            continue
        parts.append(f"## {CAT_LABELS.get(cat, cat)} ({len(items)}条)")
        for i, item in enumerate(items, 1):
            title = item.get("title", "")
            source = item.get("source", "")
            pub = time_to_str(item.get("publishedAt", ""))
            summary = item.get("summary", "")
            url = item.get("url", "")
            line = f"{i}. **{title}**"
            if source:
                line += f" — {source}"
            if pub:
                line += f"（{pub}）"
            if summary:
                short = summary[:80] + "..." if len(summary) > 80 else summary
                line += f"\n   {short}"
            if url:
                line += f"\n   <{url}>"
            parts.append(line)
        parts.append("")
    return "\n".join(parts)

if __name__ == "__main__":
    data = json.load(sys.stdin)
    items = data.get("items", data if isinstance(data, list) else [])
    filtered = filter_items(items)
    
    fmt = "--format" in sys.argv and sys.argv[sys.argv.index("--format") + 1] or "grouped"
    
    if fmt == "json":
        print(json.dumps(filtered, ensure_ascii=False, indent=2))
    elif fmt == "stats":
        for cat in CAT_ORDER:
            n = len(filtered.get(cat, []))
            if n > 0:
                print(f"{CAT_LABELS.get(cat, cat)}: {n}条")
        print(f"\n总计匹配: {sum(len(v) for v in filtered.values())}/{len(items)} 条")
    else:
        print(format_grouped(filtered))