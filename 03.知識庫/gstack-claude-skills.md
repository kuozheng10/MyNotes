---
title: "gstack - Claude Code 虛擬工程團隊"
tags: [claude-code, skills, ai, development, workflow]
date: 2026-04-03
category: 03.科技工具
source: https://github.com/garrytan/gstack
---

## 摘要

> Garry Tan（Y Combinator CEO）開發的 Claude Code skills 套件，62K GitHub stars。
> 裝完後在專案底下輸入 slash command，AI 就變成各種角色幫你工作。

## 安裝

```bash
git clone --depth 1 https://github.com/garrytan/gstack.git ~/gstack
cd ~/gstack && ./setup --host auto
```

安裝後 skills 會自動整合進 Claude Code，在任何專案底下都能用。

## 如何使用

在專案目錄下開 Claude Code，直接輸入 slash command：

```
/office-hours      # 整理專案、討論架構、產出 TODO list
/plan-eng-review   # 工程師視角審查計劃
/plan-ceo-review   # CEO 視角審查計劃
/design-html       # 產生 production-ready HTML 元件
/qa                # 真 Chromium 瀏覽器跑 E2E 測試
/review            # Staff Engineer 等級 code review
/cso               # OWASP/STRIDE 安全審查
/simplify          # 精簡程式碼
/ship              # 自動部署流程
/retro             # Sprint 回顧
```

## 最值得用的（Next.js 開發）

| 指令 | 情境 |
|------|------|
| `/office-hours` | 新功能開始前討論架構 |
| `/qa` | UI 改完跑真瀏覽器測試 |
| `/review` | PR 前做 code review |
| `/cso` | 上線前安全檢查 |

## 不需要額外設定

gstack 安裝完後就是一組 Claude Code slash commands，不需要自己寫 skill 檔案。
直接在 Claude Code 裡輸入 `/office-hours` 就啟動。

## 備註

- MIT License，免費永久
- 作者：Garry Tan（garrytan.com）
- 62K+ stars，8.3K forks，活躍維護中
