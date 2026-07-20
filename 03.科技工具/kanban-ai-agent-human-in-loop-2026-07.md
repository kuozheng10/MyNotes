---
tags: [scrum, agile, ai-coding, kanban, mcp, agent, human-in-the-loop, claude-code]
source: 敏捷三叔公（2026-07-20）
date: 2026-07-20
related: scrum-ai-code-review-responsibility-2026-07, team-of-teams-ai-coding-less-2026-07, loop-engineering-agentic-ai, ai-audit-trail-coding-agents-2026-07
---

# 看板的下一步：不只給人看，也給 AI Agent 用

> 來源：敏捷三叔公 FB 貼文 + 全文
> 全文：https://agile3uncles.com/2026/07/20/kanban-next-ai-agent/
> 同系列課程推廣：
> - Scrum 敏捷開發的系統性做法 – AI coding 時代的新做法（2026/08/29）https://agile3uncles.com/products/a004/
> - 如何利用價值流和看板改善開發效能（2026/08/30）https://agile3uncles.com/products/p004/

---

## 核心觀點

看板一直是給人看的視覺化工具，但現在多了一個新玩法：讓 AI agent 也上板工作。

人負責規劃，把任務拆小、驗收條件寫進卡片；agent 透過 MCP 自己領卡、執行、移卡、回貼留言。做完的工作停在 **In Review**，由人審查後親手移到 Done——**「agent 認為做完」和「你同意做完」是兩回事**。

> 寫程式便宜了之後，規劃品質和審查容量才是限制因子。管理這兩件事的工具，三十年前就有了，它叫看板。

---

## 實作流程（五步驟）

1. 每個 repo 設置單一看板，分四欄：To Do / In Progress / In Review / Done
2. 把看板註冊為 Claude Code 的 MCP 伺服器
3. 人負責規劃：拆解功能成明確小任務，標註驗收條件
4. Agent 自主檢取最上層任務，自動移卡、執行、回報
5. **關鍵設計**：Agent 完成後停在 In Review，等人工審查後才手動移到 Done——這欄就是內建的 human-in-the-loop

進階變體：卡片進入特定欄位時可設自動規則直接觸發 agent 執行，變成「事件驅動」而非「人工觸發」。

---

## 三個關鍵觀察

1. **WIP 限制重新定位**：真正瓶頸不在 agent 產出速度，而在 In Review 欄——也就是人的審查容量
2. **任務卡即規格**：卡片品質直接決定 agent 產出好壞，寫規格升級成「寫可執行輸入」
3. **透明性升級**：同一個看板上同時看得到人跟 agent 在共同時間軸上的所有動作

---

## 對派哥的意義

跟現有的 [[loop-engineering-agentic-ai]]、[[ai-audit-trail-coding-agents-2026-07]] 是同一個命題的另一種解法：怎麼讓多個 Claude Code / agent 自動化流程「可審查、有煞車」。目前派哥自己的自動化（cc_processor、investment 排程等）審查機制是散落在各個 skill 裡的人工截圖回報 + Telegram 對話，沒有一個統一的「agent 排隊 + 人工審查閘門」介面。

如果之後要管理的自動化流程數量變多、或想讓多個 agent 平行跑但仍然保留人工把關，這篇的「看板 + MCP + In Review 閘門」架構值得參考——本質上就是給 [[project_investment_processors]]、cc_processor 這類多支自動化排程一個共用的任務佇列 + 審查介面，而不是每支腳本各自用 Telegram 回報。

**是否「公司可用」**：這是通用的 agent 協作模式（看板本身工具中立，重點是流程設計：拆小任務+驗收條件卡片化+In Review 人工閘門），不綁定特定看板產品或公司規模，個人或團隊都適用。缺的是「哪個看板工具有現成 MCP server」這塊要另外查——全文本身沒點名具體工具。

---

## 相關筆記

- [[scrum-ai-code-review-responsibility-2026-07]] — 同作者「敏捷三叔公」，談 AI coding 時代責任邊界退化的問題，此篇的 In Review 閘門可視為對那個問題的具體解法之一
- [[team-of-teams-ai-coding-less-2026-07]] — 同作者，談協調落後於產出速度，此篇的看板正是補協調缺口的工具
- [[pbr-genai-example-driven-refinement-2026-07]] — 同作者系列作，談 agent 動工「前」的需求釐清（PBR階段），跟此篇談 agent 做完事「後」的審查閘門正好是事前/事後兩端互補
- [[loop-engineering-agentic-ai]] — 派哥自己的 loop/自動化設計原則，跟此篇「事件驅動觸發 agent」呼應
