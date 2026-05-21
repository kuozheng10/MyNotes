---
title: AI code review 無法抓住 AI 生成的安全漏洞 — 共享盲點問題
tags: [ai, security, code-review, 安全, 開發流程, 必學]
date: 2026-04-11
category: AI工具
source: https://augmentedswe.com/p/ai-code-review-security
---

## 核心問題

約 **45% 的 AI 生成程式碼存在安全漏洞**（Java 高達 70%）。
AI 大量複製訓練數據中過時或不安全的編碼實踐。

---

## 為何不能用同一個 AI 寫和審 code

**共享盲點（Shared Blind Spots）**：

> 如果 AI 生成時認為某種不安全模式是「標準答案」，
> 審查時它也會基於相同訓練權重認為該模式「正確」。

- **回音室效應**：AI 缺乏獨立判斷，只是重複訓練集偏見
- **審查疲勞**：AI 生成的 PR 規模大且「看起來沒問題」，人類容易過度依賴
- **邏輯漏洞難抓**：「缺少權限校驗」這類業務邏輯問題，AI 最容易漏

---

## 安全建議

| 建議 | 做法 |
|------|------|
| **追蹤 AI 生成程式碼** | 建立清冊，針對性安全審計 |
| **CI/CD 硬性門檻** | SAST/SCA 工具，安全掃描列為必過項目 |
| **人類角色轉型** | 從「檢查語法」→「威脅建模」+「架構審查」 |
| **跨檔案上下文** | 用能理解整個 codebase 的工具，不是看單一檔案 |

---

## 對派哥的啟示

- **cc_processor / My Wallet Trip**：AI 寫的程式碼，安全邏輯（OAuth、API key 處理）要人工審查
- **用不同 AI 審查**：Claude 寫 → Gemini 審（或反過來），避免共享盲點
- **CLAUDE.md 已有規範**：Code Review 檢查項包含安全漏洞，但要主動執行，不能只依賴 AI 自己抓

---

## 連結筆記
- [[ai-era-testing-strategy]] — AI 時代的測試策略
- [[vibe-coding-architecture-debate]] — Vibe Coding 架構爭議
- [[atr-agent-threat-rules-panguard]] — Agent 威脅規則
