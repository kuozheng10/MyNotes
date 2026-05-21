---
title: Claude Code 跨對話記憶延續 — Handover 交班單技能（簡樸就是美）
tags: [claude-code, 記憶, 跨對話, skill, 工作流, 必學]
date: 2026-04-11
category: AI工具
---

## 核心概念

> 簡單就是美。所有對話、所有裝置，共用一個 SQLite 資料庫檔。

每次對話的重點打包成「交班單」，下一個對話自動接力。

---

## 交班單結構

```sql
handovers (
  id, date, device, agent, operator,
  topic,        -- 這次對話主題
  completed,    -- 完成了什麼
  decisions,    -- 做了哪些決定
  blocked,      -- 卡住的問題
  next_priorities, -- 下次優先做什麼
  created_at
)
```

---

## 兩種使用模式

### 模式 1：對話結束時
```
/exit → 自動觸發 /handover → 寫入資料庫
下次開對話 → 自動注入上一筆交班單
```

### 模式 2：對話中途清理（更常用）⭐
```
完成一項任務後：
1. /handover    → 重點結構化存進資料庫
2. /clear       → 清掉對話 context
3. 繼續下一個任務（不用登出重登）
```

效果：保留記憶 + 釋放 context window，一石二鳥。

---

## 為什麼「單一檔案」是關鍵

- 不管哪個裝置、哪個 session，都查同一個 DB
- 結構化資料好搜尋（找「上次做了什麼」幾秒鐘）
- 比 Markdown 日誌更快找到特定決策

---

## 對派哥的評估

派哥現在的記憶系統：
- `session-YYYY-MM-DD.md`：每日工作日誌（非結構化）
- `MEMORY.md`：長期記憶（手動整理）
- Claude Code 的自動 memory 系統（`/Users/kuochengchen/.claude/projects/`）

**Handover Skill 的優勢**：
- 跨 session 自動銜接，不用手動整理
- 結構化欄位（completed / decisions / blocked）更好查
- `/clear` 後不失憶，可以更積極用 /compact + /clear

**可行的實作方式**：
- 在 Claude Code 裡建 `/handover` skill
- 資料庫放在 `~/.claude/handovers.db`（SQLite）
- 每次 session 開始自動讀最新一筆

---

## 連結筆記
- [[claude-code-powerup-guide]] — Claude Code 10 大功能
- [[claude-md-optimization]] — CLAUDE.md 優化
- [[mempalace-ai-agent-memory]] — AI Agent 記憶管理
