---
title: NanoBanana MCP — Claude Code 直接呼叫 Gemini 生圖，含 ig-carousel skill
tags: [MCP, Gemini, 圖像生成, claude-code, ig-carousel, 自動化, 社群行銷]
date: 2026-04-28
category: AI工具
---

## 這是什麼

MCP server，把 Google Gemini 圖片生成接進 Claude Code。
不開瀏覽器、不另外登入、不離開終端機，直接生圖。

---

## 安裝（一行）

```bash
claude mcp add nanobanana-mcp -- npx -y @ycse/nanobanana-mcp -e GOOGLE_AI_API_KEY=你的KEY
```

API key 在 http://aistudio.google.com 申請，有免費額度，個人用量夠。

---

## 裝完後新增工具

| 工具 | 用途 |
|------|------|
| `set_aspect_ratio` | 設定圖片比例 |
| `set_model` | 切 flash（快）或 pro（精細）|
| `gemini_generate_image` | 生圖 |
| `gemini_edit_image` | 改圖 |
| `gemini_chat` | 多輪對話微調（「顏色再深一點」）|

---

## Prompt 公式

**主體 + 風格 + 構圖 + 色彩**

範例：
```
科技綠暗底，電路板背景，大標題白字，品牌標籤左上角
```
→ Claude Code 自動翻成英文 prompt（Gemini 對英文品質更好）

**重要**：圖裡的文字常出錯，不要塞太多精確文字。標題 + 一段副文就好。

Prompt 靈感庫：awesome-nano-banana-pro-prompts（12000+ 模板，按風格分類）

---

## /ig-carousel skill（開源中）

作者自製的 IG 輪播圖生成 skill，自動化整個流程：

```
/ig-carousel Claude Code 教學 — 科技綠暗底
```

自動執行：
1. 設定 1:1 比例
2. 中文描述翻英文 prompt
3. 套品牌排版（標籤、簽名位置）
4. 清除 C2PA metadata（防止 IG 貼「Made with AI」標籤）

---

## 適用場景

✅ 適合：
- 快速出圖、風格一致的系列圖
- 每天發文但沒時間開設計軟體
- 48 天連發這種固定節奏內容

❌ 不適合：
- 像素級精準排版
- 品牌設計稿
- 圖裡有大量精確文字

核心原則：**夠用、夠快，但不完美**——發文節奏比完美重要

---

## vs 其他工具

| 工具 | 優勢 | 劣勢 |
|------|------|------|
| NanoBanana MCP（Gemini）| 終端機內完成，免費額度 | 文字精準度差 |
| Codex + GPT Image-2 | 繁中文字精準、印刷級 | 需要等 10 分鐘、有費用 |
| HTML 排版 + Playwright | 文字完全精準 | 4 個工具來回 |

混合做法（正在研究）：HTML 排版文字 + AI 生背景圖 → 精準度 + 美感兼顧

---

## 對派哥的意義

- **現在可裝**：Claude Code 已有 MCP 支援，一行指令裝好
- **Gemini 免費額度**：每天發文夠用
- **與 image2-carousel 的差異**：這個更快（即時）但文字品質較差；image2-carousel 品質更好但要等

---

## 連結筆記

- [[codex-image2-claude-carousel-workflow]] — Codex + GPT Image-2 輪播圖（高品質版）
- [[awesome-gpt-image2-prompts]] — GPT Image-2 prompt 資源庫
- [[anthropic-mcp-production-patterns]] — MCP 生產環境使用模式
