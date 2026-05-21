---
title: "Twinkle AI MCP Hub — 台灣第一個政府開放資料 MCP，49,343 筆資料集即時可查"
tags: [MCP, taiwan, opendata, government, data-gov-tw, hermes, openclaw, 龍蝦, agent]
date: 2026-05-11
category: 03.科技工具
source: Telegram 派哥分享（Twinkle AI）
url: https://hub.twinkleai.tw/
github: https://github.com/ai-twinkle/Hub
---

## 一句話

串上 data.gov.tw 全量 49,343 個資料集 + PCC 採購網，給 Claude / OpenClaw / Hermes Agent / Ollama 用，一支 Bearer token 搞定。

## 為什麼重要

以前要用台灣政府資料 → 自己爬 5 萬個檔案、處理各種 ParseError、維護 daily refresh、弄 SQL normalize、串 MCP gateway。
現在 → Bearer token，問完即用。

## 兩大核心模組

### twtools — 台灣工具箱（30+ 工具）

| 類別 | 工具 |
|------|------|
| 地址/郵政 | 中英地址互轉（中華郵政格式）、郵遞區號/行政區查詢 |
| 身份驗證 | 身分證字號驗證、統一編號驗證 |
| 金融 | 銀行代碼查詢（37 家銀行）|
| 交通 | 捷運路線（北捷/高捷/桃捷/中捷）|
| 時間 | 國曆⇄農曆、民國年⇄西元年、台灣國定假日/補班日 |
| 企業 | 公司登記資料（經濟部 API）|
| 其他 | 車牌/電話驗證、繁簡轉換、PDF 擷取、網頁抓取 |

### opendata — 政府開放資料（19 大領域）

不動產、經濟產業、交通運輸、醫療衛生、環境氣象、教育科研、農林漁牧、勞動就業、治安消防、司法法務⋯⋯

| 規格 | 數值 |
|------|------|
| 資料集數 | 49,343 個（96.6% 覆蓋率）|
| 採購資料 | PCC 13.5 萬筆，每日同步 |
| 查詢速度 | 半秒 SQL，支援跨資料源 join |
| 語系 | 中/英/日/韓/法 |

## 使用方式

1. 打開 hub.twinkleai.tw
2. 複製首頁的 prompt 片段
3. 貼進 Claude Desktop / Cursor / 任何 MCP client

```
Bearer token → 任何 MCP client 都能用
```

## 相容工具

- Claude Desktop / Cursor
- OpenClaw（龍蝦）/ Hermes Agent
- Continue / Cline
- Ollama / vLLM（本機模型也能用）

## 實用查詢範例

- 「台北今天天氣如何」→ 自動查氣象署開放資料
- 「瑞芳到九份怎麼去」→ 查交通資訊
- 「這個統一編號是哪家公司」→ 呼叫經濟部 API
- 「今年金額最大的政府採購 10 件、廠商分布」
- 「113 學年度大學招生錄取率最高的 10 個科系」
- 「比較高雄各區人口」

## 對派哥的評估

**值得試用**。

目前派哥的自動化不需要台灣政府資料，但：
- Hermes Agent loop 接上這個 = 可以直接查政府資料回答問題，不用自己寫爬蟲
- 32 個台灣專用工具（民國年、統編、地址）在本地自動化很實用
- Bug 回報：github.com/ai-twinkle/Hub

## 相關筆記

- [[anthropic-mcp-production-patterns]] — MCP 生產部署模式
- [[public-api-curation-taiwan]] — 台灣常用 Public API 清單
- [[openclaw-hermes-collaboration]] — OpenClaw + Hermes 協作架構
