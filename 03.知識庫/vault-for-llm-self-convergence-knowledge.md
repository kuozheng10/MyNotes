---
title: Vault-for-LLM：會自己判斷「學夠了沒」的知識庫
tags: ["RAG", "知識管理", "Agent", "開源", "LLM"]
date: 2026-04-22
category: AI工具
source: https://github.com/zycaskevin/Vault-for-LLM
---

## 這是什麼

Vault-for-LLM v0.4.0，開源知識引擎。核心突破：在傳統 RAG 基礎上加了「自問收斂」——知識不是你以為學完了就算數，是系統自己判斷能解釋才算完成。

安裝：`pip install -e . && vault init && vault compile`
不需要 GPU、Docker、雲端帳號。SQLite + ONNX，一台筆電可跑。

## 七個升級

### 1. 自問收斂（convergence_check.py）

學完主題後自動生成問題，答不出標記「未收斂」，下次排程繼續補。是系統通過自問才算數，不是人覺得夠就夠。

### 2. 跨家族 LLM 驗證（cross_validate.py）

用不同模型交叉驗證——同一個模型自己查自己等於考生自己改考卷。可指定任意兩個模型做交叉驗證。

### 3. 原子主張 + 來源標註

Citation 從 chunk 級下沉到 claim 級。每條主張綁 `source_span`，精確到原文哪一段，可點回來源。

### 4. 鮮度追蹤 + FSRS 間隔重複（freshness_check.py）

自動偵測過時知識，結合 FSRS 間隔排程——快忘的時候提醒複習，跟背單字卡邏輯相同。

### 5. 圖譜擴展檢索

搜尋沿知識圖譜走兩步。搜 vLLM，不只回 vLLM 筆記，還帶出 GPU memory、Qwen 相關。走出來的東西經常是你不知道自己需要的。

### 6. MCP 伺服器

任何 MCP 相容 AI Agent 可直接查知識庫、注入新知識。聊天中覺得某技術不錯，直接讓它學進去，不用複製貼上。

### 7. Precision-first 策略

選 Gemma 不選 Qwen：Precision 93.5%、Recall 50.3%。知識場景「說錯比少說嚴重」，寧可少提取一條，也不要提錯一條。

## 踩坑教訓

同步開源版前多跑了全目錄掃描，發現兩條 `/home/zycas` 硬編碼路徑藏在測試檔案裡。差點把家目錄路徑暴露到 GitHub。

教訓：掃描只認 pattern，不認語義。同步流程要兩次確認：自動掃描 + 人工覆核。

## 質疑

- 前提假設：「自問收斂」的問題品質取決於 LLM 自己生成，如果生的問題太淺，收斂了也不代表真的學透
- 適用邊界：Precision-first 適合需要高精度的場景（Guardrails、法律、醫療），但若知識庫本身就稀疏，Recall 50% 會讓很多正確知識被丟棄
- 潛在反例：FSRS 間隔重複設計給「長期記憶」場景，對快速變動的技術文件（LLM 更新頻率），複習週期可能還沒到就已過時

## 對標

- **醫學執照考試**：「能解釋給病人聽」才算真的懂，不是背完就算——自問收斂用的是同一個標準
- **雙盲審查**：跨家族 LLM 驗證的邏輯就是學術論文的雙盲 review，讓不同背景的 reviewer 互相校正

## 對派哥的啟示

MindForge 的自問收斂思路，可以直接套用到你的 MyNotes 系統：

- 存完一篇筆記後，自動生成 3 道測驗題，答不出來就標記「需補充」
- FSRS 排程 + Telegram 提醒：30 天後提醒你複習這篇筆記
- MCP 伺服器是最可行的落地點：讓 Claude Code 在 session 中直接查 MyNotes

## 連結筆記

- [[mindforge-knowledge-engine]]
- [[mindforge-knowledge-acquisition-workflow]]
- [[graphify-code-knowledge-graph]]
- [[llm-knowledge-base-karpathy]]
- [[mempalace-ai-agent-memory]]
