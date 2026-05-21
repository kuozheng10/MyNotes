---
title: Will AI Kill SaaS：Figma/Adobe 之死？Design to Code vs Code to Design
tags: ["AI", "架構設計", "工具", "工作流程"]
date: 2026-04-23
category: AI工具
source: 派哥整理
---

## 這是什麼

AI 衝擊設計類 SaaS（Figma、Adobe）的結構性分析。從軟體開發流程四個演化階段切入，說明為什麼「積極擁抱 AI」的公司還是可能死——因為死的不是技術，是流程模型。

Figma 從上市 $120 跌到 $20，Adobe 從 $400 跌到 $250。

## 四個開發流程演化階段

### 1. 傳統接力賽（The Relay Race）

老闆 → PM（PRD）→ Designer（Mockup）→ Engineer（Code）→ QA

痛點：降維傳達的溝通成本極高。每個環節都在猜上個環節的意圖。最快兩週一個循環。

### 2. Vibe Coding（直覺式）

Vision → AI → Code

繞過所有中間人。適合 Prototype，專案變大後技術債快速累積。

### 3. Contextual Coding（Cursor/Copilot 類）

（Vision + Context）→ AI Assistant + Engineer → Code

AI 理解 codebase 全局脈絡，工程師主導，AI 是外骨骼。設計和規格階段依然保留。

### 4. Agentic AI Workflow（同心圓迭代）

從線性接力變成輻射分派，最終收斂。

**Design to Code（由形入理）**：Vision → AI 同時生成規格、UI、邏輯 → 人類審批。團隊擴增的溝通邊際成本趨近於零。

**Code to Design（由理生形）**：底層架構或資料模型改變 → AI 反向推演，自動更新 UI 元件和設計文件。

過去：新增「VIP 積分」欄位 → PM 開票 → 設計師改 Figma → 前端刻圖 → 接後端。
現在：資料庫 schema 改動 → AI 自動同步 UI。

兩者循環：舊設計圖 + 舊程式碼餵給 AI → AI 更理解設計脈絡 → 產出更符合的程式碼 → 同步更新設計文件。

## 核心價值轉移

過去 80% 開發時間在把「想法」翻譯成「機器懂的語言」。AI 包辦這 80% 後，人類核心價值收斂到三點：

1. 定義問題（What to solve?）
2. 設定邊界與架構約束（How to scale and secure?）
3. 驗收結果（Is this what Customers want?）

## Figma/Adobe 的護城河還剩什麼

- **美學共識與品牌靈魂的錨點**：AI 快速生成幾百個介面，但確保符合特定 Design System（字體、間距、情緒、微互動）仍需控制中心
- **像素級精細控制**：「把這個陰影往左下移 2px 帶一點冷色調模糊」——AI 很難做到

## Claude Design/Code 在取代什麼

- 取代靜態設計稿：過去設計師畫圖 → 工程師切圖。現在直接產出可點擊的 React 元件
- 取代過度詳細的規格書：不只寫 code，能讀 codebase、理解目標，自己拆解工單

## 為什麼是 Bottom-Up 不是 Top-Down

傳統 SaaS 在企業中是 Top Down 推動。AI 工具反而是 Bottom Up——員工想偷懶自己裝，不用等公司決策。所以不需要等一代學生換血，速度快得多。

## 質疑

- 前提假設：「像素級控制是人類護城河」這個假設正在鬆動——Claude Design 的 Tweaks 功能已經開始做到即時調整參數；「2px 冷色調陰影」只是時間問題
- 適用邊界：分析的是中小型產品開發場景；大型企業的設計系統有複雜的組織政治和合規問題，AI 工具替換阻力更大
- 潛在反例：Figma 的護城河不只是工具，還有社群和教育生態（設計系課程綁定）；這個生態很慢才會被 AI 侵蝕

## 對標

- **打字機 vs Word + 印表機**：不是打字機廠商擁不擁抱技術的問題，是「整個流程模型」被取代了——Figma 面對的是同樣的結構性威脅
- **接力賽 vs 輻射網**：Figma 是為接力賽設計的中間交接站；輻射式 Agentic 工作流根本不需要中間站

## 對派哥的啟示

你現在的工作模式已經是 Agentic Workflow：Claude Code 輻射分派任務、一蘭做 Q&A、Gemini 研究。

Design to Code 對派哥最直接的落地：My Wallet Trip 的 UI 設計，不需要先畫 Figma，直接用 Claude Design 或 Huashu Design 出 HTML 原型，迭代夠了再刻成正式元件。

Code to Design 對派哥的意義：未來 My Wallet Trip 的 Notion schema 改了，理論上可以讓 AI 自動更新對應的前端元件，不用人工同步。

## 連結筆記

- [[huashu-design-claude-design-reverse]]
- [[claude-design-system-prompt-harness]]
- [[agentic-orchestration-cognitive-load-theory]]
- [[vibe-coding-architecture-debate]]
- [[stop-coding-agentic-era]]
