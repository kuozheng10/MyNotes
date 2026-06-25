---
tags: [rag, llm, local-llm, knowledge-base, pdf, agent, qdrant, fastapi, react, privacy]
source: 社群分享（LinkedIn #RAG #AI #知識庫 #地端部署）
github: https://github.com/myyang19770915/Hybride_pageindex_RAG
date: 2026-06-26
---

# 私有化 AI 知識庫實作 — Hybride PageIndex RAG

> **適用場景**：公司 SOP / 規格書 / 操作手冊資料多，又不能把文件丟上雲端 AI → 地端 PDF 問答系統。
> **核心賣點**：資料不出門、有推理能力、每句有出處頁碼。

---

## 技術架構

| 元件 | 技術 | 說明 |
|------|------|------|
| 後端 API | FastAPI | Python 框架 |
| 前端 | React 19 | 聊天介面 + 串流 |
| Agent 框架 | Agno | 自主代理，混合檢索 |
| 向量資料庫 | Qdrant | 語意搜尋 |
| 結構資料庫 | PostgreSQL | 對話歷史、文件索引 |
| PDF 解析 | MinerU | 含表格、公式、雙欄排版 |
| 本地 LLM | LM Studio | 跑在 RTX 5090，完全離線 |
| 索引方法 | PageIndex | 章節樹結構索引 |

---

## 五個關鍵功能

### 1. PDF 解析 — MinerU
- 自動解析 PDF → 抓表格、數學公式、圖片說明
- 將文件拆成「章節樹」建立索引
- 支援掃描檔、雙欄排版
- 附互動測試台：可切換解析引擎 / 語言 / 公式開關，比較不同 PDF 的解析效果

### 2. 混合檢索 Agent（非關鍵字比對）
流程：
```
問題輸入
  → 向量語意搜尋 + 關鍵字搜尋（混合）
  → 鎖定最相關章節
  → 回資料庫撈出原文
  → 根據真實原文作答
```
不是直接用嵌入片段回答，而是先定位、再取原文，減少幻覺。

### 3. 頁碼引用 + 原文對照
- 每則回答附頁碼引用
- 點擊可跳到原文那一頁對照
- 防止 AI 「一本正經地胡說八道」

### 4. 誠實邊界
- 查無資料 → 老實說「查不到」，不硬編答案
- 問題模糊 → 主動反問補充條件
- 對企業應用尤其重要（不能給假答案）

### 5. 對話體驗
- 逐字串流回答
- 記得上下文（可追問「那它的限制呢？」）
- 左側歷史對話可切換
- 可展開「思考過程」，看 AI 每步呼叫了哪些工具

---

## 和其他 RAG 方法的比較

| 方法 | 特色 | 限制 |
|------|------|------|
| 傳統向量 RAG | 快、便宜 | 碎片化，缺乏全局理解 |
| LLM Wiki（Karpathy）| 全局觀、關聯推理 | 入庫時 token 消耗高 |
| **Hybride PageIndex RAG** | 章節樹索引 + 混合檢索 + 撈原文 | 需要本地 GPU 硬體 |

→ 相關筆記：[[llm-wiki-karpathy-rag-2026-06]]

---

## 適合誰用

| 場景 | 說明 |
|------|------|
| 企業 SOP 問答 | 不想把內部文件傳雲端 |
| 技術規格書查詢 | 文件多、需要精準引用 |
| 客服知識庫 | 答案有出處，降低錯誤風險 |
| 研究文獻整理 | 跨論文推理、追問 |

---

## 延伸資源

- PageIndex 索引方法：https://github.com/VectifyAI/PageIndex
- MinerU PDF 解析：https://github.com/opendatalab/mineru
- 作者 GitHub（可能開源）：https://github.com/myyang19770915/Hybride_pageindex_RAG

---

## 派哥評估

**有沒有用**：有參考價值。
- 如果未來 MyClaude 的筆記量大到 Obsidian 搜尋不夠用，這套架構可以參考
- 本地 LLM 的門檻（需要 GPU）目前不適合 Mac mini M4，但 Qdrant + FastAPI 部分可以跑在本機
- 重點是「混合檢索後撈原文再回答」的設計，比純向量 RAG 準確
