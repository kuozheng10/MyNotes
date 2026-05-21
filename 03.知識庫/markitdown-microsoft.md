---
title: MarkItDown — Microsoft 出品，把任何文件轉成 Markdown 餵給 LLM
tags: [工具, Python, Markdown, LLM, 文件處理, OCR, MCP, RAG]
date: 2026-04-12
category: AI工具
source: https://github.com/microsoft/markitdown
---

## 這是什麼

Microsoft 開源的 Python 工具，把各種格式文件轉成 Markdown，專為餵給 LLM 設計。
核心哲學：LLM 是在大量 Markdown 上訓練的，Markdown 就是 LLM 最懂的語言。

---

## 支援格式

| 類型 | 格式 |
|------|------|
| Office | DOCX、XLSX/XLS、PPTX |
| PDF | 普通 PDF；進階用 Azure Document Intelligence |
| 圖片 | EXIF metadata + OCR（可用 LLM vision） |
| 音訊 | 自動語音轉文字 |
| 網頁 | HTML、CSV、JSON、XML |
| 其他 | ZIP、EPUB、YouTube URL（影片轉錄） |

---

## 安裝與使用

```bash
# 全部格式
pip install 'markitdown[all]'

# 只裝需要的
pip install 'markitdown[pdf,docx,pptx]'
```

### CLI

```bash
markitdown path/to/file.pdf > output.md
markitdown file.pdf -o output.md
cat file.pdf | markitdown
```

### Python API

```python
from markitdown import MarkItDown

# 基本轉換
md = MarkItDown()
result = md.convert("report.xlsx")
print(result.text_content)

# 圖片用 GPT-4V 描述
from openai import OpenAI
md = MarkItDown(llm_client=OpenAI(), llm_model="gpt-4o")
result = md.convert("screenshot.jpg")
```

---

## 整合方式

- **MCP Server**：`markitdown-mcp` 套件，可接入 Claude Desktop 或任何 MCP agent
- **Azure Document Intelligence**：企業級 PDF 處理
- **Plugin 系統**：可擴充，GitHub hashtag `#markitdown-plugin` 找社群 plugins
  - 例：`markitdown-ocr` — 用 LLM Vision 對 PDF/DOCX/PPTX 做 OCR，不需額外 ML 套件

---

## 評估：對派哥有沒有用？

**高度有用，建議現在就裝**

直接用途：

1. **sales_report_processor**：Hasna 寄來的 PDF/DOCX 附件，可先用 markitdown 轉 MD 再處理
2. **cc_processor**：帳單 PDF 轉 Markdown → 餵給 Claude 解析，比直接 OCR 更穩定
3. **My Wallet Trip**：發票/收據 PDF → Markdown → Notion 寫入
4. **MCP 整合**：裝 `markitdown-mcp`，在 Claude Code 裡直接呼叫轉換，不需另開 terminal

快速驗證：

```bash
pip install 'markitdown[all]'
markitdown ~/Documents/test.pdf
```

**不需要包成 skill**，直接用 CLI 或 Python API 即可。
