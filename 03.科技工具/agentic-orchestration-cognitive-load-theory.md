---
title: Agentic Orchestration 框架：用 Cognitive Load Theory 設計多 Agent 系統
tags: ["Agent", "架構設計", "Claude Code", "工作流程", "AI"]
date: 2026-04-22
category: 系統架構
source: 派哥整理
---

## 這是什麼

工程師角色從 creators 轉 curators：不寫 code，改成拆任務、看產出、做決策。這篇從 Cognitive Load Theory（CLT）出發，建立一套多 Agent 系統設計與協調框架。

## Agent 分類：兩種軸

### 學術軸（Russell & Norvig）

simple reflex → model-based → goal-based → utility-based → learning agent

### 實作軸（介入程度）

| 類型 | 說明 | 範例 |
|------|------|------|
| Fire-and-forget | 給 spec 跑到底 | lint fix、unit test、文件生成 |
| Context-dependent | 需讀其他 agent 產出 | API integration、前後端串接 |
| Decision-requiring | 跑到一半需人做架構決策 | schema design、auth flow |

這個分類決定了哪些能平行跑、哪些要排序、哪些需要 standby。

## Cognitive Load Theory（CLT）

John Sweller 1988。人的 working memory 同時只能處理 2-4 chunks。

| 類型 | 定義 | Agent 情境 |
|------|------|------------|
| Intrinsic load | 任務本身複雜度（element interactivity） | 解聯立方程式 |
| Extraneous load | 不必要的雜訊 | 追蹤 4 個 agent 各自寫了哪行 code |
| Germane load | 建立 mental model 的負擔 | 判斷 API boundary 劃得對不對 |

**核心洞見**：同時管多個 agent 時——
- 追蹤實作細節 = extraneous load（該消除）
- 做架構判斷 = germane load（該保留）

切換成本的關鍵不是切換頻率，是**切換的層級**：切換 review 和 decision，不切換 implementation context，認知成本就低。

**Agent 間資訊設計原則**：Agent B 只需要讀 Agent A 的 output artifact（API contract、test result、schema），不需要讀推理過程。過多的 agent 間 memory sharing = 在系統裡製造 extraneous load。

## Element Interactivity：決定能不能拆

同時決定三件事：
1. 任務的 intrinsic load 有多重
2. 能不能分解給多個 agent
3. 分解後 fragmentation 代價有多高

**BPM 2023 研究結論：abstraction over fragmentation**
- 隱藏不相關資訊有利於理解
- 把相關資訊分散到多個片段反而提高認知負擔

一個 user CRUD module 拆成 5 個 agent（migration、model、controller、route、validation）→ field 名稱不一致、validation 不知道 controller 期望的 input format → debug 整合問題的時間更長。

1 個 agent 負責完整 bounded context > 5 個 agent 各負責一層。

**判斷 decomposition 的兩層**：
- Syntactic dependency：可自動化（static analysis，看 file overlap）
- Semantic dependency：需人判斷（API contract 設計影響 frontend data flow）

後者是開發者不可替代的價值。

## Spec 精度：三層模型

| 層次 | 內容 | 誰寫 |
|------|------|------|
| 產品意圖層 | 「使用者應能在付款失敗時自動重試」 | PM/開發者 |
| 架構邊界層 | 「重試邏輯在 payment gateway client wrapper，exponential backoff，最多 3 次，超過發 event」 | 開發者 |
| 實作細節層 | retry library 選擇、error code mapping、timeout 數值 | Agent |

Spec 寫到架構邊界層就夠，agent 處理實作細節。只寫到產品意圖層 → 5 個 agent 產出 5 種不同策略。

**Addy Osmani 觀察**：模糊需求在平行執行時被乘法放大，精確 spec 才能在 fleet 中乘出精確實作。

## Spec 作為 Harness 的 Task Schema

三層可以 encode 進 harness：

```
task schema:
  product_intent: str
  architecture_boundary: str   # boundary condition、error handling strategy、interface contract
  implementation_detail: str   # agent 填
```

