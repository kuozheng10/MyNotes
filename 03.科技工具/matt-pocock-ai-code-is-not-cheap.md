---
title: Matt Pocock：AI 越強，軟體設計基礎越重要 — Code is Not Cheap
tags: [claude-code, AI開發, 軟體設計, TDD, DDD, deep-module, grill-me, 架構, vibe-coding]
date: 2026-04-28
category: AI工具
---

## 核心論點

Specs to code / Code is cheap → **完全相反**
AI 越強，好 codebase 的價值越高——壞 code 從來沒這麼貴過。

---

## 為什麼 Specs to Code 會越改越爛

每次只想到當下的改動、不管整體設計 → **軟體熵**（software entropy）
Specs to code = 把熵增過程**自動化**

- John Ousterhout《A Philosophy of Software Design》：複雜 code = 難以理解和修改的 code
- Pragmatic Programmer：爛 codebase = 難改的 codebase
- 每跑一次 specs compiler，codebase 就更亂一點

---

## 四大失敗模式

### 失敗模式一：AI 做出來的不是你要的

**原因**：你和 AI 之間從來沒有對齊過 design concept（那個飄在合作者之間、看不見的共識）

**解法**：grill me skill
→ 「無情地拷問我這個計畫的每個面向，沿著 design tree 走下去，一個一個解決決策之間的依賴，直到達成共識」
→ AI 會問 40-100 個問題才動手
→ 對話紀錄可直接整理成 PRD 或 issue

比 Claude Code 預設的 plan mode 更好：plan mode 太急著生 markdown，grill me 逼你先把腦袋裡飄忽的東西挖乾淨

### 失敗模式二：AI 太囉唆，跟你不在同一個頻道

**原因**：語言落差（和領域專家合作的同樣問題）

**解法**：Ubiquitous Language（Domain-Driven Design 的概念）
→ 建立專案專用詞彙表（markdown table）
→ 規劃時開著這份檔，對話也引用它
→ AI 的 thinking trace 開始用更精準、更短的語言思考
→ 實作更貼近原本設計

### 失敗模式三：AI 寫了，但跑不起來

**原因**：AI 預設超速駕駛——一次寫一大坨，最後才想到 type check / test

Pragmatic Programmer：「The rate of feedback is your speed limit」
→ 反饋速度就是速限，AI 一直在超速

**解法**：TDD（Test-Driven Development）
→ 先寫測試，讓它 fail，寫一點 code 讓它過，再 refactor
→ 逼 AI 一小步一小步走

**但**：好測試需要好 codebase → 繞回設計問題

### 失敗模式四：你的腦袋跟不上 AI 的速度

**原因**：AI 產出的 shallow modules codebase 難讓人腦裝載
→ 每次改動都要把一大堆細節重新塞進腦子

**解法**：Deep modules + 灰盒設計

---

## 核心概念：Deep Modules vs Shallow Modules

| 類型 | 介面 | 功能 | AI 傾向 |
|------|------|------|---------|
| Deep module | 簡單 | 豐富（藏在裡面）| 不擅長產出 |
| Shallow module | 複雜 | 少 | 天然傾向 |

**AI 特別擅長產出 shallow modules**：一堆小零件、到處都是介面和依賴
→ AI 自己回頭探索時也找不到路，修改通常歪掉

**解法**：improve codebase architecture skill
→ 掃描 codebase，找散落各處的相關 code，包進 deep module
→ 邊界乾淨後，TDD 才跑得起來

---

## 最核心的一句話

> **Design the interface, delegate the implementation.**
> 介面你設計，實作交給它。

- 寫 PRD 時要明確指出哪個 module 會被改、介面要怎麼變動
- Module map 要成為 ubiquitous language 的一部分
- Kent Beck：「Invest in the design of the system every day」

Specs to code = divest（從系統設計裡抽走）
每跑一次 compiler，你跟系統設計的距離就遠一點

---

## AI 時代需要懂多深？

不需要會手寫每一行，但要能：
- 設計介面
- 判斷模組邊界
- 知道什麼時候該介入

懂這些 → AI 是 10 倍工程師的槓桿
不懂 → AI 是 codebase 熵增加速器

---

## 對派哥的意義

- **grill me** 已在知識庫，這篇說明了它存在的理由
- **設計介面** 的能力比寫 code 更關鍵——你已經在做（和 Codex 分工就是這個原則）
- **Ubiquitous Language**：CLAUDE.md / skill 文件 = 你和 Claude 之間的共用詞彙
- cc_processor / My Wallet Trip 改功能前，先問「哪個 module 的介面要變」，比直接改 code 更有效

---

## 連結筆記

- [[grill-me]] — 對應失敗模式一的解法
- [[ai-coding-qa-myths]] — 相關的 AI 開發誤區
- [[vibe-coding-architecture-debate]] — vibe coding 的架構爭議
- [[karpathy-skills-claude-coding-rules]] — Karpathy 的 AI 開發規範
- [[stop-coding-agentic-era]] — 停止 coding，擁抱 agentic 時代
- [[ai-agent-system-design-over-prompt]] — 系統設計勝過 Prompt
