---
title: autoskills：把 Skill 當 Package 管理的基礎設施
tags: ["Claude Code", "Skill", "工具", "自動化", "架構設計"]
date: 2026-04-23
category: AI工具
source: https://github.com/midudev/autoskills
---

## 這是什麼

CLI 工具，掃你的 codebase，自動偵測 tech stack，安裝對應 AI agent skills，並生成 CLAUDE.md。

```bash
npx autoskills
# 需要 Node.js >= 22
```

「One command. Your entire AI skill stack. Installed.」

## 運作機制（4步）

1. 在專案根目錄執行
2. 掃 `package.json`、Gradle、config 檔案偵測 tech stack
3. 從 skills.sh 匹配並安裝對應 skills
4. 生成 CLAUDE.md（偵測到 Claude Code 時）

## 支援偵測的 Tech Stack

- Frontend：React、Next.js、Vue、Nuxt、Svelte、Angular、Astro、Tailwind、shadcn/ui
- Runtime：TypeScript、Node.js、Go、Bun、Deno、Dart
- Backend：Express、Hono、NestJS、Spring Boot
- Mobile/Desktop：Expo、React Native、Flutter、SwiftUI、Tauri、Electron
- Data：Supabase、Neon、Prisma、Drizzle、Zod
- Cloud：Vercel、Cloudflare、AWS、Azure、Terraform
- Testing：Vitest、Playwright、Turborepo、Vite

## 核心洞見（派哥的觀察）

AI coding 的下一步不是再多一個 model，而是把 skill distribution 做成真的 infrastructure。

當 skill 開始像 package 一樣被管理：
- 可安裝（npx install）
- 可同步（版本更新）
- 可複用（跨專案）
- 自動生成 agent context（CLAUDE.md）

原本靠人手維護的 agent context 變成 dependency，AI 開發工具才真的進入工程化。

## 質疑

- 前提假設：自動偵測的 skill 是否真的適合這個專案？Next.js skill 裝了不代表懂你的 Next.js 專案的特殊架構決策
- 適用邊界：對通用 tech stack 效果好；對高度客製化的 codebase（如派哥的多腳本系統），自動偵測可能裝一堆不相關的 skill
- 潛在反例：skills.sh 上的 skill 品質參差不齊，autoskills 批量安裝等於批量擴大了攻擊面（搭配上一篇的安全掃描 SOP 更重要）

## 對標

- **npm install vs 手動下載 JS 檔**：autoskills 對 skills 的關係，就是 npm 對 JS 套件的關係——依賴管理讓生態系才能成熟
- **Homebrew**：一個指令裝好一整套工具的 Unix 傳統，autoskills 是 AI agent 版的 Homebrew

## 對派哥的啟示

派哥目前的 skills 是手動管理的（~/.claude/skills/），沒有版本控制、沒有依賴追蹤。

autoskills 的模式值得借鑑，但直接用它的問題：
- MyClaude 是 Python/bash 腳本為主，不是典型的 JS 專案
- 派哥的 skills 大多是客製化的（handover、mynotes、cc-processor），不在 skills.sh 上

更實際的做法：
- 用 autoskills 在 My Wallet Trip（Next.js + Tailwind + Vercel）上試試——這個專案 tech stack 正好是 autoskills 的甜蜜點
- 把派哥的客製 skills 貢獻到 skills.sh，讓 autoskills 能找到

## 連結筆記

- [[skill-mcp-security-check]]
- [[agency-agents-applicable-analysis]]
- [[garry-tan-thin-harness-fat-skills]]
- [[claude-md-optimization]]
- [[karpathy-skills-claude-coding-rules]]
