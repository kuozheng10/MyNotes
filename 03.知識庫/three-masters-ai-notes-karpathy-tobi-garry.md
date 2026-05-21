---
title: 三位大師的 AI 筆記系統 — Karpathy / Tobi Lütke / Garry Tan 比較
tags: [知識管理, llm-wiki, 第二大腦, karpathy, obsidian, 必學]
date: 2026-04-11
category: AI工具
---

## 三位大師一句話

| 大師 | 比喻 | 核心問題 |
|------|------|----------|
| **Karpathy** | 羅盤 | 你的知識有沒有在長？ |
| **Tobi Lütke** | 望遠鏡 | 你找不找得到？ |
| **Garry Tan** | 營運系統 | 你能不能每天自動變聰明？ |

---

## Andrej Karpathy — LLM Wiki

**背景**：深度學習教育者，CS231n、Tesla Autopilot、OpenAI、Eureka Labs。

**核心洞見**：
> 好檢索不如好編纂 — 知識要在多次對話與多份來源中被寫進結構，而不是每次從零拼湊。

**做法**：
- 不可變原始資料當地基
- LLM 維護一層持久性 wiki（摘要、概念、交叉引用）
- 用 schema（CLAUDE.md / AGENTS.md）約束「怎麼攝入、怎麼查詢、怎麼健檢」

**適合**：個人研究者、長期主題深讀、數十到數百頁規模。

---

## Tobi Lütke — QMD（Query Markup Documents）

**背景**：Shopify CEO，複雜系統收斂成可擴展架構。

**做法**：
- 裝在本機的混合搜尋引擎：BM25 + 向量語意 + 查詢擴展 + 重排序
- 盡量用本地 GGUF 模型完成，零雲端 API
- 支援 AST 感知分塊（程式碼庫），可 MCP 整合

**適合**：工程師、離線/敏感資料、已有大量檔案但不想上雲的人。

---

## Garry Tan — GBrain

**背景**：YC 總裁，萬級 Markdown + 千級人物檔 + 多年日曆轉錄。

**做法**：
- 頁面模型 = compiled truth（當前最佳論述）+ timeline（只增不刪的證據鏈）
- Postgres + pgvector + 關鍵字 + RRF 混合檢索
- 知識隨訊號進場自動更新，Agent 可讀寫

**適合**：人脈/公司/交易高密度工作者，資料量讓 grep 失效的人。

---

## 對派哥的對照

**MyNotes = Karpathy 路線，已在做對的事。**

| Karpathy 問 | 派哥現狀 |
|-------------|----------|
| 知識有沒有在長？ | ✅ 有，SOP 每次存 MyNotes + git push |
| 有沒有 schema？ | ✅ CLAUDE.md + AGENTS.md 定死規則 |
| LLM 有沒有幫維護？ | ✅ 健檢腳本（Gemini 找矛盾/缺漏） |

**未來升級方向：**

| 當 MyNotes 長到… | 考慮加入 |
|-----------------|----------|
| 搜尋靠記憶力跟不上 | Tobi 的 QMD（本機混合搜尋）|
| 人物/公司/交易追蹤需求 | Garry 的 Postgres + timeline 結構 |
| 現在（<100 個筆記） | 維持現狀，Karpathy 路線足夠 |

---

## 連結筆記
- [[llm-knowledge-base-karpathy]] — Karpathy LLM 知識庫原始筆記
- [[obsidian-llm-knowledge-management]] — Obsidian × LLM 知識管理
- [[mempalace-ai-agent-memory]] — AI Agent 記憶管理
- [[qa-learning-roadmap]] — 知識庫學習路線圖
