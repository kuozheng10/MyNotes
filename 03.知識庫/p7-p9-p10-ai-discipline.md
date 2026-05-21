---
title: P7/P9/P10：AI 工程紀律方法論
tags: [AI, Claude Code, Agent, 工作流程]
date: 2026-04-19
category: AI工具
---

## 這是什麼

NYCU-Chung 的開源專案 [my-claude-devteam](https://github.com/NYCU-Chung/my-claude-devteam)，把 Claude Code 組成 12 人 AI 工程團隊，各角色分工明確：

- `planner`：只拆任務，不寫碼
- `fullstack-engineer`：執行實作
- `critic`：只找問題，禁止說「看起來OK」
- `vuln-verifier`：寫 PoC 證明漏洞存在
- `debugger`：只追根因

專案內建 15 個 hooks，自動攔截 debugger 語句、硬編密碼、AI 生成的 generic UI。核心方法論叫 **P7/P9/P10**。

## 核心概念

AI 不是能力不夠，是紀律不夠。方法論的作用是把「應該做但會偷懶的事」變成「不做就無法交付」。

常見的 AI 偷懶行為：
- 跳過影響分析
- 說「看起來沒問題」而非驗證
- 忘記自己改了哪些地方

**失敗2次換方法**：同一任務失敗 2 次，停止重試原方案，寫下三個全新假設逐一驗證。說「無法解決」之前，必須先搜官方文件、讀源碼、窮舉可能原因。

## P7/P9/P10 方法論

依任務規模切換工作紀律，不是角色扮演。

### P7：小事（單一功能修改）

流程：讀現況 → 設計方案 → 影響分析 → **三問自審** → 完成交付

三問自審強制 AI 回答：
1. 方案正確嗎？
2. 影響分析全面嗎？
3. 有回歸風險嗎？

答不出來就不能交付。

### P9：中事（動到 3+ 個檔案）

先拆成獨立子任務，每個子任務帶六要素：

| 要素 | 說明 |
|------|------|
| 目標 | 這個子任務要達成什麼 |
| 範圍 | 哪些檔案/模組在範圍內 |
| 輸入 | 接收什麼資料/狀態 |
| 輸出 | 產出什麼結果 |
| 驗收 | 怎麼確認完成 |
| 邊界 | 什麼不在範圍內 |

禁止 planner 自己下場寫碼。

### P10：大事（跨系統架構）

輸出戰略文件，不定義程式碼，不定義 Task，只定義：
- 目標
- 指標
- 風險

## 對派哥的啟示

派哥用 Claude Code 跑 cc_processor、sales report 自動化、Notion Todo 等系統，P7/P9/P10 直接對應三種場景：

**P7 場景**：修一個 BankAdapter 的解析邏輯、調整 Telegram 回報格式。改之前先讓 AI 做影響分析，三問自審後才允許交付，避免改 HSBC 卻爆掉國泰的情況。

**P9 場景**：新增一個銀行 adapter 同時要動 config、parser、scheduler 三個檔案。這時要先讓 planner 拆成三個帶六要素的子任務，不要讓 AI 一口氣全改。

**P10 場景**：評估要不要把 cc_processor 接進 OpenClaw gateway 統一排程。這個階段只產出目標/指標/風險文件，不急著動程式碼。

**hooks 概念**：可以在 CLAUDE.md 或 settings.json 裡加入自動攔截規則，比如禁止 hardcode API key、禁止直接 push main，強制 AI 遵守紀律而不是靠提醒。

## 連結筆記

- [[ai-agent-system-design-over-prompt]] — 系統設計優先於 prompt 工程
- [[ai-sycophancy-adversarial-agent]] — AI 說「看起來OK」的討好問題
- [[agent-skills-standard]] — Agent skill 標準化設計
