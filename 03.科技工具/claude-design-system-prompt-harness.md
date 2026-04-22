---
title: Claude Design System Prompt 逆向解析：340行的 Harness Engineering 教科書
tags: ["Claude Code", "Harness", "Agent", "System Prompt", "設計"]
date: 2026-04-22
category: AI工具
source: 派哥整理
---

## 這是什麼

Claude Design 的 340 行 system prompt 被逆向工程取出。這不是工具說明書，而是把資深設計師的品味、紀律、手感一起編碼進去的完整訓練檔。分析後可拆成五個層次。

## 五層架構

### L1 身份與護欄

告訴 agent「你是誰」，定義角色邊界與不能做的事。越上層越定性。

### L2 設計品味

整層不教工具，只講什麼叫好設計、哪些模式要避。AI slop 反面清單：
- 浮濫漸層背景
- 非品牌 emoji
- 圓角容器加左邊框強調色
- SVG 畫插圖
- 爛大街字型（Inter、Roboto、Arial、Fraunces、system fonts 全點名）

三條內容紀律：先建立設計系統再動手、不塞 filler content、加東西前先問使用者。

### L3 工作流程

Agent 的可執行路徑：
理解需求 → 探索資源 → 列 todo → 搭建並早呈現 → 完成驗證 → 極簡總結

`questions_v2` 工具強制「至少 10 題，其中至少 4 題是 problem-specific」——把「問對問題」變成強制流程，不是靠 agent 自己判斷。

### L4 工具與協議

- **驗證流程**：`done`（同步讀 console）+ `fork_verifier_agent`（背景另開 iframe 深檢）。設計原則：**silent on pass**，驗過不打擾主 agent，避免 context 被「沒事」的 feedback 污染
- **Tweaks live 編輯**：postMessage 協議，agent 註冊 listener 通知 host ready，host 把值傳回，用 `/*EDITMODE-BEGIN*/.../*EDITMODE-END*/` comment marker 精準改檔

### L5 技術規範

每一條都是踩過坑的硬教訓：
- React/Babel 必須釘版本 + integrity hash（防 CDN 污染）
- 全域 styles 物件必須用元件名 prefix（避免名稱碰撞崩潰）
- 禁用 scrollIntoView（會破壞宿主 web app）
- slide 標籤強制 1-indexed（人類不說「第 0 張」）

## 核心洞見

使用者請求 → 穿過五層 Guide → 中央 agent 生成迴路 → HTML artifact → Sensor 驗證 → 交付

這是教科書等級的 harness engineering：品味、紀律、工具、技術邊界全被前饋編碼進 prompt。Agent 不是「無限自由發揮」，而是在 guard rail 裡做有品味的選擇。

## 質疑

- 前提假設：逆向工程取得的 prompt 可能不完整，或是已過時的版本；Anthropic 隨時可能更新，這份分析有時效性
- 適用邊界：這套 harness 是針對 HTML artifact 生成場景設計的，搬到其他 agent 系統（純文字、API 呼叫）需要重新設計各層；L5 的技術規範高度 context-specific
- 潛在反例：強制 10 題問題的流程在需求明確時反而增加摩擦；「先建設計系統再動手」在快速 prototype 場景可能過重

## 對標

- **軍隊作戰手冊**：把老兵的判斷力編碼成新兵能執行的 SOP——L2 設計品味就是 Anthropic 的「老兵直覺」，L3-L5 是讓新 agent 能執行的步驟
- **建築師的規範書**：L1 是建築理念，L5 是施工圖的尺寸公差——上層定方向，下層保品質

## 對派哥的啟示

一般人看不到真實產品的 harness 怎麼設計。這 340 行是少見的公開案例，可以直接套用到自己的 agent 系統設計：

- 你的 CLAUDE.md 已有 L1（角色）+ L3（流程），但缺 **L2 品味層**（什麼叫好的 Python/回報？反面清單是什麼？）
- `silent on pass` 原則值得借鑑：驗證通過就不回報，減少 context 噪音
- `questions_v2` 的強制 10 題可以變成 SBE 的標準 checklist

## 連結筆記

- [[huashu-design-claude-design-reverse]]
- [[harness-engineering]]
- [[ai-agent-system-design-over-prompt]]
- [[claude-md-optimization]]
