---
title: Hermes Agent — create-telegram-bot Skill 定義
tags: [Agent, Hermes, Telegram, Skill, 自動化]
date: 2026-04-12
category: AI工具
---

## 這是什麼

Hermes Agent 的 `/create-telegram-bot` Skill，一鍵完成新 Telegram Bot 的完整建立流程：Profile → Token → SOUL.md → Skill → 資料夾 → registry.json。

---

## Skill Frontmatter

```yaml
---
name: create-telegram-bot
description: 新增 Hermes Agent Telegram Bot 的完整自動化流程。建立 Profile、寫入 Token、定制 SOUL.md、建立 Skill、建立本地資料夾、更新 registry.json。
trigger: /create-telegram-bot
---
```

---

## 觸發條件

- 「新增 Telegram Bot」
- 「建立新的 Bot」
- 「加一個 Telegram Bot」
- `/create-telegram-bot`
- `/create-telegram-bot {bot-name}`

---

## 執行流程（9 步驟）

### Step 1：收集基本資訊（互動式）

用 AskUserQuestion 收集：

1. Bot Token — 從 @BotFather 取得（格式：`數字:AA...`）
2. Bot username — Telegram Bot 的 username（如 `logistics_bot`）
3. Profile 名稱 — Hermes Profile 名稱（小寫英文，不含空格，如 `logistics`）
4. 角色定義 — Bot 用途（如「物流調度助理」）
5. Skill 名稱 — 專屬 Skill 名稱（如 `logistics-dispatch`）

### Step 1.5：確認資料來源與 MCP 工具（不可跳過）

用 AskUserQuestion 詢問需要哪些資料來源：

- 其他已有的 MCP Server（提供 Server 名稱和工具清單）
- 自訂腳本/API（提供腳本路徑或 API 端點）
- 參考文件/知識庫（提供文件路徑 PDF/MD/CSV）
- 目前不需要外部工具（純對話）

決策邏輯：

| 選項 | mcp_servers | SOUL.md |
|------|------------|---------|
| MCP Server | `[指定server]` | 加 MCP 規則，列出工具清單 |
| 自訂腳本/API | `[]` | 加腳本/API 使用說明 |
| 參考文件 | `[]` | 文件放 `bots/{bot-id}/knowledge/` |
| 不需要 | `[]` | 不加工具規則 |

若使用者無法回答，追問：「你希望 Bot 能查到什麼資料？」、「有現成系統/資料庫/檔案嗎？」

### Step 2：建立 Hermes Profile

```bash
hermes profile create {profile_name} --clone
```

驗證：`~/.hermes/profiles/{profile_name}/` 目錄存在

注意：clone 來的 .env TELEGRAM_BOT_TOKEN 可能帶 `#` 或是舊 Token，Step 3 兩種都要處理。

### Step 3：寫入 Telegram Token

```bash
# 移除舊的（不管有沒有 # 前綴）
sed -i '' '/TELEGRAM_BOT_TOKEN/d' ~/.hermes/profiles/{profile_name}/.env
# 寫入新的
echo 'TELEGRAM_BOT_TOKEN={token}' >> ~/.hermes/profiles/{profile_name}/.env
# 確保 GATEWAY_ALLOW_ALL_USERS
grep -q 'GATEWAY_ALLOW_ALL_USERS' ~/.hermes/profiles/{profile_name}/.env || \
  echo 'GATEWAY_ALLOW_ALL_USERS=true' >> ~/.hermes/profiles/{profile_name}/.env
```

驗證：`grep '^TELEGRAM_BOT_TOKEN=' ~/.hermes/profiles/{profile_name}/.env` 顯示正確 Token

### Step 4：定制 SOUL.md

覆寫 `~/.hermes/profiles/{profile_name}/SOUL.md`，結構如下：

```markdown
# {角色名稱}

你是一位{角色定義}，只處理{業務範圍}；不要延伸到{排除範圍}。

## 你的角色

1. **{具體職責1}** — {一句話說明}
2. **{具體職責2}** — {一句話說明}

## 業務範圍限制

- 只處理{具體列出}
- 不處理{具體列出}
- 若超出範圍，明確告知不在服務範圍內

## 工具使用規則（強制）

{根據 Step 1.5 動態生成}

## 決策原則

- {原則1}

## 溝通風格

- 繁體中文
- {風格描述}
```

