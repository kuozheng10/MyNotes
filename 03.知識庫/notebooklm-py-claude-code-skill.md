---
title: "notebooklm-py — Claude Code 自動操控 NotebookLM 的 Python 工具"
url: "https://github.com/teng-lin/notebooklm-py"
tags: [notebooklm, claude-code, skill, python, rag, automation]
date: 2026-05-10
category: 03.科技工具
source: Telegram 派哥分享
---

## 摘要

> 非官方 NotebookLM Python API + Claude Code Skill，讓腳本程式化操控 NotebookLM：上傳來源、生成音訊摘要（MP3）、投影片、測驗、問答。

## 核心能力

- 上傳來源（PDF、URL、YouTube、Google Drive、本地檔案）
- 生成音訊概覽（Podcast MP3）、簡報、Quiz、心智圖
- RAG 問答（對已上傳來源自動提問）
- 附帶 SKILL.md，可直接裝進 Claude Code

## 安裝

```bash
pip install "notebooklm-py[browser]"
playwright install chromium
notebooklm login  # 一次性，開瀏覽器登入 Google
```

後續 API 呼叫走逆向工程的 Protobuf RPC，不需要持續開瀏覽器。

## 安裝 Skill

```bash
git clone https://github.com/teng-lin/notebooklm-py.git
cp notebooklm-py/SKILL.md ~/.claude/skills/notebooklm.md
```

## 對派哥的評估

**不需要立刻裝。**

派哥已有的替代方案：
- MyNotes RAG（mcp__mynotes-rag）— 本地筆記搜尋已解決
- claude-notebooklm-mcp-5scenarios — MCP 串 NotebookLM 已涵蓋互動場景

**唯一有差異化價值的功能**：音訊摘要生成（MP3 Podcast）
— 如果想把 MyNotes 某篇筆記自動做成可以「聽」的摘要，這是目前沒有的工作流。

**風險**：
- 非官方 API，Google 改協定就壞掉
- 違反 Google ToS 的灰色地帶
- 帳號自動化有封號疑慮

## 和現有筆記的關係

| | notebooklm-py | claude-notebooklm-mcp-5scenarios |
|--|--|--|
| 層次 | Python 腳本批次自動化 | Claude 即時 MCP 互動 |
| 用途 | 上傳/生成/下載（無人值守）| 對話式查詢/研究 |
| 結合 | 可互補：py 負責上傳，MCP 負責查詢 | |

**不建議合併**，兩者角色不同，各自獨立更清楚。

## 相關筆記

- [[claude-notebooklm-mcp-5scenarios]] — MCP 即時互動場景
- [[notebooklm-professional-rag-limits]] — NotebookLM RAG 的限制
- [[notebooklm-gemini-deep-integration]] — Gemini 深度整合
