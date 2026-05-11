---
title: "面試必問：「你如何與 AI 協作？」的標準答法"
tags: [claude-code, AI協作, 面試, TDD, subagent, skill, PR, plan-mode, workflow, 職涯]
date: 2026-05-12
category: 03.科技工具
source: Telegram 派哥分享
---

## 核心洞見

「你平常如何與 AI 協作？」是現在不分公司規模必問的一題。

能說出完整流程的人已足夠在面試中脫穎而出——即使對方公司尚未導入 AI 開發。

## 標準答法（四步流程）

**1. PRD → Plan Mode → 實作規格**

把 PRD 給 Claude Code，用 plan mode 反覆討論需求，確保正確理解後：
- 請他提供程式碼拆分方式
- 確認關鍵 function 的片段
- 這段花比較多時間，但確保方向正確

**2. TDD 開發 + 即時回饋**

請 AI 用 TDD 方式開發、自己跑測試驗證。
關鍵：在 plan 階段就讓他寫清楚怎麼測，讓開發有立即回饋。

**3. Subagent 或另開 Session 做 Review**

開發完後換一個 subagent 或另開 session 請 AI review。
目的：避免球員兼裁判（同一個 context 看不出自己的盲點）。

**4. 自訂 Skill 發 PR + 自動處理 Review 建議**

用自己寫的 skill 發 PR → 等 code review bot 留言 → 用另一個 skill 分析哪些建議值得採納 → 和人討論完後自動修改、回覆留言。

## 為什麼這個答法有效

- 展示了完整的 AI 輔助開發流程觀念（不只是「用 AI 寫 code」）
- TDD + subagent review 說明理解 AI 盲點問題
- 自訂 skill 顯示有主動建構個人 AI 工作流的能力

## 相關筆記

- [[hero-framework-senior-interview]] — HERO 框架（面試答題結構）
- [[claude-code-six-slash-commands]] — /plan 使用場景
- [[claude-code-ai-organization-engineering]] — Claude Code = AI OS 概念
- [[ai-sop-vs-prompt-skills-ecosystem]] — Skill 生態系
