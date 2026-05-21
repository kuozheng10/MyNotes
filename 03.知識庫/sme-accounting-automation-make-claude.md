---
title: "中小企業財務自動化 — Claude + Make + Google 全流程"
tags: [make, automation, claude, gemini, finance, workflow, sme, google-forms]
date: 2026-05-10
category: 03.科技工具
source: Telegram 派哥分享（大貓老師林敬謙）
---

## 成果

- 原本：1個月的財務工作 → 壓縮到1天
- 升級後：1天 → 壓縮到3小時
- 升級耗時：40分鐘（AI 進步夠快）
- 適用：營業額五千萬以下的中小企業（裝修業）

## 關鍵思維轉換

**不要收廠商各種管道的請款單 → 讓廠商直接幫你建檔**

Google 表單統一請款，廠商填寫時順便上傳請款單和發票。
外包輸入工作給外部，消除內部人工。

## 六步驟流程

| 步驟 | 做什麼 | 工具 |
|------|--------|------|
| 1 | 廠商填 Google 表單請款 + 上傳發票 | Google Forms |
| 2 | 電子發票改用 Gmail 收，Gemini 自動撈 | Gmail + Gemini |
| 3 | 人工：建立各專案名稱與簽約金額 | 手動 |
| 4 | 人工：紙本發票拍照上傳 | Google Drive |
| 5 | 自動串接產出報表 | Make |
| 6 | 報帳資料自動寄給會計事務所 | Make + Gmail |

**步驟 5 產出**：發票辨識、支出圓餅圖、收入結構圖、案件損益表

## 建立流程的方法

1. 把現有流程描述給 Claude
2. Claude 先畫出流程圖（釐清全局）
3. 逐步串接 Make automation
4. 依照目標報表格式調整輸出

## 對派哥的參考價值

**cc_processor 和這套思路完全吻合**：
- 讓銀行自動寄 email（等於廠商自動建檔）
- OCR 自動辨識帳單（發票辨識）
- 自動寫入 Notion（報表產出）

**可借鑑的概念**：
- Google Forms 作為外部輸入統一入口（可用在任何需要廠商/客戶提供資料的場景）
- Gemini 撈 Gmail 發票：可整合進現有 gmail-automation
- Make 作為低代碼串接層（cc_processor 是 code-heavy，Make 適合非工程師快速搭）

## 相關筆記

- [[gmail-automation]] — Gmail 自動化分類
- [[japan-receipt-tracker]] — 收據追蹤
