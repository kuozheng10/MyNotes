---
title: Uncle Bob「我不讀Agent寫的任何程式碼」——信任AI程式碼的方式正在轉變
tags: [ai-coding, vibe-coding, clean-code, testing, verification, uncle-bob, claude-code]
source: Gnimnek Wang（軟體設計鮮思維社團，Facebook），https://www.facebook.com/share/p/1EZ8guiYZw/?mibextid=wwXIfr
date: 2026-08-26
related: vibe-coding-architecture-debate, ai-testing-agile-quality, vibe-coding-harness-taste-mental-model
---

# Uncle Bob「我不讀Agent寫的任何程式碼」：信任AI程式碼的方式正在轉變

> 原始討論來自 X（上個月底），資深工程師 Ori Pomerantz（1983年就開始寫程式）發文：如果最後程式碼要由自己負責，是不是就該理解每一段Code？所以不太放心讓Agent直接改檔案。
>
> 底下回覆的是 **Bob大叔（Uncle Bob / Robert C. Martin）**，《Clean Code》與《Clean Architecture》作者：
> **"My current strategy is to not read any of the code written by my agents."**（我目前的策略，是不閱讀Agent所寫的任何程式碼。）

---

## 這不是「甩手不管」的vibe coding

Bob大叔真正的意思，**不是**一般人以為的「只求結果、不理會Code怎麼組織」那種vibe coding。恰恰相反：他把開發者的角色，從親自撰寫、逐行閱讀實作（Implementation），提升到更高層次的**「約束（Constraint）」與「驗證（Verification）」**，更接近軟體設計者（Designer）的角色。

## 信任機制的轉變

| 舊模式 | 新模式 |
|--------|--------|
| 「這份Code我每一行都看過，所以我相信它」 | 「這份實作已經通過我定義的規格、測試與品質關卡，所以我可以相信它」 |

驗證機制清單（AI Agent負責大量實作，但必須全部通過）：
- 單元測試（Unit Tests）
- 驗收測試／Gherkin規格（Acceptance Tests / Gherkin）
- 品質保證流程（QA Procedures）
- 測試覆蓋率（Test Coverage）
- 品質指標（Quality Metrics）
- 突變測試（Mutation Testing）

## Clean Code的規範怎麼轉成AI Agent規範

作者（Gnimnek Wang）自己過去落實 Clean Code 的具體規範，在AI輔助開發時代反而更適合直接轉成**AI Agent的開發規範**：

- 單一 Method 儘量控制在 20 行以內
- Method 參數儘量不要超過 4 個
- 必然撰寫單元測試（Unit Test）
- 命名必須具有完整而清楚的語意

**核心洞察**：這些以前是「要求自己寫程式時遵守」的原則，現在變成「餵給AI Agent遵守」的規範——原則沒變，只是誰來執行變了。

## Bob大叔的背景（為什麼這句話有分量）

73歲，1960年代就開始寫程式，從機器碼、PDP-8 Assembler，一路經歷FORTRAN、COBOL、C、C++。連這種「上古時代」一路親手刻Code刻到今天的老前輩，都已經開始把實作工作交給AI Agent、自己抽離到Syntax與Implementation之上。

## 真正值得學的不是「讓AI多寫Code」

作者的結論：真正值得學習的，不是「怎麼讓AI幫我多寫一點Code」，而是**如何把多年累積的軟體設計、架構、程式規約、測試、團隊協作，轉換成AI Agent可以理解、遵循，而且可以被驗證的工作規範**。

---

## 對派哥的意義

- 跟 [[vibe-coding-architecture-debate]]（設計層不能跳）是同一立場的不同表達方式：那篇講「執行層可以跳，設計層不能跳」，這篇具體示範了「設計層」在AI時代長什麼樣子——不是自己畫架構圖，而是把約束跟驗證機制（測試/Gherkin規格/品質指標）定義清楚
- 跟 [[ai-testing-agile-quality]] 呼應：那篇談AI Coding時代測試品質缺口的應對，這篇是「為什麼測試變得比以前更重要」的具體理由——測試不再只是品保手段，而是取代「逐行閱讀」成為信任AI程式碼的**唯一機制**
- 對派哥自己的 Claude Code 使用方式的啟示：派哥目前很多自動化（cc_processor、insurance_processor等）都有寫測試/驗證步驟的習慣（如 Notion sync 後要比對筆數才能回報完成），這篇等於是給這個習慣一個更明確的理論支撐——不是「順便做」而是「這是信任AI輸出的唯一憑證」

---

## 相關筆記

- [[vibe-coding-architecture-debate]] — Vibe Coding正確姿勢：執行層可跳，設計層不能跳
- [[ai-testing-agile-quality]] — AI Coding時代測試品質缺口與應對實踐
- [[vibe-coding-harness-taste-mental-model]] — Vibe Coding真正學到的三件事：Harness、規劃、Taste
