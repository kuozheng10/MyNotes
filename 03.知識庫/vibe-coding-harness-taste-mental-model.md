---
title: Vibe Coding 真正學到的三件事：Harness、規劃、Taste
tags: [vibe-coding, harness, claude-code, agent, taste, product, workflow]
source: 社群文章（2026-06）
date: 2026-06-08
---

# Vibe Coding 真正學到的三件事

> 「模型決定系統的上限，Harness 決定系統的下限。」
> 但少了一層：**Taste 才是你打算把上限推到哪裡。**

---

## 核心心智模型

```
模型能力     → 決定系統「理論上限」（你管不著）
Harness     → 決定系統「執行下限」（你蓋的）
Taste       → 決定你實際推到哪裡（你的選擇）
```

---

## 第一件：Harness 決定系統下限

**過去的誤區：** 把精力放在 prompt，相信找到對的指令就能控制 AI。  
結果：系統越複雜，提示詞越難掌控底層邏輯的偏移。

**正確做法：**
- 把規則寫進環境（CLAUDE.md、skills、hook）
- 把角色邊界訂清楚
- 把驗收機制從「感覺沒問題」→「拿出硬證據」

### 三角色分工範例

| 角色 | 工具 | 職責 |
|-----|------|------|
| PM | Claude Code | 規劃、對齊、溝通——不碰程式碼 |
| 全端工程師 | Copilot（Codex）| 純實作 |
| 視覺設計師 | Antigravity | 畫面對齊 Design Spec |

**交接規則：** 每個 handoff 都要拿出硬證據，缺一個 handoff 無效。

---

## 第二件：前期規劃 > 實作

**現在最難的不是程式架構，是動手前的那段空白。**

必須把這些模糊意圖用「沒有歧義的語言」說清楚：
- Persona（使用者是誰）
- Scope（這次做什麼、不做什麼）
- KPI（怎樣算成功）

**反模式：**「AI 執行速度太快，如果沒想好，它就認真地把模糊念頭具現化成幾百行難以修改的 code。這時候的快，只是快速產出垃圾。」

**習慣：** 動手前逼自己坐下來把問題說清楚，和 Claude 對齊後才 vibe。

---

## 第三件：Taste 才是產品的分水嶺

**AI 給你的預設值：** 整齊、合理、可以動——但跟所有人用 AI 做出來的東西長得一樣。

**Taste 的定義：**
- 不是完美主義
- 是「持續不滿意」的能力——「這裡怪怪的」、「應該可以更好」
- 那個不舒服的感覺，才是把產品推向另一個境界的動力

**有立場的人** 才決定產品最終長什麼樣子。

---

## 實踐習慣

1. 動手前：逼自己把問題說清楚（Persona + Scope + KPI）
2. 做完後：不急著說好，問自己「真的滿意嗎？」
3. 交接時：要求硬證據，不接受「感覺沒問題」

---

## 連結筆記
- [[addy-osmani-harness-engineering-deep-dive]] — Harness Engineering 深入解析
- [[agents-md-context-engineering]] — context engineering 實作
- [[ai-subscription-downgrade-agent-addiction-reflection]] — 過度依賴 AI 的反思
- [[agent-governance-production-service]] — agent 治理原則
