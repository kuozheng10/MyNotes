---
title: Claude Code 內部執行五層架構：從輸入到產出的核心邏輯
tags: [Claude Code, 架構設計, Agent, 執行機制, context管理, 工具調用]
date: 2026-05-06
category: AI工具
source: https://gigaai.studio/learning/claude-code-five-layers.html
---

## 這是什麼

解釋 Claude Code 強大的原因不只是模型本身，而是一套「五層內部執行架構」——從用戶下指令，到代碼被正確執行，每一層各司其職。

注意：這和 [[claude-agent-five-layer-architecture]] 是不同的五層——那個是「開發者怎麼設定 Claude Code」，這個是「Claude Code 內部怎麼運作」。

---

## 五層架構總覽

| 層 | 名稱 | 核心職責 |
|----|------|---------|
| 1 | 用戶交互層 | 終端機 UI、輸入接收、中斷處理 |
| 2 | 上下文管理層 | 決定「看哪些檔案」、精簡 token |
| 3 | 工具調用與代理層 | 自主決策、拆解步驟、循環執行 |
| 4 | 執行與安全層 | 實際寫入檔案系統、權限確認 |
| 5 | 反饋與修復層 | 跑測試、抓錯誤、自動 debug |

---

## 各層細節

### 層 1：用戶交互層（終端機即畫布）

- 用 `react-ink` 構建，終端機可顯示進度條、狀態更新、格式化文字
- 支援單次指令（one-off）或互動式 session
- `Ctrl+C` 中斷機制，系統妥善處理中斷狀態

### 層 2：上下文管理層（決定「該看什麼」）

- 不是把整個資料夾塞進 context，而是根據任務篩選相關路徑
- 用 file tree + `.gitignore` 過濾無關檔案
- 長檔案做摘要或只讀片段，節省 token
- 隨對話演進動態調整，確保模型掌握最關鍵資訊

### 層 3：工具調用與代理層（核心大腦）

- Agent 屬性：根據目標自主拆解步驟，決定何時搜尋、讀取、編輯
- 工具箱：`grep`、`ls`、`cat`、`sed` 等命令的封裝版本
- 循環反饋：工具執行結果回傳模型 → 判斷完成或需修正 → 進入下一循環

### 層 4：執行與安全層（守門員）

- 寫入操作或高風險命令（如 `rm`）需顯式確認（除非開 `-y` 模式）
- 盡可能本地執行，避免敏感代碼上傳外部
- 應用更改前檢查語法或路徑有效性

### 層 5：反饋與修復層（自我進化）

- 自動執行測試命令（`npm test`、`pytest` 等）
- 測試失敗 → 錯誤 log 當新輸入 → 觸發自動 debug
- 理解 Git 狀態，生成 commit message，確保符合既有規範

---

## 為什麼這解釋了 Claude Code 的強大之處

1. 幻覺降低：層 2（精準 context）+ 層 5（測試驗證）大幅減少輸出錯誤
2. 自主性：層 3 的 agent 循環讓它不只是「補全代碼」，而是「理解→探索→解決→驗證」
3. 安全可控：層 4 的確認機制讓高風險操作不會靜默執行

類比：Claude Code 是住在終端機裡的資深工程師，不是只會按指令打字的助手。

---

## 對派哥的啟示

- 層 2 的「智慧 context 過濾」解釋了為何 `.claude/` 設定得好，執行品質差異很大
- 層 5 的「自動測試循環」說明在 CLAUDE.md 寫清楚「跑完要 type check + lint」的意義：它會真的跑，失敗會自動修
- 層 3 的循環反饋解釋了為何複雜任務要拆小步驟——每次循環的 token 累積會影響判斷品質

---

## 連結參考

- [[claude-agent-five-layer-architecture]] — 外部設定五層（CLAUDE.md/Skills/Hooks/子代理/外掛），與本篇互補
- [[claude-code-powerup-guide]] — 實戰技巧
- [[claude-subagent-context-management]] — 子代理 context 控管
- [[claude-code-token-saving-strategies]] — token 節省策略（對應層 2）
