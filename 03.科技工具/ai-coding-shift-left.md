---
title: "AI Coding 壓力左移法"
tags: [ai-coding, methodology, tdd, spec, code-review, workflow]
date: 2026-04-01
category: 03.科技工具
---

## 核心觀點

> AI 寫 code 越來越快，但你 review 的速度不會等比成長。
> 解法不是放棄 review，而是把壓力往左移——從源頭就降低需要 review 的成分。

## 四個關卡

### 1. spec_as_code
- 把需求簡化成 code（型別、介面、contract）
- 同步產生 test code 來驗證 spec 是否正確
- 靠編譯器自動找出不合規格的錯誤

### 2. test_as_code
- 這時才讓 AI 寫 implementation
- AI 被 spec（頭）和 test（尾）兩頭夾住
- build 報錯 = spec 問題；test 報錯 = 實作問題
- 形成 **ralph-loop**：AI 自己開發、自己驗證，低級問題不再丟給你

### 3. read_code
- 複雜問題留下來時，讓 AI 幫你快速理解
- 產出：pseudo code、C4 model、class diagram、sequence diagram
- 結構 / 設計問題在這階段再刪一批
- 自己的設計心得 → 轉成 SKILL，進一步減少設計錯誤

### 4. learn_code
- AI 寫出超出你能力範圍的 code → 補足自己
- 讓 AI 用你最好學習的方式教你
- 別省 token，守住品質同時強化自己

## 關鍵原則

**你還是要把關的。**
搞不清楚就按下 merge → 離能掌控 AI 的位置越來越遠。

## 對 CLAUDE.md 的啟發

在 Plan 階段加入：
- 先定義介面/型別（spec_as_code）
- 先寫測試骨架（test_as_code）
- Implement 後讓 AI 產生 pseudo code / diagram 供 review（read_code）
