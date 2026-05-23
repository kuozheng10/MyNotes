---
title: 知識管理工具演進：從 Tags 到 LLM Wiki，以及 SSOT 的根本限制
tags: [知識管理, PKM, LLM, Wiki, Obsidian, 向量搜尋, Karpathy, Cairn, SSOT]
date: 2026-05-23
category: 科技工具
source: AILogora/Cairn 創辦人觀察
---

## 五種知識組織方式（底層機制分類）

| 方式 | 代表工具 | 核心邏輯 | 問題 |
|------|---------|---------|------|
| **Flat 分類** | Notion, Confluence, PARA | 資料夾 + 標籤 | 東西一多就找不到，一篇筆記放哪都不完全對 |
| **雙向連結** | Roam, Obsidian, Logseq | [[link]] 讓結構自己長出來 | 幾百張後 graph 變毛線球，看不出哪個重要 |
| **空間化** | Heptabase | 無限白板，位置代表關聯 | 白板太大後還是需要「地圖」導航 |
| **語意搜尋** | Mem.ai, Glean, Notion AI | Vector embedding，語意相似度 | 找到的是「最相關段落」，不是有脈絡的 map |
| **LLM 編纂** | Karpathy LLM Wiki | LLM 持續維護 Markdown Wiki | 目前仍是單一視角整理，不同觀點被壓成一版 |

---

## Karpathy LLM Wiki 架構

三層設計：
- **Raw**：原始資料不動
- **Wiki**：LLM 生成的 Markdown 頁面，持續更新
- **Schema**：一份 CLAUDE.md 定義維護規則

LLM 不是拿來問答（RAG），是拿來**持續編纂**。
→ 1600 萬觀看，GitHub Gist 幾天 5000 星

LLM Wiki 的 graph 跟 Obsidian/VectorDB 的 graph 本質不同：
- Obsidian graph：誰連了誰
- VectorDB graph：誰跟誰相似
- **LLM Wiki graph：概念的語意層級**（這個屬於那個主題、這個 evidence 支持那個 claim）

---

## 核心問題：SSOT 的根本限制

> 大多數工具很擅長保存**內容**，卻不擅長保存**觀點之間的形狀**。

當三個人說「RAG 很有效」，一個人說「RAG 在我這裡一直 hallucinate」：
- 現有系統只能：平均成一個結論 / 挑最新版本 / 當相似段落處理
- 真正有價值的是：**誰在什麼 context 成功，誰在什麼條件失敗**

**例外（做得比較好的）：**
- Wikipedia NPOV：按來源顯著性比例呈現主要觀點，但 authorship/evidence 還是被抹平
- Discourse Graphs（Protocol Labs）：把研究拆成 claim、evidence、question，保留 authorship

**替代概念：Single Source of Change**
→ 不是死守 SSOT，而是保留一個統一決策和傳播的控制點，允許數據活在多個地方

---

## Cairn 的方向

不是又一個 AI Wiki，也不是幫 LLM 記住單一 user 的 memory layer。

**目標：讓多個 contextual truth 共存、保留它們之間的關係。**

背景：AILogora → Cairn，從 LLM Wiki 驗證可行，但碰到「不同人的不同經驗被 Wiki 吃掉」的問題。

---

## 對派哥的關聯

- 你的 MyNotes（Obsidian）目前是「Flat + 雙向連結」的混合
- GBrain 加入了 Vector 搜尋層
- 你的 CLAUDE.md 定義維護規則，其實就是 Karpathy 三層架構的 Schema 層
- 缺的是：**多視角/矛盾觀點的保存**（你的筆記都是一個整理版本）

---

## 相關筆記

- [[aliang-three-swords-leveraged-etf-strategy]] — 同樣是「知道這個工具在幹嘛才能用對」的思路
