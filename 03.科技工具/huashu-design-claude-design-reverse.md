---
title: Huashu Design：Claude Design 逆向開源，一句 Prompt 生原型
tags: ["Claude Code", "Skill", "工具", "AI"]
date: 2026-04-21
category: AI工具
source: https://www.koc.com.tw/archives/639936
---

## 這是什麼

Anthropic 推出 Claude Design 四天後，中國開發者「花叔」（alchaincyf）逆向開源重構成 skill。核心主張：把商業工具的核心邏輯抽象化為開放 skill，無需訂閱即可用。

安裝：`npx skills add alchaincyf/huashu-design`

## 六大能力

- iOS/Web 互動原型生成
- HTML 簡報（可匯出 PPTX）
- 時間軸動畫（MP4/GIF）
- 即時參數微調設計變體
- 資訊圖表視覺化
- 五維度設計評審

支援 Claude Code、Cursor、Codex 等多個 agent。

## 質疑

- 前提假設：「逆向開源」不是真的看原始碼，而是透過 prompt 工程推斷流程再重構，效果上限取決於推斷是否準確
- 適用邊界：取代的是 GUI 操作的便利性，複雜設計系統仍需真人設計師判斷；一句 prompt 生出的原型適合快速驗證，不適合直接交付
- 潛在反例：Anthropic 可能收到版權爭議，skill 隨時可能被下架或限制

## 對標

- **Linux 對 Unix**：花叔的做法和 Linus 當年重新實作 Unix（不是複製程式碼，而是重現功能）本質相同——開源重構比直接複製更有持續性
- **女媧 skill 模式**：同一個 alchaincyf 做的，把名人思維蒸餾成 skill，現在把商業設計工具蒸餾成 skill，是同一套方法論

## 派哥實測（2026-04-28）

- PPT 功能：輸出直接可編輯（不是截圖，是真正可編輯的 PPTX）
- README 裡的每個動畫都是這個 skill 自己跑出來的
- 體感：「把某個專案變成可編輯的 PPT」這個場景完全成立

## 對派哥的啟示

這個模式對派哥的意義：任何商業 AI 工具，只要能透過 prompt 觸發，就有機會被重構成免費 skill。選工具時不必等官方，社群逆向版可能更快。

My Wallet Trip 的 UI 設計、sales report 的視覺化，可以試試 Huashu Design 出原型。
已有 `/huashu-design` skill 可直接在 Claude Code 調用。

## 連結筆記

- [[nuwa-skill]] → 同一個作者 alchaincyf
- [[personal-ai-vault-obsidian-system]]
- [[claude-code-powerup-guide]]
- [[impeccable-design-skill]]
