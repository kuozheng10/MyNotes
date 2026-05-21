---
title: AI Infra Ops Platform：Monitoring + Workflow + AI + Knowledge + Action 三層架構
tags: [AI Agent, MCP Server, Infra Ops, 多Agent, Skill Library, 監控, 自動化, 企業AI]
date: 2026-05-07
category: AI工具
---

## 這是什麼

一個真實可落地的企業 IT Infra 自動化平台藍圖：讓 AI 理解監控告警、自動執行檢查、從知識庫取得對應 Action，用 MCP Server 統一工具，再由 Agent 協同完成分析與決策。

**核心口號**：求人不如求己。讓 IT Infra 自己呼吸。

---

## 白話文版

傳統 Infra 運維：告警跳出來 → 人去查 → 人去執行 → 人去記錄 → 下次還是一樣。

這個平台的目標：告警跳出來 → AI 看懂 → AI 查知識庫 → AI 自動執行或叫對應的 Agent → 人只在真正需要判斷的地方介入。

---

## 四層架構（含 Layer 0）

### Layer 0 — AI 基礎建設
提供整個系統的底層能力，任何 Agent 和工具都依賴這層：

| 模組 | 內容 |
|------|------|
| LLM Runtime | OpenAI/Claude/Llama 等模型閘道 |
| Workflow Runtime | n8n/Airflow/Temporal 排程與自動化 |
| Knowledge/RAG | Vector DB + 知識庫（Wiki/SOP/Runbook）|
| Security/Identity | API Token、SSO、RBAC 權限管控 |
| Observability | Prometheus/Grafana/ELK 監控堆疊 |
| DevOps/AI Platform | Git Repo、CI/CD、Container 管理 |

### Layer 1 — AI Agent Layer（智能代理）
多個專責 Agent，由 Agent Orchestrator 調度：

| Agent | 職責 |
|-------|------|
| FiOps Agent | 成本分析、資源優化 |
| Infra Ops Agent | 基礎設施監控、告警處理 |
| Service Desk Agent | 工單管理、使用者問題 |
| Security Agent | 身份驗證、安全稽核 |
| Change/Release Agent | 變更管理、部署協調 |

+ **Memory/Knowledge**：Session 記憶 + 知識庫（Wiki/SOP/Runbook）
+ **Governance**：身份管理、Audit Log、人工介入節點（Human-in-the-loop）

### Layer 2 — Skill Library（可重複使用能力）
標準化技能模組，Agent 按需呼叫：

- Azure Cost Analysis / Zabbix Alert / Log Analysis
- SOP/Runbook Query / Ticket Triage / Capacity Planning
- Reporting Skill

Skill Runtime 負責：輸入驗證 → 執行 Skill → 格式化 → 回傳 Agent

### Layer 3 — MCP Server Layer（統一工具平台）
透過 MCP Gateway 統一接入所有外部系統：

| MCP Server | 接入系統 |
|------------|---------|
| Azure MCP | Azure Cost/Resource API |
| Zabbix MCP | 告警、監控資料 |
| ELK MCP | 日誌查詢 |
| Ticket MCP | ServiceNow/Jira |
| SOP/Wiki MCP | Confluence/SharePoint |
| System MCP | 指令執行、服務重啟 |
| Notification MCP | LINE/Slack/Teams/Email |

---

## 對派哥的應用

| 場景 | 借鑑點 |
|------|--------|
| cc_processor / My Wallet Trip | 加 Observability Layer：告警→自動重試或通知 |
| OpenClaw 自動化 | 就是這個架構的簡化版：Skill = `.claude/skills/`，MCP = 現有 MCP servers |
| 未來擴充 | 把現有 TG bot 升級成真正的 Agent Orchestrator，多個 Skill 按需組合 |

---

## 連結參考

- [[claude-agent-five-layer-architecture]] — Claude Code 的 Agent 五層設定
- [[anthropic-mcp-production-patterns]] — MCP Server 生產環境模式
- [[multi-agent-system-architecture-optimization]] — 多 Agent 系統架構
- [[harness-engineering-automation-risks]] — 自動化風險管控
