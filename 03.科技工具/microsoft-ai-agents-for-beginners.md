---
title: Microsoft AI Agents for Beginners：官方開源入門課程
tags: [AI, Agent, 工作流程, RAG, 架構設計]
date: 2026-05-19
category: AI工具
source: https://github.com/microsoft/ai-agents-for-beginners
---

## 這是什麼

Microsoft 官方開源的 AI Agent 入門課程，結構化學習從基礎到生產部署的完整 Agent 知識體系。

GitHub：https://github.com/microsoft/ai-agents-for-beginners

---

## 核心概念 / 架構

課程涵蓋的主題：

| 主題 | 說明 |
|------|------|
| AI Agent 基礎 | Agent 定義、架構、工具使用 |
| Agentic RAG | RAG + Agent 結合，主動決策取回知識 |
| Multi-Agent | 多 Agent 協作架構 |
| Agent Memory | 記憶機制設計（短期/長期） |
| Context Engineering | 上下文管理與優化 |
| MCP / A2A / NLWeb | 協定層：Model Context Protocol、Agent-to-Agent、NLWeb |
| Browser Use Agent | 瀏覽器自動化 Agent |
| AI Agent Production | 生產環境部署與穩定性 |
| Trustworthy AI Agents | 安全、可信賴、可解釋 |
| Microsoft Agent Framework | AutoGen 等 MS 生態工具 |

---

## 使用方法 / 快速啟動

```bash
git clone https://github.com/microsoft/ai-agents-for-beginners
# 按章節順序學習，每章都有 notebook + 範例
```

---

## 對派哥的啟示

- **Context Engineering** 這章最值得看：派哥的 CLAUDE.md 設計本質上就是 context engineering，這章能給理論框架
- **Agentic RAG**：MyNotes 的「問知識庫」就是 Agentic RAG 的實踐，對照學可以補強設計邏輯
- **MCP / A2A**：派哥已在用 MCP（Gmail、Calendar），這章可以了解協定背後的設計意圖
- **Trustworthy AI Agents**：cc_processor 的 prompt injection 防線就是這個問題的實作

入門課的好處：給已有實作的派哥一個「補理論地基」的機會，填補「知道怎麼做但不知道為什麼」的空缺。

---

## 連結筆記

- [[agent-capability-map-expansion]] — Agent 能力地圖
- [[multi-agent-system-architecture-optimization]] — 多 Agent 架構優化
- [[anthropic-mcp-production-patterns]] — MCP 生產環境模式
- [[karpathy-llm-wiki-persistent-knowledge]] — LLM 知識工件概念
