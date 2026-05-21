---
title: NotebookLM × Gemini 深度整合 — 研究與產出終於在同一個視窗
tags: [notebooklm, gemini, 工作流, 知識管理, 整合, 必學]
date: 2026-04-11
category: AI工具
---

## 最大改變

NotebookLM notebooks 直接「搬進」Gemini 聊天室。
研究（NotebookLM 讀書）+ 產出（Gemini 生成）合為一條 workflow，不再需要剪貼搬運。

---

## 三大功能升級

### 1. Notebooks 在 Gemini 裡直接掛載

以前流程（斷點）：
```
NotebookLM 讀資料 → 整理重點 → 複製貼上 → 另開 AI 工具 → 重新給 context → 產出
```

現在流程（一條線）：
```
Gemini 對話裡說：「用 notebook X 幫我寫一封投資人 email」→ 直接產出
```

### 2. 跨多個 Notebooks 推理

以前：每個 notebook 完全隔離，無法跨本分析

現在：
```
「同時參照 A（市場研究）+ B（財報）+ C（技術規格），
 幫我整理一份完整策略建議。」
```
舊專案不再是孤立資料箱，而是可以隨時跨本串聯的「hub 大腦」。

### 3. NotebookLM 從一次性工具 → 長期 Project Space

- 可以過幾週回來繼續追問、補資料
- Gemini 能連網 → 舊研究可對照最新資訊更新
- 「用這個 notebook，幫我對照這個月最新的市場變化。」

---

## 使用建議

### 殭屍 Notebooks 喚醒策略
帳號裡沉睡的舊 notebooks，現在值得重新組織：
1. 打開舊 notebook
2. 在 Gemini 說「用這個 notebook 幫我重新整理/更新 X」
3. 讓舊研究作為新任務的基底

### Claude vs Gemini+NBLM 分工
| 任務 | 工具 |
|------|------|
| 長篇 PDF 讀書、摘要 | Gemini + NotebookLM |
| 製作 Podcast / Slides | NotebookLM 原生功能 |
| 程式碼、SOP、自動化 | Claude Code |
| 一般問答、快速任務 | Claude |

---

## 對派哥的直接應用

派哥的 MyNotes 已定期 sync 到 Google Drive → NotebookLM，現在可以：
- 在 Gemini 聊天裡直接問 MyNotes 內容
- 跨 notebook 推理（科技筆記 + 其他專案）
- 讓「MyNotes 知識庫」notebook 配合 Gemini 連網，隨時補充最新資訊

---

## 連結筆記
- [[notebooklm-gemini-integration]] — NotebookLM × Gemini 整合概覽（舊版）
- [[gemini-notebooks-feature]] — Gemini Notebooks 功能（per-notebook Instructions）
- [[claude-notebooklm-mcp-5scenarios]] — Claude × NotebookLM MCP 五大情境
