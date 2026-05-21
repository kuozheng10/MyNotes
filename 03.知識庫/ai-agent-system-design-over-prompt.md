---
title: AI Agent：從 Prompt Engineering 走向 System Design
tags: [Agent, AI, 架構設計, observability, prompt, 工程]
date: 2026-04-09
category: AI工具
source: 社群分享（Facebook）
---

## 核心觀點

**大多數 Agent 問題不是 prompt 寫得不好，而是缺乏可觀測性、明確邊界與系統設計。**

---

## 三個關鍵能力

| 能力 | 說明 |
|------|------|
| 可觀測性（Observability） | 看懂 Agent 在哪裡出錯、為什麼出錯 |
| 邊界定義（Guardrails） | 先定義不能做什麼，再定義要做什麼 |
| 可持續優化（Iterability） | 有完整 Log 才能比對版本差異 |

---

## Prompt 常見誤區

- 把 Agent 品質問題壓縮成「prompt 寫得不夠好」
- 越寫越長，規則互相干擾，變成黑盒子
- **正確做法：Prompt 應該是「決策框架」，而不是「執行腳本」**

---

## Log 的正確姿勢

- Log 是基礎設施，不是附屬品
- 在探索期：**寧可記太多，不要記太少**
- 記什麼：收到什麼 / 回了什麼 / 用了哪個工具 / 工具回傳什麼 / 失敗 + 重試
- Vibe coding 時代：清理 log 成本幾乎為零，先留完整再說

---

## 邊界 > 流程

成熟設計順序：
1. 先定紅線（不能亂猜、不能硬補、高風險操作不能擅自前進）
2. 再定方法論與判斷框架
3. 最後才是理想執行流程

---

## 何時才真的需要 Agent（vs Workflow）

- Workflow：所有分支可預先枚舉 → 不需要 Agent
- Agent：不完整資訊 + 不確定情境 + 需要動態選路 → 才值得用 Agent

---

## 對派哥的啟示

- OpenClaw / Claude Code 的 Agent 行為難預測 → **先加 Log**，不是先改 prompt
- SOUL.md 的行為規則 = 邊界定義，是對的方向
- 一蘭老說「我去看看」就停 → 是缺乏完整執行框架，不是 prompt 問題

---

## 連結筆記
- [[ai-agent-modular-architecture]] — Agent 模組化設計
- [[hermes-agent-self-learning]] — Hermes 閉環學習
- [[bugfix-8steps-workflow]] — 系統化 debug 流程（類似觀點）
