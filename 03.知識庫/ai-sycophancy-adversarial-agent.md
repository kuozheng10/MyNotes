---
title: "AI 討好傾向 (Sycophancy) 與 Adversarial Agent 制衡"
tags: [ai-agent, sycophancy, multi-agent, adversarial-review, prompt-engineering, workflow]
date: 2026-04-14
category: AI工具
---

## 核心問題

AI 不是在理解你，它是在猜你的期待然後滿足它。問「幫我找 bug」，它就算硬掰也會給你一個。這是 sycophancy（討好傾向）。

太會配合你的系統不會幫你校正偏見，只會放大偏見。

## 問法決定輸出品質

避免把答案塞進問題裡：

- ❌「幫我找 bug」→ ✅「走一遍這段邏輯，回報你觀察到的所有事情」
- ❌「這架構有什麼問題？」→ ✅「分析這個架構的 trade-offs」

## Multi-Agent 制衡模式

不要叫一個 AI 同時當球員、對手、裁判。設計三層：

1. **Bug Hunter** — 激進找問題，高風險高分，覆蓋率優先
2. **Adversarial Reviewer** — 任務是反駁 Bug Hunter，推翻有分，推翻錯扣更多
3. **Referee** — 看兩方論證，做最終收斂

本質是正、反、合。讓不同偏見互相對沖，而非追求單一「完美中立」AI。

## 管理視角

Sycophancy 不是 AI 獨有問題，是管理問題。AI 只是把它放大了——比任何人更努力討好你，24/7 不累不不好意思。

解法和人的世界一樣：制度性引入反對意見。
- 人的世界：Devil's Advocate
- AI 世界：Adversarial Agent

## 最簡單的驗證迴圈

對有明確立場的問題，開第二個 session 叫另一個 AI 反駁第一個的結論。兩邊都頭頭是道的那一刻，才開始真正思考。

## 派哥應用

`/codex:adversarial-review` 暗語已對應此概念。Claude 寫的安全邏輯用 Gemini 交叉審查，就是避免 AI 共享盲點的制度性制衡。
