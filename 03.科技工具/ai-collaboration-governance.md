---
title: AI 協作治理架構：憲法 / ADR / Skill / Memory 四層切法
tags: [ai-workflow, governance, memory, skill, adr, claude-code]
date: 2026-04-26
category: AI工作流
---

## 核心觀點

AI 協作的問題，表面上是記憶問題，骨子裡是**治理問題**。沒有治理，AI 是個很會講話但容易失憶、漂移、產生幻覺的外包商。

## 四層治理架構

### 第一層：憲法（Constitution）
最高原則，定義邊界：
- 什麼是單一事實來源（Single Source of Truth）？
- 決策跟執行誰負責？
- 記憶的邊界劃在哪？
- 哪些東西不能隨視窗、模型、時間漂走？

沒有憲法，下面什麼都會打架。

### 第二層：ADR 管 Why

ADR（Architecture Decision Record，架構決策紀錄）——重要決策不能只留在聊天裡飄走，要寫下來：
- 當時為什麼這樣做？
- 有哪些選項？
- 為什麼選這個？
- 哪些還沒拍板？

不記 ADR 的後果：幾週後只記得結論、脈絡全忘光，AI 換個視窗會自己重新發明一套理由。

### 第三層：Skill 管 How

Skill 是把重複做法寫成 SOP：
- 專案怎麼命名
- handoff 怎麼寫
- commit 前檢查什麼
- 遇到 pending 怎麼處理

**不應該每次靠聊天從頭教一次**，應變成可讀取、可版本控管、可重複使用的操作手冊，AI 直接讀。

### 第四層：Memory 管 What happened

記錄已發生的事：共識、教訓、回饋、專案狀態、偏好、踩過的坑。

**關鍵觀念：不是所有記憶都適合流動。**

記憶沒有邊界，就不是資產，是污染源。工作空間、專案、視窗都要有邊界。

## 工作流三角

| 層 | 負責 |
|----|------|
| Chat | 討論、裁決 |
| Cowork | 執行、交接 |
| Code | 實作、commit、push |

三者中間不能只靠「我記得」撐著。需要 handoff、worklog、repo 文件、CLAUDE.md、PENDING.md 等**硬載體**傳遞狀態。

## 各層失效模式

| 層 | 缺失後果 |
|----|---------|
| 憲法漂走 | 整個系統價值觀打架 |
| ADR 缺失 | AI 重新發明理由 |
| Skill 缺失 | 每次重新教一遍 |
| Memory 缺失或污染 | 上下文不準或互相干擾 |

## Pending 與觀察期

治理規則不是越多越好，也不是一次寫死。有些可等平台能力成熟（記憶、同步、snapshot），有些靠使用經驗收斂（handoff 格式、ADR 上限、哪些規則需升級）。

好的治理系統要能：新增、觀察、驗證、暫緩、升級、廢止規則。

## 與派哥現有系統的對應

| 治理層 | 派哥現有工具 |
|--------|------------|
| 憲法 | CLAUDE.md 全域規範 |
| ADR | 尚未系統化（待補） |
| Skill | `~/.claude/skills/` |
| Memory | `~/.claude/projects/.../memory/` |
| 工作流硬載體 | handover skill、session worklog |
