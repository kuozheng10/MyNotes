---
title: Anthropic Claude Code 團隊怎麼做 Code Review（AI 寫 90% 程式碼時）
tags: [AI, ClaudeCode, CodeReview, 軟體工程, Agent, 品質]
source: https://www.facebook.com/share/p/19ZM9og7jK/?mibextid=wwXIfr
article: https://claude.dev/blog/solving-code-review-at-anthropic/
author: Study4.TW 謝政廷（FB 社團整理）；原文 claude.dev Blog
created: 2026-10-19
---

# Anthropic Claude Code 團隊怎麼做 Code Review

> 來源：FB 社團 Study4.TW 謝政廷整理 → 原文 [How the Claude Code team does code review](https://claude.dev/blog/solving-code-review-at-anthropic/)。派哥丟連結說「save sop」。本筆記以原文為主、整理者觀點為輔。

## 一句話重點

Claude 寫了 Claude Code 約 **90%** 的程式碼，人根本看不完。他們沒有取消 Review，而是**把「讀 code」交給機器、人只看真正需要判斷的地方**，再搭配「出事能秒退回」的機制。結果 PR 數量翻倍，**需要 Revert 的比例反而降了 40% 以上**。

## 規模跟成果（數字）

| 指標 | 數字 |
|---|---|
| Anthropic monorepo 每天合併變更 | 5 月約 **2,500** → 9 月 **30,000+** |
| Claude Code Merged PR（6 月→9 月） | **翻倍以上** |
| 需要 Revert 的比例 | **降 40% 以上** |
| PR 拿到有料 Review 意見的比例 | **16% → 54%** |
| 一輪 review 修完就過 | **65% → 78%** |
| 需要 5 輪以上 | **8.9% → 1.5%** |
| 平均 review 輪數 | **2.08 → 1.32** |

**怎麼衡量**：追「每個 PR 要幾個人 approve、人留幾則意見、PR 等人等多久」；**護欄**是 Revert Rate 跟 Incident Rate——如果這兩個上升，代表只是把人的時間挪走，不是省下來。

---

## 核心觀念轉換（白話）

以前問：「**有沒有人看過這段 code？**」
現在問：「**這個改動可能出什麼錯？哪一道檢查（機器或人）最適合抓到它？**」

Review 變成「**像打字時的拼字檢查**」——一直在跑，大部分問題在人看到之前 Claude 就自己修掉了。

---

## 七層防護（照順序）

### 第 1 層：開 PR 之前就先驗證
- Claude 自己跑**測試、Build、Lint**，而且要**貼出輸出結果**，不能只說「我跑過了」
- UI 改動要跟設計稿**截圖比對**
- 另一個 **全新 context 的 subagent** 重看 diff
- 工程師開 PR 前會跑內部 skill：抓 bug、簡化 diff、端到端驗證行為
- Boris Cherny（Claude Code 作者）：**給 Claude 能驗證自己成果的方法，結果好 2–3 倍**
- 同樣問題一直被抓到 → **從源頭修**：寫進 skill、lint 規則或指示檔
  - **CLAUDE.md**：技術棧、慣例、目標與非目標。**短**，其他細節指去別的文件
  - **REVIEW.md**（由 code owner 寫）：這塊 code 最在意什麼。好的 REVIEW.md 會：
    - 講清楚這個 repo「出錯長什麼樣」（文件類 =「它說謊」；設定類 =「它導錯地方」）
    - 限制 nit（小毛病）數量
    - 列出不用看的路徑
    - 要求附**檔案+行號**當證據，不能看名字亂猜
    - 摘要開頭先講「幾個問題」，沒問題就直說沒問題

### 第 2 層：每個 PR 都跑 AI Review
- 拿 diff 對照**整個 repo + PR 說明的意圖**來看；修 bug 的 PR 會追**根因**
- 產品版：**Code Review for Claude Code**（Team/Enterprise 已 GA），本機輕量版是 **`/code-review`**
- 可設 **Quick / Standard / Deep** 三種深度，漏一個 bug 很貴的地方用 Deep
- **降噪做法**：多個 agent 平行找 bug → 另一組 agent **投票驗證** → 夠多票同意才貼出來；純風格、純整理類意見直接丟掉（有 A/B 測過）
- 意見會標 **Important / Nit / Pre-existing**（既有 bug 不怪作者）
- **每則意見都要回應**：修掉，或寫理由關掉。agent 常常半夜就自己修好了

### 第 3 層：安全審查（可擋 merge）
- 獨立的自動安全掃描；bug 或安全意見**還有沒處理的，PR 就不能 merge**
- 誤報寫一句理由關掉；後續 commit 修好會自動清除
- 工具：開源 **security review GitHub Action** 或 **`/security-review`**

### 第 4 層：自動化必過檢查
- Lint、型別檢查、各平台測試、Build。一個 CLI PR 通常跑幾十項
- PR 範本要寫「**怎麼測的**」跟「**怎麼退回**」——Claude 可以代寫，但**提出需求的人要簽名負責**

### 第 5 層：依風險決定要幾個人看

| 風險 | 例子 | 需要幾個人 approve |
|---|---|---|
| 低 | 文件、文案、內部功能、藏在 flag 後面的新增 | **0 人**（自動 review + 安全掃描綠燈就好） |
| 中 | 一般產品改動；快取、自動更新、system prompt 等敏感區 | **1 人** |
| 高 | 最高風險的 code、規定一定要兩人看的路徑 | **2 人** |

規則：
- **改動內容決定等級，不是看誰寫的**。分類器判等級，第二個分類器再問「這個改動不管等級都需要人看嗎？」
- 一定要人看：owner 列為敏感的路徑、**所有 CI workflow 檔**
- 只有「**信任名單**」上的作者（大多是負責團隊）能走輕量路線
- **AI 的 approve 永遠不能算人的 approve**
- agent 寫的 PR，**下指令的人是必要 reviewer**，等同自己寫的
- approve 只綁**特定 commit**：之後有新 commit（agent push 或手動解衝突）要重新 approve

### 第 6 層：Merge Queue + Feature Flag + 分階段上線
- Merge Queue 把改動套在最新 main 上**重跑所有檢查**，避免兩個各自 OK 的 PR 合起來把 main 弄壞
- 新功能先藏在 flag 後面給**Anthropic 員工**用，內部大量使用很快就會抓到問題
- 公開版先上 **`latest`** 頻道，**`stable`** 慢一步跟上

### 第 7 層：快速發現、快速退回
- Flag 不用重新部署就能關
- **每週 on-call 輪值**；事故檢討問「**哪一層應該抓到卻沒抓到？**」
- 靠作者、on-call、Revert/Incident 儀表板發現問題
- **目前缺口**：還沒有「Revert 數字一升高就自動收緊 approve 規則」的斷路器
- 哲學：放慢速度會降錯誤率，但主要是因為**產出變少**。他們寧可**變得更會發現跟修正**

---

## 讓 AI Reviewer 越來越強

### 把事故變成考題（Incident → Eval）
- 收集過去造成事故/需要 Revert 的 PR + 修正，請熟悉的工程師確認 bug 跟位置
- **每天**拿這份考卷考 AI Reviewer；每次出事就多一題
- 改 prompt、工具、模型 → 全部重考，**分數上升才留，沒升就丟**

### 量化噪音
- 每則意見依作者反應分類：修了 / 說它錯 / 說是故意的 / 覺得不重要
- 也拿**已知乾淨的 PR** 跑，看它多常亂報會導致錯誤修改的東西
- 優先順序寫死：**先抓真 bug，其次才是減少輪數**
- agent 當作者時噪音更貴：agent 會乖乖修每個 nit → 多一個 commit → 多一輪 review

### 避免 AI 無限互改（收斂）
- 曾有一個 PR 半夜被 AI 作者跟 AI reviewer 來回改了 **50 輪以上**才被人叫停
- git blame 分析：reviewer 一直抓的東西有 **59%** 是第一輪就存在的舊 code——後面幾輪只是在挖舊 bug，不是新問題
- 限制規則：
  - **最多 3 輪**，之後請作者重新考慮做法
  - 前幾輪之後**只看新 diff**
  - **標出 bug 的「類型」**，讓作者一次修掉所有同類，而不是只修一行
  - **不重複**已經提過的意見
- 另外每晚跑 review agent 掃既有 code 抓舊 bug

---

## 人要專注在什麼

1. **這個東西該不該做？** 方向、品味、範圍
2. **高風險 code**：計費、自動更新、CI workflow
3. **會被別人複製的架構**
4. **看證據**：測試輸出、跑過的指令和結果、截圖、reviewer 意見。**說不出自動檢查會漏掉什麼，就別快速 approve，要真的 review**
5. **為結果負責**：每個上線的改動都有一個人負責，不管是誰打的字

## 文化：「You land it, you own it」（誰合進去誰負責）

能這樣做是因為：
- 改動**小**，好 review、好 debug、好退回
- **一切可逆**：flag、revert、分階段上線，大部分錯誤幾分鐘內就能撤
- **爆炸半徑決定門檻**：越貴的 code 越多人、越多檢查
- telemetry + 內部使用讓問題很快浮現
- **不是究責**：owner 最有 context，事故檢討檢討的是系統

其他：
- 理解 codebase 不靠逐行看小 diff，而是請 Claude 寫該區塊的 **explainer**（幾分鐘、反映最新 code），有人還請 Claude 做小型視覺化 artifact
- agent 讓開工很便宜，所以**有些 PR 本來就不該 merge**——方向不對就早點在討論串提，不要等 PR 做完才擋。寫得快的 code 關掉不心疼

---

## 給其他團隊的建議清單

**開 PR 前**
- 給 agent 能自己跑的檢查，寫在短的 CLAUDE.md；用 hook 自動跑 formatter/linter
- 本機跑 `/code-review`、`/security-review`，或全新 context 的 subagent review
- 加 REVIEW.md，把重複出現的 review 意見搬進去

**每個 PR**
- CI 必過；PR 範本加「Testing / Risk / How to revert」
- 先在**一個 repo** 裝 AI reviewer，調幾週 REVIEW.md 再擴大
- 自動安全審查 + 所有 review thread 解決才能 merge
- 依風險選 Quick / Standard / Deep；**限制輪數**，前幾輪後只看新 diff

**Approve**
- 寫下風險等級，**依改動不依作者**；先嚴後鬆、有證據才放寬
- 輕量路線只給信任作者
- 用 **CODEOWNERS + branch protection** 讓 auth、計費、CI、發版流程、安裝程式永遠要人看
- bot 的 approve 不能取代必要的人；新 commit 進來就作廢舊 approve

**Merge 之後**
- Merge queue、feature flag、內部先用、分階段上線、一鍵 rollback
- 事故跟 revert 做成 eval 集，reviewer 每次改動都重考
- 量人的時間，用 Revert/Incident Rate 當護欄

---

## 整理者（謝政廷）的觀點

1. 最有共鳴：用 **Revert Rate / Incident Rate** 當品質護欄——不追求零錯誤，而是**快速發現、快速復原**，用數據驗證流程改得對不對
2. 「You land it, you own it」+ Revert、On-call、Incident Review，才讓「減少人工 Review」變得可控

---

## 派哥可以拿來用的

| 文章做法 | 派哥現況 / 可以怎麼套 |
|---|---|
| 開 PR 前 Claude 要貼出測試輸出 | 已有：CLAUDE.md「完成驗證：type check + lint 全過才回報」 |
| 最多 3 輪就停、請作者換做法 | 已有類似：「鬼打牆偵測：同錯 ≥2 次停下換策略」 |
| 全新 context subagent review | 已有：Codex 實作 → Claude review（codex-review skill） |
| **REVIEW.md** | 可以幫 `investment/` 寫一份：列出「出錯長什麼樣」（跨頁截斷、UNIQUE 少 dedupe、snapshot 日期時區、cash 漏算），對應 feedback_investment_pipeline_bug_pattern 的 5 點清單 |
| **事故變考題（Incident → Eval）** | investment/ 那一串 bug（台新母帳戶漏記、us_prices 死循環、sync_accounts 五個 bug）可以整理成 regression test 集，每次改 pipeline 都重跑 |
| 依風險分級 | 文件/筆記小修直接推；investment/、OAuth、自動寄信這類高風險 → 加 Gemini review + 先問派哥（跟現有規則一致） |
| `/code-review`、`/security-review` | Claude Code 內建可直接用，改 investment/ 或 cc_processor 後可以跑 |

---

## 相關筆記

- [[scrum-ai-code-review-responsibility-2026-07]] — AI 時代 Code Review 責任歸屬，對照本篇「下指令的人是必要 reviewer」
- [[boris-cherny-cleaner-maintainer-2026-07]] — Boris Cherny 觀點，本篇引用他「給 Claude 驗證方法好 2–3 倍」
- [[ai-audit-trail-coding-agents-2026-07]] — coding agent 稽核軌跡，對照本篇「approve 綁特定 commit」
- [[code-duo-ai-audit-2026-06]] — 雙 AI 互審，對照本篇「多 agent 平行找 bug + 投票驗證」
- [[loop-engineering-agentic-ai]] — Loop 停機條件，對照本篇「50 輪無限互改 → 3 輪上限」
