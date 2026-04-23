---
title: Claude Design：Anthropic 補前端設計短板的產品評估
tags: ["工具", "Claude", "設計", "Claude Code", "前端"]
date: 2026-04-24
category: AI工具
source: Telegram 派哥分享
---

## 這是什麼

Anthropic 推出的視覺設計工具，入口 claude.ai/design。
可做 prototype、slide deck、mockup，能讀 GitHub repo 自動抓品牌元素（顏色、字型、logo）。

**重點：輸出的是可跑的 web app，不是靜態圖片。**

## 核心功能

- 選設計類型（prototype / slide / mockup）
- 從 GitHub 拉 codebase 的品牌元素，自動跟現有網站保持一致
- 高保真模式：先問一堆問題（風格、配色、可調元素），類似 Plan Mode，提前找盲點
- UI 直接點選改顏色/大小
- 留 comment 給 Claude（「把這個 globe 做大一點」）
- 畫筆標記說明需求
- 匯出：PowerPoint、PDF、Canva
- 產出指令直接交接給 Claude Code 繼續開發

## 跟現有工具的定位差異

| | Claude Design | Canva | Google Stitch |
|--|--------------|-------|--------------|
| 輸出 | 可跑 web app | 靜態圖 | 待觀察 |
| 整合 Claude Code | ✅ | ❌ | ❌ |
| 讀 codebase 品牌 | ✅ | ❌ | 不確定 |
| 成熟度 | 新，待觀察 | 成熟 | 新 |

更接近 Google AI Studio，而不是 Canva。

## 限制

- 只在 web app（claude.ai）能用，不支援 terminal 或桌面版
- Pro Max 以上方案才有
- 成熟度比 Google Stitch 未知

## 質疑

- 前提假設：「設計跟開發之間的斷層」需要靠這個工具打通，但有多少人真的卡在這個環節？
- 適用邊界：對「已有品牌設計系統」的團隊有幫助；對從零開始的個人，設計品味仍然是瓶頸
- 潛在反例：高保真問卷式流程在緊急需求下太慢，Vibe Coding 直接輸出更快

## 對派哥的啟示

**MWT 目前不需要**：MWT 設計已定，不需要重新做。

**可能有用的場景**：
- 未來做新 side project 時，快速生成品牌一致的 UI mockup
- 做 demo/提案時，比截圖更有說服力的 prototype
- 搭配 Claude Code：設計完直接交接，減少「視覺轉文字再轉 code」的摩擦

**觀察時間點**：等 Pro Max 有機會用到再實測。

## 連結筆記

- [[claude-design-best-practices]] — Anthropic 內部設計師七招（使用技巧）
- [[ai-kill-saas-figma-design-to-code]] — Figma → Code 的大趨勢
- [[huashu-design-claude-design-reverse]] — 化書的 Claude Design 逆向分析
