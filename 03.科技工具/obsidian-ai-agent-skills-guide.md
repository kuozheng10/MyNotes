---
title: Obsidian × AI Agent — 必裝 Skills 與避坑指南
tags: [obsidian, openclaw, skill, defuddle, mermaid, excalidraw, 知識管理, 必學]
date: 2026-04-11
category: AI工具
source: https://youtu.be/ivApMNUlmWg
---

## 核心原則

> 「Skill 不能亂裝」— 裝錯 Skill 會狂耗 Token，知識庫效率反而更差。

---

## ❌ 避坑

### 不要用 OpenClaw 官方庫的舊版 Obsidian Skill
- 只做底層讀寫，**狂耗 Token**
- 改裝 **官方正版 obsidian CLI**（最低 token 消耗）

---

## ✅ 必裝

### 1. defuddle（神級剪藏）
- 網頁 + YouTube 剪藏工具
- **免設定 Cookie** 即可精準轉錄圖文與影片精華
- 目前派哥的 summarize_url.sh 用 Gemini CLI 抓，可評估是否換 defuddle

### 2. Obsidian Markdown Skill（排版禁忌設定）
AI 常有「格式幻覺」，把你的排版規則寫進 Skill：
```
禁用規則：
- 禁用一級標題（# H1）→ 改用 H2 開始
- 拒絕過度縮排（超過 2 層的列表）
- 不加多餘的粗體強調
```
→ 產出筆記可直接發文，不用再修格式

### 3. 視覺化三劍客（Axton 優化版）
捨棄官方白板工具，改用 AI 博主 Axton 的版本：

| 工具 | 用途 | 解決問題 |
|------|------|----------|
| **json-canvas** | 心智圖 / 白板 | 文字溢出問題 |
| **Mermaid** | 流程圖 / 架構圖 | 圖形精準對齊 |
| **Excalidraw** | 手繪風示意圖 | 自由排版 |

---

## 對派哥的直接應用

| 現狀 | 可改進 |
|------|--------|
| 用 obsidian-llm-knowledge-management Skill | 評估換 obsidian CLI（省 token） |
| summarize_url.sh 用 Gemini 抓網頁 | 評估加入 defuddle 提升品質 |
| MyNotes 無視覺化 | 加 Mermaid 生成概念地圖（健檢時） |
| AI 生成 md 排版不一致 | 在 CLAUDE.md 加 Markdown 排版規則 |

---

## 連結筆記
- [[obsidian-llm-knowledge-management]] — Obsidian × LLM 知識管理
- [[vault-search-obsidian-plugin]] — Obsidian Vault Search
- [[claude-token-saving-tips]] — Claude 省 token 策略
- [[toonify-mcp-token-compress]] — Token 壓縮工具
