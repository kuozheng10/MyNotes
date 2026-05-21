---
title: Claude Code vs Codex Desktop SSH 遠端模式差異
tags: [Claude Code, 工具, 架構設計, 工作流程]
date: 2026-05-19
category: AI工具
source: telegram/手打
---

## 這是什麼

兩個都叫「SSH 遠端」，但底層邏輯不一樣，搞混會踩到帳號、額度、MCP 配置的坑。

---

## 核心差異

| 面向 | Claude Desktop SSH | Codex Desktop SSH |
|------|-------------------|------------------|
| 主導方 | 本機 Desktop session | 遠端 host |
| 遠端安裝 | 自動幫你裝 Claude Code | 遠端要先裝好 Codex + authenticate |
| Runtime 位置 | 遠端跑 Claude Code | 遠端跑 Codex app-server |
| 帳號/額度 | 偏向本機帳號 | 偏向遠端 credential |

---

## 三個容易搞混的地方

### 1. 額度扣誰

- 私人 Claude Desktop → 公司機器：吃私人 Claude 帳號額度，但操作公司 repo
- 私人 Codex App → 公司機器（公司帳號登入）：Codex 偏向遠端那套 credential

官方文件沒寫死「本機跟遠端不同帳號扣哪邊」，但從架構看方向不一樣。

### 2. MCP / Skills 看哪裡

**關鍵原則：不要用「我本機有裝」來判斷，要看 runtime 在哪台機器。**

- Claude Desktop SSH：runtime 在遠端 → `.claude/skills`、`~/.claude`、`.mcp.json` 都是遠端的
- Codex Remote：直接以 host 為主機，projects/credentials/MCP 全看遠端設定
- stdio MCP（npx、Python script）：要確保遠端能跑，不能假設本機有裝就行
- 跨本機和遠端都要穩的 MCP：優先用 **HTTP MCP**

### 3. CLI 模式

- Claude CLI：沒有 `claude --ssh host` 模式，純 CLI 就自己 ssh 進去跑 `claude`
- Codex CLI：有 `codex --remote ws://...` 接 app-server，可搭 SSH port forwarding

「點 UI 選 SSH host」= Desktop App 功能。純 CLI 遠端是另一回事。

---

## 最容易出事的組合

私人帳號 + 公司 repo + 遠端 MCP + SSH agent 四個混在一起 → billing 跟資料流向不在同一條線。

---

## 建議做法

- 團隊共用的 rules/skills/MCP → 放 repo 裡（`.claude/`）
- 個人工具 → 放 user home
- 跨環境穩定的 MCP → 用 HTTP MCP，不用 stdio
- stdio MCP → 確認遠端 runtime 能跑，不能只看本機

---

## 連結筆記

- [[anthropic-mcp-production-patterns]] — MCP 生產環境模式
- [[claude-code-subagent-environment]] — subagent 環境隔離
- [[claude-code-powerup-guide]] — Claude Code 基本功
