---
title: Shannon — AI 驅動的主動式安全測試工具
tags: [資安, ai-security, penetration-testing, devSecOps, 漏洞驗證, 必學]
date: 2026-05-20
category: AI工具
source: https://github.com/KeygraphHQ/shannon
---

## 這是什麼

Shannon 是 AI 安全測試員，讀你的網站程式碼、找漏洞、然後**真的去測試漏洞能不能被利用**。

差別：
- 一般 SAST 工具：「這裡可能有洞」→ 靜態分析，誤報多
- Shannon：「這個洞真的打穿了」→ 主動驗證，有 PoC

## 核心能力

1. **程式碼讀取**：分析 web app 程式碼，找攻擊面
2. **漏洞驗證**：自動產生 exploit，實際打看看能不能成功
3. **報告輸出**：已驗證的漏洞才列出，減少雜訊

## 適合誰用

- 上線前想做安全檢查的開發者
- DevSecOps 團隊
- 想驗收第三方滲透測試的人

> ⚠️ 法律邊界：只能測自己的系統或已取得授權的系統。未授權掃描他人網站違法。

## 對派哥的評估

**值得備用**，但現在不是核心需求。

| 情境 | 適用程度 |
|------|---------|
| My Wallet Trip（Vercel PWA，對外） | ✅ 上線前可以跑一次 |
| cc_processor（本地 Python 腳本） | ❌ 不是 web app，不適用 |
| 新 web 功能上線前安全檢查 | ✅ 正好 |

安裝等有需要再裝，不急。

## 連結筆記

- [[ai-code-review-security-risk]] — AI 寫的安全邏輯要用 Gemini 交叉審
- [[skill-mcp-security-check]] — MCP/skill 安全審查三方流程
- [[vibe-coding-rce-heredoc-three-rules]] — heredoc 安全規則
