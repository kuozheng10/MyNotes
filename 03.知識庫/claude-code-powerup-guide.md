---
title: Claude Code /powerup — 10 個核心功能完整解析
tags: [claude-code, tips, workflow, CLAUDE.md, skills, hooks, agents, rewind]
date: 2026-04-09
category: 03.科技工具
source: 社群分享（/powerup 教程解析）
---

## 這是什麼

Claude Code 內建互動式新手教程，終端輸入 `/powerup` 可解鎖 10 關卡，每學完一項按 Enter 打勾，全解鎖出現「All powered up 10/10」。

---

## 10 個功能速查

| # | 功能 | 快速說明 |
|---|------|---------|
| 1 | `@檔案` / `@資料夾/` | 直接附加程式碼，不用貼文字 |
| 2 | Shift+Tab 切模式 | default / accept edits / plan / auto |
| 3 | `/rewind` | 每次編輯前自動 checkpoint，Esc Esc 叫出回滾 |
| 4 | `&` 背景執行 + `/tasks` | 指令加 & 背景跑，`/tasks` 查狀態 |
| 5 | `CLAUDE.md` + `/init` | 專案規範永久內建，每次 session 自動讀 |
| 6 | `/mcp` | 連 Slack、DB、瀏覽器等外部工具 |
| 7 | Skills / Hooks | `.claude/skills/` 存常用 prompt；hooks 觸發腳本 |
| 8 | `/agents` | 多代理平行處理，`.claude/agents/` 定義專屬角色 |
| 9 | `/remote-control` + `/teleport` | 手機/網頁遠端監控；`/teleport` 把雲端 session 拉回本機 |
| 10 | `/model` + `/effort` + `/fast` | 切 Opus/Sonnet/Haiku；設思考深度；快速模式 |

---

## 重點功能詳解

### /rewind — 最被低估的功能
- Claude 在**每次編輯前**自動建立 checkpoint
- `Esc Esc` → `/rewind` → 選擇要回滾的時間點
- 程式碼 + 對話歷史一起回滾，git 歷史保持乾淨
- 不用怕 Claude 改壞，有後悔藥

### 四種執行模式（Shift+Tab 切換）
| 模式 | 適合場景 |
|------|---------|
| default | 一般開發，每次編輯都確認 |
| accept edits | 自動接受檔案修改，但指令要問 |
| plan | 只規劃不動檔案，重構前用 |
| auto | Claude 自判安全性，長時間無人值守 |

### Skills + Hooks 組合 = 個人自動化
- `CLAUDE.md + hooks + skills` 三合一：把開發規範 + 自動化流程永久內建
- 每個專案都是「認識你」的 Claude 在幫你工作

---

## 對派哥的啟示
- `/rewind` 要記得用，改爛了直接回滾，比 git reset 快
- `plan` 模式 + 確認後切 `auto` = 大重構的標準流程
- `/tasks` 背景跑長任務，繼續對話不等待
- Skills 就是派哥現在用的 `.claude/skills/` 機制，完全對上

---

## 連結筆記
- [[boris-15-claude-code-tips]] — Boris Cherny 的 15 個高頻技巧（更深入）
- [[claude-code-feature-workflow]] — Feature 開發制度化流程
- [[claude-md-optimization]] — CLAUDE.md 撰寫優化技巧
