---
title: "Dcard GNTC：Agent-Native 企業轉型的關鍵拼圖"
tags: [AI, agent, enterprise, Dcard, GNTC, harness-layer, AX, governance, VibeHost, EntryDesk]
date: 2026-05-29
category: 03.知識庫
source: Dcard 創辦人 Kytu 文章
---

## GNTC 是什麼

Dcard 成立的企業 AI Agent 事業。

名字由來：`AGENTIC` 去掉 `E-AI`（Enterprise AI）= **GNTC**

核心主張：單純導入 Enterprise AI 不夠，還需要治理、工具、流程、組織變革等關鍵拼圖，才能讓公司真正變得 Agentic。

## 兩款產品

### EntryDesk
- 起源：MCP Gateway，把公司所有權限控制在一起
- 解決問題：同事不懂 Terminal，無法快速 onboard Coding Agent
- 目標：不需要懂程式，一秒 onboard，驅動 Agent 發揮價值

### VibeHost
- 起源：當所有人都能用 Agent 產出 Prototype，「分享」成了問題
- 解決問題：現有部署方案太貴（per-seat $20+/月，密碼鎖 $150+/月），設計給工程師
- 設計原則：Workspace 定價，5-10 人小團隊或百人組織都能用
- 特色：AX First（Agent Experience 優先）

## 企業導入 Agent 最重要的兩件事

| 挑戰 | 說明 |
|------|------|
| **治理 (Governance)** | RBAC、ABAC、Approval、Audit；人員到職/離職/轉調時權限如何流動 |
| **易用性** | 在保證治理的基礎上，讓一線夥伴真的用得起來 |

> Agent-Native ≠ 只有 IT 懂 Agent、一個一個部門導入。而是讓一線夥伴能自己打造需要的 Agent。

## AX (Agent Experience) — 新設計課題

過去 20 年：**UX** — 讓人容易理解、順利完成任務

Agent-Native 未來：**AX** — 產品能否被 Agent 快速理解、正確操作、遇到障礙時自行排除

> 產品的使用者不只是人，也會是 Agent。

## Harness Layer 概念

```
LLM = 電
Harness Layer = 電器系統
```

要讓電（LLM）在企業發揮價值，需要 Harness Layer：治理、權限、workflow、人機介面。

## Agent 導入的正回饋循環

1. 辦 Workshop，手把手設定好環境
2. 實作一兩個真實工作場景的 Agent
3. 有人表現出色 → 讓全公司看到 → 激發榮譽感
4. 從「恐懼 Agent」→「發現可能性」→ 自我快速迭代

一旦觸發這個轉折點，不需要人教，自然快速進步。

## 派哥啟示

Dcard 走過的路（MCP Gateway → Agent 介面 → 治理 → AX）和 MyClaude 的架構高度吻合：

| Dcard | MyClaude 對應 |
|-------|--------------|
| MCP Gateway | Claude Code + MCP tools |
| EntryDesk | Telegram bot / skills |
| Harness Layer | CLAUDE.md / skills / cc_processor |
| 治理 | 白名單、env.sh、prompt injection 防線 |
| VibeHost | Vercel 部署的 dashboard |

差異：Dcard 在做 B2B 產品化，派哥在做個人自動化。核心能力重疊度高。
