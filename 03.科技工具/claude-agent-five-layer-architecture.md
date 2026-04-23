---
title: Claude Code 代理開發套件：五層架構圖（Brij Kishore Pandey）
tags: ["Claude Code", "架構設計", "hook", "skill", "agent", "CLAUDE.md"]
date: 2026-04-24
category: AI工具
source: IG @codewithbrij，Telegram 派哥分享
---

## 五層架構公式

> CLAUDE.md + 技能 + Hooks + 子代理 + 外掛 = 代理開發套件

| 層級 | 名稱 | 職責 |
|------|------|------|
| 層 1 | CLAUDE.md（記憶層）| 架構規則、命名慣例、測試期望、儲存地圖 |
| 層 2 | 技能 SKILL.md（知識層）| 描述 + 觸發條件 → 按需自動載入；可在子代理中獨立執行 |
| 層 3 | Hooks（防護欄層）| 工具使用前後的控制點、安全強化、自動化 |
| 層 4 | 子代理（執行層）| 平行執行、委派工作、任務隔離 |
| 層 5 | 外掛（發佈層）| 技能/代理/Hooks 包成市場可安裝格式，跨專案共用 |

---

## Hooks 層詳解（層 3）

Hooks 是整個架構的關鍵控制點，類似 Web 2.0 的 trigger point。

| Hook 類型 | 時機 | 用途 |
|-----------|------|------|
| PreToolUse | 工具執行前 | 自動修正輸入、安全審查 |
| PostToolUse | 工具執行後 | 驗證輸出、記錄 log |
| SessionStart | Session 開始 | 注入 context、載入設定 |
| Stop | 任務結束 | 清理、交班、通知 |
| SubagentStop | 子代理結束 | 整合子代理結果 |

Hook 特性：
- 具確定性（Computational Sensor），不依賴 LLM 推論
- 為 AI 的行為設防護欄，在任務過程中進行檢查與限制

---

## 各層的 MCP 伺服器整合點

MCP 作為外部工具的統一介面，可在各層接入：
- 外部工具（Web、GitHub、API、自訂架構）
- 透過 Hooks 或技能層呼叫

---

## 對派哥的啟示

派哥目前的實作對應：

| 層 | 派哥現況 |
|----|---------|
| CLAUDE.md | 全域 + 專案層都有，完整 |
| Skills | ~/.claude/skills/ 手動管理，無版本控制 |
| Hooks | block-secrets.sh 等已有，注意 heredoc injection 風險 |
| 子代理 | MWT QA test 已用（mwt_qa_ui_test.mjs） |
| 外掛 | 尚無，autoskills 是可能路徑 |

**Hooks 層的待辦**：現有 hook 都要確認 heredoc 有加單引號（`<<'PYEOF'`），見 [[vibe-coding-rce-heredoc-three-rules]]

---

## 連結筆記

- [[harness-engineering]] — 四層 Harness 公式（執行/記憶/反饋/編排）
- [[karpathy-skills-claude-coding-rules]] — Skills 的哲學
- [[vibe-coding-rce-heredoc-three-rules]] — Hooks 的 RCE 漏洞案例
- [[autoskills-skill-infrastructure]] — 外掛層的分發基礎設施
- [[claude-md-optimization]] — CLAUDE.md 記憶層優化
