---
title: Playwright 很好用，但別把它當成品質保證機
tags: [playwright, testing, qa, e2e, test-automation, agile]
source: 社群文章（2026-06）
date: 2026-06-07
---

# Playwright 很好用，但別把它當成品質保證機

> 長期維護過大型 UI Automation 的人，通常不會講得這麼輕鬆。

---

## 五個常見幻想

### 幻想一：有 UI Automation = 品質有保障
只能證明「這幾條被自動化的流程，目前還能跑」。  
500 個功能只覆蓋 30 條 → 只能保證那 30 條，其餘不知道。

> 「我們有 Playwright 所以品質沒問題」 = 「客廳沒失火所以整棟房子安全」

### 幻想二：UI Automation 可以取代其他測試
倒金字塔反模式：把什麼都塞進 UI，結果跑得慢、難維護、出事難定位。

**正確比例（Mike Cohn）：**
- 70% 單元測試（邏輯）
- 20% 整合測試（規則）
- 10% E2E（關鍵使用者旅程）

UI Automation 應該是最薄的一層。

### 幻想三：錄一次就能一直跑
CI/CD 現實：timeout、selector 失效、element 未載入、第三方異常、資料污染。

**Google 研究數據：**
- 約 16% 的測試出現過 flaky
- pass 轉 fail 裡有 **84% 是 flaky，不是真 bug**
- 結果：「紅燈先 rerun」文化，可信度崩潰

### 幻想四：案例越多越好
登入×角色×操作 → 膨脹到幾百個案例 → 每個 Sprint 都在修腳本。

問題：**80% 都在測 Happy Path**，但真實問題來自：
- 權限、狀態競爭、邊界條件
- 錯誤處理、整合失敗

力氣花最多 = 風險最低的案例。

### 幻想五：跑越久越划算
幾百個 E2E 案例動輒跑 1-2 小時，維護成本常常超過攔下的 bug 數。  
紅燈多半是環境問題，不是真 bug。ROI 根本算不過去。

---

## 真正該問的三個問題

1. **你拿它守住了哪些核心流程？**（註冊、登入、付款 → 幾條夠了）
2. **你測的只有 Happy Path，還是也涵蓋了權限、邊界、異常？**
3. **它失敗時能不能分辨：產品壞 vs 環境壞 vs 測試壞？**

---

## 正確分工

| 層次 | 工具 | 職責 |
|-----|------|------|
| 單元測試 | Jest / Vitest | 邏輯正確性 |
| API 測試 | Supertest / Postman | 規則與合約 |
| UI Automation | Playwright | 最關鍵的使用者旅程（5-15 條）|
| 未知風險 | 探索性測試 | 人工發現邊界 |

---

## 對派哥的應用

Playwright 很適合拿來驗證：
- My Wallet Trip 的拍照記帳主流程
- investment-dashboard 的登入 + 資料載入
- insurance-tracker 的新增保單流程

**不值得做的事：** 每個 UI 元件都寫 E2E、對 localhost 測試（dev/prod bundle 不同）。

---

## 連結筆記
- [[feedback_playwright_mcp]] — Playwright MCP 使用時機（深度測試 vs 快速確認）
- [[feedback_test_against_prod]] — 必須打 Vercel URL，不能只測 localhost
