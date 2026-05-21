---
title: "AI 協作除錯流程：8 步驟 Bug Fix SOP"
tags: [claude-code, debugging, TDD, workflow, skills]
date: 2026-04-03
category: 03.科技工具
source: Threads post
---

## 核心原則

> **先有證據，才能動手。**
> 沒有最小重現、沒有 failing test、沒有根因證據 → 禁止直接改程式碼。

## 8 步驟流程

| 步驟 | 說明 | Skill |
|------|------|-------|
| 1. 最小重現 | 症狀 → 機器可判斷的重現步驟 | brainstorming |
| 2. Failing Test | 重現步驟 → 穩定失敗的測試 | test-driven-development |
| 3. 驗證根因 | 帶 failing test 讀 code，找真正原因 | systematic-debugging + serena MCP |
| 4. 最小修復 | 只改讓 failing test 通過的最小範圍 | subagent-driven-development |
| 5. Regression 防護 | 避免同 bug 偷偷回來 | test-driven-development |
| 6. Spec Compliance | 確認符合原始需求 | verification-before-completion |
| 7. Code Quality | 乾淨、可維護、無副作用 | requesting-code-review |
| 8. Final Report | report + 殘留風險 + git log | finishing-a-development-branch |

## 反模式（要避免）

「我大概知道怎麼修，先 patch 再說」→ 常導致：
- 修到症狀，不是根因
- 沒有 failing test，不知道修對沒
- 沒有調查紀錄，下次同類 bug 重查一次

## 文件化價值

留下 `spec.md` + `plan.md` + `report.md`，下次遇到類似問題不用從零開始。

## 適用場景

My Wallet Trip 或任何專案 bug 回報時，按此 8 步走，不要直接改 code。
