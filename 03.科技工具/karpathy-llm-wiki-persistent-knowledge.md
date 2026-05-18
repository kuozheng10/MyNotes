---
title: Karpathy LLM Wiki：持續累積的知識工件與 AI 開發鏈
tags:
  - karpathy
  - llm
  - knowledge-base
  - rag
  - agent
  - workflow
date: 2026-05-18
category: AI策略
---

## 核心概念

Karpathy 提出的 LLM Wiki 模式：不再每次查詢都從原始文件重新推導，而是讓 LLM 維護一個**持續累積、不斷複利的知識工件（wiki）**。

> "The wiki is a persistent, compounding artifact"

這是 RAG 的根本升級：RAG 每次查詢都重新發現知識，LLM Wiki 讓知識隨時間增長。

原始資料：https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

---

## 三層架構

```
Raw Sources（不可變）
    ↓ 一次性餵入
The Wiki（LLM 擁有、LLM 寫）
    ↑ 你讀；LLM 寫
The Schema（配置文件）
    → 定義 wiki 結構、規範、工作流程，讓 LLM 成為「守紀律的 wiki 維護者」
```

### 兩個特殊索引檔案

- `index.md`：內容導向的目錄（content catalog）
- `log.md`：追加式時間序列紀錄（parseable prefixes）

---

## 三個操作

### Ingest（攝入）
一個 source → 觸及 10～15 個 wiki 頁面（摘要、交叉引用更新）

### Query（查詢）
對 wiki 提問；好的答案成為新頁面，持續複利知識

### Lint（健檢）
定期掃描：矛盾點、過時聲明、孤兒頁面、缺失交叉引用

---

## AI 完整開發鏈（延伸應用）

Karpathy 概念啟發的完整循環：

```
spec
  ↓ AI 讀 spec → 寫 design
design
  ↓ AI 讀 design → 寫 code
code
  ↓ AI 讀 code → 寫 test script
test script
  ↓ AI 執行 → 生出 log
log
  ↓ AI 讀 log → 辨識 issue
issue
  ↓ AI 生出 SOP
SOP
  ↓ AI 根據 SOP debug → 發現 bug → 修正 design
  ↓ 重複循環
```

這條鏈的關鍵：每個環節的輸出都是下一個環節的輸入，LLM Wiki 讓每個產出物都被累積、不消失。

---

## 社群實作與批評

### 主要批評（jazzonenl）
- 任何單一改動觸發幾十個連結更新 → SQL 是毫秒，LLM wiki 是多次模型呼叫
- Link integrity 在規模化時降解
- 時間盲點（vector search 無時序）
- 結論：需要「AI-Native Database」結合 SQL 嚴謹性 + LLM 語意

### 值得關注的實作

| 專案 | 特色 |
|------|------|
| ΩmegaWiki (640+ stars) | 23 個 Claude Code skills、9 種 typed entities/edges、雙語 |
| SwarmVault v3.14 | 一鍵啟動 `swarmvault quickstart ./my-project` |
| expo-llm-wiki | SQLite 後端、三層記憶（Facts / Working Memory / Wisdom）|
| DPC Messenger | Git-inspired 知識圖、邊緣層級 provenance tracking、編譯管道而非即時寫入 |
| wikova.com | 公開示範、自動化 research + curation + self-healing lint loop |

### 演化方向

- **Typed knowledge graphs**：結構化關係，不只 markdown
- **Sleep cycles**：背景記憶整合
- **Claim-centric**：聲明為基本單位，引用頻率決定權重
- **微型神經網路**：50～100M 參數模型把語料存在權重裡，透過 ROME/MEMIT 更新

---

## 對派哥的參考點

派哥現有系統對應：

| LLM Wiki 概念 | 派哥對應 |
|-------------|---------|
| Raw Sources | 文章、TG 訊息、PDF |
| The Wiki | MyNotes（GitHub） |
| Schema | CLAUDE.md + skills |
| Ingest | 跑 SOP → 存 MyNotes |
| Query | 問知識庫 |
| Lint | 跑健檢 |
| log.md | session-YYYY-MM-DD.md |

缺口：MyNotes 目前沒有 `log.md`（追加式時間紀錄）和自動 Lint（掃矛盾）

→ 參見 [[llm-wiki-blog-compilation-three-steps]]、[[llm-wiki-v2-memory-mechanism]]、[[vault-for-llm-self-convergence-knowledge]]
