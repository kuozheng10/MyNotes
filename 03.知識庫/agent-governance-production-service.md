---
title: "Agent 治理：把 AI Agent 當 Production Service 管"
tags: [Agent, AI, 架構設計, 安全, 企業, governance, telemetry, human-in-the-loop]
date: 2026-05-12
category: 03.科技工具
source: Telegram 派哥分享
---

## 核心論點

不要問「怎麼雇用 AI 員工」，要問「怎麼建立可信任的 AI 基礎設施」。

> Don't hire AI employees. Build AI infrastructure.

## Agent 應具備的五個治理層

**1. Clear Owner**
業務 owner、技術 owner、風險 owner — 每個 Agent 都要有人負責。

**2. Policy Layer**
明確定義：什麼可以做，什麼不能做。

**3. Decision Telemetry**
每一次 tool call、memory read/write、decision trace 都要有紀錄。
沒有 telemetry = 黑盒子 = 無法審計。

**4. Guardian Check**
每個操作都經過：Allow / Review / Block 三態判斷。

**5. Human Escalation Path**
高風險操作必須有人接手，不能讓 Agent 自行決策到底。

## 為什麼重要

把 Agent 當「員工」的思維，會讓人聚焦在「讓 Agent 更聰明」；
把 Agent 當「infrastructure」，才會去建可觀測性、策略層、人工介入點。

企業導入 Agentic AI 的真正門檻，不是模型能力，而是治理框架。

## 對派哥的啟示

現有 cc_processor + Hermes + Flashcard Bot 都是 Agent：
- cc_processor 已有 `TRUSTED_SENDER_DOMAINS`（Policy Layer 雛形）
- 缺的是：Decision Telemetry（每次處理帳單有無 log？）和 Guardian Check（高金額交易是否需人確認？）
- Hermes 的 SOUL.md = Policy Layer，但缺 escalation path

下一步可考慮：在 cc_processor 加結構化 log（每筆帳單處理結果），異常金額 > N 元時 Telegram 通知確認。

## 連結筆記

- [[anthropic-agent-infra-strategy]] — Anthropic 的 Agent 基礎設施策略
- [[ai-agent-system-design-over-prompt]] — 系統設計 > Prompt 工程
- [[atr-agent-threat-rules-panguard]] — Agent 威脅規則
- [[claude-subagent-context-management]] — Subagent context 管理
