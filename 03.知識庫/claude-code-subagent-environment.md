---
title: Claude Code Subagent 初始環境與內建代理機制
tags: ["Claude Code", "Agent", "工作流程", "開發工具"]
date: 2026-04-17
category: 開發工具
source: goodarticle/2026-04-17_Subagent_初始環境.md
---

## 這是什麼
本文解析 Claude Code 中 Subagent 的啟動環境配置、繼承規則，以及如何透過 Explore、Plan 等內建代理機制與手動指派，達成 Token 消耗減半與高效開發。

## 核心概念
*   **環境繼承規則**：Subagent 預設從主對話繼承 MCP servers、工具權限（可用白/黑名單限制）、權限上下文及當前工作目錄。此外，全域與專案內的 `CLAUDE.md` 規則也會被載入。
*   **獨立工具化啟動**：透過 `claude --agent <名稱>`（如 `code-reviewer`）可啟動特定身份的 Session，該環境會鎖定專用的 System Prompt 與工具限制。
*   **三大內建 Subagent**：
    *   **Explore**：搭載 Haiku 模型，僅限唯讀工具，專門搜尋 codebase，成本低且速度快。
    *   **Plan**：Plan mode 下自動指派，專注於研究與產出計畫，避免邊想邊改造成錯誤。
    *   **General-purpose**：具備完整工具權限，適合執行多步驟任務。

## 使用方法 / 快速啟動
*   **手動指派任務**：在對話中主動指令「用 Explore 去查」或「用 Subagent 做這件事」，能強迫系統使用低成本方案處理搜尋任務。
*   **啟動專用環境**：執行 `claude --agent <agent-name>`，啟動後 header 會顯示身份標記，確保環境乾淨且專一。

## 對派哥的啟示
*   **自動化成本管理**：派哥在台灣開發 AI 工具時，應參考 Explore 的設計模式，在「搜尋/分析」與「執行/修改」之間切換不同的模型與權限。利用 Haiku 處理海量 codebase 檢索，可大幅降低 token 支出。
*   **模組化 Agent 設計**：目前的 OpenClaw 專案可利用 `--agent` 模式，將複雜的自動化流程（如財務報表、旅遊規劃）封裝成特定 Agent，透過 frontmatter 的 `tools` 欄位精準限縮工具權限，提升安全性。
*   **規則前置載入**：善用 `CLAUDE.md` 來定義 Subagent 的行為規範，這對派哥建構「組織知識工程」至關重要，能確保所有派出的子代理都遵循一致的代碼風格與操作邏輯。

## 連結筆記
## 連結筆記
- [[claude-code-feature-workflow]]
- [[boris-15-claude-code-tips]]
- [[boris-parallel-claude-workflow]]
- [[claude-code-powerup-guide]]
- [[claude-subagent-context-management]]
