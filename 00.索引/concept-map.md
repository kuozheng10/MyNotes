# 概念地圖

> 自動生成，上次更新：2026-04-06
> 用途：一眼看清知識庫的主題群、筆記間的關聯

---

## 群組 1：Claude Code 使用技巧
> 怎麼用 Claude Code 更好、更快、更省錢

| 筆記 | 核心概念 |
|------|----------|
| [[boris-15-claude-code-tips]] | 15 個高頻技巧：手機寫 code、worktree、hooks |
| [[claude-code-source-leak-insights]] | 原始碼洩露 → 95% 是 harness，真正理解架構 |
| [[claude-hidden-combo]] | 零程式碼自動化：瀏覽器 + 排程 + Memory |
| [[claude-code-computer-use]] | 直控 Mac GUI，native app 測試 |
| [[agent-prompt-token-cost]] | 中文 prompt 省 token 40% 技法 |
| [[openmemory-auto-manager]] | Claude/Gemini/Codex 三工具共用記憶庫 |

---

## 群組 2：開發方法論
> 怎麼讓 AI 開發更有紀律、更少 bug

| 筆記 | 核心概念 |
|------|----------|
| [[ai-coding-shift-left]] | 壓力左移：spec_as_code → test_as_code → review |
| [[SDD-vs-SBE]] | SBE 講溝通，SDD 講執行；solo dev + AI 用 SDD |
| [[claude-code-feature-workflow]] | Feature 開發 SOP：Brainstorm → Plan → Impl → Review |
| [[bugfix-8steps-workflow]] | Bug Fix 8 步：先有證據再動手 |
| [[exploratory-testing-sbtm]] | ET + SBTM：比自動化腳本更快找 bug |
| [[dual-agent-dev-loop]] | 雙 AI 迴圈：一個寫、一個測、Notion 協調 |

---

## 群組 3：UI / 設計 Skills
> 讓 AI 做的 UI 不要有「AI 味」

| 筆記 | 核心概念 |
|------|----------|
| [[ui-ux-pro-max-skill]] | 161 條規則，自動產出設計系統 |
| [[impeccable-design-skill]] | 20 個指令各個擊破 AI 設計味 |
| [[web-design-guidelines-skill]] | Vercel Labs 官方 WCAG 合規審查 |

---

## 群組 4：自建工具 / 專案
> 派哥親自動手建的東西，有文件可查

| 筆記 | 核心概念 |
|------|----------|
| [[my-wallet-trip-setup]] | 旅遊記帳 PWA：Next.js + Gemini OCR + Notion |
| [[gmail-automation]] | Gmail 自動分類：5 label，每日 2 次 |
| [[gmail-automation-spec]] | Gmail v2.0 完整規格書 |

---

## 群組 5：AI 工具 / 開源套件
> 別人建的工具，值得注意或可能用上

| 筆記 | 核心概念 |
|------|----------|
| [[gstack-claude-skills]] | Garry Tan 的虛擬工程團隊（62K stars） |
| [[codex-plugin-cc]] | OpenAI Codex 把關 Claude 輸出 |
| [[MiniMax-AI-skills]] | 14 個 skills 模組，生產級開發指南 |
| [[expo-skills-plugin]] | Expo 官方 React Native Skills |
| [[opendataloader-pdf]] | PDF → Markdown，表格準確率 0.93 |
| [[CodexBar]] | macOS menu bar AI 用量監控 |
| [[vibevoice-microsoft]] | Microsoft 語音 AI，60 分鐘音訊 + 說話人辨識 |
| [[japan-receipt-tracker]] | 日本旅行記帳 App 架構參考 |
| [[llm-knowledge-base-karpathy]] | Karpathy 知識庫 4 層架構 |

---

## 群組 6：點數 / 金融 / 旅遊
> 哩程、信用卡、旅行相關

| 筆記 | 核心概念 |
|------|----------|
| [[tripplus-快訊260401-信用卡哩程新聞]] | Amex、X Debit、星宇、阿拉斯加哩程新聞 |

---

## 概念連結圖

```
知識庫架構 ──────────── llm-knowledge-base-karpathy
                              ↑ 啟發
記憶系統 ←── openmemory-auto-manager
         ←── claude-hidden-combo

開發方法論：
ai-coding-shift-left
    └── spec_as_code → SDD-vs-SBE
    └── test_as_code → bugfix-8steps-workflow
                           └── exploratory-testing-sbtm

Claude Code 效率：
boris-15-claude-code-tips
    └── hooks → claude-code-feature-workflow
    └── worktree → dual-agent-dev-loop

UI 設計鏈：
ui-ux-pro-max-skill → impeccable-design-skill → web-design-guidelines-skill
（設計系統）        （消除 AI 味）             （合規審查）
```
