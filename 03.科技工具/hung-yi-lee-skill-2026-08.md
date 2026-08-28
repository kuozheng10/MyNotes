---
tags: [claude-code, skill, knowledge-graph, distillation, open-source, mit-license, education]
source: 工程師米奇 FB 貼文（2026-08-25 系列第二篇）
url: https://github.com/voidful/hung-yi-lee-skill
references:
  - github.com/voidful/hung-yi-lee-skill（MIT，1.2k stars）
date: 2026-08-28
---

# 李宏毅 Skill — 把一位老師的「知識 + 教法」整包交給 AI

> 「以前大家比的是『你用哪一個 AI？』
> 以後可能還會多一句『你的 AI 裝了哪些 Skill？』」

作者 voidful（台灣 NLP 研究者）。承接 [[eli5-plugin-marketplace-2026-08]] 的觀察：Skill 真正有意思的地方，是能把**知識與做事方法直接交給 AI 使用**——今天是李宏毅老師的 AI 教學，未來可以是寫作、程式、設計、研究，甚至各種產業經驗。

---

## 這個 Skill 包了什麼

不是把語錄堆在一起，而是蒸餾出老師的**教學法、知識框架、溝通模式**。

| 資產 | 內容 |
|------|------|
| YouTube metadata | 478 部影片 |
| 完整逐字稿 | 27 份 |
| 主題頁 | 8 個（ML、LLM、語音、diffusion、agent） |
| 知識圖譜 | 916 節點 / 3,664 邊 / 10 個概念社群 |
| 語言標記 | 風格模式，例如「比如說」在逐字稿出現 609 次 |
| 校準 | 直接訪談李宏毅本人 |

**跟靜態 RAG 的差別**：持久化的知識結構、可抽取的概念關係、以「god nodes（樞紐節點）」為基礎的教學路徑、資訊來源可追溯（標記為 extracted 或 inferred）。

---

## 安裝 / 使用

```bash
git clone https://github.com/voidful/hung-yi-lee-skill.git
pip install -r requirements.txt
# 把 SKILL.md 放到 AI 助理讀得到的目錄
```

`scripts/` 有 CLI 工具做 search、graph query、wiki 編譯。查詢範例：用李宏毅的教學風格解釋某個概念、用他的教學視角分析內容。

repo 結構：`scripts/`（CLI）、`raw/youtube/`（逐字稿快取）、`wiki/`（主題頁 + 互動圖譜）、`references/`（原始素材、訪談協議、教學哲學）。

---

## 對派哥的意義

- **這是 [[cangjie-skill-distill-2026-07]] 的完整實作範例**：倉頡.Skill 講「把書/長影片蒸餾成可調用 skill」的方法論，這個 repo 就是拿一整個 YouTube 頻道 + 訪談做出來的成品，可以拆開來看 pipeline 怎麼跑
- **跟 [[graphify]] skill 同一個核心**：input → 知識圖譜 → 社群分群。派哥的 graphify 產出 HTML + JSON + audit report，這個 repo 是把圖譜當成 skill 的長期記憶結構
- **可套用到派哥自己的內容**：MyNotes 300+ 頁、工作日誌、cc_processor 的踩雷經驗，理論上都能用同一套方法蒸餾成「派哥自動化經驗 skill」，讓新 session 一開始就帶著這些判斷
- **趨勢訊號**：Skill 開始從「工具能力」（ELI5、UI 動畫）擴張到「某個人 / 某個領域的完整知識體系」，marketplace 之後這類 skill 會變多

---

## 相關筆記

- [[eli5-plugin-marketplace-2026-08]] — 同一系列貼文，官方 plugin marketplace 成形
- [[cangjie-skill-distill-2026-07]] — 把書/長影片/播客蒸餾成可調用 skill 的方法論（RIA-TV++ 七階段），這個 repo 是成品範例
- [[understand-anything-codebase-kg]] — 用知識圖譜理解大型 codebase，同樣的 god-node / 概念社群概念
- [[llm-wiki-karpathy-rag-2026-06]] — 把知識庫 pre-compile 成 LLM Wiki，持久化結構 vs 每次 RAG
- [[anthropic-skill-three-layers-2026-06]] — Skill 三層架構，這個 repo 的第三層（工具 / 參考檔）做得非常重
