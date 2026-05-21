---
title: "88% AI Agent 失敗的五個陷阱 — Pipeline 思維才是關鍵"
tags: [claude-code, agent, pipeline, token, openclaw, workflow, 思維, 必讀]
date: 2026-05-10
category: 03.科技工具
source: Telegram 派哥分享（Gucci / AI效率革命聯盟）
---

## 核心數字

- 88% 企業 AI Agent 進不了 production（Stanford AI Index 2026）
- 剩下 11% 平均 ROI = 171%
- Agentic coding session 有 60–80% token 是浪費（Stanford Digital Economy Lab）

## 五個陷阱

### 陷阱一：裝完了，但什麼都不能做
工具預設值永遠是「最保守」不是「最實用」。
OpenClaw 預設工具鎖死 → 要改 `"tools": { "profile": "full" }`。
**教訓**：每個新工具裝完，第一件事看 default 設定，不是跑 demo。

### 陷阱二：80% 帳單是在付「重讀」的錢
實測比例：139M 輸入 token vs 935K 輸出 token = 148:1。
AI 大部分時間在「複習」你之前說的，不是在「思考」。

解法：
- 把該記的放記憶系統，不是每次塞進 prompt
- 開 prompt caching（Anthropic cache 省 90% 重複費用）
- 大段內容換語意搜尋，不要全量灌入

### 陷阱三：便宜模型省 API 費，花了更多時間
全掛 Haiku → 回覆 miss 重點 → 手動修 → 比自己寫還久。

正確分層：
- **跟人互動**（對話/創作/模糊指令）→ Sonnet / Opus
- **資料提取/固定流程**（爬蟲/格式轉換）→ Haiku / GPT-mini

### 陷阱四：沒有下游消費者的 Agent = 黑洞
案例：刪掉一個「每天產報告但沒人看的 Agent」→ token 下降 44%、速度提升 62%。
**問自己三個問題**：
1. 我生成什麼輸出？
2. 誰在接收？
3. 我永遠不碰什麼？

設計 Agent 前，先答得出第 2 題。答不出就不要建。

### 陷阱五：過度設計的紙上架構師
不要先畫架構圖。架構是「長出來的」，不是「設計出來的」。

**正確時程**：
- 第一天：1 個 Agent + 1 個任務 + 接 Telegram，直接 production
- 第一週：修問題（工具/規則/效能）
- 第二週：看 token 帳單，優化 prompt
- 第三週：加第二個 Agent，理解下游消費者
- 第四週：架構自然成形

## 核心洞見：Pipeline > Tools

> 工具會過時，pipeline 會升級。工具會被取代，pipeline 會吸收新工具。

真正的差距不是工具，是：
- 把「一次性的成功」變成「可重複交付的流程」的能力
- 系統思維 > 追新工具的衝動

**作者的 Continuous Delivery System 長相**：
靈感 → 研究層（Agent 整理 brief）→ 創作層（腳本/簡報生成）→ 策略層（市場痛點掃描）→ 監控層（X/標籤監控）→ Deploy → Ship

## 對派哥的對照

| 陷阱 | 派哥現況 |
|------|---------|
| 工具預設值 | cc_processor 每次新銀行都要確認設定 ✅ |
| 重讀 token | `/compact` + prompt cache 已在用 ✅ |
| 模型分層 | Sonnet 主力 / Haiku 未用 → 可優化 |
| 無人消費 | 幾個 cron job 要確認有沒有人在看 ⚠️ |
| 過度設計 | cc_processor 就是先跑後長 ✅ |

**最值得檢查的**：有沒有「自我感動工作流」在每天跑但沒被消費？

## 相關筆記

- [[claude-token-saving-tips]] — Token 省法
- [[agent-prompt-token-cost]] — Token 成本分析
- [[claude-code-token-saving-strategies]] — Claude Code 省 token
- [[openclaw-hermes-collaboration]] — Pipeline 架構
