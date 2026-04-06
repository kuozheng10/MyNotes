---
title: "CLAUDE.md 瘦身法：5 條規則 + 按需讀取"
tags: [claude-code, CLAUDE.md, token, optimization, cost, workflow]
date: 2026-04-06
category: 03.科技工具
source: 社群分享
---

## 核心觀點

> 把所有規則塞進 CLAUDE.md = 每輪對話強迫 AI 背員工手冊。

**優化前**：每輪對話扣 5,000 token 基本消費
**優化後**：壓到 500 token，成本差 10 倍

## 做法

### 1. CLAUDE.md 瘦身
- 只留 5 條核心規則，總字數 < 500 token
- 細節用檔案路徑標註，例如：
  ```
  API 規範：見 docs/api.md
  測試規範：見 docs/testing.md
  ```
- AI 真的需要時才去讀那個檔案，不是每輪都載入

### 2. 模型分級
| 任務 | 模型 |
|------|------|
| 複雜架構設計、業務決策 | Opus |
| 一般開發、功能實作 | Sonnet |
| 寫測試、修格式、重複勞動 | Haiku |

## 評估：對派哥有用嗎？

**直接有用。** 派哥的 CLAUDE.md 現在包含完整的：
- Feature 開發流程（SBE + 5步）
- 影片摘要流程
- Bug Fix 8步驟
- 測試策略
- 多個規範段落

這些每輪都載入，估計超過 2,000 token。

**建議行動**：
把 CLAUDE.md 改成「目錄 + 路徑」結構：
- 核心規則 5 條留著
- 各流程細節移到 ~/.claude/skills/ 或 docs/ 下
- CLAUDE.md 只說「Bug Fix 流程見 ~/.claude/skills/bugfix.md」

## 相關筆記

- [[agent-prompt-token-cost]] — Prompt 中文省 token 手法
- [[claude-code-source-leak-insights]] — CLAUDE.md 的實際作用（harness）
- [[bugfix-8steps-workflow]] — 可以從 CLAUDE.md 移出的流程
