---
title: "雙 AI 協作開發迴圈（Claude Code + Coworker + Notion）"
tags: [claude-code, coworker, notion, automation, testing, multi-agent, workflow]
date: 2026-04-01
category: 03.科技工具
---

## 核心概念

> 用兩個 AI 分工：一個寫/修 code，一個測試；Notion 當中樞協調，形成「邊睡覺邊優化」的自動循環。

## 角色分工

| 角色 | 工具 | 職責 |
|------|------|------|
| **開發者** | Claude Code | 讀 Notion 問題 → 修復 code → 更新狀態 |
| **測試者** | Claude Coworker | 透過瀏覽器視覺測試 → 寫問題進 Notion → 複測驗證 |
| **中樞** | Notion | 問題清單、狀態追蹤、兩個 AI 的溝通介面 |

## 流程

```
Coworker 發現問題
  → 寫入 Notion（狀態：待修復）
  ↓
Claude Code 讀取
  → 修復 code
  → 更新 Notion 狀態（已修改）
  ↓
Coworker 複測
  → 通過 → 狀態：複測 OK
  → 未通過 → 重新整理描述，等下一輪
  ↓
Coworker 測試中發現新問題
  → 自動補進 Notion
  ↓
（回到頂端，無限循環）
```

## 實際效果（案例）

1. Coworker 寫了 4 個問題
2. Claude Code 修復，狀態改「已修改」
3. Coworker 複測：3 個通過（→「複測 OK」）、1 個未解
4. 同時新發現 3 個問題，自動補進 Notion
5. 下一輪繼續處理

## 為什麼用 Coworker 而不是 Subagent？

- Coworker 透過**瀏覽器 + 視覺**測試，模擬真實使用者行為
- DOM 判斷不夠，視覺測試更接近實際使用情境
- 缺點：效率較低、token 消耗較高
- 適合還需要人工確認品質的開發階段

## 可替代方案

- 兩個 Claude Code 互搭
- Claude Code + Subagent 做自動化測試
- Coworker 替換成 Playwright / Puppeteer 腳本

## 如何用 / 用在哪

**適合場景：**
- Web app 功能開發，需要反覆測試修復
- 睡前跑任務，早起看結果
- 不想盯著 IDE 的長跑式優化

**前提條件：**
- Claude Code 可存取專案 repo
- Claude Coworker 可開啟瀏覽器
- Notion 設好問題追蹤頁面（或用其他共享資料來源，如 GitHub Issues、Airtable）

**啟動方式：**
1. 設好 Notion 問題頁面格式（title、狀態欄、描述欄）
2. 給 Coworker 指令：測試 → 寫問題進 Notion
3. 給 Claude Code 排程：讀 Notion → 修復 → 更新狀態
4. 讓兩個 agent 各自跑排程，互相等待對方完成

## 關鍵洞察

這個模式本質是把 **spec_as_code / test_as_code** 的精神自動化：
- 測試不是人跑，是 AI 跑
- 問題不是人記，是 AI 記進 Notion
- 修復不是人催，是排程自動觸發

→ 開發者角色從「執行者」變成「架構者 + 最終審核者」

## 相關

- [[ai-coding-shift-left]]
- [[codex-plugin-cc]]
