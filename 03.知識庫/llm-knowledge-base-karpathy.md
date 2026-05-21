# LLM 知識庫：Karpathy 概念 + gatelynch 實作

> 收錄日期：2026-04-06
> 來源：社群貼文 × 2 + GitHub: gatelynch/llm-knowledge-base

## 核心主張

「讓 AI 負責整理，人只負責輸入與輸出。」

Andrej Karpathy（Tesla AI 總監、OpenAI 創始成員）的流程：
- raw/ 放原始素材（文章、逐字稿、筆記）
- LLM 自動「編譯」成 wiki/（摘要 + 概念條目 + backlink）
- 用 Obsidian 瀏覽 wiki，幾乎不手動改
- 累積後可對 wiki 問複雜問題，LLM 交叉比對
- 定期讓 LLM 跑「健檢」找矛盾、補缺漏

---

## 四層架構（gatelynch 實作版）

| 層 | 資料夾 | 規則 |
|----|--------|------|
| 1 | `raw/` | 原始素材，**唯讀**，任何人/AI 不得修改 |
| 2 | `wiki/` | LLM 編譯輸出：摘要 + 概念條目 + backlink |
| 3 | `brainstorming/` | 與 AI 的探索對話、知識健康報告 |
| 4 | `artifacts/` | 最終成品（電子報、Podcast 大綱） |

## Claude Code Slash Commands

- `/compile` — 掃 raw/，自動寫入 wiki/
- `/health-check` — 找不一致、補缺漏
- `/thinking-partner` — 深度共同探索
- `/write-partner` — 寫作前梳理相關知識
- `/braindump` — 對話沉澱成知識素材

---

## 派哥現況 vs. Karpathy 的差距

**現況**：素材按人物/主題分資料夾 → 選題 → 讀素材 → 寫電子報/Podcast
**缺口**：素材之間的連結全在腦中，素材越多越吃力

**派哥想借用的概念**：
- 追蹤哪些段落已寫進哪篇文章
- 哪些故事還沒寫過
- 列出未用過的寫作角度

---

## 評估：對派哥 MyNotes 的建議

見 session-2026-04-06.md

---

## 為什麼這比 RAG 更好（2026-04-08 補充）

> 來源：社群教學貼文

| 比較 | 傳統 RAG | Wiki / Graph 方法 |
|------|---------|-----------------|
| 架設複雜度 | 高（向量 DB、Embedding 模型） | 低（只需 Claude 訂閱） |
| 知識累積 | 不累積，每次查碎片拼湊 | 持續編譯，知識有 backlink |
| 查詢體驗 | 碎片化相似度搜尋 | 自然語言 + 精準來源引用 |
| 維護 | 需重新 embed 新文件 | 丟進 raw/ 叫 Claude 整理 |

**核心論點**：Wiki = Graph DB，速度快、成本低、知識有結構。

---

## 快速啟動 Prompt（繁中版）

**Step 1**：建立 `ProjectName/raw/` 目錄並放入原始文件
**Step 2**：Claude Code 輸入以下 prompt：

```
你是我專屬的 LLM Wiki Agent。請完成上面所有文字的內容實作，
當作我的第二個大腦，並一步一步指導我。
請建立 CLAUDE.md 作為 Schema 檔案，內含完整的運行規則。
接著建立 index.md 和 log.md，定義資料夾的命名規範與傳統，
並產出你的第一個文摘範例讓我確認。
從現在開始，所有的互動都要遵守 Schema 規則，且全部使用繁體中文。
```

**新增文件後**：直接說「幫我整理新文件」即可。

---

## 對派哥的啟示

- **MyNotes 本身就是 Wiki**，已在做同樣的事
- 可試著在某個子專案（如 AI2027 或 sales-report）先跑起來
- CLAUDE.md as Schema 的概念值得借鑑：把 MyNotes 的規範寫進 CLAUDE.md
- 未來可考慮：把 `~/.claude/skills/mynotes.md` 升級為完整 Schema
