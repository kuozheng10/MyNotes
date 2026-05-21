---
title: 從 Prompt 到系統化：NotebookLM 與 Gemini 的知識複利實作指南
tags: ["AI", "知識管理", "工作流程", "Google"]
date: 2026-04-17
category: 知識管理
source: goodarticle/2026-04-17_NotebookLM-Gemini文獻探究實作指南.md
---

## 這是什麼
這是一份關於如何從破碎的 Prompt 對話轉向系統化 AI 設定的實作指南。透過結合 NotebookLM 的自訂功能與 Gemini Gem，建立一個能持續累積、跨文獻整合的研究系統，以實現知識複利。

## 核心概念
*   **脫離遊牧模式**：反對每次對話都重新輸入 Prompt，主張將分析邏輯內置於系統設定中。
*   **三層進化階段**：
    *   **Level 1 (遊牧)**：重複複製貼上指令，缺乏效率與累積。
    *   **Level 2 (定居)**：使用 NotebookLM 處理單一專案，但資訊無法跨筆記本互通。
    *   **Level 3 (系統化)**：結合 NotebookLM 的深度角色設定與 Gemini Gem 的跨來源處理能力。
*   **初期投資心法**：花一小時建立完善的六層分析結構（理論、方法、論證、溯源、CIMO 等），能為後續研究節省數百小時的重複勞動。

## 使用方法 / 快速啟動
1.  **結構化角色設定**：在 NotebookLM 的「自訂指令」中，預設好深度的分析框架（如：要求 AI 必須分析文獻的 CIMO 機制或理論貢獻）。
2.  **跨筆記本整合**：利用 Gemini Gem 的功能，將多個 NotebookLM 的輸出作為輸入源，進行橫向的「缺口識別」與「矛盾對比」。
3.  **一次性設定**：將研究員的專業素養（Schema）寫入系統層級，確保每一次的新對話都站在前人的肩膀上。

## 對派哥的啟示
*   **技能模組化 (Skills as Assets)**：派哥目前在 `skills/` 資料夾中維護了如 `cathay.md`, `hsbc.md` 等規則，這正符合文章中「系統設定」的精神。未來可以進一步將這些規則整合成一個「財務處理 Gem」，讓 AI 在處理不同銀行帳單時，自動套用一致的會計邏輯與分類標準。
*   **跨專案知識庫**：派哥目前的 `cc_processor` 和 `notion_todo` 是獨立的。可以參考文章的「雙璧系統化」，建立一個「派哥自動化架構知識庫」，讓 AI 在撰寫新的 `taishin_ocr.py` 時，能參考舊有 `fubon.py` 的架構優點與踩過的坑。
*   **台灣在地自動化優化**：利用這套系統化思維，可以將台灣特有的發票制度、信用卡點數機制寫入 NotebookLM 的底層設定，讓 AI 在摘要財務資訊時，能主動識別出最適合台灣使用者的優惠路徑，而不僅僅是字面翻譯。

## 連結筆記
## 連結筆記
- [[claude-notebooklm-mcp-5scenarios]]
- [[claude-handover-skill-memory]]
- [[boris-parallel-claude-workflow]]
- [[claude-routines-automation]]
- [[claude-project-management-best-practices]]
