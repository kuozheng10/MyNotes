---
title: OpenClaw Docs Skill — 多頻道 AI Gateway 完整文件技能
tags: [OpenClaw, AI, Gateway, Skill, 多頻道, Claude Code]
date: 2026-04-08
category: AI工具
source: https://github.com/tbdavid2019/openclaw-docs-skill/
---

## 這是什麼

OpenClaw 官方 docs skill，提供給 Claude Code / Codex / Gemini 使用，讓 AI 助理能回答 OpenClaw 的安裝、設定、操作、除錯問題。

---

## OpenClaw 簡介

自架多頻道 AI Gateway，一套設定路由至 15+ 通訊頻道：
- Telegram、WhatsApp、Discord、Slack、iMessage、Line、Signal、Matrix…
- 支援 60+ AI 提供者（Anthropic、OpenAI、Google、Groq、Ollama…）
- 多 Agent 路由 + 工作區隔離
- 外掛系統（Plugin SDK）
- 安全強化（沙盒、信任代理認證）

---

## Skill 安裝方式

### Claude Code
```bash
cp ~/Documents/GitHub/openclaw-docs-skill/SKILL.md ~/.claude/skills/openclaw.md
```

### 保持更新
```bash
cd ~/Documents/GitHub/openclaw-docs-skill && git pull
cp SKILL.md ~/.claude/skills/openclaw.md
```

---

## Skill 覆蓋範圍（SKILL.md 402 行）

- 安裝與升級（15+ 平台）
- openclaw.json 設定與模型管理
- 30+ 頻道設定（含 Telegram、WhatsApp、Discord）
- Gateway 操作、健康監控、排錯
- 多 Agent 路由與工作區隔離
- Plugin 開發（SDK）
- 安全強化（沙盒、secrets、威脅模型）
- 常見錯誤 11 條 + 修復方式

---

## 關鍵路徑
- 設定檔：`~/.openclaw/openclaw.json`
- 工作區：`~/.openclaw/workspace`
- Gateway bind：`127.0.0.1:18789`

---

## OpenClaw CLI 快速指令

```bash
openclaw status                     # 整體狀態
openclaw gateway status             # Gateway 守護進程
openclaw doctor                     # 診斷問題
openclaw channels status --probe    # 頻道健康檢查
openclaw gateway start/stop/restart
openclaw gateway --force            # 強制關閉重啟
openclaw config set <path> <value>  # 設定配置
openclaw security audit --fix       # 安全自動修復
openclaw channels add               # 新增頻道
openclaw models set <model>         # 設定預設模型
```

---

## 自動更新架構
GitHub Actions 每天 04:00 UTC 從上游 openclaw/openclaw 同步最新文件並 auto-commit。

---

## 連結筆記
- [[ai-agent-modular-architecture]] — OpenClaw = 核心能力層與介面層分離的典範
- [[agent-skills-standard]] — Skill 資產化的實作方式
