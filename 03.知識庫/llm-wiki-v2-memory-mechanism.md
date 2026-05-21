---
title: LLM Wiki v2：仿生 AI 記憶更新與遺忘機制
tags: ["AI", "知識管理", "工作流程", "LLM"]
date: 2026-04-19
category: 知識管理
source: goodarticle/2026-04-19_Wiki記憶更新機制.md
---

## 這是什麼
這是一套針對 Karpathy LLM Wiki 框架的進階改進方案，透過模仿人類記憶的四層結構（工作、情節、語意、程序），解決 AI 長效記憶中資訊冗餘、過時與雜訊堆積的問題。

## 核心概念
- **四層記憶模型**：
    - **工作記憶 (Working memory)**：當下對話的即時資訊，隨對話結束清除。
    - **情節記憶 (Episodic memory)**：過去事件、操作與決定的歷史紀錄。
    - **語意記憶 (Semantic memory)**：從情節記憶中反覆出現、沉澱出來的穩定知識。
    - **程序記憶 (Procedural memory)**：已內化的自動化 SOP 與偏好，無需思考即可執行。
- **記憶流向機制**：資訊從事件進入情節記憶，經由重複驗證後沉澱為語意記憶，最終轉化為程序記憶。
- **信心分數與遺忘**：每條記憶具備評估分數，新資訊可動態覆蓋信心值低的舊資訊，並透過遺忘機制過濾長期未使用的噪音。

## 對派哥的啟示
- **優化財務處理邏輯**：派哥在維護 `cc_processor`（如 Cathay, HSBC 帳單處理）時，可將特定消費的分類決策從「工作記憶」提煉為「程序記憶」，讓 AI 在多次處理後自動形成固定的分類 SOP。
- **智慧化 Telegram 機器人**：為 `telegram_bot` 加入「情節記憶」，讓機器人能記住使用者過去一週的特殊指令或偏好，並在重複發生時自動更新為語意知識，提升助手感。
- **專案技能文件更新**：目前的 `skills/` 資料夾（如 `video-summary.md`）可以導入「信心分數」概念，當開發工具（如 Claude Code 或 API）更新時，自動識別並覆蓋舊有的操作說明，避免 Claude 讀取到過時的背景資訊。

## 連結筆記
## 連結筆記
- [[claude-project-management-best-practices]]
- [[claude-mem-system]]
- [[boris-parallel-claude-workflow]]
- [[claude-routines-automation]]
- [[claude-handover-skill-memory]]
