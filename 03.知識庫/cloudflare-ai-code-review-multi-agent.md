---
title: "Cloudflare AI Code Review：七個專家 + 分級策略的多 Agent 實戰"
tags: [AI, Agent, code-review, 多模態, 工作流程, 架構設計, prompt, QA, 安全]
date: 2026-05-12
category: 03.科技工具
source: https://blog.cloudflare.com/ai-code-review/
---

## 核心洞見

> 「告訴 LLM 不要做什麼，才是 prompt engineering 真正有價值的地方。」

30 天、5,169 個 repo、13 萬次 review，平均 3 分 39 秒、不到 1 美元/次。

## 四個關鍵設計

**1. 七個專家，不是一個全能選手**

七個專業 reviewer：安全性、效能、程式品質、文件、發版、合規、AGENTS.md 檢查。
一個協調者 agent 負責去重、判斷嚴重程度、整合輸出。

**2. 負向 prompt 比正向 prompt 更重要**

不只說「請找 SQL injection」，還明確列出不要做的事：
- 不要報理論風險
- 不要動沒被改到的程式碼
- 不要建議「考慮改用 X 函式庫」

**3. 三級分流，依變更大小決定火力**

| 等級 | 條件 | Agent 數 | 費用 |
|------|------|----------|------|
| 小 | typo 等級 | 2 | $0.20 |
| 中 | 100 行內 | 4 | $0.67 |
| 大 | 100 行+ 或敏感目錄 | 7 | $1.68 |

碰到 auth、crypto 等安全檔案，不管多小直接升最高級。

**4. Break Glass 逃生通道**

工程師確定要硬上線時，留言打 `break glass` 強制放行並記錄。
30 天 48,095 個 MR 只用了 288 次（0.6%）。關鍵：給正當逃生通道，人才不會亂鑽漏洞。

## 對派哥的啟示

**立即可用：負向 prompt 加進 CLAUDE.md**

現有 CLAUDE.md 的 Code Review 只有正向規則（找安全漏洞/邊界條件）。補上「不要做」清單：
- 不要 review 沒被修改的函數
- 不要建議重構沒在改的部分
- 不要報「理論上可能發生」的風險

**分級概念套用到 cc_processor**

目前 cc_processor 每封 email 都全力跑。可參考 Cloudflare 的分級：
- 一般帳單 → 快速處理
- 金額異常 > N 元 → 升級驗證 + TG 通知

**AI review = 第零道防線，不是替代品**

AI 抓不到：架構問題、跨系統影響、細微 concurrency bug。
人類 QA 專注抓 AI 抓不到的事，不是重複 AI 做的事。

## 連結筆記

- [[ai-code-review-security-risk]] — AI Code Review 安全風險
- [[multiagent-specialized-vs-general]] — 多 agent 專才 vs 通才
- [[performance-testing-90-percent-not-tools]] — 工具以外的思維（同樣強調分工與目標）
- [[claude-code-ai-organization-engineering]] — Claude Code 作為 AI 組織工程
