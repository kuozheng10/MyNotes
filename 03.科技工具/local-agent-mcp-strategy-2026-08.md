# 地端 Agent + MCP 策略：自建知識庫，開放接口給雲端大模型

> 來源：[Facebook - 陳盟升](https://www.facebook.com/share/p/1McmDGgVz9/?mibextid=wwXIfr)
> 儲存日期：2026-08-04
> 標籤：#ai-agent #mcp #local-agent #architecture

---

## 核心觀點

地端（本機）Agent 不用擔心「戰力輸給雲端大模型」，因為策略不是硬碰硬比拼模型能力，而是**分工**：透過開放 Model Context Protocol (MCP)，把非機密資料共享給 Codex、Claude 等雲端大型語言模型呼叫。

## 分層架構

| 層級 | 負責內容 |
|------|----------|
| 地端處理 | 機密資料、企業內部知識、專有工作流程 |
| 雲端調用 | Codex、Claude、ChatGPT 等支援 MCP 的模型 |

## 核心論述（原文引用）

> 「要隨意修改 Codex、Claude 很麻煩，新功能就打亂自己的工作節奏，不如專心開發自己的 Agent，專心累積自己的知識庫」

也就是：與其去改雲端供應商的 Agent（版本一直變動、跟不上節奏），不如專心建自己的地端 Agent + 知識庫，再用 MCP 這個標準接口讓外部大模型（Codex/Claude/ChatGPT，支援多模型連接）進來調用，兩邊各司其職。

## 網友回應

Junjun Zhang 表示認同：自建 Agent 搭配 MCP，能同時兼顧「模型能力」（借雲端大模型的推理優勢）與「數據自主性」（機密資料留在地端不外流）。

---

## 相關筆記

- [[ai-framework-vs-harness-2026-07]] — 同樣討論「自建編排邏輯 vs 用供應商 Harness」的分野，可對照參考：陳盟升這篇更聚焦在「資料留地端、能力接雲端」的分工策略，而非 Framework/Harness 的技術站位選擇
- [[gpt-claude-gemini-20usd-comparison-2026-08]] — 同作者：GPT/Claude/Gemini三家$20方案使用比較
