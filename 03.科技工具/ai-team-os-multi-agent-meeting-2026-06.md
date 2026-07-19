---
tags: [ai, agent, multi-agent, meeting, brainstorming, solo-founder, six-thinking-hats, open-source]
source: 社群分享 / AI Team OS 實測心得（Hermes）
saved: 2026-06-30
---

# AI Team OS — 讓一群 AI 替你開會，做腦力激盪

> 一句話：把 AI Agent 變成一間公司，不同角色各自上網查資料、互相辯論，最後主席出面做結論。一人公司最大的痛是沒人討論，現在你當董事長，AI 幫你開會。

---

## 什麼是 AI Team OS？

GitHub 上的開源專案，概念：

```
AI Agent × 多角色 × 真實搜尋 → 模擬企業會議決策流程
```

- 原本設計給 Claude，但可以改寫成適合其他 LLM 的版本
- 不需要 MCP Server，不需要 FastAPI 後端，**全部用內建功能搞定**
- 最大亮點：每個 Agent 都能透過 **AnySearch CLI 真的上網搜尋**，不只靠訓練知識

---

## 三種會議格式

### 1. 自由辯論
**題目**：「一人公司該先做 AI 產品還是企業服務？」

- 正反方各提出五個論點
- 裁判最後給出結論
- **結論**：以企業服務為現金引擎，產品開發為戰略北極星

### 2. 六頂思考帽
六個角色同時分析同一個行銷策略問題：

| 帽子顏色 | 角色職責 |
|---------|---------|
| 白帽 | 找數據、事實 |
| 黑帽 | 找風險、問題 |
| 綠帽 | 想創意、新點子 |
| 紅帽 | 情感直覺 |
| 黃帽 | 正面樂觀分析 |
| 藍帽 | 流程管理、總結 |

→ 五分鐘後收到完整多角度報告

### 3. 深度版（有網路搜尋）
- 每個角色都上網搜尋最新趨勢
- 產出：Top 5 商品推薦 + **完整 12 週開發計畫**

---

## 實測數字

| 項目 | 數字 |
|-----|------|
| 開會場數 | 3 場 |
| 派出 Agent 數 | 16 個 |
| 每個 Agent 搜尋關鍵字組數 | 3~5 組 |
| 產出內容量 | 數萬字報告 |
| Token 消耗 | **僅 3%（MiMo PRO 月費包）** |

> Token 消耗比預期低得多，CP 值極高。

---

## 適合對象：一人公司

**最大的痛**：沒人可以討論、沒有多元觀點

**AI Team OS 的解法**：
- 你當董事長
- AI 幫你開會，從多角度分析問題
- 你只負責聽報告做最終決定

---

## 改造重點（Hermes 的做法）

原版是給 Claude 的，改寫時的關鍵改動：
1. 移除 MCP Server 依賴
2. 移除 FastAPI 後端
3. 加入 AnySearch CLI → 讓每個 Agent 能真的上網查即時資料

---

## 相關連結

- AI Team OS 開源專案 → GitHub（搜尋 AI Team OS）
- 多 Agent 協作架構 → [[loop-engineering-agentic-ai]]（子代理程式：分離創造者與檢查者）
- 企業 AI 信任問題 → [[enterprise-ai-market-signal-2026-06]]
- 一人公司 vs 大公司 AI 策略 → [[enterprise-ai-market-signal-2026-06]]
- Anthropic 官方一人公司 Playbook（四階段 + 護城河在哪）→ [[anthropic-founder-playbook-solo-startup-2026-07]]
