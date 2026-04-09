---
title: Hermes Agent — 自我學習、自主進化的 AI 代理系統
tags: [Agent, AI, LLM, 知識管理, 工具, 架構設計]
date: 2026-04-09
category: AI工具
source: https://github.com/NousResearch/hermes-agent
---

## 這是什麼

Nous Research 開源的 AI Agent，具備「閉環學習（Closed Learning Loop）」能力。
成功完成任務後會自動抽取邏輯、寫成 Skill，並持續自我進化。

---

## 核心架構：閉環學習

```
對話/任務
  ↓
自動評估哪些資訊有長期價值
  ↓
存入長期記憶 / 生成新 Skill
  ↓
下次遇到同類任務，直接用 Skill
  ↓
發現更優路徑 → 即時更新 Skill（self-improvement）
```

---

## 四層記憶系統

| 層 | 儲存 | 特點 |
|----|------|------|
| 1 | MEMORY.md + USER.md | 最高優先，~3575 字元上限，強制精煉 |
| 2 | SQLite / FTS5 | 全歷史訊息，毫秒搜尋數百萬 Token |
| 3 | Skills（Markdown） | 代理自動生成的工具庫，agentskills.io 標準 |
| 4 | Honcho | 追蹤使用者溝通風格、目標、偏好演進 |

---

## 技術亮點

- **SQLite WAL**：CLI 與 Gateway 同時存取不衝突
- **FTS5 全文檢索**：超快歷史搜尋
- **Cache-aware**：利用 Anthropic Prompt Caching 控成本
- **多平台**：14+ 頻道（Telegram、Discord、Slack…）
- **6 種執行環境**：Local / Docker / SSH / Daytona / Singularity / Modal

---

## 快速安裝

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
hermes setup
hermes
```

---

## 對派哥的啟示

- **OpenClaw + SOUL.md 架構跟 Hermes 同一個思路**：都在做持久記憶 + Skill 進化
- **self-improving-agent skill** 一蘭已安裝，原理跟 Hermes 的 Skill 系統相同
- **四層記憶概念**：可以參考第 4 層 Honcho（使用者建模），一蘭現在只有 MEMORY.md，沒有系統性的用戶偏好追蹤
- Hermes 的「閉環學習」就是一蘭未來應該做到的目標

---

## 連結筆記
- [[mempalace-ai-agent-memory]] — AI 記憶管理多層架構
- [[ai-agent-modular-architecture]] — Agent 模組化設計
- [[agent-skills-standard]] — Skill 標準化（agentskills.io）
