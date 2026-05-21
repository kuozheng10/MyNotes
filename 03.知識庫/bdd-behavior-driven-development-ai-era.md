---
title: BDD 不是測試框架——Dan North 親口澄清，AI Coding 時代更該搞懂
tags: [BDD, 測試策略, AI協作, SDD, 需求工程, Gherkin]
date: 2026-04-29
category: 測試與品質
---

## 這是什麼

BDD（Behavior-Driven Development，行為驅動開發）是 Dan North 發明的需求釐清方法論，核心不是測試工具或語法，而是「先講清楚，再寫程式」的習慣。

2026 年因 AI Coding（Claude Code、Cursor、Copilot）、Spec-Driven Development（SDD）、AWS Kiro 等工具興起，BDD 重新成為焦點——因為 **AI 會把含糊需求以一百倍速產出一百倍垃圾**。

---

## BDD 的本質

- 用具體例子說一個故事，讓 PM、工程師、設計師、QA 都看得懂同一份需求
- 再拿這個故事去驅動開發
- 核心不是 Cucumber、Gherkin，而是「建立共識」的過程

---

## BDD vs 傳統測試：五個關鍵差異

| 維度 | 傳統測試 | BDD |
|------|---------|-----|
| 切入點 | 寫完才驗證 | 動工前先講清楚 |
| 目的 | 抓 bug | 建立信心與共識 |
| 語言 | 工程師才看得懂 | 所有角色都看得懂 |
| 時間點 | 事後補測試 | 先畫藍圖再動工 |
| 寫太多 | 尚可 | 反而是災難（腳本冗長難維護） |

---

## Gherkin 語法範例

```gherkin
Scenario: 餘額不足時扣款應該失敗
  Given 用戶餘額為 50 元
  When 收到扣款 100 元的請求
  Then API 應回傳 HTTP 400
  And 錯誤代碼應為 'INSUFFICIENT_FUNDS'
```

PM、業務、客服全看得懂，同時可直接作為 AI prompt。

---

## AI Coding 時代，BDD 為何重要

**Given/When/Then 是天然的 prompt 格式**：結構化、無歧義、貼近自然語言，丟給 AI 的輸出品質遠高於「幫我做個登入功能」。

**可執行規格 = AI 的護欄**：AI 寫完程式必須通過這些測試，提供客觀驗收防線。Adrian Cockcroft 指出：「比起 unit test，AI 更難偽造 BDD 測試的結果，品質明顯更好。」

**規格變活文件**：Feature file 綁定測試，只要測試還會跑，文件就一定是最新的。

---

## 三個核心觀念

1. **BDD 是釐清需求的方法，不是測試框架**——核心是建立共識，測試只是副產品
2. **BDD 是必要條件（知道要做什麼），測試是充分條件（確認做對了）**——兩件事不能混為一談
3. **AI Coding 時代，BDD 是給 AI 的最佳輸入格式**——越早習慣 Given/When/Then，AI 回報越誇張

---

## 對派哥的意義

- cc_processor、My Wallet Trip 新功能開發前，可用 BDD 情境先對齊需求
- 搭配已有的 `SDD-vs-SBE.md` 筆記，形成完整的需求→規格→測試鏈路
- Claude Code 可直接吃 Feature file 當 prompt，比模糊描述精準十倍

---

## 連結筆記

- [[SDD-vs-SBE]] — 規格驅動 vs 實例化需求的比較
- [[ai-era-testing-strategy]] — AI 時代的測試策略全貌
- [[ai-test-case-design-blind-spot]] — AI 無法設計測試案例的根本原因
- [[ai-coding-testing-management-10-issues]] — AI coding 測試管理十大問題
