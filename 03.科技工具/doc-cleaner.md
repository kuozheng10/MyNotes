---
title: doc-cleaner v1.2.0 — 文件轉乾淨 Markdown 工具
tags: [工具, 知識管理, LLM, Python, 隱私, 自動化]
date: 2026-04-09
category: 知識管理
source: https://github.com/notoriouslab/doc-cleaner
---

## 這是什麼

輕量 Python 工具，把各種文件格式轉成乾淨、結構化的 Markdown。全程離線可跑，適合隱私優先場景。特別針對繁體中文財務文件優化（Big5/CP950/UTF-16 自動偵測）。

---

## 支援格式

PDF（原生文字 + 掃描圖片）、DOCX、XLSX、CSV、PPTX、DXF、純文字

---

## 核心功能

| 功能 | 說明 |
|------|------|
| 智慧 PDF 分類 | 自動偵測原生 / 損壞 / 掃描，分別處理 |
| 格式保留 | DOCX/XLSX 表格轉 Markdown pipe table，不丟資料 |
| 多語言編碼 | Big5、CP950、UTF-16 自動識別 |
| 雜訊清除 | 廣告、頁首頁尾用 regex 過濾 |
| 彈性 AI 後端 | Gemini / Groq / Ollama，或 `--ai none` 完全離線 |
| 隱私優先 | 所有運算本機完成 |

---

## 快速啟動

```bash
# 安裝
git clone https://github.com/notoriouslab/doc-cleaner
pip install -r requirements.txt

# 基本用法（輸出至 ./output/）
python cleaner.py --input document.pdf

# 完全離線
python cleaner.py --input document.pdf --ai none

# 預覽不實際執行
python cleaner.py --input document.pdf --dry-run
```

---

## 對派哥的啟示

- **配合 Vault Search 效果最好**：doc-cleaner 先清乾淨格式，Vault Search 再建語意索引——兩者是前後端搭配
- **cc_processor / 財務文件**：HSBC、國泰 PDF 帳單可以先跑 doc-cleaner 轉 Markdown，再餵 LLM 分析
- **MyNotes 原始素材**：剪貼文章/報告前先跑一遍，省去手動清格式的時間
- **opendataloader-pdf 整合**：需要 Java 11+，適合複雜 PDF；一般 PDF 不需要額外安裝

---

## 連結筆記
- [[vault-search-obsidian-plugin]] — doc-cleaner 是前處理層，Vault Search 是查詢層
- [[llm-knowledge-base-karpathy]] — raw/ 原始素材清洗後入庫的最佳前置工具
- [[opendataloader-pdf]] — PDF 解析進階後端選項
