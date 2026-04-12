---
title: 全 Agent 開發生態實錄 — GoatWang 的 20 commits/day 工作法
tags: [Agent, Codex, Claude, Worktree, 開發流程, 測試, iOS, 效率]
date: 2026-04-12
category: AI工具
source: https://goatwang.github.io/posts/20260412_full_agent_dev_ecosystem/
---

## 核心主張

GoatWang 一個月內完全轉型：「我不再看任何一行程式碼、不再審查 Agent 的 diff」，只做需求規劃和交付驗收。每日 4 個 Codex sessions + 3 個 Telegram Claude sessions，可交付 20+ 個驗證過的 commits。

---

## 8 個實戰建議

### 1. 必須閉環（Self-Verification Loop）

Agent 必須能自我驗證，否則人類驗收跟不上開發速度。

- Web：已成熟，透過 DOM/ID 操作控制
- iOS 突破：發現 UI Automation 套件（類似 Android adb），可取得 UI component ID
- Agent 現可自行撰寫驗證提案、產截圖報告
- 限制：一次只能用一個 Simulator，多開會 conflict

### 2. 只要動到 Code 就要開 Worktree

無論功能大小都開獨立 worktree，避免 main 分支阻塞。

- 同時掛載 3-4 條開發主線
- 每提交 prompt 後即有下個 terminal 等待回應
- 「心流不是被打斷，是被換了一種形狀」
- 可維持 15 小時以上高強度開發

### 3. 獨立乾淨的驗證環境

每個 session 各自的資料夾、邏輯、port、資料庫。

- 開發效率至少快 2 倍
- 好的 test plan 設計，AI 跑驗證的時間可能是開發時間的好幾倍

### 4. 先抄襲後加 Feature

應用程式背後有深層工程 domain，先複製成熟基礎架構，再加自己的功能。

- Telegram 案例：內建 SQLite、半透明設計、local pagination 優化
- 減少「A feature 做完 B feature 就壞」的 debug 迴圈
- 讓 Agent session 可連續工作 2 小時以上不需介入

### 5. 可維護性設計

AI 傾向短期解決問題，容易在多個檔案重複寫相同邏輯。

- 改一個地方適用全專案
- File Explorer 案例：三個入口同一元件，應 modularize 而非複製
- 重複邏輯整理成 function/module

### 6. File System 就是 Memory System

每個 feature：implementation plan → verification plan → report，用日期+序號命名資料夾。

- 一天 20 commits ≈ 600 個月度資料夾
- 加上 commit logs + session history，用 grep 仍可用
- 自建 `find_context` command 搜尋相關資料夾
- 「太過系統化、高階抽象化的 Memory，對人類反而是障礙」

### 7. Effort 開到最大

寧願慢慢等，也不要繞圈子。

- Claude：無法看清全局、討好人格令人煩躁
- Codex：「只要沒有 misalignment，基本上都能完成任務」

### 8. 搭配使用策略

- Claude 買 100（當 PM）+ Codex 買 200（執行開發）
- Claude 負責翻譯需求、拆任務、督促進度、產決策報告
- 可延長連續工作時間 1.5 倍
- 但若有整天時間，直接開 4 個 Codex sessions 效率更高

---

## 核心洞見

- 開發模式質變：從審查 code → 規劃需求 + 驗收
- 多 worktree 平行工作提升心流，不造成疲倦
- 檔案系統 + grep 比抽象記憶系統更務實可用
- 複製成熟應用基礎架構 >> 從零開始
- 一個月產出超過一年傳統開發工作量

---

## 對派哥的應用建議

- Worktree 策略值得立刻採用（已有 Claude Code，再加 Codex 更有威力）
- File System as Memory 的做法和現有 MyNotes 方向一致，可強化 session report 命名規則
- Self-Verification Loop 概念：sales_report_processor 驗證流程可加自動截圖/log 報告
- Claude PM + Codex Dev 分工：目前架構剛好匹配，可實驗看看
