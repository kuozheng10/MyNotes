---
title: "Claude for Legal：Anthropic 開源法律 AI 插件集（域別客製化範例）"
tags: [claude-code, CLAUDE.md, 架構設計, skill, domain-specific, 開源, Agent]
date: 2026-05-13
category: 03.科技工具
source: https://github.com/anthropics/claude-for-legal
---

## 這是什麼

Anthropic 官方開源的法律領域 AI 插件集：
- 12 個針對不同法律職位的插件（公司法務、M&A 律師、隱私/AI 治理顧問、訴訟律師、法學院學生）
- 20+ 個與業界常用法律軟件的整合工具

## 冷啟動模式（重要的設計模式）

每個插件需要 10-20 分鐘「冷啟動」：把團隊的 SOP、常用範本、寫作風格寫進 CLAUDE.md。

這樣 Claude 跑任務時自動照團隊規矩輸出，不是罐頭文字。

**這個模式是可複製的設計原則：**

```
領域插件 = 基礎工具 + CLAUDE.md 冷啟動（SOP + 範本 + 風格）
```

任何垂直領域都能套用：法律 → 財務、物流、客服、醫療

## 對派哥的啟示

法律版做的事，派哥的 cc_processor 已經在做了（CLAUDE.md + skill 系統）。

更有趣的是這個開源集的結構啟示：
- **12 個插件對應 12 種職位** → cc_processor 未來可拆成「帳單分析插件」「繳款提醒插件」「Notion 寫入插件」各自獨立
- **冷啟動 CLAUDE.md** → 已有，繼續完善就好
- **Anthropic 官方示範** → 這是學習如何設計高品質 skill 的最佳範本

值得去 repo 看插件結構，學設計模式。

## 行動建議

跳過（法律不是你的領域），但 repo 結構值得花 15 分鐘看，參考 skill 設計方式。

## 連結筆記

- [[agents-md-context-engineering]] — AGENTS.md 冷啟動概念
- [[claude-md-optimization]] — CLAUDE.md 優化
- [[garry-tan-thin-harness-fat-skills]] — 薄 Harness 厚 Skills 設計原則
- [[ai-sop-vs-prompt-skills-ecosystem]] — Skills 生態系
