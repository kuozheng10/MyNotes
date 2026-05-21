---
title: 雙 AI 自動化團隊：OpenClaw 與 Hermes 的協作架構
tags: ["AI", "Agent", "工作流程", "自動化"]
date: 2026-04-17
category: 工作流程
source: goodarticle/2026-04-16_雙AI自動化團隊.md
---

## 這是什麼
這是一套結合 OpenClaw（主腦）與 Hermes（執行）的雙代理協作架構，透過 Obsidian 作為共享資料夾與知識樞紐，建立低成本、高效率且具備自動除錯能力的 AI 自動化團隊。

## 核心概念
- **主從互補架構**：OpenClaw 擔任主腦專攻複雜思考與高難度任務；Hermes 則作為運算成本極低的勞工，負責跑腿、基礎除錯與格式處理。
- **Obsidian 知識樞紐**：利用 Obsidian 建立專屬共享資料夾，讓不同 AI 代理同步任務脈絡、記錄犯過的錯誤，實現全天候無縫協作。
- **雙視窗監工模式**：使用者從「工人」轉變為「監工」，透過並排視窗將一端的優良半成品快速複製給另一端接手，優化交付流程。
- **低成本自動修復**：利用低配助理 Hermes 快速掃描高配代理 OpenClaw 的代碼報錯，縮短系統停機時間。

## 使用方法 / 快速啟動
1. **環境配置**：同時開啟 OpenClaw 與 Hermes 的介面並排顯示。
2. **建立樞紐**：在 Obsidian 中設定一個專屬資料夾，作為雙方代理的「共享記憶區」。
3. **任務交辦**：由 OpenClaw 產出核心邏輯或代碼庫，當發生報錯或需重複性修改時，交由 Hermes 執行。
4. **錯誤同步**：將執行過程中的錯誤記錄回 Obsidian 筆記，確保下次協作時能自動避坑。

## 對派哥的啟示
這套架構能直接應用在派哥目前的 `cc_processor` 與 `telegram_bot` 自動化專案中。派哥可以讓強大的 Claude 模型負責處理複雜的台灣銀行帳單（如國泰、台新、匯豐）解析邏輯，而將較簡單的 Telegram 訊息格式化、Log 監控與初步錯誤排除交給成本較低的 Hermes 等級模型。透過現有的 Obsidian 筆記庫，派哥可以將台灣特有的金融規則（如 amex 優惠、各行分期計算）寫成「技能筆記 (Skills)」，讓雙代理團隊在執行自動化任務時能隨時調閱，達成更精準且低成本的財務管理自動化。

## 連結筆記
## 連結筆記
- [[claude-routines-automation]]
- [[boris-parallel-claude-workflow]]
- [[full-agent-dev-ecosystem-goatwang]]
- [[ai-agent-modular-architecture]]
- [[ai-agent-system-design-over-prompt]]
