---
title: "Impeccable：消除 AI 設計味的 Claude Code Skill"
tags: [claude-code, skill, ui-ux, design, anti-pattern, 設計審查]
date: 2026-04-02
category: 03.科技工具
source: Facebook + impeccable.style
---

## 是什麼

針對「UI 寫完但看起來像 AI 做的」問題，提供 20 個設計指令，讓你針對特定問題各個擊破。

官網：https://impeccable.style
GitHub：https://github.com/pbakaus/impeccable

Anthropic 官方有 `frontend-design` skill，Impeccable 是加強版：
- 7 個領域參考文件（字型、色彩、空間、動態、互動、RWD、UX 文案）
- 20 個 slash command
- 明確列出 anti-patterns（告訴 AI 不要做什麼）

## 20 個指令

| 指令 | 用途 |
|------|------|
| `/audit` | 技術品質檢查（a11y、效能、RWD），只報告不修改 |
| `/critique` | UX 設計評審：層次、清晰度、情感共鳴 |
| `/normalize` | 對齊設計系統規範 |
| `/polish` | 上線前最後一輪潤色 |
| `/distill` | 剝除多餘元素，回歸本質 |
| `/clarify` | 修改不清楚的 UX 文案 |
| `/optimize` | 效能優化 |
| `/harden` | 錯誤處理、i18n、邊界條件 |
| `/animate` | 加入有目的性的動畫 |
| `/colorize` | 加入策略性色彩 |
| `/bolder` | 讓設計更大膽有力 |
| `/quieter` | 讓過於強烈的設計沉穩下來 |
| `/delight` | 加入讓人記住的細節/驚喜 |
| `/extract` | 抽出可重用元件 |
| `/adapt` | 調整不同裝置的呈現 |
| `/onboard` | 設計引導流程 |
| `/typeset` | 修正字型選擇、層次、大小 |
| `/arrange` | 修正版面、間距、視覺節奏 |
| `/overdrive` | 加入技術上出色的視覺效果（beta）|
| `/teach-impeccable` | 一次性設定：讓 AI 了解你的設計系統 |

## 典型 AI 設計味（Anti-patterns）

- 字型：過度使用 Inter、Arial、system defaults
- 色彩：灰字放在彩色背景上 / 純黑純灰不加色調
- 版面：所有東西都包在 card 裡 / card 套 card
- 動畫：bounce/elastic easing（已過時感）

## 安裝（Claude Code 全域）

```bash
# 下載 zip 後執行：
cp -r dist/claude-code/.claude/* ~/.claude/

# 或用 npx
npx skills add pbakaus/impeccable
```

## 典型工作流

```
/audit dashboard        # 先找問題，只報告
/normalize dashboard    # 修正設計系統不一致
/polish dashboard       # 上線前最後確認

# 組合使用
/audit /normalize /polish blog
/critique /harden checkout
```

## vs UI-UX-Pro-Max

| | UI-UX-Pro-Max | Impeccable |
|--|--|--|
| **時機** | 寫 code 前（設計系統） | 寫完 code 後（改善品質） |
| **強項** | 色彩/字型/風格選擇 | 審查/修正/消除 AI 設計味 |
| **互補** | ✅ 兩個可以一起用 | ✅ |

## 相關

- [[ui-ux-pro-max-skill]]
- [[boris-15-claude-code-tips]]
- [[claude-hidden-combo]]
