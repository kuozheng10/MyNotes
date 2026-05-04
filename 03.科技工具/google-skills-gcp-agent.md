---
title: Google 官方 Agent Skills 合集 — 讓 AI 精通 Google Cloud
tags: [agent, skills, Google, GCP, Gemini, Firebase, Claude Code, RAG]
date: 2026-05-04
category: AI工具
source: https://github.com/google/skills
---

## 這是什麼

Google 官方開源的 Agent Skills 合集，把 Google Cloud 的最佳實踐封裝成 AI 可讀取的結構化指令庫。
核心概念跟 Claude Code skills 相同：讓 Agent 在執行特定任務時自動獲得對應領域的「專家直覺」。

---

## 包含的 Skills（共 13 項）

| 類別 | Skills |
|------|--------|
| AI | Gemini API 核心實踐 |
| 計算 | Cloud Run、GKE (Kubernetes) 基礎 |
| 資料庫 | BigQuery、AlloyDB、Cloud SQL |
| 前後端 | Firebase（認證+資料庫） |
| 基礎設施 | GCP 上手指南、身份驗證、網路配置 |
| 架構優化 | Well-Architected Framework（安全/可靠性/成本） |

---

## 安裝與使用

```bash
# 一鍵安裝全部（互動式選擇）
npx skills add google/skills
```

安裝後 Agent（如 Claude Code）執行 GCP 相關任務時會自動載入對應 skill。

---

## 對比：這跟 addyosmani/skills 有何不同？

| | addyosmani/skills | google/skills |
|--|--|--|
| 覆蓋範圍 | 前端、效能優化 | Google Cloud 全系列 |
| 官方支援 | 非官方 | Google 官方 |
| 適用對象 | Web 前端開發者 | GCP/Gemini 開發者 |

---

## 評估：對派哥有沒有用？

**部分有用，選擇性安裝即可**

| Skill | 對派哥的用途 | 建議 |
|-------|------------|------|
| Gemini API | Gemini CLI 調用優化 | ✅ 值得裝 |
| Firebase | 若 My Wallet Trip 換後端 | 🟡 備用 |
| BigQuery | 目前無需求 | ❌ 跳過 |
| Cloud Run / GKE | 派哥用 Vercel，不用 GCP | ❌ 跳過 |
| Well-Architected | 架構評估時可參考 | 🟡 備用 |

快速驗證（只裝 Gemini）：

```bash
npx skills add google/skills
# 互動選擇：只勾 gemini-api
```

**不需要包成 skill**，直接用 `npx skills add` 按需載入即可。

---

## 連結參考

- [[addyosmani-agent-skills]] — 同類型的前端 skills
- [[agent-skills-standard]] — skills 生態系統概念
- [[ai-build-skills-nick-baumann]] — 自建 skills 的方法論
