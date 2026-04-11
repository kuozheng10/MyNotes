---
title: Obsidian Tutor Skill — 自動把 PDF/GitHub 轉成雙向連結筆記庫 + 測驗系統
tags: [obsidian, skill, moc, 雙向連結, 學習, 知識管理, 必學]
date: 2026-04-11
category: AI工具
source: https://github.com/bevibing/tutor-skills
---

## 這是什麼

**Tutor Skill** — 丟入 PDF 或 GitHub 專案，AI 自動建構：
- 雙向連結（`[[wikilinks]]`）知識網
- MOC（Map of Content）索引筆記
- 主動回憶測驗題 + 互動測驗模式

---

## 轉換流程

```
PDF / GitHub 專案
    ↓ /tutor-setup
原子化筆記（每個概念一個檔案）
    ↓ 自動建立 [[wikilinks]]
雙向連結知識網 + MOC 索引
    ↓ /tutor
互動測驗（追蹤薄弱環節）
```

---

## 安裝與使用

```bash
# 安裝
npx skills add bevibing/tutor-skills

# 建庫（進入資料夾後）
/tutor-setup

# 啟動測驗
/tutor
```

---

## kepano 官方 Obsidian Skills（配套）

GitHub: https://github.com/kepano/obsidian-skills
由 Obsidian 執行長發起，提供 AI 正確操作 Obsidian 的 Skills：

| Skill | 功能 |
|-------|------|
| **obsidian-markdown** | 教 AI 用 wikilinks、Callouts、frontmatter |
| **json-canvas** | 讀寫 `.canvas` 白板檔 |
| **obsidian-bases** | 操作 Obsidian 結構化資料庫 |
| **defuddle** | 網頁 → 乾淨 Markdown，省 token |

---

## MOC vs Base 資料庫的選擇

| 方式 | 優點 | 缺點 |
|------|------|------|
| **手動 MOC + 雙向連結** | 知識網絡豐富，意外連結多 | 維護費力 |
| **Base 資料庫** | 過濾快、結構化查詢 | 無雙向連結 |

**派哥建議**：MyNotes 已是 md 檔 + 手動 wikilinks，Tutor Skill 適合學新領域時快速建庫，現有 MyNotes 維持現狀即可。

---

## 對派哥的直接應用

- **學新工具（如 cc_processor 用到的 Google API）**：丟入官方文件 PDF → Tutor Skill 自動建學習庫
- **閱讀 GitHub 專案**：丟入 repo → 快速理解架構，比直接讀 code 快
- **現有 MyNotes**：不需要跑 Tutor Skill，格式已OK

---

## 連結筆記
- [[obsidian-ai-agent-skills-guide]] — Obsidian AI Agent Skills 必裝指南
- [[obsidian-llm-knowledge-management]] — Obsidian × LLM 知識管理
- [[vault-search-obsidian-plugin]] — Obsidian Vault Search
