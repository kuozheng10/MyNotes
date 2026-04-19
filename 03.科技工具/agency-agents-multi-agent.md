---
title: Agency Agents — 144+ 專業 AI Agent 人格庫
tags: [AI, Agent, Claude Code, 工具]
date: 2026-04-20
category: AI工具
---

## 這是什麼

[Agency Agents](https://github.com/msitarzewski/agency-agents) 是一個開源的 AI agent 人格庫，收錄 144+ 個有名有姓、有專業背景的 AI 角色。每個 agent 都是 Markdown 文件，包含身份定義、核心使命、工作流程、交付物模板與成功指標——不是泛用 prompt，而是模擬真實職能分工的「AI 員工」。

專案原發於 Reddit，經數月迭代精煉，MIT 授權，支援 Claude Code、GitHub Copilot、Cursor、Aider、Windsurf 等多平台。

## 核心功能

**17 個職能部門，含：**

- Engineering（27+ agent）：Frontend Developer、Backend Architect、AI Engineer、DevOps Automator、Security Engineer
- Marketing（30+ agent）：Growth Hacker、Content Creator、Reddit Builder、TikTok Strategist
- Finance（5 agent）：Accounting、Investment Researcher
- Testing（8 agent）：QA Engineer、Verification Expert
- Sales、Design、Product、Project Management、Support 等

**每個 agent 文件包含：**

- 身份與人格特質
- 核心使命與規則
- 技術交付物（附程式碼範例）
- 標準作業流程（SOP）
- 溝通風格與成功指標

**安裝方式（Claude Code）：**
```bash
./scripts/install.sh --tool claude-code
```

一行指令即可將 agent 批量安裝為 Claude Code skills，也支援 CI/CD 非互動模式。

## 對派哥的啟示

派哥目前的自動化體系（cc_processor、sales-report-analysis、MyNotes）本質上已是多 agent 架構，但 agent 的「人格」和「SOP」都是自己摸索出來的。Agency Agents 提供了一個可直接借用的 agent 人格資料庫：

- **cc_processor**：Finance 部門的 Accounting agent 可作為帳單分析邏輯的參考 prompt 基底，其工作流程模板能直接移植到 BankAdapter 的決策規則中。
- **Sales Report**：Sales 部門的 Account Manager agent 和 Reporting Analyst 可強化月報的撰寫邏輯，讓 generate_report.py 的摘要段落更像人寫的。
- **MyNotes 知識工程**：Marketing 的 Content Creator agent 可作為筆記整理、摘要生成的 prompt persona，讓存入 MyNotes 的筆記風格更一致。
- **Claude Code Skills 整合**：install.sh 支援直接安裝到 Claude Code，派哥可以把需要的 agent 變成 skill，在對話中呼叫不同角色視角處理任務（例如用 QA agent 審查 cc_processor 的邏輯）。

非工程師背景不是障礙——agent 文件是純 Markdown，不需要寫程式，只需要挑選適合的角色、貼入 Claude Code 的 system prompt 或 skill 即可使用。

## 建議行動

1. **先瀏覽 Finance 和 Sales 部門**：直接讀 `finance/` 和 `sales/` 資料夾的 agent 文件，看哪個角色的工作流程最接近派哥現有專案。

2. **試裝一個 agent 到 Claude Code**：執行 `./scripts/install.sh --tool claude-code`，先裝 3-5 個 agent，感受在對話中切換角色的效果。

3. **提取 SOP 模板**：把 Finance accounting agent 的「deliverables」段落借用到 cc_processor 的月報格式，不需要完整整合，只需複製 Markdown 模板。

4. **作為 skill prompt 的參考素材**：下次寫新 skill（如 MyNotes 健檢 SOP）時，先看同類 agent 的人格設定，能省去從零撰寫 persona 的時間。

## 連結筆記

- [[agent-skills-standard]] — 派哥自己的 skill 標準規範
- [[garry-tan-thin-harness-fat-skills]] — thin harness / fat skills 架構觀念
- [[multiagent-specialized-vs-general]] — 專業 agent vs 通用 agent 的取捨討論
- [[claude-code-powerup-guide]] — Claude Code 強化使用指南
