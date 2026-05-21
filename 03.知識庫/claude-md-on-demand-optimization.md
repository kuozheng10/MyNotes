---
title: CLAUDE.md 按需讀取優化：節省 10 倍 Token 的目錄架構
tags: ["Claude Code", "工具", "工作流程", "知識管理"]
date: 2026-04-19
category: 開發工具
source: goodarticle/2026-04-19_CLAUDE.md_按需讀取優化.md
---

## 這是什麼（1-3行）
這是一種針對 Claude Code 運作機制的優化策略，將 `CLAUDE.md` 從原本收錄所有規則的「完整員工手冊」轉型為「引導目錄」，大幅降低 API Token 的消耗與成本。

## 核心概念
Claude Code 在每一輪對話中都會重新載入整份 `CLAUDE.md`。透過將具體流程（如 Bug Fix、Feature 開發）拆分至獨立的規範檔案，並在 `CLAUDE.md` 僅保留核心規則與檔案路徑標註，可實現「按需讀取」。這能讓單次對話的基本 Token 消耗從 5,000 降至 500 左右。

## 使用方法 / 快速啟動
1. **建立獨立規範檔**：將特定任務的詳細步驟（例如 Bug Fix 8 步驟）移至 `~/.claude/skills/` 或 `docs/` 目錄下的獨立 Markdown 檔案。
2. **瘦身核心檔案**：將 `CLAUDE.md` 內容限制在 500 Token 內，僅保留最重要的全局規則。
3. **路徑標註**：在 `CLAUDE.md` 中使用路徑標註指示 AI，例如：「Bug Fix：見 ~/.claude/skills/bugfix.md」。
4. **觸發讀取**：當使用者下達相關指令（如「幫我解 bug」）時，AI 才會根據路徑讀取詳細規範。

## 對派哥的啟示（必填：跟現有工作/專案的具體連結，派哥住台灣，做自動化 AI 工具）
派哥目前在 `/Users/kuochengchen/Documents/MyClaude` 專案中已經建立了 `skills/` 資料夾，內含 `video-summary.md`、`cathay.md` 與 `hsbc.md` 等模組化規範。接下來應優化根目錄的 `CLAUDE.md`（或專案引導規則），不要在裡面寫死所有處理信用卡的細節，而是明確註記「處理國泰帳單請參考 skills/cathay.md」。這樣在處理日常自動化腳本開發時，AI 就不會每次都載入無關的財務處理規則，能有效節省派哥開發自動化 AI 工具的 API 成本，並提升 AI 遵循台灣特定金融格式（如國泰、匯豐）的準確性。

## 連結筆記
## 連結筆記
- [[boris-15-claude-code-tips]]
- [[boris-parallel-claude-workflow]]
- [[claude-code-feature-workflow]]
- [[claude-code-powerup-guide]]
- [[claude-code-token-saving-strategies]]
