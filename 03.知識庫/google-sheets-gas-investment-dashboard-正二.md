---
title: 正二社團 Google Sheets GAS 戰情室——風險評估與使用方式
tags: [投資, 正二, Google Sheets, GAS, 戰情室, 台股]
date: 2026-05-24
category: 理財投資
source: https://docs.google.com/spreadsheets/d/1dtybfQsSazaQEvkosxn330GkezctRVeVotK36XHwxzE/copy
---

## 這是什麼

正二社團成員用 AI 寫的 Google Apps Script 投資戰情室。
複製副本後，在自己的 Google Sheet 上跑，顯示台美股持倉、損益日曆、再平衡建議等。

---

## GAS 做了什麼

| 函式 | 功能 |
|------|------|
| `doGet()` | 讀試算表資料，生成網頁介面 |
| `doPost()` | 接收每月投入表單，寫回試算表 |
| `snapshotAssets()` | 每日 9:00 AM 自動記錄資產快照 |
| `setupDailyTrigger()` | 建立每日自動觸發器 |

---

## 風險評估

### ✅ 低風險項目
- **資料全在你自己的 Google 帳號內**：副本後你是擁有者，GAS 只能存取你的試算表
- **無外部 API 呼叫**：使用說明未提及向外傳送資料
- **免費**：用 Google Apps Script 免費額度

### ⚠️ 需注意
1. **Web App 部署設定**：原版設為「所有人可存取」，建議複製後改為「只有我」或「登入才能看」
2. **授權前先看 code**：在 Google Sheet → 擴充功能 → Apps Script，先閱讀所有函式再按授權
3. **每日觸發器**：會佔用你 Google 帳號的 Apps Script 執行配額（免費版每天 6 分鐘，夠用）
4. **股數/成本要自己填**：原版是測試資料，需手動改成你的持股

### ❌ 不建議
- 直接用原版 Sheet（對方有 owner 權限看你的資料）→ **一定要複製副本後使用**

---

## 如何使用

1. 點副本連結複製到自己的 Google Drive
2. 進 Apps Script 看 code，確認無異常
3. 部署 Web App，將存取設定改為「只有我」
4. 填入自己的持股資料
5. 執行 `setupDailyTrigger()` 設定每日快照

---

## 對派哥的評估

你已有自己的 Next.js 投資 dashboard + Notion + SQLite，功能更完整。
這個 Google Sheets 版本對你沒有直接用途。
參考價值：GAS 實作方式，以及「一人公司如何用 AI 快速做工具」的案例。
