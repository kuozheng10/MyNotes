---
title: "Codex Plugin for Claude Code"
tags: [claude-code, openai, codex, code-review, plugin]
date: 2026-03-31
category: 03.科技工具
source: https://github.com/openai/codex-plugin-cc
---

## 摘要

> OpenAI Codex 的 Claude Code plugin，在 Claude Code 裡直接呼叫 Codex 做 code review 或背景任務執行。⭐ 950

## 功能

| 指令 | 說明 |
|------|------|
| `/codex:review` | 一般 code review |
| `/codex:adversarial-review` | 挑戰性審查（找漏洞、邏輯錯誤） |
| `/codex:rescue` | 把任務委派給 Codex 背景執行 |
| `/codex:status` / `result` / `cancel` | 管理背景任務 |

## 安裝

```bash
/plugin marketplace add openai/codex-plugin-cc
/plugin install codex@openai-codex
/reload-plugins
/codex:setup
```

全域安裝 Codex CLI：
```bash
npm install -g @openai/codex
```

## 需求

- ChatGPT 訂閱（含 Free）或 OpenAI API key
- Node.js 18.18+

## 評估

- **優點**：adversarial review 角度更多元，可補 Claude 的盲點
- **缺點**：需要 OpenAI 訂閱，雙重付費
- **替代方案**：CodeRabbit（Vercel Marketplace）、直接讓 Claude 做嚴格審查

## 相關

- [[my-wallet-trip-setup]]
- [[gmail-automation]]
