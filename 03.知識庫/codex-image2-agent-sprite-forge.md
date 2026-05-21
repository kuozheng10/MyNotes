---
title: Codex Image2 × agent-sprite-forge：一句 Prompt 生成 2D 遊戲 Sprite
tags: ["Codex", "Image生成", "2D遊戲", "Sprite", "開源", "agent"]
date: 2026-04-25
category: AI工具
source: Telegram 派哥分享 + https://github.com/0x0funky/agent-sprite-forge
---

## 這是什麼

agent-sprite-forge 是一個 Codex Skill，讓你用一句自然語言 prompt 生成遊戲用的 2D Sprite sheet、透明 PNG 幀、和動態 GIF。

**核心賣點**：Codex 內建 Image2（圖像生成能力）+ Python 後處理，全流程不需要外部 API、不需要 Canva 手動去背。

---

## 完整流程（全部 Codex 一手包辦）

1. **Prompt 設計** — 用自然語言描述角色、動作、風格
2. **Image Gen** — Codex Image2 生成原始 sprite sheet
3. **Cleanup** — chroma-key 去背、frame 切割、bounding-box 對齊
4. **Transparent PNG** — 輸出透明背景的獨立幀
5. **Animated GIF** — 組合成可直接使用的動畫

生成完後 agent 還會自動 review、微調，直到輸出乾淨為止。

---

## 可以生成的素材類型

- 角色、NPC、怪物的行走四方向動畫
- 技能施放、投射物、衝擊特效
- 爆炸、FX 特效 sheet
- Unit bundle、Spell bundle、Combat bundle
- 以參考圖片為基礎的衍生 sprite

---

## 技術架構

| 層 | 工具 |
|----|------|
| Agent 規劃 | Codex（決定素材類型、動作、幀數、排列策略） |
| 圖像生成 | Codex Image2（內建，不需外部 API） |
| 後處理 | Python（Pillow + NumPy） |
| 輸出格式 | 透明 PNG / sprite sheet / animated GIF |

---

## 為什麼值得注意

- **Image2 穩定度提升**：sprite sheet 的多幀一致性過去是生成式 AI 的弱點，現在明顯改善
- **不需串接 API**：去背、格式轉換全在本地 Python 跑，沒有 token 成本
- **Agent self-review**：生成後自動檢查品質並微調，是 agentic loop 的實際應用案例
- **開源 MIT**：可直接拿來改造或整合進自己的 skill 體系

---

## 對派哥的啟示

**短期不需要行動**，但有兩個值得記住的概念：

1. **Codex Image2 的能力邊界擴大了**：不只是截圖分析，現在連 game asset 生成都能做。下次有視覺素材需求可以優先試 Codex，不要直接跳到外部 API。
2. **Agent + deterministic post-processing 的模式**：AI 做創意，Python 做精確後處理（chroma-key、frame alignment）。這個分層是值得複用的架構模式。

---

## 連結筆記

- [[free-claude-code-proxy-design-analysis]] — 格式適配層：AI 輸出 → 下游系統，同樣的中間層概念
- [[harness-engineering]] — agent self-review loop = feedback sensor 的具體實作
- [[agent-skills-standard]] — 把 sprite-forge 這類工具包成 skill 的標準方式
