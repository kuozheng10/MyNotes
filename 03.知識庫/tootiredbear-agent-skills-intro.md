---
title: Agent Skills 是什麼？一篇看懂 AI Agent Skills 核心概念
tags: [agent-skills, SKILL.md, progressive-disclosure, MCP, AI架構, 入門]
date: 2026-04-28
category: AI工具
source: tootiredbear on Medium
---

## 核心定義

Agent Skills = 輕量級開放格式，賦予 AI agent 專業知識與工作流程

封裝的內容：
- 特定任務的做法與規則
- 任務執行所需的 context
- 穩定可重複的輸出方式

---

## 最小結構

```
skill-name/
├── SKILL.md         # 必填：name + description + 執行指令
├── scripts/         # 可執行程式碼
├── references/      # 文件與流程指南
└── assets/          # 模板與資源
```

---

## 關鍵架構概念：Progressive Disclosure（漸進式揭露）

Agent 只在需要時才載入 skill 的完整內容：

```
1. 平時只載入 skill name + description（極低 token）
2. 任務相關時才讀取完整 SKILL.md
3. 需要時再取用 scripts / references / assets
```

這就是為什麼 skill 能在不爆 context 的情況下，讓 agent 擁有大量專業能力。

---

## Skills vs Prompts vs MCP

| 工具 | 定位 | 使用時機 |
|------|------|---------|
| Prompt | 一次性指令 | 臨時任務 |
| Agent Skill | 可重用能力包 | 重複性、需要領域知識的工作 |
| MCP | 外部系統連接 | 需要連 Jira / Notion / API 等外部工具 |

Skills 處理「agent 要怎麼做」，MCP 處理「agent 要連什麼系統」。
兩者互補，不是競爭關係。

---

## 適合包成 Skill 的工作

- 固定格式的重複性任務（會議記錄、文件轉 Markdown）
- 需要領域知識的任務（測試策略、設計審查）
- 跨專案通用的工作流（SOP、健檢、交班）

不適合：一次性任務、高度動態的任務

---

## 意義：從對話 AI → 可維護的組織系統

Skills 的本質是**知識的制度化**：
- 不依賴人類記憶，agent 能可靠執行複雜重複流程
- 知識可以跨 agent 共享（一個 skill，多個 agent 都能用）
- 從「聊天工具」進化為「可靠的機構系統」

---

## 對派哥的意義

你已有 20+ 個 skill（grill-me、handover、image2-carousel 等）
→ 你做的事就是這篇說的「知識制度化」

CLAUDE.md + skills = 你和 Claude 之間的 ubiquitous language（對照 Matt Pocock 那篇）

---

## 連結筆記

- [[agent-skills-standard]] — agent skill 標準格式
- [[garry-tan-thin-harness-fat-skills]] — thin harness, fat skills 設計哲學
- [[karpathy-skills-claude-coding-rules]] — Karpathy 的 skill 規範
- [[ai-build-skills-nick-baumann]] — Nick Baumann 的 skill 建構方法
- [[matt-pocock-ai-code-is-not-cheap]] — 設計介面 = 定義 skill 邊界
