---
title: Codex Hooks：事件觸發機制取代超長 System Prompt
tags: [Claude Code, 自動化, 工作流程, 工具, 架構設計]
date: 2026-05-19
category: AI工具
source: https://www.patreon.com/posts/ni-huan-zai-yong-158551055
---

## 這是什麼

Codex 官方新功能：Hooks 是綁在工作流程特定時機上的自動觸發規則，不靠 prompt 記憶，而是在對的時間點直接把規則推到 Agent 面前。

---

## 為什麼比 System Prompt 好

System Prompt 的問題：對話越長，注意力被稀釋，規則就被淡化忘記。

Hooks 的方式：事件發生 → 規則自動觸發，不管 session 多長都有效。

就像智能家居：「有人開門 → 自動開燈」，不是「希望電燈記得要亮」。

---

## 四個實用場景

| 時機 | Hook 做什麼 |
|------|------------|
| session 開始 | 提醒 Agent 遵守工作習慣 |
| 送出 prompt 前 | 檢查有沒有貼到 API key |
| 執行指令前 | 攔截危險操作（`rm -rf` 等） |
| 準備停下前 | 確認「你真的跑過測試了嗎？」|

---

## 使用方法 / 快速啟動

設定檔：`hooks.json`（放在專案或全域 config）

```json
{
  "hooks": [
    {
      "event": "session_start",
      "action": "remind",
      "message": "遵守 CLAUDE.md 規則，有疑問先問再動"
    },
    {
      "event": "pre_command",
      "action": "check",
      "pattern": "rm -rf",
      "block": true
    }
  ]
}
```

詳細格式見官方文件（Patreon 文章有新手範本）。

---

## 對派哥的啟示

你的 CLAUDE.md 現在靠 prompt 規範 Claude 行為，但長 session 規則會被遺忘。Hooks 是補充而不是替代：

- **已有**：CLAUDE.md + SessionStart hook（現在 session 開始已有自動讀 log.md）
- **可加**：pre-commit hook 強制跑 lint；pre-command hook 攔截危險指令
- **cc_processor 適用**：每次處理帳單前 hook 確認 sender 白名單已啟動

Claude Code 也有 Hooks（你現在就在用），Codex 的 hooks.json 設計邏輯相同。

---

## 連結筆記

- [[claude-code-powerup-guide]] — Claude Code 基本功，Hooks 是第 7 項
- [[karpathy-skills-claude-coding-rules]] — 測試驅動 + 先想再寫，Hooks 是執行層保障
- [[claude-code-setup-plugin-official]] — claude-code-setup 也會自動配置 Hooks
