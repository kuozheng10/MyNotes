---
title: KnowDB — 給 AI Agent 看的知識資料庫：有地圖，不是只給答案
tags: [RAG, AI Agent, 知識庫, 向量搜尋, 文件結構]
date: 2026-04-29
category: AI工具
---

## 這是什麼

KnowDB 是一個專為 AI Agent 設計的知識資料庫，核心差異是保留文件的層級結構，讓 AI 像人一樣「知道自己在哪裡」，而不只是拿到一堆碎片。

Demo：https://kirisame-wang.github.io/knowdb/
Repo：https://github.com/kirisame-wang/knowdb

---

## 傳統 RAG vs KnowDB 的根本差異

**傳統 RAG 流程**：
文件切塊 → 轉向量 → 找最相近幾塊 → 交給 AI 回答

問題：AI 是被動的，沒有地圖，不知道自己在文件的哪個位置。

**KnowDB 的做法**：
- 保留標題層級結構（目錄完整呈現）
- AI 可以看目錄、走章節、往下鑽、用關鍵字跳到其他文件
- AI **知道自己在哪裡**

---

## 關鍵設計：顯性失敗 vs 靜默失敗

傳統 RAG 找不到東西時，AI 不知道——它繼續用手邊的碎片拼出「聽起來合理」的答案（幻覺）。

KnowDB 找不到時，AI 知道。**缺口是顯性的，不是靜默失敗。**

核心理念：**A map, not an answer.**

---

## 技術特點

- 早期概念原型
- 可部署在任何靜態網站，**不需要後端**
- 無需向量資料庫或額外基礎設施

---

## 對派哥的意義

- MyNotes RAG 目前用向量搜尋，是被動模式；KnowDB 的「層級導航」概念值得參考
- 靜默失敗問題：目前 `mcp__mynotes-rag__search_notes` 找不到時不會明確回報——可考慮加 fallback 提示
- 靜態部署特性適合個人知識庫場景，無運維負擔

---

## 連結筆記

- [[llm-knowledge-base-karpathy]] — Karpathy 的知識庫設計哲學
- [[notebooklm-professional-rag-limits]] — RAG 系統的侷限
- [[mindforge-knowledge-engine]] — 主動學習型知識引擎
- [[vault-for-llm-self-convergence-knowledge]] — LLM 知識收斂設計
