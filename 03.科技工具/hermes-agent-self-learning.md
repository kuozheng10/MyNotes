---
title: Hermes Agent — 安裝指南、架構與多 Bot 管理
tags: [Agent, AI, LLM, Telegram, 知識管理, 工具, 架構設計, 安裝指南]
date: 2026-04-12
category: AI工具
source: https://github.com/NousResearch/hermes-agent
---

## 這是什麼

Nous Research 開源的 AI Agent，具備「閉環學習（Closed Learning Loop）」能力。
成功完成任務後會自動抽取邏輯、寫成 Skill，並持續自我進化。
支援 14+ 平台（Telegram、Discord、Slack…），可部署多個獨立 Bot（Profile 隔離）。

---

## macOS 安裝（一鍵）

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
source ~/.zshrc
hermes setup    # 互動式設定 LLM provider + API key
hermes          # 開始聊天
```

安裝器自動處理：uv、Python 3.11、Node.js v22、ripgrep、ffmpeg。
**不要用 sudo，會壞掉。**

診斷工具：`hermes doctor`

---

## 初次設定流程（hermes setup）

1. 選 LLM provider（Anthropic / OpenAI / OpenRouter / Ollama 等）
2. 輸入 API key
3. 設定工具開關
4. 選配平台（Telegram / Discord / Slack）

**注意：需要至少 64,000 token context window 的模型，否則拒絕啟動。**

---

## Profiles — 多 Bot 隔離架構

每個 Profile 是完全獨立的 Agent 實例：

```bash
hermes profile create logistics --clone   # 從預設 clone
hermes profile list                       # * = 當前預設
hermes -p logistics chat                  # 臨時指定
hermes profile export logistics           # 備份
```

**Profile 目錄** `~/.hermes/profiles/<name>/`：

```
config.yaml   — 模型設定
.env          — API keys、Bot token
SOUL.md       — 角色個性（最高優先系統 prompt）
memories/     — 對話歷史
skills/       — 安裝的 Skills
state.db      — 記憶資料庫（SQLite）
```

---

## Telegram Gateway 設定

```bash
# 從 @BotFather 取得 token，@userinfobot 取得 user ID（數字）
hermes gateway setup   # 選 Telegram → 貼 token → 輸入 user ID
hermes gateway start
```

多 Profile 各自獨立 Bot token：

```bash
hermes -p logistics gateway setup
hermes -p logistics gateway start
```

已知坑：
- 必須從 home 目錄啟動 gateway，否則讀到開發版 SOUL.md
- WSL2 建議 `hermes gateway run`（前景）代替 systemd
- 安裝新工具後重跑 `hermes gateway setup` 刷新 PATH

---

## SOUL.md — 角色定義

定義 Bot 是誰、邊界在哪、怎麼說話。

```markdown
# 角色名稱

你是一位 {角色}，只處理 {業務範圍}；不延伸到 {排除範圍}。

## 你的角色
1. **職責一** — 說明

## 業務範圍限制
- 只處理：...
- 不處理：...

## 工具使用規則（若有 MCP）
查詢 {系統} 時必須優先用 MCP 工具（mcp_{server}_*）。

## 溝通風格
繁體中文，{風格}
```

---

## MCP Server 整合

在 `~/.hermes/config.yaml`：

```yaml
mcp_servers:
  my_server:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-xxx"]
    env:
      API_KEY: "xxx"
    tools:
      include: ["tool1", "tool2"]   # 白名單
```

工具命名：`mcp_<server>_<tool>`（如 `mcp_scheduler_query_orders`）

---

## Skills 系統

存放：`~/.hermes/profiles/<name>/skills/<skill-name>/SKILL.md`

```yaml
---
name: skill-name
description: 一句話含業務邊界
version: 1.0.0
metadata:
  hermes:
    tags: [標籤]
---
```

Progressive disclosure：L0 名稱→L1 全文→L2 reference，按需載入省 token。

---

## 四層記憶系統

| 層 | 儲存 | 特點 |
|----|------|------|
| 1 | MEMORY.md + USER.md | ~3575 字元上限，最高優先 |
| 2 | SQLite FTS5 | 全歷史，毫秒搜尋 |
| 3 | Skills（Markdown） | 自動生成工具庫 |
| 4 | Honcho | 使用者偏好演進追蹤 |

---

## 常見問題排查

| 問題 | 解法 |
|------|------|
| `hermes` not found | `source ~/.zshrc` |
| HTTP 400 on chat | 模型名稱錯，確認 provider 有此 model |
| Gateway 讀到開發版 SOUL | 從 home 目錄啟動 |
| clone 的 .env token 有 # 前綴 | `sed -i '' '/TELEGRAM_BOT_TOKEN/d' .env && echo 'TELEGRAM_BOT_TOKEN=xxx' >> .env` |

---

## 安裝前準備清單

- [ ] 確認有 `git`
- [ ] 準備 Anthropic 或 OpenRouter API key
- [ ] @BotFather 建立 Bot → token
- [ ] @userinfobot 取得自己的 user ID（數字）

---

## 對派哥的應用

- OpenClaw + 一蘭是類似架構；Hermes 更完整（原生多平台、profile 隔離、自動 skill 生成）
- 未來：用 Hermes 建多個專用 Bot（物流、客服、業績…），Profile 隔離互不干擾
- 第一步：裝 Hermes → 設 Anthropic API → 驗 Telegram gateway
- `create-telegram-bot` skill 已設計好，安裝後一鍵新增 Bot

---

## 連結筆記

- [[hermes-create-telegram-bot-skill]] — create-telegram-bot 完整 Skill 定義
- [[mempalace-ai-agent-memory]] — AI 記憶管理多層架構
- [[agent-skills-standard]] — Skill 標準化（agentskills.io）
