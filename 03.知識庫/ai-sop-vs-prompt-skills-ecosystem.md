---
title: Prompt 是一次性指令，SOP 是可重複能力——Skills Ecosystem Explosion
tags: [AI工作流, SOP, Prompt, Skills, 知識管理, 自動化]
date: 2026-04-29
category: AI工具
---

## 核心洞見

GitHub Trending 現象（2025 末至 2026 初）：上榜的不是新 framework 或 model wrapper，而是一批 **skills repo**（html-ppt-skill、diagram-design、design-extract、agentic-stack），兩週內衝上 1,000+ star。

背後訊號：**AI 使用方式正從「會問問題」進化成「會設計流程」**。

---

## Prompt vs SOP 的核心差異

| | Prompt | AI SOP |
|--|--------|--------|
| 定義 | 一次性指令 | 可重複產生結果的流程 |
| 問題 | 每次重新交代背景，像每天 onboarding 新人 | 告訴 AI「以後遇到這類事情，都照這套做」 |
| 價值 | 夠用但不可複製 | 效率工具（個人）+ know-how 容器（團隊） |

---

## AI SOP 的五個組成要素

1. **Context**：每次開始前要知道什麼背景
2. **Steps**：任務怎麼拆分
3. **Standards**：什麼叫做好
4. **Output**：要交付什麼格式
5. **Review**：哪些地方必須交給人確認

---

## AI 使用能力三階段

| 階段 | 做法 | 解決的問題 |
|------|------|-----------|
| 初學者 | 每次問新 prompt | — |
| 進階者 | 整理 prompt library | 下次不用重打 |
| 高手 | 封裝成 skills / workflows / SOP | 穩定做對，別人也能照套 |

**工程師說的 skill = 管理者說的 SOP**——本質相同，把判斷流程封裝成可重用格式。過去兩條線各走各的，現在開始合流。

---

## SOP 模板（最小可用版）

```markdown
# [SOP 名稱]

## 目標
這個 SOP 要幫我重複完成什麼工作？

## 背景
AI 每次開始前需要知道哪些 context？

## 步驟
1. 先確認輸入資料
2. 拆解任務
3. 產出第一版
4. 自我檢查
5. 回報不確定性

## 輸出格式
最後用什麼格式交付？

## 驗收標準
什麼情況才算完成？哪些必須請人確認？
```

---

## 三種固化方式（依難度）

| 方式 | 做法 | 門檻 |
|------|------|------|
| 對話貼上 | 每次開新對話貼模板 | 最低，今天就能做 |
| 工具固化 | 存成 Claude Project instructions / Custom GPT | 中，自動載入 |
| 工程封裝 | 製作成 Skill（SKILL.md 格式） | 最高，可被呼叫重用 |

---

## 對派哥的意義

- 派哥的 `~/.claude/skills/` 已經是高手階段——skills repo 就是在做這件事
- 本文可作為說服他人導入 AI SOP 的參考框架
- 重點：**先把每週重複做的工作挑一件，整理成 AI 可重複執行的流程**
- Prompt 會過期，SOP 會累積；Prompt 大全越存越亂，SOP 越用越值錢

---

## 連結筆記

- [[agent-skills-standard]] — Skill 標準格式設計
- [[garry-tan-thin-harness-fat-skills]] — Fat Skills 的價值主張
- [[autoskills-skill-infrastructure]] — Skill 基礎設施
- [[claude-md-optimization]] — CLAUDE.md 即一種 SOP
- [[ai-build-skills-nick-baumann]] — 用 AI 建立 skills 的實踐
