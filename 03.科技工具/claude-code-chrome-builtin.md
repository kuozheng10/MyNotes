---
title: Claude Code --chrome 內建瀏覽器功能，不需要 Playwright MCP
tags: [claude-code, chrome, browser, mcp, playwright, 省錢]
date: 2026-04-10
category: AI工具
---

## 這是什麼

Claude Code 內建 Chrome 整合，啟動時加 `--chrome` 旗標即可操控瀏覽器。
不需要另外裝 Playwright MCP。

```bash
claude --chrome
```

---

## 啟用後可用工具

`mcp__claude-in-chrome__*` 工具組：
- `navigate` — 開啟網頁
- `click` — 點擊元素
- `read_page` — 讀取頁面內容
- 以及更多瀏覽器操作工具

---

## 應用場景

| 場景 | 做法 |
|------|------|
| 查每日股市/新聞 | 直接開網頁抓，不靠 Gemini CLI |
| Debug 網站 | 開瀏覽器看實際渲染 |
| 查詢訂位/票價 | 直接操控網頁 |
| 排程每日資訊 | `claude --chrome` 搭配 cron |

---

## 對現有工作流的影響

- **晨報美股資訊**：可改用 `--chrome` 直接抓，不依賴 Gemini CLI（解決 Gemini 掛住問題）
- **Playwright MCP**：可評估移除，功能已被內建取代
- **inbox SOP URL 摘要**：可考慮用 `--chrome read_page` 取代 Gemini CLI 抓網頁內容

---

## 連結筆記
- [[claude-code-powerup-guide]] — Claude Code 10 大功能
- [[claude-token-saving-tips]] — Claude 省 token 策略
- [[feedback_playwright_mcp]] — Playwright MCP 使用時機
