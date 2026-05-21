---
title: "Codex OpenAI Developers Plugin：AI 產品代工廠模式"
tags: [AI, 工具, 工作流程, 架構設計, 自動化]
date: 2026-05-13
category: AI工具
source: Telegram 派哥分享
---

## 這是什麼

OpenAI 推出 OpenAI Developers plugin for Codex，讓 Codex 從「寫 code 的工具」進化為「做產品的代工廠」。

一句訂單描述需求 → Codex 自動申請 API key、設定環境、選模型、寫前後端、生成圖片、產出文件，全部一條龍。

**官方 demo（32 秒）**：
> 「Use @OpenAI Developers and @Frontend App Builder to make a product ad studio that uses GPT-5.5 and GPT Image 2 to generate ads from product photos」

交出：9 個檔案、1389 行 code、Vite+React+Express full-stack、GPT Image 2 廣告草圖、README、桌面/手機截圖。

## 核心改變：SDLC 全產線化

| 過去的流程 | 代工廠模式 |
|-----------|-----------|
| 開瀏覽器登 platform、點 Create key、複製貼 .env | Codex 自動建 project key、寫 .env、驗證但不打印 key |
| 查 docs 確認 env 變數、手動 wire | Codex 按專案慣例自動 wire |
| 自己 init React+Vite、配 Express、寫 API 呼叫 | 一句話拿到 1389 行可跑的 full-stack |
| 另開 image API、自己寫 prompt 跑圖 | GPT Image 2 同一產線產出所有資產 |
| rate limit 要回 dashboard 對日誌 | Codex 內建診斷直接給下一步 |

## @ Plugin 介面

- 一句訂單可以同時 tag 多個 plugin（`@OpenAI Developers`、`@Frontend App Builder`）
- Codex 在 marketplace 把 OpenAI 自家 API 跟 Vercel、Notion、Figma 平起平坐 → **中立 marketplace 定位，不是 OpenAI 專用 IDE**

## 這週 OpenAI 連發六發（5/7–5/13）

| 日期 | 發布 | 意義 |
|------|------|------|
| 5/7 | Chrome plugin | 代工廠業務窗口開到瀏覽器 |
| 5/7 | GPT-Realtime-2 / Translate / Whisper | 語音產線上線，context 32K→128K |
| 5/11 | Daybreak | 代工廠切第一個垂直行業：資安 |
| 5/12 | Standup ticket demo | PM workflow 接管（674K views）|
| 5/12 | OpenAI Developers plugin（本文）| 下訂單做產品 |
| 5/13 | Symphony | 每個 task 自動配一隻 agent，多條產線並行 |

主軸：把 dev 在 dashboard、瀏覽器、PM 工具、IDE 之間反覆橫跳的時間全部吃進 Codex 一個介面。

## 限制

- 需要 Codex 桌面 App 或 CLI，網頁版 ChatGPT 沒有
- 建 key 預設進 Default Org，要分專案管 key 需先在 platform.openai.com 設好
- Computer Use 部分仍 macOS 限定，EU/UK 慢一波

## 對派哥的啟示

代工廠模式對派哥的實際影響：

- **Sales report 新功能**：下一次要加新圖表或新欄位，可以試試一句 prompt 丟給 Codex OpenAI Developers plugin 生，而不是手寫 boilerplate
- **My Wallet Trip 後端**：下個版本的 API 擴展可以用代工廠模式快速起版，再交給 Claude Code 精修
- **旗幟意義**：過去「會寫 code」是進入門檻，代工廠模式之後門檻是「能描述清楚需求」，SDD（Spec Driven Development）的重要性更高

Symphony（多 agent 並行）是目前最值得追的發展——對應 cc_processor 的多 adapter 並行架構，OpenAI 也在往同方向走。

## 連結筆記

- [[codex-plugin-cc]] — Codex Plugin for Claude Code（review/rescue 功能）
- [[codex-chrome-browser-plugin]] — Codex 瀏覽器延伸（5/7 同週發布）
- [[vibe-vc-five-ai-employees-mac-mini]] — 多 agent 並行架構（Symphony 對應概念）
- [[claude-code-ai-dev-team-design]] — 4 層 AI 開發團隊（對應 Codex 的代工廠層次）
- [[SDD-vs-SBE]] — Spec Driven Development（需求描述能力更重要）
