---
title: NotebookLM 整合進 Gemini — 個人知識庫進入新階段
tags: [notebooklm, gemini, google, 知識管理, 知識庫, MyNotes]
date: 2026-04-09
category: AI工具
---

## 這是什麼

Google 宣布 NotebookLM 核心功能直接內建進 Gemini 平台。
不再需要兩個工具切換，一個平台搞定：上傳資料 → 建立知識庫 → AI 對話分析。

---

## 四大新能力

1. **個人專屬知識庫**：上傳文件/PDF/筆記 → 建資料夾 → Gemini 直接對這些資料問答
2. **深度問答**：不是問網路，是問你自己的資料，幻覺大幅降低
3. **跨文件整合分析**：多份文件同時上傳，找出不同資料間的關聯
4. **資料夾式專案管理**：不同專案/主題分開管理

---

## 對派哥的直接影響

### 🔥 最大機會：MyNotes × Gemini 查詢省 token

現在「問知識庫」要跑 Claude Code，每次消耗大量 token。
**新做法**：把 MyNotes/03.科技工具/ 的 md 批次上傳到 Gemini 資料夾
→ 日常查詢直接在 Gemini 問，0 Claude token
→ Claude 只負責「新增筆記/SOP」這段有創作價值的工作

### 工作流建議

| 任務 | 用誰 | 原因 |
|------|------|------|
| 查既有知識（問知識庫）| Gemini + NotebookLM | 免費/便宜，資料在裡面 |
| 新增筆記、SOP 分析 | Claude Code（我）| 需要判斷力 |
| 生簡報 | NotebookLM Slides | 已有 skill |
| 健檢 / 找連結 | Claude Code | 複雜推理 |

### 與現有工具的定位

```
MyNotes（原始 md，GitHub）
    ↓ 批次上傳
Gemini NotebookLM（查詢用，不修改）
    ↑ 新增/更新
Claude Code SOP → git push → MyNotes
```

---

## 需要跟 MyNotes 整合嗎？

**需要，而且可以做到：**

- Obsidian 已有 md 檔 → 直接上傳到 Gemini 資料夾
- 建議每週或每次大量新增後同步一次
- 不需要自動化，手動上傳即可（量不大）

**限制**：
- Gemini 資料夾不會自動 git sync，需手動上傳
- 適合「讀」，不適合「寫」（寫還是回 MyNotes git）

---

## 連結筆記
- [[notebooklm-slides-advanced]] — NotebookLM 生簡報 + Graphify
- [[obsidian-llm-knowledge-management]] — Obsidian + LLM 知識管理
- [[llm-knowledge-base-karpathy]] — Karpathy 的知識庫觀點
- [[claude-token-saving-tips]] — Claude 省 token 策略
