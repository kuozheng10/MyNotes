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

## 為什麼需要 SbE：米達斯問題（AI 對齊）

AI 有高度能力（Competence）但缺乏價值對齊（Alignment）。
就像米達斯國王祈求「什麼都變黃金」，連食物和女兒都變金屬。

> 「當你說『快速實現扣款功能』，AI 可能寫出一個很快但沒有餘額檢查、也沒處理 race condition 的程式碼。它沒有惡意，只是太想幫你把需求變成現實。」

**SbE 是護欄**：從「描述」轉為「定義驗證」——不說「處理折扣」，而是給 $100 + 20% 折扣碼 → 應得 $80 的具體例子。把 AI 的能力限制在可預測的實例框架內。

來源：Nigel Warburton 的 Alignment Problem 概念。
