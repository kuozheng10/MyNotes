---
title: Harness 100：100 組 Multi-Agent 配置集（Claude Code 三層架構）
tags: [Claude Code, multi-agent, harness, skills, 自動化, agent架構]
date: 2026-05-05
category: AI工具
source: https://github.com/revfactory/harness-100
author: revfactory
---

## 這是什麼

一個開源 GitHub 專案，收錄 100 組已設計好的 `.claude/` 配置，每組針對特定領域部署「現成可用的多代理人工作團隊」。複製即用，不需從頭設計 Agent 架構。

- 100 個領域配置，涵蓋 10 大類
- 英文 + 韓文雙語版本（共 200 套）
- 978 個 Agent 定義、630 個 Skills、1,808 個 Markdown 設定檔
- 授權：Apache 2.0

---

## 三層 Skill 架構

每個配置都遵循相同的三層設計：

| 層級 | 說明 | 數量 |
|------|------|------|
| **Orchestrator Skill** | 統籌者，協調整個 workflow | 每配置 1 個 |
| **Agent-Extending Skills** | 擴充個別 agent 能力的模組 | 每配置 2-3 個 |
| **External Skills** | 跨配置可複用的通用技能 | 共用 |

每組配置包含 4-5 個專家 Agent + 上述三層 Skill，組成一個完整的領域作業團隊。

---

## 10 大領域對照表

| 編號 | 領域 | 代表性配置 |
|------|------|-----------|
| 01-15 | 內容創作 / 媒體 | YouTube 製作、Podcast、部落格 |
| 16-30 | 軟體開發 / DevOps | Code Review、CI/CD、技術文件 |
| 31-42 | 資料 / ML | 資料分析、ML 模型、報表 |
| 43-55 | 商業 / 行銷 | 市場分析、客服、銷售 |
| 56-65 | 教育 | 課程設計、教材、學習評估 |
| 66-72 | 法律 | 合約審查、法規遵循 |
| 73-80 | 健康 / 醫療 | 臨床文件、研究摘要 |
| 81-88 | 技術文件 | API 文件、使用手冊 |
| 89-95 | 業務運營 | 流程優化、HR、財務 |
| 96-100 | 特殊領域 | 安全、研究、其他 |

---

## 安裝方式

```bash
# 複製特定配置的 .claude/ 資料夾到目標專案
cp -r en/01-youtube-production/.claude/ /path/to/your/project/.claude/

# 或整組複製來研究架構
git clone https://github.com/revfactory/harness-100
```

每個 `.claude/` 資料夾內含：
- `CLAUDE.md` — 主配置
- `agents/` — Agent 定義檔
- `skills/` — Skill 實作檔

---

## 對派哥的評估

**使用定位：參考庫，不是替換現有架構**

| 面向 | 評估 |
|------|------|
| 軟體開發 #16-30 | ✅ 值得研究，可能有 Code Review / DevOps 配置能直接抄 |
| 商業 / 運營 #43-55 | 🟡 個別 skill 設計可借用（如報表、行銷文案流程） |
| 其餘領域 | ❌ 派哥現有工具更針對性，不需要替換 |
| 全套導入 | ❌ 目前系統已有 garry-tan 瘦 harness 原則，引入 100 組會混亂 |

**最佳用法**：遇到新 workflow 需求時，先到對應編號查「有沒有人設計過」，再選擇性抄取 agent 定義或 skill 結構，而非整套導入。

---

## 與現有知識的對比

- **[[garry-tan-thin-harness-fat-skills]]**：Harness 100 走的是「預設 fat harness」路線，與 Garry Tan 的瘦 harness 原則相反，更適合標準化場景而非高度客製化的個人工作流
- **[[harness-engineering]]**：Harness 工程核心仍是 Feedforward + Feedback 原則，Harness 100 是更大規模的 Feedforward 配置集
- **[[agent-skills-standard]]**：Harness 100 的三層架構與現有 skill 標準一致，可當設計時的範本庫

---

## 連結參考

- [[garry-tan-thin-harness-fat-skills]] — 瘦 harness 哲學（設計方向對比）
- [[harness-engineering]] — Harness 工程原則
- [[agent-skills-standard]] — Skill 設計標準
- [[claude-code-powerup-guide]] — Claude Code 實戰技巧
