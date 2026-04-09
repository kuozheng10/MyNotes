---
title: Toonify MCP — Claude Token 壓縮工具，平均省 60%
tags: [MCP, token, claude-code, 省錢, 工具, 壓縮]
date: 2026-04-09
category: AI工具
source: https://github.com/kevintseng/toonify-mcp
---

## 這是什麼

MCP 工具，在資料丟進 Claude 之前**先整理、壓縮內容**。
官方宣稱平均減少 60% token 用量，等於同樣對話可以撐更久。

---

## 安裝

```bash
npm install -g toonify-mcp
```

---

## 適合場景

- 餵入大文件（PDF / 程式碼 / 長文）
- 對話已很深、接近 token 上限時
- 不想重開 session 但快爆了

---

## 對派哥的啟示

- **搭配 save-token.skill 用**：save-token 控回覆行為，Toonify 控輸入壓縮，雙管齊下
- **搭配 session-reset-hello schedule**：session 不容易爆，搭配壓縮輸入 = 最省
- 先試安裝看看實際壓縮效果，對 cc_processor / MyNotes SOP 的長文處理特別有用

---

## 連結筆記
- [[claude-token-saving-tips]] — Claude Code 省 token 10 招
- [[prompt-cache-llm-mechanism]] — Prompt Cache 保護原則
- [[agent-prompt-token-cost]] — 中文 prompt token 成本
