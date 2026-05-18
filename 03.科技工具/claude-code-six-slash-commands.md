---
title: "Claude Code 最常用指令（含使用場景）"
tags: [claude-code, slash-commands, /compact, /plan, /simplify, /statusline, /goal, workflow, 新手, productivity]
date: 2026-05-18
category: 03.科技工具
source: Telegram 派哥分享
---

## 核心洞見

Claude Code 裡有幾個指令，用對時機能大幅節省 token 和混亂感。

## 六個指令

**1. /context — 檢查上下文**

查目前對話裡 Claude 知道什麼。對話久了、丟了很多檔案或錯誤訊息後，用它確認 Claude 目前的記憶狀態。

**2. /compact — 壓縮對話**

長對話壓縮成重點摘要，告訴 Claude 哪些東西要保留。
適合：長專案、長修 bug、長重構完一個階段後。

**3. /simplify — 程式碼三向優化**（gstack skill）

啟動三個平行 AI，分別檢查重用性、品質、效率，自動整理優化。
功能寫完後做最後一輪清理用。
> 注意：這是 gstack skill，不是 Claude Code 內建，需要先裝 gstack。

**4. /plan — 新功能前先規劃**

開新功能或複雜任務前強制先規劃架構、拆解步驟、確認方向，避免 Claude 未討論清楚就直接改檔案。

**5. /statusline — 自訂狀態列**

設定狀態列顯示哪些資訊。
推薦放：上下文長度、專案名稱、目前使用模型、5 小時用量、7 天用量。

**6. # 符號 — 背景資訊注入**

`#` 開頭的內容不是立即指令，而是讓 Claude 讀進去記住的背景規則，存入 CLAUDE.md。
適合放：專案規範、命名規則、不能動的檔案、團隊約定。

**7. /goal — 長任務自動循環到完成**（Claude Code + Codex 均支援）

給定一個可驗證的完成條件，Claude 自動一輪接一輪執行直到目標達成：

```
/goal auth 測試全部通過，並且 lint 乾淨
```

Claude 會：執行 → 檢查目標是否達成 → 未完成繼續 → 達成才停。

適合：修測試、重構、清理 backlog、跑 CI 直到 pass。
關鍵：**目標必須可驗證**（測試通過、lint 0 error），不能是模糊的「做好這個功能」。

→ 這就是 [[codex-agent-os-workflow-jason]] 的 Goal 要素實作版本

## 使用節奏建議

| 時機 | 指令 |
|------|------|
| 開新功能前 | /plan |
| 功能寫完後 | /simplify |
| 對話太長/混亂 | /compact |
| 懷疑 Claude 記錯 | /context |
| 第一次設定 | /statusline |
| 交代背景規則 | # |
| 長任務跑到完成（測試/lint/重構）| /goal |

## 相關筆記

- [[gstack-claude-skills]] — /simplify、/review、/ship 完整說明
- [[cc-statusline-plugin]] — statusline 詳細設定
- [[claude-code-token-saving-strategies]] — token 節省策略
- [[claude-code-newbie-guide]] — 新手完整入門
