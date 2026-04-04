---
title: "SDD 規格驅動開發 vs SBE 規格由範例"
tags: [ai-coding, methodology, spec, sbe, sdd]
date: 2026-04-04
category: 03.科技工具
---

## 核心差異

| | SBE（Specification by Example） | SDD（Spec Driven Development） |
|---|---|---|
| 起源 | ~2010，敏捷開發 | ~2025，AI coding agent 時代 |
| 重點 | 把需求講對 | 把東西做對 |
| 工具 | Given-When-Then 具體情境 | 結構化規格文件 |
| 適合 | 多人團隊、跨職能溝通 | Solo dev + AI 執行 |
| 解決 | 「我們要做什麼」 | 「怎麼做出來」 |

## SBE 寫法範例

```
Given：使用者已註冊，密碼是 123456
When：他輸入錯誤密碼 abcdef
Then：系統顯示「密碼錯誤，請再試一次」，且不允許登入
```

## 常見陷阱

- 只有 SDD（AI 照規格產出）→ 技術上正確，業務上卻不是真正要的
- 只有 SBE（大家討論例子）→ 共識有了，但沒有嚴謹規格給 AI 執行

## 健康做法（兩者結合）

1. SBE：用具體例子討論清楚需求邊界
2. SDD：把例子整理成結構化規格
3. AI：照規格產生程式碼，再用例子驗證

## 我們的現況

詳見下方「派哥 + Claude Code 的建議」
