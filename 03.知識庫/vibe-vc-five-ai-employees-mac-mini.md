---
title: "Vibe VC #6：在 Mac Mini 上跑 5 個 AI 員工"
tags: [multi-agent, claude-code, automation, 架構設計, harness, 個人AI, Mac-Mini, 工作流程]
date: 2026-05-13
category: 03.科技工具
source: Vibe VC newsletter #6
---

## 核心架構

5 個 AI 員工，每人一個角色，跑在同一台 Mac Mini：

| 員工 | 角色 |
|------|------|
| Jared | EA（行政助理）|
| Bobby | VC analyst |
| Taylor | Investment |
| Steve | PM |
| Samantha | Content |

**每個員工的設定框架：Goal → Context → Skills → Actions**

這是可複製的結構，不是角色扮演，而是定義工作邊界。

## 技術架構

- **執行環境**：Mac Mini（本地跑，不上雲）
- **心跳排程**：4 小時一次 cron job（從 2 小時調整而來）
- **共享基礎設施**：
  - Notion shared dashboard（任務看板）
  - Shared skill repo（技能庫共用）
  - Shared knowledge base

**瓶頸是人類節奏，不是 AI 速度。** 4 小時心跳是因為人類處理 output 的速度，不是 AI 跑不動。

## 權限設計

| 帳號類型 | 權限 |
|---------|------|
| 個人 Google 帳號 | Read-only（AI 只能看，不能改） |
| Shared agent 帳號 | Read/Write（AI 執行任務）|

這是最小權限原則的落地實作，個人資料保護同時讓 agent 能動。

## 為什麼要多 Agent 而不是單一 Agent

1. **平行吞吐量**：5 個同時跑，不用排隊
2. **乾淨的 log**：每個 agent 有自己的 log，不混在一起
3. **共用 skill repo + task board + knowledge base**：協作不互相干擾

## Self-reflection 機制

每日 20:00 自我反思，agents 更新自己的 config。  
這是讓系統自我進化的關鍵，不是靜態設定。

## 資訊密度原則

輸出格式：**結論 + 下一步行動 + 3 個選項 + 關鍵數字**

這是每個 agent output 的標準格式，讓人類能快速決策。

## 對派哥的啟示

cc_processor 已有這個架構的雛形（BankAdapter 多 adapter 並行），但還差一步：

**可以做的事**：
- 把 cc_processor 的每個 adapter 視為獨立「員工」，各自有獨立 log
- 加入每月 self-reflection：執行後輸出「本月錯誤/成功率 + 下次調整建議」寫進 Notion
- 4 小時心跳的設計可以參考：cc_processor 目前每天 09:00 跑一次，可以試驗「多時段輕量掃描」

更大的啟示是**授權結構**：  
read-only vs read/write 的帳號分離，cc_processor 目前都是 read/write，有機會拆得更細。

## 連結筆記

- [[multi-agent-team-24h-codex-claude-architecture]] — 多 agent 24h 開發架構
- [[full-agent-dev-ecosystem-goatwang]] — 完整 AI agent 開發生態系
- [[harness-engineering]] — Harness Engineering 核心概念
- [[garry-tan-thin-harness-fat-skills]] — 薄 Harness 厚 Skills
- [[claude-routines-automation]] — Claude Code 排程自動化
