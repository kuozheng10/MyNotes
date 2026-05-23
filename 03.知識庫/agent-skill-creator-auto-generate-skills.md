---
title: Agent Skill Creator——自動從文件生成 AI Skill 模組，支援 14 個平台
tags: [AI Agent, Skill, Claude Code, 自動化, 知識管理, 團隊協作]
date: 2026-05-23
category: 科技工具
source: https://github.com/FrancyJGLisboa/agent-skill-creator
---

## 解決什麼問題

Claude Code、Copilot、Cursor 等工具初始狀態不知道你的內部流程，每次對話都要重複說明。
→ **Agent Skill（技能模組）** 讓 AI 自動載入你的知識，不用每次解釋。

但建構一個合格 Skill 很繁瑣（規格格式、prompt、漸進載入、啟動關鍵字…）

**Agent Skill Creator = 把這個流程全自動化。**

---

## 怎麼用

輸入任何素材（亂文件 / URL / PDF / 程式碼 / 會議紀錄）
→ AI 自動解讀需求 → 生成 SKILL.md + 目錄結構 + 程式碼
→ 安全掃描（排除硬編碼 key）
→ 一鍵安裝到你的 AI 工具

---

## 支援平台

| Tier | 工具 | 安裝方式 |
|------|------|---------|
| Tier 1（原生支援）| Claude Code、GitHub Copilot、Gemini CLI | 直接讀 SKILL.md |
| Tier 2（自動轉換）| Cursor、Windsurf 等 | 轉換為 .mdc / .md 規則格式 |

通用路徑：`~/.agents/skills/`（多工具共享）

---

## 團隊共享機制

1. AI 建好 Skill 後自動偵測你的 Git 平台（GitHub / GitLab）
2. 建立 repo + 推送
3. 產出單行安裝指令供團隊成員複製
4. 成員 clone 後即可在自己的 AI 用 `/skill名稱` 喚用

---

## 品質維護

- **結構驗證**：規格格式是否符合標準
- **安全審計**：掃描是否有硬編碼 API key
- **過期偵測**：外部 URL 可達性、API 回傳結構變更自動告警

---

## 對派哥的評估

你已經有自己的 skill 系統（`~/.claude/skills/`），且已手動維護多個 SKILL.md。

Agent Skill Creator 的價值在於：
- 把「亂文件 → Skill」這段自動化
- 如果要把你的 SOP 分享給別人（或未來的自己），可以用它生成標準格式

**建議**：先試一個現有 SOP（如 cc_processor 流程文件）看生成品質，再決定是否導入。

---

## 相關

- [[cisco-jeetu-patel-agentic-ai-digital-coworkers]] — 代理邊界與委派思維
