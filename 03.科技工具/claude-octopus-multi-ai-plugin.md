---
title: "Claude Octopus：多 AI 協作 Claude Code Plugin"
tags: [claude-code, multi-agent, plugin, consensus, adversarial-review, codex]
date: 2026-04-14
category: AI工具
source: https://github.com/claude-octopus (2.6k stars)
---

## 是什麼

社群開源 Claude Code plugin（非官方）。讓 Claude 當指揮，同時協調最多 8 個 AI model（Claude、Codex、Gemini、Qwen、Ollama 等）一起處理任務。

## 核心機制

**75% 共識門檻** — 多個 model 跑完後若有不同意，攔下讓用戶決定，不自動放行。解決「單一 AI 寫完就直接信」的問題。

4 階段工作流：Discover → Define → Develop → Deliver，每階段有 quality gate。

**Debate 功能** — 讓多個 AI 就技術決策（如 monorepo vs microservices）正式辯論，最後看共識在哪。

## 指令

- `/octo:embrace` — 跑全程 4 階段
- `/octo:review` — 只跑 code review

## vs codex-plugin-cc

| | Claude Octopus | codex-plugin-cc |
|---|---|---|
| 定位 | 最多 8 provider，結構化工作流 | Claude + Codex 雙引擎 |
| 機制 | consensus gate、32 專家人格 | adversarial review、rescue 模式 |
| 設定 | 較重 | 輕量，裝了就用 |

## 實務

只有 Claude 也能用全部 persona 和 workflow，多 AI 協作在設定外部 provider 後才啟動。額外成本可壓低：Codex/Gemini 走 OAuth，Qwen 有免費額度，Ollama 跑本地。

## 評估

方向正確：多角度 review。對 side project 獨立開發者有用（沒人幫你 review 的場景）。Debate 功能值得試——架構選型時讓 AI 互相辯論，比一個人想省力。派哥已有 adversarial review 概念，這是工具化版本。
