---
title: "Addy Osmani：Harness Engineering 深度展開"
tags: [harness, agent, claude-code, architecture, context-engineering, hooks, sandbox, multi-agent, 工作流程]
date: 2026-05-14
category: 03.科技工具
source: Telegram 派哥分享（Addy Osmani 文章）
---

## 核心定義

> Agent = Model + Harness
> If you're not the model, you're the harness.

Harness = 所有不是模型本體的程式碼、設定和執行邏輯：
- System prompt / CLAUDE.md / AGENTS.md / skill files
- Tools / skills / MCP servers（及其工具描述）
- 執行環境（filesystem、sandbox、headless browser）
- Orchestration logic（subagent、handoff、model routing）
- Hooks / middleware（lint check、context compaction）
- Observability（logs、traces、cost、latency）

## Harness 元件逐一拆解

### Filesystem + Git
模型只能處理 context window 裡的東西。Filesystem 讓 agent 有地方讀資料、保存中間產出、卸載暫時不需要的資訊、讓多 agent 協作。Git 加上版本紀錄，agent 可以追蹤進度、開分支實驗、rollback。

### Bash / Code Execution — 通用工具層
給 agent bash 和 code execution 能力，讓它能自己組合解法，不需要預先設計每種工具。這是 ReAct loop（reason → 呼叫工具 → 觀察 → 繼續）的執行基礎。

### Sandbox
- 隔離邊界，試錯不傷主機環境
- 好的 sandbox 預裝語言環境、測試 CLI、headless browser
- 讓 agent 形成 **self-verification loop**（自己做完自己先查）

### Memory + Search
- AGENTS.md 等 memory file：session 開始時注入專案知識、慣例、過去踩坑
- Web search / MCP tools：補充即時資訊（新版 library、最新 API）

### Context Rot 三種對策
| 方法 | 說明 |
|------|------|
| Compaction | 舊對話整理成摘要，避免 context 爆掉 |
| Tool-call offloading | 大型輸出存 filesystem，context 只保留摘要 |
| Progressive disclosure | 工具/文件按需載入，不一次全塞 |

### Long-Horizon Execution
| 機制 | 說明 |
|------|------|
| Loop | 攔截模型提早結束，強制繼續 |
| Planning | 先拆 step-by-step plan file，每步後 self-verification hook |
| Split | 產出和評估拆給不同 agent（同一模型評自己作品有正向偏差）|

### Hooks — 執行層強制機制
**原則：成功時安靜，失敗時大聲。**

Hook 在生命週期節點自動執行（工具呼叫前、檔案修改後、commit 前）：
- 阻擋危險指令
- 自動 formatting（省 token）
- 跑 test suite / typecheck
- 失敗 → 錯誤直接注入回 loop，agent 自行修正

Hook 不是建議，是守門員。

### Rulebook 設計原則
> AGENTS.md 應該像飛行員的檢查清單，不是冗長風格指南。

- 每一條規則都要能追溯到某次失敗
- 10 個職責清楚的工具 >> 50 個功能重疊的工具
- **安全警告**：工具描述直接進 prompt，惡意或品質差的 MCP server 可在 agent 開始前注入指令

## Ratchet：錯誤轉規則

每次 agent 失敗不是「下次小心」，而是永久修正：

```
agent 把測試註解掉被 merge
→ AGENTS.md 加規則：不要註解掉測試
→ pre-commit hook 自動抓 .skip(
→ reviewer subagent 更新：遇到此狀況阻擋
```

限制只在真正觀察到失敗時加入；模型變強後，過時限制也要移除。

## 從行為往回設計 Harness

**先問：我希望 agent 出現什麼行為？**

每個 harness 元件都要能回答：「它幫 agent 變好在哪裡？」說不出來的元件就移除。這讓 harness 工程更像產品設計，不是堆設定。

## Harness 不會萎縮，只會移動

模型越強，舊的 scaffolding 可以移除，但更高的任務邊界帶來新的失敗模式，又需要新的 scaffolding。每個 harness 元件背後都在說「這裡不能完全相信模型自己處理」。

## Harness 也影響模型訓練

Post-training 階段模型在特定 harness 裡被訓練，會 overfit 到該 harness 重視的動作（filesystem ops、bash、subagent dispatch）。**Harness 是 living system，和模型一起演化。**

## 產業方向：Harness-as-a-Service

從「用 LLM API 寫東西（completion）」→「用 Harness API 跑東西（runtime）」

現有 SDK 已把 loop、工具管理、context management、hook、sandbox 打包好。工程師選 harness framework，設定核心模組，心力放在領域 prompt 和工具設計。

未來：harness 不像靜態設定檔，更像 **compiler**——根據任務即時組裝工具、流程、限制和檢查機制。

## 對派哥的啟示

這篇是目前知識庫裡 harness 概念最完整的一篇，幾乎是 cc_processor + CLAUDE.md 的設計理論基礎。

**已在做的（對照）**：
| Harness 元件 | 派哥的實作 |
|-------------|-----------|
| Rulebook (AGENTS.md) | CLAUDE.md + skills/ |
| Hooks | SessionStart hook + pre-commit |
| Ratchet | CLAUDE.md 每條規則都有失敗教訓 |
| Context Rot — Compaction | /compact 指令 |
| Memory | `~/.claude/projects/.../memory/` |
| Split（產出/評估分離）| Claude 寫安全邏輯 → Gemini 審 |

**值得補的**：
1. **Observability**：cc_processor 目前 log 零散，沒有 cost/latency 追蹤
2. **Progressive disclosure**：skills/ 已有，但部分 CLAUDE.md 內容可以進一步拆出
3. **Self-verification hook**：typecheck/lint 在完成前強制跑，目前靠人工觸發

## 連結筆記

- [[harness-engineering]] — 基礎版（Birgitta Böckeler / Martin Fowler）
- [[harness-engineering-coding-agents]] — Coding agents 的 harness 應用
- [[addyosmani-agent-skills]] — Addy 的 19 個 agent skills 套件
- [[agents-md-context-engineering]] — AGENTS.md 設計與 context engineering
- [[claude-md-optimization]] — CLAUDE.md 優化
- [[garry-tan-thin-harness-fat-skills]] — 薄 Harness 厚 Skills
