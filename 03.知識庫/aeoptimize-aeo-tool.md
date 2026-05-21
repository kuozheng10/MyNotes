---
title: aeoptimize — 開源 AEO 工具，讓 AI 正確引用你的內容
tags: [aeo, seo, ai, claude-code, 開源, 工具]
date: 2026-04-11
category: AI工具
source: https://github.com/dexuwang627-cloud/aeoptimize
---

## 這是什麼

**AEO（Answer Engine Optimization）** 開源工具。
不同於 SEO 專注搜尋引擎排名，AEO 旨在提升內容對 AI（ChatGPT、Perplexity、Google AI Overviews）的可讀性與「引用率」。

---

## 主要功能

| 功能 | 說明 |
|------|------|
| **自動化評分** | 17 條規則、50+ 測試，評估 JSON-LD、標題層級、內容密度 |
| **多 AI 共識分析** | `--multi-ai` 調用 Gemini/Copilot 給改進建議 |
| **自動生成資產** | 自動生成 `llms.txt`（AI 爬蟲指引）+ JSON-LD Schema |
| **CI/CD 整合** | GitHub Actions + Pre-commit hooks，分數低於門檻自動攔截 |

---

## 使用方式

```bash
# 即時掃描
npx aeoptimize scan your-site.com

# 安裝 pre-commit hook
npx aeoptimize hook install --min-score 80
```

支援 **Vite / Next.js 插件**，在 build 時自動優化。
與 Claude Code 整合，支援 `/aeo-scan` 指令。

---

## 對派哥的用途

- **My Wallet Trip / 部落格**：若有公開內容希望被 AI 引用，可跑 AEO 掃描
- **目前優先度低**：派哥的工具大多是私有工作流，非公開內容

---

## 連結筆記
- [[claude-code-powerup-guide]] — Claude Code 整合工具