SOUL.md 撰寫要點：

1. 開頭必須含業務邊界 — 「只處理 X；不延伸到 Y」
2. 角色職責要具體 — 不只寫「查詢」，要寫「查詢客戶下了哪些訂單、數量、交期與狀態」
3. 業務範圍限制必含 — 明確「做什麼」和「不做什麼」
4. 決策原則第一條寫範圍限制

工具使用規則生成邏輯：

- 有 MCP：「查詢 X 時，必須優先用 MCP 工具（mcp_{server}_*），禁止直接跑 SQL」，列出可用工具
- 有腳本/API：「優先用 {腳本路徑}，失敗才用 terminal」
- 只有文件：加「知識庫」區塊，列出文件路徑
- 無工具：不加此區塊

### Step 5：建立專屬 Skill

建立 `~/.hermes/profiles/{profile_name}/skills/{skill_name}/SKILL.md`：

```yaml
---
name: {skill_name}
description: {一句話描述，必須含業務邊界}
version: 1.0.0
author: hermes-agent-team
license: MIT
metadata:
  hermes:
    tags: [{相關標籤}]
---
```

Skill 主體結構：

- **適用範圍** — 明確列出做什麼/不做什麼
- **工作流程** — 標準步驟，含具體 MCP 工具（帶前綴）
- **MCP 工具對應表** — 場景 → 工具名稱（如有 MCP）
- **輸出格式** — 定義回覆的標準格式模板

### Step 6：建立本地資料夾

```bash
mkdir -p ~/bots/{bot-username}/knowledge
cat > ~/bots/{bot-username}/README.md << EOF
# {角色名稱}

Bot Username: @{bot-username}
Hermes Profile: {profile_name}
Skill: {skill_name}
Created: $(date +%Y-%m-%d)

## 用途
{角色定義}
EOF
```

### Step 7：更新 registry.json

```bash
# 若 ~/bots/registry.json 不存在，先建立
[ -f ~/bots/registry.json ] || echo '{"bots":[]}' > ~/bots/registry.json

# 用 Python 安全寫入（不破壞既有內容）
python3 - << 'PYEOF'
import json, os
from datetime import date

registry_path = os.path.expanduser('~/bots/registry.json')
with open(registry_path) as f:
    reg = json.load(f)

new_bot = {
    "username": "{bot-username}",
    "profile": "{profile_name}",
    "skill": "{skill_name}",
    "role": "{角色定義}",
    "created": str(date.today()),
    "local_dir": f"~/bots/{'{bot-username}'}"
}

# 避免重複
if not any(b['username'] == new_bot['username'] for b in reg['bots']):
    reg['bots'].append(new_bot)

with open(registry_path, 'w') as f:
    json.dump(reg, f, ensure_ascii=False, indent=2)

print(f"✓ 已新增 @{new_bot['username']} 至 registry.json")
PYEOF
```

### Step 8：驗證

```bash
# 確認 Profile 存在
ls ~/.hermes/profiles/{profile_name}/

# 確認 Token 正確
grep '^TELEGRAM_BOT_TOKEN=' ~/.hermes/profiles/{profile_name}/.env

# 確認 Skill 存在
ls ~/.hermes/profiles/{profile_name}/skills/{skill_name}/

# 嘗試啟動 Gateway（測試模式）
hermes -p {profile_name} gateway start &
sleep 3
# 在 Telegram 對 Bot 發 /start，確認有回應
kill %1 2>/dev/null
```

### Step 9：輸出摘要

完成後輸出：

```
✅ Telegram Bot 建立完成

Bot: @{bot-username}
Profile: ~/.hermes/profiles/{profile_name}/
Skill: {skill_name}
Local Dir: ~/bots/{bot-username}/

啟動指令：
  hermes -p {profile_name} gateway start

驗證：在 Telegram 對 @{bot-username} 發 /start
```

---

## 使用場景

- 新增業務 Bot（sales-bot）
- 新增客服 Bot（support-bot）
- 新增排程助理 Bot（scheduler-bot）
- 任何需要獨立 Telegram Bot + 專屬角色的場景
