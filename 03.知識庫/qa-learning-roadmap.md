---
title: QA 學習路線圖 — 軟體測試理念自學計畫（Claude SOP 串接）
tags: [qa, testing, 學習計畫, sbe, exploratory-testing, 路線圖]
date: 2026-04-11
category: AI工具
---

## 學習目標

掌握 AI 時代的 QA 測試**理念**，不是寫測試程式碼，而是：
- 知道「測什麼」比「怎麼測」更重要
- 能在 Claude SOP 流程中辨識 QA 知識，持續累積
- 將測試思維融入 cc_processor、My Wallet Trip 的開發流程

---

## 學習路線（5 個階段）

### 階段 1：需求驗證（已完成 ✅）
在寫 code 之前先驗證方向正確。

| 主題 | 筆記 | 狀態 |
|------|------|------|
| SBE 實例化需求 | [[SDD-vs-SBE]] | ✅ |
| Pre-totyping + 效率錯覺 | [[genai-pretotyping-wrong-direction]] | ✅ |
| Impact Mapping | （含在 pretotyping 筆記） | ✅ |

### 階段 2：測試思維（部分完成）
「測試」不是找 bug，是建立對系統行為的共識。

| 主題 | 筆記 | 狀態 |
|------|------|------|
| AI 時代測試策略 | [[ai-era-testing-strategy]] | ✅ |
| 探索性測試 SBTM | [[exploratory-testing-sbtm]] | ✅ |
| 測試案例設計原則 | 待 SOP | ⏳ |
| 風險導向測試（Risk-based） | 待 SOP | ⏳ |

### 階段 3：AI 協作測試（進行中）
如何讓 Claude 幫你測試，而不是幫你製造新 bug。

| 主題 | 筆記 | 狀態 |
|------|------|------|
| AI code review 共享盲點 | [[ai-code-review-security-risk]] | ✅ |
| Claude + Gemini 交叉審查 | （CLAUDE.md 規則） | ✅ |
| 用 SBE 餵 AI 生精準程式碼 | （含在 SBE 筆記） | ✅ |
| AI 協作的探索性測試 | 待 SOP | ⏳ |

### 階段 4：Bug 管理與回報（未開始）
發現問題後如何有效處理。

| 主題 | 筆記 | 狀態 |
|------|------|------|
| Bug 報告撰寫（複現步驟、環境、預期/實際） | 待 SOP | ⏳ |
| Root Cause Analysis（5 Whys） | 待 SOP | ⏳ |
| Regression 迴歸測試思維 | 待 SOP | ⏳ |

### 階段 5：QA 文化與流程（未開始）
讓測試思維融入開發習慣。

| 主題 | 筆記 | 狀態 |
|------|------|------|
| Shift Left Testing（測試前移） | 待 SOP | ⏳ |
| Definition of Done（完成定義） | 待 SOP | ⏳ |
| QA Checklist（每次發布前） | 待建立 | ⏳ |

---

## SOP 串接規則

**當派哥丟 QA 相關文章時（SOP 流程）：**
1. 識別屬於哪個階段（1-5）
2. 存成 MyNotes 筆記
3. **更新此路線圖的對應狀態** → ✅
4. 如果連結到實際專案，在筆記末尾加「對 cc_processor / My Wallet Trip 的應用」

**判斷是否 QA 相關的關鍵字：**
測試 / QA / bug / 需求 / SBE / TDD / BDD / 探索性 / 驗收 / regression / checklist

---

## 近期建議 SOP 的資源

- Agile 3 Uncles 課程文章（4/18 探索性測試）
- 「如何寫好 bug report」
- 「Risk-based testing」
- 「Shift Left Testing」

---

## 連結筆記
- [[SDD-vs-SBE]] — 實例化需求
- [[ai-era-testing-strategy]] — AI 時代測試策略
- [[exploratory-testing-sbtm]] — 探索性測試
- [[genai-pretotyping-wrong-direction]] — Pre-totyping
- [[ai-code-review-security-risk]] — AI code review 安全
