# Ponytail — 防止 AI 過度設計的開源插件

> 來源：ExplainThis｜2026-06
> 連結：https://github.com/DietrichGebert/ponytail

---

## 解決什麼問題

AI agent 寫程式時常把 5 行能解決的問題寫成 500 行。
Ponytail 在 AI agent 運行時提醒它：**不寫程式碼是最容易維護的程式碼**。

---

## 實測結果

| 指標 | 效果 |
|------|------|
| Token 消耗 | 下降 40%+ |
| 完成速度 | 提高 3～6 倍 |

測試場景：email 驗證器、限流器實作等。

---

## 核心哲學

> "The best code is no code."

提醒 AI agent 的三個原則（依 Ponytail 精神）：
1. 能用標準庫就別引外部套件
2. 能用 10 行就別寫 100 行
3. 抽象只有在真的被複用時才值得

---

## 對派哥的評估

**值得試**：Claude Code 有時確實會過度包裝（多一層 class、多一個 helper）。
在跑大任務前加這個 prompt 約束，可減少 review 來回。

**怎麼用**：參考 README，應是一個 system prompt snippet 或 MCP plugin，加進 CLAUDE.md 或 `/system-prompt`。

---

## 關聯筆記

- [[agentic-sop-to-work]] — Claude Code 任務品質管控
- [[ai-engineering-evolution]] — AI 工程演進，過度設計是常見陷阱
