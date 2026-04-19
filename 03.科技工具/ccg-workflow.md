---
title: ccg-workflow：多 AI 協作開發的 CLI 編排系統
tags: ["Claude Code", "AI", "工作流程", "工具"]
date: 2026-04-19
category: 開發工具
source: goodarticle/2026-04-19_ccg-workflow：多AI協作開發.md
---

## 這是什麼
ccg-workflow 是一個基於 CLI 的多 AI 協作編排系統，整合了 Claude Code、Gemini 與 Codex，旨在透過不同模型間的三角分工，提升自動化開發的效率與安全性。

## 核心概念
- **三角分工系統**：由 Claude Code 擔任監督角色，Gemini 處理前端任務，Codex 處理後端開發，發揮各模型長處。
- **安全審查模型**：外部模型（Gemini/Codex）產出的內容僅作為 Patch（補丁），必須經由 Claude Code 審查後才能正式套用至代碼庫，防止未經檢核的代碼直接執行。
- **OPSX (Specification-driven development)**：強調規範驅動開發，將模糊的原始需求轉化為可驗證、具體化的技術規格文件。

## 使用方法 / 快速啟動
- **安裝環境**：需要 Node.js 20+、Codex CLI 與 Gemini CLI。
- **快速開始**：
    1. 執行 `npm install -g ccg-workflow` 進行全域安裝。
    2. 使用 `/ccg:plan` 指令分析需求，自動產出 `plan.md`。
    3. 選擇實作模式：
        - 高精準度：使用 Claude Code 實作。
        - 高性價比：執行 `/ccg:codex-exec`，由 Codex 依照計畫執行，Claude 僅負責最終審核。
- **指令系統**：內建 28 個斜槓指令，涵蓋 Planning、Execution、Git Workflow 與 Code Review。

## 對派哥的啟示
- **工具鍊整合**：派哥目前已在台灣開發環境中佈署 Gemini CLI 與 Codex，安裝後可無縫銜接現有工作流。
- **架構設計自動化**：透過 `/ccg:plan` 自動生成架構規劃，能大幅節省在開發初期手動構思系統架構的思考成本與 Token 消耗。
- **成本優化策略**：針對 `cc_processor` 財務處理器的重構或 `My Wallet Trip` 的新功能開發，可採用「Codex 執行、Claude 審查」的低成本高效模式。
- **安全性提升**：安全審查模型能確保在自動化處理台灣各銀行（如國泰、台新）財務數據的代碼變動時，均經過 Claude 的邏輯驗證，降低出錯風險。

## 連結筆記
## 連結筆記
- [[boris-15-claude-code-tips]]
- [[claude-code-feature-workflow]]
- [[claude-code-powerup-guide]]
- [[boris-parallel-claude-workflow]]
- [[claude-code-subagent-environment]]
