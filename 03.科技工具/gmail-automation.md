---
title: "Gmail Automation - Google Apps Script"
tags: [gmail, apps-script, automation, telegram]
date: 2026-03-29
category: 03.科技工具
source: 自建
---

## 摘要

> Google Apps Script 自動分類 Gmail，依規則貼標籤 + 歸檔，每天早上 8 點 / 晚上 8 點執行，結果推送 Telegram。每月 1 日清除垃圾筒。

## 設定

| 項目 | 值 |
|------|-----|
| 觸發時間 | 每日 08:00 / 20:00 |
| 掃描範圍 | in:inbox newer_than:30d（最多 200 則）|
| 舊信清理 | 購物-外送 / 電子報-學習 超過 14 天 → 移至垃圾筒 |
| 垃圾筒清理 | 每月 1 日 03:00 永久刪除 30 天以上郵件 |
| Telegram Bot | BOT_TOKEN / CHAT_ID 填在 script 頂部 |

## 部署步驟

1. 前往 [script.google.com](https://script.google.com)
2. 進入專案 → 全選刪除 → 貼上下方程式碼
3. 存檔
4. 執行 `setupTriggers()` → 授權（會要求 Gmail 權限）
5. 執行 `processEmails()` 測試

## 版本記錄

| 版本 | 日期 | 變更 |
|------|------|------|
| v1.0 | 2026-03-27 | 初版：規則分類 + OTP 推送 |
| v1.1 | 2026-03-27 | 修 Telegram 推送格式 |
| v1.2 | 2026-03-29 | 移除 OTP 功能；修 label double-count |
| v1.3 | 2026-03-30 | 購物-外送/電子報-學習 超過 14 天移至垃圾筒；新增 emptyTrash() 每月清除 |
| v1.4 | 2026-03-30 | inbox 不移垃圾筒；只有已歸檔的舊信才移（搜尋加 -in:inbox）|
| v1.5 | 2026-03-30 | label 名稱加引號，修 `-` 被 Gmail 當成排除符號的 bug |
| v1.6 | 2026-03-31 | BOT_TOKEN / CHAT_ID 改用 PropertiesService，不再明碼寫死 |

## 完整程式碼 v1.5

```javascript
// ========================================
// Gmail 自動分類 v1.5
// ========================================

var BOT_TOKEN = PropertiesService.getScriptProperties().getProperty("BOT_TOKEN");
var CHAT_ID   = PropertiesService.getScriptProperties().getProperty("CHAT_ID");

var RULES = [
  {
    label: "銀行-信用卡",
    senders: ["hsbc", "中國信託", "ctbcbank", "國泰世華", "cathaybk", "台新銀行", "taishinbank",
              "玉山銀行", "esunbank", "渣打銀行", "standardchartered", "line bank", "linebank",
              "將來銀行", "nextbank", "台北富邦", "fubon", "american express", "amex", "bitopro"],
    subjects: ["帳單", "對帳單", "繳費通知", "信用卡", "扣款", "statement", "payment due"],
    archiveReadDays: 3,
    archiveUnreadDays: null
  },
  {
    label: "投資-證券",
    senders: ["富邦證券", "firstrade", "安聯投信", "野村", "財報狗", "強基金"],
    subjects: ["交易確認", "對帳", "配息", "淨值", "買進", "賣出"],
    archiveReadDays: 3,
    archiveUnreadDays: null
  },
  {
    label: "保險",
    senders: ["三商美邦", "富邦產險", "凱基人壽", "國泰人壽"],
    subjects: ["保費", "保單", "理賠", "繳費通知", "續保"],
    archiveReadDays: 7,
    archiveUnreadDays: null
  },
  {
    label: "旅遊-訂房",
    senders: ["skyscanner", "agoda", "trip.com", "intercontinental", "cathay pacific",
              "じゃらん", "長榮航空", "eztravel", "i prefer", "small luxury hotels"],
    subjects: ["訂房確認", "booking confirmation", "航班確認", "itinerary", "check-in"],
    archiveReadDays: 1,
    archiveUnreadDays: null
  },
  {
    label: "購物-外送",
    senders: ["uber eats", "ubereats", "rakuten", "coupang", "costco", "蝦皮", "shopback",
              "atmos", "星巴克", "starbucks", "樂天kobo", "kobo"],
    subjects: ["訂單確認", "出貨通知", "配送", "order confirmation", "shipped", "已出貨"],
    archiveReadDays: 1,
    archiveUnreadDays: 7,
    deleteAfterDays: 14   // 超過 14 天移至垃圾筒
  },
  {
    label: "科技-訂閱",
    senders: ["google", "github", "ollama", "anthropic", "claude", "asus"],
    subjects: ["subscription", "invoice", "payment receipt", "訂閱", "發票", "receipt"],
    archiveReadDays: 3,
    archiveUnreadDays: null
  },
  {
    label: "電子報-學習",
    senders: ["it邦幫忙", "ithome", "商業周刊", "coursera", "udemy", "畫張圖", "嘛賺金", "accupass"],
    subjects: ["每日摘要", "電子報", "newsletter", "daily digest", "週報"],
    archiveReadDays: 1,
    archiveUnreadDays: 3,
    deleteAfterDays: 14   // 超過 14 天移至垃圾筒
  },
  {
    label: "待刪除",
    senders: [],
    subjects: ["已登入", "登入通知", "sign-in alert", "login alert", "security alert",
               "new sign-in", "新裝置登入", "登入提醒", "異常登入", "suspicious sign"],
    archiveReadDays: 0,
    archiveUnreadDays: 0,
    markRead: true
  }
];

// 超過 deleteAfterDays 的 label 舊信（已歸檔）→ 移至垃圾筒
var DELETE_RULES = [
  { label: "購物-外送",  days: 14 },
  { label: "電子報-學習", days: 14 }
];

function processEmails() {
  var labels = ensureLabels();
  var now = new Date();
  // 掃描範圍拉到 30 天，才能抓到超過 14 天待刪的舊信
  var threads = GmailApp.search("in:inbox newer_than:30d", 0, 200);
  var labelCount = {};
  var archivedCount = 0;
  var trashedCount = 0;

  threads.forEach(function(thread) {
    var firstMsg = thread.getMessages()[0];
    var from     = firstMsg.getFrom().toLowerCase();
    var subject  = firstMsg.getSubject().toLowerCase();
    var isRead   = !thread.isUnread();
    var ageDays  = (now - firstMsg.getDate()) / (1000 * 60 * 60 * 24);

    for (var i = 0; i < RULES.length; i++) {
      var rule = RULES[i];
      if (!matchesRule(from, subject, rule)) continue;

      // 只有尚未貼過這個 label 才計入統計（避免早晚 double count）
      if (labels[rule.label]) {
        var alreadyLabeled = thread.getLabels().some(function(l) {
          return l.getName() === rule.label;
        });
        if (!alreadyLabeled) {
          thread.addLabel(labels[rule.label]);
          labelCount[rule.label] = (labelCount[rule.label] || 0) + 1;
        }
      }

      if (rule.markRead) {
        thread.markRead();
        isRead = true;
      }

      var shouldArchive = false;
      if (rule.archiveUnreadDays === 0) {
        shouldArchive = true;
      } else if (isRead && rule.archiveReadDays !== null && ageDays >= rule.archiveReadDays) {
        shouldArchive = true;
      } else if (!isRead && rule.archiveUnreadDays !== null && ageDays >= rule.archiveUnreadDays) {
        shouldArchive = true;
      }

      if (shouldArchive) {
        thread.moveToArchive();
        archivedCount++;
      }
      break;
    }
  });

  // 掃描已歸檔（非 inbox）但超過 deleteAfterDays 的舊信 → 移至垃圾筒
  // label 名稱加引號，避免 - 被 Gmail 當成排除符號
  DELETE_RULES.forEach(function(item) {
    var oldThreads = GmailApp.search(
      "label:\"" + item.label + "\" older_than:" + item.days + "d -in:inbox -in:trash",
      0, 200
    );
    oldThreads.forEach(function(thread) {
      thread.moveToTrash();
      trashedCount++;
    });
  });

  var hour = now.getHours();
  var timeLabel = hour < 12 ? "早上" : "晚上";
  var labelLines = Object.keys(labelCount).map(function(k) {
    return "  • " + k + "：" + labelCount[k] + " 封";
  });

  var msg = "Gmail 整理完成（" + timeLabel + "）\n\n"
          + "掃描：" + threads.length + " 則對話\n"
          + "歸檔：" + archivedCount + " 則\n"
          + "移至垃圾筒：" + trashedCount + " 則\n";

  if (labelLines.length > 0) {
    msg += "標籤分類：\n" + labelLines.join("\n");
  } else {
    msg += "無新郵件需分類";
  }

  sendTelegram(msg);
  Logger.log("processEmails 完成，歸檔 " + archivedCount + "，垃圾筒 " + trashedCount);
}

// 每月 1 日：永久清除垃圾筒 30 天以上的郵件
function emptyTrash() {
  var token = ScriptApp.getOAuthToken();
  var threads = GmailApp.search("in:trash older_than:30d", 0, 500);
  var count = threads.length;

  threads.forEach(function(thread) {
    try {
      UrlFetchApp.fetch(
        "https://gmail.googleapis.com/gmail/v1/users/me/threads/" + thread.getId(),
        {
          method: "delete",
          headers: { "Authorization": "Bearer " + token },
          muteHttpExceptions: true
        }
      );
    } catch(e) {
      Logger.log("永久刪除失敗: " + thread.getId() + " - " + e);
    }
  });

  var msg = "垃圾筒清理完成（每月）\n永久刪除：" + count + " 則對話";
  sendTelegram(msg);
  Logger.log(msg);
}

function matchesRule(from, subject, rule) {
  var senderHit  = rule.senders.some(function(s)  { return from.indexOf(s.toLowerCase()) !== -1; });
  var subjectHit = rule.subjects.some(function(s) { return subject.indexOf(s.toLowerCase()) !== -1; });
  return senderHit || subjectHit;
}

function ensureLabels() {
  var map = {};
  RULES.forEach(function(rule) {
    var lbl = GmailApp.getUserLabelByName(rule.label);
    if (!lbl) lbl = GmailApp.createLabel(rule.label);
    map[rule.label] = lbl;
  });
  return map;
}

function sendTelegram(text) {
  try {
    UrlFetchApp.fetch("https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage", {
      method: "post",
      contentType: "application/json",
      payload: JSON.stringify({ chat_id: CHAT_ID, text: text, parse_mode: "Markdown" })
    });
  } catch(e) {
    Logger.log("Telegram 推送失敗: " + e);
  }
}

function setupTriggers() {
  ScriptApp.getProjectTriggers().forEach(function(t) {
    ScriptApp.deleteTrigger(t);
  });

  ScriptApp.newTrigger("processEmails")
    .timeBased().atHour(8).nearMinute(0).everyDays(1).create();

  ScriptApp.newTrigger("processEmails")
    .timeBased().atHour(20).nearMinute(0).everyDays(1).create();

  ScriptApp.newTrigger("emptyTrash")
    .timeBased().onMonthDay(1).atHour(3).create();

  Logger.log("Triggers: processEmails(8am/8pm) + emptyTrash(每月1日3am)");
}
```
