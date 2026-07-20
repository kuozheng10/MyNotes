---
title: 有了 AI Agent 後反而更愛寫文件——文件與程式碼同步演進的迭代模式
tags: ["AI", "spec-driven-development", "工作流程", "文件管理", "敏捷"]
date: 2026-07-20
category: 系統架構
source: Facebook 貼文（作者直接貼全文，無公開連結）
related: [[efficient-sdd-delta-spec]], [[cline-memory-bank-structured-ai-memory]], [[claude-project-management-best-practices]]
---

## 這是什麼

作者分享自己從「不重視文件」到「AI輔助開發後反而愛寫文件」的心態轉變，並提出一套具體的 docs 目錄結構，把 AI Agent 而不是人，當成文件的主要讀者。

## 核心概念

**沒有 AI 的年代（Waterfall 的陷阱）**
- 傳統開發常見迷思：要先寫完詳細需求文件才能寫碼，但文件寫得越詳細反而越模糊——因為文件完成到實際寫碼常有數週甚至數月落差，內容早就失真
- Agile 的 I&I（Iteration & Increment）就是為了解決這個問題：快速走 SA→SD→Coding 循環，盡早拿回饋再修正
- 那個年代文件的角色是「草稿」而非「精確規格」：UML 圖（使用案例圖/類別圖/循序圖/不限格式架構圖）只是溝通思維的工具，手繪都行

**有了 AI Agent 後（角色反轉）**
- 現在寫文件的**主要讀者是 AI Agent**，人（開發者/使用者）只是審閱、參考、掌握重點
- 用 Markdown 作為文件格式：AI 和人都好讀好編輯，是最方便的交換格式
- 開發者不再照文件自己寫碼，而是 AI Agent 讀文件生成程式碼（含測試、部署腳本）
- 因為文件現在有 AI 幫忙整理和維護，可以寫得比以前細很多——甚至細到 Function Point、業務邏輯、欄位明細

**具體文件目錄結構**

```
.\docs
├─ research/         # 技術調研與參考資料
├─ requirements/      # 需求、範圍與驗收條件（用 PRD Skill 生成）
├─ architecture/      # 系統架構與設計決策（技術框架、分層結構規範）
└─ prj-tracking/      # 專案進度與執行紀錄
   ├─ work-note/      # 工作筆記與討論紀錄
   ├─ backlog/        # 待辦需求與改善項目（每次迭代前先整理進去）
   └─ devlog/         # 開發進度與變更紀錄（完成後把實際內容寫進去）
```

- 每次迭代前：先把預定工作項目整理到 `backlog/`
- 完成後：把實際完成內容整理成紀錄寫進 `devlog/`
- 最後：commit + push 到 GitHub 做版本管理

**關鍵心法：不是回到 Waterfall**

先建好完整目錄、寫完所有文件才開始寫碼，仍然是 Waterfall 思維。作者強調文件與寫碼之間**沒有絕對先後順序**，但最終要讓兩者保持一致。過去文件跟程式碼常因為不同人在不同時間維護而不同步，但 AI Agent 恰好有能力讓兩者同步演進。

**最終的迭代循環**：
```
撰寫最小規格／文件 ⇄ AI Agent 實作 ⇄ 根據實作結果驗證、修訂並補充規格文件
```

## 對派哥的啟示

- 這篇的核心心法（文件主要讀者是 AI Agent、Markdown 交換格式、docs與code同步迭代不追求一次寫完）跟你 CLAUDE.md 裡「非小修前先確認有沒有 SDD/SBE/Playbook」的規則是同一個精神，可以互相印證：不是每次改動都要停下來寫一份完美規格，而是規格跟著迭代滾動更新
- 具體的 `docs/{research,requirements,architecture,prj-tracking/{work-note,backlog,devlog}}` 目錄結構，比你現在 MyClaude/各專案裡文件散落各處（SDD/SBE/Playbook 命名不一）更systematic，可以考慮在新專案（例如正在規劃的雙 Agent 助理計畫）套用這套結構，跟既有的 [[efficient-sdd-delta-spec]]（增量規格降低token）、[[cline-memory-bank-structured-ai-memory]]（結構化記憶banks）是同一類「用固定文件結構餵AI」的做法，可以三篇對照參考怎麼混用
- `backlog/`+`devlog/`分離的做法，跟你自己的 handover skill（`~/.claude/skills/handover/SKILL.md`）功能上有點像，但這篇是「每個專案自己一份」而不是「跨專案一份 handovers.db」，如果你想讓某個特定專案的AI協作歷程更完整可查，可以在該專案下試著加這兩個資料夾
