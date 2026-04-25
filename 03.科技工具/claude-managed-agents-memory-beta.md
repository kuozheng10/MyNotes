---
title: Claude Managed Agents Memory：Filesystem 記憶架構（Public Beta）
tags: ["Claude", "Managed Agents", "Memory", "企業AI", "架構設計", "agent"]
date: 2026-04-25
category: AI工具
source: Telegram 派哥分享
---

## 核心設計：記憶掛在 Filesystem，不是獨立 API

Anthropic 的 Memory 設計選擇：直接用檔案系統存記憶，而非打造專屬記憶 API。

**為什麼這樣做**：Claude 本來就擅長 bash 和 code execution，讀寫檔案就是它已熟悉的工具棧。Agent 不必學新 API、不必切換 context——記憶就是多讀寫幾個檔。看起來 naive，實際上是減少認知負擔的設計。

**Opus 的調校**：最新 Opus 模型針對 filesystem memory 特別優化，會主動分類筆記、挑重點保留，而不是把雜訊全部寫進去。

---

## 企業層的三個關鍵設計

### 1. 跨 Agent 共享 + 權限分層

- 組織層級知識：唯讀（所有 agent 可讀，不可寫）
- 個人層級記憶：讀寫
- 多個 agent 同時寫入不互相覆蓋

### 2. 審計紀錄（Audit Trail）

每筆記憶改動都附帶：
- 是哪個 session 寫的
- 是哪個 agent 寫的
- 可回滾（記錯了可以復原）
- 可遮罩抹除（記到不該記的可從歷史移除）

### 3. 記憶是可治理的基礎建設

不只是功能，而是可匯出、可審計、可治理的架構——對有稽核需求的企業（金融、醫療）有直接意義。

---

## 早期客戶數據

| 客戶 | 做法 | 效果 |
|------|------|------|
| Rakuten | 長執行 agent 用 memory 學自己的錯 | 第一次就對的比例提升 97% |
| Wisedocs | 文件驗證流程，跨 session 記住反覆出現的問題 | 驗證速度快 30% |
| Netflix | 跨對話延續脈絡，人類中途修正也寫回 | 不需手動更新 prompt 與 skill |
| Ando | 直接省掉自建記憶基礎建設 | 工程時間轉移到產品層 |

---

## 核心命題

Agent 從「每次開新對話都冷啟動」走向「會累積的工作夥伴」。

記憶不再只是功能，而是可匯出、可審計、可治理的基礎建設。

---

## 對派哥的啟示

**目前的關聯**：
- 派哥的 `~/.claude/projects/memory/` 系統本質上就是這個設計的個人版——filesystem-based、可審計、跨 session 持久
- Claude Code 已有 handover.db + MEMORY.md 做到類似效果，只是沒有多 agent 共享層

**值得觀察的**：
- Managed Agents Memory 的組織層唯讀知識 = 派哥 CLAUDE.md 的概念，但可以多 agent 共享
- 等 Managed Agents 穩定後，cc_processor / 一蘭 的跨 agent 知識共享可以參考這個架構

**短期不需要行動**：繼續觀察 public beta 演進。

---

## 連結筆記

- [[claude-managed-agents-beta]] — Managed Agents 整體功能
- [[claude-mem-system]] — 派哥現有的 memory 系統設計
- [[harness-engineering]] — Agent 基礎建設層的思路
- [[anthropic-mcp-production-patterns]] — Vaults：OAuth token 管理，同樣是 Managed Agents 的基礎建設層
