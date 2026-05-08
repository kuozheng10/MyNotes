---
title: Python 共用設定：單一來源原則（Single Source of Truth）
tags: [Python, OAuth, 設計原則, DRY, Google API, 教訓]
date: 2026-05-08
category: AI工具
---

## 核心規則

共用設定（OAuth scopes、token 路徑、API key 等）只能定義一次，其他腳本一律 import，不能複製貼上。

---

## 真實案例：Google token 三度崩潰

**現象**：`invalid_grant` 每隔幾天就出現一次，重新授權後隔天又壞。

**根因**：
- `google_utils.py` 定義 `SCOPES = [gmail.modify, drive, calendar]`（3 個）
- `check_google_token.py` 自己複製了一份 `SCOPES = [gmail.modify]`（1 個）
- 健檢每天 08:30 用 1 個 scope 刷新並寫回 token
- 09:00 主腳本讀 token，發現 scope 不足，嘗試重新授權 → `invalid_grant`

**修法**：
```python
# ❌ 錯誤：自己寫一份
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

# ✅ 正確：從來源 import
import sys
sys.path.insert(0, '/Users/kuochengchen/Documents/MyClaude')
from cc_processor.google_utils import SCOPES, TOKEN_FILE, CREDS_FILE
```

---

## 通用原則

| 設定類型 | 放在哪裡 | 其他地方怎麼用 |
|---------|---------|-------------|
| OAuth scopes | `google_utils.py` | `from google_utils import SCOPES` |
| token 路徑 | `google_utils.py` | `from google_utils import TOKEN_FILE` |
| API key / bot token | `.env` 或 `config.py` | `import os; os.environ['KEY']` |
| 資料庫連線字串 | `db.py` 或 `.env` | import 或環境變數 |

**任何需要在兩個以上地方用到的值，就是需要抽出來的訊號。**

---

## 連結參考

- [[harness-engineering-automation-risks]] — 自動化風險管控
- [[claude-agent-five-layer-architecture]] — Claude Code 設定架構
