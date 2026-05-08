---
title: RuFlo v3.5：開源 Enterprise AI Orchestration Platform
tags: [AI編排, 多Agent, Claude, 開源, 成本優化, MCP]
date: 2026-05-09
category: AI工具
---

## 核心定位

RuFlo（原 RuFlow）是開源的 AI 編排框架，把 Claude Code 單一 agent 升級成 60+ 專門 agent 的蜂群（swarm）。由 **Reuven Cohen (ruvnet)** 開發，GitHub: `ruvnet/ruflo`。

安裝：

```bash
npx ruvflo@latest init-wizard
```

---

## 核心功能

- **多 Agent 蜂群**：Queen/Worker 階層架構或 mesh 拓撲，平行執行任務
- **RuVector Intelligence Layer**：WASM 神經引擎（SONA），子毫秒任務路由，智能分派給對應角色
- **成本優化**：簡單任務派給小模型，宣稱降低 API 費用 75%
- **MCP Native**：整合 215+ MCP 工具（CI/CD、安全掃描、雲端部署）
- **自學記憶**：向量記憶持久化，agent 之間共享上下文

---

## 效能數據

- SWE-bench 解決率：**84.8%**（頂級自動化 coding 系統之一）

---

## 與 Claude Code 的關係

RuFlow 坐在 Claude Code 上層，攔截高階指令後拆解成 atomic sub-tasks，分配給 60+ 專門角色（Architect、Coder、Tester、Security Reviewer 等）。

---

## 派哥適用場景

- 大型重構 / 多檔案任務（目前靠 Codex exec 處理）
- 想降低 Claude API 用量
- 需要平行 agent 協作的複雜功能

---

## 連結參考

- [[multi-agent-system-architecture-optimization]] — 多 agent 架構優化
- [[claude-agent-five-layer-architecture]] — Claude Code 五層架構
- [[agent-skills-standard]] — Agent skill 標準
