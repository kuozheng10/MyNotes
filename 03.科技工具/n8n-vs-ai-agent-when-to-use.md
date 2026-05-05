---
title: n8n vs AI Agent：什麼時候用哪個？派哥需要 n8n 嗎？
tags: [n8n, 自動化, workflow, no-code, AI整合, OpenClaw, Claude Code]
date: 2026-05-05
category: AI工具
source: X/社群討論
---

## 這是什麼

n8n 是開源的 no-code 自動化工具（類似 Zapier/Make 但可自架）。一篇討論「n8n 已死了嗎（被 Claude Code/OpenClaw 取代）」的文章，結論是：沒有，兩者互補。

---

## n8n 核心強項

- **穩定固定流程**：一旦設定好，跑 100 次結果相同，不會「想太多」
- **視覺化**：拖拉式 workflow，非技術人員也能維護
- **現成 400+ 節點**：Gmail、Google Sheets、Slack、Notion、Webhook 等直接串
- **自架**：資料不過第三方，可完全控制
- **觸發器多樣**：Webhook、定時、Email、API 呼叫

## AI Agent 的強項

- **彈性決策**：根據內容判斷下一步，n8n 做不到條件太複雜的情況
- **非結構化輸入**：圖片 OCR、PDF 解析、自然語言理解
- **動態任務**：任務不固定、需要上下文理解

---

## 最佳實踐：n8n + AI Agent 組合

最強的模式不是「選一個」，而是分工：

**n8n 當穩定管道，AI Agent 當決策核心**
- n8n：接收 webhook → 清洗資料 → 呼叫 AI → 寫回 Notion/Google Sheets
- AI Agent：接受 n8n 提供的結構化資料，做判斷/生成

**AI Agent 把 n8n workflow 當工具**
- OpenClaw/Claude Code 呼叫 n8n workflow（via Webhook）
- n8n 負責「固定的骨架」，AI 負責「彈性的大腦」

類比：n8n 是 CI/CD pipeline，AI Agent 是程式碼。pipeline 穩定，程式碼靈活。

---

## 派哥需要 n8n 嗎？

**現況評估**：

| 派哥現有流程 | 現在怎麼做 | n8n 能幫嗎？ |
|------------|-----------|------------|
| cc_processor 帳單處理 | Python + Vision OCR + Notion API | ❌ 太複雜，OCR 非 n8n 強項 |
| Morning briefing | Bash + Gemini CLI + Telegram | ❌ 已穩定跑，換平台沒必要 |
| Gmail automation | Google Apps Script | 🟡 n8n 可取代，但 GAS 已在跑 |
| MyNotes 備份 | git + OpenClaw cron | ❌ 太簡單，不需要 n8n |
| 未來：新增 Webhook 觸發流程 | 沒有 | ✅ 這是 n8n 最值得用的地方 |

**結論：派哥目前不需要導入 n8n**

原因：
1. 現有流程都是 Python/Bash 實作，遷移成本高
2. Claude Code + OpenClaw 已覆蓋動態任務
3. cc_processor 的 OCR 邏輯遠超 n8n 節點能做的

**何時才值得導入**：
- 想新增「不涉及複雜邏輯」的串接（如：收到 Gmail → 自動貼 Telegram）
- 想讓非技術夥伴維護部分流程
- 有需要「穩定 webhook 觸發」的新專案（不是改舊的）

---

## 學習資源（備查）

- 18 天免費課程：x.com/ClickUpWithAda（基礎串接 → RAG → AI Agent → MCP → 後端）
- Papaya 中文系列：YouTube（英文不習慣的入門）
- n8n 官網：n8n.io（可自架，Community Edition 免費）

---

## 對比參考

- [[claude-routines-automation]] — Claude Code 做自動化的方式
- [[gmail-automation]] — 派哥的 Gmail GAS 方案
- [[openclaw-hermes-collaboration]] — OpenClaw + Hermes 分工
