---
title: "Agent Skills — 跨工具開放標準"
url: "https://agentskills.io"
tags: [claude-code, skill, open-standard, cross-tool]
date: 2026-04-07
category: 03.科技工具
source: Telegram 派哥分享（高見龍文章）
---

## 摘要

> Agent Skills 是 Anthropic 開發、現已開放的跨工具 skill 格式標準。Claude Code 用的 SKILL.md 格式就是這個標準，目前已被 30+ AI 開發工具支援。

## 重點

- **跨工具可攜**：同一個 skill 可在 Claude Code、Cursor、GitHub Copilot、VS Code、Gemini CLI、OpenCode 等工具使用
- **開放標準**：原由 Anthropic 開發，現在社群共同維護
- **格式簡單**：一個 SKILL.md 檔，含 frontmatter（name, description, triggers）+ prompt 內容

## 官方資源

- **Anthropic 官方示範 skill 庫**：https://github.com/anthropics/skills
- **規格文件**：https://agentskills.io/specification
- **討論 Discord**：https://discord.gg/MKPE9g8aUy

## 高見龍教學文

- 說明 skill 原理，示範做 `commit-message-helper`（Conventional Commits 規範）
- 適合初次了解 skill 格式的讀者

## 對派哥的實用建議

1. 翻 `github.com/anthropics/skills` — 看有沒有現成可用的
2. 寫 skill 時用標準 SKILL.md 格式 — 以後換工具也帶走，不鎖定 Claude Code

## 相關筆記

- [[grill-me-skill]] — 壓力測試設計的 skill（符合此標準）
- [[frontend-slides-skill]] — HTML 投影片 skill（符合此標準）
- [[caveman-skill]] — 省 token skill
