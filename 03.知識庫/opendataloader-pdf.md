---
title: "OpenDataLoader PDF - PDF 結構化資料提取"
url: "https://github.com/opendataloader-project/opendataloader-pdf"
tags: [PDF, OCR, Markdown, RAG, 文件處理, Python, Node.js]
date: 2026-03-29
category: 03.科技工具
source: 網路發現
---

## 摘要

> 開源 PDF → 結構化資料工具，輸出 Markdown / JSON / HTML，保留排版、表格、標題層級。Benchmark 第一，表格準確率 0.93。

## 功能

- 正確閱讀順序的文字提取
- 表格偵測（含無框線複雜表格）
- 標題層級 + 清單結構
- 圖片 + 圖表 → AI 自動描述
- 掃描版 PDF → OCR
- LaTeX 公式辨識
- Prompt injection 過濾（防 PDF 隱藏文字攻擊）

## SDK 支援

Python / Node.js / Java

## 適用場景

- PDF 帳單 / 報告 → 結構化資料
- PDF 文章 → Markdown → 存 MyNotes
- 建 RAG / LLM 知識庫

## 與 MyNotes 整合

一般 PDF 文字稿：直接用 Read tool 讀取即可（不需安裝此工具）
複雜 PDF（掃描版、大量表格）：用 OpenDataLoader 前處理再存入
