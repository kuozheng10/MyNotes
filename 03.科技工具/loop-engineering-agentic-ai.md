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

---

## 六大組成部分（2026-06 補充，含資訊圖）

> 來源：TripPlus 社群分享資訊圖，2026-06-11

| # | 元件 | 說明 |
|---|------|------|
| 1 | **自動化流程** | 按排程執行，探索、分類，將結果送回收件匣 |
| 2 | **工作樹 (Worktree)** | 使用獨立 worktree，平行工作不互相干擾 |
| 3 | **技能 (Skills)** | 記錄專案知識與規則（SKILL.md），減少重複解釋 |
| 4 | **外掛程式與連接器** | 透過 MCP 連接真實工具（Linear、Slack、CI、DB） |
| 5 | **子代理程式** | 分離「創造者」與「檢查者」，提升品質與可靠性 |
| 6 | **記憶（狀態）** | 使用 markdown/看板，記錄進度與待辦事項，不只放在對話 context |

### 一個 Loop 的流程（簡化版）

```
自動化流程每天執行
  → 開啟工作樹（隔離環境）
  → 子代理程式實作
  → 子代理程式檢查
  → 連接器行動（開 PR、更新工單）
  → 記錄結果（更新狀態）
  → 分類收件匣（人工處理）
  → 持續迭代，直到目標達成
```

### Loop 依然無法為你做的事

| ⚠️ | 說明 |
|---|------|
| **驗證** | 「完成」不等於「證明」，仍由人負責 |
| **理解力** | 不閱讀，就會與專案脫節 |
| **避免認知投障** | 自動化容易讓人停止思考 |

> 核心：建構 loop，但不要只當那個按下開始鍵的人。**保持工程師本色。**

---

---

## LangChain 四層 Loop 架構（2026-06 補充）

> 來源：工程師米奇 LinkedIn，轉述 LangChain Blog「The Art of Loop Engineering」
> 更新日期：2026-06-27

**核心觀點**：Agent 的威力不在模型本身，在於你在模型外面設計了幾層迴圈。

### 四層迴圈

| 層 | 名稱 | 功能 | 代價 |
|----|------|------|------|
| 1 | **Agent Loop** | 讓工作被完成（工具呼叫反覆跑到完成）| 基礎成本 |
| 2 | **Verification Loop** | 確保工作品質（Grader 評分 → 沒過 → 重做）| 延遲 + 成本增加 |
| 3 | **Event-Driven Loop** | 工作規模化自動化（事件觸發，agent 嵌入系統）| 架構複雜度 |
| 4 | **Hill Climbing Loop** | 系統自我改進（trace 分析 → 自動修改 prompt/tool）| 工程量高 |

### 各層流程

```
Loop 1 — Agent Loop
接收任務 → LLM 思考 → 呼叫工具 → 未完成？→ 繼續 → 完成 → 輸出

Loop 2 — Verification Loop
Agent 產出 → Grader 評分 → 通過 → 輸出
                          → 沒過 → feedback 回 agent → 重做

Loop 3 — Event-Driven Loop
事件觸發（webhook/排程/新文件）→ Agent 自動跑 → 結果寫回系統

Loop 4 — Hill Climbing Loop
Agent 跑 → 留 trace → 分析 agent 找問題 → 自動改 harness → 下輪更強
```

### 人類的位置

自動化不等於移除人類，而是把人類放在最有價值的位置：
- Loop 1 → 敏感操作前確認
- Loop 2 → 人類可當 Grader
- Loop 3 → 審批最終產出
- Loop 4 → harness 改動需人類 review 才部署

### Satya Nadella 的觀點

> 越早建立 learning loop 的公司——讓人類判斷力跟運算資源一起複利成長——會累積出很難被複製的優勢。

大部分人停在 Loop 1~2。真正的複利在 Loop 3~4。

### 對派哥現有系統的對應

| 派哥的系統 | 對應 Loop |
|-----------|----------|
| cc_processor 排程每天跑 | Loop 3（Event-Driven） |
| SQLite vs Notion 驗證 | Loop 2（Verification） |
| Claude Code 自動修錯 | Loop 1（Agent） |
| GBrain 記憶 + skill 進化 | Loop 4（Hill Climbing，雛形） |

---

## 標籤
`#AI架構` `#Agent` `#自動化` `#Loop` `#PromptEngineering` `#LangChain`

---
*存入日期：2026-06-10 | 更新：2026-06-11（六大元件）| 更新：2026-06-27（LangChain 四層架構）*
