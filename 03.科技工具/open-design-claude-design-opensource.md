---
title: Open-Design：Claude Design 開源替代，直接徵用 Claude Code / Gemini 當設計師
tags: [設計, Claude Code, Gemini, 開源, UI, 工作流程, 自動化]
date: 2026-05-06
category: AI工具
source: https://github.com/nexu-io/open-design
---

## 這是什麼

Claude Design 的開源替代方案。核心理念是 **BYOK（Bring Your Own Agent）**——不內建 AI 大腦，直接徵用你電腦裡現成的 Claude Code、Gemini CLI、Cursor，把它們瞬間變成有設計思維的首席設計師。

解決的問題：Claude Design 閉源、有 token 限制、綁官方生態。Open-Design 在本地跑，資料不離開機器。

---

## 架構（daemon + Web UI）

```
od daemon（本機守護進程）
  ├── 掃描 PATH → 偵測 claude / gemini / cursor CLI
  ├── Agent Adapter Pool → 統一各家輸出格式
  ├── Design System Resolvers → 注入品牌規範到 prompt
  └── Artifact Store → .od/artifacts/ 本地存放所有產出
```

Web UI（localhost:3000）即時渲染 Agent 生成的 HTML/JSX。

---

## 內建資產

| 類型 | 數量 | 舉例 |
|------|------|------|
| 企業設計系統 | 71 套 | Stripe、Vercel、Notion、Linear、Apple、Tesla |
| 核心設計技能 | 19 種 | SaaS Landing Page、Dashboard、Slide Deck、Mobile App |
| 視覺流派 | 5 種 | 極簡現代、粗獷主義... |

**關鍵價值**：設計系統裡有 CSS 變數、配色、字型，注入 prompt 後 AI 產出自帶商業質感，不是廉價套版。

---

## 防偷懶機制（Anti-Shortcut Protocol）

1. 動工前：表單確認受眾、調性、品牌脈絡
2. 交件前：AI 自我五維度評分，不達標打掉重練

---

## 安裝

```bash
# 前置：Node.js 24+ 和 pnpm 10+
git clone https://github.com/nexu-io/open-design.git
cd open-design
corepack enable
pnpm install
pnpm tools-dev run web
# 開 http://localhost:3000，自動偵測你已裝的 claude / gemini CLI
```

---

## 對派哥的應用（一定要用上）

| 場景 | 用法 |
|------|------|
| My Wallet Trip UI | 選 Stripe/Linear 設計系統 + Dashboard skill，讓 Gemini 跑設計稿，Claude Code 實作 |
| SPA 安庫彙總表簡報 | Slide Deck skill + 選商務風格，匯出 PPTX 直接給客戶 |
| 新功能 landing page | SaaS Landing Page skill，直接輸出可部署 HTML |
| 快速 mockup 給派哥確認 | 本地跑 → localhost 預覽 → 滿意了才讓 Claude Code 實作 |

**最佳分工**：Open-Design 跑 Gemini（設計稿）→ 人確認 → Claude Code（實作進 codebase）

---

## 輸出格式

- 靜態 HTML（直接可部署）
- PDF
- 可編輯 PPTX
- MP4 動畫（進階）
- 所有產出存 `.od/artifacts/`，git 友好

---

## 連結參考

- [[claude-design-product-overview]] — Claude Design 官方版比較
- [[claude-design-best-practices]] — Claude Design 七招實戰
- [[awesome-design-systems]] — 設計系統資源
- [[my-wallet-trip-setup]] — My Wallet Trip 專案
