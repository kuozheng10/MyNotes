---
title: "Leeway：YAML 決策樹控制 AI Agent 執行順序"
tags: [ai-agent, yaml, workflow, decision-tree, deterministic, human-in-the-loop]
date: 2026-04-14
category: AI工具
---

## 解決什麼問題

AI Agent 每次執行順序不固定，無法重現也難以稽核。即使寫了嚴密 system prompt，也難鎖死流程。

## 核心機制

用 YAML 定義工作流程為決策樹：

- 每個節點 = 獨立 agent loop，可精確指定權限（MCP server、skill、檔案、shell 指令）
- 節點執行完後，LLM 回傳訊號（例如 "passed" / "needs_fix"）
- Agent 根據訊號決定下一條路徑
- 同樣流程跑 100 次，順序一致

## vs 其他工具

| | Leeway | OpenClaw 類 | n8n |
|---|---|---|---|
| 流程控制 | YAML 決策樹 | LLM 主導 | Visual node editor |
| 適合場景 | 本地 codebase | 開放式探索 | SaaS 串接 |
| 可重現性 | 高 | 低 | 高 |

## 特點

- Human-in-the-loop 是預設行為（不是選配）
- 敏感操作有審核機制 + 唯讀計畫模式
- Python + React/Ink TUI，支援 OpenAI / Anthropic 等
- MIT 開源

## 評估

適合需要可稽核、可重現的工程流程。「讓模型解題，讓流程圖控方向」——比完全讓 LLM 自由發揮更穩定，比 n8n 更貼近開發場景。
