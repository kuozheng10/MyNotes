---
tags: [testing, e2e, playwright, page-object-model, claude-code, refactor, automation]
source: DavidKo Learning Journey，FB分享，https://www.facebook.com/share/p/1Bf6jEDxVd/?mibextid=wwXIfr
date: 2026-08-21
related: playwright-popups-iframe-newtab-datepicker-2026-08, playwright-trace-viewer-2026-08, ai-coding-e2e-test-speed-myth-2026-07, ui-test-layers-2026-06, playwright-fixtures-test-data-2026-08
---

# Playwright 測試維護的真正痛點：用 AI 做 Page Object Model 重構

> **系列**：「AI 時代下最值得投資的 UI 自動化：30 天用 Claude Code 學會寫 Playwright」Day 21（作者 kojenchieh，同系列另見 [[playwright-popups-iframe-newtab-datepicker-2026-08]] Day17、[[playwright-trace-viewer-2026-08]] Day10、[[playwright-fixtures-test-data-2026-08]] Day22）

---

## 核心論點

自動化測試真正的挑戰不在「寫」，在「維護」。用 Playwright 寫 10~20 個測試看似很有效率，但 UI 一改版（例如按鈕定位變動），CI 就整批崩潰。

## 具體問題

同一段「登入、搜尋、送出」操作，被複製貼上在十幾個測試檔裡——例如同一個定位 `#login-btn` 出現了 14 份。UI 改版時要改 14 個地方，漏改任何一處，測試就失敗。

## 解法：Page Object Model（POM）

把定位（locator）集中管理到單一檔案（例如 `LoginPage.ts`），不要散落在每個測試檔案裡。UI 改版只需要改一個地方。

## AI 輔助的新角度

過去重構既有測試是苦工，現在的做法是：
- 讓 Claude Code 做重構（把散落的 locator 收斂進 Page Object）
- 驗證重構後的準確性
- 幾分鐘內就能審查完重構品質

跟 [[ai-coding-e2e-test-speed-myth-2026-07]] 提到的「AI 改進的是腳本生成與維護層面」呼應——POM 重構正是「維護層面」的具體案例。

## 對派哥的意義

- 派哥用 Claude Code 寫 Playwright 測 Vercel 部署（[[feedback_test_against_prod|測試打Prod URL]]）時，如果測試檔案開始變多、同樣的登入/操作邏輯到處複製貼上，這就是該導入 POM 的訊號——先讓 Claude Code 抽出 Page Object，而不是手動一個一個改
- 跟 [[ui-test-layers-2026-06]] 的分層原則是不同軸線的問題：分層解決「測試該驗證什麼」，POM 解決「測試怎麼維護不重複」，兩者可以同時套用

---

## 相關筆記

- [[playwright-popups-iframe-newtab-datepicker-2026-08]] — 同系列Day17：處理彈窗/iframe/新分頁/日期選擇器
- [[playwright-trace-viewer-2026-08]] — 同系列Day10：測試失敗時用Trace Viewer查根因
- [[ai-coding-e2e-test-speed-myth-2026-07]] — AI對測試的實際貢獻在腳本生成與維護，不是加速瀏覽器
- [[ui-test-layers-2026-06]] — 測試分層責任邊界（Unit/Integration/E2E該驗證什麼）
- [[playwright-fixtures-test-data-2026-08]] — 同系列Day22：用Fixture解決測試資料互踩的問題
