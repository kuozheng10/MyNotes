---
title: Agent 連上正式環境：MCP 串接外部系統實作模式（Anthropic 官方）
tags: ["MCP", "Agent", "架構設計", "Claude", "工具", "自動化"]
date: 2026-04-24
category: AI工具
source: Anthropic 官方文章，Telegram 派哥分享
---

## 核心論點

Agent 能做多少事，取決於它能碰到什麼。連接方式決定了 Agent 的能力邊界。

---

## 三種連接方式比較

| 方式 | 適合場景 | 問題 |
|------|---------|------|
| 直接打 API | 少數整合、快速驗證 | M×N 問題：M 個 Agent × N 個服務，各自管授權/工具描述 |
| CLI | 本地開發、有 container 環境 | 手機/網頁/雲端沒有 shell |
| MCP | 雲端 Agent、正式環境 | 前期建 server 成本較高，但換來可攜性 |

**成熟整合最後三種都做**：API 是基礎，CLI 給本地，MCP 給雲端 Agent。

---

## MCP 規模指標（2026-04）

- MCP SDK 月下載量：3 億次（年初時 1 億）
- 每天數百萬人在 Claude 裡使用 MCP
- Claude Cowork、Managed Agents、Claude Code channels 底層都是 MCP
- 官方 directory：超過 200 個 MCP server

---

## 建好的 MCP Server 設計模式

### 1. 建 Remote Server，不要只做 Local

本地 server 只能跑在有 shell 的環境。Remote server 才能讓網頁、手機、雲端的 Agent 都接得到。所有主要 client 針對 remote server 最佳化。

### 2. 依意圖分組工具（Intent-Grouped）

**不要一對一對映 API**：

```
❌ get_thread → parse_messages → create_issue → link_attachment（4 次呼叫）
✅ create_issue_from_thread（1 次呼叫）
```

### 3. 大型 API 用 Script Sandbox 模式

服務有幾百個操作時（Cloudflare、AWS、Kubernetes），intent-grouped 包不完。

解法：暴露薄工具層 → Agent 寫 script → Server 在 sandbox 跑 → 只回傳結果。

**Cloudflare 案例**：2 個工具（search + execute）涵蓋約 2,500 個 endpoint，只佔 ~1K tokens。

---

## 互動與授權新功能

### MCP Apps
讓工具回傳互動式介面（圖表、表單、dashboard），在聊天介面裡直接呈現。有 MCP Apps 的 server，採用率和留存率明顯更高。

### Elicitation（詢問/引導）
工具執行到一半可以暫停，跟用戶要資料：
- **Form mode**：送 schema → client 端渲染原生表單，可問缺少的參數、確認危險操作
- **URL mode**：把用戶帶到瀏覽器完成 OAuth、付款（憑證不經過 MCP client）

### Vaults（Claude Managed Agents）
雲端 Agent 的 token 管理機制：
- 用戶 OAuth token 只註冊一次
- 建立 session 時指定 vault ID，平台自動注入 credential + 處理 refresh
- 不用自己建 secret store

---

## Client 端省 Context 的兩個模式

### Tool Search（節省 85%+ token）
不一次塞所有工具定義進 context，Agent 需要時才搜尋並載入。
- 效果：砍 85%+ 工具定義 token，工具選擇準確度維持

### Programmatic Tool Calling（節省 37% token）
工具回傳結果先在 code sandbox 處理（迴圈、過濾、聚合），只把處理好的送回 context。
- 效果：複雜多步驟任務省 ~37% token

兩個模式可同時用在多個 server 上。

---

## Skill + MCP 搭配模式

**兩者互補**：MCP 給工具能力，Skill 教 Agent 怎麼用這些工具把事做完。

### 模式 A：Plugin 打包
Skill + MCP server + hooks 打包成 plugin 一起發佈。

Anthropic data plugin for Cowork：10 個 skill + 8 個 MCP server，接 Snowflake/Databricks/BigQuery/Hex。

### 模式 B：MCP Server 附帶 Skill
服務商發佈 MCP server 時同時附上 Skill（使用手冊）。Canva、Notion、Sentry 已在做。

---

## 對派哥的啟示

**目前已在用的**：
- Claude Code 的 MCP（GitHub、notebooklm）= 直接 API 模式
- 沒有建自己的 MCP Server

**值得注意的**：
- Tool Search 省 85% token 的概念：派哥的 CLAUDE.md 裡的「按需讀取」原則和這個一致
- Elicitation URL mode：未來如果要做有 OAuth 的整合，這是比瀏覽器 MCP 更乾淨的方式
- Vaults：等 Claude Managed Agents 穩定後可以用在 cc_processor 的 OAuth token 管理

**短期不需要行動**：除非要建自己的服務給外部 Agent 用，否則先觀察生態演進。

---

## 連結筆記

- [[skill-mcp-security-check]] — MCP 安全掃描 SOP
- [[claude-notebooklm-mcp-5scenarios]] — 實際用 MCP 串 NotebookLM
- [[harness-engineering]] — Agent Harness 四層架構
- [[garry-tan-thin-harness-fat-skills]] — Thin Harness + Fat Skills 哲學
