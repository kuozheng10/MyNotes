---
title: PPT Master：可編輯的開源 AI PPT 生成工具
tags: ["AI", "工具", "自動化", "Python"]
date: 2026-04-19
category: AI工具
source: goodarticle/2026-04-18_PPT_Master：開源_AI_PPT.md
---

## 這是什麼
PPT Master 是一款開源的 AI PPT 生成工具，能將 PDF、DOCX 或 Markdown 轉換為真實、可編輯的 PowerPoint 檔案。它解決了多數 AI 工具僅能產出不可修改的圖片或網頁截圖的痛點。

## 核心概念
- **真實元素輸出**：生成的每個物件（文字、形狀、圖表）都是 PowerPoint 原始格式，使用者可以直接點擊並編輯。
- **隱私與本地化**：支援在本地環境運行，配合 Claude Code 等工具處理敏感文件，無需上傳至第三方伺服器。
- **解決實務痛點**：由投行顧問開發，專為需要高頻率、高品質簡報修改的專業人士設計。

## 使用方法 / 快速啟動
1. **下載專案**：`git clone https://github.com/hugohe3/ppt-master`
2. **安裝環境**：`pip install -r requirements.txt`
3. **放置素材**：將 PDF、DOCX 或 Markdown 檔案放入 `projects/` 目錄。
4. **指令生成**：告訴 AI：「請用這個文件生成 PPT」。
5. **獲取成果**：至 `exports/` 目錄下載生成好的 `.pptx` 檔案。

## 對派哥的啟示
- **自動化報表升級**：派哥目前的信用卡消費處理（`cc_processor`）或銷售報告（`sales_report_processor.py`）可以整合此工具，將分析結果直接轉換為可編輯的簡報，提升交付價值。
- **本地化隱私優先**：針對派哥在台灣開發的自動化工具，這類本地運行的 AI 工具非常符合處理敏感財務或個人資訊的安全性需求。
- **模組化 Skill 擴充**：可以將 PPT Master 封裝成一個 `skill`，讓現有的 Telegram Bot 或是自動化流程在產出 Markdown 摘要（如影片摘要或財務總結）後，能一鍵產出對應的簡報檔案。

## 連結筆記
## 連結筆記
- [[claude-routines-automation]]
- [[claude-code-powerup-guide]]
- [[ai-auto-post-facebook-cdp]]
- [[claude-code-feature-workflow]]
- [[ai-agent-modular-architecture]]
