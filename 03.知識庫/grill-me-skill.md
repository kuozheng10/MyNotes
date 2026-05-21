---
title: "grill-me — 壓力測試計劃的 Claude Code Skill"
url: "https://github.com/mattpocock/skills/blob/main/grill-me/SKILL.md"
tags: [claude-code, skill, planning, design, architecture]
date: 2026-04-07
category: 03.科技工具
source: Telegram 派哥分享
---

## 摘要

> Claude Code skill，像面試官一樣連環提問，逐一攻破計劃的每個決策分支，直到完全釐清。每問附上推薦答案，一次一題。

## 功能

- 對設計/計劃做壓力測試，不讓模糊假設蒙混過關
- 走完整個決策樹，解決分支間的依賴關係
- 每個問題附推薦答案（省去自己查的時間）
- 如果問題可以靠讀 codebase 回答，直接去讀（不浪費時問答）

## 觸發時機

說「grill me」或「想被考一下這個設計」時觸發。

## 安裝

```bash
git clone https://github.com/mattpocock/skills ~/.claude/skills/grill-me
```

使用：在 Claude Code 輸入 `/grill-me`

## 評估：對派哥有用嗎？

**有用。** 適合這些場景：
- 新功能設計前（cc_processor 擴充、My Wallet Trip 新需求）
- 架構決定時想確認自己沒遺漏
- 做到一半卡住，想快速拆解問題

和 [[vibe-coding-architecture-debate]] 的差異：
- 那個是「看兩種觀點」→ 適合看清楚大方向
- 這個是「你被逼著回答每個細節」→ 適合確認設計完整性

## 相關筆記

- [[vibe-coding-architecture-debate]] — 架構設計辯論觀點
- [[claude-code-feature-workflow]] — Feature 開發流程
