---
title: Claude × NotebookLM MCP — 五大進階應用情境（三師爸）
tags: [claude, notebooklm, mcp, skill, dispatch, 自動化, 工作流, 必學]
date: 2026-04-10
category: AI工具
source: https://youtu.be/hr6pgjEUFj4
---

## 核心概念

**Claude = 代理人（Agent）　NotebookLM = 知識庫**

透過 Claude MCP 串接 NotebookLM，在單一對話視窗操控多工具，完成複雜多步驟任務。

---

## 五大應用情境（五化）

| 情境 | 說明 | 派哥的用法 |
|------|------|-----------|
| **自動化** | SOP 打包成 Skill，一句觸發多步驟 | 「跑 SOP」→ 自動存 MyNotes + git push |
| **定時化** | 設定時間自動執行（如每週一晨報） | 每日健檢、晨報已設 cron |
| **行動化** | 手機下指令，Dispatch 排隊，電腦端執行 | TG 發指令 → 我執行 |
| **串聯化** | NBLM 內容 → GitHub / Obsidian / Google 試算表 | MyNotes-combined → NBLM → 查詢 |
| **規模化** | 批次處理上百本 NBLM 筆記本 | 整理/清理 NBLM 筆記本 |

---

## 關鍵技巧

### Skill 打包流程
1. 在 Claude Code 環境測試步驟
2. 選取成功的步驟 → `Create Skill`
3. 之後一句指令重複執行複雜任務

### 多工並行
Claude 同步執行多個 MCP 指令，不等一個做完才下一個，持續回報進度。

### Dispatch 調度（行動化關鍵）
- 手機 TG/Claude 輸入指令
- Claude 把任務排入工作隊列
- 電腦端自動執行（即使不在電腦旁）

---

## MCP 管理原則（80/20）

> 只裝最常用的幾個 MCP（如 NotebookLM、GitHub、Obsidian）
> 過多 MCP 佔用 Context Window，影響模型判斷

**建議組合（派哥版）：**
- NotebookLM MCP（知識庫查詢/管理）
- GitHub（MyNotes git 操作）
- 必要時加 Google Drive

### 模型選擇
- Claude 3.5 Sonnet 勝任大部分調度任務
- 不一定要用最高階模型

---

## 超強備課工作流（範例）

說「我要備課」→ Claude 自動：
1. NotebookLM 搜尋最新趨勢
2. 依 Bloom 認知層次生成三難度教材
3. 各難度 10 題測驗 → CSV/JSON → Google 試算表
4. 20 頁教學簡報 → GitHub
5. 6 張 Infographics
6. 影片/音訊總覽

---

## 對派哥的直接應用

1. **已完成的**：MyNotes → Google Drive → NBLM 查詢（週日同步）
2. **下一步可做**：
   - 安裝 NBLM MCP，讓 Claude 直接管理 NBLM 筆記本
   - 打包「跑 SOP + 存 MyNotes」為正式 Skill
   - Dispatch：TG 發 URL → 我在背景執行 SOP → 完成再通知

---

## 連結筆記
- [[notebooklm-gemini-integration]] — NotebookLM × Gemini 整合概覽
- [[gemini-notebooks-feature]] — Gemini Notebooks 功能細節
- [[notebooklm-slides-advanced]] — NotebookLM 生簡報
- [[claude-code-powerup-guide]] — Claude Code 10 大功能
