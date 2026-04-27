---
title: LINE 家庭群組機器人開源模板 — 長輩的好朋友
tags: [LINE, chatbot, n8n, 家庭群組, LLM, 自動化, 開源模板]
date: 2026-04-28
category: AI工具
---

## 這是什麼

LINE 家庭群組 AI 機器人開源模板，對長輩分享的文字/照片/轉傳訊息自動回覆溫暖回應。
GitHub: https://github.com/castlen3/line-family-comment-bot

---

## 技術棧

| 元件 | 說明 |
|------|------|
| n8n | 工作流自動化平台（核心）|
| LLM | LM Studio（本地）/ Gemini API / OpenAI-compatible |
| LINE Messaging API | 群組整合 |
| Ngrok | 本地 n8n 暴露到網路（自架版）|

---

## 主要功能

- 選擇性回覆：只對特定關鍵字、長輩相關內容、圖片、@提及回應（避免太吵）
- 上下文記憶：保留約 5 則最近對話（可調整）
- 保守設計：刻意克制，不會搶話
- 隱私優先：支援本地模型，資料不外送

---

## 安裝方式（非工程師友好）

1. 把 GitHub 網址貼給 Claude Code / Codex
2. 請 agent 依照 AGENTS.md 一步一步帶你安裝
3. 先加自己為 LINE 好友測試
4. 確認沒問題再拉進群組

---

## 對派哥的意義

- 技術棧：n8n + LINE API，和 cc_processor 不同方向
- 如果要做 LINE 版的通知機器人，可以參考這個模板的 webhook 架構
- 目前派哥主要用 Telegram，LINE 群組暫無需求
- 但「AGENTS.md 帶新手安裝」的設計模式值得參考（把安裝 SOP 寫進 AGENTS.md 給 agent 讀）

---

## 連結筆記

- [[hermes-create-telegram-bot-skill]] — Telegram bot 建立 skill
- [[agentcrew-beeper-mcp-messenger-ig]] — 多平台訊息整合
- [[claude-code-line-channel-plugin]] — Claude Code LINE channel 整合
