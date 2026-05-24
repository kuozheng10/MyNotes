---
title: Claude Code 蓋量化交易系統——Playbook 方法論與六個核心教訓
tags: [Claude Code, Playbook, 量化交易, 架構設計, 並行, CLAUDE.md, 工作流]
date: 2026-05-24
category: 科技工具
---

## 這是什麼

一位工程師用一個週末和 Claude Code 協作，蓋出能跑 2 年台股資料、80 組參數回測、榨乾 M4 Max 16 核的量化交易系統。
記錄方法論、踩過的坑、以及四個具體協作場景。

---

## 核心方法：Playbook（操作手冊）

> 「Claude Code 用得好不好，差別不在 prompt 寫得多漂亮，而在有沒有一份 playbook」

**操作流程：**
先寫 markdown → 把專案拆成 N 個 prompt → 每個 prompt 後附驗收清單 → 一次只做一件事 → 驗收過了才給下一個

**三鐵則：**
1. 一次只給一個 prompt，等驗收過了再給下一個
2. 遇到錯誤先看訊息，不要直接讓 AI 重寫（會把問題藏起來）
3. 每完成一個 prompt 就 git commit，能回去才敢往前

---

## 架構設計三個刻意決定

| 決定 | 原因 |
|------|------|
| config 集中 | Claude 改完不會把參數散到各處 |
| data fetcher 與 strategy 解耦 | 換策略不用動資料層 |
| execution 獨立模組 | 滑價/漲跌停/手續費可單獨測試和替換 |

→ 加新策略、新 ablation 實驗時，舊程式碼一行都不用動

---

## 兩個錯誤

### 錯誤一：v2 沒寫 playbook

- v2 升級（parquet cache、prefetch、empty marker）直接邊改邊跟 Claude 來回，沒寫 playbook
- 現在要重現 v2 思路，只能翻 git log
- **教訓：沒寫 playbook 的升級 = 沒有外部記憶，下次開新對話 Claude 接不上**

### 錯誤二：README 其實是 CLAUDE.md

- README 寫的是安裝步驟、指令、FinMind quota 雷、cache 救援——全是寫給 AI 和未來的自己
- 這個專案根本沒給別人看過，用 README 是慣性
- **教訓：改名成 CLAUDE.md，每次新對話自動載入，省 5 分鐘重新解釋**

---

## 四個具體場景

### 場景 1：升級執行細節（v3）
關鍵指令：「不要把舊的 Execution Model 改爛」
→ 新版掛在旁邊，產出 ideal / realistic / pessimistic 三模式同跑，舊版留著當對照

### 場景 2：並行新增策略
指令：「不要動 smart_screener。新增 orb_strategy.py 和 hybrid_screener.py。最後做三方比較。」
→ 原版毫髮無傷，三套策略同框比較

### 場景 3：資料工程（FinMind 600次/小時限制）
Claude 主動建議：
- 寬範圍 parquet cache（一次抓10年）
- empty marker（沒資料也記下來，避免重打 API）
- quota 用盡自動退避 65 分鐘再續
→ 第一晚 4 小時建 cache，之後重跑只要 5 分鐘

### 場景 4：榨乾 16 核（v4）
需求：「14 核平行，保留 2 核給系統，每個策略/參數獨立 process，共用 cache，結果寫獨立檔」
→ ParallelRunner：80 組參數從 6 小時壓到 30 分鐘

> **把「能不能平行？」變成跟 Claude 對話的預設問題**

---

## .claude/ 目錄要不要做？

他有的：playbook md × 4、CLAUDE.md（叫 README）
他沒做：settings.json、commands/、hooks/、agents/

**原因：「重複性的稅金折扣」——同一個流程一週要跑 5 次以上才划算。**
實驗階段硬上自動化反而綁手腳，等策略驗證完、進入每日盤後自動跑才值得。

---

## 六個核心教訓

1. **Playbook > Prompt**：寫好操作手冊，AI 才不會跑歪
2. **驗收 > 速度**：每階段 commit + test，能回頭才敢往前
3. **並行擴充 > 重寫**：舊版留著當基準，新版掛旁邊跑 A/B
4. **工具配置跟流程成熟度走**：實驗階段別硬上自動化
5. **每次升級都要寫 playbook**：沒寫的那次就是最找不回脈絡的一段
6. **檔名反映真實用途**：README 其實是 CLAUDE.md

---

## 對派哥的關聯

- 你的 CLAUDE.md 已經在做這件事 ✓
- 你的每個 SDD 就是 playbook 的一種形式 ✓
- 缺的：改動前有沒有先寫 spec/playbook，還是直接改 code（類似 v2 的錯誤）

[[cisco-jeetu-patel-agentic-ai-digital-coworkers]] — 代理設計思維
