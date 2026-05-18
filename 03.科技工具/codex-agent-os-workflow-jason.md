---
title: Codex Agent OS：從聊天工具到持續運作的個人作業系統
tags:
  - codex
  - agent
  - workflow
  - automation
  - memory
date: 2026-05-18
category: AI工具
---

## 核心轉變

OpenAI 工程師 Jason 公開 Codex 頂級工作流：coding agent 不只寫 code，而是進入知識工作（簡報、筆記、PDF、試算表、Slack/Gmail/Calendar 自動化）

關鍵不是模型能力，而是**工作有地方可以延續**——建立工作流。

---

## 五大核心能力

### Durable Threads（可持久的對話流）

為不同工作流保留長期 thread：Chief of Staff、開源專案、特定 SDK、社群監控。

- Thread 累積歷史、偏好、決策
- 不用每次從零開始
- → 派哥現有對應：Claude Code session + handover skill

### Memory as Files（記憶檔案化）

真正有用的記憶應被整理成**可檢查、可 diff、可版本控制的檔案**：

- Obsidian vault 或 GitHub repo 保存人物、專案、決策、待辦、open loops
- 記憶變得可管理，不是一團模糊的上下文
- → 派哥現有對應：MyNotes + ~/.claude/memory/ 系統

### Tool Use + Browser/Computer Use

- Browser Use：檢查網頁、操作系統後台、review UI
- Computer Use：點擊、輸入、切換畫面，處理跨工具流程
- 串接 Slack、Gmail、Calendar、Chrome

### Heartbeats（定時處理任務）

每 30 分鐘檢查 Slack/Gmail 有沒有需要回覆的訊息、定期看 PR comment、Google Docs comment、根據回饋重新產出版本。

工作單位不再是 prompt→答案，而是**持續運作的小型 loop**。

退款案例：Agent 每幾分鐘檢查客服是否進線，一旦回覆立刻切成高頻率處理。AI 不是比人更會爭取退款，而是幫你守住瑣碎、等待、重複檢查的流程。

→ 派哥現有對應：launchd cron + cc_processor 排程

### Artifact Review（產出物檢視）

Markdown、CSV、PDF、slides、HTML、Streamlit 在同一介面被產生、檢查、註解、修改。

AI 進入真正的工作現場，不只輸出文字。

---

## Agent OS 七要素

| 要素 | 說明 |
|------|------|
| Memory | 保存專案狀態、人物偏好、決策紀錄、待辦 |
| Tool Use | 呼叫外部工具完成任務（查資料、改檔案、開 PR）|
| Browser Use | 操作網頁、review UI、測試互動流程 |
| Computer Use | GUI 操作，處理跨工具複雜流程 |
| Artifact Surface | 產出物可被直接檢視、註解、修改 |
| Automation Loop | 定期檢查訊息、追蹤回饋、更新進度 |
| Goal | 明確可驗證的成功條件（不是「重構專案」，而是「通過測試、保持 API 行為一致、產出可 review PR」）|

**Goal 的設計最關鍵**：讓 Agent 有判斷任務是否完成的標準，不只是照著計畫做。

---

## 對派哥的參考點

派哥現有系統已涵蓋部分要素：

| Agent OS 要素 | 派哥現有對應 |
|--------------|-------------|
| Memory | MyNotes + ~/.claude/memory/ |
| Tool Use | Claude Code tools + MCP |
| Automation Loop | launchd + cc_processor + 晨報 |
| Artifact Surface | Telegram 回報 + Google Drive |
| Durable Threads | handover skill + session log |

缺口：
- Browser/Computer Use：目前主要靠 Playwright 測試，不是常態工作流
- Heartbeat：目前排程固定時間，沒有「事件觸發→高頻輪詢」的模式
- Artifact Review：產出物散落各對話，缺集中 review 介面

→ 參見 [[claude-routines-automation]]、[[hermes-agent-self-learning]]、[[autoskills-skill-infrastructure]]
