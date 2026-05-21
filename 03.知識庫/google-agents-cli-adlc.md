---
title: "google/agents-cli — 給 AI 編程助手用的 Google Cloud Agent 開發 CLI"
url: "https://github.com/google/agents-cli"
tags: [google, gcp, claude-code, cli, agent, deploy, eval, adlc]
date: 2026-05-10
category: 03.科技工具
source: Telegram 派哥分享（Cloud Next '26）
---

## 摘要

> Google 官方 CLI，把 Agent 開發生命週期（ADLC）整合成一個工具鏈，讓 Claude Code / Gemini CLI / Codex 用自然語言完成 build → eval → deploy → monitor 全流程。

## 七個核心 Skill 模組

| 模組 | 功能 |
|------|------|
| Workflow | 整體流程協調，串接所有 skill |
| ADK Code | 寫 ADK Agent 程式碼 |
| Scaffold | 從零建立 Agent 專案結構 |
| Evaluation | 自動跑 eval，含 trajectory scoring |
| Deployment | 部署到 Cloud Run / GKE / Agent Runtime |
| Publish | 發布到 Gemini Enterprise |
| Observability | Cloud Trace、Logging、第三方整合 |

## 使用方式

```bash
# 安裝
pip install google-agents-cli  # 或 npm，視實際安裝方式

# 在 Claude Code 裡直接說：
> 幫我建一個可以分類 incident 的 agent
```

支援：Claude Code、Gemini CLI、Codex、Cursor

## 和 google/skills 的差異

| | google/skills | google/agents-cli |
|--|--|--|
| 性質 | Agent Skills 知識庫（參考文件）| CLI 工具鏈（可執行動作）|
| 用途 | 讓 AI 學會 GCP 最佳實踐 | 讓 AI 直接 build/deploy GCP Agent |
| 關係 | 互補，agents-cli 執行，skills 提供知識 |

## 對派哥的評估

**先存，未來用。**

現在不需要：派哥的自動化（cc_processor、sales report）是本地 Python，不需要 GCP Agent Runtime。

有用的時機：
- 想把某個 automation 搬到 GCP 跑（有 uptime/scaling 需求）
- 需要 trajectory scoring 做 Agent eval（測 cc_processor 的準確率）
- 替客戶建正式的 GCP Agent 服務

最值得關注的模組：**Evaluation**（trajectory scoring）— 可以量化測試 Agent 的行為是否符合預期，這在現有工具裡很少見。

## 相關筆記

- [[google-skills-gcp-agent]] — google/skills Agent 知識庫（互補）
- [[anthropic-mcp-production-patterns]] — MCP 生產部署模式
