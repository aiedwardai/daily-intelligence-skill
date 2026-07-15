# PPT → Markdown 提取工作流

## 场景
用户上传 .pptx 文件，需要提取全文为可编辑的 Markdown 格式。

## 工具依赖
- `unzip`（sudo apt-get install -y unzip）
- Python 3 + xml.etree.ElementTree

## 步骤

### 1. 解压 PPTX
```bash
mkdir -p /tmp/pptx-extract && cd /tmp/pptx-extract
unzip -o "/path/to/file.pptx" > /dev/null 2>&1
# 幻灯片在 ppt/slides/slide*.xml
```

### 2. 提取文本
```python
import xml.etree.ElementTree as ET
import os, re

slides_dir = 'ppt/slides'
slide_files = sorted(
    [f for f in os.listdir(slides_dir) if f.startswith('slide') and f.endswith('.xml')],
    key=lambda x: int(re.search(r'slide(\d+)', x).group(1))
)

all_text = []
for sf in slide_files:
    tree = ET.parse(os.path.join(slides_dir, sf))
    root = tree.getroot()
    slide_num = re.search(r'slide(\d+)', sf).group(1)
    texts = []
    for t in root.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}t'):
        if t.text:
            texts.append(t.text)
    slide_text = ''.join(texts).strip()
    if slide_text:
        all_text.append(f"## 第{slide_num}页\n{slide_text}\n")
```

### 3. 结构化排版
- 按内容逻辑分 Part/Section
- 表格数据转为 Markdown 表格
- 保留原始层级关系
- 添加 YAML frontmatter

### 4. 注意事项
- 大文件（>50MB / >100页）需分批读取，不要一次性 print 所有文本
- 写入 wiki 时用分段 patch 而非单次大 write_file（避免 stream timeout）
- PPT 中图片/图表无法提取，标注 [图片] 占位
- 如果 stream timeout，用 patch mode=replace 分段追加
