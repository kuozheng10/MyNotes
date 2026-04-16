---
title: 一人 SaaS 的反叛：用 20 美元架構撐起月入萬金的產品
tags: ["架構設計", "自動化", "LLM", "工具"]
date: 2026-04-17
category: 系統架構
source: goodarticle/2026-04-16_一人SaaS的反叛.md
---

## 這是什麼
這篇文章講述了 Steve Hanov 如何以極低成本（每月約 20 美元）運營多個營收破萬美元的 SaaS 產品。他透過選擇高效率、低認知負擔的工具（如 Go、SQLite 和本地 GPU），挑戰了矽谷追求高額融資與複雜架構的傳統思維。

## 核心概念
- **低認知負擔的技術棧**：選擇 Go 語言而非 Rust，因為 Go 與 AI 協作（LLM 生成程式碼）的錯誤率更低且編譯極快。
- **資料庫簡約化**：使用 SQLite 搭配 WAL 模式，省去運維 Postgres 等獨立資料庫服務器的複雜性與成本。
- **硬體資產化**：利用二手 RTX 3090 跑本地 VLLM 進行批次 AI 推理，將昂貴的 API 呼叫轉為一次性投資。
- **AI 友善的架構**：選擇 LLM 擅長生成的程式語言和簡單的 Binary 部署方式，最大化一人開發的產能。

## 使用方法 / 快速啟動
- **後端開發**：採用 Go 語言，將應用程式編譯為單一 Binary 檔案。
- **伺服器部署**：租用 5-10 美元的 VPS（如 Linode 或 DigitalOcean），使用 scp 直接上傳部署。
- **資料處理**：開啟 SQLite 的 WAL (Write-Ahead Logging) 模式以應對高併發讀寫。
- **AI 推理**：若有大量重複性分析任務，考慮部署本地模型（OpenRouter 作為備援）。

## 對派哥的啟示
- **優化現有自動化流程**：派哥在台灣開發的 `cc_processor`（信用卡處理）與 `sales_report_processor` 可借鏡此架構。若處理量大，可考慮將 OCR 或分類邏輯從 API 轉向本地輕量模型以節省成本。
- **維持工具的「AI 寫作親和力」**：目前專案多使用 Python，這與 Go 同樣屬於 LLM 支援度極高的語言。在擴展 Telegram Bot 功能時，應保持程式碼結構清晰，讓 Claude Code 能更精準地進行重構。
- **技術架構減法**：在整合 Cathay 或 HSBC 帳單自動化時，優先考慮 SQLite 作為本地快取或資料庫，避免引入不必要的雲端資料庫維護成本，維持「一人工具」的高機動性。

## 連結筆記
## 連結筆記
- [[ai-agent-modular-architecture]]
- [[ai-agent-system-design-over-prompt]]
- [[claude-routines-automation]]
- [[agent-skills-standard]]
- [[full-agent-dev-ecosystem-goatwang]]
