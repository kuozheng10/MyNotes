---
title: 瀏覽器自動化六種方法與 Agent 應用場景
tags: [瀏覽器自動化, OpenClaw, BrowserUse, Firecrawl, Camofox, CDP, 爬蟲, AI Agent]
date: 2026-05-08
category: AI工具
---

## 核心結論

瀏覽器自動化理論上可以取代多模態模型（生圖/影片/音樂），但穩定度不佳、前端等待久。
個人用可接受，生產環境還是付費 API 比較可靠。

---

## 六種瀏覽器自動化方法（HermesAgent 整理）

| 方法 | 特性 |
|------|------|
| BrowserUse | 通用瀏覽器自動化框架 |
| Firecrawl | 付費訂閱，穩定可靠 |
| Camofox | 擬人化爬蟲，較難被偵測 |
| AgentBrowser | Agent 導向操作 |
| CDP 9222 | 主流走法，透過 Chrome DevTools Protocol |
| OpenCLI 快閃爬法 | 快速但不像人類行為 |

---

## 免費生影片方案（個人用）

Google 基本訂閱 + Flow + Opal + 瀏覽器自動化：
- Opal 每天 10 部影片額度，串 Agent 自動完成

進階版（有 Grok）：
- ChatGPT (Codex) 生圖 → Grok 生影片 → 全流程在 Agent 完成
- 缺點：Grok 有防機器人機制，穩定度差，不好串

---

## 最佳使用場景

**資料收集（大量爬取）** = 瀏覽器自動化最大優勢

---

## 連結參考

- [[openclaw-hermes-collaboration]] — OpenClaw 協作模式
- [[self-hosted-scraper-solution]] — 自架爬蟲方案
- [[agentcrew-beeper-mcp-messenger-ig]] — Agent 自動化整合
