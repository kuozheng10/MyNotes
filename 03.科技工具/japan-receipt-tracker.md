---
title: "japan-receipt-tracker-stack"
url: "https://github.com/chasehuang/japan-receipt-tracker-stack"
tags: [AI, OCR, 記帳, Next.js, Notion, 旅遊, app]
date: 2026-03-29
category: 03.科技工具
source: GitHub
---

## 摘要

> 日本旅行 AI 收據記帳 app：拍收據 → Gemini OCR 辨識翻譯 → Notion 資料庫 → 儀表板統計，月費 $5。

## 內容

開發者一個月日本旅行全程使用，開源可直接參考架構。

## 重點摘錄

- **AI OCR**：Google Gemini 2.0 Flash，一個 API call 搞定辨識、翻譯、分類
- **資料庫**：Notion API（免費、有 GUI、可手動編輯）
- **前端**：Next.js 16 + TypeScript + Tailwind CSS v4
- **部署**：Zeabur，zero-config，月費 $5
- **功能**：今日花費、累計金額、每日趨勢、類別佔比、支付方式分布、前十大消費
- **地區自動判定**：根據旅程日程自動歸類
- **多人記帳**：支援多旅伴各自記帳

## 個人想法

這個架構可以參考來做自己的 app：拍照 + AI 辨識 + 資料庫 + 分析表，核心技術已驗證可行。

## 相關連結

- https://github.com/chasehuang/japan-receipt-tracker-stack
