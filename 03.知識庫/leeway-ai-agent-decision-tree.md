---
title: Leeway：用 YAML 決策樹找回 AI Agent 的執行秩序
tags: ["AI", "Agent", "自動化", "架構設計"]
date: 2026-04-15
category: 開發工具
source: goodarticle/Leeway_YAML_Decision_Tree_for_AI_Agent_Order_repost.md
---

## 這是什麼
Leeway 是一個開源的 AI Agent 編排工具，透過 YAML 定義的決策樹來規範 Agent 的執行流程。它旨在解決 AI 執行過程不可預測、難以稽核的問題，讓複雜的工程任務能以穩定的順序重複執行。

## 核心概念
*   **YAML 決策樹**：將工作流定義為結構化的節點，確保執行順序一致，解決 LLM 執行過程隨機性過高的痛點。
*   **節點化權限管理**：精確控制每個節點可使用的 MCP server、特定檔案路徑及 shell 指令，實現細粒度的安全限制。
*   **訊號驅動流程**：LLM 在節點內解決問題後回傳狀態訊號（如 "passed" 或 "needs_fix"），由流程圖根據訊號決定下一個執行節點。
*   **Human-in-the-loop**：預設人工審核機制與敏感操作監控，並提供唯讀計畫模式，確保 AI 自主性不等於失去控制。
*   **本地開發導向**：不同於雲端整合工具，Leeway 專注於本地 codebase、檔案系統與終端機環境的深度操作。

## 使用方法 / 快速啟動
1.  **環境安裝**：底層基於 Python，介面採用 React/Ink TUI。
2.  **定義流程**：撰寫 YAML 檔案，劃分任務節點並配置各節點的權限範圍與可用 Skill。
3.  **配置模型**：設定 OpenAI 或 Anthropic 等主流模型的 API 金鑰。
4.  **執行與互動**：啟動工具後，Agent 將依照決策樹路徑執行，並在必要時請求人工審核。

## 對派哥的啟示
*   **提升自動化工具的商用可靠度**：派哥在台灣開發 AI 工具時，穩定性是企業客戶的首要考量。引入「流程圖控制大方向、模型專心解題」的架構，能大幅降低 AI 亂跑的風險。
*   **強化安全閘道設計**：Leeway 的節點權限管理與人工審核機制，可直接應用在派哥開發的自動化工具中，特別是涉及 shell 指令或檔案修改等高風險操作時。
*   **本地端自動化利基**：相較於 n8n，派哥可以參考 Leeway 對本地環境（Codebase/Shell）的控制方式，開發更貼近開發者或系統管理需求的自動化工具。
*   **架構設計的平衡藝術**：這提醒派哥在追求 AI「全自主」的同時，必須保留「結構化秩序」，在 LLM 的靈活性與工程任務的嚴謹性之間找到最佳平衡點。

## 連結筆記
## 連結筆記
- [[ai-agent-modular-architecture]]
- [[ai-agent-system-design-over-prompt]]
- [[claude-routines-automation]]
- [[full-agent-dev-ecosystem-goatwang]]
- [[agent-skills-standard]]
