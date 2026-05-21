---
title: "Claude Code 原始碼洩露：6 個改變使用方式的發現"
tags: [claude-code, harness, CLAUDE.md, context, agent, 效率, 原始碼]
date: 2026-04-02
category: 03.科技工具
source: Facebook 派哥分享
---

## 背景

2026/03/31 Anthropic 更新 Claude Code npm 套件時，不小心把 source map 留在發布包裡，任何人可還原完整 TypeScript 原始碼（51 萬行、1,902 個檔案）。這是第二次犯相同錯誤（第一次在 2025 年首次發布時）。

---

## 六大發現

### 1. 真正呼叫 LLM API 的部分不到 5%

剩下 95% 是 **harness**：安全檢查、權限控制、上下文管理、記憶系統、工具編排。

> 模型是引擎，harness 是整台車。同樣呼叫 Claude API，不同產品體驗天差地別，差的是 harness 設計。

### 2. CLAUDE.md 每一輪對話都會重新載入

大部分人以為只讀一次，**錯**。原始碼顯示每次送出訊息都會重新讀取。

- 額度：**40,000 字元**，大多數人只用了不到 200 字
- 等於「每次對話都被讀取的操作手冊」

**CLAUDE.md 層級結構：**

| 檔案 | 用途 |
|------|------|
| `~/.claude/CLAUDE.md` | 全域設定（coding style、偏好） |
| `./CLAUDE.md` | 專案層級（架構決策、慣例） |
| `.claude/rules/*.md` | 模組化規則 |
| `CLAUDE.local.md` | 私人筆記（不進 git） |

### 3. 五個內建 Agent 各司其職

| Agent | 特性 |
|-------|------|
| Explore Agent | 純唯讀，連建檔案的權限都沒有 |
| Plan Agent | 負責規劃但不執行 |
| Verification Agent | 目標是「想辦法搞壞它」，不是確認看起來沒問題 |

> 做事的人跟驗收的人分開，和管理團隊的邏輯一模一樣。

### 4. 子 Agent 共享快取 — 開 5 個只花 1 個的錢

Fork 子 Agent 時，建立 byte-identical 的上下文副本，API 會 cache 這份副本。
**開 5 個並行 Agent，成本幾乎等於 1 個。**

> 用它跑單線程，等於買了法拉利只開一檔。

### 5. 對話超過 167K tokens 自動壓縮

系統保留：5 個檔案（各上限 5K tokens）+ 50K tokens 摘要，其餘全部丟掉。

- 你之前的推理鏈、中間決策、讀過的檔案內容全部消失
- AI 不知道自己忘了什麼，會用**幻覺補上**
- **高手做法**：主動用 `/compact` 手動「存檔」，保留重要的，清掉不需要的

### 6. 從原始碼學到的 CLAUDE.md 高價值規則

Anthropic 內部版比外部版多了幾條關鍵規則，可以自己寫進 CLAUDE.md：

#### (a) 強制驗證，不准說「Done」就跑
每次修改檔案後，必須跑 type check 和 lint，全部通過才能回報完成。
（AI 判斷寫入成功只看 bytes 有沒有寫進磁碟，不看能否編譯）

#### (b) 大檔案必須分段讀取
每次讀檔有 **2,000 行 / 25,000 tokens 的硬上限**，超過會被截斷且 AI 不會告訴你。
超過 500 行的檔案，強制用 `offset + limit` 分段讀。

#### (c) 超過 10 輪對話，編輯前必須重讀檔案
上下文壓縮後，之前讀過的內容可能已被丟棄。編輯前一律重新讀取，不准信任記憶。

#### (d) 搜尋結果永遠要懷疑
工具結果超過 **50,000 字元**會被截斷成 2,000 byte 預覽。結果看起來太少，就縮小範圍重搜。

#### (e) 重構前先清垃圾
dead code、unused import、orphaned props 每一行都在吃 token，加速觸發上下文壓縮。
大型重構前，先開一個 commit 專門清理。

#### (f) 複雜任務拆成子 Agent 並行
一個 Agent 約 167K tokens 工作記憶。超過 5 個獨立檔案的任務，拆成子 Agent 分頭進行。

---

## 對日常使用的啟示

1. **CLAUDE.md 是最高 ROI 的投資**，每次對話都讀，花 30 分鐘寫好
2. **主動用 `/compact`** 而非等系統自動壓縮
3. **複雜任務用 subagent**，不要讓一個 Agent 硬撐
4. **不信任 AI 的完成回報**，要求強制驗證

---

## 相關

- [[boris-15-claude-code-tips]]
- [[claude-hidden-combo]]
- [[claude-code-feature-workflow]]
- [[agent-prompt-token-cost]]
