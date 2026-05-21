---
title: Claude Subagent 上下文繼承與配置指南
tags: ["AI", "Agent", "Claude", "架構設計"]
date: 2026-04-17
category: 開發工具
source: goodarticle/2026-04-17_Subagent_上下文清單.md
---

## 這是什麼
本文解析 Claude Subagent 啟動時的環境繼承機制，明確界定子代理在「空白狀態」下會攜帶哪些主對話的上下文資訊，以及如何透過配置進行限縮。

## 核心概念
- **自動繼承機制**：Subagent 預設會繼承主對話的 MCP 伺服器、工具權限、權限上下文（Permission Context）以及當前工作目錄（CWD）。
- **規則載入路徑**：會自動載入全域（`~/.claude/CLAUDE.md`）與專案（`./.claude/CLAUDE.md`）的規則檔案，包含所有經由 `@-import` 引入的規範。
- **精確控制欄位**：
    - `mcpServers`：用於限縮或新增子代理可用的 MCP 工具。
    - `tools` / `disallowedTools`：建立工具呼叫的白名單或黑名單。
    - `permissionMode`：可覆蓋從主對話繼承而來的權限模式。

## 使用方法 / 快速啟動
若需客製化 Subagent 的執行環境，可在 frontmatter 進行配置：
1. **限縮權限**：使用 `disallowedTools` 禁用具破壞性的工具，確保子代理在安全邊界內執行。
2. **定義規則**：在專案根目錄建立 `.claude/CLAUDE.md`，將開發規範與工作流程寫入，子代理啟動時將自動遵循這些指令。
3. **環境隔離**：透過 `mcpServers` 欄位指定特定的伺服器，避免子代理過度消耗主對話的 MCP 資源。

## 對派哥的啟示
在開發 OpenClaw 自動化 AI 工具時，這套繼承邏輯非常重要：
- **安全性優化**：派哥在台灣開發的自動化流程若涉及敏感資料（如財務或個人筆記），應利用 `disallowedTools` 預防 Subagent 誤刪除或誤改核心配置。
- **規範統一化**：將 OpenClaw 的 `IDENTITY.md` 或 `SOUL.md` 邏輯整合進 `CLAUDE.md`，能確保即便是在深層的 Subagent 呼叫中，AI 依然能維持一致的人格設定與作業標準。
- **模組化開發**：針對不同的自動化任務（如 Telegram 閘道器或 Google 財經抓取），可以為其子代理配置專屬的 MCP 白名單，提升執行效率並減少 token 浪費。

## 連結筆記
## 連結筆記
- [[ai-agent-modular-architecture]]
- [[ai-agent-system-design-over-prompt]]
- [[claude-managed-agents-beta]]
- [[ai-agent-hermes-openab-openclaw-comparison]]
- [[dual-agent-dev-loop]]
