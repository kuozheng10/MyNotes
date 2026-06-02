# AI Coding 時代的測試四象限

> 來源：agile3uncles.com 課程 T005《不確定時代下的敏捷測試》
> 整理日期：2026-06-02

---

## 核心洞見

> AI 讓寫 code 變便宜，但「判斷 code 對不對、需求清不清楚」的重要性反而整個往上跳。
> 測試的重心，從敲鍵盤的那一刻，往前挪到了想清楚的那一刻。

---

## 四個階段

### 1. 測試左移：把問題擋在進來之前

| 做法 | 說明 |
|------|------|
| Spec by Example | 用具體例子把需求釘死，需求模糊 AI 只會把模糊放大 |
| AI Code Quality Gate | 在 PR 階段卡品質，爛代碼進不了主幹 |
| Secure-by-Default | 安全變成預設值，不等出事才補 |

---

### 2. 持續集成：讓 pipeline 自己撐住

| 做法 | 說明 |
|------|------|
| Test Impact Analysis | 只跑真正受影響的測試，AI 大量產 code → 測試案例爆量時，不全跑省時間 |
| **Self-Healing CI** | 環境抖動、測試莫名紅燈時，自動修掉一部分，不用半夜爬起來盯 pipeline |

---

### 3. 持續測試：在迭代裡反覆驗

標準項目：功能、非功能、探索、回歸、驗收

**AI 時代新增：**

| 做法 | 說明 |
|------|------|
| **Eval Gate** | 用一整組評測題組驗證 AI 行為穩不穩，單筆碰巧通過不算數 |
| **Adversarial Testing** | 刻意用怪輸入、邊界情況去戳 AI，找出沒想到的出包點 |

---

### 4. 測試右移：把生產環境也當成測試場

| 做法 | 說明 |
|------|------|
| **Continuous Verification** | 持續盯著系統行為有沒有慢慢漂掉（drift） |
| **Audit Trail** | 把 AI 做過的決策一筆筆記下來，出事時查得到誰在什麼時候做了什麼 |
| 生產線上測試 / A/B 測試 / 線上監控 | 標準 |

---

## 心理層面：為什麼功能做完反而更不踏實

- 以前：一行行自己敲，心裡有底
- 現在：一大段瞬間冒出來，「這段代碼是誰寫的？邏輯對不對？有沒有埋雷？」

**對應做法**：Audit Trail + Adversarial Testing 是找回「心理確定感」的兩個主要工具。

---

## 相關筆記

- [[ai-era-testing-full-pipeline]] — AI Coding 測試全流程骨架
- [[ai-era-testing-strategy]] — 什麼值得測（高 ROI 測試案例）
- [[performance-testing-before-you-start]] — 同源（agile3uncles）效能測試五件事
- [[performance-testing-basics-quiz]] — 效能測試基本概念
