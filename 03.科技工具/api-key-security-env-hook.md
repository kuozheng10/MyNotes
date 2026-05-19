---
title: API Key 安全：不貼給 AI，用 .env + Hook 真正攔截
tags: [安全, Claude Code, 工具, 自動化]
date: 2026-05-19
category: AI工具
source: telegram/手打
---

## 核心觀念

AI 叫你「把 API Key 貼上」很方便，但 key 就進了 AI 公司的伺服器歷史紀錄。正確做法：key 放 `.env`，由 script 自己讀，不讓 AI 碰。

---

## 三層防護

### 1. 存 .env，叫 script 讀
```bash
# .env
OPENAI_API_KEY=sk-...

# script 裡
from dotenv import load_dotenv
load_dotenv()
key = os.environ["OPENAI_API_KEY"]
```

叫 AI 設定時說：「請教我怎麼用 .env 存 API key，但你不要打開它」

### 2. CLAUDE.md 加規則（口頭約定）
```
永遠不讀 .env、~/.zshrc 等敏感檔案
永遠不要問我 API Key，由 script 自己載入
```

### 3. Hook 真正攔截（比口頭有效）

口頭規則 = 希望 AI 記得。Hook = 強制執行，不管 session 多長。

---

## 實作（已套用到派哥設定）

`~/.claude/hooks/env-guard.sh`：PreToolUse hook，攔截 Read/Edit 工具存取：
- `/.env`、`.env.*`
- `.zshrc`、`.bashrc`、`.profile`
- `/.ssh/`、`id_rsa`、`id_ed25519`
- `.netrc`

---

## 哪些不在攔截清單

- `token.json`、`credentials.json` — Google API 合法存取，不擋
- `.claude/settings.json` — 設定檔，不是 secret

---

## 連結筆記

- [[codex-hooks-event-trigger]] — Hook 機制完整說明
- [[python-shared-config-single-source-of-truth]] — token 路徑單一來源原則
- [[vibe-coding-rce-heredoc-three-rules]] — vibe coding 安全天條
