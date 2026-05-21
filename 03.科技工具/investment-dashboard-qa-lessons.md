---
title: Investment Dashboard QA 教訓（2026-05-22）
tags:
  - testing
  - qa
  - lessons-learned
  - investment-dashboard
date: 2026-05-22
---

# Investment Dashboard QA 教訓

> 上線後才發現 7 個問題，全部是測試沒覆蓋到的盲點。記錄根本原因和改進方法。

## 犯的錯 & 根本原因

### 1. 重複交易（QYLD 4/23 出現 3 筆）

**現象：** 同一筆配息被存成 DIV / reinvest / dividend 三筆。

**根本原因：** SQLite UNIQUE constraint 包含 `type` 欄位，Gemini parser 把同一筆解析成不同 type，全都通過了。

**修法：** 重建 UNIQUE(account_id, txn_date, symbol, amount, cusip)，不含 type。

**測試沒測出原因：** 只驗 transactions array 存在，沒驗「同日期同標的不能有多筆」的商業規則。

---

### 2. 配息 tab 顯示 0 筆

**現象：** FirstTrade 配息 tab 空白，但交易 tab 有 DIV 記錄。

**根本原因：** FirstTrade 配息存在 transactions（type=DIV），不在 dividends table。先定規格再動手就能發現。

**修法：** dividends tab 合併顯示 DIV/INT transactions + dividends table。

**測試沒測出原因：** 只驗 `/api/account/firsttrade` 回 200 和 dividends array 存在，沒驗「配息 tab 實際顯示幾筆」。

---

### 3. DIV 重複出現兩個 tab

**現象：** 交易 tab 和配息 tab 都顯示 QYLD DIV，重複。

**根本原因：** 沒先定規格就動手。應該先定：交易 tab = buy/sell，配息 tab = DIV/INT/interest，兩者互斥。

**修法：** trades 用 TRADE_EXCLUDE 過濾（含 reinvest），dividends 只合併 DIV/INT。

**測試沒測出原因：** 沒有「同一筆不能同時出現在兩個 tab」的測試情境。

---

### 4. 利息金額顯示負數

**現象：** 利息顯示 -$1.63（應為正）。

**根本原因：** INCOME_TYPES = ['DIV', 'SELL', 'INT', 'CRE']，但 type 實際是 'interest'（小寫），不在清單裡。

**修法：** 改成用 `t.amount >= 0` 判斷正負，不依靠 type 字串。

**測試沒測出原因：** 沒驗金額顯示的正負號，只驗金額數值。

---

### 5. Notion 舊記錄不會自動清理

**現象：** SQLite 刪掉的記錄，Notion 裡的舊頁面還在。

**根本原因：** `_upsert_page` 只新增/更新，沒有清理 SQLite 已刪除但 Notion 還在的記錄。

**修法：** 手動 archive Notion 裡的多餘頁面；positions 有 `_archive_stale_pages_for_account`，transactions 沒有。

**改進方向：** sync_transactions 也應該支援清理孤立記錄（比對 id）。

---

### 6. fund_name 沒有 sync 到 Notion

**現象：** 安聯基金配息 tab 顯示「—」，fund_name 是 null。

**根本原因：** `sync_dividends` 沒有 SELECT fund_name，也沒有 sync 到 Notion 的 symbol 欄位。

**修法：** 加入 fund_name SELECT，`symbol` 欄位 = fund_name ?? sym。

**測試沒測出原因：** 只驗 dividends array 長度，沒驗 label 不是 null 或「—」。

---

### 7. 帳戶名稱在 Notion 手動改會被覆蓋

**現象：** 手動把 Notion 的 account_name 改成「安聯基金」，再跑 sync 又蓋回「安聯收益成長基金」。

**根本原因：** account_name 的來源是 SQLite accounts.name，sync 永遠以 SQLite 為準。

**修法：** 修改 SQLite 的 accounts.name，sync 才會正確。

---

## 測試沒測出的通用原因

| 盲點 | 描述 |
|------|------|
| 只驗 HTTP 200 | 沒有驗資料值（金額 > 0、名稱不是 null） |
| 只驗結構存在 | 沒有驗「筆數正確」、「不重複」 |
| 沒有 tab 互斥驗證 | 同一筆資料不能同時在兩個 tab |
| 沒有商業規則驗證 | 同帳戶同日期同標的不應有多筆 |
| 沒有 UI 顯示驗證 | label 是不是「—」、金額正負號對不對 |

---

## 改進 SOP

### Test Charter 必加項目（Data Integrity Check）

```
Target: /api/account/{id} + UI tab 顯示
Task:
  - 每個 tab 的筆數 > 0（有資料的帳戶）
  - 金額欄位 > 0
  - 名稱欄位不是 null / "—"
  - 同一筆資料不在兩個 tab 重複出現
  - 正收入顯示綠色 +，費用顯示 -
Timebox: 20 分鐘
```

### 功能改版前先寫 EDD 情境

多個 tab 的功能，先列：
- ✅ 哪些資料只在 A tab
- ✅ 哪些資料只在 B tab
- ⚠️ 哪些資料不能同時在兩個 tab
- ❌ 什麼情況顯示空

### Notion sync 原則

- Notion 資料以 SQLite 為準，不要在 Notion 手動改會被 sync 覆蓋的欄位
- 帳戶名稱改了要改 SQLite → 再 sync
- 刪除資料要同時刪 SQLite + archive Notion

---

## 相關 memory

- [[feedback-sbe-ui-tabs]] — 多 tab 先定 EDD 情境
- [[feedback-sbe-workflow]] — 新功能 SOP：Claude 規格 → Codex 實作 → Claude review
- [[feedback-testing-sop]] — 測試 SOP：Charter → Codex 測試 → bug → 回歸測試
