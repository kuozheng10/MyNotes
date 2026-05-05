---
title: 三模型協作策略：Claude Code + Codex + Gemini 任務路由 + 免費額度最大化
tags: [Claude Code, Codex, Gemini, multi-agent, 自動化, CLAUDE.md, 免費額度, 工作流]
date: 2026-05-05
category: AI工具
source: 派哥實戰策略
---

## 核心概念

不只用一個 AI，而是讓三個不同 provider 的 AI 依任務特性分工——既能發揮各家強項，又能把三方免費額度全部用盡，形成「反擊」單一 provider 依賴的策略。

---

## 分工設計

| 模型 | Provider | 職責 |
|------|----------|------|
| **Claude Code** | Anthropic | 主力編程、架構設計、CLAUDE.md 規則執行 |
| **Codex** | OpenAI | 檢視已生成內容、給意見、Code Review |
| **Gemini** | Google | YouTube 摘要、圖片生成、長文本處理 |

---

## CLAUDE.md 路由規則（實際配置）

在 CLAUDE.md 設定自動路由，讓 Claude Code 知道何時轉交：

```markdown
## 工具分工

- **Codex**（主力寫 code）：純 coding 任務優先用 Codex
- **Gemini CLI**（研究/掃描）：`gemini -p "問題"`
  - YouTube 影片摘要
  - 圖片生成提示詞設計
  - 長文本掃描 / 文件批量處理
  - 有關任務：Claude 判斷 + 實作，Gemini 查資料
```

規則寫進 CLAUDE.md 後，Claude Code 遇到觸發條件會自動調用，不需要每次手動指定。

---

## 免費額度最大化邏輯

三個 provider 各有獨立的免費/訂閱額度：

- Anthropic Claude：訂閱上限，但 Claude Code session 另計
- OpenAI Codex：有一定免費 API 額度
- Google Gemini CLI：免費額度相對寬鬆（尤其 Flash tier）

三方同時跑的好處：
1. 各家額度**不互相抵扣**
2. 高峰期一家額度耗盡，另外兩家仍可繼續
3. 特定任務自然對應最便宜（或免費）的那個模型

---

## 實際工作流示意

```
派哥丟任務
  ↓
Claude Code 判斷類型
  ├── 編程任務 → 交給 Codex 寫 → Claude Code 或 Codex 自己 Review
  ├── YouTube/圖片/長文 → Gemini CLI 處理 → Claude Code 整合結果
  └── 架構/判斷/整合 → Claude Code 自己做
```

---

## 這是一種「反擊」

傳統做法：選一個最強的 AI，全部任務都壓在同一個 provider。

這個策略的反擊點：
- **不被單一 provider 綁死**：任何一家調漲、降速、爛掉，都不影響整體
- **免費額度最大化**：同樣的工作量，分攤到三家，付出的錢更少
- **各取所長**：Gemini 長上下文強、Codex 執行力穩、Claude 判斷架構佳

---

## 未來趨勢面向

這個模式預示 AI 工作流的方向：
- 個人開發者的「AI 工作室」會是多模型混搭，而非單一助理
- CLAUDE.md 類的 routing 配置會成為個人 AI 工作流的核心設定
- 免費額度策略會變成降低 AI 使用成本的主流手段

---

## 對比參考

- [[multi-agent-team-24h-codex-claude-architecture]] — Codex+Claude 分工的 TL/PM 架構（單一專案協作）
- [[dual-agent-dev-loop]] — Claude+Coworker 開發測試循環
- [[claude-code-token-saving-strategies]] — Claude Code token 省用策略
- [[n8n-vs-ai-agent-when-to-use]] — 自動化工具選擇框架
