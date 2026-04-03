---
title: "Gmail Automation - Google Apps Script"
tags: [gmail, apps-script, automation, telegram]
date: 2026-04-03
category: 03.科技工具
source: 自建
---

## 摘要

> Google Apps Script 自動分類 Gmail。5 個 label、4 支函數，每天早晚自動跑。
> 規格書：[gmail-automation-spec.md](gmail-automation-spec.md)

## 設定

| 項目 | 值 |
|------|-----|
| 觸發時間 | 每日 08:00 / 20:00 |
| 掃描範圍 | in:inbox newer_than:30d（最多 200 則）|
| 週清理 | 每週日 2am → 通知/促銷 15天~1年前 → trash |
| 月清理 | 每月 1 日 3am → 垃圾桶永久刪除 30 天以上 |
| Telegram Bot | BOT_TOKEN / CHAT_ID 存在 PropertiesService |

## Labels（5 個）

| Label | 用途 | 處理 |
|-------|------|------|
| 重要文件 | 帳單/收據/確認書/保單/股息 | archive，永不 trash |
| 銀行金融 | 銀行/信用卡通知 | 已讀 7 天→archive |
| 購物旅遊 | 購物/旅遊通知 | 已讀 7 天→archive |
| 電子報 | newsletter/週報 | 已讀 3 天→trash |
| （無） | 登入/促銷/科技通知 | 快速 trash |

## 部署步驟（第一次）

