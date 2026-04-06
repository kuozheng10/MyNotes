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
