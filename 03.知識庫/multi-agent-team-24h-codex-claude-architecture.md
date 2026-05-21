---
title: 連續 24 小時工作的 Multi-Agent 開發團隊架構：TL(Codex) + PM(Claude) + 3 Workers(Codex)
tags: [Multi-Agent, Codex, Claude, 自動化, 開發架構, Agent團隊]
date: 2026-04-29
category: AI Agent 架構
---

## 架構概覽

```
Team Lead (Codex)        ← 最信任的決策者，遵守流程、檢視交付品質
    └── PM (Claude)      ← Loop 調度器，省 token，傳聲筒
         ├── Worker 1 (Codex)
         ├── Worker 2 (Codex)
         └── Worker 3 (Codex)
```

實績：連續三週 24 小時不間斷工作。

---

## 為何 Claude 當 PM（不當 TL）

**Claude 的定位：極度初階工程師 + Loop 調度器**

- 大型複雜專案（超過 10 個文件互動）容易鬼打牆，bug 會 rotate 出現
- **Loop 功能**：像 CPU 的 clock，每輪確認任務完成，向 TL 拿新任務
- **超省 token**：loop 優化過（可能因 cache），貴但笨，適合當傳聲筒

**Claude 不適合當 TL 的原因**：
- 無法遵照定義的流程給 Worker 指令
- 遇到問題會跟著 Worker 走，容易被工程師唬爛

---

## 為何需要三個 Worker

- 很多任務可以平行執行
- 測試需要 Computer Vision 逐步檢視畫面，耗時
- TL 自動分配任務給三個 Worker，parallel 大幅提升效率

---

## 為何 Codex 當 TL

Codex 在大型專案的流程遵循度更高，設定了三道驗證 gate：

| Gate | 說明 |
|------|------|
| Forward Path Verification | 重新 trace code 邏輯是否正確 |
| Human Path Verification | 透過介面操作一次，確認結果符合預期 |
| Requirement Alignment Verification | 用 `claude -p` + `codex exec` 呼叫外部專家，確認實作符合需求文件與專案標準 |

---

## 演進歷程

| 階段 | 架構 | 最長工作時間 | 問題 |
|------|------|-------------|------|
| 1 | 人工控制 3 個 Codex session | <30 分鐘 | 要自己追進度、安排任務、處理 blocker |
| 2 | 每個 Worker 配一個 PM（Claude） | >2 小時 | 3 個 PM 要獨立追進度，PM 多在做空 loop |
| 3 | 合併為一個 PM，加入 loop 功能 | 更長 | Claude PM 無法遵守流程，被 Worker 帶著走 |
| 4 | 新增 TL（Codex） | **24 小時連續** | 架構穩定，三週不間斷 |

---

## 待優化方向

- 怎麼開第二隻團隊，讓環境依舊乾淨
- 讓每個角色有自己的 agent file，不共用專案 agent file
- 更漂亮的介面讓 agent 之間傳訊息，人類可監視互動（openab 可評估：github.com/openabdev/openab）

---

## 對派哥的意義

- 目前 cc_processor / daily briefing 是單一 Claude session，複雜任務可借鑑此架構
- TL(Codex) + PM(Claude Loop) 的分工值得在大型改版時試用
- 三道 gate 驗證（forward/human/requirement）可納入 feature-workflow.md
- Claude loop 功能搭配 tmux 是低成本的任務調度方式

---

## 連結筆記

- [[boris-parallel-claude-workflow]] — parallel Claude session 工作流程
- [[dual-agent-dev-loop]] — 雙 agent 開發 loop
- [[multi-agent-system-architecture-optimization]] — multi-agent 架構優化
- [[claude-subagent-context-management]] — subagent context 管理
- [[codex-plugin-cc]] — Codex CLI 整合 Claude Code
