---
title: 自建開源爬蟲省錢方案：Crawlee 與 DrissionPage
tags: ["工具", "自動化", "Python", "開發工具"]
date: 2026-04-17
category: 開發工具
source: goodarticle/2026-04-15_自建開源爬蟲省錢方案.md
---

## 這是什麼
介紹如何透過開源框架（如 Crawlee 與 DrissionPage）自建爬蟲架構，以取代昂貴的 SaaS 服務，在個人伺服器上實現高效、低成本且具備防偵測功能的數據採集方案。

## 核心概念
* **Crawlee (Node.js)**：由 Apify 官方開源，目前最強的 Node.js 爬蟲框架。內建自動切換 Proxy、瀏覽器指紋偽裝與防偵測機制，適合大規模抓取並規避 Apify 昂貴的計費。
* **DrissionPage (Python)**：結合了 Selenium 的強大模擬功能與 Requests 的高執行速度。其設計理念是不容易被網站檢測為機器人，非常適合處理複雜的登入邏輯或重度依賴 JavaScript 的動態網頁。
* **省錢關鍵**：將爬蟲部署在自己的 VPS 而非使用雲端代管服務，可繞過按量計費的限制。

## 使用方法 / 快速啟動
* **Crawlee**：適合習慣 JavaScript/TypeScript 的開發者，直接從 npm 安裝後，利用其內建的 `PlaywrightCrawler` 或 `CheerioCrawler` 快速啟動。
* **DrissionPage**：適合 Python 開發者，透過 `pip install DrissionPage` 安裝，即可在同一套 API 下切換「收發封包模式」與「瀏覽器控制模式」。

## 對派哥的啟示
派哥在開發財務自動化工具（如 `cathay_statement.py` 或信用卡處理器）時，經常需要處理銀行網頁的數據抓取。
1. **穩定抓取財務資料**：使用 DrissionPage 可以更輕易地處理銀行官網複雜的登入驗證與動態跳轉，且不容易被封鎖。
2. **降低維運成本**：目前的專案如 `sales_report_processor.py` 若需擴充網頁抓取功能，採用這些開源方案能確保工具在長期運作下維持極低成本，符合派哥開發輕量化、高效能自動化工具的風格。

## 連結筆記
## 連結筆記
- [[claude-code-powerup-guide]]
- [[claude-routines-automation]]
- [[full-agent-dev-ecosystem-goatwang]]
- [[claude-code-feature-workflow]]
- [[codex-plugin-cc]]
