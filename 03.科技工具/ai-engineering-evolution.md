# AI 使用技巧的演進：從 Prompt Engineering 到 Loop Engineering

> 來源：圖片整理（2026-06-14）
> 核心演進：輸出 → 資訊 → 能力 → 環境 → 流程 → 收斂

---

## 六個演進階段

### 1. Prompt Engineering / 提示工程
從「會問問題」到「設計可重複使用的指令」

- 學會寫清楚的 prompt
- 設計 template、few-shot 範例
- 讓 AI 輸出品質穩定可預期

### 2. Context Engineering / 上下文工程
管理模型決策時需要看到的資訊

- 控制 context window 的內容
- RAG、memory、summaries
- 決定 AI 「看到什麼」來做決策

### 3. Tool Engineering / 工具工程
讓模型安全穩定地使用外部工具與 API

- 定義 tool schema（function calling）
- 錯誤處理、retry、timeout
- 工具的安全邊界與授權

### 4. Harness Engineering / 執行環境工程
管理任務狀態、工具存取、權限、驗證與觀測

- Task queue、state machine
- 權限控管（哪些 tool 可被呼叫）
- 觀測：logging、tracing、alerting

### 5. Workflow Engineering / 工作流程工程
把多步驟、多代理人流程組成可維護架構

- 拆解 agent 職責（spec → plan → build → review）
- 定義 handoff 條件與資料格式
- 讓複雜流程可以被版本控管與測試

### 6. Loop Engineering / 迴圈工程
讓系統能觀察、行動、評估、反思、重試並收斂

- Observe → Act → Evaluate → Reflect → Retry
- 自我修正機制
- 收斂條件（何時停止）

---

## 核心演進方向

```
輸出品質 → 資訊品質 → 工具能力 → 執行環境 → 多步驟流程 → 自主收斂
```

每一層都是對上一層的擴展，不是替代。成熟的 AI 工程師需要同時具備全部六層能力。

---

## 關聯筆記

- [[loop-engineering-agentic-ai]] — Loop engineering 實作模式
- [[agentic-sop-to-work]] — Agent SOP 到工作流程
- [[ai-coding-team-cld]] — AI coding team 架構
