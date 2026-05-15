---
title: "Claude for Financial Services：Anthropic 開源金融 AI 插件集"
tags: [claude-code, 架構設計, skill, domain-specific, 開源, Agent, MCP]
date: 2026-05-15
category: AI工具
source: https://github.com/anthropics/financial-services
---

## 這是什麼

Anthropic 官方開源金融服務業 Claude 插件集，涵蓋投資銀行、股權研究、私募股權、財富管理。

架構：Markdown + JSON（無複雜程式碼），輕量高整合。

## 核心結構

**11 個端到端 AI Agents**（代表性）：
- Pitch Agent — 併購簡報製作
- Earnings Reviewer — 財報點評 + 財務模型更新

**7 大垂直 Skills 包** + 合作夥伴資源

**11 個金融數據源 MCP 連接器**：FactSet、S&P Global、PitchBook、Aiera 等

## 與法律版的關鍵差異

| 面向 | 法律版 | 金融版 |
|------|--------|--------|
| 核心痛點 | 文件審查、合約草擬 | 財報分析、財務模型 |
| 數據源整合 | 法律資料庫 | FactSet/PitchBook 等 11 個 |
| 合規要求 | 律師保密義務 | 金融監管（高標準） |
| 設計重點 | 冷啟動 CLAUDE.md | 數據來源追溯 + 推論可解釋性 |

兩者都是同一個設計公式：**基礎工具 + 冷啟動 CLAUDE.md（SOP + 範本 + 風格）**

## 對派哥的啟示

金融版的 MCP 數據連接器設計值得注意：它把 FactSet 這類授權數據源包成 MCP server，讓 agent 能精確引用數據而不是亂猜。

這個模式可以參考：cc_processor 的 Notion、Gmail 串接，其實是同一個邏輯——把外部數據源包成 MCP，讓 agent 有乾淨的讀寫介面。

實際用途有限（不是金融從業者），但 repo 結構是學 agent + MCP 設計模式的一手範本，尤其是 11 個 data connector 的包法。

## 連結筆記

- [[claude-for-legal-domain-customization]] — 同系列法律版（冷啟動 CLAUDE.md 設計模式）
- [[anthropic-mcp-production-patterns]] — MCP 生產環境設計
- [[garry-tan-thin-harness-fat-skills]] — 薄 Harness 厚 Skills
- [[agents-md-context-engineering]] — AGENTS.md 冷啟動概念
