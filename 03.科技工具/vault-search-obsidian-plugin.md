---
title: Vault Search — Obsidian 本地語意搜尋 Plugin
tags: [Obsidian, 知識管理, LLM, 工具, 隱私, 自動化]
date: 2026-04-09
category: 知識管理
source: https://github.com/notoriouslab/vault-search
---

## 這是什麼

Obsidian plugin，用 Ollama 做本地語意搜尋。全部在本機跑，不上雲、不付費、筆記不外傳。輸入概念就算用詞不同也找得到（語意搜尋 + 同義詞擴展）。

推薦模型：`qwen3-embedding:0.6b`，對中英混合 vault 特別友善。

---

## v0.3 核心功能

| 功能 | 說明 |
|------|------|
| 語意搜尋 | 概念搜尋，不是關鍵字，同義詞自動補 |
| 相似筆記 | 開啟任一篇，零延遲顯示相關筆記（純向量運算） |
| **主動發掘** | 打開筆記→側欄自動顯示冷門相關筆記（v0.3 新） |
| **全域發掘** | 一鍵找出「最被遺忘但值得看的筆記」（v0.3 新） |
| **MOC 生成** | 搜尋/發掘結果一鍵匯出為 Map of Content（v0.3 新） |
| **Canvas 拖拉** | 結果直接拖到畫布做視覺整理（v0.3 新） |
| Hot/Cold 分層 | 有連結/近期=Hot；孤立=Cold；Discover 挖 Cold |
| LLM 摘要 | 本地 LLM 自動生成 description，提升搜尋精準度 |
| 智慧分段 | 長文自動切重疊片段，長筆記內容不被埋沒 |
| 多後端 | Ollama、LM Studio、llama.cpp、vLLM、任何 OpenAI-compatible |

8GB 筆電跑得動，增量索引，日常幾乎零負擔。

---

## 安裝

目前等 Obsidian plugin 社群審查，先從 GitHub 手動安裝：
```
https://github.com/notoriouslab/vault-search
```

---

## 對派哥的啟示

- **MyNotes 最直接的補強**：現在找筆記只能 grep 關鍵字，語意搜尋可以找到「概念相關但用詞不同」的筆記
- **「全域發掘」= 跑健檢的視覺化版本**：找出被遺忘的 Cold 筆記，跟 mynotes.md 的健檢標準互補
- **Hot/Cold 分層** 可識別孤立筆記（健檢標準之一）
- **MOC 生成** 可以快速建立主題索引（補強 00.索引/ 資料夾）
- 配合 doc-cleaner 先把文件清成乾淨 Markdown，再入庫效果更好

---

## 連結筆記
- [[obsidian-llm-knowledge-management]] — Obsidian 知識管理整體架構
- [[llm-knowledge-base-karpathy]] — raw → wiki 編譯概念（Vault Search 是查詢層）
- [[mempalace-ai-agent-memory]] — AI 記憶管理，語意搜尋是其中一層
