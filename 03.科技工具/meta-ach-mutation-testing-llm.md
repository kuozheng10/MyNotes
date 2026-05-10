---
title: "Meta ACH — LLM 引導的 Mutation Testing，反過來驗證測試有效性"
tags: [testing, mutation-testing, LLM, meta, quality, AI-coding, privacy, 必讀]
date: 2026-05-10
category: 03.科技工具
source: Telegram 派哥分享（FSE 2025 / Eurostar 2025）
---

## 核心問題

覆蓋率 90% ≠ 測試有效。覆蓋率只說「程式碼被執行過」，不說「有 bug 時測試會不會抓到」。

AI Coding 時代：一天可以產幾百個測試 → **數量不稀缺，有效性才稀缺**。

## Mutation Testing 基本概念

故意把程式改壞（製造 mutants），看測試能不能抓到：

```
age >= 18  →  age > 18  /  age <= 18  /  age >= 17
```

- 測試抓到 → mutant 被「殺死」（killed）✅
- 測試通過 → mutant「存活」（survived）⚠️ = 測試盲點

存活 mutant 越多 = 測試越虛。比覆蓋率更嚴格的測試品質指標。

## 傳統 Mutation Testing 三個老問題

1. **規模爆炸**：規則式 operator 無差別產生大量 mutants，壓垮基礎設施
2. **Equivalent Mutant**：`a + b` → `b + a`，語法不同語意一樣，純浪費算力
3. **不夠真實**：隨機改運算子，跟真實開發者會犯的錯（隱私/合規）差很遠

## Meta ACH 的解法

**少一點，但對症下藥**：產生相對少量的 mutants，但專注在「現有測試抓不到」且「跟特定議題相關」的缺陷。

### 工作流程（以隱私合規為例）

```
1. 自然語言描述風險
   「使用者位置資訊在未取得同意時被外傳」

2. LLM 生成「相關 + 現有測試抓不到」的 mutants
   只關注 currently uncaught，能抓到的代表已有覆蓋

3. Equivalence Detector Agent 過濾等價 mutants
   LLM-as-judge，語意等價的丟掉

4. LLM 生成能殺死這些 mutants 的測試
   每個交付的測試都已驗證：原始程式通過，mutant 失敗
   → Assurance：保證測試真的能抓到那種 bug
```

## 為什麼這個迴路能驗證測試有效性

一個測試只有在它能成功殺死至少一個 mutant 時，才被認定為有效。

如果測試在原始程式和所有 mutants 上都通過 → 它只是在「執行」程式碼，形同虛設。

## Meta 規模化成績

- 7 個 Meta 部署平台
- 10,795 個 Android Kotlin 類別
- 9,095 個 mutants
- 571 個隱私強化測試案例
- 工程師接受率 73%，其中 36% 被判定與隱私相關

## AI Coding 時代的啟示

借用 ACH 思路 → 用人工製造的、貼近真實風險的缺陷，反過來檢驗測試是否真的有效。
這才是 SBE 與品質保證在 AI 時代該走的方向（對應 SDD-vs-SBE 筆記的「測試驗證需求」概念）。

## 實作參考（非 Meta 規模也能用的思路）

1. 找一個你最擔心的 bug 類型（e.g. cc_processor 金額解析錯誤）
2. 用 Claude 故意製造幾個語意接近的「壞版本」
3. 用現有測試跑 → 看存活多少
4. 對存活的 mutant 補測試

## 相關筆記

- [[SDD-vs-SBE]] — Spec-Driven 和 Spec-by-Example，測試驗證需求
- [[ai-test-case-design-blind-spot]] — AI 測試案例設計盲點
- [[ai-era-testing-strategy]] — AI 時代測試策略全局
- [[ai-coding-qa-myths]] — AI coding QA 迷思
