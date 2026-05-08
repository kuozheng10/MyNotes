---
title: Codex Chrome Plugin：直接控制已登入的 Chrome
tags: [Codex, Chrome, 瀏覽器自動化, OpenAI, Playwright替代]
date: 2026-05-09
category: AI工具
---

## 核心功能

OpenAI Codex App 推出 Chrome Plugin，可以直接控制已開啟並登入的 Chrome 瀏覽器，不需要 Playwright 模擬登入流程。

使用方式：

```
@chrome，幫我檢查今天的 Gmail 郵件
```

Codex 會開啟一個受控分頁，操作完畢後將結果回傳 Codex App。

---

## 安裝方式

1. 更新 Codex App 到最新版
2. 在 Codex App 的「Plugins」中找到 Chrome
3. 安裝後 Chrome 會出現對應 Extension
4. 不是從 Chrome Web Store 安裝，必須從 Codex App 內安裝

---

## 為何重要（對比 Playwright）

| 方法 | 登入狀態 | 被 Bot 防護擋 | 難度 |
|------|---------|------------|------|
| Playwright（新 browser） | 需自己登入 / 帶 Cookie | 容易被擋（Akamai 等） | 中 |
| Codex Chrome Plugin | 直接用已登入的 Chrome | 理論上難區分真人 | 低 |

**實際案例**：長榮酬賓機位查詢被 Akamai 擋，Playwright 即使加 stealth 設定也 403。用 Codex Chrome Plugin 有機會繞過，因為是真實 Chrome session。

---

## 與 Claude Code 的差異

Codex 正在對齊 Claude Code 的功能（Claude Code 也有 `claude-code-chrome-builtin` 功能）。目前兩者在瀏覽器控制方向都在快速進化，屬於 AI Harness 競賽的重要戰場。

---

## 連結參考

- [[browser-automation-agent-six-methods]] — 六種瀏覽器自動化方法比較
- [[eva-award-monitor]] — 長榮酬賓機位監控（Akamai 被擋的實際案例）
- [[claude-code-chrome-builtin]] — Claude Code 內建 Chrome 功能
