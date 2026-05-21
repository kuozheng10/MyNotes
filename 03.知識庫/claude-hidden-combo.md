---
title: "Claude 隱藏組合拳：瀏覽器抓取 + 排程 + Memory"
tags: [claude, automation, browser, schedule, memory, cowork, no-code, 競品分析]
date: 2026-04-01
category: 03.科技工具
source: https://youtu.be/S5tlVwPoHqk
author: Wilson威爾森實驗室
duration: 11:41
---

## 影片主旨

> 零程式碼，讓電腦每天自動爬競品資料並累積成可查詢資料庫。
> Claude Cowork 三個功能組合：Chrome 瀏覽器操控 + 排程自動化 + Memory 記憶。

## 三大功能

### 1. Claude in Chrome（瀏覽器操控）
- 安裝 Chrome 擴充功能，讓 Claude 直接操控瀏覽器
- 自動瀏覽競品網站、抓取首頁熱銷產品名稱/售價/促銷
- 可設定 **Act without asking**（不逐步詢問，自動執行）
  - ⚠️ 有 High Risk 警告，會代你在網路上執行動作

### 2. Cowork Schedule（排程自動化）
- 路徑：Cowork → Schedule → New Task
- 設定 Name（需含英數）、Prompt、Frequency、執行時間、模型
- 觸發條件：**電腦要開著 + Claude 保持聯網**（本機執行，非 server-side）

**範例 Prompt：**
```
每天早上 8 點，用 Claude in Chrome 依序瀏覽網站A/B/C 首頁，
取前三熱銷產品含售價與促銷狀態，
更新到 Memory，格式：咖啡競品_年月日
```

### 3. Memory（記憶累積）
- 排程每次執行後自動寫入 Memory（Claude 的筆記本）
- 跨 session 保留，可直接問「這週競品有誰在促銷？」
- ⚠️ 限**同一 Project 內**才能跨 session 共享

## 實際案例：台灣精品咖啡豆競品分析

三家競品（黑沃/歐克勞/烘焙者）9 個產品比較：

| 品牌 | 定價策略 | 特色 |
|------|----------|------|
| 黑沃咖啡 | 原價 800，促銷 400（5折） | 低價衝轉換率，視覺衝擊強 |
| 歐克勞 | 買二送一，換算約 533–667/磅 | 不直接折價，實質多拿一包 |
| 烘焙者 | 定價 680，無折扣 | 走品牌質感，不打折 |

**Claude 的分析洞察：**
黑沃和歐克勞用促銷製造低價感，非真的低價品位；若黑沃恢復原價，三家定價其實相近。

## 流程總覽

```
指令：找競品品牌
  → Claude Google 搜尋 → 確認官網
  → 逐一瀏覽首頁 → 抓前三熱銷產品
  → 整理比較表 + 定價策略分析
  ↓
設定 Schedule（每週一次）
  → 自動重複爬取
  → 結果寫入 Memory
  ↓
隨時問 Claude：「這週競品有沒有促銷？」
  → 從 Memory 回答，資料越積越多
```

## 限制與建議

- 排程需電腦開著，不適合長時間離線
- Token 消耗高（Opus 尤其燒）→ 排程建議用 Sonnet
- Memory 限同一 Project，跨 Project 不共享
- 免費提示詞範本：[Skool 社群](https://www.skool.com/wilson-9076)

## 對比現有工具

| | 這個方案 | Claude Code（我）|
|---|---|---|
| 對象 | 不寫程式的人 | 開發者 |
| 排程 | Cowork Schedule（本機） | Cron / 伺服器排程 |
| 記憶 | Claude Memory（Project 內） | 自訂 memory 系統 |
| 測試 | 視覺瀏覽器 | 可整合 Playwright/Whisper |

## 相關

- [[dual-agent-dev-loop]]
- [[openmemory-auto-manager]]
