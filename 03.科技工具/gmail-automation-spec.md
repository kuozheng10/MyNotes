---
title: "Gmail Automation v2.0 規格書"
tags: [gmail, apps-script, automation, spec]
date: 2026-04-03
category: 03.科技工具
---

# Gmail Automation v2.0 規格書

> 程式碼：`~/Documents/MyClaude/gmail-automation.gs`
> 版本記錄：`~/Documents/GitHub/MyNotes/03.科技工具/gmail-automation.md`

---

## Label 設計（5 個）

| Label | 用途 | 處理策略 |
|-------|------|----------|
| `重要文件` | 帳單/收據/確認書/保單/股息 | archive，永不 trash |
| `銀行金融` | 銀行/信用卡「通知」（非帳單） | 已讀 7 天→archive，未讀 14 天→archive |
| `購物旅遊` | 購物出貨/旅遊通知 | 已讀 7 天→archive，未讀 14 天→archive |
| `電子報` | newsletter/週報/學習電子報 | 已讀 3 天→trash，未讀 7 天→trash |
| （無） | 登入/促銷/科技通知 | 直接 trash（依天數） |

**原則：⭐ 有星號 = 永遠不動**

---

## 重要文件觸發關鍵字（主旨符合即保護）

```
帳單、對帳單、發票、收據、確認書、確認單、繳費確認
訂單確認、交易確認、付款確認、匯款、出金、入金
配息、股息、理賠、保費、保單
booking confirmation、order confirmation、payment confirmation
invoice、receipt、statement、itinerary、e-ticket
```

---

## 各類別處理規則

### 銀行金融（通知類，非帳單）
- Senders: hsbc, ctbcbank, cathaybk, taishinbank, esunbank, standardchartered, linebank, nextbank, fubon, amex, bitopro
- Subjects: 消費通知、刷卡通知、刷卡成功、消費提醒、帳戶通知、transaction alert
- 已讀 7 天 → archive；未讀 14 天 → archive

### 購物旅遊
- Senders: uber eats, rakuten, coupang, costco, 蝦皮, shopback, 星巴克, kobo
- Subjects: 出貨通知、配送、shipped、已出貨
- 已讀 7 天 → archive；未讀 14 天 → archive

### 電子報
- Senders: it邦幫忙, ithome, 商業周刊, coursera, udemy, accupass
- Subjects: 電子報、newsletter、每日摘要、daily digest、週報
- 已讀 3 天 → trash；未讀 7 天 → trash

### 登入通知（直接清）
- Subjects: 已登入、登入通知、sign-in alert、login alert、網路銀行登入、網銀登入、帳號登入、account login
- 已讀 1 天 → trash；未讀 3 天 → trash

### 促銷廣告（直接清）
- Subjects: 優惠活動、限時特賣、會員專屬、折扣、promo、special offer、limited time
- 已讀 3 天 → trash；未讀 7 天 → trash

### 科技通知（GitHub/Vercel 等）
- Senders: github, vercel, noreply@github
- Subjects: pushed to、workflow run、deployed、build、pull request、merged
- 已讀 1 天 → trash；未讀 3 天 → trash

### 兜底（無規則符合）
- 已讀或未讀 ≥ 30 天 → archive

---

## 四支函數

### ① processEmails()（每天 8am / 8pm）
搜尋：`in:inbox newer_than:30d`

判斷順序：
1. 有星號 → 跳過
2. 主旨符合重要文件關鍵字 → 貼「重要文件」label → 老信 archive
3. 符合規則 → 依規則 archive 或 trash
4. 無規則符合 → 30 天後 archive

### ② cleanupInbox()（手動跑一次）
搜尋：`in:inbox older_than:90d newer_than:365d`

判斷順序：
1. 有星號 → 跳過
2. 符合重要文件 → label + archive
3. 符合 trash 規則 → removeLabels + trash
4. 已有 label → archive
5. 其他 → archive（保守）

### ③ migrateLabels()（手動跑一次）

| 舊 label | 新 label |
|----------|----------|
| 銀行-信用卡 | 銀行金融 |
| 購物-外送 | 購物旅遊 |
| 旅遊-訂房 | 購物旅遊 |
| 電子報-學習 | 電子報 |
| 投資-證券 | 重要文件 |
| 保險 | 重要文件 |
| 科技-訂閱 | （刪除） |
| 待刪除 | （刪除） |

### ④ trashOldNotifications()（每週日 2am）
清理 15 天前～1 年內的通知/促銷信 → removeLabels + trash

### ⑤ emptyTrash()（每月 1 日 3am）
永久刪除垃圾桶 30 天以上的郵件

---

## 部署順序（第一次）

```
1. 貼上新版 gmail-automation.gs
2. 執行 setupTriggers()     ← 設定排程
3. 執行 migrateLabels()     ← 舊 label 遷移（跑一次）
4. 執行 cleanupInbox()      ← inbox 大掃除（跑一次）
5. 完成，之後 processEmails() 自動跑
```

---

## 觸發排程

| 函數 | 頻率 |
|------|------|
| processEmails | 每天 8am / 8pm |
| trashOldNotifications | 每週日 2am |
| emptyTrash | 每月 1 日 3am |
