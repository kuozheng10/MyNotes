# agentic-sop-kit — 把人工 SOP 變成安全的 agentic workflow

> 來源：https://github.com/s0912758806p/agentic-sop-to-work
> 儲存日期：2026-06-13
> 標籤：#claude-plugin #sop #workflow #agentic #automation

---

## 是什麼

Claude Code plugin，把你手寫的 SOP 工程化成 LLM 可安全、可重複執行的 agentic workflow。

核心概念：Human SOP → single-tool skills → run.py（確定性引擎）→ per-step 硬閘門 → DRAFT → 人核准

**不是聊天機器人，是流程引擎。**

---

## 為什麼安全（解決 LLM 四大問題）

| 問題 | 解法 |
|------|------|
| 臆造（fabrication） | 事實只來自輸入，缺的標 `【待補】` |
| 假自主 | 確定性的事用程式；硬閘門零 LLM |
| 無人負責的產出 | 產出一律 DRAFT，需人核准 |
| mega-agent 退化 | Stop-hook 回歸閘門，每次變更重跑測試 |

---

## 主要組件

| 組件 | 說明 |
|------|------|
| `agentic-sop` skill | 入口：純需求 → 起草 SOP；有 spec → 直接用 |
| `agentic-workflow-audit` skill | 唯讀稽核，檢查 mega-agent 退化 |
| `/agentic-sop-kit:sop-flow` | 執行編排，回報 DRAFT |
| `Stop` hook | 每次變更 → 自動重跑測試 → 失敗就擋住 |
| `kit/run.py` | 確定性引擎（cmd_gate/schema_gate/trace_gate/recompute_gate） |

---

## 安裝

```bash
# Claude Code 內執行
/plugin marketplace add s0912758806p/agentic-sop-to-work
/plugin install agentic-sop-kit@agentic-sop-to-work
/reload-plugins
```

---

## 使用方式

```
# 有需求 → 自動起草 SOP
「我想自動化帳單匯入流程」

# 有現成 spec → 直接執行
/agentic-sop-kit:sop-flow

# 搭配 /goal + auto mode 效果最好
```

---

## 評估（對派哥的用途）

✅ **很對口**，理由：
- 派哥有很多重複性 SOP（cc_processor 帳單匯入、bank sync、notion 驗證）
- Stop-hook 回歸閘門 = 改完自動跑測試，正好補 cc_processor 的安全網
- 「DRAFT + 人核准」符合派哥「大改版推前確認」的習慣
- 作者是台灣人，repo 中文文件齊全

⚠️ **前提**：
- 不是「裝了馬上爽」，需要先把現有 SOP 整理成 flow.json
- 適合先拿一個流程試水溫（建議：bank sync 驗證流程）
- 160 stars，相對小眾但品質高、今天仍在更新

---

## 建議先試的流程

派哥的 `notion_sync` 驗證流程（SQLite vs Notion 筆數比對）是最好的入門對象：
1. 有明確的輸入（SQLite）和輸出（Notion 頁面）
2. 有硬性驗證條件（每月筆數全 ✅）
3. 失敗要擋住不能回報完成
