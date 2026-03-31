---
title: "Claude Code Feature 開發流程（gstack 模式）"
tags: [claude-code, workflow, CLAUDE.md, feature-development, code-review]
date: 2026-03-31
category: 03.科技工具
source: LinkedIn 分享（作者 4/1 轉待職）
---

## 摘要

> 一套把 feature 開發「制度化」的 Claude Code 流程：需求澄清 → 任務拆解 → 平行實作 → 雙階段審查 → 可追溯報告。作者將自己的 CLAUDE.md 整理分享出來。

## 完整流程

觸發條件：偵測到 `spec.md` 或使用者說「實作這個 feature」

| 步驟 | 動作 | Skill |
|------|------|-------|
| 1. Brainstorm 💡 | 針對 spec 提問、澄清需求、確認功能邊界 | `gstack:plan-ceo-review` |
| 2. Plan 🗂️ | 拆成 2–5 分鐘 task，產出 plan.md + tasks.md | `gstack:plan-eng-review` |
| 3. Implement ⚙️ | 每個 task 獨立 Agent + worktree 隔離，支援平行 | Agent Teams（parallel） |
| 4. Review Stage 1 ✅ | Spec Compliance 檢查，逐條對照驗收條件 | `gstack:review` |
| 5. Review Stage 2 🔍 | Code Quality：架構品質、DRY、constitution 合規 | `simplify` + `gstack:review` |
| 6. Report 📝 | 產出 report.md，整理 pass/fail + git log | `gstack:document-release` |

## 核心價值

- 減少 spec 誤解帶來的返工
- task 粒度適合 Agent 執行
- review 從主觀變成有依據的檢查流程
- 每次 release 留下可回溯紀錄

## 評估（個人開發適用性）

**適合直接採用的部分：**
- Brainstorm（澄清需求）→ Plan（拆 task）流程，避免跳太快動手
- 雙階段 review：spec compliance + code quality 分開跑
- 產出 report 紀錄

**需要注意：**
- `gstack:*` 是作者自定義 skill，需要安裝 gstack marketplace
- worktree 平行 Agent 適合大型 feature，小功能可簡化
- 個人開發可省略部分儀式感，保留骨幹邏輯即可

## 可加進自己 CLAUDE.md 的精華版

```markdown
當收到「實作 feature」指令時：
1. 先提問澄清需求（5 分鐘內完成）
2. 拆成 task list，每個 task 2-5 分鐘可完成
3. 實作完做 spec compliance 檢查
4. 再做 code quality 檢查（DRY、安全性）
```

## 相關

- [[codex-plugin-cc]] — 另一種 code review 工具
- [[claude-code-computer-use]] — UI 驗證工具
