---
title: 跨 Model 工作流三條路徑：從 claude -p 到 Gateway 模式
tags: [AI, Claude Code, Codex, 工作流程, 自動化, cross-model]
date: 2026-05-20
category: AI工具
source: telegram/手打
---

## 最小可行版：claude -p non-interactive

```bash
claude -p "幫我驗證這份研究報告"
codex exec "用 second opinion 角度挑戰這個報告"
```

兩邊都是 non-interactive mode，stdout 拿結果，互為 first-class。不是正式 A2A Protocol，但這就是 agent-to-agent 的底層原理。

---

## 為什麼要跨 Model？

三家旗艦 model 各有盲點：

| Model | 擅長 |
|-------|------|
| ChatGPT | 對話語氣、社群貼文、社群研究 |
| Claude | 系統架構、寫程式、framework 設計 |
| Gemini | ？（待確認） |

用法：
- 寫貼文 → ChatGPT 主寫，Claude 找邏輯漏洞
- 設計架構 → Claude 主寫，ChatGPT 整理 narrative
- 做研究 → 兩個丟同樣素材，看切角差異

跨 model 不是哪個不好，是每個都有看不到的盲點。

---

## ⚠️ 6/15 計費重大變動

Anthropic 公告：6/15 起 `claude -p` 與整個 Agent SDK 從 subscription 用量池搬出，改成獨立 monthly credit，按 API list price 計費。

**兩種計費模型的本質差異：**

| 模式 | 認證 | 計費 |
|------|------|------|
| `claude`（互動） | OAuth + subscription quota | 訂閱制 |
| `claude -p`（自動化） | 6/15 後改吃 Agent SDK monthly credit | 按 token 計費 |

Interactive = 人在迴圈、自然限速。Autonomous = 機器跑、可一晚燒掉幾百萬 token，需要硬性 cost ceiling。

---

## 三條路徑

### 路徑 1：Web 介面手動複製貼上（最低門檻）

開兩個 tab，A 的回答貼給 B：

> 「請以獨立 reviewer 角度找出這份回答最弱的論點、漏掉的角度、你會怎麼重排重點順序」

優點：所有算力都在 OpenAI / Anthropic 伺服器，不用付硬體錢。
適合：寫作、研究、決策、論點驗證。

### 路徑 2：Coding Agent 互相呼叫

2026 主流做法：

- **Plugin**：`codex-plugin-cc` 提供 `/codex:review`、`/codex:rescue`、`/codex:adversarial-review`
- **Skill**：`~/.claude/skills/` 放 codex skill，Claude 看到適合任務自動丟給 Codex

適合：coding、自動化、有明確 task boundary 的工作。

### 路徑 3：統一 API 路由層（Gateway 模式）

| 工具 | 性質 | 特點 |
|------|------|------|
| OpenRouter | SaaS | 一個 key 通數百個 model，OpenAI-compatible，內建 auto-routing |
| LiteLLM | Open source 自建 | 100+ providers，cost tracking、virtual key、rate limit 自己掌控 |

選擇邏輯：個人用 OpenRouter，公司或重度使用上 LiteLLM。

IDE-driven 版本：RooCode / Cline / Cursor = 把 gateway 包進 IDE，context 自動帶入。

---

## OpenClaw 的 cross-model 實作

OpenClaw 規劃任務、分解步驟，實作丟 Claude Code；
Claude Code 用 web search 當 harness，驗證兩邊的「左右互搏」結果；
兩個 model 都同意 + web 有獨立來源 = 才算數。

---

## OpenClaw 封鎖歷史

- 1 月 9 日：Anthropic server-side block + 2 月更新 ToS，OAuth 路被堵
- 社群繞道：改讓 OpenClaw 直接呼叫本機 `claude -p`
- 6/15：`claude -p` 從 subscription 搬走，繞道路的經濟模型要重算

意圖明確：interactive 跟 autonomous 分開算錢，subscription 不補貼自動化。

---

## 學術分類：三種溝通模式

出處：2025《Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems》

| 模式 | 定義 | 對應路徑 |
|------|------|---------|
| Message Passing | Agent A 直接送訊息給 Agent B | 路徑 2（CLI / plugin / skill） |
| Blackboard / Indirect | 共享「黑板」，沒有明確 sender/receiver | 路徑 1（你是搬運者，model 不知道對方存在） |
| Shared Memory | 寫入 / 讀取同一個共享記憶體層 | Mem0、Letta、Zep、Obsidian、Notion |

路徑 3（OpenRouter / LiteLLM）是通訊路由層，本身不儲存狀態，不算 Shared Memory。目前主流 cross-model 停留在前兩種，Shared Memory 越來越重要。

---

## 終極思維轉換：Stateless Execution

舊思維：context 是一封信，model 是收信人，換 model = 把信轉寄
新思維：context 是雲端硬碟，model 是打開檔案的軟體，換 model = 換開檔案的軟體

| | 舊思維 | 新思維 |
|-|--------|--------|
| 載體 | Chat session | Memory store + protocol |
| 換 model | 要帶 context 過去 | Model 是可被換掉的執行單元 |
| 工具 | 找「同 session 切 model」 | 找 Mem0、Letta、Zep、A2A |

管的不再是 model，而是 context。這是 cross-model 從「工具技巧」升級為「系統架構」的關鍵。

---

## 對不同使用者的建議

| 類型 | 路徑 |
|------|------|
| 寫作/研究型 | 路徑 1（Web 複貼）+ Obsidian / Notion 整理 |
| 工程師 | 路徑 2（CLI 互呼）+ 精算 token 預算 |
| 重度自動化 production | 路徑 3（OpenRouter 或 LiteLLM） |

---

## 連結筆記

- [[claude-codex-ssh-remote-mode]] — Codex SSH 遠端模式
- [[codex-plugin-cc]] — Codex plugin for Claude Code
- [[codex-hooks-event-trigger]] — Codex hooks 事件觸發
- [[three-provider-ai-routing-strategy]] — 三家 AI 路由策略
- [[claude-code-setup-plugin-official]] — Claude Code plugin 設定
