# AI Coding 架構：Guardrails + Contract First（AndrewShop 案例）

> 來源：Andrew（DevOpsDays Taipei 2026 Keynote Speaker）Facebook 貼文
> 整理日期：2026-06-01

---

## 核心論點

**Guardrails（護欄）= 把 AI 行為框在可控範圍內的方法**

本質上與過去十幾年的 API First / Contract First / 依賴反轉是同一件事：

| 時代 | 名稱 | 約束對象 |
|------|------|---------|
| 過去 | API First / Contract First | 人寫的 code |
| 現在 | Guardrails / Harness | AI 寫的 code |

> 架構師現在最重要的事：用 code 把這條界線定義清楚。

---

## AI 開發的基本結構（ralph-loop）

```
頭（需求 / Contract）
  + 尾（期待 / Tests）
  → 中間讓 Agent 自己跑（ralph-loop）
```

**ralph-loop**：agent 執行 → 驗證 → 修正，反覆循環直到通過驗證。

**架構師的任務**：把大型系統拆成一個個「頭尾都清楚」的單位，逐一開發、驗證、組裝。

---

## AndrewShop 專案結構（.NET 實作）

| 層級 | Namespace | 職責 |
|------|-----------|------|
| 需求（頭） | `.Abstract` | 只有介面定義 + 註解，**無任何邏輯** |
| 實作 | `.Core` | 只依賴 `.Abstract`，建構主要流程（例如結帳） |
| 客製擴充 | `.Extension` | 按 `.Abstract` 介面擴充專屬行為 |
| Hosting | `.API` / `.Storefront` | 非功能性需求（認證、授權、高可用） |
| 驗證（尾） | `.Tests` | AI 依「.Abstract + scenario」自動產生 |

---

## 三個 Review 重點（只看這三件事）

1. **Contract 是不是我要的？**
   - 只看介面定義與註解，確認沒有邏輯滲入

2. **Scenario 是不是我要的？**
   - 只看情境敘述與 decision table，確認覆蓋範圍正確

3. **Test code 怎麼「使用」這個 Contract？（DX 問題）**
   - 從「contract 被呼叫的方式」回頭調整 interface 設計
   - 不管真人 developer 還是未來 agent，呼叫方式要直覺

> 三點確認完，直接把專案丟給 agent 跑，最後看測試結果。

---

## 實際執行結果

- 工具：Codex（ChatGPT Plus 附贈額度，GPT-5.4）
- 時間：零碎下班時間，約一週額度
- 時期：2026/03
- 結論：規劃做好，AI 執行很輕鬆

---

## 工具無關論

> 與其追工具（必要但不是全部），更該問：換了工具我一樣順利嗎？

大廠模型與工具約每 3～6 個月翻盤一次。核心競爭力在「大型系統的工作方法」，而不是特定工具。

---

## 下一個難題：客製化隔離（已完成，待公開）

**目標**：完全不動既有 code，完成客製化擴充，甚至 binary code 完全共用（不允許 rebuild）。

已完成的兩個實作案例：
1. **Apple BTS 教育優惠方案**：專屬官網流程 + 高整合優惠規則（會員認證 + 商品/贈品規則）
2. **寵物店服務案例**：商品 + 寵物美容預約（非正規商品）+ 購物車整合 + 組合優惠

---

## 與其他筆記的連結

這篇和之前存的文章高度呼應：

[[senior-dev-ai-era-harness-complexity]]：
- 「Harness」= 這篇的 guardrails + ralph-loop
- 「管複雜度」= 這篇的拆「頭尾清楚的單位」
- BDD/SBE = 這篇的 scenario + decision table

[[vibe-coding-dodonov-stanley-ai-tool]]：
- Vibe Coding = 極端版的「中間讓 agent 跑」
- 差別在：這篇有 Contract + Tests 兜住，Vibe Coding 沒有 → 溫徹斯特風險

**差異對比**：

| 維度 | Andrew 的做法 | Vibe Coding |
|------|--------------|-------------|
| 速度 | 較慢（需設計 contract） | 極快 |
| 品質 | 可控（有 guardrails） | 未知 |
| 規模 | 適合大型系統 | 適合 MVP |
| 複雜度管理 | 核心能力 | 缺乏 |
