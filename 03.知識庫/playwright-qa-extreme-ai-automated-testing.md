---
title: playwright-qa-extreme：AI + Playwright 雙軌自動化 QA，輸出 HTML 報告
tags: ["工具", "Claude Code", "自動化", "Python", "工作流程"]
date: 2026-04-23
category: 工作流程
source: https://github.com/aster-life/playwright-qa-extreme
---

## 這是什麼

把 QA 流程自動化的 Claude Code skill。AI 像真實用戶逛網站找問題，腳本負責邊界測試，最後輸出可分享的 HTML 報告。

安裝：一行指令（Windows/macOS）→ github.com/aster-life/playwright-qa-extreme

## 兩套工具分工

| 工具 | 負責什麼 | 為什麼 |
|------|---------|--------|
| Claude_in_Chrome | 「理解」：看截圖、讀 DOM、用自然語言找元素（「找關閉按鈕」）| AI 適合模糊判斷 |
| Playwright | 「重複」：邊界測試（空白送出、XSS 注入、500字 overflow）、regression check | 腳本快、省 token、無隨機性 |

AI 負責理解，腳本負責重複。

## 輸出三份產物

1. **UAT 清單**：逐條打勾，對照規格一目了然
2. **Bug 報告**：P0–P3 分層，每個 Bug 有截圖 + 重現步驟 + 預期 vs 實際
3. **單一 HTML 報告**：截圖全部 base64 內嵌，離線可用，直接丟給老闆/客戶

## 核心洞見

最大感觸不是「AI 好強」——是**流程設計才是關鍵**。

AI 工具本身能力上限很高，但沒有清楚的流程框架，就會亂跑、亂判。每個 Phase 的邊界畫清楚，AI 才知道什麼時候做什麼、什麼時候停下來問人。

## 質疑

- 前提假設：「AI 像剛接案的 QA 工程師亂逛」——但 AI 的「亂逛」路徑是由訓練資料決定的，可能系統性地忽略某些邊界（例如特定語言的輸入、行動裝置邊界）
- 適用邊界：適合有明確 UI 的 web app；對 API-only、資料管線、非同步後台處理的測試幾乎沒幫助
- 潛在反例：base64 內嵌截圖的 HTML 報告在截圖很多時會很大，老闆用手機打開可能卡死

## 對標

- **人類 QA vs 自動化 QA 的老問題**：這篇的解法不是選一個，而是讓 AI 做「第一輪探索」，Playwright 做「確認性重複驗證」——同時保留了兩者的優點
- **醫院分診系統**：AI 先做 triage（哪裡可能有問題），腳本做精確診斷——分工邏輯一樣

## 對派哥的啟示

My Wallet Trip 目前沒有 QA 流程，每次改完就手動點幾下就上了。

最直接的落地：
- 用這個 skill 跑一次 MWT 的 UAT，輸出 HTML 報告存 Google Drive
- 把 Playwright 的邊界測試腳本固定下來（空白送出、幣別換算、日期邊界），之後每次改版前跑一次

比較適用的場景：
- MWT 記帳頁面（輸入欄位多，邊界複雜）
- 報表頁面（數字顯示正確性）
- 旅程建立流程（跨頁狀態）

## 連結筆記

- [[ai-era-testing-strategy]]
- [[ai-coding-testing-management-10-issues]]
- [[harness-engineering-coding-agents]]
- [[claude-code-computer-use]]
