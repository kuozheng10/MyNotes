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

---

## OpenAI 視角補充（2026-05）

### OpenAI 官方實驗數據
- 5 個月、3 位工程師
- 從空白 Git Repo 開始
- 幾乎所有程式碼由 Codex Agent 生成（應用邏輯、測試、CI/CD、文件、Observability、內部工具）
- 最終：超過 100 萬行程式碼
- 開發速度：約人工的 10 倍
- **沒有人工手寫程式碼**

### 核心宣言
> **Humans steer. Agents execute.**
> 人類負責掌舵，Agent 負責執行。

人的工作不再是逐行寫程式，而是：
- 設計規則與流程
- 建立文件、測試、回饋系統
- 管理 Agent 協作

### 傳統 vs 新工作流程

| 舊 | 新 |
|----|-----|
| 人 → Prompt → AI → 回答 | 人 → Harness → 多 Agent → 測試 → 修正 → 驗證 → 部署 |

### 未來工程師兩種分類

**第一種（容易被取代）：**
- CRUD、重複開發、基礎功能、樣板式 Coding

**第二種（價值暴增）：**
- 系統架構、Workflow 設計、Agent 協作、AI 治理
- Feedback Loop、SOP、商業流程理解、知識管理

### 企業競爭力轉移

未來企業競爭力不再只是「有沒有 AI」，而是：
> **「有沒有 AI 工作系統（Harness）」**

因為：模型越來越便宜，真正困難的是 SOP/流程/文件/規則/Workflow。

### 新興企業角色

- AI Team Lead
- AI Workflow Architect
- Agent Manager
- AI Operations

### 一句話總結

> 「讓 AI 不只是會做事，而是能**穩定、可管理、可擴充**地工作。」

---

## 相關筆記

- [[addyosmani-agent-skills]] — Skills 本身就是 Inferential Guides 的系統化實作
- [[SDD-vs-SBE]] — 規格 = Feedforward Guide；例子驗證 = Sensor
- [[enterprise-ai-roles-prediction]] — Harness 架構師 = 文中的 「龍蝦架構師」職務
- [[claude-code-feature-workflow]] — 派哥的 feature workflow = User Harness 的具體流程
