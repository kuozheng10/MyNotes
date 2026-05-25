---
title: "cat-skills：AI 專家顧問模式 Elevate + 結構化開發 Architect"
tags: [skills, cat-skills, Claude, AI顧問, 架構師, context, 結構化開發, CLAUDE.md, 思維模式]
date: 2026-05-25
category: 03.知識庫
source: Telegram 分享（catcatcatstudio/cat-skills）
---

## 一句話核心

> cat-skills 最值得借鑑的兩個概念：Elevate 把 AI 從「找事做的工人」變成「敢說不的顧問」；Architect 解決大型專案 AI 失去 context 的頭號問題。

---

## 專案資訊

- GitHub：`catcatcatstudio/cat-skills`
- 包含 14 項獨立技能
- 最值得關注的兩項：Elevate、Architect

---

## 1. AI 專家顧問模式（Elevate）

### 運作方式
1. 自動偵測任務所屬領域
2. 採納該領域頂尖實踐者的思維框架
3. 最多提出 **3 個提案**
4. 成果夠好時，**選擇不提出任何修改建議**

### 關鍵洞察
> AI 通常被設計成「總是找事做」，但 Elevate 反其道而行：品質達標時保持沉默，這才是真正的專業顧問行為。

### 對照派哥的 Harness 觀念
- 這是一種 **Inferential Guide** 的設計——不只是傳遞規則，而是傳遞「思維模式」
- 對應到：CLAUDE.md 不只是說明書，而是「我希望 AI 以什麼角色思考這個任務」

---

## 2. AI 輔助結構化開發（Architect）

### 解決的問題
大型專案中 AI 失去上下文（context），顧此失彼，是 AI 編碼的頭號失敗原因。

### 結構化生命週期

```
探索（Explore）
  ↓
設計（Design）
  ↓
規劃（Plan）
  ↓
建構（Build）
```

每個階段有明確產出物，進入下一階段前確認上下文完整，避免「AI 忘記前半段在幹嘛」。

### 對照派哥的工作流程
- 對應 Claude Code 的 SDD → 實作 → code review 流程
- Explore = 讀 spec、問澄清問題
- Design = 寫 SDD/SBE
- Plan = 拆 task
- Build = 實作 + 驗證

---

## 核心啟發：CLAUDE.md 的正確定位

| 舊思維 | 新思維 |
|--------|--------|
| CLAUDE.md = 專案說明書 | CLAUDE.md = AI 的思維模式引導 |
| 告訴 AI 「這個專案有什麼」 | 告訴 AI 「面對這個任務時，你應該用什麼角色思考」 |

> 從「寫程式的工人」→「會思考的架構師」的差距，不在 model 本身，在 Harness 的設計。

---

## 相關筆記

- [[harness-engineering]] — Guides（前饋）vs Sensors（回饋），cat-skills 的 Elevate 是 Inferential Guide 的絕佳範例
- [[addyosmani-agent-skills]] — Skills 作為 Feedforward Guide 的系統化實作
- [[agent-skills-standard]] — Skills 標準規範
- [[garry-tan-thin-harness-fat-skills]] — Thin Harness, Fat Skills 的設計哲學
