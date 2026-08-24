---
title: Claude Code 狀態列儀表板插件：即時追蹤費用與配額
tags: ["Claude Code", "工具", "工作流程", "自動化"]
date: 2026-04-21
category: 開發工具
source: goodarticle/2026-04-21_CC_狀態列插件.md
---

## 這是什麼
由 SammyLin 開發的 Claude Code 狀態列插件，能將費用、Token 配額、任務進度等關鍵資訊直接顯示在終端機 Prompt 旁，解決頻繁詢問狀態的痛點。

## 核心概念
- **即時監控儀表板**：整合費用追蹤（Compaction 記錄）、Rate Limit 倒數（5h/7d）以及 Context Compaction 進度。
- **任務透明化**：可追蹤 Subagent 狀態、MCP Server 健康狀況以及目前已編輯的檔案清單。
- **外掛式架構**：採用 Plugin 模式實作而非 Fork 原始碼，確保 Claude Code 版本更新時不會導致功能失效。
- **Hooks 系統探索**：克服官方文件不足的困難，透過 Log 與嘗試錯誤找出 Subagent Start/Stop 等 Hooks 的正確運作機制。

## 使用方法 / 快速啟動
1. 訪問專案倉庫：`https://github.com/SammyLin/cc-statusline`
2. 依照專案說明將其整合至 Claude Code 環境，即可在開發時即時掌握資源消耗。

## 對派哥的啟示
這對於開發自動化 AI 工具非常有參考價值。在派哥處理如「業務業績統計」或「銷售報告分析」等長時間運行的 Agent 任務時，可以參考此專案的 Hooks 實作方式，為自己的自動化流程加入可視化的儀表板或狀態監控，精確掌控 Token 成本與 API 配額，提升工具的穩定性與使用者體驗。

---

## 補充：不裝插件、直接請 Claude Code 幫你寫一支 statusLine 腳本

> 來源：卡斯伯（Facebook），https://www.facebook.com/share/1FeVEW5tqL/?mibextid=wwXIfr，2026-08-24

比起上面的完整插件，這是更輕量的DIY做法：`~/.claude/settings.json` 的 `statusLine` 欄位可以指向一支腳本，Claude Code 每次刷新會把一包 JSON 從 stdin 餵給它，腳本印到 stdout 的內容就是狀態列（可多行、可用 ANSI 顏色）。

**作者實際顯示的 7 項資訊：**

1. **資料夾名稱** — 同時開多個 Claude Code 視窗時，快速確認目前是哪個專案，避免做到一半跑錯地方
2. **Git 分支名稱** — 隨時確認現在在哪個 branch，不容易跟預期不一致
3. **目前使用的模型** — 切換模型後忘記換回來，容易跑出不如預期的結果或浪費額度，顯示出來就不會忘
4. **目前的思考等級（Effort）** — 簡單任務不用開太高、複雜任務拉高，跟模型一樣容易忘記切回來
5. **Context 剩餘量** — 快用完時該不該先 `/compact`，看這個百分比決定，呼應派哥自己「60%就壓縮」的額度管理習慣
6. **5 小時額度剩餘量** — 額度快用完可以先停下來、排程等 reset 後再跑，處理大型工作時比較好抓節奏
7. **Session 名稱** — 現在 Claude Code 可跨 Session 延續工作，同時開多個 Session 時方便分辨是在跟哪個 Session 對話

**可直接丟給 Claude Code 的提示詞（照抄可用）：**

```
幫我做 Claude Code 的 status line。
設定在 `~/.claude/settings.json` 的 `statusLine`，指向一支腳本：
Claude Code 每次刷新會執行它、把一包 JSON 從 stdin 餵進來，腳本印到 stdout 的就是狀態列（可多行、可用 ANSI 顏色）。

我要顯示內容如下：
第一行　資料夾名稱｜git 分支｜模型｜effort 等級
第二行　context 剩餘 %｜5 小時額度剩餘 %｜session 名稱（整行 dim 灰）
```

**跟上面 cc-statusline 插件的差異**：插件是別人維護好的完整套件（費用追蹤、Subagent狀態、MCP健康度都有），這個是「自己講需求、讓 Claude Code 現場幫你刻一支」——客製化程度更高，但要自己維護。派哥如果只是想要「一眼看到context/額度剩餘量」，這個DIY提示詞比裝整個插件更輕量。

## 連結筆記
## 連結筆記
- [[boris-15-claude-code-tips]]
- [[claude-code-feature-workflow]]
- [[claude-code-powerup-guide]]
- [[claude-code-subagent-environment]]
- [[claude-routines-automation]]
