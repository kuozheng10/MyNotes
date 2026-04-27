---
title: Figma Design System Workflows Skill — Codex 自動抽 Component、整理 DS
tags: [figma, design-system, codex, skill, UI設計, component, 自動化]
date: 2026-04-28
category: AI工具
source: https://github.com/chelswcs/figma-ds-workflows
---

## 這是什麼

用 Codex + Figma MCP 自動從畫面抽取 Design System 的 CLI skill。
解決設計師「畫面做完但超不想整理 component」的懶癌問題。

GitHub: https://github.com/chelswcs/figma-ds-workflows

---

## 兩個 skill

| Skill | 用途 |
|-------|------|
| DS 抽取 | 從現有畫面識別可重用元素，建立 component，套回原稿（換成 instance）|
| DS 審計 | 檢查現有 library 的結構問題（命名重複、標題不對齊、分類不一致）|

---

## 核心哲學：不是「全部都抽」

AI 會判斷：
- ✅ 要抽：button、card 等可重用的 UI pattern
- ❌ 不抽：單頁 layout、裝飾元素

「選擇性抽取」比「componentize everything」更重要。

---

## 工作流程

```
1. 先做 1-2 個頁面把風格定下來
2. 丟給 Codex skill
3. 它識別可重用 UI pattern
4. 建立基礎 component
5. 回頭把原稿換成 instance
6. （可選）跑 DS 審計確認命名一致性
```

---

## 技術棧

- Codex（Anthropic CLI）
- Figma MCP（需預先設定）

---

## 對派哥的意義

- My Wallet Trip UI 改版時可用：先做幾頁 → 丟 skill 整理 DS
- 個人品牌素材有重用需要時適用
- 目前沒有 Figma 重度使用場景，**備用**即可

---

## 連結筆記

- [[huashu-design-claude-design-reverse]] — Claude Design 逆向 skill（同類工具）
- [[impeccable-design-skill]] — 設計品質提升 skill
- [[ui-ux-design-resources-collection]] — UI/UX 設計資源
- [[awesome-design-systems]] — Design System 參考資料
