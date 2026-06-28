---
tags: [claude-code, plugin, setup, mcp, skills, hooks, subagent, slash-commands, anthropic]
source: 派哥 TG 心得（2026-06-28）
date: 2026-06-28
---

# Claude Code Setup — Anthropic 官方外掛

## 是什麼

Anthropic 官方推出的 Claude Code 外掛，協助個人化設定工作流程。

**安裝方式：** Claude Code 輸入 `/plugin`，搜尋 `claude-code-setup`

---

## 功能

分析你的專案結構與使用模式，針對以下五個面向提出客製化建議：

| 面向 | 說明 |
|------|------|
| **MCP** | 哪些 MCP server 適合你的工作流 |
| **Skills** | 哪些 skill 值得建立 |
| **Hooks** | 哪些 hook 可以自動化 |
| **Subagent** | 哪些任務適合拆成子代理 |
| **Slash Commands** | 哪些指令值得客製化 |

---

## 派哥實測心得

> 針對我日常的工作流給出很具體的建議，有些地方真的都是我覺得卡卡的但是一直沒有時間好好想過要怎麼處理的痛點。

→ 值得定期跑一次，讓它幫你找出 CLAUDE.md / skills 的盲點

---

## 相關連結

→ [[claude-agent-five-layer-architecture]] — 外部設定五層（CLAUDE.md/Skills/Hooks/子代理/外掛）
→ [[anthropic-skill-three-layers-2026-06]] — Skill 三層架構
→ [[codex-plugins-openai]] — Codex 外掛對比
