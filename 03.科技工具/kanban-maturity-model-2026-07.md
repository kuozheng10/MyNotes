---
tags: [scrum, agile, ai-coding, kanban, kmm, maturity-model]
source: 敏捷三叔公（2026-07-24）
date: 2026-07-24
related: kanban-ai-agent-human-in-loop-2026-07, scrum-ai-code-review-responsibility-2026-07, team-of-teams-ai-coding-less-2026-07
---

# 你的 Kanban 板貼滿了便利貼，然後呢？——Kanban Maturity Model

> 來源：敏捷三叔公 FB 貼文 + 全文
> 全文：https://agile3uncles.com/2026/07/24/kanban-maturity-model-00/
> 同系列課程推廣：
> - Scrum 敏捷開發的系統性做法 – AI coding 時代的新做法（2026/08/29）https://agile3uncles.com/products/a004/
> - 如何利用價值流和看板改善開發效能（2026/08/30）https://agile3uncles.com/products/p004/

---

## 核心觀點

很多團隊導入 Kanban 只做了「畫板子、分 To Do/Doing/Done、每天站前講進度」，幾個月後便利貼越貼越多，流程沒變快、交期一樣難預測、瓶頸沒消失。

問題不是 Kanban 沒用，是把 Kanban 誤當成「一塊板子」。真正的 Kanban Method 是一整套從視覺化、限制 WIP、管理流動，到建立可靠交付能力的管理方法。**Kanban Maturity Model（KMM，David J. Anderson 與 Teodora Bozheva 提出）** 提供的是一張組織成長地圖：判斷目前在哪個成熟度、現在適合採用哪些實務、下一步該往哪走。

三大支柱：**文化**（各等級對應價值觀）、**實務**（適合該等級的管理做法）、**成果**（可觀察的業務成效）。

---

## 7 個成熟度等級

| 等級 | 名稱 | 特徵 |
|------|------|------|
| ML0 | 渾然不覺 | 無結構化協作，需求靠訊息傳遞 |
| ML1 | 團隊聚焦 | 有板子與三欄制，各團隊獨立運作 |
| ML2 | 客戶驅動 | 定義工作類型、設 WIP 限制、看流動指標 |
| ML3 | 符合目的 | 端到端管理，能用歷史資料做承諾 |
| ML4 | 風險對沖 | 量化風險管理（如 Cost of Delay） |
| ML5 | 市場領導 | 全組織持續改善，決策一致 |
| ML6 | 生存導向 | 組織具備自我重塑能力 |

**現實定位**：多數團隊卡在 ML1-ML2（只有板子、頂多定義工作類型），目標應設在 ML3（端到端管理 + 用歷史資料承諾交期）。

---

## 兩種典型失敗模式

1. **好高騖遠**：組織跳級採用進階實務（例如 ML1 直上 ML3 的做法），基礎沒打穩導致夭折
2. **假山頂**：初步改善後就停滯，誤以為「有板子 + 有流動」就是導入完成了 Kanban

## 實務案例

- **BBVA**：兩年導入後管理成本下降 28%
- **Vanguard**：40% 團隊從 Scrum 改用 Kanban，流動指標優於 Scrum 團隊

---

## AI coding 時代的調整

AI 工具讓瓶頸從「產出」轉向「驗證」，各成熟度等級要跟著調整關注點：

- **ML0-ML1**：AI 讓 PR 堆積速度變快，得先把 AI 產出的工作視覺化出來，不然瓶頸看不見
- **ML2**：WIP 限制要盯「審查容量」而不是「開發人力」——這點跟 [[kanban-ai-agent-human-in-loop-2026-07]] 裡「真正瓶頸在 In Review 欄」完全呼應
- **ML3**：Lead time 的組成改變了（產出變快、審查變慢），要重新收集資料分析

> 若組織仍停留在低成熟度就導入 AI coding，AI 只會讓混亂來得更快——量先於質的產出，撞上沒有分級管理的流程，就是災難的組合。

---

## 對派哥的意義

這篇是「組織該在哪個成熟度導入哪些 Kanban 實務」的宏觀地圖，跟 [[kanban-ai-agent-human-in-loop-2026-07]] 是互補角度——那篇談「怎麼把 agent 放上看板、In Review 當人工閘門」是**具體技術做法**（偏 ML2-ML3 的實務層），這篇是**先判斷自己在哪一級、再決定現在該不該導入那個做法**的前置診斷。兩篇合起來看：先用 KMM 定位現況，再挑對應等級能撐得住的實務（例如還在 ML1 就別急著上 In Review 閘門，先把 AI 產出視覺化出來就好）。

派哥自己的自動化（cc_processor、investment 排程）目前接近 ML1：有分工的腳本、有 Telegram 回報，但沒有正式 WIP 限制、沒有用歷史資料做交期承諾。KMM 這個角度提醒：不用急著把 [[kanban-ai-agent-human-in-loop-2026-07]] 那套「看板+MCP+審查閘門」整套搬過來，先確認現在的自動化規模是否真的需要跳到 ML2-ML3，還是维持現況、缺的只是「把哪些流程正在跑」視覺化出來就夠。

**是否「公司可用」**：KMM 是通用的組織成熟度診斷框架，不綁定特定產業或公司規模，個人（如派哥自己的自動化流程管理）也可以借用「先定位、再挑實務」的邏輯，不需要照搬企業版全部七級。

---

## 相關筆記

- [[kanban-ai-agent-human-in-loop-2026-07]] — 同作者「敏捷三叔公」，談具體的「agent 上看板 + In Review 人工閘門」技術做法；跟本篇「先定位成熟度再挑實務」互為前置診斷/具體解法的關係
- [[scrum-ai-code-review-responsibility-2026-07]] — 同作者，談 AI coding 時代責任邊界退化，跟本篇「ML2 WIP 限制要盯審查容量」呼應同一個瓶頸轉移現象
- [[team-of-teams-ai-coding-less-2026-07]] — 同作者，談協調落後於產出速度，跟本篇「AI 只會讓混亂來得更快」是同一個觀察的不同表述
