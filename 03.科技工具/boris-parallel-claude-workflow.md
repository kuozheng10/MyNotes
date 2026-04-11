---
title: Boris Cherny — 並行運行 5-10 個 Claude Code 實例的實戰工作流
tags: [claude-code, 並行, 工作流, boris, 生產力, 必學]
date: 2026-04-11
category: AI工具
source: https://howborisusesclaudecode.com
---

## 核心概念

不是在單一終端操作，而是用**多個終端分頁同時執行獨立任務**。
人類角色從「打字員」轉為「審閱者」。

---

## 如何並行運行 5-10 個實例

- **非同步開發**：一個實例跑長任務（安裝依賴、執行測試、大規模重構）時，切換另一個分頁啟動新任務
- **上下文隔離**：每個實例專注一個獨立子問題，避免單一對話過於臃腫
- **測試驅動驗證**：改完就跑測試，確認無誤才切換任務

---

## 具體工作流程

1. `claude` 啟動，直接給明確目標（如 `implement feature X`）
2. 授權 Claude 自行探索程式碼庫（grep、ls、read）
3. Claude 跑測試自我驗證 → 人類審查結果
4. 同時在其他分頁進行下一個任務

---

## Key Insights

| 洞察 | 說明 |
|------|------|
| **廉價實習生隊伍** | 並行化 = 同時擁有多個 AI 實習生 |
| **不追求一次到位** | 接受 AI 犯錯，並行快速反饋比單線程精雕細琢更有效 |
| **善用 MCP** | 讓 AI 存取外部工具（DB、API），極大化生產力 |

---

## 對派哥的用途

派哥已用 Claude Code 做自動化，升級方向：
- **多 terminal 並行**：同時跑 cc_processor 修 bug + MyNotes 整理
- **不要等一個跑完才開下一個**：切分頁，讓 Claude 各自跑

---

## 連結筆記
- [[boris-15-claude-code-tips]] — Boris 的 15 個 Claude Code 技巧
- [[claude-code-powerup-guide]] — Claude Code 10 大功能
- [[ai-agent-modular-architecture]] — 模組化 AI 架構
