---
title: Claude Code 狀態列儀表板插件：即時追蹤費用與配額
tags: ["Claude Code", "工具", "工作流程", "自動化"]
date: 2026-04-21
category: 開發工具
source: goodarticle/2026-04-21_CC_狀態列插件.md
---

## 這是什麼
由 SammyLin 開發的 Claude Code 狀態列插件，能將費用、Token 配額、任務進度等關鍵資訊直接顯示在終端機 Prompt 旁，解決頻繁詢問狀態的痛點。

## 核心概念
- **即時監控儀表板**：整合費用追蹤（Compaction 記錄）、Rate Limit 倒數（5h/7d）以及 Context Compaction 進度。
- **任務透明化**：可追蹤 Subagent 狀態、MCP Server 健康狀況以及目前已編輯的檔案清單。
- **外掛式架構**：採用 Plugin 模式實作而非 Fork 原始碼，確保 Claude Code 版本更新時不會導致功能失效。
- **Hooks 系統探索**：克服官方文件不足的困難，透過 Log 與嘗試錯誤找出 Subagent Start/Stop 等 Hooks 的正確運作機制。

## 使用方法 / 快速啟動
1. 訪問專案倉庫：`https://github.com/SammyLin/cc-statusline`
2. 依照專案說明將其整合至 Claude Code 環境，即可在開發時即時掌握資源消耗。

## 對派哥的啟示
這對於開發自動化 AI 工具非常有參考價值。在派哥處理如「業務業績統計」或「銷售報告分析」等長時間運行的 Agent 任務時，可以參考此專案的 Hooks 實作方式，為自己的自動化流程加入可視化的儀表板或狀態監控，精確掌控 Token 成本與 API 配額，提升工具的穩定性與使用者體驗。

## 連結筆記
## 連結筆記
- [[boris-15-claude-code-tips]]
- [[claude-code-feature-workflow]]
- [[claude-code-powerup-guide]]
- [[claude-code-subagent-environment]]
- [[claude-routines-automation]]
