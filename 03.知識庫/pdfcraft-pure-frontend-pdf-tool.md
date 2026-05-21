---
title: "PDFCraft — 純前端 WebAssembly PDF 工具箱（零上傳）"
url: "https://github.com/PDFCraftTool/pdfcraft"
tags: [pdf, privacy, webassembly, opensource, security, self-host]
date: 2026-05-10
category: 03.科技工具
source: Telegram 派哥分享
---

## 摘要

> 90+ 種 PDF 工具（合併/分割/轉檔/加密），用 WebAssembly 在瀏覽器內運算，檔案完全不離開本機。免安裝、支援視覺化工作流批次處理、可 Docker 自架。

## 核心差異：為什麼不用 Smallpdf / ilovepdf

傳統線上 PDF 工具 → 上傳到對方伺服器處理 → **檔案被備份風險**

PDFCraft → 所有運算在瀏覽器內（WebAssembly）→ **零上傳，100% 本機**

## 功能

- 90+ 工具：合併、分割、壓縮、轉檔、加密、編輯、浮水印
- 視覺化工作流：把多個動作串接成積木，一鍵批次執行
- 免安裝：開網頁就用
- Docker 自架：企業內網部署

## 適合場景

- 處理合約、財務報表、個資文件時
- 公司有資安政策禁止上傳文件到外部服務
- 需要批次處理大量 PDF（視覺化工作流）

## 對派哥的評估

**有用，但不急。**

cc_processor 處理的信用卡 PDF 已走本地 OCR（不上雲），這個工具不重疊。

有用的場景：
- 手動合併/分割某些文件時，替代 Smallpdf（信用卡帳單、合約等敏感文件）
- 公司層面：給需要處理機密文件的同事用

用法：書籤存網址，需要時打開用，不需要安裝。

## 相關筆記

- [[opendataloader-pdf]] — PDF 解析/RAG
- [[opendataloader-pdf-rag-parser]] — PDF RAG 解析器
