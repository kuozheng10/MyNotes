---
title: Chandra OCR：複雜 PDF 結構保留最強開源解析模型
tags: [OCR, PDF, RAG, 工具, 自動化]
date: 2026-04-27
category: AI工具
---

## 是什麼

datalab-to 出品的開源 OCR 模型，把 PDF / 圖片轉成乾淨的 Markdown / HTML / JSON，完整保留結構。
GitHub: https://github.com/datalab-to/chandra（10k ⭐ / 1.1k forks）
最新版：Chandra 2（2026-03）

## 強在哪

- 表格 → 完整還原（不是爛掉的一行字）
- 數學公式 → 轉 LaTeX
- 手寫 / 草寫 / 舊手稿 → 也能讀
- 核取方塊、表單 → 原封不動重建
- 圖表 + caption → 一起抓
- 支援 90+ 語言

## 跟其他 PDF Parser 比

| 模型 | olmOCR 基準 |
|------|------------|
| Chandra 2 | 85.9%（SOTA） |
| Gemini 2.5 Flash | 60.8% |

90 語言評測：Chandra 2 平均 72.7% vs Gemini 72.7%（Chandra 贏）

## 使用方式

**本地跑（要 GPU）**
```bash
pip install chandra-ocr[torch]
# 需要 NVIDIA H100 80GB，速度約 2 頁/秒
```

**Docker**
```bash
docker pull ghcr.io/datalab-to/chandra-ocr:latest
```

**Managed API（Datalab）**
- 零資料保留（預設）
- SOC 2 Type 2 合規
- 批次處理（每週 2 億頁）
- 適合不想自架 GPU 的場景

## 授權限制

- Code：Apache 2.0（自由）
- Model：Modified OpenRAIL-M
  - ✅ 研究、個人、收入 < $200 萬美元的新創
  - ❌ 不能拿去做跟 Datalab API 競爭的產品

## 對派哥的應用

**最直接的場景：保險存摺 / 台灣人壽 PDF 讀取**
→ 現在掃描保單照片，OCR 結果常常亂掉
→ Chandra 2 可以把表格欄位完整保留，直接餵給 Claude 寫入 Notion

**cc_processor Phase 2**
→ 帳單掃描目前用 Gemini OCR，複雜表格可考慮換 Chandra

**實際限制**：本地跑要 H100，沒有 GPU 就用 Managed API（要付費）

## 與現有工具比較

| 工具 | 適合 | 不適合 |
|------|------|--------|
| Gemini OCR（現在用） | 快速、免費、一般文件 | 複雜表格、手寫 |
| Chandra 2 | 複雜結構、手寫、RAG 前處理 | 沒 GPU 成本高 |
| MarkItDown（微軟） | Office 文件轉 Markdown | PDF 掃描件 |
