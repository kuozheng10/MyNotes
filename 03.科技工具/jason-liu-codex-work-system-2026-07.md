# Jason Liu（OpenAI DevEx）用 Codex 打造的個人工作系統

> 來源：張維峰 FB 分享，https://www.facebook.com/share/p/19KGiNWNjQ/?mibextid=wwXIfr
> 儲存日期：2026-07-29
> 標籤：#codex #chatgpt-work #ai-agent #skill #workflow #automation

---

## 核心觀點

Jason Liu（OpenAI DevEx 工程師）：「剩下的唯一工作，就是搞清楚你對某個東西哪裡不滿意，然後把它說出來。」

用 Codex + ChatGPT Work 處理幾乎所有工作，不管程式碼還是生活雜事。

---

## ChatGPT Work vs Codex

兩者本質上是同一個 coding agent 的不同介面：
- **Codex**：顯示 git 歷史、PR、程式碼變更
- **Work**：隱藏這些細節，重新包裝成一般工作者體驗

Jason 主要用 Work，因為不需要審查自己的程式碼。

**模型選擇**：
- 日常瑣事（整理、讀 Slack、排行事曆）→ Sol medium
- 複雜原型（他自己在做的學鼓 app）→ extra high / ultra

---

## Chief of Staff 系統（雙層 scheduled tasks）

- **Daily 版本**：早上 9 點、下午 1 點、下午 5 點各跑一次
- 整合 Slack、Twitter DM、email、Linear board
- 自動處理任務：航班 check-in、傳登機證、提醒領包裹
- 預先草擬回覆信件，等 Jason 微調就發

> 對派哥的類比：跟 [[project_notion_todo|Notion Todo 晨報]] 的概念很像，但 Jason 這套是多來源（Slack/Twitter/email/Linear）彙整 + 主動代辦（不只是提醒，還會先擬好回覆）。

---

## Pinned Thread 工作台

不開幾百個背景 thread，而是用少數幾個 **pinned thread** 當長期工作空間，靠 compaction 機制管理上下文。主要 thread 舉例：
- 紅迪/推特/領英監控
- DevDay 規劃、任務影片製作
- Agents API 思考、鼓練習專案
- 個人專案、投影片製作

---

## Obsidian Vault 當全代理人的上下文起點

所有上下文集中存在一個 Obsidian vault（純 markdown），目錄含 projects、people、notes、daily notes、preferences 等。**所有代理人都從這個 vault 拿上下文**，不是各自散存。

> 這跟派哥自己的 MyNotes（Obsidian）+ Claude Code memory 系統架構理念完全一致，算是外部驗證：集中式 markdown vault 當 agent 記憶層是可行且被業界資深工程師採用的模式。

---

## 寫作 Style 系統（個人 skill repo）

- **Email me skill**、**tweet me skill**
- 語音逐字稿 → blog post 的 skill
- 影片 → video essay 的 skill

「write me」skill 能自動判斷對象（外部使用者/團隊/主管）該用什麼語氣，Codex 自動抓情境切換。

---

## Skill 清理與 Self-Improve Skill

Jason 定期清理沒在用的 skill，並建立 **self-improve skill**：
- 找出被呼叫最多的 skill
- 分析使用者對它的一致性回饋
- 識別重複模式並自動優化（例如自動回覆 Slack 完成通知）

→ 跟派哥的 [[cangjie-skill-distill-2026-07]]（把長內容蒸餾成 skill）、[[lore-skill-implicit-knowledge-2026-06]]（skill 裡藏隱性知識）方向互補：cangjie 講「怎麼生出 skill」，Jason 這套講「skill 生出來之後怎麼持續自我優化、汰弱留強」。

---

## Browser / Computer Use 實戰案例

騎腳踏車時用語音遠端命令 Codex 在 MacBook 上：
- 找到問題影片、修字幕
- 設每 30 分鐘檢查 Slack 回饋、自動 export 新版本
- 20 分鐘內修完一支 launch video

其他：
- 多 tab 購物比較（開 4 個 tab 給 Jason 審完再結帳）
- AirTable 表單自動化（下載 CSV → 跑後續自動化）
- App 測試、OAuth 登入操作

---

## 學鼓 App 案例（長期 Goal 結構）

三檔案系統管理長期專案：
- **goal.md**：成功標準與驗證條件
- **plan.md**：實作細節與技術選擇
- **worklog**：進度紀錄與限制分析

關鍵：Jason 不自己寫 goal，讓 Codex 根據需求自己設定 goal。

---

## 品味與反饋的方法論

品味養成的關鍵是「認真想你不喜歡什麼」：
1. 讓 Codex 先做出東西
2. 辨識自己不滿意的具體地方
3. 用精確語言表達改進需求（例：「需要鍵盤快捷鍵改 tempo」）

這跟寫程式碼的學習方式一樣，只是問題從「怎麼寫」變成「使用體驗為何不好」。

---

## Skill vs Plugin 的定義

- **Skill**：plugin 的組件
- **Plugin**：skill + MCP server + resources 的集合，可分享到 Codex plugin directory

上週 OpenAI 開放使用者提交 plugin：純 skill 的審核快，含 MCP server 的需額外安全審查。

→ 對照 [[codex-plugins-openai]]（官方 173 個 plugin 範例庫）看架構會更完整。

---

## 未來方向

Jason 最期待 Codex 從桌面端擴展到 ChatGPT Work 雲端體驗，讓「工作不因蓋上筆電而停下來」。語音指令是重點方向。

**給普通人的起手式**：從簡單語音指令開始，例如「把這條 thread 變成 heartbeat，我要你在早上9點、下午1點、下午5點檢查 email、Slack、Linear」，隨時間逐步告知偏好，系統持續改進。

---

## 相關筆記

- [[cangjie-skill-distill-2026-07]] — 怎麼把長內容蒸餾成可執行 skill
- [[lore-skill-implicit-knowledge-2026-06]] — skill 裡的隱性知識設計
- [[codex-plugins-openai]] — Codex plugin 官方架構與範例庫
- [[caveman-token-saving-skill-2026-07]] — token 省法 skill 案例
