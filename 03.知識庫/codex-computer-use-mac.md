---
title: Codex Computer Use——AI 直接操控 Mac 視窗
tags: [Codex, AI工具, Computer Use, 自動化, Mac]
date: 2026-05-23
category: 科技工具
---

## 這是什麼

OpenAI Codex 的 Computer Use 功能，讓 AI 直接看著當前 Mac 畫面、點擊、切換、操作視窗。
比 Claude Computer Use 更進一步，整台電腦都能控制。

---

## 啟用方式

1. **開 Mac 權限**：系統設定 → 隱私權與安全性 → 螢幕錄製 + 輔助使用，給 Codex 權限
2. **在 Codex 輸入啟用指令：**

```
@Computer 請幫我操作目前的 Mac 視窗。
```

（中文版也可以用 `@電腦`）

---

## 使用範例

```
@電腦 請幫我操作 Chrome。
@電腦 請幫我操作 Finder。
@電腦 請幫我操作目前這個視窗，幫我點到 ___。
```

---

## 適合哪些場景

- 重複性 UI 操作（找設定、切視窗）
- 無 API 的桌面 App 自動化
- 結合 Codex 指令，讓 AI 跑完整個工作流程

---

## 注意

- 需先有 Codex 環境（`npm i -g @openai/codex` 或已安裝）
- Computer Use 屬於高權限功能，授予螢幕錄製前確認信任來源

---

## 相關

- [[codex-workflow]] — Codex 在派哥工作流的分工定位
