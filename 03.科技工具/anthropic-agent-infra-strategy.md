---
title: Anthropic 的 Agent Infra 大賭注：要當 Chrome/Office 還是 Intel/AMD？
tags: [anthropic, agent, agent-infra, aws, google, azure, claude-code, 競爭策略, 基礎建設]
date: 2026-04-27
category: AI工具
---

## 核心論點

Anthropic 正從「模型開發商」轉型為「Agent 基礎架構提供者」。
底層 LLM 差距縮小是大勢，**體驗與架構鎖定**才是決勝關鍵。

---

## 關鍵事件（2026-04-23）

Anthropic 宣布 **Claude Cowork（Harness 框架）開放給第三方模型**：
- 可串接 GPT、Gemini 等任何 LLM
- 透過 OpenRouter 也支援開源模型
- AWS Bedrock、Google Vertex AI、微軟 Foundry 全面支援

意義：Anthropic 把自家的 Runtime 框架做成「中立基礎設施」，不再只綁自家模型。

---

## Agent Infra 四層架構

| 層級 | 說明 | 代表產品 |
|------|------|---------|
| **模型層** | 各家 LLM | Claude, GPT, Gemini |
| **協定層** | 呼叫模型的通訊標準 | OpenAI Chat Completions、Anthropic Messages API |
| **Runtime 層** | 工作執行環境 | Claude Code、Cursor、Codex |
| **控制面層** | 企業大規模部署與治理 | AWS Bedrock AgentCore、Azure Agent 365 |

**目前戰場**：各巨頭都在搶「控制面層」的企業客戶忠誠度。

---

## 三大雲端巨頭的 Agent Infra 布局

### AWS
- **Bedrock AgentCore**：Agent 執行環境（Runtime）
- **Agent Registry**：企業管理 Agent 的中樞平台

### Google
- **Vertex AI Agent Builder + ADK**：開發框架
- **Apigee**：API 閘道器整合（Google Cloud 企業的既有護城河）

### Microsoft Azure
- **護城河**：企業身分認證（Active Directory）
- **願景**：每個 Agent 有獨立帳號身分、權限分級、生命週期
- **Agent 365**：像用 AD 管員工一樣管 AI 代理

---

## Anthropic 的賭局

**Anthropic 目前專注 Runtime 體驗**（Claude Code 等），快速建立終端用戶忠誠度。
**長期目標**：掌握 Agent Infra 的框架話語權，透過三大雲端平台切入企業端。

為什麼這是豪賭：
- 純做 LLM = 虧本生意（訓練+推理持續燒錢）
- 做起 Agent Infra = 企業客戶對基礎架構的信任極難轉移
- 企業遷移 Agent 架構的痛苦 ≈ 強迫大公司放棄 Microsoft Office

Anthropic 的戰略入口：**2026-04-08 推出 Managed Agents Beta**

---

## 核心比喻

| 比喻 | 意思 |
|------|------|
| 用 Chrome 上網，不在意底層是 Windows 還是 macOS | 用 Claude Code 工作，不在意底層是哪家 LLM |
| 用 Office，不在意是 Intel 還是 AMD CPU | 用 Agent Infra，底層模型隨插即用 |

---

## 對派哥的意義

- **現在跑分 Benchmark 已失去意義**，選工具看 Runtime 體驗與生態整合
- **Claude Code 的護城河不是模型**，是 Harness 框架與技能生態
- **企業上 Agent 時代**：1-2 年內 Agent Infra 標準會成形，先佔者通吃
- cc_processor / MyNotes 等個人自動化流程，長期考慮能否遷移到雲端 Agent Infra

---

## 連結筆記

- [[claude-managed-agents-beta]] — Anthropic Managed Agents 全託管平台 Beta
- [[ai-agent-modular-architecture]] — Agent 模組化架構設計
- [[enterprise-ai-adoption-strategy]] — 企業 AI 採用策略
- [[claude-code-powerup-guide]] — Claude Code 功能深度解析
- [[full-agent-dev-ecosystem-goatwang]] — Agent 完整開發生態觀察
