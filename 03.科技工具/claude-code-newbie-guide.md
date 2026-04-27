---
title: Claude Code 新手該知道的幾件事 — 入門心法與常用指令
tags: [claude-code, 新手, 入門, CLAUDE.md, MCP, agents, commands, tips]
date: 2026-04-28
category: AI工具
---

## 第一句不要問程式碼

問：「這個 Repository 是做什麼的？怎麼跑起來？」
→ 新人 onboard 從讀兩天文件壓縮到幾次對話

---

## 常用指令

| 指令 | 用途 |
|------|------|
| `/clear` | 清空對話 |
| `/compact` | 主動壓縮歷史（別等自動壓縮）|
| `/plan` | 大改動先出方案 |
| `/model` | 切換 Opus / Sonnet / Haiku |
| `/resume` | 恢復對話 |
| `npx ccusage` | 即時監看 Token 消耗 |

---

## 鍵盤與輸入前綴

| 按鍵 | 用途 |
|------|------|
| `ESC` | 打斷輸出 |
| `↑` / `↓` | 翻閱歷史指令 |
| `Shift + Enter` | 換行 |
| `!command` | 直接執行 Shell，輸出進入 Session 供 AI 參考 |

---

## CLAUDE.md = 專案約定手冊

放根目錄，每次會話都讀取。

要寫：
- 約定、禁區、反直覺的地方

不寫：
- 技術棧、目錄結構（AI 掃程式碼就能看到，不要浪費空間）

---

## 文件系統三層架構

| 層 | 路徑 | 用途 |
|----|------|------|
| enterprise | 公司目錄 | 公司強制規範 |
| user | `~/.claude/` | 個人偏好（派哥的主要設定層）|
| project | `.claude/` | 團隊共享，提交 Git |

---

## Commands 固化高頻流程

在 `.claude/commands/` 下建 `review.md`
→ 定義 `/review` 指令
→ 每天重複的工作都能做成自定義命令

---

## Agents 派分身（節省 Context Window）

| Agent | 用途 |
|-------|------|
| Explore | 探索程式碼 |
| Plan | 出方案 |

核心優勢：主會話不被污染，節省大量 Context Window

---

## MCP 接軌外部系統

`claude mcp add playwright`

邏輯：你幫它裝什麼，它就會什麼

---

## 底層工具鏈（不用直接調用）

Read / Edit / Bash / Grep / Write / Agent / WebFetch / LSP

注意：Bash 按命令授權，危險操作謹慎確認

---

## 最重要的心法

> 掌握如何寫出好專案的心法才是最重要的

短時間感覺錯過很多更新，長時間回頭看好像又沒錯過什麼。
慢慢上手的好處：到時只要用最新、最成熟的整合性工具就好。

---

## 連結筆記

- [[boris-15-claude-code-tips]] — Boris Cherny 的 15 個進階技巧（與本篇互補）
- [[claude-code-powerup-guide]] — Claude Code 功能深度解析
- [[karpathy-skills-claude-coding-rules]] — Karpathy 的 AI 開發規範
- [[matt-pocock-ai-code-is-not-cheap]] — 設計介面比寫 code 更重要
