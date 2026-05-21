---
title: "hermes-hudui：Hermes Agent 瀏覽器監控面板"
tags: [hermes-agent, web-ui, monitoring, token-cost, dashboard]
date: 2026-04-14
category: AI工具
source: https://github.com/joeynyc/hermes-hudui
---

## 是什麼

Hermes Agent 的瀏覽器版可視化監控面板，`http://localhost:3001`，讀 `~/.hermes/` 資料。

之前有 TUI（終端介面）版本，這個是瀏覽器版，兩個可以同時跑。

## 面板內容

- Identity：Agent 運行天數、大腦大小
- Memory：記憶容量、使用者畫像、被糾正次數
- Token Costs：每個模型每天燒多少錢（帶趨勢圖）
- Skills：最近修改的技能，分類展示
- Cron Jobs：背景自動執行的任務狀態
- Growth Delta：快照對比，看 Agent 今天學了什麼

## 主題

4 套：Neural Awakening / Blade Runner / fsociety / Anime，含 CRT 掃描線特效。

## 評估

適合重度 Hermes 用戶監控 token 成本。如果派哥之後加大 Hermes 使用量，可以用這個追蹤消耗。目前主力是 Claude Code，先記錄備用。
