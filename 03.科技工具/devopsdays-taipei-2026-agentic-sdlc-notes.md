---
tags: [agentic-sdlc, devops, ai-agent, sdlc, 粒度, tasking, 91app, devopsdays]
source: DevOpsDays Taipei 2026 現場心得（派哥人手打）
date: 2026-06-28
speaker: 濮紹華 AlanPu（91APP 產品發展處副總經理）
---

# DevOpsDays Taipei 2026：AI Agent 重構 SDLC 演講心得

> 派哥親身觀察筆記，加上多年 Agentic SDLC 實戰觀點。  
> 完全無 AI 潤飾，是派哥所學、所思、所歷練的個人記錄。

---

## 核心洞察（派哥視角）

### 1. AI 是放大鏡，不是新問題

> AI 導入所遇到的困難——文件不完整、規範不清楚、程式碼沒有架構——這些問題在沒有 AI 時就已存在。AI 只是把這些問題放大，讓你不得不重視。

工程師需要轉變：從「不愛寫文件」→「能清楚表達工作內容」

---

### 2. 粒度（顆粒度）是比 TDD 更大的開發方法論

這是派哥著墨最多的一塊：

| 方法論 | 範圍 |
|--------|------|
| TDD | 測試驅動，偏實作層 |
| **粒度方法論** | 從需求 → 實作的完整過程，比 TDD 範圍更大 |

「顆粒度」決定了 AI 每個 Task 的邊界——太大走偏，太小碎片化。

---

### 3. GitHub Copilot Custom Agent + Skill 才完整

演講者提到 GitHub Copilot Custom Agent 可以「限制 AI 在某個特定角色上」，但派哥的觀點：

> **沒有搭配 Skill 是不足的。** 如果只是以 Task 作為上下文自動化生成程式碼，很容易走偏。

---

### 4. Agentic SDLC 的三大驗證問題（91APP 沒講清楚的）

演講中未深入的部分，但派哥認為最關鍵：

1. **需求上下文怎麼定義？**（copilot-instructions.md 規範）
2. **規範怎麼定義？**（單一任務的 DoD、驗收條件）
3. **人類介入時機點？** AI 做錯了你怎麼知道？從哪裡開始做錯的？

---

### 5. Skills 的邊界原則（派哥觀點）

> **不建議將 Business/Knowledge 包成 Skills。**

| 類型 | 適合 Skills？ | 原因 |
|------|-------------|------|
| 技術技能（deploy、lint、test）| ✅ | 技術是死的，規則固定 |
| 商業流程 | ❌ | 商業流程是活的、會變的 |
| 知識庫 | ❌ | 知識應該在記憶系統，而非限定技能 |

**Agent Skills = 讓 AI 框在某項特定技能上發揮。商業邏輯不應被框死。**

---

## 演講內容評述

| 主題 | 派哥評分 | 說明 |
|------|---------|------|
| PRD / User Story | 😐 普通 | 沒有 AI 也應該做好的基礎工 |
| Copilot 差異比較 | 🙂 尚可 | 文件問題早就存在，AI 只是放大器 |
| 粒度 / Tasking Flow | ✅ 有趣 | 點到為止，但沒深入——時間不夠 |
| Coding Agent 實作 | ⚠️ 不足 | 缺少驗證機制和人類介入設計 |
| Tasking Flow 圖 | ❌ 有問題 | 軟體開發不是 Task to Code 而已 |

---

## 相關概念連結

→ [[agentic-sop-to-work]] — SOP 工程化成 Agentic workflow
→ [[loop-engineering-agentic-ai]] — Loop Engineering 在 Agentic AI 的應用
→ [[claude-agent-five-layer-architecture]] — Agent 設定五層架構（CLAUDE.md/Skills 邊界）
→ [[ai-coding-team-cld]] — Claude + Codex 協作分工
