---
tags: [testing, e2e, playwright, ai-coding, automation, performance]
source: DavidKo Learning Journey，FB分享，https://www.facebook.com/share/p/1AoRLzF51B/?mibextid=wwXIfr
date: 2026-07-30
related: ui-test-layers-2026-06, ai-testing-agile-quality, loop-engineering-testing, playwright-page-object-model-2026-08, playwright-fixtures-test-data-2026-08
---

# AI Coding 時代的 UI 自動化測試速度：真正變快的是架構，不是 AI

> **核心結論**：「AI 讓 UI 自動化比較容易寫，不代表瀏覽器本身跑得比較快。」

---

## 現代測試執行時間參考

| 測試類型 | 時間 |
|---------|------|
| 簡單頁面操作 | 5～10 秒 |
| 登入 + 核心流程 | 10～30 秒 |
| 跨多頁面業務流程 | 20～60 秒 |
| 含付款/非同步處理 | 1～數分鐘 |

---

## 過去測試慢的四大原因

1. 每步操作後固定 `sleep 3` 秒
2. 每個案例都重啟瀏覽器、重新登入、重建測試資料
3. 測試依序執行（100 個案例要跑 50 分鐘）
4. 單一測試包山包海，塞太多功能驗證

## 現在變快的真正原因（跟 AI 無關）

- **自動等待機制**取代固定 sleep 延遲
- 透過 **API** 直接建立測試資料，不走 UI 操作
- **重用登入狀態**，不用每次重新登入
- **平行執行**：10 個 worker 可把 50 分鐘壓到 5 分鐘
- **只執行相關測試**（test impact analysis，跟 [[ai-testing-agile-quality]] 提到的概念同一件事）

## AI 的實際貢獻在哪

AI 改進的是**腳本生成與維護層面**：
- 產生測試程式碼
- 補充/修正 locator
- 分析失敗原因

AI **不能**加速瀏覽器載入或後端處理時間——即時 AI agent 操作反而更慢（agent 要先「看」再「想」再「做」，比寫死的腳本慢）。

## 對派哥的意義

- 派哥自己用 Playwright 測 Vercel 部署（[[feedback_test_against_prod|測試打Prod URL]] 那條紀律）時，如果測試跑得慢，該檢查的是「有沒有固定sleep」「有沒有平行跑」「有沒有重複登入」，不是想著換更強的AI模型來加速
- 呼應 [[ui-test-layers-2026-06]] 的分層原則：這篇補上「就算全部塞在 E2E 層，只要把上面五個架構問題解決，速度還是能大幅改善」，兩篇合起來看＝「先分層減少E2E案例數量，再用這篇的架構技巧加速剩下的E2E」

---

## 相關筆記

- [[ui-test-layers-2026-06]] — 測試分層責任邊界（Unit/Integration/E2E該驗證什麼）
- [[ai-testing-agile-quality]] — Test Impact Analysis 加速CI的理由
- [[loop-engineering-testing]] — Loop的stop condition該對應正確測試層次
- [[playwright-trace-viewer-2026-08]] — 同系列Day10：測試失敗時用Trace Viewer查根因
- [[playwright-page-object-model-2026-08]] — 同系列Day21：用Claude Code做Page Object Model重構
- [[playwright-fixtures-test-data-2026-08]] — 同系列Day22：用Fixture解決測試資料互踩的問題
- [[playwright-page-object-model-2026-08]] — 同系列Day21：用Claude Code做Page Object Model重構
