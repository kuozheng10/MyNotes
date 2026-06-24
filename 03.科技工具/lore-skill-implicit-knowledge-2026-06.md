---
tags: [claude, skill, claude-code, lore, implicit-knowledge, project-management, ai-tools]
source: 社群分享（muki，2026-06-24）
github: https://github.com/mukiwu/muki-ai-plugins
date: 2026-06-24
---

# Lore Skill — 管理專案隱性知識的 Claude Code 插件

> AI 可以讀懂程式碼，但讀不出那些只有人知道的眉角。Lore Skill 就是用來記錄這些。

---

## 什麼是 Lore？

「Lore」源自遊戲/奇幻文學，指長期口耳相傳、累積的知識（世界觀、歷史、傳說）。

在軟體專案裡，lore 是 **AI 光靠程式碼讀不出來的隱性知識**，例如：

- 各種合理、不合理的商業邏輯（及其背後成因）
- 某個 function 迂迴繞圈 → 為了相容某個舊系統
- 某些地方改起來沒事，實際上會把 B、C、D、E、F、G 整條線搞壞

**判斷標準**：一個資深工程師，光看現在的程式碼、型別、測試，能不能自己還原出這件事？

→ **不能** → 應該記成一條 lore

---

## 目錄結構

```
docs/lore/
├── payments/
│   ├── pitfalls.md          # 踩坑
│   ├── business-rules.md    # 商業邏輯與背後成因
│   └── api-map.md           # 可選
├── auth/
│   ├── pitfalls.md
│   └── business-rules.md
└── architecture/            # 可選補充
```

---

## 每個條目的格式

標題下加一行屬性（供 AI grep 用）：

| 屬性 | 說明 |
|------|------|
| `code` | 指到相關檔案/符號 |
| `updated` | 最後確認有效的日期 |
| `status` | `active` / `resolved` / `obsolete` |

**維護哲學**：標記優先於刪除。過期的知識標成 `obsolete`，不直接刪——很多時候還有參考價值。

---

## 四個 Skill

| Skill | 時機 | 作用 |
|-------|------|------|
| `lore-init` | 一次性 | 建立 `docs/lore/` 結構 |
| `lore-consult` | 動手前 | 撈出相關 lore，標記可能過期的條目 |
| `lore-capture` | 踩雷後 / 決策釐清後 | 把隱性知識整理成新條目 |
| `lore-maintain` | 定期整理 | 標記過期、調整索引，防止文件長成叢林 |

**標準流程**：動手前先 `consult` → 學到東西就 `capture` → 偶爾 `maintain` 打掃 → `init` 只做一次

---

## CLAUDE.md 整合建議

```
專案 lore plugin 放在 docs/lore/，在規劃以及修 bug 前先查，學到隱性知識就紀錄進去
```

加進去後，其他 skill 會自然把 lore 納入流程。

---

## 最大好處

即使幾個月沒碰這個 repo，再回來也不用重新認識一次——當初的理由跟教訓都在 lore 裡。

---

## 對派哥的評估

✅ **直接相關**：
- 派哥的 cc_processor、investment 系統都有大量只有他知道的眉角（e.g. CTBC 2026 格式換了、PyMuPDF 讀不了電子對帳單）
- 這些知識目前散落在 CLAUDE.md、memory files、handover 裡，lore 是更結構化的補充

💡 **可考慮的整合**：
- cc_processor `docs/lore/pitfalls.md` → 記錄 invalid_grant、CTBC 格式換版、Amex PDF 加密等踩坑
- investment `docs/lore/business-rules.md` → 記錄正負號規則、Notion UID 設計、Fubon 基金 vs 台股分流等

---

## 相關筆記

- [[anthropic-skill-three-layers-2026-06]] — Skill 三層架構 + 自我進化迴圈
- [[claude-skill-social-post]] — Skill 社群實踐
- [[agentic-sop-to-work]] — Agentic SOP 流程
