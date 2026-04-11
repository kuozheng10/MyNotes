---
title: GBrain — Garry Tan 開源的生產級 AI Agent 記憶系統（含隱私警告）
tags: [gbrain, 知識管理, ai-agent, 記憶, 第二大腦, 隱私, 必學]
date: 2026-04-11
category: AI工具
source: https://github.com/garrytan/gbrain
---

## 這是什麼

YC 總裁 Garry Tan 把他本人真實跑很久的 AI 記憶系統整包開源（MIT）。
不是 demo，是真實配置：10,000+ Markdown、3,000+ 人物檔、13 年 Google 日曆、5,800 條 Apple Notes。

---

## ⚠️ 隱私警告（重要）

> **社群方案（Community Plan）會把你特定的商業邏輯決策回傳到 Garry Tan 的 server。**

- 文件裡有寫，自己讀過確認
- 有公司機密或私人商業邏輯 → **必須關掉社群方案** 或改用完全自架
- 安全選擇：全部 Docker 本地跑，資料不出內網

---

## 架構

```
Markdown 筆記（本地）
    ↓
混合搜尋（grep + Postgres + pgvector 語義搜尋）
    ↓
Dream Cycle（自動從互動記錄提取實體、鞏固記憶）
    ↓
MCP Server（任何相容 Agent 可呼叫）
```

**頁面模型**：
- `compiled truth`：當前最佳論述
- `timeline`：只增不刪的證據鏈

---

## 安裝需求

- Postgres + pgvector
- 小規模：Supabase 免費層
- 萬級文件：Supabase Pro（~$25/月）或自架 Docker

---

## 對派哥的評估

**現在不需要，維持 MyNotes + Karpathy 路線。**

| 條件 | 派哥現狀 |
|------|----------|
| 文件量 | ~70 個筆記，規模小 |
| 需要 Postgres | 多一層基礎設施維護 |
| 隱私顧慮 | 有機密資料要自架，成本增加 |
| 人物/交易追蹤 | 目前無此需求 |

**什麼時候值得考慮：**
- MyNotes 超過 500 個筆記，搜尋跟不上
- 開始做投資或需要追蹤大量人物/公司
- 有能力維護 Postgres 自架環境

---

## 連結筆記
- [[three-masters-ai-notes-karpathy-tobi-garry]] — 三位大師 AI 筆記系統比較
- [[mempalace-ai-agent-memory]] — AI Agent 記憶管理
- [[llm-knowledge-base-karpathy]] — Karpathy LLM 知識庫
