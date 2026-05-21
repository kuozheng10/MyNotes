---
title: "Claude Code：建立 AI 開發團隊的 4 層架構"
tags: [claude-code, agent, sub-agent, skills, 架構設計, 工作流程, 分工]
date: 2026-05-14
category: 03.科技工具
source: Telegram 追蹤者分享
---

## 核心思維轉換

不是「叫 AI 寫 code」，而是「建立可分工的 AI 開發團隊」。

> 我能不能把自己的開發工作流，拆成一組可分工的 AI 團隊？

## 成熟的 4 層架構

| 層次 | 角色 | 負責什麼 |
|------|------|---------|
| **Agent** | 主對話 | 統籌任務、規劃、協調、整合結果 |
| **Sub-agent** | 專業分身 | 特定任務執行、摘要回報給主 Agent |
| **Skills** | 流程封裝 | 可重複使用的工作程序 |
| **Tools / MCP** | 外部接入 | 連接外部服務與資料 |

## Sub-agent 設計的 4 個問題

建立 Sub-agent 前必須先回答清楚：

1. **它負責什麼**：code review / 跑測試 / 整理文件 / 分析錯誤
2. **什麼時候呼叫它**：寫在 `description`，讓 Claude Code 自動判斷委派時機
3. **它可以用哪些工具**：例如只給 `Read, Glob, Grep` = 只能讀不能改
4. **它要不要改檔案**：很多時候只需要「看清楚、說明白、給建議」

> Sub-agent 不是越萬能越好，邊界越清楚越好。

## 建立方式

**App 版**（適合新手）：`/agents` 互動介面管理

**CLI 版**（適合團隊/跨專案）：
```
# 專案層級（跟 repo 走，可版本控制）
.claude/agents/code-reviewer.md

# 個人層級（跨專案可用）
~/.claude/agents/code-reviewer.md
```

## 實作範例：code-reviewer sub-agent

觸發方式：
> 請使用 code-reviewer 檢查我剛剛修改的登入功能，確認是否有安全性、命名與錯誤處理問題。

Sub-agent 先審查回報 → 主 Agent 決定是否修改 → 更穩健的協作方式

## 對派哥的啟示

派哥的架構其實已在實作這 4 層：
- Agent：主對話（Claude Code）
- Sub-agent：`~/.claude/agents/` 裡的 code-reviewer、Gemini 審安全邏輯
- Skills：`~/.claude/skills/` 下的各種 skill
- Tools/MCP：Twinkle Hub、Gmail MCP、Google Calendar MCP

**還沒做的**：
- Sub-agent 的 `description` 欄位寫清楚觸發時機（讓 Claude Code 自動委派，不用手動說）
- 工具白名單：例如 code-reviewer 限定只有 Read/Glob/Grep，防止誤改

## 連結筆記

- [[claude-subagent-context-management]] — Sub-agent context 繼承技術細節
- [[claude-code-subagent-environment]] — Sub-agent 初始環境與內建代理
- [[addy-osmani-harness-engineering-deep-dive]] — Sub-agent 是 harness 的 orchestration 層
- [[garry-tan-thin-harness-fat-skills]] — 薄 Harness 厚 Skills
- [[addyosmani-agent-skills]] — Addy 的 19 個 agent skills 套件
