# Loop Engineering — 迴圈工程

> 來源：Peter Steinberger（技術圈名人）X 推文，2026-06，突破 200 萬瀏覽
> 核心論點：不要再自己對 AI 下 Prompt，改設計一個「Loop」讓迴圈去驅動 AI。

---

## 什麼是 Loop Engineering？

從「對話框輸入 Prompt」升級到「用程式自動驅動 AI」的開發思維轉變。

人類抽離對話，改寫自動化程式去控制 AI 的輸入與輸出。

---

## 三個核心要素

### 1. 主動代理（Proactive Agent）
AI 不再被動一問一答，而是能：
- 主動讀取 GitHub、Slack、Email 等外部資料
- 根據狀態自主做決策並執行

### 2. Feedback Loop（自動糾錯迴圈）
```
AI 產出 → 執行 → 自動測試 → 有錯 → 餵回 AI → 再修正 → 直到通過
```
不需人工介入，Loop 自己跑到正確才停。

### 3. 停機控制（Budget / Max Iteration）
- 設定最大迭代次數（避免無限死循環）
- 設定 token/cost 上限（省 API 帳單）
- **現代 AI 工程核心已是「如何讓 Loop 知道何時停下」**

---

## 過去 vs 現在

| 過去 | 現在 |
|------|------|
| 寫完美的 Prompt（低效） | 設計有自我驗證 + 預算上限的 Loop |
| 人工監看輸出 | 關筆電去睡覺，Loop 自己跑 |
| 一問一答 | Agent 自主讀資料、決策、執行 |

---

## 對派哥的關聯

這個概念其實就是派哥現在做的事：

- `cc_processor` = Feedback Loop（OCR → 解析 → 寫 Notion → 驗證）
- `run_bank_statements.py` = 排程自動執行的 Loop
- Claude Code + Codex = AI 代理執行任務，自動修錯後回報

**關鍵差距**：目前缺少的是「預算天花板」設計——萬一某個 parser 壞掉，可能無限 retry。建議後續在 launchd 任務加 max_retries + 失敗通知。

---

## 實作建議（派哥適用）

1. **加 max_retries**：每個 parser 最多 retry 3 次，超過就 TG 通知
2. **加 cost tracking**：記錄每次 Gemini API call 的 token 用量
3. **驗證閘門**：Loop 的結束條件不是「跑完」而是「驗證通過」（已有 SQLite vs Notion 比對，繼續沿用）

---

## 標籤
`#AI架構` `#Agent` `#自動化` `#Loop` `#PromptEngineering`

---
*存入日期：2026-06-10*
