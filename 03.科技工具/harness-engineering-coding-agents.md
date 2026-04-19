---
title: Harness Engineering for Coding Agent Users 重點摘要
tags: [AI, Agent, LLM, 架構設計]
date: 2026-04-20
category: 系統架構
author: Birgitta Böckeler (Thoughtworks)
---

## 這是什麼

這篇文章由 Thoughtworks 的 Birgitta Böckeler 撰寫，探討在使用 AI Coding Agent 時，如何透過設計「Harness（馬具）」來提高 Agent 的可靠性。核心論點：**Agent = Model + Harness**，而 Harness 是模型之外所有支持系統的總稱。

設計良好的 Outer Harness 有兩個目標：
- 提高 Agent 第一次就做對的機率
- 建立 Feedback loop，讓 Agent 在問題到達人類眼前之前完成自我修正

---

## 核心框架

### Feedforward 與 Feedback

- **Guides（Feedforward）**：預判錯誤並在行動前引導。例如 `AGENTS.md`、Skills 指令文件
- **Sensors（Feedback）**：在 Agent 行動後觀察結果。最強大的 Sensor 針對 LLM 優化，在自定義 Linter 訊息中包含修正指令，形成「正向 Prompt Injection」

### Computational 與 Inferential

- **Computational**：由 CPU 執行，決定性且極速。例如 Tests、Linters、Type checkers、Structural analysis
- **Inferential**：由 GPU/NPU 執行（LLM-as-judge）。語意分析、AI Code Review。非決定性，但能提供語意層面的判斷

### The Steering Loop

人類透過迭代 Harness 來「轉向」Agent。問題重複發生時，不只修程式碼，而是改進 Feedforward Guides 或 Feedback Sensors。這是持續優化系統的核心機制。

### Keep Quality Left（品質左移）

- Integration 前：快速 Linter、Fast Test、基礎 Code Review Agent
- Post-integration：Mutation testing、大範圍語意審核
- Continuous Sensors：死碼偵測、依賴掃描、執行期 SLO 監控

---

## Harness 三大維度

### Maintainability Harness

針對程式碼可維護性的監控：重複程式碼、複雜度、架構偏離、風格違規。

### Architecture Fitness Harness

定義並檢查「架構特性（Fitness Functions）」，確保系統演進方向符合預期。

### Behaviour Harness

三者中挑戰最大。**過度信任 AI 生成的測試非常危險**，AI 可能自圓其說地通過自己寫的測試，卻漏掉真正的邊界條件。

---

## 對派哥的啟示

派哥平時用 Claude Code 管理多個自動化專案，以下對照具體場景：

**cc_processor（信用卡帳單自動化）**
- 目前的 `CLAUDE.md` 就是 Feedforward Guide，但可以更精確：例如針對 HSBC/國泰不同格式，寫入「如果欄位遺失，不要自動補0，要報錯」這類具體指引
- Sensor 層面：每次 Agent 解析帳單後，加一個 Computational 檢查（總金額是否在合理範圍），異常就阻止寫入

**MyNotes 自動化（這篇筆記本身就是例子）**
- 現在每次存筆記的指令（frontmatter 規則、禁用 H1、tag 清單）就是 Feedforward Guide
- Sensor 可以更進化：寫一個 linter 自動檢查 frontmatter 是否完整、H1 是否出現，在 git commit 前擋下格式錯誤

**My Wallet Trip / Sales Report**
- Agent 跑完自動化任務後，若能加一個「執行後摘要回報到 Telegram」的 Feedback Sensor，派哥就不用主動查，異常即時感知

**最重要的啟示**：當同一個問題在 Agent 身上重複發生時，解法不是再叮嚀一次，而是把叮嚀**外化成規則檔或自動檢查**，讓 Harness 替派哥記住經驗。

---

## 連結筆記

- [[harness-engineering]] — Harness 概念初版整理
- [[harness-engineering-automation-risks]] — AI 自動化的安全風險
- [[garry-tan-thin-harness-fat-skills]] — Thin Harness + Fat Skills 設計哲學
- [[ai-era-testing-strategy]] — AI 時代的測試策略
- [[claude-code-powerup-guide]] — Claude Code 強化指南
