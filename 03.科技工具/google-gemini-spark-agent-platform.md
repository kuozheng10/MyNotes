---
title: Google Gemini Spark：24小時背景自主 AI Agent 平台
tags: [AI, Agent, 自動化, 工作流程, Google]
date: 2026-05-19
category: AI工具
source: telegram/手打 + Gemini CLI 研究
---

## 這是什麼

Google I/O 2026/5 發表。Gemini Spark 是跑在 Google Cloud VM 上的自主 AI Agent，不用你盯著，24 小時背景跑、跨 Google Workspace 自動化。

---

## 核心能力

- **24/7 背景跑**：設定「守護任務（Guardians）」，你關電腦它還在跑
- **自然語言下令（No-Code）**：不用寫程式，口語描述工作流就行
- **跨應用鏈式觸發**：Gmail → Sheets → Docs → Calendar 全部串起來

---

## 串接方式

| 服務 | 能做什麼 |
|------|---------|
| Gmail | 監測郵件內容、自動擬草稿、識別收據/合約 |
| Sheets | 提取非結構資料填入欄位、數據達閾值觸發警報 |
| Docs | 文件更新 → 自動發摘要郵件給成員 |
| Calendar | 機票/飯店確認信自動更新行程 |
| 第三方 | MCP 協議，可接 Asana、Dropbox、Uber 等 30+ 服務 |

---

## 上市時間與費用

- **現在**：受信任測試者計畫
- **Beta**：2026/5/25 當週，美國 AI Ultra 用戶開放
- **費用**：$100/月（AI Ultra），包含背景雲端運算資源
- **企業版**：Gemini Enterprise 近期預覽

---

## 對派哥的啟示

你現在的 Gmail 整理靠 Python script + launchd 排程。Spark 如果夠穩，可以直接取代這段：

| 現在做法 | Spark 對應 |
|----------|-----------|
| Gmail 整理 script（掃描/歸檔/垃圾桶）| Spark 守護任務，口語設定 |
| launchd 排程 | Spark 跑在 Google Cloud，不需本機常駐 |
| cc_processor 結果通知 | Spark 讀 Sheets 數據 → 觸發 Gmail 草稿 |

**建議**：5/25 Beta 開放後，先試一個小場景（如機票確認自動更新日曆），跑穩再考慮替換 Gmail 整理 script。

---

## 連結筆記

- [[gemini-35-flash-pro-agentic]] — Gemini 3.5 Flash + Spark 整體生態
- [[gmail-automation]] — 現有 Gmail 整理自動化
- [[anthropic-mcp-production-patterns]] — MCP 協議生產環境
- [[n8n-vs-ai-agent-when-to-use]] — 自動化工具選擇框架
