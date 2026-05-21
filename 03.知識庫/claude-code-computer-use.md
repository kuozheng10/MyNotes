---
title: "Claude Code Computer Use"
tags: [claude-code, computer-use, mac, automation, ui-testing]
date: 2026-03-31
category: 03.科技工具
source: https://code.claude.com/docs/en/computer-use
---

## 摘要

> Claude Code 的 Computer Use 功能，讓 Claude 直接控制 Mac 螢幕：點擊、輸入、截圖、開 App，像人一樣操作 GUI。可用於 native app 測試、視覺 bug 重現、iOS Simulator 自動化。

## 能做什麼

| 使用情境 | 說明 |
|----------|------|
| 驗證 native build | 寫完 app → Claude 自動編譯、啟動、點每個按鈕截圖 |
| 視覺 bug 重現 | 告訴 Claude bug 描述 → 自動縮窗截圖 + 修 CSS 驗證 |
| iOS Simulator | 跑 onboarding flow，不用寫 XCTest |
| 無 API 的工具 | 設計工具、硬體控制面板等 GUI-only 工具 |

## 需求

- macOS 限定（不支援 Windows/Linux）
- Claude Code v2.1.85+
- Pro 或 Max 方案
- 必須用 claude.ai 帳號（不能用 Bedrock/Vertex API key）
- 互動式 session（-p 非互動模式不支援）

## 開啟方式

```
/mcp → 找 computer-use → Enable
```

授權兩個 macOS 權限：
- Accessibility（點擊/輸入/滾動）
- Screen Recording（看螢幕）

## 安全機制

- 每個 App 需要單獨授權（per-session）
- Terminal 視窗不會被截圖（防止 prompt injection）
- 按 `Esc` 可隨時中斷
- 同時只有一個 session 能控制螢幕

## 使用範例

```
Build the MenuBarStats target, launch it, open the preferences window,
and verify the interval slider updates the label. Screenshot when done.
```

```
The settings modal clips its footer on narrow windows. Resize the app
window until you reproduce it, screenshot the clipped state, then fix the CSS.
```

## 適用場景（my-wallet-trip）

- 讓 Claude 直接開 Safari 測試 PWA 介面
- 截圖驗 layout（不用手動截圖給 Claude 看）
- 測試 iOS Simulator 的 expense 新增流程

## 參考

- [Computer use in Desktop](https://code.claude.com/docs/en/desktop#let-claude-use-your-computer)
- [Safety guide](https://support.claude.com/en/articles/14128542)
- [[my-wallet-trip-setup]]
