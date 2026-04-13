---
title: AI 全自動發 Facebook — CDP + Claude CLI 流程
tags: [自動化, CDP, Facebook, 社群自動化, Claude-Code, Chrome]
date: 2026-04-13
category: AI工具
source: 社群文章（作者不明，轉自 goodarticle）
---

## 五步驟全自動流程

```
① GitHub API → 找今天最熱門 repo（自動選題）
② CDP 操控 Chrome → 去 X 搜尋 5 篇相關討論（帶登入 session，無需 API key）
③ Claude CLI → 整合 repo + 推文 → 寫輕鬆中文貼文
④ Nano Banana 2 → 自動生成配圖（隨機風格）
⑤ CDP 回 Facebook → 上傳圖片 + 發文
```

---

## 關鍵技術巧思

### 1. Chrome 登入狀態複製

新開 Chrome 實例 = 需要重新登入。解法：

> 把主 Chrome profile 的 cookie 複製到新實例，帶著原本的登入狀態啟動

學會這招，X 和 FB 都不需要重新登入，整個自動化的門就開了。

### 2. Claude CLI 巢狀環境問題

在 Claude Code 環境內呼叫 `claude` CLI 會卡住。解法：

```bash
unset CLAUDECODE
claude ...
```

讓它不把自己當成被另一個 Claude 呼叫的 subprocess。

### 3. 隨機發文間隔

不用固定間隔，改用亂數 10 分鐘到 3 小時：
- 避免平台偵測（機器感）
- 模擬真人行為

---

## Pre-flight check 設計

每次啟動前先確認：Python 套件、Chrome CDP 連線、FB/X 登入狀態、Nano Banana API、claude 指令可用。任何一項不對就提早報錯。

---

## 對派哥的應用價值

- Chrome CDP cookie 複製技巧：凡是需要帶登入 session 操作 web 的自動化，都適用
- `unset CLAUDECODE` 技巧：cc_processor 或其他從 Claude Code 呼叫 claude CLI 時可能用到
- 整個 pipeline 模式：GitHub trending → 生成內容 → 自動發文，如果派哥有社群自動化需求可參考
