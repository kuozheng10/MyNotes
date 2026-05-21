---
title: Google Gemini Notebooks — 對話資料夾化，打造個人 AI 知識庫
tags: [gemini, notebooklm, google, 知識管理, notebooks, 工作流]
date: 2026-04-10
category: AI工具
source: https://applealmond.com/posts/309536
---

## 這是什麼

Google Gemini 於 2026-04-09 推出 **Notebooks** 功能（付費用戶優先）。
把 Gemini 對話從「單次問答」升級為「資料夾式專案管理」，與 NotebookLM 雙向打通。

---

## 六大功能

| 功能 | 說明 |
|------|------|
| **Notebooks（資料夾化）** | 對話分門別類，旅遊/研究/專案各自獨立 |
| **NotebookLM 深度整合** | NotebookLM 收集+比對來源，Gemini 分析+產出 |
| **Instructions（指令）** | 每個 Notebook 可設專屬語氣/風格，互不干擾 |
| **Sources（來源）** | 上傳 PDF / 文字檔 / 貼網址作背景知識，降低幻覺 |
| **自動共享來源** | 同 Notebook 內所有對話自動共用已上傳的資料 |
| **個人化脈絡** | 記住特定專案的上下文，建議更精準 |

---

## 對派哥的實際用法

### MyNotes × Gemini Notebooks 組合技

```
MyNotes md → Google Drive → Gemini Notebook「知識庫」
                               ↑ Sources：上傳 MyNotes-combined.txt
                               ↑ Instructions：「你是派哥的知識庫助手，回答時引用筆記來源」
                               ↓
                          查詢直接在 Gemini 問，0 Claude token
```

### 建議 Notebook 結構

| Notebook 名稱 | Instructions 設定 | Sources |
|---|---|---|
| MyNotes 知識庫 | 引用筆記來源，繁體中文 | MyNotes-combined.txt |
| cc_processor 專案 | 技術風格，專注帳單自動化 | 相關文件 |
| 旅遊規劃 | 輕鬆語氣，重點條列 | 旅遊筆記 |

### Instructions 的關鍵價值

同一個 Gemini 帳號可以有多個 Notebook，每個行為不同。
→ 用「MyNotes 知識庫」Notebook 查資料時，不會和其他對話混淆

---

## 上線狀態

- 2026-04-09 起推送
- 優先：Gemini Advanced 付費用戶
- 免費用戶：等後續批次更新

---

## 連結筆記
- [[notebooklm-gemini-integration]] — NotebookLM 整合 Gemini 概覽
- [[notebooklm-slides-advanced]] — NotebookLM 生簡報 + Graphify
- [[claude-token-saving-tips]] — Claude 省 token 策略
