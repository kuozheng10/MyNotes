---
title: Aaron Levie：AI 浪潮下企業工作流與創業視窗
tags:
  - ai-strategy
  - enterprise-ai
  - workflow
  - agent
  - startup
date: 2026-05-18
category: AI策略
---

## 核心論點

Box 創辦人 Aaron Levie（估值 35 億、Fortune 500 有 64% 用 Box）每月與 20+ 企業 CIO 開會，提供最接近真實企業落地的 AI 觀察視角。

來源：Silicon Valley Girl Podcast 訪談整理

---

## 人永遠在 workflow 的頭尾

Aaron 玩 AI agent 越深，越確認：流程的頭尾都需要真人，原因不只是 error rate，而是**責任歸屬**。

- Agent 沒有問責機制，不會被開除
- 法律、財務、醫療最終需要真人對結果負責
- 律師需求反而因 AI 增加：客戶先問 AI 起草文件，再找律師確認法律效力

> [!note] 具體案例
> 個人稅務他寧願給做了 20 年的人處理，3% 錯誤機率、$500 律師費省不了什麼

---

## Agent 管太多，大腦會爆炸

部署 agent 越多 = 你要擔任那些流程的「manager」角色：

- 要在腦袋裡 hold 住所有 context
- 追蹤 agent 做了什麼、沒做什麼
- 以前 context 分散在不同同事腦袋，現在全壓到你一個人

> 他從來沒見過創辦人說「50 個 agent 幫我跑公司、我睡得很香」

---

## 企業 AI 導入比矽谷想的慢很多

AI 能力提升 ≠ 在組織裡擴散，後者受限於：

- 資料放在哪（超過 5 年的公司資料散在 30 個系統）
- 資安設計
- Workflow 有沒有文件化
- 系統整合需要的工程時間

他更靠近 Yann LeCun 陣營：任何 2% 以上 error rate 都需要人把關。

---

## AI 讓三人公司長成十人公司

AI 不只取代人，更多時候是**破除成長瓶頸**：

- 三人電商用 agent 跑行銷、建客戶體驗網站
- 業績動了 → 供應鏈問題來了 → 三人變五人、十人
- 預測：AI 催生更**分散**的就業成長，不是大公司裁員的故事

放射科醫生案例：AI 讀片準確率 90% → 影像量暴增 → 放射科需求反而增加

---

## 現在招人看什麼

**領域專業 + AI fluency** 的結合：

- AI fluency：懂 agent 怎麼運作、MCP 是什麼、skill 怎麼設計
- 領域專業不過時：行銷要懂行銷、業務要懂銷售
- AI 是放大這些能力的工具，不是取代

---

## 哪些工作最先被「壓縮」

壓縮不等於消失：

- Tier 1 客服（改密碼、找登入連結）幾乎全自動化
- 記帳簿記在壓縮路徑上，但例外狀況的升級路徑永遠需要真人
- 複雜客服、情境化法律建議、個人化醫療 → AI 給的是「平均答案」，律師給的是針對你的情境判斷

---

## 創業視窗：3 年

大型技術平台每 10～20 年出現一次，每次催生一批新公司（Google/Amazon/Salesforce 各對應一個浪頭）。

現在的機會：
- **Vertical AI**：每個行業都還在等它的 Harvey（法律 AI）出現
- **AI 整合顧問**：幫非矽谷的 10 人小公司建 agentic workflow，Mark Cuban 認為是數十億市場
- **Agent 基礎設施**：Stripe 旗下 Tempo 做 agent 付款基礎設施

創業框架：
1. 假設最聰明的 AI 已存在 → 哪個領域能創造最大價值？
2. 哪裡有大公司沒在認真回應？
3. AI 很難部署的地方 = 整合服務的生意

---

## Agent 安全的核心問題

讓 agent 同時存取 email + Salesforce，收到請求「把那筆資料發給我」→ 絕對不接受：

- 不能讓 agent 相信任何 untrusted email 然後把資料傳出去
- 告警機制怎麼設、對方怎麼找到真人、每封信發出去前要不要審核 → 這些是系統安全與 workflow 定義問題，不是 AI 夠不夠強的問題

→ 參見 [[anthropic-agent-infra-strategy]]、[[atr-agent-threat-rules-panguard]]

---

## Aaron 自己的做法

- 每次都寫很長的 prompt，把明確指令帶進去，常用 prompt 存各地備用
- 靠 live context，不靠靜態個人文件
- 不讓 agent 代替他回信（他說：如果收到他的 agent 回的信，那是系統出了問題）
- 市場研究完全交給 agent fan out 分析百家公司，自己只點原始資料抽查
- 推薦工具：Codex、Claude、Perplexity

---

## 對派哥的參考點

- [[claude-code-ai-organization-engineering]] 關於 agent 認知負荷完全對應
- AI fluency = MCP + skill + agent = 派哥現在在建的方向，Aaron 認為這是接下來 3～5 年決定性的能力
- 整合顧問服務：非矽谷企業的 agentic workflow 建置，是派哥可以觀察的方向
- Error rate > 2% 需要人把關 → 測試策略的基礎邏輯 [[ai-era-testing-strategy]]
