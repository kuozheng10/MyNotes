---
tags: [agile, less, ai-coding, org-design, leadership, team-of-teams, scrum]
source: 敏捷三叔公（2026-07-04）
date: 2026-07-04
related: scrum-ai-five-fails-2026-06, ai-middle-management-less-block, ai-testing-agile-quality, ai-dev-problems-amplified-2026-06
---

# 從打仗到 AI coding：美軍作戰經驗為什麼在 2026 年更值得軟體團隊參考

> 來源：敏捷三叔公，同系列課程「不確定時代下的大規模敏捷 – LeSS 入門篇」(2026-07-25) 推廣文
> 對照書籍：Stanley McChrystal《Team of Teams: New Rules of Engagement for a Complex World》(2015)

---

## 背景：同一本書，兩種對照時機

《Team of Teams》是美國四星上將 McChrystal 反思他在伊拉克/阿富汗反恐戰爭中的組織與領導經驗。

- **十年前**：用來對照 LeSS，談的是**多團隊協作**
- **2026 現在**：AI coding 讓寫程式速度暴增，這本書反而更貼近軟體團隊眼前的處境——**協調落後於產出速度**

核心類比：美軍當年輸在「組織方式落後於敵人」（蓋達組織鬆散、去中心化、反應快；美軍是工業時代官僚體系）。放到現在：**AI 讓個別工程師產出暴增，但組織協調方式還停留在 AI 出現之前**。瓶頸已經從「寫得夠不夠快」移到「大家做的東西能不能兜在一起、能不能被信任」。

---

## 美軍四個轉變 × AI coding 時代的新意義

### (1) 命令控制 → 共享意圖（Shared Consciousness）

**美軍原做法**：打破情報壟斷，讓所有部隊知道「為什麼而戰」，前線不必事事等指令，能依共同意圖快速判斷。

**AI 時代對應**：團隊成員各自帶 AI agent 開發，若對「要解決什麼問題」理解有落差，**AI 只會用更快速度放大這個落差**。以前意圖沒對齊，開幾次會還來得及修正；現在一天就能長出好幾個方向錯誤的功能。

→ 這正是 **Specification by Example (SBE)** 在 AI 時代重要性上升的原因：具體範例是團隊與 AI 共享的意圖載體，**人看得懂，AI 也讀得懂**。

### (2) 功能分工 → 跨單位任務部隊（Task Force）

**美軍原做法**：拆掉情報、特種部隊、技術、後勤之間的牆，組跨單位、多角色 Task Force 面對複雜情勢。

**AI 時代對應**：AI 大幅降低跨技術棧門檻——後端工程師可在 AI 協助下改前端，測試人員能自己寫自動化腳本。**Feature team 過去最大阻力「一個人不可能什麼都會」正在變小**。

反過來說：若還維持 component team 切法，AI 加速的只是**每個部門各自的產出**，部門間的等待與整合成本一點沒少，甚至因半成品堆更快而更嚴重。

### (3) 層級通報 → 每日共識同步

**美軍原做法**：每天數千人視訊會議同步最新情資，決策權下放給掌握全局脈絡的現場指揮官。

**AI 時代對應**：AI 產出的程式碼量已超過人類逐行審查能力，團隊更需要高頻同步「AI 昨天幫我們長出了什麼」。這種同步的重點跟舊 standup 不同——**要同步的是決策脈絡**：哪些放手讓 AI 做、哪些需要人把關、驗證標準是什麼。

少了這層同步，每個人腦中對系統的理解會以肉眼可見速度和實際程式碼脫節——**這就是 cognitive debt 累積的過程**。

### (4) 指揮官 → 園丁

**美軍原做法**：McChrystal 把自己從決策中心角色，轉變成營造環境、建立連結的「園丁」。

**AI 時代對應**：這個比喻現在有具體工程版本。Thoughtworks 的 Birgitta Böckeler 談 harness engineering 提出 **Guides 與 Sensors**，本質就是園丁的工作：

- 不逐行指揮 AI 怎麼寫
- 設計**護欄**（coding standards、架構決策紀錄 ADR）
- 設計**感測器**（自動化測試、quality gate、eval）

領導者心力從「審查每個產出」轉向「設計讓好產出自然發生的環境」。

---

## 與 LeSS 的四項呼應

| Team of Teams | LeSS 對應 | AI coding 加值的新意義 |
|---|---|---|
| Shared Consciousness | 單一 Product Backlog + 共同 Sprint Review | Backlog item 配上 SBE 具體範例，共同理解可直接餵給 AI，成為人與 AI 共用的規格 |
| 跨單位任務部隊 | Feature Team | AI 降低跨棧門檻後，組 feature team 的技術理由更充分；剩下阻力多半是組織設計與考核制度 |
| 大規模同步 | Overall Sprint Planning + 多團隊協調 | 同步內容變了：除了「我在做什麼」，還要包含「AI 幫我做了什麼、驗證到什麼程度」 |
| 領導者是園丁 | Scrum Master 是組織改變的催化者 | SM 多一項工作：幫團隊建立與 AI 協作的工作協議——什麼交給 AI、什麼由人把關、出錯時如何回饋改進 |

---

## 結語（原文核心提問）

> 麥克里斯特爾面對的敵人是蓋達組織，軟體團隊面對的是被 AI 放大的複雜度與速度。他的答案——共享意圖、跨單位團隊、高頻同步、園丁式領導——LeSS 十年前就在講。
>
> AI coding 改變的是**代價**：以前少做這四件事，頂多交付慢一點；現在少做這四件事，是用更快的速度，做出彼此衝突、無人能驗證的東西。
>
> 你的團隊在用 AI 加速產出的同時，有沒有跟著加速「對齊」？

---

## 與既有筆記的關係

- **[[ai-middle-management-less-block]]**：同樣是 LeSS 視角談協調，但那篇的對照組是 Block「把協調交給 AI 模型、砍掉中階管理」；這篇的對照組是 McChrystal「把協調攤開來給前線人自己拼」。**兩篇合起來看，正好是「協調給人 vs 協調給機器」這條光譜的兩端**，Team of Teams/LeSS 站在人這一端，Block 站在機器那一端。
- **[[scrum-ai-five-fails-2026-06]]**：那篇談「各做各的」失效模式時提到跨職能只是形式（症狀），這篇的「跨單位任務部隊」章節給出同一問題的組織設計解方（Feature Team）。
- **[[ai-testing-agile-quality]]**：這篇的「園丁 = Guides + Sensors」跟該筆記的 Eval Gate / Self-Healing CI 是同一套機制的兩種說法——**護欄與感測器就是驗證機制的組織化**。
- **[[ai-dev-problems-amplified-2026-06]]**：DORA 數據講的 rework rate、verification overhead，是本篇「意圖沒對齊、一天長出好幾個錯誤方向」的量化版本。

---

## 課程資訊（同系列）

| 課程 | 日期 |
|------|------|
| 不確定時代下的大規模敏捷 – LeSS 入門篇（= 本篇主標題課程） | 2026-07-25 |
| 不確定時代下的敏捷測試 | 2026-07-26 |
| Scrum 敏捷開發的系統性做法 – 基礎篇 | 2026-08-29 |
| 如何利用價值流和看板改善開發效能 | 2026-08-30 |

來源：https://agile3uncles.com/products/a003/ (LeSS), https://agile3uncles.com/products/t005/ (測試), https://agile3uncles.com/products/a004/ (Scrum), https://agile3uncles.com/products/p004/ (價值流看板)
