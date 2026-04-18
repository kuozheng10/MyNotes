---
title: 高效 SDD 文件設計：利用 Delta Spec 降低 Token 成本並精準控管系統演進
tags: ["AI", "架構設計", "工具", "工作流程"]
date: 2026-04-18
category: 系統架構
source: goodarticle/2026-04-18_高效SDD文件設計.md
---

## 這是什麼
這是一種基於 SDD（Spec-Driven Development）的進階文件設計方法，核心在於引入 OpenSpec 的 Delta Spec（增量規格）概念，解決開發過程中系統規格隨規模增長而導致的 Token 浪費與脈絡遺失問題。

## 核心概念
- **Delta Spec（增量規格）**：不生成完整的系統規格，而是只記錄「單次變更」的內容（新增、修改、移除），使文件體積與 PR 範圍對等。
- **狀態與提案分離**：將「系統現狀（Current State）」與「變更提案（Change Proposal）」分開存放，直觀呈現 Diff 差異，降低 AI 處理脈絡的難度。
- **Token 效率優化**：透過限縮 Context 範圍，大幅節省 API 消耗，並提升 AI 的回應速度與精準度。
- **漸進式文檔化**：解決「既有系統（Brownfield）難以補全文件」的心理障礙，透過一次次小規模的變更紀錄，自然形塑出完整的系統架構圖。

## 使用方法 / 快速啟動
1. **定義現狀**：在開發新功能前，先擷取受影響模組的目前狀態。
2. **撰寫 Delta Spec**：明確標註本次 PR 預計調整的邏輯、介面或資料結構。
3. **AI 開工**：餵入 Delta Spec 進行 Vibe Coding，確保 AI 只針對變更範圍進行操作。
4. **封存合併**：任務完成後，將 Delta Spec 的變更內容合併回主規格文件或作為歷史紀錄封存。

## 對派哥的啟示
- **OpenClaw 的模組化管理**：目前的 OpenClaw 專案功能日益增加（如 `self-improving-agent`、各類 `skills`），若每次修改 Skill 都重新餵入整體架構會造成嚴重 Token 負擔。應導入 Delta Spec 模式，針對單一 Skill 或特定 Gateway 進行增量更新。
- **既有自動化腳本優化**：派哥在 `myclaude/` 目錄下的多個自動化腳本（如 `morning_briefing.sh`、`payment_reminder.py`）多屬 Brownfield 狀態。利用此方法，可以從下一個功能需求開始，只針對該改動撰寫規格，不需要一次性重寫所有腳本的文件。
- **提升 AI 工具開發精準度**：身為在台灣開發自動化 AI 工具的專家，導入 Delta Spec 能讓 AI 助手（如 Claude Code 或 Gemini CLI）更專注於當前的變更任務，減少因脈絡過長而產生的幻覺或邏輯錯誤。

## 連結筆記
## 連結筆記
- [[ai-agent-modular-architecture]]
- [[ai-agent-system-design-over-prompt]]
- [[agent-skills-standard]]
- [[architecture-diagram-generator-skill]]
- [[claude-code-feature-workflow]]
