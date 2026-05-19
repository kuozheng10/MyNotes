---
title: claude-code-setup：一行指令建好 Claude Code 完整生態
tags: [Claude Code, Skill, 工具, 自動化, 工作流程]
date: 2026-05-19
category: AI工具
source: https://x.com/NFTCPS/status/2056556067929350602
---

## 這是什麼

`claude-plugins-official` 是 Anthropic 官方 plugin 市集（GitHub）。
`claude-code-setup` 是其中的生態初始化外掛，一行指令自動掃描專案並設定完整開發環境。

```
/plugin install claude-code-setup@claude-plugins-official
```

---

## 核心概念 / 架構

安裝後自動配置四個層級：

| 層級 | 功能 |
|------|------|
| Hooks | 自動觸發腳本（git commit、lint、測試等） |
| Skills | 擴展任務（`/compact`、`/goal`、自訂 slash command） |
| MCP servers | 串接外部服務（DB、Slack、瀏覽器等） |
| Subagents | 子代理並行處理定義（`.claude/agents/`） |

Automations 負責把重複性工作全自動化，讓 Claude 從「打字機」升級為「自動化特種部隊」。

---

## 使用方法 / 快速啟動

```bash
# 安裝 claude-code-setup
/plugin install claude-code-setup@claude-plugins-official

# 已在用的 plugins（派哥現有）
claude --channels plugin:telegram@claude-plugins-official  # TG 串接
/plugin install claude-code-lsp@claude-plugins-official    # LSP 整合
```

---

## 對派哥的啟示

派哥已在用 `claude-plugins-official`（TG 串接就是走這個 registry）。下一步：

1. **跑 `claude-code-setup`** — 看它掃出什麼 Hooks/Skills 缺口，可能比手動維護 CLAUDE.md 更快
2. **Automations** — 如果 cc_processor、晨報、Gmail 整理可以包成 Hook，就不用靠 launchd 排程
3. **Subagents 自動生成** — 比照 `.claude/agents/` 手動管理，setup 可能直接從專案結構推導出建議的 agent 分工

注意：這篇是社群行銷文，有誇大成份。`claude-code-setup` 的實際功能以官方 README 為準，跑前先看一遍。

---

## 連結筆記

- [[claude-code-powerup-guide]] — /powerup 10 關卡，Claude Code 基本功
- [[claude-code-six-slash-commands]] — /goal、/compact 等核心指令
- [[gstack-claude-skills]] — Skills 生態完整說明
- [[claude-code-newbie-guide]] — 新手入門
