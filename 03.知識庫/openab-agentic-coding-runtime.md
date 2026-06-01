# OpenAB：Agentic Coding 的 Runtime 解法

> 來源：Facebook 貼文（#OpenAB #AgenticCoding）
> 整理日期：2026-06-01

---

## 核心主張

> OpenAB 解的不是單純的 chat interface 問題，而是 Agentic Engineering 的 runtime 問題。

---

## 問題的起點：自己做 Adapter 的限制

早期做法：自己寫 adapter，把 Telegram / Discord 訊息接到 coding agent CLI 的 headless / one-shot prompt 模式（如 `-p` 用法）。

**問題**：headless 模式本質是一次性 CLI 呼叫，要延續對話需自己處理：
- Session resume
- Context 拼接（哪些訊息塞回去）
- 看起來像連續對話，底層是獨立呼叫

**真正麻煩的是這幾項：**
| 問題 | 說明 |
|------|------|
| Session lifecycle | 怎麼延續？ |
| Context 邊界 | 交給誰處理？ |
| Streaming output | 怎麼呈現？ |
| Tool call / permission | 怎麼表達？ |
| 中斷 / resume / 錯誤 | 怎麼接回協作介面？ |
| 跨 Coding CLI | 能不能用同一套接？ |

---

## ACP（Agent Client Protocol）

ACP 不是單純多包一層 CLI，而是把 **Agent Lifecycle 變成 Protocol 的一部分**。

- Session、streaming、tool call、permission、cancel / resume → 變成共通 lifecycle 介面
- Context 本身由各 coding agent runtime 自己管理（ACP 不介入）

---

## 為什麼不用各家 SDK 自建平台

- 手上有多個訂閱平台（Claude、Codex、Gemini 等）
- 每家 SDK 功能不同、呼叫時機不同、permission 模型不同
- 整合代價高：不斷針對不同平台做特殊處理

**結論**：不重做每個 Coding Agent 的能力，只提供更好的 Runtime 讓這些 Coding Agent 在自己的環境工作。

---

## OpenAB 是什麼

**Discord / Slack / Custom Gateway → ACP-compatible coding CLI → 可管理的 runtime**

Runtime 支援：sandbox、container、Kubernetes、PVC、session pool

**提供的 Primitive：**
- Bot-to-bot messaging
- Thread session
- Allowlist
- Turn cap
- Reply directive

> OpenAB 不負責決定誰接手任務，也不設計整個流程。它提供的是 primitive，流程設計是使用者的空間。

---

## Workflow 設計哲學：Main Agent Handoff vs. Orchestrator

### Orchestrator 模式（常見）
一個主控 agent 分派多個 subagent，各自處理任務，最後整合。

**限制**：Subagent 不一定完整繼承 MCP / Skill / memory / local config 等 runtime 能力。

### Main Agent Handoff 模式（作者偏好）
每個 workflow 完成後 **handoff 給下一個 workflow**，每一步都走 **main agent**。

- 過去：需要自己寫 workflow 串接腳本
- 用 OpenAB：透過 bot-to-bot 協作即可，指派不同 bot 各自跑 workflow

---

## STOP CODING. START ENGINEERING.

> Stop Coding 不是不要寫程式，而是從「我親手寫每一行 code」轉成「我設計 context、tools、stdout、tests、architecture、plans，讓 Agent 能自主完成工作」。

操作方式：
1. 設定好 Agent 的 runtime
2. 提供 input、定義需要的 output
3. 用工程方式驗證結果
4. 中間不需要一步一步指揮

---

## 相關筆記

- [[ai-era-dont-preimplement]] — 做太快，官方就會推出（DIY adapter → ACP / OpenAB）
- [[claude-code-dynamic-workflows-multi-agent]] — Claude Code Dynamic Workflows（官方 multi-agent 方案）
- [[senior-dev-ai-era-harness-complexity]] — AI 時代的工程師角色
