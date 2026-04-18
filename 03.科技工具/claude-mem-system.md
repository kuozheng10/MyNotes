---
title: Claude-mem：Claude Code 的持久化記憶與語義檢索系統
tags: ["AI", "Claude Code", "知識管理", "自動化"]
date: 2026-04-19
category: 開發工具
source: goodarticle/2026-04-19_claude-mem_記憶系統.md
---

## 這是什麼
claude-mem 是專為 Claude Code 打造的持久化記憶壓縮系統，能自動捕獲開發過程中的工具使用觀察並生成語義摘要，讓 Claude 在不同對話會話（Session）間保持知識連續性。

## 核心概念
- **持久化內存**：上下文跨 Session 保留，解決關閉終端後開發脈絡消失的問題。
- **漸進式披露（Progressive Disclosure）**：採用分層記憶檢索機制，在維持背景完整度的同時優化 Token 成本與可見性。
- **混合儲存架構**：利用 SQLite 儲存結構化資料（Sessions、摘要），並結合 Chroma 向量資料庫實現混合語義與關鍵詞搜索。
- **生命週期鉤子**：透過 5 個關鍵節點（SessionStart, PostToolUse 等）實現自動化操作，無需人工干預即可更新記憶。
- **隱私控制**：支援使用 `<private>` 標籤排除敏感內容，確保記憶庫安全性。

## 使用方法 / 快速啟動
1. **安裝插件**：在 Claude Code 中輸入 `/plugin marketplace add thedotmack/claude-mem` 後接 `/plugin install claude-mem`。
2. **重啟生效**：重啟 Claude Code 即可激活記憶功能。
3. **語義查詢**：直接在 Claude 中呼叫 `mem-search` 技能，使用自然語言詢問：「我們上次修復了哪個 bug？」或「Authentication 是如何實作的？」
4. **即時監控**：開啟瀏覽器訪問 `http://localhost:37777` 即可實時查看當前的記憶流與摘要狀態。

## 對派哥的啟示
1. **跨專案開發連續性**：派哥目前維護多個自動化工具（如 `cc_processor` 財務處理、`notion_todo` 等），利用此系統可以讓 AI 記住不同專案間的依賴邏輯與開發約定，避免每次切換專案都要重新讀取 README。
2. **自動化日誌摘要**：系統採用的生命週期鉤子機制，可以應用在派哥的 `telegram_bot_monitor` 或銷售報告處理中，將大量的操作 Log 自動壓縮成「重點摘要」，存入 SQLite 中供後續 RAG 檢索。
3. **個人知識工程 RAG 化**：參考其結合 SQLite + Chroma 的架構，派哥可以為自己的 Obsidian 筆記庫建立一套類似的「開發觀察者」，自動記錄在終端機執行的指令與結果，實現真正的「自動化二樓大腦」。

## 連結筆記
## 連結筆記
- [[claude-code-powerup-guide]]
- [[claude-routines-automation]]
- [[claude-handover-skill-memory]]
- [[claude-code-token-saving-strategies]]
- [[boris-15-claude-code-tips]]
