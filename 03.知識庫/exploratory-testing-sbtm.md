---
title: "探索性測試 + SBTM：AI 時代的測試策略"
tags: [testing, playwright, claude-code, QA, exploratory-testing]
date: 2026-04-03
category: 03.科技工具
source: Threads post
---

## 核心觀念

AI 寫 code 速度×10，但自動化測試慢（10 個測項跑 35 分鐘）→ 抵消 AI 帶來的效能紅利。

**解法：探索性測試（Exploratory Testing, ET）+ SBTM**

## 為什麼自動化測試不夠？

1. 維護成本高：UI 一變，腳本就斷
2. 回饋太慢：等腳本跑完，思路已斷
3. 只能驗證「已知」，測不到意外 Bug

## 探索性測試精髓：Test Charter

不是亂測，而是寫好「測試章程」：

| 要素 | 說明 | 範例 |
|------|------|------|
| **Target（目標）** | 要攻擊哪個功能/邏輯 | 早鳥票邊界日期計算 |
| **Task（任務）** | 具體攻擊方式 | 跨月、閏年、極端時間點 |
| **Timebox（時限）** | 專注時間 | 30 分鐘內 |

## AI 時代建議流程

```
AI 寫 code 完成
    ↓
寫 Test Charter（5 分鐘）
    ↓
ET 探索測試（15~30 分鐘）← 比等腳本跑完更快找到 Bug
    ↓
自動化腳本驗證已知問題（背景跑）
```

## 適用於 My Wallet Trip

- 每次新功能完成 → 先寫 Charter 再跑 Playwright MCP
- Charter 範例：
  - Target：旅遊模式刪除所有旅程後的狀態
  - Task：刪光旅程 → 切模式 → 確認空狀態
  - Timebox：15 分鐘

## 參考資源

- AI 協作的探索性測試課程 (2026/4/18)：https://agile3uncles.com/products/t001/
- 研發效能評量 (2024/4/19)：https://agile3uncles.com/products/p002/
