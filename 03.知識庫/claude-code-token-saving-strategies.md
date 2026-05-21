---
title: Claude Code 節流與 Token 優化策略實戰
tags: ["Claude Code", "AI", "工具", "自動化"]
date: 2026-04-19
category: AI工具
source: goodarticle/2026-04-19_Claude_Code_節流策略.md
---

## 這是什麼
本文介紹在使用 Claude Code 開發環境時，如何透過優化系統指令、善用快取機制以及搭配特定的 Skills/MCP 工具，有效降低 Token 消耗並提升回應效率的實作指南。

## 核心概念
- **配置模組化**：避免將所有規則塞入 `CLAUDE.md`，採用「按需讀取」策略降低每輪對話的基礎 Token 消耗。
- **跨語言效能優化**：利用英文在 Token 計算上的優勢編寫核心邏輯，僅在輸出端保留繁體中文。
- **快取完整性維護**：透過穩定的 Session 與環境配置保護 Prompt Cache，節省高達 76% 的推論成本。
- **輸出入雙向壓縮**：導入 Caveman Skill 精簡輸出廢話，並使用 Toonify MCP 預處理長文件以減少輸入量。

## 使用方法 / 快速啟動
- **精簡 CLAUDE.md**：僅保留 5 條核心規則，其餘規範使用路徑標註（如 `測試規範：見 docs/testing.md`）。
- **指令習慣**：完成任務後執行 `/clear` 清空上下文，或在對話過長時使用 `/compact` 壓縮記憶。
- **Prompt 設計**：將 System Prompt 核心轉為英文，並在末尾加入 `Respond in Traditional Chinese`。
- **工具啟用**：在處理大型文件前先執行 Toonify 進行預縮，或開啟 `/caveman` 模式節省輸出成本。

## 對派哥的啟示
- **開發成本控管**：派哥在台灣開發 AI 自動化工具時，應將現有的後台 SOP（如信用卡處理、銷售報表邏輯）全面英文話，僅在 Telegram 機器人前端與使用者互動時採用繁體中文，可直接砍掉約 40% 的輸入成本。
- **專案結構優化**：目前 `cc_processor` 目錄下有多個銀行模組，應將各銀行的解析規則分開存放，並在 `CLAUDE.md` 中僅指引路徑，避免每次分析 Cathay 帳單時都讀入 HSBC 的解析規則。
- **快取應用於日常**：在開發 Telegram Bot 或處理重複性財務數據時，盡量保持在同一個對話 Session 中，利用 Prompt Cache 縮短回應時間，讓自動化流程更流暢。

## 連結筆記
## 連結筆記
- [[boris-15-claude-code-tips]]
- [[claude-code-powerup-guide]]
- [[claude-routines-automation]]
- [[claude-code-feature-workflow]]
- [[claude-code-subagent-environment]]
