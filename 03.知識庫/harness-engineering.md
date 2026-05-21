---
title: "Harness Engineering：Agent = Model + Harness"
url: "https://martinfowler.com/articles/harness-engineering.html"
tags: [ai-coding, agent, harness, claude-code, architecture, llm]
date: 2026-04-07
category: 03.科技工具
source: Telegram 分享（Birgitta Böckeler / Martin Fowler Blog）
---

## 一句話核心

> Agent = Model + Harness。除了 LLM 本身以外的所有東西都叫 Harness。掌握 Harness 設計，才是讓 AI 可靠工作的核心技術。

## 概念架構

```
Agent
├── Model（LLM，自迴歸文字生成）
└── Harness（= 以下全部）
    ├── Base Harness（內建工具、系統提示詞）← Claude Code 目前多數人停在這
    └── User Harness（使用者自行建構）← 這裡才是工程挑戰
```

## User Harness 兩大元件

| 元件 | 方向 | 說明 | 例子 |
|------|------|------|------|
| **Guides（指南）** | 前饋（Feedforward）| 事前餵給 Agent 的資料 | CLAUDE.md、AGENTS.md、skills/ |
| **Sensors（感測器）** | 回饋（Feedback）| Agent 運作產生的資料 + 外部監督 | 測試結果、type check、git status |

## 來源分類

| 類型 | 特性 | 例子 |
|------|------|------|
| **Computational** | 確定性、不隨機，CPU 運算 | CLI 輸出、Docker log、型別檢查結果 |
| **Inferential** | LLM 推論，不 100% 準確但夠用 | CLAUDE.md、Computer Use 截圖判斷 |

## Computer Use 的真正用途

不是跟 Cursor 比拚，而是：當 Claude Code 開發桌面 App 時，需要知道「按鈕按下後畫面長什麼樣」→ Computer Use = **Inferential Sensor**，讓 Agent 能驗證 UI 行為，持續開發而不中斷。

## 關鍵洞察

1. **Harness 會被模型吸收**：GitHub MCP 等 Harness 隨著模型學習 gh 指令後可能被淘汰，因為新模型原生支援
2. **CI/CD 整合是 Harness Engineering 的進階章節**（原文尚未展開）
3. **這不是軟體工程專屬**：未來影響各行各業的核心技術

## 派哥目前的 Harness 對應

| Harness 類型 | 派哥的實作 |
|-------------|-----------|
| Inferential Guide | `CLAUDE.md`、`bugfix.md`、`feature-workflow.md`、skills/ |
| Computational Sensor | `npx tsc --noEmit`、`git status`、cc_processor log |
| Inferential Sensor | （未來）Computer Use 驗證 UI |
| User Harness 架構 | Gemini + Claude 分工 = 雛形 multi-agent harness |

## 實作案例：C# Multi-Agent Chain（2026-04-24）

一個工程師用 C# + Microsoft Agent Framework 1.0 實作的 agents chain，驗證 Harness 四層公式：

```
按下 run →
  Coder agent（寫 code）
  → Reviewer agent（審 code）
  → build 成功後 PM agent（對 spec）
  → Security agent（刻意用不同 LLM 掃漏洞）← AI 審 AI
  → Deploy agent（推 source control）
→ 去倒咖啡，回來看 report
```

**Harness 四層對應**：
- 執行層：bash/file/MCP，給 LLM「手」
- 記憶層：rules 文件 auto inject（= Skills）
- 反饋層：test/lint error 回傳
- 編排層：拆任務 / 防死循環

**角色轉變**：從「code 審查員」（全程在線）→ orchestrator（按 run 後去倒咖啡）

**關鍵洞見**：差別不是 AI 變聰明，是**流程**終於拆得出去。同樣的 model 換不同 IDE 表現天差地別，差別在那層「外殼（Harness）」。

## 相關筆記

- [[addyosmani-agent-skills]] — Skills 本身就是 Inferential Guides 的系統化實作
- [[SDD-vs-SBE]] — 規格 = Feedforward Guide；例子驗證 = Sensor
- [[enterprise-ai-roles-prediction]] — Harness 架構師 = 文中的 「龍蝦架構師」職務
- [[claude-code-feature-workflow]] — 派哥的 feature workflow = User Harness 的具體流程
