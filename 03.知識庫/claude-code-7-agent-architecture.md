---
title: "Claude Code 7-Agent 架構：拆開分工避免互踩"
tags: [claude-code, multi-agent, architecture, agents, workflow, 分工]
date: 2026-05-29
category: 03.知識庫
source: Telegram 分享
related: [[agency-agents-multi-agent]], [[agent-skills-standard]]
---

## 核心問題

單一 Claude Code session 被迫同時扮演太多角色（需求分析、架構設計、後端、前端、測試、審查），導致改一個地方觸發其他 bug。

## 7-Agent 架構

```
研究員 → 需求整理員 → 規格撰寫員 → 後端建構員
                                   ↓
                              前端建構員 → 測試驗證員 → 品質驗證員
```

中間加 3 個人工檢查點：
1. ✔️ 確認需求
2. ✔️ 確認規格
3. ✔️ 最後 Review & PR

## 實作方式

每個 Agent = 一個 `.md` 檔，放在：

```
.claude/agents/
```

檔案內容：名稱、觸發時機、工具權限、工作規則。

## 觸發方式

### 手動指定（建議先用這個）
```
「請使用研究員 Agent 先讀懂這個專案架構」
「請使用規格撰寫員 Agent 幫我整理技術規格」
「請使用品質驗證員 Agent 檢查這次改動」
```

### 自動觸發（流程跑順後再設定）
Agent `.md` 檔裡的 `description` 欄位決定 Claude Code 何時自動派用：

```markdown
description: Use before implementation to inspect the codebase and identify patterns.
```

> **重點：`description` 不只是說明文字，它影響 Claude Code 的自動路由邏輯。**

## 建議導入順序

1. 先手動指定每個 Agent
2. 等流程熟了、description 寫清楚了
3. 再讓 Claude Code 自動判斷派誰

## 派哥現狀對應

派哥的 MyClaude 目前用 `~/.claude/skills/` 放 skill（類似 agent），但沒有明確的 `.claude/agents/` 分工架構。

如果要套用這個 pattern，可以把 cc_processor、insurance_processor 等複雜任務拆成：研究員→規格員→實作員→品質驗證員 四層。
