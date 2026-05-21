---
title: Claude Design 實戰七招：Anthropic 設計師的 AI 協作秘訣
tags: ["AI", "Claude", "工具", "工作流程"]
date: 2026-04-19
category: AI工具
source: goodarticle/2026-04-19_Claude設計七招.md
---

## 這是什麼
這篇文章整理了 Anthropic 內部垂直團隊設計師 Ryan Mather 的實戰心得，分享他如何利用 Claude Design 同時服務 7 個產品線，將傳統冗長的設計流程壓縮至「一場會議」內完成的七大技巧。

## 核心概念
1. **建立設計基石**：先花一小時設定 Design System（顏色、字體、組件）與核心頁面，確保後續生成的視覺一致性。
2. **即時協作迭代**：在會議中直接生成 Mockup，讓溝通停留在邏輯與約束條件，而非像素細節。
3. **視覺化精確修改**：利用 Inline Comment 工具直接點選畫面標註修改，避免模糊的文字描述。
4. **生成動態展示**：讓 Claude 製作帶有交互動效的影片或 Demo，提升原型真實感。
5. **串接外部數據**：連結 Docs 或 Slack 等數據源，根據 PRD 或討論紀錄直接生成設計方案。
6. **打造專屬小工具**：不只是畫圖，而是讓 Claude 寫程式打造臨時的設計輔助工具。
7. **保留人類判斷力**：識別 AI 的邊界，在圖標、插畫與關鍵命名上投入人類的品味與打磨。

## 使用方法 / 快速啟動
* **第一步**：將現有的設計規範（如 CSS 變數或 Figma 截圖）餵給 Claude。
* **第二步**：使用 Artifacts 預覽功能，透過對話不斷調整版面。
* **第三步**：針對特定區域使用「評論」功能進行微調。
* **第四步**：將生成的 React 代碼直接整合進開發專案中。

## 對派哥的啟示
1. **UI 快速原型化**：對於派哥正在開發的信用卡處理器（`cc_processor`）或 Telegram Bot 監控介面，可以利用 Claude Design 快速產出美觀的管理後台或報表圖表，而不必深陷於 CSS 調整。
2. **與現有工具整合**：Tip 5 提到串接外部數據，這非常適合派哥的 Notion (`notion_todo.py`) 或 Google Sheets 工作流，可以直接把報表邏輯轉化為可視化的 Dashboard 設計。
3. **以程式碼為中心的設計**：因為 Claude Design 輸出的是代碼，派哥可以直接將設計成果對接到現有的 Python/JS 專案中，實現「設計即程式」的自動化流程。

## 連結筆記
## 連結筆記
- [[boris-parallel-claude-workflow]]
- [[claude-code-feature-workflow]]
- [[claude-code-powerup-guide]]
- [[claude-routines-automation]]
- [[boris-15-claude-code-tips]]
