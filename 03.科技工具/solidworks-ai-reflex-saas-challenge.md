---
title: SolidWorks AI 挑戰：用 Reflex 0.9 做工業設計 SaaS + AI 協作
tags: [Reflex, Python, SaaS, AI協作, 機械設計, 工業軟體, Agent, 共編]
date: 2026-05-07
category: AI工具
---

## 這是什麼

有人用 Python Reflex 0.9，花幾小時做出一個可以讓 AI Agent 操控的 3D 機械設計 SaaS，直接挑戰年費 9 萬的 SOLIDWORKS。

---

## 白話文版

**問題**：台灣機構工程師都在用 SOLIDWORKS，貴、不能 AI 協作、也不能讓遠端專家一起改圖。

**他的實驗**：
1. 用 Python Reflex 把 SOLIDWORKS 功能寫成 Web App（SaaS）
2. 改成 HackMD 左右分割介面：左邊打指令，右邊即時顯示 3D 圖
3. Reflex 0.9 內建 AI Agent endpoint → AI 可以直接操控這個設計軟體
4. 寫一個 agent bridge → 在 VSCode 裡用 GitHub Copilot 選任何 AI 幫你設計機構
5. 搞不定的問題，直接把連結傳給專家朋友，一起線上改圖

**結論**：
- 軟體本身成本 = 0
- 唯一費用 = AI Agent 費用
- AI 解不了就叫專家上來共編

---

## 核心技術：Reflex 0.9

| 特點 | 說明 |
|------|------|
| Python 全端 | 前後端都 Python，不用學 JS |
| 內建 AI Agent endpoint | App 天生支持 AI 溝通，不用額外串接 |
| 即時共編 | 類 HackMD 的協作體驗 |
| SaaS 即開即用 | 有瀏覽器就能用，不用安裝 |

---

## 更大的問題

不只機械設計——醫療、汽車、IC 設計、電路設計，所有需要專業桌面軟體的領域：

> **是否都應該直接原生支援 AI 協作 ＋ 專家共編？**

這個問題的答案幾乎是「是」，但傳統軟體廠商還沒跟上。

---

## 對派哥的應用

| 場景 | 用法 |
|------|------|
| Python 全端 Web App | 用 Reflex 替代 Next.js，省 JS 學習成本 |
| 任何工具加 AI endpoint | My Wallet Trip 或 cc_processor 可以考慮類似架構 |
| 協作連結 | 設計稿/報表直接傳連結讓對方編輯，不用來回傳檔案 |

---

## 連結參考

- [[open-design-claude-design-opensource]] — 類似概念：BYOK 讓 AI 當設計師
- [[ai-kill-saas-figma-design-to-code]] — AI 時代的 SaaS 設計趨勢
- [[one-person-saas-rebellion]] — 一人 SaaS 的可行性