1. 前往 [script.google.com](https://script.google.com)
2. 貼上完整程式碼
3. 執行 `setupTriggers()` → 授權
4. 執行 `migrateLabels()` → 舊 label 遷移
5. 執行 `cleanupInbox()` → 一次性大掃除
6. 完成，之後 processEmails() 每天自動跑

## 版本記錄

| 版本 | 日期 | 變更 |
|------|------|------|
| v1.0 | 2026-03-27 | 初版：規則分類 + OTP 推送 |
| v1.1 | 2026-03-27 | 修 Telegram 推送格式 |
| v1.2 | 2026-03-29 | 移除 OTP 功能；修 label double-count |
| v1.3 | 2026-03-30 | 購物-外送/電子報-學習 超過 14 天移至垃圾筒；新增 emptyTrash() |
| v1.4 | 2026-03-30 | inbox 不移垃圾筒；只有已歸檔的舊信才移 |
| v1.5 | 2026-03-30 | label 名稱加引號，修 `-` 被 Gmail 當成排除符號的 bug |
| v1.6 | 2026-03-31 | BOT_TOKEN / CHAT_ID 改用 PropertiesService |
| v1.7 | 2026-04-03 | 信用卡消費通知關鍵字補強；登入通知關鍵字補強；新增 trashOldNotifications() |
| v1.8 | 2026-04-03 | 待刪除規則改為 trashImmediately，直接丟垃圾桶，不再貼 label |
| v1.9 | 2026-04-03 | 丟垃圾桶前先移除所有 label（removeLabelsAndTrash helper） |
| v2.0 | 2026-04-03 | 全面重寫：5 label 精簡設計、重要文件優先保護、cleanupInbox 大掃除、migrateLabels 遷移、未讀有寬限天數 |
| v2.1 | 2026-04-03 | 修 thread.isStarred() 不存在錯誤，改用 isThreadStarred() 檢查 messages |

## 完整程式碼 v2.1

```javascript
// ========================================
// Gmail Automation v2.0
// 規格書：~/Documents/GitHub/MyNotes/03.科技工具/gmail-automation-spec.md
// 版本記錄：~/Documents/GitHub/MyNotes/03.科技工具/gmail-automation.md
// 更新日期：2026-04-03
// ========================================

var BOT_TOKEN = PropertiesService.getScriptProperties().getProperty("BOT_TOKEN");
var CHAT_ID   = PropertiesService.getScriptProperties().getProperty("CHAT_ID");

// ── Label 定義（5 個）──────────────────────────────────────────
var LABEL_IMPORTANT  = "重要文件";   // 帳單/收據/確認書，永不 trash
var LABEL_BANKING    = "銀行金融";   // 銀行/信用卡通知
var LABEL_SHOPPING   = "購物旅遊";   // 購物/旅遊通知
var LABEL_NEWSLETTER = "電子報";     // 電子報/學習

// ── 重要文件關鍵字（主旨符合 → 優先保護，永不 trash）──────────
var IMPORTANT_SUBJECTS = [
  "帳單", "對帳單", "發票", "收據", "確認書", "確認單", "繳費確認",
  "訂單確認", "交易確認", "付款確認", "匯款", "出金", "入金",
  "配息", "股息", "理賠", "保費", "保單",
  "booking confirmation", "order confirmation", "payment confirmation",
  "invoice", "receipt", "statement", "itinerary", "e-ticket"
];

// ── 分類規則 ────────────────────────────────────────────────────
// 欄位說明：
//   label            → 要貼的 label（null = 不貼）
//   senders[]        → sender 包含其中任一
//   subjects[]       → 主旨包含其中任一
//   archiveReadDays  → 已讀 N 天後 archive
//   archiveUnreadDays→ 未讀 N 天後 archive
//   trashReadDays    → 已讀 N 天後 trash（與 archive 互斥）
//   trashUnreadDays  → 未讀 N 天後 trash
var RULES = [
  {
    // 銀行/信用卡「通知」（帳單已被 IMPORTANT_SUBJECTS 先攔）
    label: LABEL_BANKING,
    senders: ["hsbc", "ctbcbank", "cathaybk", "taishinbank", "esunbank",
              "standardchartered", "linebank", "nextbank", "fubon", "amex", "bitopro"],
    subjects: ["消費通知", "刷卡通知", "刷卡成功", "消費提醒", "帳戶通知",
               "帳戶異動", "transaction alert", "spending alert", "purchase alert"],
    archiveReadDays: 7,
    archiveUnreadDays: 14
  },
  {
    // 購物/外送通知
    label: LABEL_SHOPPING,
    senders: ["uber eats", "ubereats", "rakuten", "coupang", "costco", "蝦皮",
              "shopback", "atmos", "星巴克", "starbucks", "樂天kobo", "kobo"],
    subjects: ["出貨通知", "配送通知", "shipped", "已出貨", "到貨通知"],
    archiveReadDays: 7,
    archiveUnreadDays: 14
  },
  {
    // 電子報/學習
    label: LABEL_NEWSLETTER,
    senders: ["it邦幫忙", "ithome", "商業周刊", "coursera", "udemy", "畫張圖", "accupass"],
    subjects: ["電子報", "newsletter", "每日摘要", "daily digest", "週報"],
    trashReadDays: 3,
    trashUnreadDays: 7
  },
  {
    // 登入通知 → 快速清
    label: null,
    senders: [],
    subjects: ["已登入", "登入通知", "sign-in alert", "login alert", "security alert",
               "new sign-in", "新裝置登入", "登入提醒", "網路銀行登入", "網銀登入",
               "帳號登入", "裝置驗證", "account login", "account sign-in", "logged in to"],
    trashReadDays: 1,
    trashUnreadDays: 3
  },
  {
    // 促銷/廣告
    label: null,
    senders: [],
    subjects: ["優惠活動", "限時特賣", "會員專屬", "獨家優惠", "折扣碼",
               "promo", "special offer", "limited time", "sale", "discount"],
    trashReadDays: 3,
    trashUnreadDays: 7
  },
  {
    // GitHub/Vercel 等科技通知
    label: null,
    senders: ["github", "vercel", "noreply@github", "notifications@github"],
    subjects: ["pushed to", "workflow run", "deployed", "build failed", "build passed",
               "pull request", "merged", "opened an issue", "mentioned you", "review requested"],
    trashReadDays: 1,
    trashUnreadDays: 3
  }
];

// ════════════════════════════════════════════════════════════════
// ① processEmails — 每天 8am / 8pm
// ════════════════════════════════════════════════════════════════
function processEmails() {
  var labels  = ensureLabels();
  var now     = new Date();
  var threads = GmailApp.search("in:inbox newer_than:30d", 0, 200);
  var stats   = { labeled: 0, archived: 0, trashed: 0 };

  threads.forEach(function(thread) {
    if (isThreadStarred(thread)) return; // ⭐ 有星號：永遠不動

    var firstMsg = thread.getMessages()[0];
    var from     = firstMsg.getFrom().toLowerCase();
    var subject  = firstMsg.getSubject().toLowerCase();
    var isRead   = !thread.isUnread();
    var ageDays  = (now - firstMsg.getDate()) / 86400000;

    // Step 1：重要文件？ → label + archive
    if (isImportant(subject)) {
      addLabelIfNew(thread, LABEL_IMPORTANT, labels, stats);
      if ((isRead && ageDays >= 14) || ageDays >= 30) {
        thread.moveToArchive(); stats.archived++;
      }
      return;
    }

    // Step 2：規則比對
    for (var i = 0; i < RULES.length; i++) {
      var rule = RULES[i];
      if (!matchesRule(from, subject, rule)) continue;

      if (rule.label) addLabelIfNew(thread, rule.label, labels, stats);

      if (rule.trashReadDays !== undefined) {
        var shouldTrash = (isRead  && ageDays >= rule.trashReadDays) ||
                          (!isRead && ageDays >= rule.trashUnreadDays);
        if (shouldTrash) { removeLabelsAndTrash(thread); stats.trashed++; }
      } else {
        var shouldArchive = (isRead  && ageDays >= rule.archiveReadDays) ||
                            (!isRead && ageDays >= rule.archiveUnreadDays);
        if (shouldArchive) { thread.moveToArchive(); stats.archived++; }
      }
      return;
    }

    // Step 3：兜底 — 無規則，30 天後 archive
    if (ageDays >= 30) { thread.moveToArchive(); stats.archived++; }
  });

  var hour = now.getHours();
  var msg = "Gmail 整理完成（" + (hour < 12 ? "早上" : "晚上") + "）\n\n"
          + "掃描：" + threads.length + " 則\n"
          + "標籤：" + stats.labeled + " 則\n"
          + "歸檔：" + stats.archived + " 則\n"
          + "垃圾桶：" + stats.trashed + " 則";
  sendTelegram(msg);
  Logger.log(msg);
}

// ════════════════════════════════════════════════════════════════
// ② cleanupInbox — 一次性大掃除（手動跑一次）
//    清理 90天前 ~ 1年內的 inbox
// ════════════════════════════════════════════════════════════════
function cleanupInbox() {
  var labels  = ensureLabels();
  var now     = new Date();
  var threads = GmailApp.search("in:inbox older_than:90d newer_than:365d", 0, 500);
  var stats   = { skipped: 0, archived: 0, trashed: 0 };

  threads.forEach(function(thread) {
    if (isThreadStarred(thread)) { stats.skipped++; return; }

    var firstMsg = thread.getMessages()[0];
    var from     = firstMsg.getFrom().toLowerCase();
    var subject  = firstMsg.getSubject().toLowerCase();

    // 重要文件 → label + archive
    if (isImportant(subject)) {
      addLabelIfNew(thread, LABEL_IMPORTANT, labels, stats);
      thread.moveToArchive(); stats.archived++;
      return;
    }

    // 符合 trash 規則 → trash
    var isTrashable = RULES.some(function(r) {
      return r.trashReadDays !== undefined && matchesRule(from, subject, r);
    });
    if (isTrashable) {
      removeLabelsAndTrash(thread); stats.trashed++;
      return;
    }

    // 其他（含已有 label）→ archive
    thread.moveToArchive(); stats.archived++;
  });

  var msg = "Inbox 大掃除完成\n\n"
          + "掃描：" + threads.length + " 則（90天前~1年內）\n"
          + "星號跳過：" + stats.skipped + " 則\n"
          + "歸檔：" + stats.archived + " 則\n"
          + "垃圾桶：" + stats.trashed + " 則";
  sendTelegram(msg);
  Logger.log(msg);
}

// ════════════════════════════════════════════════════════════════
// ③ migrateLabels — 舊 label 遷移到新 label（手動跑一次）
// ════════════════════════════════════════════════════════════════
function migrateLabels() {
  var migrationMap = [
    { from: "銀行-信用卡",  to: LABEL_BANKING },
    { from: "購物-外送",    to: LABEL_SHOPPING },
    { from: "旅遊-訂房",    to: LABEL_SHOPPING },
    { from: "電子報-學習",  to: LABEL_NEWSLETTER },
    { from: "投資-證券",    to: LABEL_IMPORTANT },
    { from: "保險",         to: LABEL_IMPORTANT },
    { from: "科技-訂閱",    to: null },
    { from: "待刪除",       to: null }
  ];

  var newLabels = ensureLabels();
  var totalMoved = 0;

  migrationMap.forEach(function(m) {
    var oldLabel = GmailApp.getUserLabelByName(m.from);
    if (!oldLabel) return;

    var threads = GmailApp.search('label:"' + m.from + '"', 0, 500);
    threads.forEach(function(thread) {
      thread.removeLabel(oldLabel);
      if (m.to && newLabels[m.to]) {
        thread.addLabel(newLabels[m.to]);
      }
      totalMoved++;
    });

    // 刪除舊 label
    deleteLabel(oldLabel.getId());
    Logger.log("遷移完成：" + m.from + " → " + (m.to || "（刪除）") + "，" + threads.length + " 則");
  });

  sendTelegram("標籤遷移完成\n共處理：" + totalMoved + " 則對話");
  Logger.log("migrateLabels 完成，共 " + totalMoved + " 則");
}

// ════════════════════════════════════════════════════════════════
// ④ trashOldNotifications — 每週日 2am
//    清理 15天前 ~ 1年內的通知/促銷類信件
// ════════════════════════════════════════════════════════════════
var TRASH_QUERIES = [
  'subject:("消費通知" OR "刷卡通知" OR "消費提醒" OR "刷卡成功" OR "transaction alert")',
  'subject:("登入通知" OR "登入提醒" OR "網銀登入" OR "sign-in alert" OR "login alert")',
  'subject:("優惠活動" OR "限時特賣" OR "折扣碼" OR "promo code" OR "special offer")'
];

function trashOldNotifications() {
  var total = 0;
  TRASH_QUERIES.forEach(function(q) {
    var threads = GmailApp.search(q + " older_than:15d newer_than:365d -in:trash", 0, 200);
    threads.forEach(function(t) { removeLabelsAndTrash(t); });
    total += threads.length;
  });
  sendTelegram("定期清理完成\n移入垃圾桶：" + total + " 則（15天~1年前）");
  Logger.log("trashOldNotifications 完成，共 " + total + " 則");
}

// ════════════════════════════════════════════════════════════════
// ⑤ emptyTrash — 每月 1 日 3am（永久刪除）
// ════════════════════════════════════════════════════════════════
function emptyTrash() {
  var token   = ScriptApp.getOAuthToken();
  var threads = GmailApp.search("in:trash older_than:30d", 0, 500);
  var count   = threads.length;

  threads.forEach(function(thread) {
    try {
      UrlFetchApp.fetch(
        "https://gmail.googleapis.com/gmail/v1/users/me/threads/" + thread.getId(),
        { method: "delete", headers: { "Authorization": "Bearer " + token }, muteHttpExceptions: true }
      );
    } catch(e) { Logger.log("永久刪除失敗: " + thread.getId() + " - " + e); }
  });

  sendTelegram("垃圾桶清理完成（每月）\n永久刪除：" + count + " 則");
  Logger.log("emptyTrash 完成，刪除 " + count + " 則");
}

// ════════════════════════════════════════════════════════════════
// 工具函數
// ════════════════════════════════════════════════════════════════

function isThreadStarred(thread) {
  return thread.getMessages().some(function(m) { return m.isStarred(); });
}

function isImportant(subject) {
  return IMPORTANT_SUBJECTS.some(function(kw) {
    return subject.indexOf(kw.toLowerCase()) !== -1;
  });
}

function matchesRule(from, subject, rule) {
  var senderHit  = rule.senders.some(function(s)  { return from.indexOf(s.toLowerCase())    !== -1; });
  var subjectHit = rule.subjects.some(function(s) { return subject.indexOf(s.toLowerCase()) !== -1; });
  return senderHit || subjectHit;
}

function addLabelIfNew(thread, labelName, labels, stats) {
  if (!labelName || !labels[labelName]) return;
  var already = thread.getLabels().some(function(l) { return l.getName() === labelName; });
  if (!already) {
    thread.addLabel(labels[labelName]);
    if (stats) stats.labeled++;
  }
}

function removeLabelsAndTrash(thread) {
  thread.getLabels().forEach(function(lbl) { thread.removeLabel(lbl); });
  thread.moveToTrash();
}

function ensureLabels() {
  var map = {};
  [LABEL_IMPORTANT, LABEL_BANKING, LABEL_SHOPPING, LABEL_NEWSLETTER].forEach(function(name) {
    var lbl = GmailApp.getUserLabelByName(name);
    if (!lbl) lbl = GmailApp.createLabel(name);
    map[name] = lbl;
  });
  return map;
}

function deleteLabel(labelId) {
  try {
    var token = ScriptApp.getOAuthToken();
    UrlFetchApp.fetch(
      "https://gmail.googleapis.com/gmail/v1/users/me/labels/" + labelId,
      { method: "delete", headers: { "Authorization": "Bearer " + token }, muteHttpExceptions: true }
    );
  } catch(e) { Logger.log("Label 刪除失敗: " + labelId + " - " + e); }
}

function sendTelegram(text) {
  try {
    UrlFetchApp.fetch("https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage", {
      method: "post",
      contentType: "application/json",
      payload: JSON.stringify({ chat_id: CHAT_ID, text: text })
    });
  } catch(e) { Logger.log("Telegram 推送失敗: " + e); }
}

// ════════════════════════════════════════════════════════════════
// setupTriggers — 只跑一次
// ════════════════════════════════════════════════════════════════
function setupTriggers() {
  ScriptApp.getProjectTriggers().forEach(function(t) { ScriptApp.deleteTrigger(t); });

  ScriptApp.newTrigger("processEmails")
    .timeBased().atHour(8).nearMinute(0).everyDays(1).create();
  ScriptApp.newTrigger("processEmails")
    .timeBased().atHour(20).nearMinute(0).everyDays(1).create();
  ScriptApp.newTrigger("trashOldNotifications")
    .timeBased().onWeekDay(ScriptApp.WeekDay.SUNDAY).atHour(2).create();
  ScriptApp.newTrigger("emptyTrash")
    .timeBased().onMonthDay(1).atHour(3).create();

  Logger.log("Triggers: processEmails(8am/8pm) + trashOldNotifications(週日2am) + emptyTrash(月1日3am)");
}

```
