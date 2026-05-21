---
title: MemPalace — AI Agent 長期記憶架構
tags: [AI, Agent, 記憶管理, RAG, PKM, 向量資料庫]
date: 2026-04-08
category: AI工具
source: https://github.com/milla-jovovich/mempalace
---

## 這是什麼？

AI 的記憶系統。解決「每次開新對話，AI 就忘光之前說過什麼」的問題。

名字叫「記憶宮殿」，概念就是：不是把所有對話都存起來，而是只存**重要的事實**，需要的時候再找出來。

## 怎麼運作？

**存的時候**：把整段對話提煉成簡短的「事實」，例如：
- 「這個用戶喜歡簡短的回答」
- 「上次討論過用 Python 寫爬蟲」

**找的時候**：不是用關鍵字搜尋，而是用「語意」搜尋——問「上次那個爬蟲怎麼了」也能找到相關記憶，就算你忘了當時用什麼關鍵字。

**整理的時候**：會自動合併重複的記憶、刪掉過時的資訊，不會越堆越亂。

## 對我的用途

跟 **OpenClaw 的記憶系統**、**MyNotes 知識庫**概念類似，但更系統化。

幾個可以參考的點：
1. **筆記要提煉，不是只存原文** → MyNotes 每篇可以加「3個重點句」
2. **語意搜尋比關鍵字強** → 未來 MyNotes 可以考慮加 Embedding
3. **要定期清理，不只是新增** → 健檢功能的進化方向

## 連結筆記
- [[harness-engineering]] — 記憶是 Agent Harness 的核心部分
- [[obsidian-llm-knowledge-management]] — Obsidian 是人工版記憶宮殿
