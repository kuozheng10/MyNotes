---
tags: [claude, skill, prompt-engineering, anthropic, agent-skills, productivity]
source: 社群貼文（AI新手村，TG 2026-06-23）
references:
  - Anthropic 官方〈Introducing Agent Skills〉2025-10-16
  - Anthropic 工程部落格〈Equipping agents for the real world with Agent Skills〉
  - Austin Marchese〈How Anthropic Engineers ACTUALLY Prompt Claude Code〉2026-05-15
date: 2026-06-23
---

# Anthropic 官方 Skill 三層架構 — 你只做了三分之一

> 多數人只寫到第二層就停了。Anthropic 工程師用同一份 skill 用一整年的秘密在這。

---

## 三層結構

| 層 | 名稱 | 作用 | 大家有沒有做 |
|----|------|------|------------|
| **1** | **描述** | Claude 自動判斷「什麼時候該用這個 skill」的依據 | 常跳過 |
| **2** | **指令** | 步驟操作手冊 | 幾乎人人都有 |
| **3** | **工具** | 範本、腳本、參考檔 | **99% 的人漏掉** |

---

## 範例：「每週工作週報」

**只有第二層（多數人）：**
- 步驟：整理本週 → 分類 → 寫三段
- 問題：每次還要重貼格式、重講分類規則

**三層齊全（Anthropic 工程師）：**
- 描述：「當我說『幫我整理本週週報』時，自動啟用」
- 指令：本週完成事項 → 已完成/進行中/卡關三類 → 固定語氣三段
- 工具：公司週報格式範本 ＋ 分類規則 ＋ 自動撈任務清單的腳本

打一句話 → 格式對、分類對、語氣也對。

---

## 工程師的反直覺做法

Anthropic 工程師 Eric 的觀點：

> 「大家花很多力氣寫超詳細的 prompt，卻給模型的工具簡陋到不行——參數叫 A、叫 B，沒有說明。換成工程師，他根本沒辦法用。」

工程師**把力氣花在附件（第三層）上**，而不是把指令寫得更漂亮。

---

## 最有感的例子：把腳本存進 skill

Claude 每次都重寫同一段 Python 來套投影片格式 → 把那段腳本「存進 skill 當工具」 → 下次直接重跑。

**為什麼這招強：**
- Code 是確定性的：同樣輸入，永遠同樣輸出
- AI 每次重新「猜」：燒 token、花錢、結果可能不一樣

> 一句話原則：**能用 code 解決的，就別讓 AI 每次重想。**（你不用自己會寫——讓 AI 幫你寫一次，之後重複用）

---

## 三個現實

1. **不是 prompt 寫不好，是少了「附件」** → 覺得 AI 不穩，先問：有沒有給現成範本/清單/腳本？
2. **第三層才是拉開差距的地方** → 描述、指令大家都會；工具才是在養資產
3. **與其潤飾指令，不如先補第三層** → 花十分鐘存一份範本，比改十次字有用

---

## 升級 Prompt 為三層 Skill 的模板

```
我想把「XX 任務」做成一個 skill。請幫我寫出三層：
（1）描述：讓 AI 能自動判斷何時該用它；
（2）指令：完成這件事的步驟；
（3）工具：列出它需要哪些範本、清單或腳本，並幫我把能用 code 做的部分寫出來。
```

---

## 對派哥的評估

✅ **直接相關**：
- 派哥用 Claude Code skills（`~/.claude/skills/`）就是這套架構
- 現有 skill 大多只有 SKILL.md（第一 + 第二層）
- 第三層可以加：固定格式的 frontmatter 範本、SQL 查詢、Python snippet

💡 **可考慮做的：**
- 檢查現有 skill 有沒有附第三層工具
- 常用的 Python 腳本段落可以直接存入對應 skill

---

## 相關筆記

- [[claude-skill-social-post]] — Claude Code skill 社群分享
- [[agentic-sop-to-work]] — Agentic SOP 實務
