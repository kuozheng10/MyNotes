---
tags: [ai-coding, workflow, claude, gemini, antigravity, ide, local-ai]
source: 社群分享（TG 2026-06-22）
date: 2026-06-22
---

# Claude + Antigravity：個人地端 AI 助理開發工作流

> 作者 7 天熬夜，全自動模式讓 AI 寫了 26,346 行程式碼，整理出這套開發環境。

---

## 模型分工

| 模型 | 用途 | 特性 |
|------|------|------|
| **Claude Opus 4.8** | 核心程式碼、複雜模組 | 邏輯推理強、穩定、貴 |
| **Gemini 2.5 Flash** | 查資料、寫文件、小幅微調、發想 | 極快、便宜、可同時跑不影響 Opus |

> ⚠️ 原文寫「Gemini 3.5 Flash」，實際上不存在此版本，正確為 **Gemini 2.5 Flash**。

**工作流程：**
1. 有新想法 → 先讓 Gemini 寫成企劃書
2. 轉交 Opus 4.8 開發核心邏輯
3. 查程式碼 / 問問題 → 用 Gemini（速度快、不打斷 Opus）

---

## Antigravity IDE 雙工具佈局

```
┌──────────────────────────────────────────────────┐
│  文件 (上)      │  Chat (右) → Gemini 2.5 Flash  │
│─────────────────│────────────────────────────────│
│  資料夾 (左)   │  終端機 → Claude Opus 4.8       │
└──────────────────────────────────────────────────┘
```

- **終端機**：呼叫 Claude Opus 全自動寫程式碼
- **右側 Chat**：問 Gemini 問題、查資料
- 不需在多視窗間切換，一人兼顧架構與細節

---

## 版本控制原則

- 全自動模式必須搭配 **Git 版本控管**
- 每次 commit 寫清楚說明，保留回退機會
- Claude 內建安全機制：沒要求 Push 不會主動執行；不會主動刪除雲端備份

---

## 成本估算

| 項目 | 費用 |
|------|------|
| Claude 訂閱 | 付費方案（可先試免費 7 天） |
| Gemini 訂閱 | Google 方案近期大幅降價 |
| **兩者合計** | **每月千元有找（TWD）** |

---

## 評估（對派哥的適用性）

✅ 模型分工邏輯與 CLAUDE.md 的「Gemini 研究 / Claude 實作」完全一致  
✅ 全自動 + Git 的安全感符合派哥現有習慣  
⚠️ Antigravity IDE 是新工具，目前派哥主力用 Claude Code CLI，切換成本需評估  
💡 Gemini 2.5 Flash 的「先寫企劃書再交 Opus」這個模式值得試試

---

## 相關筆記

- [[ai-coding-team-cld]] — AI 時代 WIP 天然煞車消失的 CLD
- [[ai-testing-agile-quality]] — Eval Gate + 品質把關實踐
- [[loop-engineering-agentic-ai]] — Loop Engineering 基礎
