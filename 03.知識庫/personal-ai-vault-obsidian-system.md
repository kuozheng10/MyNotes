---
title: 打造個人 AI 金庫：Obsidian + Claude 的知識系統架構
tags: ["知識管理", "AI", "Obsidian", "工作流程"]
date: 2026-04-21
category: 知識管理
source: telegram/save-sop
---

## 這是什麼

把散落的知識（Notion、瀏覽器分頁、腦海）整理進 Obsidian，建成讓 AI「認識你」的個人金庫。核心問題：每次換工具或開新對話都要從頭解釋自己，消耗極大。解法是把自己打造成「上下文」。

## 核心架構

三個參考來源整合成一套：
- **Vault for Founders**（林啟維）— 資料夾骨架：identity / context / memory / wiki / raw / skills / projects
- **LLM Wiki**（Karpathy）— 知識庫管理方法，ingest 文章 → 提煉概念
- **女媧 skill**（alchaincyf）— 把名人思維蒸餾成可呼叫的 skill

雙層記憶架構：索引層 + 內容層，記憶累積越多不會線性增加 token 消耗。

內建 skills：
- ingest — 把文章拆解進 wiki，連結既有筆記
- query — 跨頁綜合回答問題
- lint — 定期健檢整個金庫的一致性
- writing-voice — 提煉個人寫作風格
- 思維顧問 — 納瓦爾、查理芒格、馬斯克等，換視角思考

## 質疑

- 前提假設：你本身已有足夠多的輸入材料（文章、筆記、決策紀錄），才能讓 AI「認識你」；若平時沒有輸入習慣，金庫會很空
- 適用邊界：writing-voice skill 對寫作風格固定的人效果好；風格仍在探索期的人，AI 提煉出來的模板反而會限制發展
- 潛在反例：雙層記憶架構若索引設計不良，查詢時仍會 miss 掉重要內容，並不能保證 token 效率

## 對標

- **個人 CRM**：金庫讓 AI 認識你，本質上和 CRM 讓業務認識客戶是同構的——都是把關係的上下文持久化，而不是每次從頭建立
- **編譯器 vs 直譯器**：ingest 步驟是「預先編譯」，對比每次對話臨時 RAG 是「即時直譯」，前者更穩定一致（與 LLM Wiki 三步編譯法連結）

## 對派哥的啟示

MyNotes 現有架構已經是這套的子集：03.科技工具/ = wiki，save_article.sh = ingest，upgrade_to_mynotes.sh = 提煉。目前缺的：
1. writing-voice skill — 可從 MyNotes 文章中提煉派哥的寫作風格
2. identity / context 資料夾 — 目前靠 SOUL.md + CLAUDE.md，但沒有整合進 Obsidian
3. lint 健檢 skill — 可以對應「跑健檢」暗語，但尚未自動化

## 連結筆記

- [[llm-wiki-blog-compilation-three-steps]]
- [[llm-wiki-v2-memory-mechanism]]
- [[founders-ai-vault-framework]]
- [[karpathy-second-brain-workflow]]
- [[obsidian-llm-knowledge-management]]
