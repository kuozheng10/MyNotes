---
title: guizang-ppt-skill：一句 prompt 出雜誌風 PPT（單檔 HTML）
tags: ["PPT", "Claude Code", "Skill", "設計", "HTML", "開源"]
date: 2026-04-25
category: AI工具
source: Telegram 派哥分享 + https://github.com/op7418/guizang-ppt-skill
---

## 這是什麼

Claude Code Skill，輸入文字 → 輸出單檔 HTML 投影片，走「數位雜誌 × 電子墨水」美學，對標 Monocle 雜誌設計風格。不需要任何 build 工具，直接瀏覽器打開。

**核心特點**：AI 做出來的 PPT 不像 AI 做的——有排版美感、設計感。

---

## 安裝

```bash
git clone https://github.com/op7418/guizang-ppt-skill.git ~/.claude/skills/guizang-ppt-skill
```

---

## 觸發詞

在 Claude Code 裡說：
- 「幫我做一份雜誌風 PPT」
- 「horizontal swipe deck」
- 「editorial magazine style presentation」

---

## 內建資源

**5 套主題色**：
- Ink Classic（墨水）
- Indigo Porcelain（青花瓷）
- Forest Ink（森林墨）
- Kraft Paper（牛皮紙）
- Dune（沙漠）

**10 種版面**：封面、章節分隔、數據頁、雙欄、圖片格、流程圖、問題頁、引言、對比（前後）、混合內容

**技術細節**：WebGL 背景動效（hero 頁）、鍵盤/滾輪/觸控/點導覽、無依賴單檔 HTML

---

## 適合用在

✅ 現場演講、產品發表、個人風格演說、業界分享
❌ 大量資料表格、教學材料、多人協作編輯

---

## 工作流程

1. 說清楚需求（對象、時長、主題、圖片、限制）
2. Skill 從 assets/template.html 起手，填內容
3. 用 references/ 裡的版面骨架組合
4. 自動對照 checklist.md 品質檢查
5. 輸出可直接在瀏覽器預覽的 HTML

---

## 對派哥的啟示

**立刻可裝**：git clone 一行搞定，不需要額外設定。

用途：
- MyNotes 的知識整理做成簡報分享
- 任何需要一份乾淨投影片的場合

已有的 ppt-master-ai-ppt 是另一種做法（Markdown → reveal.js），這個走單檔 HTML + 雜誌美學，兩者可以視場合選。

---

## 連結筆記

- [[ppt-master-ai-ppt]] — 另一個 PPT 工具（Markdown + reveal.js 風格）
- [[claude-code-powerup-guide]] — Claude Code Skill 生態
- [[agent-skills-standard]] — Skill 安裝與管理規範
