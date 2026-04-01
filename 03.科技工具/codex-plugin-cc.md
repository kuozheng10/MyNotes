---
title: "Codex Plugin for Claude Code"
tags: [claude-code, openai, codex, code-review, plugin]
date: 2026-03-31
category: 03.科技工具
source: https://github.com/openai/codex-plugin-cc
---

## 摘要

> OpenAI Codex 的 Claude Code plugin，讓 Claude 負責開發、Codex 負責把關，雙引擎協作。⭐ 950

## 三大使用情境

### 1. 自動審查閘門（Auto Gate）
Claude 生成 code 準備回覆前，Codex 先在背景 scan。有問題直接擋下，叫 Claude 修好再出貨。

### 2. 全面大健檢（pre-merge review）
Merge 到 main 前執行：
```
/codex:review
/codex:review --background   # 背景跑，不干擾開發
```
針對未 commit 的變更做深度審查。

### 3. 難解 Bug 外包救火
```
/codex:rescue    # 把調查+修復丟給 Codex 子代理人
/codex:status    # 查看進度
/codex:result    # 收割結果
/codex:cancel    # 取消任務
```

### 附加：惡意找碴審查
```
/codex:adversarial-review
```
針對 race conditions、資安漏洞、容錯模式進行挑戰性審查。適合複雜架構完成後使用。

## 指令總表

| 指令 | 說明 |
|------|------|
| `/codex:review` | pre-merge code review（支援 `--background`）|
| `/codex:adversarial-review` | 惡意找碴：race condition、安全漏洞 |
| `/codex:rescue` | 把 bug 調查+修復外包給 Codex |
| `/codex:status` | 查背景任務進度 |
| `/codex:result` | 取得任務結果 |
| `/codex:cancel` | 取消任務 |
| `/codex:setup` | 初始化設定，抓取本機 Codex CLI 登入狀態 |

## 安裝

```bash
/plugin marketplace add openai/codex-plugin-cc
/plugin install codex@openai-codex
/reload-plugins
/codex:setup
```

全域安裝 Codex CLI：
```bash
npm install -g @openai/codex
```

## 需求

- ChatGPT 訂閱（含 Free）或 OpenAI API key
- Node.js 18.18+

## 評估

- **優點**：adversarial review 角度更多元，可補 Claude 的盲點；rescue 可外包難解 bug
- **缺點**：需要 OpenAI 訂閱，雙重付費
- **替代方案**：CodeRabbit（Vercel Marketplace）、直接讓 Claude 做嚴格審查

## 相關

- [[dual-agent-dev-loop]]
