# Slack 當 Claude Code CLI 介面 — 取代 Claude App/Desktop

tags: #Slack #ClaudeCode #CLI #Automation #工作流程 #遠端操作

> 核心概念：用 Slack 的對話管理 + Mobile App 取代 Claude Desktop App，讓 Claude Code 可以手機遠端操作

---

## 為什麼用 Slack 當 Claude Code 介面？

**Claude App 的限制：**
- Desktop/Mobile App 是 CLI 的閹割版
- 很多 CLI 能做的事，App 做不到
- App 只適合初期釐清需求用

**Slack 的優勢：**
- 對話管理清楚（Channel = 資料夾/專案）
- Mobile App 遠端使用 → 手機操控 Claude Code
- 可實作 Automation → Auto-pilot 模式

---

## 實際用法

### 公司帳號
- 把 feature 規劃好
- 後續讓 Claude Code Auto-pilot 自己跑
- 流程：規劃 → Auto-pilot → Merge → 關 Jira 票

### 個人帳號
- 開一個獨立的 Slack Account
- 將客戶、個人專案分類成不同 Channel
- **每個 Slack Channel 對應到 Claude Code 的不同資料夾**

---

## 效果

- 越來越少開 Cursor/Webstorm（IDE 使用減少）
- 越來越少開 Claude App（Desktop/Mobile）
- Slack + Claude Code CLI = 完整取代 Claude App

---

## 適合誰

✅ 有多個專案/客戶需要分類管理的開發者
✅ 想用手機遠端控制 Claude Code 的人
✅ 已經在用 Slack 的團隊/個人

❌ 只有單一專案、不需要遠端操作的人（CLI 就夠了）

---

## 相關筆記

- [[claude-code-powerup-guide]] — Claude Code 進階使用指南
- [[claude-code-feature-workflow]] — Claude Code Feature 開發流程
- [[iterm2-tmux-claude-workflow]] — iTerm2 + tmux + Claude 工作流程
