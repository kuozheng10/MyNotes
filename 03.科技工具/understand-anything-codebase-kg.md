# Understand Anything — 程式碼庫知識圖譜工具

> 來源：GitHub Trending｜2026-06
> 連結：https://github.com/Egonex-AI/Understand-Anything
> 星數：59.2k（Trending #1）

---

## 做什麼

把整個程式碼庫轉成可點擊、可提問的知識圖譜：

- **依賴視覺化**：點一個函式，立刻看出誰呼叫誰
- **自然語言 Q&A**：直接問「支付流程怎麼跑？」，它回答你
- **Diff 影響分析**：改程式碼前跑 `/understand-diff`，預告哪些地方可能出問題
- **整合支援**：Claude Code、Cursor、VS Code，一行指令裝好

---

## 怎麼用（一行裝好）

```bash
# 參考官方 README
npx understand-anything init
```

然後在 Claude Code 裡：
```
/understand-diff          # 分析這次改動的影響範圍
/understand "問題"        # 自然語言問 codebase
```

---

## 對派哥的評估

| 場景 | 有沒有用 |
|------|----------|
| 接手 cc_processor 這種自動化 Python | ✅ 可以快速看清函式呼叫關係 |
| investment dashboard Next.js | ✅ 改 API route 前確認影響範圍 |
| 小腳本修改（<200行）| ❌ 沒必要，直接讀即可 |

**建議**：中大型 codebase（>10 個檔案互相呼叫）才裝，小腳本不值得。

---

## 關聯筆記

- [[agentic-sop-to-work]] — Claude Code 輔助工具生態
