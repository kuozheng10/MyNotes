---
title: 創業者 AI 金庫：打造給 LLM 讀的企業維基百科
tags: ["知識管理", "工作流程", "AI", "Obsidian"]
date: 2026-04-17
category: 知識管理
source: goodarticle/2026-04-17_創業者的_AI_金庫.md
---

## 這是什麼
AI Vault 是一個存放在本地端的資料存取結構，本質上是一套專為 AI (LLM) 設計的維基百科（LLM Wiki）。它透過結構化的純文字檔案，讓 AI 能快速理解個人或公司的核心資訊、運作邏輯與專業知識。

## 核心概念
*   **LLM 友善結構**：全數使用 .md 格式，並在檔案開頭加入 YAML frontmatter（包含標籤、日期、分類），方便 AI 進行語義檢索與資料標註。
*   **README 索引系統**：透過核心索引文件引導 AI 快速定位所需資訊，避免 AI 在大量檔案中迷失。
*   **本地優先與版本控管**：結合 Obsidian 的視覺化管理與 GitHub 的版本同步功能，確保資料安全且具備可追溯性。
*   **創業者思維導向**：強調邏輯與架構的清晰度，讓非技術背景的經營者也能建構出讓 AI 高效協作的地基。

## 使用方法 / 快速啟動
1.  **環境架設**：安裝 Obsidian 並建立 Vault，同步安裝 GitHub 桌面版進行版本管理。
2.  **建立入口**：撰寫 `README.md` 作為 AI 讀取金庫的總綱。
3.  **資料結構化**：將現有的公司願景、專案文檔、SOP 存入 .md 檔，並嚴格執行 YAML frontmatter 標註。
4.  **AI 串接**：將金庫路徑提供給具備檔案存取能力的 AI 工具（如 Claude Code 或 OpenClaw），讓 AI 根據金庫內容執行任務。

## 對派哥的啟示
派哥目前在台灣開發多項自動化 AI 工具，此架構可與現有專案深度結合：
*   **整合現有專案文檔**：將目前目錄下的 `cc_processor_spec.md`、`notion_todo_spec.md` 與 `skills/` 資料夾內的技術筆記納入此 Vault 體系，讓 AI 在開發時能隨時參考跨模組的邏輯。
*   **財務自動化知識庫**：針對 `cathay.py`、`hsbc.py` 等模組，建立對應的「台灣金融規格說明書」存於 Vault 中，未來新增銀行模組時，AI 可根據 Vault 內的規範快速生成代碼。
*   **提升 AI Agent 的上下文品質**：將 `daily_briefing.py` 或 `telegram_bot` 的執行邏輯與偏好設定寫成筆記，讓 AI 代理人在執行自動化任務時，更貼近派哥的個人需求與台灣在地使用情境。

## 連結筆記
## 連結筆記
- [[claude-md-optimization]]
- [[boris-parallel-claude-workflow]]
- [[claude-project-management-best-practices]]
- [[claude-notebooklm-mcp-5scenarios]]
- [[claude-handover-skill-memory]]
