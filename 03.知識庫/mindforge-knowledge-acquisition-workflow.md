---
title: MindForge 知識獲取與推論架構：零幻覺的六道防線
tags: ["AI", "Agent", "架構設計", "RAG"]
date: 2026-04-15
category: 系統架構
source: goodarticle/MindForge_KAL_Inference_Stack_Architecture_Diagram_Explanation.md
---

## 這是什麼
MindForge 是一個整合知識獲取迴圈（KAL）與推論棧（Inference Stack）的 AI Agent 架構，旨在透過多重驗證、蒸餾與自我反問機制，實現高精度的自動化學習與知識庫建構。

## 核心概念
*   **知識獲取迴圈 (KAL)**：透過 Brave API 搜尋並擷取資料，利用 Gemma 與 Claude 進行知識驗證，並引入「自我反問」機制，若理解程度不足則自動觸發重新學習，確保知識攝取的深度。
*   **多層儲存架構**：區分 Raw 原文、Wiki 蒸餾內容與 Schema 控制層，並使用 pgvector (HNSW 1024d) 向量資料庫進行高效能的語意檢索。
*   **高效推論技術棧**：採用 DGX Spark 硬體運行 Gemma 26B，結合 BGE-M3 Embedding 與 BGE Reranker v2 進行重排序（Reranking），最後由 Claude 擔任純驗證角色，構建「零幻覺六道防線」。

## 使用方法 / 快速啟動
1. **輸入來源**：於 MindForge 介面輸入 GitHub 連結或目標 URL。
2. **啟動學習**：點擊 "Learn" 觸發 KAL 迴圈，系統自動執行搜尋、蒸餾、驗證與向量存儲。
3. **推論查詢**：透過 Inference Stack 進行問答，系統會自動執行檢索、重排序與最終驗證。

## 對派哥的啟示
*   **強化 Agent 的自我稽核**：派哥在台灣開發 `claude-telegram` 等自動化工具時，可導入「自我反問」機制。在 Agent 執行任務或更新 Notion 資料庫前，先進行一步邏輯檢核，能大幅提升自動化流程的穩定性。
*   **精細化的 RAG 架構**：目前派哥處理 Telegram 碎片化訊息時，可參考此架構引入 Reranker（如 BGE Reranker）與多模型交叉驗證（Gemma + Claude），這對降低知識管理系統的幻覺至關重要。
*   **模組化知識處理**：將原始訊息 (Raw) 與精煉知識 (Distilled Wiki) 分開儲存，並配合明確的 Schema 管理，有助於派哥在擴展不同頻道的自動化工具時，維持高品質的長短期記憶。

## 連結筆記
## 連結筆記
- [[ai-agent-modular-architecture]]
- [[ai-agent-system-design-over-prompt]]
- [[claude-notebooklm-mcp-5scenarios]]
- [[gbrain-garry-tan-memory-system]]
- [[full-agent-dev-ecosystem-goatwang]]
