---
title: 現在的工作脈絡
tags: ["上下文", "專案"]
date: 2026-04-21
category: 身份
---

## 進行中的專案

| 專案 | 說明 | 狀態 |
|------|------|------|
| cc_processor | 信用卡帳單自動化（HSBC + 國泰），OCR + Notion 寫入 | 運作中，每日 09:00 |
| sales_report_processor | Gmail 觸發 → 下載 xlsx → 跑業績統計 → 寄報表 | 運作中，每日排程 |
| spa_anku_processor | SPA安庫彙總，Gmail 觸發 → 生成 xlsx → 寄送 | 運作中 |
| My Wallet Trip | 旅遊 + 日常記帳 PWA，Gemini OCR + Notion + Vercel | 運作中 |
| MyNotes | 個人知識庫，Obsidian + GitHub，每小時自動備份 | 整理中 |
| Gmail Automation | Google Apps Script 自動分類 Gmail | 運作中 |

## 關鍵腳本一句話說明

| 腳本 | 這個腳本做什麼 |
|------|--------------|
| sales_report_processor.py | Gmail 收到 Hasna 寄的 SalesOrderReport xlsx → 跑業務業績統計 → 寄報表給雙方 |
| spa_anku_processor.py | Gmail 收到 Hasna 寄的 SPA安庫 xlsx → 生成機種×安庫×庫存×接單彙總表 → 寄送 |
| 業務業績統計.py | 讀 SalesOrderReport + 料號產品分類，產出 6 個樞紐分析（照品類/機種/業務分析業績） |
| reauth_gmail.py | 重新授權 Gmail OAuth token（token 7天過期，需手動跑） |
| mygmail_automationn.js | 每天 8am/8pm 掃 inbox，依規則貼標籤/歸檔/丟垃圾桶；週日清通知信；月初清垃圾桶 |

## AI 工具分工

| Agent | 角色 |
|-------|------|
| Claude Code | 主力執行（coding、自動化、存 MyNotes） |
| 一蘭（openclaw） | Telegram Q&A、save_article |
| Gemini CLI | 研究、掃描文件 |
| Codex | 純 coding 任務 |

## 目前卡住的問題

- Gmail OAuth token 7天過期，需定期跑 reauth_gmail.py
- MyNotes 索引自動更新（concept-map、tag-index 未自動同步）
- writing-voice skill 需要更多派哥的寫作樣本來精煉

## 暗語 / 快捷指令

| 說法 | 意思 |
|------|------|
| 跑 SOP | 研究文章 → 評估 → 存 MyNotes → 建議 skill |
| 問知識庫 | 翻 03.科技工具/*.md，交叉比對後回答 |
| 存下來 | 把洞見存為新筆記，git push |
| 跑健檢 | 掃所有筆記：找矛盾、缺漏、意外連結 |
| 收工 | 寫交班單，/compact |
