---
title: "AI 開發工作流：iTerm2 + tmux + Claude hook notification"
tags: [claude-code, workflow, tmux, iterm2, parallel, productivity]
date: 2026-04-14
category: AI工具
---

## 核心架構

每個專案一個 tmux window，拆 3 個 pane：

- Agent Skill 執行（openspec + subagent）
- Server logs 監控
- Task 進度追蹤

## 多專案並行

同時跑 2-3 個專案（前後端並行），卡住時右上角自動通知對應 session，只需切 tab 去看 + 與 Agent 互動。

單一大專案：一個 window 對一個 worktree 資料夾，拆開跑。

## 使用哲學

Agent 自己跑，人負責監控 + 關鍵決策。一週只需花一天在專案上，其他時間研究新 skills 或自己的東西。
