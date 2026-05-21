---
title: "CLI Printing Press — 把 API/網站變成 AI Agent 專用 CLI"
url: "https://github.com/mvanhorn/cli-printing-press"
tags: [claude-code, mcp, cli, agent-tools, workflow, skill]
date: 2026-05-09
category: 03.科技工具
source: Telegram 派哥分享
---

## 摘要

> 把 API 文件、HAR 檔或網站，自動生成 AI Agent 原生的 Go CLI、MCP Server 和 Claude Code Skill（SKILL.md）。讓 Agent 不用每次重新摸索 API，直接呼叫穩定指令。

## 核心概念

**問題**：AI Agent 操作外部服務時，每次都要重新讀文件、猜 API、處理格式。

**解法**：把服務「壓縮」成 Agent 可直接呼叫的 CLI 工具 + 本地 SQLite 鏡像，搜尋快、省 token、行為可預期。

**一次生成三種產物**：
- Go CLI（靜態二進制）
- MCP Server（直接串 Claude Desktop）
- SKILL.md（Claude Code 直接讀取）

## 使用流程

```bash
# 安裝
go install github.com/mvanhorn/cli-printing-press/v4/cmd/printing-press@latest

# 印刷（掃 OpenAPI spec / 網址 / HAR 檔）
printing-press <資料源>

# 輸出：binary + mcp config + SKILL.md
```

1. 準備資料源（OpenAPI spec、網址、HAR 側錄）
2. 執行印刷，系統跑「行為證明」（路徑/參數/認證評分）
3. 部署 binary 或 MCP Server

## 預製工具（starter-pack）

官方 `mvanhorn/printing-press-library` 有 50+ 個預印好的 CLI：
- espn（即時賽事）、flight-goat（機票）、movie-goat、recipe-goat
- PyPI、Product Hunt 等

## 和 Claude Code 整合

- **SKILL.md 直接用**：產出的 skill 讓 Claude 知道所有指令和邊界
- **MCP 串接**：產出的 MCP Server 讓 Claude 直接 tool use 操作本地資料
- **減少 round-trip**：複雜 API 流程封裝成複合指令，Agent 不用拆解每一步

## 對派哥的評估

適合場景：
- 常用但沒有現成 MCP 的服務（e.g. 長榮查票、特定台灣網站）
- 想讓 Claude Code 穩定操作某個 API，不想每次重寫 prompt
- 替 OpenClaw / cc_processor 生成更多工具

暫時用不到：派哥目前服務都有現成方案（Gmail MCP、Google Calendar、Notion MCP）

## 限制

- 初始 SQLite 鏡像同步耗時（大資料量）
- 複雜 OAuth 可能需手動調整生成的 Go code
- API 結構大改需重跑印刷流程
- 需要有 Go 環境

## 相關筆記

- [[addyosmani-agent-skills]] — 也是替 Agent 加 skill 的方向
- [[anthropic-mcp-production-patterns]] — MCP 整合模式
- [[codex-chrome-browser-plugin]] — 另一種讓 Agent 操作外部服務的方法
