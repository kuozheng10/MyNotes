---
title: Next AI Draw.io — 自然語言畫流程圖神器
tags: [ai-tool, diagram, drawio, mcp, open-source, architecture, flowchart]
source: 社群文章（2026-06）
date: 2026-06-08
github: https://github.com/draw-it-for-me/draw-it-for-me (示意，需確認實際 repo)
stars: 30,800
---

# Next AI Draw.io — 自然語言畫流程圖神器

> 用聊天的方式畫流程圖：說幾個字，架構圖自動生成。

---

## 核心功能

| 功能 | 說明 |
|-----|------|
| 自然語言生圖 | 描述需求 → 自動產出流程圖、架構圖、心智圖 |
| 圖片轉可編輯 | 上傳截圖 → AI 重建成可編輯版本 |
| 文件 / PDF 轉圖 | 丟文件 → 自動抓重點畫成圖表 |
| 版本歷史 | 每次 AI 修改都有紀錄，可回滾 |
| 多模型支援 | Claude、GPT、Gemini、DeepSeek |
| MCP 整合 | 在 Claude Code / Cursor / VS Code 直接叫 AI 畫圖 |
| 自部署 | Docker 或 Vercel 一鍵部署 |

---

## 對派哥的應用場景

1. **系統架構圖** — 直接描述 cc_processor / investment 的架構，生成圖給文件用
2. **流程圖** — SOP / SDD 寫作時，用語言描述流程 → 自動畫出
3. **MCP 串接** — 若有 MCP server，可在 Claude Code session 裡直接叫它畫圖（比 /graphify 更視覺化）

---

## 推薦用途

- **雲端架構圖** → 用 Claude 畫（有訓練過 AWS/Azure/GCP 圖標）
- **流程圖複製** → 截圖丟入，AI 重建可編輯版本
- **開會報告** → 丟文件讓 AI 自動整理成圖

---

## vs 現有工具比較

| 工具 | 用途 | 差異 |
|-----|------|------|
| /graphify | 知識圖譜（概念連結） | 偏分析，輸出 Obsidian 格式 |
| Next AI Draw | 流程圖 / 架構圖 | 偏視覺輸出，適合簡報/文件 |
| Mermaid | Code 生圖 | 不支援拖拉編輯 |

---

## 連結筆記
- [[graphify]] — 現有知識圖譜 skill
- [[addyosmani-agent-skills]] — agent workflow 視覺化
