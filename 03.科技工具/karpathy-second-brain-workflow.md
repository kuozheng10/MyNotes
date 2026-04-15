---
title: Karpathy 的 AI 第二大腦：使用 Claude Code 與 Obsidian 打造複利知識庫
tags: ["AI", "Claude Code", "知識管理", "工作流程"]
date: 2026-04-15
category: 知識管理
source: goodarticle/2026-04-15_article_20260415_081924.md
---

## 這是什麼
這套系統由 OpenAI 創始成員 Andrej Karpathy 提出，核心概念是利用 Claude Code 自動化維護 Obsidian 知識庫。透過將知識管理從「人工標記」轉向「AI 維護」，實現知識的複利成長與高品質的上下文輸出。

## 核心概念
*   **三層結構化管理**：
    *   **原始素材 (Raw)**：存放未經加工的筆記與資料。
    *   **整理後的知識 (Wiki)**：由 AI 根據素材提煉出的精華頁面。
    *   **規則文件 (Rules)**：告訴 AI 如何管理目錄、標籤、連結與結構的指令集。
*   **AI 驅動維護**：由 Claude Code 負責清理結構、打標籤、建立交叉連結，解決人工維護知識庫容易隨時間崩潰的問題。
*   **關鍵檔案**：
    *   `index.md`：自動生成的全域索引。
    *   `log.md`：記錄所有 AI 對知識庫進行的操作歷史。

## 使用方法 / 快速啟動
1.  **環境準備**：安裝 Obsidian 並設定好 Claude Code 環境。
2.  **建立庫 (Vault)**：在 Obsidian 中新建一個資料夾作為知識庫。
3.  **啟動 AI**：使用終端機進入該資料夾，啟動 `claude` 命令列工具。
4.  **導入規則**：將 [Karpathy 的規則文件](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) 貼給 Claude Code。
5.  **初始化**：指令 Claude Code：「照這套規則幫我把知識庫目錄建好」。
6.  **錄入與迭代**：開始將第一篇素材放入 `raw/`，讓 AI 自動分類、整理並更新 `wiki/` 與索引。

## 對派哥的啟示
*   **AI Agent 的長期記憶**：身為在台灣開發自動化 AI 工具的工程師，這套系統可作為 AI Agent 的「外部大腦」，解決 RAG 應用中數據來源混亂的痛點。
*   **開發流程自動化**：派哥可以將日常的開發日誌、技術方案自動餵入此系統，讓 Claude Code 自動生成技術 Wiki，減少手寫文件的負擔。
*   **在地化知識工程**：利用這套架構管理台灣市場的自動化需求案例，透過 AI 建立跨專案的關聯性，能更快發現重複的需求模式並封裝成新工具。

## 連結筆記
## 連結筆記
- [[boris-15-claude-code-tips]]
- [[claude-code-feature-workflow]]
- [[claude-handover-skill-memory]]
- [[claude-notebooklm-mcp-5scenarios]]
- [[claude-code-powerup-guide]]
