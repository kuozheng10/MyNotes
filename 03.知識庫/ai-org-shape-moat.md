---
title: "未來公司真正的護城河：組織形狀即護城河"
tags: [AI, 架構設計, 工作流程, 組織知識工程]
date: 2026-05-13
category: 系統架構
source: Telegram 派哥分享
---

## 核心論點

> 護城河不是技術，不是資料，而是**組織形狀**。

Foundation Capital Jaya Gupta：AI 時代最難複製的不是模型或算力，而是「誰站在哪個位置、有什麼權限去做哪些決定」的內部結構。

公式：**組織形狀 = 對的人 + 對的位置 + 對的權限**

## 為什麼重要

- 喊 AI 轉型戰略容易，但 AI 落地是從下到上長出來的，不是從上往下宣布的
- 護城河的判斷標準：**這個組合是否難以被外部複製？**
- 三個難複製的案例：
  - OpenAI：把研究員直接放在產品決策鏈上
  - Palantir：Forward Deployment（工程師嵌入客戶端現場）
  - Tesla：軟體工程師 + 製造業工程師融合在同一團隊

## 隱藏的護城河人才

企業裡最被低估的人，往往是「懂 context 的人」：

- PM who can code（不是工程師，但能判斷技術可行性）
- 財務人員 who 懂流程全貌（不只是算數字，而是看流程斷點）
- 客服人員 who maintains SOPs（實際知道哪些流程是活的、哪些已經爛掉）

這些人是 AI 流程設計的真正架構師，而不是 AI 工具使用者。

## 三個可行動步驟

1. **從真實流程出發**：不要問「我們能用 AI 做什麼」，問「這件事現在誰在做、怎麼做、什麼卡住了」
2. **找隱性 context 持有者**：財務、客服、PM 等跨職能的人，他們知道流程的真實樣子
3. **重新定義權限**：讓對的人有權限修改 SOP、調整 AI prompt，不要所有改動都卡在 IT

## 對派哥的啟示

cc_processor 的架構其實就是這個邏輯的個人版本：

- 派哥是唯一知道「帳單怎麼處理才對」的人 → 就是那個隱性 context 持有者
- CLAUDE.md 裡的每條規則都能追溯到某次失敗 → 就是 Ratchet（組織學習固化）
- 只有派哥能改 CLAUDE.md → 這是「對的人有對的權限」

**實際可做的事**：
- cc_processor 每個 adapter 加上「誰理解這段流程」的備註 → 防止未來 handover 斷掉
- 找出派哥工作流裡的「隱性 context」文件，把它們顯性化寫進 CLAUDE.md 或 skill

## 連結筆記

- [[enterprise-ai-adoption-strategy]] — 企業 AI 導入策略（由上到下 vs 由下到上）
- [[enterprise-ai-roles-prediction]] — AI 時代新職能（Skills 規劃師、龍蝦架構師）
- [[addy-osmani-harness-engineering-deep-dive]] — Ratchet 原則（錯誤轉規則）
- [[claude-code-ai-dev-team-design]] — 4層架構 = 組織形狀的技術版本
- [[vibe-vc-five-ai-employees-mac-mini]] — 5 AI 員工 = 組織形狀落地實作
