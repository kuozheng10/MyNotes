---
title: Multica：把 AI Agent 變成可派工的團隊成員
tags: [agent, multi-agent, workflow, openclaw, claude-code, self-hosted]
date: 2026-04-27
category: AI工具
---

## 是什麼

開源 Agent 協作後台，讓你像用 Jira 一樣發 Issue 給 AI Agent。
GitHub: https://github.com/multica-ai/multica（21.4k ⭐ / 2.6k forks）

Agent 收到工單 → 自己領取 → 寫 code → 即時串流進度 → 遇到問題回報 → 成功經驗沉澱成技能池。

## 架構

| 層 | 技術 |
|----|------|
| Frontend | Next.js 16 App Router |
| Backend | Go + Chi + WebSocket |
| Database | PostgreSQL 17 + pgvector |
| Runtime | 本機 daemon 執行 agent CLI |

## 支援的 Agent CLI

Claude Code、Codex、OpenClaw、OpenCode、Hermes、Gemini、Pi、Cursor Agent
→ daemon 自動偵測 PATH 裡有哪些，免手動設定

## 部署選項

| 方式 | 說明 |
|------|------|
| Cloud（預設） | 連官方雲端，省事但不適合機密程式碼 |
| Self-hosted | Docker 部署，`--with-server`，程式碼不外泄 |

**安全提醒**：有公司/個人機密 code，一定要用 self-hosted。預設會連回官方雲端。

## 安裝（macOS）

```bash
brew install multica-ai/tap/multica
multica setup   # 自動偵測環境裡的 agent CLI
```

## 對派哥有沒有用？

**有，但不急。**

適合的場景：
- 同時跑多個 AI agent 執行不同任務
- 想要一個「派工看板」追蹤進度，不用一直盯著 TG
- 讓 OpenClaw + Claude Code 各司其職，統一管理

目前不急的原因：
- 你現在的任務量還不到需要「看板管理」的程度
- Self-hosted 需要跑 Docker + PostgreSQL，維護成本不低
- 先觀察文章作者 OpenClaw 接上的實驗結果

## 值得做 Skill？

還不急。觀望到有 OpenClaw 接上的實作紀錄再評估。
