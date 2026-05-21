---
title: free-claude-code：Proxy 設計思路分析（我們為什麼不裝）
tags: ["Claude Code", "開源", "Proxy", "cost-engineering", "架構設計"]
date: 2026-04-24
category: AI工具
source: Telegram 派哥分享
---

## 這是什麼

本地 proxy 伺服器，把 Claude Code 的 API 請求轉發到免費模型（NVIDIA NIM、OpenRouter、LM Studio）。一週漲近兩萬星，GitHub Trending 前幾。

**本質**：用 Claude Code 的殼，裡面跑別人家的腦。

---

## 三個值得學的設計思路

### 1. Thinking Token 格式適配

免費模型把推理過程吐在 `<thinking>` 標籤裡，Claude Code 看不懂。Proxy 自動轉換成 Claude 原生的 thinking block。

**洞見：格式適配比模型能力更重要**。不只是選對模型，還要讓模型輸出能被下游系統吃掉。Thinking token 解析、tool call 轉換，這些髒活才是 proxy 真正的價值。

### 2. Heuristic Tool Parser

開源模型常把工具呼叫寫成純文字（「我要呼叫 search_files...」）而非結構化 JSON。啟發式解析器自動轉換，讓便宜模型也能「假裝」會用工具。

### 3. Subagent Control（在 Proxy 層做防護）

Claude Code 習慣開子代理狂跑，free-claude-code 直接攔截 Task 工具，強制 `run_in_background=False`。

**洞見：在 proxy/harness 層強制限制，比在 prompt 裡寫「請不要開太多子任務」可靠一百倍。** 不靠模型自覺，在請求層強制控制。

---

## 第三個洞見：把「免費」工程化

rate limiting + 指數退避 + 多 provider 降級。把免費當工程問題解，而不是靠運氣。

---

## 為什麼不裝（派哥的場景分析）

free-claude-code 解決的問題：想用 Claude Code 但不想付錢。

派哥的場景不同：
- 已有 provider-agnostic 的 coding agent（不綁 Claude Code CLI）
- 一蘭（Hermes）自己調度多個模型：glm-5.1 日常、deepseek 翻譯、qwen3 本地審查
- 月費控制在 1000 台幣左右，Ollama Cloud 夠用
- 多一層 proxy = 多一層延遲，沒必要

**「free-claude-code 解了一個真實的痛點，只是那個痛點不是我們的痛點。」**

---

## 質疑

- 前提假設：免費模型能力足夠替代 Claude Sonnet/Opus 做複雜任務？工具呼叫的啟發式解析有多穩定？
- 適用邊界：適合「想學 Claude Code 但付不起費用」的個人；不適合有自己 agent 架構的場景
- 潛在反例：proxy 增加故障點，免費 API rate limit 在密集使用時會卡住

---

## 對派哥的直接應用

**不裝，但偷三個設計模式**：

1. **格式適配層** — 未來如果要串接不同模型，記得在 harness 層做輸出格式轉換，不要讓下游系統直接吃原始輸出
2. **Proxy 層防護** — 子代理/任務暴走的防護不該只靠 prompt，要在 harness 層強制控制（CLAUDE.md 的 hooks 就是這個概念）
3. **免費工程化** — 多 provider 降級是 cost engineering 的標準手段，值得在一蘭的調度層參考

---

## 連結筆記

- [[harness-engineering]] — Proxy 層防護 = Feedback Sensor 的具體實作
- [[vibe-coding-rce-heredoc-three-rules]] — 在 harness 層控制，不靠模型自覺
- [[agent-prompt-token-cost]] — token cost engineering
- [[claude-token-saving-tips]] — 省 token 的其他方法
