---
title: Hermes → qiaomu → NotebookLM 一鍵知識整理流程
tags: ["AI", "知識管理", "工作流程", "Agent"]
date: 2026-04-21
category: 知識管理
source: telegram/save-sop
---

## 這是什麼

三段式自動知識整理流程：Hermes AI Agent 觸發 → qiaomu 轉換內容格式 → NotebookLM 生成思維導圖。解決手動整理資料的痛點，支援 15+ 種內容來源。

## 工具說明

- **Hermes** — AI Agent，接收自然語言指令，觸發整個流程
- **qiaomu（anything-to-notebooklm）** — 內容轉換工具，把各種格式轉成 NotebookLM 可讀的結構
- **NotebookLM** — Google AI 知識庫，生成摘要、思維導圖、問答

## qiaomu 核心能力

支援內容源（15+ 種）：
- 社交與媒體：Twitter、YouTube、Podcast 等
- 網頁（含付費牆繞過，6層層聯技術）
- 電子書與文檔、Office 文檔、其他格式

輸出格式（8種）：Markdown、PDF、思維導圖、音頻概覽等

自然語言觸發（8種類型）：在 Hermes 中直接說「整理這篇文章」「轉成筆記」等

## 質疑

- 前提假設：qiaomu 的付費牆繞過技術有合規爭議，部分網站可能有版權問題
- 適用邊界：NotebookLM 是 Google 服務，資料會上傳 Google；對隱私敏感的內容不適合
- 潛在反例：流程鏈越長，每個環節出錯的機率累加；Hermes → qiaomu → NotebookLM 任一環節掛掉整個流程就停

## 對標

- **CI/CD pipeline**：這個三段流程跟軟體開發的 Source → Build → Deploy 同構——每個階段各司其職，自動串聯
- **ETL pipeline**：Extract（qiaomu 抓內容）→ Transform（格式轉換）→ Load（進 NotebookLM）

## 對派哥的啟示

派哥的 save_article.sh → upgrade_to_mynotes.sh → git push 是同樣的三段流程邏輯。差別是 NotebookLM 多了思維導圖視覺化，MyNotes 多了 cross-link 和質疑/對標步驟。

如果要整合：qiaomu 可以作為 save_article.sh 的前置步驟，先把各種格式（PDF、YouTube、網頁）統一轉成 Markdown，再走現有流程存入 MyNotes。

## 連結筆記

- [[notebooklm-gemini-deep-integration]]
- [[notebooklm-gemini-integration]]
- [[hermes-create-telegram-bot-skill]]
- [[llm-wiki-blog-compilation-three-steps]]
- [[personal-ai-vault-obsidian-system]]
