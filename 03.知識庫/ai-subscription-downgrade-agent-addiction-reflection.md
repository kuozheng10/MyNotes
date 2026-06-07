---
title: AI 訂閱降級與 Agent 成癮反思
tags: [ai-agent, claude-code, subscription, productivity, work-life-balance, codex]
source: 個人反思文章（2026-06）
date: 2026-06-07
---

# AI 訂閱降級與 Agent 成癮反思

> 訂閱 $200 Max 是我這輩子產出最多、也最焦慮的時候。  
> 半年後，選擇從 $200 降回 $60，主因不是錢，是心理健康。

---

## 三個 Phase 的演變

### Phase 1：$200 Max 的誘惑
- 2026/1：因聖誕活動 hit limit，升 Claude Code Max $100
- 2026/3：用量爆炸，升 $200 Max，體驗 Opus 4.6
- 產出：全端寫作系統（skills + genre 適配）、個人 CMS + 金流網站

### Phase 2：Claude Code + Codex 二重奏
- Codex 5.5 xhigh + fast 幾乎與 Claude Code 並駕齊驅
- ChatGPT 5.5 pro 是最強 AI 聊天，但升 $100 的人根本沒空回去用它
- 踩完 Orchestrate 坑後，設計了 **handoff / relay agent 交棒機制**：agent 自開 tmux/terminal 視窗交接任務，不被單一 session 綁定
- Codex UX 設計佳，是 **Agent 體驗最好的入坑起點**

### Phase 3：降級，想休息了
- 配置改為：Claude Pro $20 + ChatGPT Plus $20 + Antigravity AI Pro $20 = $60/月
- 原因不是 ROI，而是心理與生活品質

---

## 關鍵洞見

### 1. 慣老闆效應（Token Hoarding Psychology）
> 「當發現這週還有 token 剩，我就會 *invent* 一個工作給它。」

- 擔心 token 浪費 → 創造無意義工作 → 開過多戰線
- 桌面從 antigravity → + cmux → + 龍蝦 → + codex → + vs code → ...
- 這不是生產力，是偽裝成生產力的焦慮

### 2. Token Reset = 遊戲副本 CD 重置
- 用完 token = 推完尾王，反而舒暢
- Token reset = 以為可以下班，結果副本重置，「只好強迫提早開工跟上進度」
- 解法：**限量反而強制專注**，5h limit = 吃飯休息的訊號

### 3. 靈活性 > 單一模型開發能力
- 不想被 Claude Code 完全綁定，希望「任何 Agent 都可以操作」
- 理想：隨時調度最適合做這份工作的 Agent，甚至本地模型
- 結論：**Agent OS 設計要 model-agnostic**，不是單押一支

### 4. $200 FOMO 效應
- 物超所值反而製造壓力，「務必要花光 token」
- 降到 $20 的好處：**避免多開戰線、等待時去思考而非再開 session**

### 5. AI 三人行實驗
- Claude Pro $20 + ChatGPT Plus $20 + Antigravity Pro $20
- 增加多元性，減少單一依賴

---

## 可操作結論

| 行為模式 | 調整方向 |
|---------|---------|
| 看到剩餘 token 就找工作給 AI | 先問「這件事真的重要嗎？」 |
| token reset 後立刻開工 | 當作休息訊號，不跟 reset 的人競賽 |
| 同時跑多個 session | 一次一件事，做完才開下一個 |
| 全靠 Claude Code | 保持 model-agnostic，設計給任何 agent 用的環境 |

---

## 連結筆記
- [[agent-capability-map-expansion]] — Agent 能力地圖
- [[agentic-orchestration-cognitive-load-theory]] — orchestration 認知負荷
- [[agent-governance-production-service]] — agent 治理原則
