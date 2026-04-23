---
title: Vibe Coding 三條保命規則 + Claude Hook RCE 真實案例
tags: ["安全", "Claude Code", "hook", "Vibe Coding", "開發流程"]
date: 2026-04-24
category: AI工具
source: Telegram 派哥分享
---

## 事件摘要

用 Claude Code 寫了 5 個 `.claude/hooks/` shell script，其中 `block-secrets.sh` 設計用來擋敏感資訊寫入，結果本身就有 RCE 漏洞。

**漏洞被另一個 AI subagent 抓到，不是人工審查。**

---

## 技術細節：heredoc injection

### 問題根源

```bash
# 有漏洞的寫法
python3 - <<PYEOF   # ← 沒有單引號！
content = """$FILE_CONTENT"""  # ← 直接插值
PYEOF
```

`<<PYEOF`（無引號）→ bash 先展開變數 `$FILE_CONTENT`
若檔案內容是 `"""; import os; os.system('rm -rf ~'); """`
→ Python 把它當成真正程式碼執行 → **RCE**

### 修正寫法

```bash
# 正確：heredoc 加單引號，變數用環境變數傳
export FILE_CONTENT="$INPUT"
python3 - <<'PYEOF'   # ← 單引號，bash 不展開
import os
content = os.environ['FILE_CONTENT']  # ← 環境變數，是資料不是程式碼
PYEOF
```

**原則：使用者資料不能跟程式碼混在一起（同 SQL injection、XSS、command injection 的道理）**

### 影響範圍

同樣的模式出現在 5 個 hook，`audit-log.sh` 有 2 個 heredoc 中招，**共 10 個注入點**，全部 AI 生成。

---

## Vibe Coding 三條保命規則

### 規則①：永遠懷疑確認選項

Claude Code 確認視窗的三個選項：
1. Yes（這次允許）
2. Yes, and don't ask again（永遠允許）
3. No

**操作紀律**：
- 第一次用的 skill/hook/agent → 選 1
- 用過 3 次確認行為可預期 → 才升級成 2
- 手滑選 2 的 3 秒鐘，就是攔下 AI 亂搞的最後機會

### 規則②：AI 審 AI，但要換 context

寫 code 的腦袋和挑毛病的腦袋要分開：

- 同一個 AI 在同一個 session 自己 review 自己 → 有偏見（「我剛寫的應該沒問題」）
- 換一個 subagent、換一個 session、換角色（如 `@schema-reviewer`）→ 才能抓到自己的盲點

問法：把 hook 丟給新 subagent，prompt = 「找出所有的 security 風險」

→ 跟 CLAUDE.md 的規範一致：**AI 寫的安全相關邏輯必須用另一個 AI 交叉審查**

### 規則③：commit 但不 push

在 CLAUDE.md 加硬規則：

> Claude can git add and git commit, but never git push. Push is a human-only action.

- `commit` 是本地的，可以 `reset`
- `push` 是公開的，爬不回來
- 若 repo 是 public，有 RCE 的 hook 被 clone 下去就會攻擊使用者

**這條規則已寫入派哥的 CLAUDE.md。**

---

## 對派哥的啟示

### 技術面

- 所有 heredoc 都要加單引號 `<<'PYEOF'`，這是必查項目
- 變數傳入 Python/其他語言的 inline script，用環境變數，不用字串插值
- hook 寫完後必須用 `gemini -p "找這個 hook 的安全漏洞"` 掃一次（AI 共享盲點規則）

### 已有保護

- CLAUDE.md 已有「不自動 push」規則
- 已有「安全相關邏輯用 Gemini 交叉審查」規則
- 這篇強化了具體的 heredoc 漏洞型態，值得加進 hook 撰寫的 checklist

### 額外洞見：透明度建立信任

作者 demo 時改說「AI 會出錯，我有規範去抓錯」，比說「AI 多強」更受客戶信任。
**賣「我怎麼管 AI」，不賣「AI 多厲害」。**

---

## 連結筆記

- [[ai-code-review-security-risk]] — AI 共享盲點問題（45% 漏洞率）
- [[skill-mcp-security-check]] — Skill/MCP 安全掃描 SOP
- [[harness-engineering]] — Hook + 防呆機制設計
- [[vibe-coding-architecture-debate]] — Vibe Coding 架構層不能省
