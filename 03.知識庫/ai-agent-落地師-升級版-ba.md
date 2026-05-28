---
title: "AI Agent 落地師 = 升級版 BA"
tags: [AI, agent, BA, 職涯, 角色轉型, 流程設計, human-in-the-loop]
date: 2026-05-29
category: 03.知識庫
source: Telegram 派哥分享
---

## 核心洞見

AI Agent 落地師在做的事，其實就是 BA 一直在做的事——只是交付物從文件變成了「會跑的 workflow」。

## AI Agent 落地師做什麼

- 跟 BU 釐清問題
- 拆解現有流程
- 找出重複性任務
- 設計 decision logic
- 設計 human-in-the-loop
- 讓 Agent 真的跑進日常工作

## BA 以前交付的 vs. 現在

| 以前 | 現在 |
|------|------|
| 報表 | 自動生成的 report pipeline |
| 需求文件 | Agent spec / SDD |
| 流程圖 | 實際執行的 AI workflow |

## 對派哥的啟示

派哥用 Claude Code 做的事（cc_processor、insurance_processor、investment dashboard）本質上就是 BA + 落地師的組合：
- 釐清問題：哪些帳單要自動化？
- 拆解流程：Gmail → PDF → Notion → TG
- Decision logic：信任寄件者白名單、金額驗證
- Human-in-the-loop：dry-run 確認後才執行
- 讓 Agent 跑進日常：launchd 排程

## 核心能力轉移路徑

```
BA（流程分析）
  ↓
Prompt Engineer（描述流程給 AI）
  ↓
Agent 落地師（設計 AI workflow）
  ↓
「流程即產品」思維
```

## 關鍵差異

BA 寫的文件需要人去執行，Agent 落地師設計的 workflow 由 AI 自動執行。
但問題定義、流程拆解、edge case 處理——這些仍然是人的工作。

> **AI 不會取代 BA，但會讓懂 AI 的 BA 取代不懂 AI 的 BA。**
