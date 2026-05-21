---
title: Cline Memory Bank——AI 助手的結構化外部記憶系統
tags: [AI記憶, Cline, Memory Bank, AI工作流, 知識管理, Agent]
date: 2026-05-01
category: AI工具
source: https://docs.cline.bot/features/memory-bank
---

## 這是什麼

Cline（AI 程式開發助手）設計的結構化文件記憶系統，解決 LLM 每次 session 重置的問題。把專案的核心邏輯、架構決策、當前進度存在 Markdown 文件裡，讓 AI 每次開始前快速同步上下文。

---

## 核心文件結構

存放在專案根目錄 `memory-bank/` 下：

| 文件 | 用途 |
|------|------|
| `projectbrief.md` | 專案目標、核心功能、成功定義 |
| `productContext.md` | 為什麼做、解決什麼問題、目標用戶 |
| `systemPatterns.md` | 架構設計、技術模式、代碼結構規範 |
| `techContext.md` | 技術棧、安裝指令、技術限制 |
| `activeContext.md` | **最常更新**：現在做什麼、最近改了什麼、下一步是什麼 |
| `progress.md` | 已完成清單、待辦、未來計畫 |
| `.clinerules` | 特定專案的編碼規則、命名規範 |

## 運作流程

**計畫 → 執行 → 同步** 循環：

1. 進入專案 → 讀取所有 memory-bank 文件
2. 依 `systemPatterns.md` 架構寫程式
3. 完成任務 → 更新 `activeContext.md` 和 `progress.md`
4. 下次 session → 讀文件接續，不需重新解釋

---

## 核心價值

- **省 Token**：只讀精煉文件，不需把所有代碼餵給 AI
- **一致性**：長期開發不偏離架構
- **跨 session 銜接**：隔天重開 = 接續昨天進度

---

## 與現有工具的類比

| Cline Memory Bank | 派哥的系統 |
|------------------|-----------|
| `projectbrief.md` | `CLAUDE.md` 專案說明 |
| `systemPatterns.md` | `CLAUDE.md` 架構規範 |
| `.clinerules` | `CLAUDE.md` 全域規則 |
| `activeContext.md` | 工作日誌 `session-YYYY-MM-DD.md` |
| `progress.md` | 交班單（handover skill） |
| `memory-bank/` 整個目錄 | `~/.claude/projects/.../memory/` |

**結論：概念幾乎一樣，派哥的系統已自然實現這個模式。**

---

## 對一蘭的適用性評估

**部分有用，但不需要完整複製：**

- 一蘭已有：`SOUL.md`（身份）、`MEMORY.md`（長期記憶）、`MANUAL.md`（操作手冊）、每日日誌
- Memory Bank 是針對**程式開發**設計的，一蘭的任務是 TG 助理 + inbox 處理
- 可借鑒的：`activeContext.md` 概念（「現在正在做什麼」），一蘭可在每日日誌加「今日進行中任務」區塊
- 不需要：`systemPatterns.md`、`techContext.md`（這些是 coding 專用的）

---

## 連結筆記

- [[claude-mem-system]] — Claude 記憶系統設計
- [[llm-wiki-v2-memory-mechanism]] — LLM 記憶機制整理
- [[gbrain-garry-tan-memory-system]] — Garry Tan 的 AI 記憶系統
- [[obsidian-ai-agent-skills-guide]] — Obsidian + AI Agent 結合
