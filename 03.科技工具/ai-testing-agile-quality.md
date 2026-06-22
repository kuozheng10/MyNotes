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

---

## Eval Gate 深探：三層架構 + 雙信號線

> 來源：敏捷三叔公 LinkedIn（2026-06-22）

### 核心問題：LLM 沒有唯一正確答案

傳統測試：`assertEqual(A → B)`，答案唯一。  
LLM 測試：同一問題有十種合理答法，不能逐字對比。

Eval Gate 不驗「答案對不對」，驗的是**這個輸出有沒有違反我們在乎的規則**：
- 有沒有亂編沒根據的內容（hallucination）
- 該引用來源的有沒有引用
- 該拒答的有沒有拒答
- 語氣有沒有歪掉
- 該回答的有沒有答完整

### 三難困境：便宜 × 快 × 統計顯著

| 若只顧兩個 | 結果 |
|-----------|------|
| 便宜 + 快（30 個範例） | 誤差範圍 > 品質退步幅度，假警報多，團隊學會無視 |
| 統計顯著 + 快（每 PR 跑 2000 筆） | $9/PR，22 分鐘，一個月後被默默關掉 |
| 統計顯著 + 便宜（夜間才跑） | 合理但無法即時擋 PR |

### 業界三層實作

| 層 | 觸發時機 | 內容 | 成本 |
|----|---------|------|------|
| **L1：快速閘門** | 每個 PR | 格式、引用、hallucination，用小型分類器判 | 幾乎免費 |
| **L2：LLM 評審** | 每日夜間 | 最強模型對全部範例打主觀分（語氣、幫助性） | 集中跑，攤平費用 |
| **L3：人工分群審查** | 每日 5 分鐘 | 工程師只看「問題分群後的異常」，不看每筆 | 時間極低 |

### 雙信號線

- **絕對地板**：抓災難級崩壞（如客服 agent 拒答率暴增）
- **滾動基準線**：跟過去 7 天平均比，抓「慢慢漂的退步」

> 基準必須滾動更新，不能凍結在上線當天——模型會漂、prompt 會漂、資料也會漂。

### 典型失敗案例

工程師只改一行 prompt → CI 全綠 → merge → 12 小時後客服 agent 開始把正常問題判成「我無法回答」。沒有 function 壞掉，只是 LLM 輸出悄悄變差了。

---

---

## Self-Healing CI — 兩個層次 + 三級成熟度

> 來源：敏捷三叔公 LinkedIn（2026-06-22）

### 兩個層次（常被混為一談）

| 層次 | 痛點 | 解法 |
|------|------|------|
| **L1 自我修復測試** | UI 改版 → locator 抓不到 → 整批紅燈（程式沒壞，測試腳本壞了）| AI 同時看文字/位置/class/DOM 結構「指紋」，自動找回元素 |
| **L2 自我修復管線** | build 失敗、dependency drift、YAML 打錯、環境問題 | 回饋迴圈：偵測 → 分析根因 → 動手修 → 驗證 → **提 PR 給人審**（不直接 merge）|

**核心迴圈（跟 Harness/Agentic Loop 同一家族）：**
`偵測失敗 → 分析根因 → 動手修 → 驗證 → 提 PR 給人審`

### 三級成熟度

| 級別 | 名稱 | 行為 |
|------|------|------|
| ① | 觀察者 | AI 只在旁評分，不擋 build，先累積「什麼叫好」的黃金資料集 |
| ② | 守門員 | blocking gate，信心分數低於門檻就擋下來，但不動手修 |
| ③ | 治療者 | 有寫入權限，自動修測試腳本或設定檔，再提 PR |

> 大部分認真的團隊現在卡在 ① 到 ② 之間。

### LLM-as-a-Judge（測 AI Agent 本身）

當測試對象是 AI agent，傳統字串比對完全失效。用另一個專門模型給主 agent 的輸出評分 → 這就是 [[ai-testing-agile-quality#Eval Gate]] 的核心概念。

### 工具地圖

| 類型 | 工具 |
|------|------|
| 測試平台型 | Mabl、Testim、Functionize、testRigor |
| 視覺回歸 | Applitools、Percy、Meticulous |
| 框架加掛 | Katalon、ACCELQ、Virtuoso QA |
| Playwright 導向 | Shiplight、Playwright MCP、Stagehand |
| 管線層 | GitHub Actions + Copilot、GitLab CI、CircleCI、Jenkins、Dagger |

**技術路線差異：**
- Testim 類：ML 多維評分（文字+位置+class+id+結構）
- Functionize 類：NLP + 電腦視覺，DOM 完全改掉也能辨識（含 canvas 渲染 UI）

### 效果數字（打折看）

| 數字 | 來源 | 可信度 |
|------|------|--------|
| 腳本維護 -95%、回歸快 2× | 全球零售商案例 | ⚠️ 廠商 case study |
| 維護工時 -88%（3 個月）| 不明 | ⚠️ 廠商 case study |
| 維護工作節省 ~70% | Capgemini World Quality Report | ✅ 較中性第三方 |

**建議用「七成」而非「九成五」跟人溝通預期。**

---

## 相關筆記
- [[loop-engineering-testing]] — Loop 測試端四元件實作
- [[loop-engineering-agentic-ai]] — Loop Engineering 基礎概念
- [[ai-coding-team-cld]] — WIP 天然煞車消失的 CLD
- [[ai-dev-problems-amplified-2026-06]] — DORA/Faros 數據：PR review +441%
