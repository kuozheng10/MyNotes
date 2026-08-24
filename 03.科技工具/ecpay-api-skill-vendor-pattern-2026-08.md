---
tags: [ai-coding, claude-code, skill, api, ecpay, vendor, github, taiwan]
source: arthurlai (Threads分享)，https://www.threads.com/share/_wXZXBZjG/ ／ 專案：https://github.com/ECPay/ecpay-api-skill
date: 2026-08-24
related: agent-skill-eval-best-practices-2026-07, anthropic-skill-three-layers-2026-06, public-api-curation-taiwan
---

# ECPay API Skill：金流廠商「出Skill取代出文件」的新模式

> **Threads熱議金句**（mazdashie）：「AI的新商業模式出現了，金流廠商不再需要出文件、範例程式。出skill讓用戶自己去訂閱AI付token錢」
> （foodietravelbike）：「這絕對是未來串api的方向：以前出文件，現在出skill」

---

## 這是什麼

綠界科技（ECPay）官方發布的 API 整合知識套件，不是傳統 API 文件，而是一組給 AI 開發助手讀的 Markdown 檔案（入口 `SKILL.md`）。安裝後，開發者用中文描述需求，AI 直接生成可用的串接程式碼，不用自己翻官方文件。

## 支援的 AI 工具（一套內容，七個入口檔案適配不同平台）

| 平台 | 安裝方式 | 入口檔案 |
|------|---------|---------|
| Claude Code | `git clone` 到 `~/.claude/skills/ecpay` | SKILL.md |
| VS Code Copilot Chat | 下載ZIP解壓縮 | `.github/copilot-instructions.md` |
| Visual Studio 2026 | Clone + Custom Instructions | `.github/copilot-instructions.md` |
| GitHub Copilot CLI | Clone後自動讀取 | `.github/copilot-instructions.md` |
| Cursor | Clone → 引用 | AGENTS.md |
| OpenAI Codex CLI | 讀取 | AGENTS.md |
| Google Gemini CLI | 讀取 | GEMINI.md |

```bash
# Claude Code 全域安裝
git clone https://github.com/ECPay/ECPay-API-Skill.git ~/.claude/skills/ecpay

# 驗證安裝：問AI「綠界AIO金流的測試MerchantID是多少？」，答案是 3002607 就成功
```

## 知識庫規模

- 29 份整合指南（金流/發票/收據/物流/ECTicket）
- 134 個官方驗證 PHP 範例
- 12 種語言加密實作自動翻譯（Python/Node.js/TS/Go/Java/C#/Kotlin/Ruby/Rust/Swift/C/C++）
- 443 個 API 即時規格 URL 索引（產生程式碼前 AI 會即時去讀最新規格，不是背過時文件）
- 25 組跨語言加密測試向量（CheckMacValue×8、AES-CBC×9、AES-GCM×4、URL Encode×4），每次發布前CI全跑一遍才放行
- 6 個 Claude Code 快速指令（`/ecpay-pay`、`/ecpay-invoice`、`/ecpay-debug`）

## 跟傳統 API 文件的差異

| 項目 | 傳統文件 | ECPay Skill |
|------|---------|-------------|
| 入門門檻 | 高，要理解複雜規格 | 低，中文描述需求即可 |
| 跨語言支援 | 通常只有PHP範例 | 12種語言自動翻譯 |
| 即時性 | 文件可能過時 | AI即時讀取官網最新規格 |
| 加密實作 | 自己刻，容易出錯 | 25組測試向量持續驗證 |
| 除錯 | 自己土法煉鋼 | AI協助分析CheckMacValue/AES錯誤 |

**安全性**：Skill本身不收集資料、不連第三方伺服器，金鑰完全由開發者自行管理；架構基於綠界官方PHP SDK。

**授權限制**：All Rights Reserved，僅供檢視/研讀/搭配AI編程助手參考，禁止重新散布或商業轉售。

## 對派哥的意義

- 這是「廠商出Skill取代出文件」的具體範例，跟派哥自己維護的一整套 `~/.claude/skills/` 是同一個模式的兩端：派哥是**用skill組織自己的工作流程**，ECPay是**用skill當作對外產品介面**——如果派哥之後有專案要接綠界金流/物流/發票，這個skill可以直接clone進專案用，不用自己翻文件
- 跟 [[agent-skill-eval-best-practices-2026-07]] 呼應的地方：ECPay這套用「25組加密測試向量CI跑過才發布」實踐了「skill也要有eval」的原則，是少見真的把這條原則做出來的商業案例
- 跟 [[public-api-curation-taiwan]]（派哥的台灣Public API清單）性質不同但互補：那份是「免費開放API清單」，這個是「付費金流服務但用skill取代文件」——如果之後要更新那份清單，可以把「廠商出skill而非純文件」列成篩選/推薦的加分項

---

## 相關筆記

- [[agent-skill-eval-best-practices-2026-07]] — Skill也要寫測試/eval的最佳實踐（Google DeepMind），ECPay這套是實踐範例
- [[anthropic-skill-three-layers-2026-06]] — Anthropic官方Skill三層架構設計原則
- [[public-api-curation-taiwan]] — 派哥的台灣Public API精選清單
