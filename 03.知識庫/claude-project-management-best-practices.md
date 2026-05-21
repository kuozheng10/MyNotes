---
title: 系統化管理 Claude 開發專案的目錄架構與規範建議
tags: ["Claude Code", "架構設計", "自動化", "工作流程"]
date: 2026-04-15
category: 開發工具
source: goodarticle/Managing_Claude_Projects.md
---

## 這是什麼
本文介紹如何透過系統化的目錄結構與配置檔案（如 CLAUDE.md、rules/ 等）來管理 Claude 開發專案，將原本零散的 Prompt 轉化為可維護、可共享且具備自動化能力的工程化流程。

## 核心概念
- **CLAUDE.md (核心指南)**：專案的行動準則，包含背景、編碼標準與注意事項，是 Claude 每次啟動必讀的 Onboarding 文件。
- **rules/ (模組化規範)**：將規則按主題（如 Style、測試、資安）拆分，提升維護便利性。
- **commands/ (流程自動化)**：將常用操作（如 Lint 檢查、發 PR、產 Changelog）定義為指令，實現一句話調用。
- **skills/ (情境觸發)**：根據上下文（如開啟特定檔案）自動執行的智慧檢查邏輯。
- **agents/ (獨立任務專家)**：建立彼此隔離的子代理處理特定任務，避免 Context 互相污染。
- **settings.json (權限管控)**：嚴格鎖定執行權限與安全白名單，確保操作安全性。
- **雙層級管理**：區分「專案層級」（隨 Repo 共享）與「全域層級」（位於 `~/.claude/`，儲存個人偏好與跨專案記憶）。

## 使用方法 / 快速啟動
1. **建立核心檔案**：在專案根目錄建立 `CLAUDE.md`，寫入你的開發標準與專案脈絡。
2. **結構化目錄**：建立 `.claude/` 資料夾，並根據需求設置 `rules/` 與 `commands/` 子目錄。
3. **定義權限**：透過 `settings.json` 設定哪些指令需要人工確認，哪些可以直接執行。
4. **封裝指令**：將重複性的開發流程寫入 `commands/`，例如 `npm run lint && git commit` 等連動動作。

## 對派哥的啟示
對於在台灣開發自動化 AI 工具的派哥來說，這套架構能解決開發多個專案時「背景資訊混亂」的問題。
- **系統化封裝**：派哥在串接 Telegram 或 Notion API 時，可將特定的 API 限制與錯誤處理規範寫入 `rules/`，讓 Claude 在開發相關模組時自動遵守，減少 Debug 時間。
- **安全性與穩定性**：透過 `settings.json` 鎖定權限，避免 AI 在執行自動化腳本時意外更改環境變數或刪除正式資料庫。
- **效率倍增**：將「部署測試版」或「串接 API 文件」等繁瑣工作封裝進 `commands/`，能更專注於 AI 工具的邏輯設計，而非重複的 CLI 指令敲擊。

## 連結筆記
## 連結筆記
- [[claude-code-feature-workflow]]
- [[boris-parallel-claude-workflow]]
- [[ai-agent-modular-architecture]]
- [[claude-routines-automation]]
- [[full-agent-dev-ecosystem-goatwang]]