Harness 收到 task 時，檢查 spec 層級是否足夠。不夠就 flag 出來讓人補完，不讓 agent 自己猜。

**Strong engineers get more leverage from agents** — 不是因為 prompt 更好，是因為他們本來就有更清晰的 architectural thinking。Spec 不再是 prompt，是 product thinking 的外顯化。

## 認知外部化：四種 Agent Memory

Clark & Chalmers 1998「Extended Mind Thesis」：認知過程可延伸到環境工具和 artifacts。筆記本、ADR、AGENT.md 都是 extended mind 的實例。

| Memory 類型 | 外部化形式 | 作用 |
|------------|-----------|------|
| Semantic memory | AGENT.md | domain knowledge，agent 需要知道什麼背景 |
| Episodic memory | session log / git history | what happened，上次做了什麼 |
| Procedural memory | workflow scripts / harness config | how to do，步驟和流程 |
| Strategic memory | MEMORY.md | what worked, why, what next |

**Filesystem = agent 間的 shared memory**：Agent A 寫 output 到 file，Agent B 讀 file——IPC 的 pipe 模式。Context window = RAM，filesystem = disk，每次 LLM call 都是 stateless 的。

**Strategic Memory 特別重要**：記錄的是 distilled causality（萃取因果），不只是 episodic（記錄事件）。例：「上次 payment module 用 fixed interval retry，在 high traffic 造成 thundering herd → 改用 exponential backoff + jitter」。讓每個 session 站在前一個 session 的肩膀上。

## Feedback Loop：用 Agent 訓練設計 Agent 的能力

Chris Argyris 1977 的兩種學習：
- **Single-loop**：修正行動達成目標（「spec 寫太模糊，下次寫清楚」）
- **Double-loop**：質疑目標本身（「我對 agent 的分工方式根本設計錯了」）

三條 feedback 路徑：
- 協調 agent 時練出的 decomposition sense → 就是 harness 該內建的 task routing logic
- 用 CLT 判斷認知負擔的框架 → 就是 agent 間 memory sharing boundary 的設計依據
- 外部化認知的習慣 → 就是 Strategic Memory 的 schema 和使用場景

用 agent 的過程訓練我們設計 agent 的能力——這個 feedback loop 才是真正的 flywheel。

## 質疑

- 前提假設：CLT 的 working memory 限制（2-4 chunks）是針對人類認知，AI agent 沒有相同限制；把 CLT 框架套到 agent 設計是比喻，不是等式
- 適用邊界：「1 agent 負責完整 bounded context」在小型專案成立，但 bounded context 的邊界本身就需要 domain expertise 定義，beginner 很難判斷
- 潛在反例：fire-and-forget 看起來不佔 working memory，但如果 agent 產出有問題被合進主線，review 成本可能比自己寫還高

## 對標

- **軟體系統設計的同步問題**：不把兩個 write-heavy process 同時打到 shared resource——agent 的 decision-requiring 任務就是需要「加鎖」的臨界區
- **外科手術團隊分工**：主刀只做決定，不拿工具遞紗布；germane load 給主刀，extraneous load 交給團隊——agent 協調的理想形態

## 對派哥的啟示

你現在的工作模式已經是這篇在說的 curator 模式。具體對應：

- **分類任務**：sales_report / cc_processor 的 auto run = fire-and-forget；OAuth token 更新 = decision-requiring（你需要在場）
- **Spec 精度**：你給 Codex 任務時寫到架構邊界層（指定哪個函數、哪個邏輯），不只說「修好那個 bug」——這就是為什麼 Codex 成功率高
- **Extraneous load 消除**：你現在透過 Telegram → Claude Code 傳達決策，不看每行 code——已在實踐這個框架

下一步可做：把 Syntactic dependency 自動化——在 MyClaude 的任務 dispatch 前，加一步 file overlap 分析，自動標出哪些任務可平行。

## 連結筆記

- [[harness-engineering]]
- [[ai-agent-system-design-over-prompt]]
- [[multi-agent-system-architecture-optimization]]
- [[boris-parallel-claude-workflow]]
- [[claude-code-subagent-environment]]
- [[claude-md-optimization]]
