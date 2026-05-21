---
title: ADR：MCP 協議 vs 直接打 API 的決策標準
tags: [ADR, MCP, API, 架構設計, Agent]
date: 2026-04-27
category: 系統架構
---

## 決定

依場景選擇，不是一律走 MCP 或一律直接打 API。

## 決策矩陣

| 情境 | 選擇 | 原因 |
|------|------|------|
| 工具數量 > 5 個、未來會擴充 | MCP | 統一介面，擴展成本低 |
| 對延遲敏感（< 500ms 體驗要求） | 直接 API | 少一層呼叫，快 |
| 工具是第三方服務（Notion/GitHub/Gmail） | MCP | 有現成 MCP server 直接用 |
| 內部自建工具、邏輯簡單 | 直接 API | 不值得包 MCP server |
| 需要跨 agent/session 共享工具 | MCP | MCP 設計目的就是這個 |
| 一次性、快速驗證 POC | 直接 API | 速度優先，不值得建 MCP |

## 簡化版判斷

- 工具要給「多個 AI / 多個 session」用 → MCP
- 工具只給「這個 agent 用一次」→ 直接 API

## 背景

健檢發現：MCP 官方建議走 MCP 解決擴展問題，但 Sprite-forge 等實作偏好直接呼叫換取速度。知識庫缺乏統一決策標準，造成每次遇到這個問題都要重新思考。

## 相關筆記

- [[anthropic-mcp-production-patterns]]
- [[codex-image2-agent-sprite-forge]]
