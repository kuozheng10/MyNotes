---
title: "Karpathy：要求 LLM 輸出 HTML，把回答變成工具"
tags: [LLM, prompt, HTML, 工作流程, 可視化, karpathy, productivity]
date: 2026-05-13
category: 03.科技工具
source: https://x.com/i/status/2053872850101285137
---

## 核心洞見

> HTML 是資訊傳遞的「十線道超級高速公路」。比起純文字或 Markdown，HTML 讓 AI 的回答從「一段話」變成「功能性工具」。

人類輸入偏好語音，但輸出消費效率：圖像/HTML >> Markdown >> 純文字。

## AI 輸出演化四階段

1. 純文字 — 閱讀費力
2. Markdown — 目前主流，仍受限
3. **HTML（現在可做）** — 含圖形、複雜佈局、互動元素（滑桿、按鈕）
4. 互動式神經網路影片 — 未來趨勢

## 實用操作

在 prompt 末尾加：
```
structure your response as HTML
```
把輸出存成 `.html`，用瀏覽器開，就得到一個功能性的儀表板或工具。

## 對派哥的啟示

Gemini CLI 分析結果、月報、SPA 安庫彙總說明，都可以要求輸出 HTML 檢視。

例如：
- 每月 cc_processor 帳單分析 → 存 HTML，瀏覽器開比看 terminal 清楚
- 複雜資料查詢結果（Twinkle Hub）→ 要求 HTML 表格輸出

加一句話，輸出品質大幅提升。

## 連結筆記

- [[karpathy-second-brain-workflow]] — Karpathy 第二大腦工作流
- [[karpathy-skills-claude-coding-rules]] — Karpathy 的 Claude coding rules
