---
title: "Boris Cherny 的 15 個 Claude Code 高頻技巧"
tags: [claude-code, tips, productivity, automation, cli, worktree, hooks]
date: 2026-04-01
category: 03.科技工具
source: Boris Cherny (Anthropic, Claude Code 主導開發) on X
---

## 背景

> Anthropic 主導 Claude Code 開發的 Boris Cherny 分享他最常用的 15 個技巧，發出後超過 300 萬次瀏覽。

---

## 隨時隨地寫程式

### 1. 手機 App 直接 Code
- Claude App（iOS / Android）左邊有 Code 分頁
- Boris 經常直接在手機上寫程式

### 2. `claude --teleport` 跨裝置移動 Session
- 雲端跑的 session 想在本機繼續 → `claude --teleport` 或 `/teleport`
- 反過來從手機/網頁遠端控制本地 session → `/remote-control`
- 建議預設開啟「Enable Remote Control by default」

### 15. `/voice` 語音輸入
- CLI 執行 `/voice`，長按空白鍵說話
- 手機上按語音按鈕
- Boris 大部分程式都是講話寫的，不是打字

---

## 自動化與排程

### 3. `/loop` 和 `/schedule` 排程執行
- 設定時間間隔，最多跑一個禮拜
- 範例：`/loop 5m /babysit` → 每 5 分鐘自動處理 code review、rebase、修 CI

### 4. Hooks 在 Session 生命週期運行邏輯
- SessionStart：動態載入最新 context
- PreToolUse：記錄每條 bash 指令
- 進階：把權限提示傳到 WhatsApp 求核准

---

## Session 管理

### 8. `/branch` 或 `--fork-session` 分支 Session
- 複製一份 session，改方向試試，不影響原本工作
- 方法一：現有 session 內執行 `/branch`
- 方法二：`claude --resume <session-id> --fork-session`

### 9. `/btw` 快速旁問
- 主 session 還在跑，同時問 Claude 一個快速問題
- Claude 繼續做自己的事，同時給你答案
- Boris 說他一直在用這個

---

## 前端開發輔助

### 6. Chrome Extension 讓 Claude 看到自己寫的東西
- Boris 說這是**最重要的技巧**
- Claude 能看到自己建的頁面、點擊測試、看 console、然後迭代
- 前端光程式碼對了不夠，要親眼看執行結果

### 7. Desktop App 內建網頁伺服器和測試
- Claude Desktop App 內建自動執行網頁伺服器、在瀏覽器裡測試的能力
- CLI 也可以設定類似功能

---

## 平行處理大量工作

### 10. Git Worktrees 同時跑多個 Claude
- `claude -w` → 在 worktree 開新 session
- Boris 經常有幾十個 Claude 同時跑，在同一 repo 的不同 worktree
- Worktree = 同一資料夾建多個獨立工作分支，互不干擾

### 11. `/batch` 大量展開工作
- 把大工作分散給幾十/幾百/幾千個 worktree agent
- 適用：大型程式碼遷移、可平行化的工作
- `/batch` 會問你問題後自動分配

---

## 進階 CLI 技巧

### 12. `--bare` 啟動速度提升最多 10 倍
- 預設 `claude -p` 會搜尋 CLAUDE.md、設定、MCPs
- `--bare` 跳過自動搜尋，明確指定要載什麼
- 適用非互動式場景（腳本、CI/CD）

### 13. `--add-dir` 跨資料夾存取多個 repo
- 在一個 repo 啟動 Claude，用 `--add-dir`（或 `/add-dir`）讓 Claude 同時看到其他 repo
- 不用重開 session

### 14. `--agent` 自訂 Agent
- 在 `.claude/agents` 定義 agent，設定自訂 system prompt 和工具
- `--agent` 執行
- 打造專屬某類工作的 Claude 版本

---

## Cowork 相關

### 5. Dispatch 遠端控制
- Boris 每天用 Dispatch 趕上 Slack、email、管理檔案、不在辦公室時處理筆電上的事
- Dispatch = Claude Desktop App 的安全遠端控制
- 支援 MCPs、瀏覽器、computer use、skills、plugins

---

## 對派哥最有用的幾個

| 技巧 | 場景 |
|------|------|
| `/btw` | 讓我做事的同時快速問一個問題 |
| `/branch` | 試一個想法，不影響主線工作 |
| `/loop` + `/schedule` | 定時讓我自動做某件事 |
| `--add-dir` | 同時處理多個專案 |
| `--agent` | 定義專屬某任務的 Claude 版本 |
| `/batch` | 大量遷移或重構任務平行化 |

## 相關

- [[claude-hidden-combo]]
- [[dual-agent-dev-loop]]
