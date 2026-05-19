---
title: "Karpathy 開發哲學打包成 Claude Skill"
tags: [claude-code, claude-md, karpathy, coding-rules, ai-coding, skill, codex-cli, copilot]
date: 2026-04-14
category: AI工具
source: https://github.com/forrestchang/andrej-karpathy-skills
---

## 是什麼

把 Andrej Karpathy 的 AI 開發哲學包成 CLAUDE.md 規則，直接管控 Claude Code 行為。

解決的痛點：AI 亂改已寫好的 code、需求未問清就腦補、過度工程、不測試只叫你「再試」。

相關 repo：
- `forrestchang/andrej-karpathy-skills`（19.5K stars）
- `multica-ai/andrej-karpathy-skills`（136K stars，較新）

## 4 個核心規則

- **先想再寫**：遇到模糊需求先提問，沒弄清楚邏輯前不動 code
- **極簡主義**：能 10 行解決不寫 100 行，沒要求的功能一字不多
- **外科手術式修改**：只動該改的地方，不亂碰註解、格式或沒壞的 code
- **測試驅動**：給成功標準或測試案例，讓 AI 跑 loop 自行修正直到通過

## 對應到派哥的 CLAUDE.md

這套哲學已在派哥的全域 CLAUDE.md 中實踐：
- 完成驗證（跑 type check + lint）→ 先想再寫 + 測試驅動
- 禁止自動加功能 → 極簡主義
- 對話 >10 輪後重讀再編輯 → 外科手術式修改

## 怎麼用

一鍵載入：
```bash
curl -o CLAUDE.md https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md
```

最高級用法不是全盤接收——抓下來讀一遍，挑出你開發痛點最深的幾條，裁切後化為己用。

## Codex CLI / Copilot CLI 移植版

doggy8088 把同套哲學移植成支援 AGENTS.md 的版本，任何支援 AGENTS.md 的 Coding Agent 都可以用：

```bash
# Copilot CLI plugin 安裝
copilot plugin marketplace add doggy8088/andrej-karpathy-skills
copilot plugin install andrej-karpathy-skills@karpathy-skills
```

repo：https://github.com/doggy8088/andrej-karpathy-skills

## 目標導向執行：給成功標準，不給步驟

不要說「幫我寫一個處理使用者輸入的函式」。

要說：

> 設計 `process_user_input(s: str)`，驗證是否為有效 JSON。
> 不是 → 回傳含 error 的 dict。
> 是 → 回傳解析後的 dict。
> **驗收標準**：通過 `test_valid_json_input` 和 `test_invalid_json_input`。

核心差異：Claude 不只要寫出函式，還要「確保能通過測試」。讓 AI 自己 loop 驗收，大幅減少來回輪次。

## 提煉

AI coding 的本質管理問題：把 AI 當「需要精確 SOP 的頂級實習生」，而不是「萬能助手」。規則越清楚，實習生越不會亂來。
