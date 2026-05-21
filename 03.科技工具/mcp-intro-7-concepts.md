---
title: MCP 入門 7 個觀念：USB 比喻到 Single Source of Truth
tags: [MCP, 架構設計, AI工作流, 工具, 協議]
date: 2026-04-27
category: AI工具
---

## 來源

Anthropic 官方 Introduction to Model Context Protocol 課程筆記（觀念整理，非 code）

---

## 第一組：MCP 到底在做什麼

### 1. MCP 是 AI 工具世界的 USB

USB 出現前，每個設備自己一種接頭。MCP 在 AI 世界做一樣的事。

GitHub 官方出一個 MCP Server → Claude Code 安裝就接 → Codex 拿去也能用 → Cursor 也能用。
工具方寫一次，所有 AI 端直接接。

### 2. MCP Server 三種服務

| Primitive | 啟動方 | 例子 |
|-----------|--------|------|
| Tools | AI 自己決定 | 「幫我寄信」「改文件」 |
| Resources | 應用直接拉 | 打 @ 跳出文件清單 |
| Prompts | 使用者主動觸發 | 打 / 啟動「整理會議記錄」 |

記這句話：**tools serve the model, resources serve your app, and prompts serve your users.**

### 3. 6 個角色，角色是相對的

```
使用者 → 你的應用 → MCP Client → MCP Server → 外部 API
                          ↕
                          AI（Claude/ChatGPT）
```

關鍵：Server/Client 是相對概念。你的 chat app 對使用者是 Server，對 MCP 系統是 Client。
→ 看任何系統，別問「誰是 Server」，問「對誰來說是 Server」。

### 4. Server 和 Client 可以同時在你電腦上

- 本機版：stdio 通訊，資料不出電腦，快
- 遠端版：像 GitHub 雲端 MCP endpoint，直接連但資料送對方

涉及機密資料 → 選本機版或自架遠端版，不直接連第三方雲端。

---

## 第二組：跨界都通的設計觀念

### 5. 協議 vs 框架

MCP 是「協議」，只規定對話格式，不管實作語言（Python/TypeScript/Go 都行）。

規範原則：
- 對話格式（Interface）→ 管很細，差一個欄位接不起來
- 實作方式 → 完全放手

好的制度設計也是這樣：會議、文件、跨部門提案（格式）管細；個人解法、工具、策略（實作）放手。

### 6. 誰啟動，決定整個設計

設計任何工作流，第一個問的不是「要做什麼」，而是「**誰啟動**」。

同樣是「摘要文件」：
- AI 自己判斷需要 → Tool
- 使用者打 / 主動觸發 → Prompt

設計、UI、權限、錯誤處理完全不同。答錯這題，整個工作流走錯。

### 7. Single Source of Truth

真相只存在一個地方，其他全部自動跟著。

MCP SDK 做法：說明書從程式碼自動生成，程式改了說明書跟著改，不存在「忘了同步」這個 bug。

反例：公司共用 Excel，多人維護不同欄位 → 有人離職沒人更新 → 下游一路錯。

設計流程/資料時第一個要問：**「真相在哪一份？誰負責？其他全部該自動跟著動。」**

---

## 與派哥現有系統的對應

| MCP 觀念 | 派哥現有系統 |
|---------|-------------|
| USB 統一接口 | OpenClaw 統一接多個 AI |
| Tools/Resources/Prompts | Skill（How）/ Memory（What）/ handover（狀態） |
| Single Source of Truth | CLAUDE.md 是行為真相，skill 是 SOP 真相 |
| 誰啟動 | 一蘭負責收貼文/健檢，Claude Code 負責閉環/URL |

## ADR 更新

這篇強化了之前開的 [[adr-mcp-vs-direct-api]]：
Prompts 是使用者啟動、Tools 是 AI 啟動 → 對應的 UX 設計完全不同，不只是技術問題。
