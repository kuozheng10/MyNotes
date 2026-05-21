---
title: "Architecture Diagram Generator：AI Skill 自動產 HTML 架構圖"
tags: [claude-code, skill, architecture-diagram, html, reverse-engineering]
date: 2026-04-14
category: AI工具
source: https://github.com/samjhill/diagrammer
---

## 是什麼

Claude Code skill，用白話描述或直接丟 code，自動產出系統架構圖。輸出為**獨立 HTML**，瀏覽器打開即看，支援對話方式反覆修改。

## 安裝方式

skill（非 plugin），複製到 `~/.claude/skills/` 即可使用，不需要 `claude plugin install`。

## 用途

- 系統設計草稿
- 舊系統 reverse engineering（丟 code 分析）
- 技術文件視覺化
- 描述 components / 資料流 / 相依關係 → 生圖

## 特點

輸出不是死圖，是可互動的 HTML，可繼續對話修改。適合 PM 跟架構師快速出圖。
