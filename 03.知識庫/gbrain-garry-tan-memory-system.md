---
title: GBrain — Garry Tan 開源的生產級 AI Agent 記憶系統（含隱私警告）
tags: [gbrain, 知識管理, ai-agent, 記憶, 第二大腦, 隱私, 必學]
date: 2026-04-11
updated: 2026-05-20
category: AI工具
source: https://github.com/garrytan/gbrain
---

## 這是什麼

YC 總裁 Garry Tan 把他本人真實跑很久的 AI 記憶系統整包開源（MIT）。
生產環境（v0.36）：**17,888 頁、4,383 人物、723 公司、21 個 cron job**，12 天建成。

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

## v0.36 新功能

- **ZeroEntropy** 預設 embedding（2.2x 快、2.6x 便宜 vs OpenAI）
- **PGLite**（Postgres 17 via WASM）：零設定，不需 server，個人用到 5 萬頁
- **43 個 skill**：signal 捕捉、ingest、enrichment、cron、dream cycle、eval
- `gbrain doctor --remediate --yes`：自動修復腦健康到 90 分
- **OpenClaw / Hermes 原生整合**：`gbrain skillpack scaffold --all` 一行搞定

---

## 對派哥的評估（2026-05）

**值得試了。** 主要因為：
1. PGLite 不用裝 Postgres，30 分鐘裝完
2. 投資追蹤（公司/人物關係）剛好是 gbrain 最強的
3. OpenClaw（一蘭）原生支援，一蘭直接獲得 43 個記憶 skill

| 條件 | 現狀 | GBrain 加什麼 |
|------|------|--------------|
| MyNotes 200+ 筆記 | Obsidian 管 | 可 ingest 成可查詢知識圖譜 |
| OpenClaw（一蘭）| 跑中 | 自動獲得 43 個記憶/知識 skill |
| 投資追蹤 | SQLite 手動 | 公司/人物自動 enrichment |
| 隱私 | 有商業資料 | 用 PGLite 本地跑就沒問題 |

**安裝順序建議：**
1. `bun install -g github:garrytan/gbrain`
2. `gbrain init --pglite`
3. `gbrain doctor`（驗證健康）
4. 試一個 skill，看看感覺
5. 確認穩了再接 OpenClaw

---

## 連結筆記
- [[three-masters-ai-notes-karpathy-tobi-garry]] — 三位大師 AI 筆記系統比較
- [[mempalace-ai-agent-memory]] — AI Agent 記憶管理
- [[llm-knowledge-base-karpathy]] — Karpathy LLM 知識庫
