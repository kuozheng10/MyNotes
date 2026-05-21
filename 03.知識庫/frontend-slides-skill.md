---
title: "Frontend Slides — Claude Code 一鍵生成 HTML 簡報"
url: "https://github.com/zarazhangrui/frontend-slides"
tags: [claude-code, skill, slides, presentation, html, design]
date: 2026-04-06
category: 03.科技工具
source: Telegram 分享
---

## 摘要

> Claude Code skill，用自然語言描述就能生成動態 HTML 簡報，也能把 .pptx 轉成網頁投影片。零依賴，單一 HTML 檔案。

## 功能

- 描述內容 → 先顯示風格預覽選項 → 生成完整簡報（不用猜設計）
- 直接丟 .pptx → 自動提取文字/圖片/備注 → 轉成網頁版
- 12 種預設風格（深色/淺色/Neon/Terminal 等）
- 可 deploy 到 Vercel 或匯出 PDF（Playwright）

## 安裝

```bash
git clone https://github.com/zarazhangrui/frontend-slides ~/.claude/skills/frontend-slides
```

使用：在 Claude Code 輸入 `/frontend-slides`

## 評估：對派哥有用嗎？

**偶爾有用。** 需要做簡報的時候可以用，省掉開 Keynote/PowerPoint 的時間。
最實用場景：快速做一個技術說明的投影片，或把現有 pptx 轉成可以丟 URL 分享的網頁版。

不需要包成 skill（它本身就是 skill，直接 clone 就好）。

## 相關筆記

- [[awesome-design-md]] — 大廠設計語言參考（做 UI 時用）
- [[ui-ux-pro-max-skill]] — 設計系統 skill
