---
title: open-slide：Codex 內直接生簡報（gpt-image-2 + browser-use）
tags: [工具, 自動化, AI, 工作流程]
date: 2026-05-19
category: AI工具
source: https://github.com/1weiho/open-slide
---

## 這是什麼

open-slide 是一個接在 Codex 裡的簡報生成工具，prompt → 簡報，全程不離開 Codex 環境。

- 官網：https://open-slide.dev
- GitHub：https://github.com/1weiho/open-slide

---

## 核心概念 / 架構

整合四個能力在一個流程：

| 能力 | 說明 |
|------|------|
| `gpt-image-2` | 一鍵生成配圖 |
| 網路撈素材 | 自動抓參考資料 |
| `browser-use` | 逐頁視覺檢查 |
| Codex 內預覽 | 成品不用切視窗 |

Codex 的 browser-use 讓 AI 能「看」簡報成品逐頁審查，不只是生出來就算，還能自動回饋修正。

---

## 使用方法 / 快速啟動

```bash
# 在 Codex 環境內安裝
# 詳細步驟見 https://open-slide.dev

# 使用方式：在 Codex 輸入 prompt
# 例：「幫我做一份關於 AI Agent 架構的 10 頁簡報，商務風格」
```

---

## 對派哥的啟示

- 目前用 guizang-ppt-skill（HTML 雜誌風）和 PPT Master（可編輯 .pptx）
- open-slide 的差異：**在 Codex 裡跑**，不用另開工具，適合要在 agentic 流程裡自動產簡報的場景
- gpt-image-2 配圖 + browser-use 視覺審查 = 更接近「AI 自主完成一份簡報」
- 適合場景：銷售報告、提案、定期產出的格式化簡報

---

## 連結筆記

- [[guizang-ppt-skill]] — HTML 雜誌風 PPT，Claude Code Skill
- [[ppt-master-ai-ppt]] — 可編輯 .pptx 輸出，Python 工具
- [[codex-gpt-image2-skill-workflow]] — Codex + gpt-image-2 圖像生成流程
