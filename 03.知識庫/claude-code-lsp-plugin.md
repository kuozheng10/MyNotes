---
title: "Claude Code LSP Plugin — 編譯器等級語意分析"
tags: [claude-code, plugin, LSP, python, rust, typescript, refactoring]
date: 2026-04-06
category: 03.科技工具
source: 社群分享
---

## 摘要

> Claude Code 可安裝 LSP（Language Server Protocol）plugin，讓 Claude 用編譯器等級的語意理解程式碼，而不是只靠 grep 搜字串。

## 功能

- 跳到定義（Go to Definition）
- 追蹤呼叫鏈（Call Hierarchy）
- 即時型別錯誤偵測
- 改了方法簽章 → LSP 自動回報哪些地方壞掉 → Claude 同一輪修好

## 安裝步驟

1. 先在電腦裝對應語言伺服器：

| 語言 | 語言伺服器 |
|------|-----------|
| Python | `pip install pyright` 或 `npm i -g pyright` |
| Rust | `rustup component add rust-analyzer` |
| TypeScript | `npm i -g typescript-language-server typescript` |
| Go | `go install golang.org/x/tools/gopls@latest` |

2. 在 Claude Code 搜尋安裝：
```
/plugin 搜尋 LSP
```

## 評估：對派哥有用嗎？

**有用，特別是 TypeScript 專案（My Wallet）和 Python（cc_processor）。**

My Wallet 有多個 component import 同一個 type，LSP 能讓 Claude 改介面時直接知道哪裡壞掉，不用跑 tsc 才發現。

cc_processor 是 Python，pyright 能抓型別錯誤。

## 安裝建議

- My Wallet（TypeScript）→ 裝 typescript-language-server
- cc_processor（Python）→ 裝 pyright

## 相關筆記

- [[claude-code-source-leak-insights]] — Claude Code 95% 是 harness，LSP 就是讓 harness 更強的工具
- [[dual-agent-dev-loop]] — 讓 Claude 改 code 更精準，少跑測試
