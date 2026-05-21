---
title: "Vibe Coding 的正確姿勢：設計層不能跳"
tags: [ai-coding, vibe-coding, methodology, architecture, spec, workflow]
date: 2026-04-06
category: 03.科技工具
source: 社群討論（Facebook/Threads）
---

## 核心爭論

**架構師觀點**：Vibe coding = 執行層跳過設計層
- 正常：需求分析 → 架構設計 → 技術選型 → 實作
- Vibe coding：把前三步塞給 AI，你只剩最後一步
- 快速 MVP 有用，長期這樣做像蓋房子不畫施工圖
- 「跳過設計不是罪；跳過設計還以為不需要設計，才是」

**15 年老手觀點**：Vibe coding 不只是寫 code，重點是讓 AI 協助做設計
- 先花大量時間讓 AI 討論、產出 10+ 份規格文件：
  1. 系統架構
  2. 技術選型
  3. User Stories
  4. DB Schema
  5. 資訊安全
  6. 部署選型
- 文件全部設定完才讓 AI 開發
- 結論：Vibe coding 不讓專案失控，關鍵在開始就有施工藍圖

## 兩個觀點的共同結論

> 用 AI 加速的不是「跳過設計」，而是「讓設計變更快、更便宜」。

設計不能省，只是以前要花幾週，現在花幾小時。

## 評估：對派哥有用嗎？

**直接有用。** 你的 CLAUDE.md 裡已有 Feature 開發流程（spec_as_code → test_as_code → implement），本質上就是第二個觀點的實踐。

這兩篇社群文章是對你現有流程的理論支撐：
- 你已經在做對的事
- 遇到有人質疑「為什麼要花時間寫 spec」時，這是最好的回答

## 相關筆記

- [[ai-coding-shift-left]] — 壓力左移法（同樣強調 spec 先行）
- [[SDD-vs-SBE]] — SDD 就是 AI 時代的「施工藍圖」方法
- [[claude-code-feature-workflow]] — 派哥的實作版 Vibe Coding 流程
