---
tags: [ai, agent, devops, agent-enablement, org-scaling, claude-code, governance, continuous-learning]
source: Patrick Debois - The Rise of Agent Enablement - AI Native DevCon June 2026
url: https://www.youtube.com/watch?v=I9RWrW32QEw&t=47s
saved: 2026-07-18
related: agentic-sop-to-work, scrum-ai-code-review-responsibility-2026-07, loop-engineering-agentic-ai
---

# DevOps 之父潑冷水：AI agent 寫錯，你跳進去改——這就是團隊卡住的原因

> Patrick Debois（DevOps 之父）在 AI Native DevCon 的演講，主張 AI agent 在企業規模化不是技術問題，是組織問題。他把 10 年前推 DevOps 遇到的阻力、方法論，原封不動搬來對付 AI agent 導入。

---

## 一句話總結

**Agent 寫錯 code，不要自己跳進去改——要回頭改「系統」（CLAUDE.md / spec / guardrail），讓 agent 下次不會再錯。改一次 code 只救一次，改一次系統救到永遠。**

這正是 [[agentic-sop-to-work]] 的核心精神（人工 SOP → 工程化成 agentic workflow）在組織管理層面的呼應版本。

---

## 老規矩，換個對象再做一次

教工程師的老規矩，原封不動搬到 agent 身上：

1. 動手前先規劃 → agent 先做 plan 再寫 code
2. 要寫測試 → 用測試檢查 agent 有沒有亂改東西
3. 要寫文件 → 寫 spec / context 給 agent 看
4. 任務要切小 → 任務太大，agent 就會亂跑
5. 目標要講清楚 → 指令太模糊，token 燒到爆

> 「我從沒想過有一天工程師會自願寫文件——因為寫了 spec，agent 就變聰明，大家就肯寫了。」

---

## 四個層次，一層一層墊高

### 第 1 層：工程師自己 — 養成習慣

每做完一件事，問自己：**怎樣讓這件事不用再做第二次？**

- 團隊共用一份 CLAUDE.md，不要每個人各自維護、上網東抄西貼
- Spec 要持續維護，不是寫完就丟，不然會過期
- 限制 agent 的權限——它能碰客戶資料庫嗎？先想好，別讓它亂炸

### 第 2 層：Team Lead — 把 agent 當團隊成員管

- 新指標：**agent 要來回幾次（turns）才做對**。例：上個 sprint 平均 3 次過，這個 sprint 要 8 次——retro 時討論為什麼（例：新加的 spec 寫太模糊）
- Retro 也要回顧 agent 表現，不只回顧人
- 人才轉型：coding 高手要轉型成「Agent 馴獸師」——最會給 context 的人
- 遇到「AI 做不了我做的事」的懷疑派，回他：「太好了！那請你把你會的寫下來，agent 就會了。」

### 第 3 層：平台團隊 — 別讓每個團隊重複造輪子

普及路徑：1 個人試用 → 幾個人 → 一個團隊 → 平台團隊接手 → 全公司。平台團隊該提供：

- **Skills 商店（Registry）**：像 npm 一樣集中放、有版本、直接 pull，不用手動複製貼上
- **集中監控**：全公司 agent 表現看一個儀表板
- **內建護欄**：安全掃描、gateway 直接做進平台，讓「正確的路」變成「最輕鬆的路」

**Fork 問題（常見悲劇）**：分享一個很棒的 skill，同事說「99% 很讚，但我想改一小點」→ fork 一份 → 兩個版本各自沒人維護 → 都爛掉。解法：把 skill 設計成可擴充，讓大家貢獻回同一份。

**「我們很特殊」的抗拒**：當年推 DevOps 也聽過無數次「我們是金融業」、「我們系統很老」、「我們流程很獨特」，結果幾年後這些公司全都做起來了。
> 「你這個人很特別，但你的工作方式並不特別。」

### 第 4 層：VP / 高層 — 不能只是發工具、看帳單

多數公司卡在：買 license 發下去 → 監控花費 → 沒有然後了。高層真正該做的：

- 平衡各團隊：A 團隊產出爆量、B 團隊 review 不完？要調節，不是放生
- 投資不只是買工具：教育訓練、改善流程、監控成效都要編預算
- 訂治理規則：誰能用哪些 skill？外部 skill 要不要審核才能引進？
- 把痛點量化：跟資安一樣，拿不出「有幾個漏洞、風險多大」就要不到預算，不能只說「感覺變快了」

---

## 木桶理論

木桶能裝多少水，看最短的那片板子。自動化做到 100 分、治理 0 分 → agent 全自動狂產 code，卻沒人管它能碰什麼資料、有沒有掃安全漏洞 → 水全部從短板漏光。策略不是單點衝刺，是每一層都推進一點點，全面墊高。

---

## 最後結論

- CI/CD 年代比的是「交付多快」
- AI 年代比的是「**組織學習多快**」——整個組織吸收新知識、換上新工具的速度，Patrick 稱之為 **Continuous Learning**

---

## 對派哥的意義

派哥目前是個人使用場景（不是團隊管理），但第 1 層「工程師自己」的習慣完全適用：

- CLAUDE.md 就是派哥自己的「系統」，每次 Claude 犯同一種錯，該做的是把規則寫進 CLAUDE.md / skill，而不是每次手動糾正（這也是 memory 系統 feedback 類型存在的意義）
- 「agent 要來回幾次才做對」這個指標，可以類比成派哥自己感受到的「同一個問題要提醒幾次」——如果同一件事一直要重複講，代表該補進 CLAUDE.md 或 skill 了，不是繼續口頭糾正

延伸閱讀：[[agentic-sop-to-work]]（把人工 SOP 工程化成安全 agentic workflow 的具體工具）、[[scrum-ai-code-review-responsibility-2026-07]]（AI 產出責任歸屬的團隊心理層面）
