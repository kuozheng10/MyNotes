---
title: "OpenMemory Auto Manager"
tags: [claude-code, gemini, codex, mcp, memory, cross-tool]
date: 2026-04-01
category: 03.科技工具
source: https://github.com/vancelin/openmemory
---

## 摘要

> 讓 Claude Code、Codex CLI、Gemini CLI 共用同一個長期記憶庫，自動管理 server 開關。

## 運作原理

```
開 claude   → OpenMemory 自動啟動 (refcount = 1)
開 gemini   → 共用同一個 server    (refcount = 2)
開 codex    → 共用同一個 server    (refcount = 3)
關 claude   → 繼續運行             (refcount = 2)
關 gemini   → 繼續運行             (refcount = 1)
關 codex    → 自動停止             (refcount = 0)
```

## 特色

- **Zero config** — 不需要 API key、不需要 Docker
- **Auto lifecycle** — 第一個 CLI 啟動時開，最後一個關閉時停
- **Cross-tool memory** — Claude Code、Codex CLI、Gemini CLI 共享同一記憶庫
- **SQLite 本地儲存** — 資料不出機器
- **Reference counting** — 多終端安全使用，自動清理

## 前提條件

- OpenMemory server 裝在 `~/OpenMemory`
- Python 3.10+（Codex CLI 的 STDIO proxy 需要）
- Node.js 18+
- `curl`, `lsof`

## 評估

- **優點**：三個 AI 工具共享記憶，不用手動同步
- **缺點**：需要額外安裝 OpenMemory server；Codex 需要 Python proxy
- **適用情境**：同時用多個 AI CLI 工具的人
- **對派哥的價值**：Claude Code 已有自己的 memory 系統；若不常用 Gemini/Codex，加值有限

## 相關

- [[codex-plugin-cc]]
