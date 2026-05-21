---
title: 龍蝦族維運架構 — 藍綠部署 + 不可變基礎架構，告別升級崩潰
tags: [openclaw, devops, 藍綠部署, 維運, ai-agent, 不可變基礎架構, 必學]
date: 2026-04-11
category: AI工具
---

## 核心觀念

> 「我不相信更新不會壞，所以我把系統設計成壞了也沒關係。」

**藍綠部署（Blue-Green Deployment）** + **不可變基礎架構（Immutable Infrastructure）** 應用在 AI Agent 維運。

---

## 四大保命原則

### 1. 靈肉分離（資料與程式碼絕對隔離）

**靈魂（記憶庫 + 金鑰）** 獨立存放，不放在程式碼目錄下：
- `.env`、`SOUL.md`、`MEMORY.md`、資料庫 → 獨立安全儲存區
- 程式碼（肉身）可以隨時丟棄重建

| 配置 | 靈魂 | 肉身 |
|------|------|------|
| 旗艦（NAS + VM） | NAS（高可用 + 快照） | VM SSD（高速運算） |
| 單機（PC + VM） | PC Host OS | VM（壞了重灌，靈魂不受影響） |

### 2. 一鍵轉世（Symlink 原子化部署）

```bash
# 版本資料夾
~/.openclaw/versions/v2.1/
~/.openclaw/versions/v2.2/   ← 新版本在旁邊安裝，不影響現有

# Symlink 當啟動指標
~/.openclaw/current → versions/v2.1/

# 升級：一行切換
ln -sfn ~/.openclaw/versions/v2.2 ~/.openclaw/current

# 回滾：一行切回
ln -sfn ~/.openclaw/versions/v2.1 ~/.openclaw/current
```

**秒級回滾**，新版有 bug 立刻切回舊版。

### 3. 物理結界（systemd 資源上限）

```ini
# /etc/systemd/system/openclaw.service
[Service]
CPUQuota=200%
MemoryMax=4G
Restart=on-failure   # 崩潰自動重啟（Self-healing）
```

防止 AI 死迴圈把整台機器搞掛。Mac 上可用 launchd `HardResourceLimits` 替代。

### 4. 海關安檢（版本相容性檢查）

```python
# check_version.py — 啟動前跑
if code_version != memory_version:
    raise SystemExit("記憶庫版本不相容，阻擋啟動，保護記憶不被污染")
```

新版程式碼改了資料庫結構，寧可不啟動，也不破壞舊記憶。

---

## 對派哥（一蘭）的直接應用

| 原則 | 現狀 | 可改進 |
|------|------|--------|
| 靈肉分離 | SOUL.md/MEMORY.md 在 workspace/ ✅ | 確保腳本更新不覆蓋記憶檔 |
| 一鍵轉世 | myclaude/ 直接覆蓋 ❌ | 加版本資料夾 + symlink |
| 物理結界 | Mac，無 systemd | launchd 設 CPU/Memory limit |
| 海關安檢 | 無 ❌ | AGENTS.md 版本號，session 開始時比對 |

---

## 連結筆記
- [[ai-agent-system-design-over-prompt]] — 系統設計優於 prompt 工程
- [[mempalace-ai-agent-memory]] — AI Agent 記憶管理
- [[openclaw-docs-skill]] — OpenClaw 文件
