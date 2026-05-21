---
title: 用 AI 建武器再交給 AI 用 — Nick Baumann 的 Skill 建構思路
tags: [Agent, Skills, 自動化, Codex, 架構設計, Claude-Code]
date: 2026-04-13
category: AI工具
source: 社群文章（作者不明，Nick Baumann / OpenAI，轉自 goodarticle）
---

## 核心問題

每次叫 AI 處理事情，都要重新解釋一遍背景、格式、遊戲規則。**問題不是你不會問，而是你一直在問同一件事。**

Nick Baumann（OpenAI 員工）的解法：**讓 AI 記住你的規則，與其一直解釋，不如把解釋寫進工具裡。**

> 這個概念和 Garry Tan 的 [thin harness / fat skills](garry-tan-thin-harness-fat-skills.md) 完全一致。

---

## Nick 的三個 Skill 案例

### codex-threads — 搜自己的對話紀錄

問題：直接把整個 session 存檔丟給 Codex 太雜，裡面混著工具輸出、測試痕跡。

解法：建本地可搜尋索引，讓 Codex 用指令搜尋、解讀特定段落，不整包倒進去。

**最佳實踐**：從「效果好的 thread」抽出模式 → 固化成 skill。

### slack-cli — 在 Slack 歷史裡挖答案

問題：授權決策、review 結論埋在某個 thread 裡，關鍵字搜不到。

解法：把操作包成 command，讓 Codex 自己組合執行。走正常 Slack 授權，只是把相同的存取行為塑造成 agent 能組合的指令形式。

### typefully-cli — 管 Twitter/X 草稿

設計重點：預設只建草稿，不允許刪除或覆蓋。

**最聰明的地方**：安全紀律被寫進工具設計裡，不靠每次口頭提醒。

> **安全的預設值，比事後叮嚀更可靠。**

---

## 作者的實戰：火車票乘車證明自動下載

做法：
1. 先讓 AI 自己用瀏覽器跑一遍，觀察卡在哪裡
2. 卡住就介入，直到完成
3. 讓 AI 覆盤 → 把流程寫成腳本

結果：之後只要給截圖 + 身分證，自動下載 PDF、上傳雲端、記錄到 Sheet。

工具：Playwright（讓 AI 看見每一步操作，可視化卡點）

---

## Session 觀察工具

作者寫了「漸進式讀取 session」工具：
- 先掌握整個流程：步驟、工具呼叫、錯誤
- 再選擇深入某個 tool call 的細節

效果：不在黑箱裡猜 AI 做了什麼，能一層一層拆開來看，大幅提升 skill 迭代效率。

---

## 閉環思維

```
讓 AI 先操作一遍 → 覆盤寫成腳本 → 把解釋寫進工具
                                    ↑
         session 觀察工具讓這個循環可以持續強化
```

**「可以寫成程式的就寫起來、可以變成 Skill 的就提煉出來，AI 用起來才會更高效。」**

---

## 對派哥的應用

- 任何重複超過 3 次的任務 → 問自己「這該寫成 skill 嗎？」
- Playwright 觀察 AI 操作流程：cc_processor 卡住時可用這個方式 debug
- 預設值安全設計：一蘭的 skill 裡也要有「預設唯讀，要寫入才明確說」的規範
