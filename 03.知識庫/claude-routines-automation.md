---
title: Claude Routines：打包排程、API 與 GitHub 事件的 AI 自動化新利器
tags: ["AI", "Claude", "自動化", "工作流程"]
date: 2026-04-15
category: 工作流程
source: goodarticle/Claude_Routines_Automations.md
---

## 這是什麼
Claude 推出的 Routines 功能（研究預覽版），是一個整合型的 AI 自動化解決方案。它將 Prompt、儲存庫與 MCP 連接器打包，讓使用者能透過 UI 快速設定排程、API 或 GitHub 事件觸發的自動化任務。

## 核心概念
*   **整合化配置**：捨棄複雜的 GitHub Actions YAML 與 Secret 設定，改以 Web UI 直接勾選 MCP 連接器（如 Slack、Linear）與關聯 Repo。
*   **多重觸發機制**：
    *   **排程 (Schedule)**：支援自定義 Cron 格式，執行週期性任務。
    *   **API 呼叫**：提供專屬 HTTP Endpoint 與 Token，可從外部系統（如 Deploy Pipeline）觸發。
    *   **GitHub 事件**：監控 PR、Push 或 Issue，並可針對作者、分支或標籤進行篩選。
*   **全自動執行**：執行過程中無需人工介入確認（No Approval Prompt），強調流程的連貫性。

## 使用方法 / 快速啟動
1.  **建立 Routine**：在 Claude 介面設定 Prompt 任務內容與目標 Repo。
2.  **串接工具**：勾選所需的 MCP Connectors，系統會自動處理授權與連線。
3.  **設定觸發點**：
    *   若為排程：設定執行頻率。
    *   若為 API：獲取 Bearer Token 並整合至現有工作流。
    *   若為 GitHub：連結 Repo 並設定過濾條件。
4.  **監控與調整**：檢視執行日誌，因處於預覽階段，需留意每日執行次數上限。

## 對派哥的啟示
身為在台灣開發自動化 AI 工具的開發者，這項功能提供了一個極佳的「輕量化後台」方案：
1.  **簡化客戶交付**：以往幫客戶做 GitHub 自動化需要寫 YAML 和設 Secret，現在可以透過 Routines 的 UI 快速封裝，降低維護門檻。
2.  **異常監控自動化**：可結合現有的監控系統，當系統出錯時打 API 觸發 Routine，讓 Claude 自動分析日誌、開啟 Issue 並透過 Telegram 頻道（派哥常用頻道）發送結構化摘要。
3.  **在地化知識同步**：可排程每晚掃描技術文件或 PR，自動生成繁體中文的開發摘要，並同步至 Notion 或派哥的工作管理系統中。

## 連結筆記
## 連結筆記
- [[boris-parallel-claude-workflow]]
- [[claude-code-feature-workflow]]
- [[claude-managed-agents-beta]]
- [[bugfix-8steps-workflow]]
- [[gmail-automation-spec]]
