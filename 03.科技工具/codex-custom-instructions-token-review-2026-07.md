---
tags: [ai-coding, codex, custom-instructions, token-optimization, workflow]
source: 派哥個人 Codex 自訂指令，自己貼出來問評估
date: 2026-07-30
related: caveman-token-saving-skill-2026-07, ai-token-cost-governance-tesla-2026-07, jason-liu-codex-work-system-2026-07
---

# 派哥的 Codex 自訂指令評估：哪些真的省 token、哪些沒用

> 起因：有人問派哥「為什麼你的每週使用上限感覺用很久」，他懷疑是自己這段 Codex 自訂指令幫他省了算力，拿來問 Claude 評估。

---

## 原始指令（存查）

```
使用繁體中文回覆。
優先以：工程化、模組化、Workflow 化方式思考問題。

回答時：
1. 優先拆解需求
2. 優先降低 token 消耗
3. 優先提高可維護性
4. 優先建立可擴充架構
5. 優先考慮 Agent Workflow
6. 優先考慮 Claude Code / Codex 可執行性
7. 避免冗長理論與空泛描述
8. 回答需具備工程結構與實作方向
9. 適合大型 AI Workflow 與多 Agent 系統
10. 優先輸出可直接執行的流程與架構

回答盡量包含：Workflow拆解 / Agent分工 / API架構 / Cursor Rules / Skills / TODO Tree / Token成本優化建議

風格：AI PM + AI Tech Lead + Workflow Architect
避免過度聊天與無結構回答。
```

---

## 評估結論

### ✅ 真的有用、值得保留

| 條款 | 為什麼有效 |
|------|-----------|
| #7 避免冗長理論與空泛描述 | 直接砍輸出端贅字，跟 [[caveman-token-saving-skill-2026-07]] 同一個原理——**輸出 token 是真金白銀，減廢話最直接** |
| #10 優先輸出可直接執行的流程與架構 | 逼模型一次到位給結論，減少「再問一次細節」的來回輪次 |
| 角色鎖定（PM+TechLead+Architect） | 固定回答框架，避免模型發散閒聊，間接減少無效輪次 |

### ⚠️ 自相矛盾、實際上可能沒省甚至更貴

1. **#2「優先降低 token 消耗」是空泛指令，犯了自己 #7 禁止的毛病**——沒有具體字數/篇幅上限，模型不會真的因為這句話變精簡，「省 token」需要可量化的約束（例如 caveman 那樣分等級：lite/full/ultra），純喊口號沒用。
2. **「回答盡量包含」那七項清單本身會拉長輸出**：Workflow拆解、Agent分工、API架構、Cursor Rules、Skills、TODO Tree、Token成本優化建議——每次都要求塞這七塊，等於逼模型每次回答都寫一份小型架構文件。如果拿來問一個小問題，反而比不設這指令更貴。這條跟「省token」的目標互相打架。

### 對「用量上限用很快」這個原始問題的判斷

這段自訂指令**不是**主因。參考稍早存的 [[ai-token-cost-governance-tesla-2026-07]]：真正燒錢的是 **agentic loop 的呼叫次數**（一輪一輪自己讀改跑），跟每次帶入 context 的大小（讀大檔案、貼大段工具輸出），不是系統提示詞本身的字數（那個是一次性小開銷）。這段指令頂多影響「單次回答的輸出長度」，對「一週跑幾百輪」這種消耗沒有直接控制力。

---

## 可包成 Skill 嗎？

可以，但建議跟目前派哥的 Claude Code 習慣分開，**不要當成全域預設**：

- 派哥的 Claude 目前預設是 [[feedback_reply_style|TG 白話口語短句]] 風格，跟這段「AI PM+架構師」的結構化輸出正好相反
- 建議包成一個**觸發式** skill（例如 `/pm-architect-mode` 或直接說「架構規劃模式」），只在他明確要做 workflow/agent 架構設計時切換進這個結構化模式，平常聊天/交辦小事維持現在的短句風格
- 如果目的真的是省 token，更該做的是把 #2 那句空話換成 [[caveman-token-saving-skill-2026-07]] 這種**有具體壓縮等級**的機制，而不是自己重造一個沒有量化標準的版本

**派哥還沒決定要不要真的包這個 skill，先存這篇評估，之後要做再回來動手。**
