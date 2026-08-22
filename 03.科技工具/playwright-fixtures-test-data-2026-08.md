---
tags: [testing, e2e, playwright, fixtures, test-data, claude-code, automation]
source: DavidKo Learning Journey，FB分享 https://www.facebook.com/share/p/1D5X1igqMe/?mibextid=wwXIfr ／ [原文iThome鐵人賽Day22](https://ithelp.ithome.com.tw/articles/10404161)
date: 2026-08-22
related: playwright-page-object-model-2026-08, playwright-popups-iframe-newtab-datepicker-2026-08, playwright-trace-viewer-2026-08, ai-coding-e2e-test-speed-myth-2026-07, ui-test-layers-2026-06
---

# Playwright Fixture 與測試資料管理：flaky test 的病根常常是資料，不是 selector

> **系列**：「AI 時代下最值得投資的 UI 自動化：30 天用 Claude Code 學會寫 Playwright」Day 22（作者 kojenchieh，同系列另見 [[playwright-page-object-model-2026-08]] Day21、[[playwright-popups-iframe-newtab-datepicker-2026-08]] Day17、[[playwright-trace-viewer-2026-08]] Day10）

---

## 核心論點

自動化測試最崩潰的，很多時候不是 selector 壞掉、不是 Playwright 不穩，而是**測試資料彼此互踩**：單獨跑是綠的，一開平行就紅；昨天正常，今天莫名多一筆資料；A 測試要先跑，B 才會過。這些看起來像 flaky test 的問題，病根常常是「這筆測試資料到底是誰的」沒處理好。

## Fixture 的生命週期（三個性質）

- **清理一定執行**：測試失敗也照清，不會留垃圾害到別人
- **沒宣告就不會建**：只有用到的測試才付出建立成本，`beforeEach` 做不到這件事（它對整檔一視同仁）
- **fixture 之間可以互相依賴**：A 需要 B，Playwright 自動排建立順序，再反向清理

## 接手既有專案常見的三種 fixture

1. **登入狀態**：獨立 setup 專案先登入一次，把 cookie/localStorage 存成檔案（看 config 裡的 `projects` 與 `storageState`）
2. **Page Object 注入**：測試直接拿到組好的 page object（跟 [[playwright-page-object-model-2026-08]] Day21 的 POM 是同一件事的另一面）
3. **auto fixture**：`{ auto: true }` 的 fixture 每個測試都自動套用，是隱形的——「測試明明過了卻報一個沒印象的錯誤」，先搜 `auto: true`

## Fixture 真正要解決的問題：測試資料隔離

資料隔離要做到三件事：測試前建立自己專屬的資料、測試後刪掉、失敗時刪除也要發生。手寫十次測試就要重複十次，漏一個環境就髒回去——這正好就是 fixture 的三個性質。

**四種測試資料策略**（隔離度與成本同步上升，業界實際落點多在中間）：
| 策略 | 說明 |
|------|------|
| 全部共用固定資料 | 成本最低，互踩風險最高 |
| 部分共用（如商品目錄共用、登入用帳號池） | 業界主流混用方式 |
| 訂單/購物車自建自清 | 用 API 建立專屬資料，測完刪掉 |
| 完全自建自清 | 每個測試完全獨立，可單獨跑/平行跑/任意順序跑 |

## 三個診斷指令（測試無故變紅時用，比 fixture 語法更常用）

```bash
npx playwright test tests/orders.spec.ts --workers=1      # 單執行緒
npx playwright test tests/orders.spec.ts --repeat-each=3  # 連跑三次
npx playwright test tests/orders.spec.ts -g "下單後"       # 只跑那一個
```

判斷準則：
- `--workers=1` 就不紅 → **平行互踩**
- 單獨跑會過、整檔跑會紅 → **順序依賴**
- 連跑第二次開始紅 → **髒資料累積**
- 三種都紅 → 不是資料問題

## 沒有建資料 API 時的五個做法（由好到差）

1. 跟開發要一支測試環境專用的建資料端點
2. 直接打資料庫用 SQL 建資料（快但繞過商業邏輯，schema 一改就壞，只能當過渡方案）
3. 用 UI 建一批共用資料（整個套件開始前建、結束後刪）
4. 改不動建立，至少改得動清理
5. 測試開頭驗證前提（「購物車應為空，不是就先清空」）

額外兩層保險：測試資料一律加 `e2e-` 前綴方便排程掃除；測試環境每晚從乾淨快照重置。

## 對派哥的意義

- 呼應 [[playwright-page-object-model-2026-08]]：POM 解決「測試怎麼維護不重複」，Fixture 解決「測試資料互不干擾」，是兩個不同軸線的問題，可以同時套用
- 派哥用 Claude Code 測 Vercel 部署（[[feedback_test_against_prod|測試打Prod URL]]）如果之後測試多了、開始出現「單獨跑過、一起跑就紅」的靈異現象，先用上面三個診斷指令分診，不要急著改程式碼——這篇強調「先看表格，不要先猜」
- 跟 [[ai-coding-e2e-test-speed-myth-2026-07]] 提到的「test impact analysis」不同軸線但互補：那篇談的是「只跑相關測試」加速 CI，這篇談的是「跑的測試彼此不能互踩」，兩者都是让平行測試可靠變快的前提

---

## 相關筆記

- [[playwright-page-object-model-2026-08]] — 同系列Day21：用Claude Code做Page Object Model重構
- [[playwright-popups-iframe-newtab-datepicker-2026-08]] — 同系列Day17：彈窗/iframe/新分頁/日期選擇器處理法
- [[playwright-trace-viewer-2026-08]] — 同系列Day10：測試失敗時用Trace Viewer查根因
- [[ai-coding-e2e-test-speed-myth-2026-07]] — AI對測試的實際貢獻在腳本生成與維護，不是加速瀏覽器
- [[ui-test-layers-2026-06]] — 測試分層責任邊界（Unit/Integration/E2E該驗證什麼）
