---
title: Thin Harness, Fat Skills — Garry Tan 的 AI 架構理念
tags: [Agent, Skills, 架構設計, Claude-Code, 系統設計, AI工具, harness]
date: 2026-04-13
category: AI工具
source: Garry Tan (YC) — 轉自 Google Drive goodarticle
---

## 核心主張

同一個 AI 模型，有人做出 100 倍效率、有人只有 2 倍。
差別不在模型，不在 prompt，**在架構**：Thin harness（薄外殼）+ Fat skills（厚技能）。

---

## 五個定義

### 1. Skill Files（技能檔案）

可重複使用的 markdown 文件，教模型「怎麼做」，不是「做什麼」（那由使用者決定）。

關鍵洞見：**Skill file 的運作方式就像函式呼叫**，接受參數，不同引數產生截然不同的能力。

例：同一個 `/investigate` skill（7 步驟），傳入不同的 TARGET + QUESTION + DATASET：
- 指向科學家 + 210 萬封 email → 醫學研究分析師
- 指向空殼公司 + FEC 資料 → 法務調查員

這不是 prompt engineering，**這是軟體設計，用 markdown 當程式語言**。

### 2. Harness（外殼/駕馭工程）

運行 LLM 的程式，只做四件事：迴圈執行模型、讀寫檔案、管理 context、強制安全規則。就這樣。

反面模式（Fat harness）：40+ 工具定義吃掉一半 context window、God-tools、REST API wrapper。
→ 三倍 token 消耗、三倍延遲、三倍失敗率。

正面模式：專門打造的快速工具。
→ Playwright CLI（100ms/操作）vs Chrome MCP（15 秒），快 75 倍。

### 3. Resolvers（解析器/路由器）

Context 的路由表：任務類型 X 出現時，先載入文件 Y。

Claude Code 的 CLAUDE.md 就是 resolver——每個 skill 的 description 欄位讓模型自動配對意圖。

> Garry Tan：我的 CLAUDE.md 曾經有 2 萬行，每個怪癖都記進去，完全荒謬。修正後約 200 行，只是指向各文件的指標。Resolver 在需要時載入對的那份。

### 4. Latent vs. Deterministic

| 類型 | 說明 | 適合用 |
|------|------|--------|
| Latent（潛在空間） | 智力所在：閱讀、詮釋、決策、判斷、綜合 | LLM |
| Deterministic（確定性） | 信任所在：同樣輸入同樣輸出 | SQL、算術、編譯 |

最常見錯誤：把確定性問題硬塞進 latent space（如叫 LLM 排 800 人座位）。

### 5. Diarization（結構化摘要/側寫）

模型閱讀大量文件，蒸餾出一頁結構化的判斷摘要。
不是 SQL 查詢能產出的，不是 RAG pipeline 能產出的。

例：
```
FOUNDER: Maria Santos
SAYS: 「Datadog for AI agents」
ACTUALLY BUILDING: 80% commit 在帳務模組
→ 實際上是 FinOps 工具，偽裝成可觀測性工具
```
這種「說的 vs 做的」落差，只有同時讀完 GitHub + 申請表 + 逐字稿才能發現。

---

## 三層架構

```
Fat Skills（最上層）
  markdown 格式的流程，編碼判斷 + 過程 + 領域知識
  90% 的價值在這裡

Thin CLI Harness（中間層）
  ~200 行程式碼，JSON in → 文字 out，預設唯讀

你的應用（底層）
  QueryDB、ReadDoc、Search — 確定性的基礎層
```

原則：把智力往上推進 skills，把執行往下推進確定性工具，保持 harness 精簡。

---

## 會學習的系統（YC Startup School 案例）

6000 位創辦人，每晚 cron job 更新 profile：

- `/enrich-founder`：enrichment → diarization → 標示「說的 vs 做的」落差
- `/match-breakout`：按行業親和度分群（embedding + 確定性分配）
- `/match-lunch`：跨行業 serendipity matching，LLM 發明主題
- `/match-live`：200ms 回應，當下場景一對一配對

活動後 `/improve` skill 讀取 NPS 調查，對「還好」的回饋做 diarization，提取模式，把新規則**回寫到 matching skill**。Skill 自己改寫了自己。

12% → 4% 的「還好」評分，不需要任何人重寫程式碼。

---

## Garry Tan 給 AI 的黃金規則

> 你不准做一次性的工作。如果我叫你做一件事，而且它是那種以後還會再做的事，你必須：先手動做 3~10 個項目 → 給我看結果 → 如果批准，就把它寫成 skill file → 如果應該自動執行，就放上 cron。
>
> **測試標準：如果我需要同一件事跟你說兩次，就是你的失敗。**

---

## 對派哥的應用

- CLAUDE.md = resolver：現有架構已對，繼續保持精簡 + 指向 skill 檔案
- MyNotes skill 系統：就是 Fat Skills 的實踐
- 每次重複任務 → 問自己「這該寫成 skill 嗎？」
- Diarization 概念：之後 Hermes 多 Bot 分析任務可直接套用
- 學習迴圈：skill 能自我更新是終極目標，可先從手動 review + 更新 skill 做起
