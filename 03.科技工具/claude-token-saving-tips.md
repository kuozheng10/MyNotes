---
title: Claude Token 省錢攻略 — 10 個技巧最高省 65%
tags: [Claude Code, AI, 工具, 工作流程, 自動化]
date: 2026-04-09
category: AI工具
source: https://www.koc.com.tw/archives/638387
---

## 這是什麼

使用 Claude（尤其 Claude Code CLI）的 10 個省 Token 實戰技巧，搭配 `save-token.skill` 可省最高 65%。

---

## 10 個核心技巧

| 技巧 | 重點 |
|------|------|
| 選對模型 | 簡單任務用 Haiku，複雜才用 Sonnet/Opus |
| /clear 習慣 | Context 堆疊是倍數燒，定期清空 |
| 封裝 Skill | SOP 寫成 Skill，減少來回 Turn 數 |
| Prompt Caching | 重複背景資料快取可省 90% 輸入成本 |
| 批次思考 | 一次提問含完整背景 + 多子任務 |
| 限制輸出 | max_tokens 或 Prompt 要求「簡短」 |
| Temperature 0.5–0.7 | 穩定性高、廢話少、錯誤重試少 |
| Batch API | 非即時任務走 Batch，更便宜 |
| 精確指令 | Few-shot 範例 > 模糊描述 |
| 監控用量 | 建立成本意識，不要不知不覺燒爆 |

---

## save-token.skill 核心邏輯

- **指令壓縮**：複雜 SOP → 單一指令
- **減少回合**：單次 Turn 完成「分析→執行→驗證」
- **實測**：中大型程式專案 Token 省 65%

---

## 對派哥的啟示

- `~/.claude/skills/` 裡每個 skill 都是省 Token 的投資，一次寫好、反覆用
- `/clear` 和 `/compact` 是最低成本的省錢習慣，閒置 >1h 也應該破 cache
- MyNotes SOP 已做到「批次思考」：一次 prompt 給完整背景
- 中文 system prompt 改英文已在做（參考 agent-prompt-token-cost）

---

## 連結筆記
- [[agent-prompt-token-cost]] — 中文 token 爆量問題，互補
- [[agent-skills-standard]] — Skill 資產化實作
