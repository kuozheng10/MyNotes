# AI Coding 時代的敏捷測試 — 品質缺口與應對實踐

> 來源：敏捷三叔公，課程「GenAI 時代下的敏捷測試」
> 課程日期：2026-07-26（線下）
> 儲存日期：2026-06-12
> 標籤：#testing #agile #ai-coding #QA #eval-gate #SBE #quality

---

## 問題背景：兩層缺口疊加

### AI 帶來的新缺口
- AI 幾秒生 200 行 code → reviewer 看不完
- AI 自己寫 code 又自己寫測試 → 全綠燈不代表品質
- 覆蓋率高，上線還是出包
- 出事了，責任怎麼追？

### 數據支撐
| 數據來源 | 數字 |
|---------|------|
| Stack Overflow 2025 | 84% 開發者已用或計畫用 AI 工具 |
| Veracode 2025 | **45% AI 生成程式碼含安全漏洞** |
| Apiiro 2025/09 | AI 程式碼導致特權提升漏洞增加 **322%** |

### 敏捷時代留下的測試債（舊問題未解）
- 發布頻率拉高 → 測試時間被壓縮
- 需求不清楚 → 測試憑感覺
- 回歸測試積累 → 跑一輪要好幾天

AI 把開發速度再往上推，舊問題沒解，缺口只會更大。

---

## AI 時代需重視的測試實踐

| 實踐 | 說明 |
|------|------|
| **Spec by Example (SBE)** | 需求用具體範例定義，測試才能當停止條件 |
| **Eval Gate** | AI 產出的驗收閘門，不讓未驗證程式碼進入 main |
| **對抗式測試** | 獨立 verifier agent 挑毛病，不讓寫的人自己驗收 |
| **Self-Healing CI** | CI 失敗自動修復並回報 |
| **Test Impact Analysis** | 只跑受影響的測試，加快 CI |
| **Audit Trail** | AI 修改的可追溯性，出事能追責 |

### 業界案例
- **Canva Magic Switch** — 大型 AI 功能的測試設計
- **Meta 預測式測試選擇** — 智能選擇要跑哪些測試

---

## 敏捷測試三層架構

### 測試左移
- 需求階段就對齊認知（SBE）
- 確認「對」長什麼樣子，再讓 AI 動手

### 開發過程多層次守住品質
- unit → integration → e2e 各層有自己的 guard
- AI 寫的測試需要人審查意圖，不只看通過率

### 測試右移 + 連續驗證
- 上線後的真實世界場景驗證
- flaky test 管理、canary 部署監控

---

## QA 角色轉變

```
過去：執行測試
現在：品質編排者（Quality Orchestrator）
```

- AI 接手越來越多測試執行工作
- QA 價值往「設計驗收條件」「管理 Eval Gate」「追蹤 Audit Trail」移動
- 需要的新能力：SBE 撰寫、AI 工具評估、風險判斷

---

## 與 Loop Engineering 的連結

這篇跟 [[loop-engineering-testing]] 高度互補：
- Loop Engineering 講「如何讓測試成為 agent 的停止條件」
- 這篇講「為什麼 AI 時代測試更重要，以及哪些實踐要補上」

**核心共識**：AI 加速了程式碼產出，但驗收標準（Spec）必須由人定義清楚，否則全綠燈只是「AI 說它測過了」。

---

## 相關筆記
- [[loop-engineering-testing]] — Loop 測試端四元件實作
- [[loop-engineering-agentic-ai]] — Loop Engineering 基礎概念
- [[ai-coding-team-cld]] — WIP 天然煞車消失的 CLD
