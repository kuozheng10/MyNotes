---
title: AI Coding 時代的 Performance Test 基本知識
tags: [效能測試, AI Coding, k6, CI/CD, vibe-coding, P95, Load Test, Soak Test]
date: 2026-05-07
category: AI工具
---

## 這是什麼

AI 寫的程式「跑得動」不等於「跑得順」。這篇整理 AI coding 時代開發團隊必知的效能測試知識，特別適合 vibe coding / Cursor / Copilot 開發者。

---

## AI 程式碼的效能地雷

| 地雷 | 說明 |
|------|------|
| N+1 查詢 | 迴圈裡逐筆查 DB，100 筆資料查 100 次 |
| 繞路邏輯 | 寫法「漂亮」但多繞不必要的步驟 |
| 沒快取 | 相同資料每次都重新取，不做 cache |
| 肥套件 | 裝了整包 library 只用一個 function |

這些問題單元測試/E2E 測試看不出來，只有 performance test 抓得到。

---

## 四種必知測試

| 測試類型 | 用途 |
|---------|------|
| Load Test（負載）| 模擬正常使用人數，看穩定性 |
| Stress Test（壓力）| 持續加壓到極限，找系統上限 |
| Spike Test（尖峰）| 模擬活動/上新聞的瞬間爆量 |
| Soak Test（耐久）| 連跑數小時，找 memory leak、連線未關閉 |

**實例**：Cursor 寫的訂單 API 功能全過，Soak Test 跑 8 小時後記憶體一直長大——原來 AI 忘了關 DB 連線。

---

## 關鍵數字

**不要只看平均值，平均值會騙人。**

| 指標 | 說明 |
|------|------|
| P95 / P99 | 最慢 5%/1% 使用者的等待時間。平均 200ms 但 P99 是 5s → 每 100 人有 1 人爆炸 |
| TPS / RPS | 每秒處理量，系統容量 |
| 錯誤率 | 高壓下錯了多少，門檻通常 < 1% |
| 資源使用率 | CPU/RAM/Disk/Network，AI 常出現「CPU 100% 但沒處理多少事」 |

---

## 導入策略

### 上線守門員
把效能測試加進上線 checklist：P95 < 500ms、錯誤率 < 0.5%，過不了不准上線。

### CI/CD 輕量壓測
每個 PR 跑 1-2 分鐘小壓測。AI 改一行可能讓某個查詢慢 10 倍，code review 看不出來，跑一下就現形。

### 建基準線
沒有「昨天的成績」就不知道今天進步還退步。AI 持續改 code，基準線必備。

### 測完整使用者流程
不要只測單一 API。登入→瀏覽→下單→付款串起來測，才能找到 AI 只看片段、沒看整體造成的慢點。

---

## 推薦工具

| 工具 | 特色 |
|------|------|
| **k6** | JS 寫腳本，與 CI/CD 整合容易，**最推薦** |
| JMeter | 老牌，有 GUI，QA 友善 |
| Locust | Python 寫腳本，Python 工程師首選 |

**最佳組合**：k6 + GitHub Actions — vibe coding 團隊 CP 值最高，幾乎無痛導入。

---

## 對派哥的應用

| 場景 | 建議 |
|------|------|
| My Wallet Trip | Notion API 呼叫容易 N+1，加 Soak Test 確認無 memory leak |
| cc_processor | 信用卡解析批次跑，加 Load Test 確認 09:00 排程不爆炸 |
| 任何 AI 生成的 API | PR 時加 k6 小壓測，防止 AI 悄悄塞地雷 |

---

## 連結參考

- [[ai-era-testing-strategy]] — AI 時代測試策略全局
- [[playwright-qa-extreme-ai-automated-testing]] — E2E 測試
- [[ai-coding-qa-myths]] — AI 測試迷思
- [[bdd-behavior-driven-development-ai-era]] — 行為驅動測試
