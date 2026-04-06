---
title: "UI-UX-Pro-Max：Claude Code 設計系統 Skill"
tags: [claude-code, skill, ui-ux, design-system, 色彩, 字型, tailwind]
date: 2026-04-02
category: 03.科技工具
source: Facebook + GitHub
---

## 是什麼

Claude Code 的設計智慧 Skill，在動手寫 code 前，先根據產品類型自動產出完整設計系統。

GitHub：https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

## 資料庫規模

| 資料 | 數量 |
|------|------|
| 行業推理規則 | 161 條 |
| UI 風格 | 67 種 |
| 色彩方案 | 161 套 |
| 字型搭配 | 57 組 |
| UX 最佳實踐 | 99 條 |

## 輸出範例

給 prompt：「Build a landing page for my beauty spa」

自動產出：
- **Pattern**：Hero-Centric + Social Proof
- **Style**：Soft UI Evolution
- **Colors**：Soft Pink / Sage Green / Gold accent
- **Typography**：Cormorant Garamond / Montserrat
- **Anti-patterns**：禁用亮色 neon、hard animation、dark mode
- **Pre-delivery checklist**：對比度、hover 動畫、無障礙等

## 安裝方式

### Claude Code Marketplace（最快）
```
/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill
/plugin install ui-ux-pro-max@ui-ux-pro-max-skill
```

### npm CLI（全域安裝）
```bash
npm install -g uipro-cli
uipro init --ai claude --global   # 安裝到 ~/.claude/skills/
```

## 適用情境

- 新專案選色、選風格不知從何下手
- 想讓所有頁面維持一致設計規範
- 快速驗證某個產品類型適合什麼 UI style

## 支援技術棧

React / Next.js / shadcn/ui / Vue / Nuxt / Angular / Svelte / Astro / SwiftUI / Flutter / React Native

## 進階：持久化設計系統

```bash
# 產出設計系統並存到 design-system/MASTER.md
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "SaaS dashboard" --design-system --persist -p "MyApp"
```

後續在每頁 prompt：
```
I am building the [Page Name] page. Please read design-system/MASTER.md.
Also check if design-system/pages/[page-name].md exists.
```

## 相關

- [[boris-15-claude-code-tips]]
- [[claude-hidden-combo]]
- [[MiniMax-AI-skills]]
