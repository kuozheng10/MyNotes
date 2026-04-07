---
title: "addyosmani/agent-skills — 系統化開發生命週期 Skill 套件"
url: "https://github.com/addyosmani/agent-skills"
tags: [claude-code, skill, workflow, spec-driven, tdd, architecture]
date: 2026-04-07
category: 03.科技工具
source: Telegram 派哥分享
---

## 摘要

> Addy Osmani（Google Chrome DevRel 主管）釋出的 19 個 Agent Skills，強制 AI 遵守完整開發流程，防止跳過規格、測試、安全審查。

## 7 個核心指令

| 指令 | 用途 |
|------|------|
| `/spec` | 先寫規格再開始寫程式（Spec-Driven Development）|
| `/plan` | 拆成原子任務（可驗證的小步驟）|
| `/build` | 增量實作，垂直切片 |
| `/test` | TDD + 瀏覽器測試 |
| `/review` | 程式碼品質 + 安全強化 + 效能優化 |
| `/code-simplify` | 降低複雜度（Chesterton's Fence 原則）|
| `/ship` | Git 工作流 + CI/CD + 上線清單 |

## 內建工程原則

- **Shift Left**：問題越早發現越便宜
- **Chesterton's Fence**：先理解為何存在，再移除
- **Hyrum's Law**：所有可觀察行為都會被依賴
- **Beyonce Rule**：「If you liked it, you shoulda put a test on it」

## 安裝

```bash
git clone https://github.com/addyosmani/agent-skills ~/.claude/skills/agent-skills
```

## 對派哥最實用的 3 個

1. **`/spec`** — 新功能前先寫規格，Claude 不會亂猜
2. **`/plan`** — 拆任務，避免 Claude 一次做太多、中途失控
3. **`/review`** — 安全審查對 cc_processor（碰個資）特別有用

其餘（browser-testing, CI/CD, deprecation）派哥目前規模用不到。

## vs gstack

- gstack：/review /ship 輕量快速
- 這套：更嚴格，19 個，有安全強化、效能優化等
- 兩套可並存，看場合選用

## 相關筆記

- [[SDD-vs-SBE]] — Spec-Driven 和 Spec-by-Example 的差異
- [[vibe-coding-architecture-debate]] — 設計層不能省的論點
- [[gstack-claude-skills]] — gstack /review /ship 輕量版
