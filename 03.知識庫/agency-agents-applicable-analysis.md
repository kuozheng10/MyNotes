---
title: Agency Agents：150+ 專業 AI Agent 角色庫 + 派哥適用分析
tags: ["Agent", "Claude Code", "工具", "自動化"]
date: 2026-04-22
category: AI工具
source: https://github.com/msitarzewski/agency-agents
---

## 這是什麼

150+ 個專業 AI Agent 角色庫，涵蓋 Engineering、Design、Marketing、Sales、Testing、Product 等領域。每個 agent 有明確的 identity、使命、技術交付物和成功指標，可直接安裝進 Claude Code。

安裝（全部）：
```bash
./scripts/install.sh --tool claude-code
cp engineering/*.md ~/.claude/agents/
```

## 對派哥有用的 Agent（優先度排序）

### 🔴 高優先（直接對應現有工作）

| Agent | 對應場景 |
|-------|----------|
| **Report Distribution** | sales_report + SPA安庫 自動發送，可強化寄送邏輯 |
| **Data Consolidation** | 業務業績統計.py 樞紐分析的資料整合邏輯 |
| **Sales Data Extraction** | SalesOrderReport xlsx 解析、欄位提取 |
| **DevOps Automator** | launchd plist 排程、Gmail token 自動更新流程 |

### 🟡 中優先（偶爾用到）

| Agent | 對應場景 |
|-------|----------|
| **Security Engineer** | Gmail OAuth 安全性、API key 處理審查 |
| **Backend Architect** | 多個 processor 的架構設計，避免重複邏輯 |
| **Data Engineer** | Excel/xlsx pipeline 優化 |
| **Support Analytics Reporter** | Telegram 報告格式改善、異常監控 |

### 🟢 未來用到（有計畫方向）

| Agent | 對應場景 |
|-------|----------|
| **API Tester** | 測試 Gmail API、Notion API 連線穩定性 |
| **Senior PM** | 多專案（cc/sales/SPA/MyWallet）優先序管理 |
| **UI Designer** | My Wallet Trip 前端設計 |
| **Performance Benchmarker** | 測試腳本執行時間、瓶頸分析 |

## 質疑

- 前提假設：Agent 角色庫假設你會主動呼叫對應角色；實際上多數人裝了就忘，需要有觸發機制
- 適用邊界：Engineering 類 agent 對大型 team 設計的，派哥單人維護的小腳本用 Senior Developer 就夠，不需要 DevOps + SRE + Security 全上
- 潛在反例：太多 agent 在同一個 Claude Code session 中會互相干擾 context，建議按任務載入單一 agent

## 對標

- **工具箱 vs 工具人**：這個 repo 是工具箱——你要知道什麼場景拿什麼工具。跟 MyNotes skill 系統是同一個思維，只是針對 Agent 角色而非知識

## 自動建議機制（如何不忘記用）

在 CLAUDE.md 加一個「場景 → agent 建議」對照表，讓每次啟動 Claude Code 時能對號入座。→ 見 [[context.md]] 更新版

## 連結筆記

- [[agency-agents-multi-agent]]
- [[ai-agent-system-design-over-prompt]]
- [[harness-engineering-coding-agents]]
- [[claude-code-powerup-guide]]
