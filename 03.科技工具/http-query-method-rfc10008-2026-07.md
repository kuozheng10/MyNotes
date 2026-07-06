---
tags: [http, api-design, rfc, web-standards]
source: IETF RFC 10008（2026-06 正式發布）
date: 2026-07-06
---

# HTTP 多了新方法：QUERY（RFC 10008）

> IETF（Internet Engineering Task Force，網際網路工程任務組——制定 HTTP/TCP/IP/DNS 等底層協議的組織）2026-06 正式發布 RFC 10008《The HTTP QUERY Method》

---

## 解決什麼問題：複雜查詢的兩難

過去要向伺服器搜尋/篩選資料（複雜電商篩選、GraphQL 查詢、大範圍 SQL/JSON 條件），只有兩種爛選擇：

| 方法 | 問題 |
|------|------|
| **GET** | 複雜參數塞進 URL Query String，會撞 URL 長度限制（多數瀏覽器/proxy 超過2~8KB報錯）；PII 留在網址上，被瀏覽器歷史和伺服器 log 記錄，隱私風險 |
| **POST** | 語意上是「新增資料」，不安全且非等冪(non-idempotent)。斷線時瀏覽器不敢自動重試（怕重複下單）；下游快取伺服器預設不快取POST回應，當GET用享受不到快取優化 |

## QUERY 方法：帶 Body 的 GET

**QUERY = 可以帶 Request Body 的 GET**，融合兩者優點：
- 像 GET：安全、等冪（idempotent）、純讀取——斷線可以放心自動重試，proxy/瀏覽器可以快取結果
- 像 POST：可以把複雜龐大的 JSON/SQL/GraphQL 查詢條件放 Body，不用塞爆 URL，避免隱私資訊洩露在網址上

## 配套細節

- **新 Header `Accept-Query`**：伺服器用這個告訴 client 支援哪些查詢格式，例如 `Accept-Query: application/json, application/sql`
- **415 Unsupported Media Type**：client 傳的查詢格式伺服器看不懂
- **422 Unprocessable Content**：格式看得懂但語法有誤（例如查詢不存在的欄位）
- **不屬於 CORS-safelisted 方法**：跨網域發送 QUERY 前，瀏覽器必須先送 `OPTIONS` 做 preflight 預檢

## 意義

補齊 HTTP 協議幾十年來在大規模 read-only 查詢上的語意空缺。目前各後端框架與網路基礎設施正陸續加入原生支援。

**跟現有專案的關聯**：investment-dashboard/my-wallet-trip 這類專案若未來有複雜篩選查詢需求（例如多條件交易篩選），QUERY method 成熟後會是比「GET塞爆URL」或「POST濫用」更乾淨的選擇，值得留意框架（Next.js/Vercel）何時原生支援。
