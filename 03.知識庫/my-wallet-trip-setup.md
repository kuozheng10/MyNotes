---
title: "My Wallet Trip - 完整設定記錄"
url: "https://github.com/kuozheng10/My-Wallet-Trip"
tags: [app, Next.js, PWA, Notion, Vercel, Gemini, 記帳]
date: 2026-03-29
category: 03.科技工具
source: 自建
---

## 摘要

> 個人旅遊 + 日常記帳 PWA，AI OCR 拍收據，Notion 存資料，Vercel 部署。

## 架構

| 層級 | 技術 |
|------|------|
| 前端 | Next.js 16 + TypeScript + Tailwind CSS |
| AI OCR | Google Gemini 2.0 Flash |
| 資料庫 | Notion API |
| 圖表 | Recharts |
| 部署 | Vercel（auto-deploy from GitHub main） |
| 手機安裝 | PWA（Safari → 加入主畫面） |

## 連結

- App：https://my-wallet-trip.vercel.app
- GitHub：https://github.com/kuozheng10/My-Wallet-Trip
- Notion DB：https://notion.so/332849e1230180068e15d8d2e33e8f2f

## 環境變數

| Key | 說明 | 存放位置 |
|-----|------|----------|
| NOTION_TOKEN | Notion Integration Secret | ~/.claude/notion-token |
| NOTION_TRIPS_DB_ID | 332849e1230181d4861ac3499141d9ce | Vercel env |
| NOTION_EXPENSES_DB_ID | 332849e1230181368e61f3c47a530b35 | Vercel env |
| GEMINI_API_KEY | Google AI Studio key | ~/.zshrc GOOGLE_API_KEY |

## Notion 設定

- Workspace page：My Wallet Trip（授權給 integration：my-wallet-trip）
- Trips database：欄位 name / country / city / startDate / endDate / currency
- Expenses database：欄位 store / date / amount / currency / amountTWD / exchangeRate / category / note / tripId / dayNumber / isPreTrip

## 本機開發

```bash
cd ~/Documents/my-wallet-trip
npm run dev   # http://localhost:3000
```

## 部署

```bash
cd ~/Documents/my-wallet-trip
npx vercel --prod
```

或 push 到 GitHub main → Vercel 自動部署。

## 功能

- 旅遊模式：建旅程 → 自動 Day 1/Day 2 → 旅程總結
- 日常模式：按月份分類
- 拍照 / 匯入圖片 → Gemini OCR 自動填日期、金額、類別
- 即時匯率（多 API fallback）
- 原幣 + 台幣雙欄顯示
- 消費可編輯 / 刪除
- 圓餅圖（類別分布）+ 面積折線圖（每日花費）
- Top 5 消費排行
