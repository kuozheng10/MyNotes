---
tags: [rag, llm, knowledge-management, n8n, karpathy, obsidian, google-sheets, ai]
source: 社群分享（TG 2026-06-23）
github: https://github.com/uncle6me-web/LLM-Wiki-for-n8n
original: https://gist.github.com/karpathy/442a6bf555914893e9891c11ac484894
date: 2026-06-23
---

# LLM Wiki — Karpathy 的 Pre-Compile RAG 新觀念

> Karpathy（前 OpenAI/Tesla，現 Anthropic）提出的知識庫方法，有人做了 n8n 版。

---

## 傳統 RAG vs LLM Wiki

| | 傳統 RAG（向量法） | LLM Wiki（Pre-compile） |
|---|---|---|
| 比喻 | 碎紙機：文件碎成向量片段 | 總編輯：AI 讀懂全局後改寫 |
| 查詢方式 | 數學相似度抽幾條「碎紙」 | 查目錄（index）→ 讀 wiki |
| AI 的視角 | 只看幾條碎紙，不知全局 | 知道文章間的關聯（入庫時就寫好）|
| 適合場景 | 大量文件、token 預算低 | 需要全局觀、關聯推理 |
| Token 消耗 | 低（嵌入模型便宜）| 高（處理時燒 LLM token）|

---

## 核心概念

### Pre-Compile（預編譯）
把你的原稿「編譯」成 AI 愛看的定稿。人類寫原稿，AI 產出定稿。
- 原稿 = Single Source of Truth（有爭議時回去看原稿）
- 定稿 = AI 查詢時實際讀的內容

### 更新而非新增
1 萬份文件 → 不是 1 萬條 wiki，而是整理成 500 頁「教科書」。
- 內容相近 → 更新現有條目
- 差異大 → 才新增
- 結果：知識庫（知識有結構）而非知識倉庫（堆積如山）

### 目錄（Index）設計
每則 wiki 有配套目錄欄位：篇名、關鍵字、摘要、更新日期 → AI 查目錄再讀內文。

---

## n8n 實作（Google 版）

原版用 Obsidian（無網頁版），n8n 版改用：
- **Google Docs** → wiki 文章本體
- **Google Sheets** → index（結構化，n8n 直讀 JSON，速度快）

---

## 為什麼現在才出現？

嵌入模型極便宜 → 傳統 RAG 划算。  
LLM token 貴 → 以前燒不起。  
現在 LLM 便宜了 → 這個方法開始可行。

---

## 對派哥的評估

✅ **高度相關**：
- GBrain 的設計哲學跟 LLM Wiki 非常接近（pre-compile + index + 全局觀）
- MyNotes 的 Obsidian 結構就是這個概念的手動版
- 「語音輸入當原稿，AI 整理成定稿」完全符合派哥的工作流偏好

⚠️ **注意**：
- token 燒得兇（每次有新文件都要 LLM 處理）
- n8n 需要另外架設或用雲端版
- Google Sheets 當 index 適合中小型知識庫；大型仍需向量搜尋補強

💡 **可考慮**：把現有 MyNotes 的 Obsidian MD 接進這個 pre-compile 流程，讓 GBrain 同時有向量搜尋 + LLM Wiki 兩種查詢模式。

---

## 相關筆記

- [[understand-anything-codebase-kg]] — 知識圖譜理解大型 codebase
- [[headroom-context-compression]] — Context 壓縮與記憶管理
