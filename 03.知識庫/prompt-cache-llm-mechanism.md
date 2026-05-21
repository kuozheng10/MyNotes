---
title: Prompt Cache — LLM 推論快取機制與 Claude Code 實作
tags: [prompt-cache, token, LLM, claude-code, 效能, 省錢, 架構]
date: 2026-04-09
category: 03.科技工具
source: 社群分享（IT 技術文）
---

## 這是什麼

Prompt Cache 讓模型把前面看過、這一輪不變的內容存成可重用的中間結果（KV cache），下次推論時直接從快取接著算，不用從頭重算整段 system prompt。

**本質：推論層的快取機制，不是聊天記憶。**

---

## 為什麼重要

沒有快取：10 輪對話燒 255K tokens（O(N²) 增長）
有快取：60K 等價 tokens，線性增長 → 省 76%

---

## Claude Code 的快取結構

```
Block 3（靜態 CC 指令）  → global 快取，全球用戶共享
── DYNAMIC_BOUNDARY ──
Block 4（CLAUDE.md）     → org 快取
tools                   → session 內凍結
messages                → 最後一條加 cache_control 標記
```

- **TTL**：免費用戶 5 分鐘，Pro/Max 1 小時
- **快取斷裂偵測**：cache_read_input_tokens 下降 >5% 就告警

---

## 保護快取 vs 破壞快取

| 保護快取 ✅ | 破壞快取 ❌ |
|-----------|-----------|
| 連續對話，一個 session 做到底 | 開新 session → 冷啟動，~20K tokens 全價重算 |
| CLAUDE.md 工作中不動 | 改 CLAUDE.md → Block 4 以後全失效 |
| MCP 工具 session 前配好 | 加減 MCP → 工具 schema 變 = 快取斷裂 |
| 同一模型用到底 | 切換模型 → KV 不互通，完全失效 |
| 對話 >100K 再用 /compact | /compact → 訊息歷史重寫 = 斷裂 |
| 不超過 Pro/Max 1h TTL | 發呆超 TTL → 快取消失 |

---

## Sub-agent 的快取問題

Sub-agent 幾乎**不能復用**主線程快取：
- 工具集不同
- 訊息歷史獨立
- 可能用不同模型

→ 每個 agent 都是迷你冷啟動，CLAUDE.md 寫「多用 agent 並行」前要考慮這個成本

---

## 本地實驗數據（Gemma 4B, Ollama）

| 狀態 | 處理時間 |
|------|---------|
| 首次（無快取） | 31,000ms |
| 有快取 | 250ms |

**100 倍加速差距**

---

## OpenClaw 與 Prompt Cache

Boris Cherny（CC 作者）暗示封掉 OpenClaw 的原因之一是 Prompt Cache 做得差，甚至提交 Claude API PR 給 OpenClaw 改善。→ 快取品質影響 token 用量和效能，是大事。

---

## 對派哥的啟示

- **保持 session 連續** 是省 token 最簡單的方法
- **CLAUDE.md 工作中別亂改**，會破壞 Block 4 以後的快取
- **用量突然暴增** → 先查是否快取失效，不是用量習慣改變
- **一蘭（OpenClaw）的快取效率** 目前未知，是潛在成本來源

---

## 連結筆記
- [[agent-prompt-token-cost]] — 中文 prompt token 爆量問題
- [[claude-token-saving-tips]] — Claude Code 省 token 10 招
- [[hermes-agent-self-learning]] — Agent 記憶架構（快取與記憶的關係）
