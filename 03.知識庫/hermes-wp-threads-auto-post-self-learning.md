# Hermes + WP + Threads 自動發文 — AI 自學卡關實戰三心法

tags: #Hermes #Threads #WordPress #AI自學 #Agent #卡關排查

> 學員案例：WP工程師三小時完成全套自動化，下午自學再接 WP 爬文→改寫→TG審核→自動發文

---

## 成果摘要

**學員成就（三小時課 + 一個下午自學）：**

1. 安裝插件版 Claude、Codex
2. 申請 Threads API
3. 以兩個 Agent 設置自動發文環境
4. 撰寫 Skills
5. 設置發文排程
6. 發文前傳 LINE 人工審核
7. 安裝 Hermes 在雲端主機（Ubuntu + nginx）
8. 訓練 Hermes 學習整套流程

**自學延伸：** Hermes 爬 WP 自有 SEO 文章 → 改寫成 Threads 格式 → 每日自動發文 → TG 審核

---

## 心法一：不要只會複製貼上 AI 的答案

**卡關場景：** Hermes 安裝失敗（nginx 環境、套件缺失、權限不足）

**錯誤做法：**
- 丟 log 給 Codex → 照指令執行 → 還是失敗 → 再丟 log → 鬼打牆 2～3 輪

**正確做法：**
- 直接找 Hermes 的 GitHub repo
- 請 Codex 讀 README → 一次安裝成功

**核心原則：**
> 當 AI 鬼打牆，不要只照 AI 的答案做，要自己提供更精準的上下文

---

## 心法二：換個角度主動發問，而不是複製答案

**卡關根因：** 給 AI 的資訊不夠清楚（環境、作業系統、使用情境）

**反例：** Windows 本地安裝 → 沒告知要開 WSL → AI 不會主動說要換 Linux 環境 → 一直在錯誤方向打轉

**正確問法：**
- ❌「執行這個指令還是失敗」（貼 log 無腦照做）
- ✅「是不是因為我的作業系統問題，而不是安裝指令的問題？」
- ✅「能不能從不同角度列出為什麼安裝失敗的可能原因？」

**效果：** 換個問法，比一直貼 log 省掉很多時間

---

## 心法三：多嘗試不同工具、不同做法

**關鍵升級：** 從 Chat 模式 → Agent 模式

| 模式 | 特點 |
|------|------|
| Chat 模式 | AI 給答案，人工操作，效率低 |
| Agent 模式 | AI 長出手腳，直接跟 API / 主機 / WP / LINE / TG 互動 |

**AI 不能直接執行的五種可能原因：**
1. Chat 沒有切換成 Agent
2. 困在沙盒裡，碰不到外面
3. 少安裝套件 / Skills
4. 給錯上下文，或上下文不足
5. 權限、環境變數設定問題

> 有時候卡很久的問題，換個做法一次就解決了

---

## 技術架構（本案例）

```
WP 後台（SEO 文章）
    ↓ Hermes 爬取
    ↓ 改寫成 Threads 格式
    ↓ 排程自動發文
    ↓ 發文前傳 TG/LINE 審核
Threads 自動發佈
```

**環境：** Ubuntu + nginx 雲端主機（Linux 環境相容性較佳）

---

## 相關筆記

- [[ai-agent-hermes-openab-openclaw-comparison]] — Hermes vs OpenClaw 比較
- [[hermes-agent-self-learning]] — Hermes 自學機制
- [[agentcrew-beeper-mcp-messenger-ig]] — Agent + 社群媒體自動化
- [[claude-code-ai-dev-team-design]] — Agent 設計架構
