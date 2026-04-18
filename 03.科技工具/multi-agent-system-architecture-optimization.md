---
title: 為什麼多代理人團隊越跑越偏？從層級式到平行架構的實作思考
tags: ["AI", "Agent", "架構設計", "工作流程"]
date: 2026-04-18
category: 系統架構
source: goodarticle/2026-04-17_為何代理團隊越跑越偏.md
---

## 這是什麼
本文探討在建構多代理人（Multi-Agent）系統時，採用傳統層級式「CEO 模式」所面臨的資訊傳遞誤差與效能瓶頸，並分享轉向「C-level 平行架構」的實作經驗。

## 核心概念
*   **資訊傳遞衰減**：在層級架構中，指令每經過一層 Agent 轉述，就會產生二次偏誤。Agent 會用「推測」來補足資訊缺口，導致最終執行偏離原始需求。
*   **單點瓶頸與 Context 限制**：Supervisor 模式容易面臨 Context 無法有效共享的問題，這也是目前 AI 社群（如 Claude vs. Devin 團隊）爭論的核心。
*   **C-level 平行模式**：將任務直接指派給職責明確的專業 Agent（如 CPO、COO、CTO），縮短指揮鏈至多僅保留一層 sub-agent。
*   **橫向協作機制**：允許 Agent 之間直接進行溝通（例如透過 Discord 互相 mention），減少人類介入或中心節點轉述的負擔。

## 使用方法 / 快速啟動
1.  **扁平化設計**：重新設計 Agent 職責，取消「總管型」Agent，改為多個領域專家 Agent 平行運作。
2.  **明確職責邊界**：確保每個 Agent 負責的範疇互不重疊，減少決策模糊地帶。
3.  **建立通訊協定**：在系統中實作 Agent 間的直接溝通管道，讓它們能自行交換執行所需的 Context。

## 對派哥的啟示
在開發 OpenClaw 的過程中，隨著自動化流程（如 Gmail、Notion、財務、旅遊）增加，應避免設計一個「萬能調度 Agent」來分配工作。針對派哥的工具集，可以將「財務計算」、「資訊彙整」與「通訊發送」設計成平級的專業模組，並讓它們直接存取共享的 Workspace 狀態或資料庫。這樣能避免因層層指令傳遞而導致的自動化失效，特別是針對複雜的台灣在地金融或生活資訊處理，精準的職責切割比強大的主管 Agent 更加可靠。

## 連結筆記
## 連結筆記
- [[ai-agent-modular-architecture]]
- [[ai-agent-system-design-over-prompt]]
- [[claude-subagent-context-management]]
- [[claude-code-feature-workflow]]
- [[boris-parallel-claude-workflow]]
