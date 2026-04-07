---
title: MemPalace — AI Agent 長期記憶架構
tags: [AI, Agent, 記憶管理, RAG, PKM, 向量資料庫]
date: 2026-04-08
category: AI工具
source: https://github.com/milla-jovovich/mempalace
---

## 核心用途

解決 AI Agent「健忘」問題的記憶中間層。讓 AI 能夠：
- **跨 Session 記憶**：保持對使用者偏好、過去決策的記憶
- **語義提取**：將對話自動轉化為結構化「記憶點」
- **按需檢索**：精準從歷史中提取當前相關資訊

## 技術棧

- Python + 向量資料庫（ChromaDB / Qdrant）
- OpenAI API（提取原子記憶用）
- 異步處理（確保記憶寫入不阻塞主流程）

## 核心架構：記憶生命週期

### 記憶原子化
不儲存整段對話，提煉成「Facts」：
> 「使用者喜歡用 Rust 開發」← 這才是一個原子記憶

### 分層儲存
| 層級 | 內容 |
|------|------|
| 短暫記憶 | 當前對話 Context |
| 長期記憶 | 向量 DB 中的 Facts（含時間戳 + 權重） |

### 檢索與重排序
- 查詢向量 ↔ 記憶向量相似度計算
- 根據「時間衰減」+ 「重要性」重新排序

### 記憶更新機制（Reflection）
定期回顧，合併衝突資訊，更新過時數據

## 對派哥的啟示

### 1. 從「收藏」轉向「事實提取」
MyNotes 目前是全文存，未來可考慮：**每篇筆記自動提取 3-5 個原子事實**，放獨立索引。

### 2. 語義檢索 > 關鍵字
現在 MyNotes 靠 grep 找筆記。如果加入 Embedding + 向量搜尋，「忘記關鍵字也能找到」。

### 3. 記憶需要「整合」而非只是「增加」
PKM 系統不應只 Append，要定期 Merge（合併類似筆記）+ Prune（清除過時內容）。
→ 對應「跑健檢」的進化版

### 4. Context 管理才是 AI 工具的核心
> AI 工具的未來不在於模型多大，而在於其 Context 管理能力

這是 OpenClaw / Claude Code 長期記憶設計的方向

## 連結筆記
- [[harness-engineering]] — Agent = Model + Harness，記憶是 Harness 的一部分
- [[obsidian-llm-knowledge-management]] — Obsidian 作為人工版 Memory Palace
- [[openmemory-auto-manager]] — 類似的記憶管理工具
