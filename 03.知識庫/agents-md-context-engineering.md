---
title: "AGENTS.md：Agent 的導航文件與 Context Engineering"
tags: [Agent, AI, 架構設計, 工作流程, context-engineering, harness, coding-standard, CLAUDE.md]
date: 2026-05-12
category: 03.科技工具
source: Telegram 派哥分享
---

## 核心洞見

> AGENTS.md 不是百科全書，是導航。好的 AGENTS.md 讓 Agent 知道「現在需要什麼資訊，應該去哪裡找」。

## 為什麼 AGENTS.md 重要

Agent 不知道你的團隊默契。沒有文件化的規則，Agent 寫出「可以跑」但不符合維護方式的 code。

典型的隱性團隊規則（沒寫下來 Agent 就不知道）：
- Controller 只處理 request/response
- Business logic 放 Service
- Database access 放 Repository
- DTO 不能直接暴露 Entity
- 新功能要補 unit test

## Harness Engineering 的延伸

Agent 寫出不符規範的 code，不應該只是人類手改那一段。

應該問：
- coding standard 有沒有寫清楚？
- architecture boundary 有沒有文件化？
- CI 有沒有擋下這類錯誤？

**修 output 治標，修系統才治本。**

## 結構建議：導航 + 細節分離

```
AGENTS.md（導航）
├── 這個專案是什麼
├── 重要文件在哪裡
├── 開發遵守什麼規則
└── 哪些地方不能碰

docs/（細節）
├── architecture.md
├── coding-standard.md
├── api-contract.md
├── testing-guide.md
└── runbook.md
```

AGENTS.md 只放指針，細節放 docs/。避免資訊過載讓 Agent 抓不到重點。

## Context Engineering 本質

不是 context 越多越好，而是在正確時間提供正確資訊。

AGENTS.md = 好的路由層，讓 Agent 按需取用正確的 context。

## 對派哥的啟示

CLAUDE.md 已經在做這件事——但目前是「全部擠在同一個檔案」。

可考慮拆分：
- CLAUDE.md 只留導航規則（核心規則 + 工具分工 + 安全天條）
- 詳細的 skill 邏輯移到 `~/.claude/skills/` 各自的 md
- 目前已有這個方向（skills/mynotes.md、skills/bugfix.md），繼續走就對了

## 連結筆記

- [[harness-engineering]] — Harness Engineering 核心概念（Agent = Model + Harness）
- [[claude-md-optimization]] — CLAUDE.md 優化策略
- [[claude-md-on-demand-optimization]] — 按需載入 CLAUDE.md
- [[garry-tan-thin-harness-fat-skills]] — 薄 Harness 厚 Skills 架構
