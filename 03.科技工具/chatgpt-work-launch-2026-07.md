---
tags: [openai, chatgpt, codex, ai-agent, claude-comparison, mcp, skills]
source: 派哥貼文轉貼（無原始連結，附推特連結 x.com/OpenAIDevs/status/2075275868268789885）
date: 2026-07-11
category: 03.科技工具
related: codex-plugins-openai
---

# OpenAI 推出 ChatGPT Work：把 ChatGPT 變成能真正做事的夥伴

> **一句話**：Codex（OpenAI的coding agent）併入ChatGPT桌面版，網頁版新增「Work」對話模式，能呼叫skill+MCP工具、長時間自主跑多步驟任務、產出可分享的互動網站——本質上是OpenAI在追平Claude Code這一年多來已經在做的事。

## ChatGPT Work 是什麼

ChatGPT 裡新增的 agent，內建 **Codex** 技術，由新模型 **GPT-5.6** 驅動。能跨 app/檔案採取行動，複雜專案可連續處理好幾個小時，把目標拆成小步驟獨立完成，產出試算表/簡報/文件/網頁應用等完整成品，不只是回答問題。

Codex 目前每週 500萬人用，其中 100萬人用在非開發工作上。Codex 底下三個模型：**Sol**（需要細節打磨的任務）、**Terra**（日常主力）、**Luna**（明確可重複的工作）。

## 核心功能拆解

| 功能 | 說明 |
|------|------|
| **Plugins** | 接 Slack/Teams/Google Drive/SharePoint/email/行事曆/CRM/專案追蹤工具。ChatGPT自動判斷該用哪個，或打「@」指定app。統一plugins目錄，對話中會主動建議相關plugin |
| **Skills** | Work模式下可對話直接呼叫skill+對接工具(MCP)，之前的chat模式不支援skill。可上傳skill zip/md檔案（派哥貼文原文提到：作者實測把Claude的skill檔案上傳到ChatGPT Work也能成功） |
| **Sites**（公開測試版） | 把工作/構想變成可互動網站/網頁app，一個網址分享。適合即時dashboard、專案追蹤器、原型、互動式報告。底層資訊變動時自動更新 |
| **Scheduled Tasks** | 執行一次/按排程重複/事件觸發/持續監控。例：每週整理Slack動態、每天檢查dashboard產出摘要、監控顧客回饋轉優先順序清單 |
| **桌面版內建瀏覽器** | 研究市場、比對來源、直接編輯Google Workspace/Microsoft 365檔案 |
| **Computer Use** | 代替操作電腦：點擊、輸入文字、搬移檔案，可單次執行或設成Scheduled Task的一部分 |

Codex app 已併入全新 ChatGPT 桌面版：diff裡行內編輯、側邊欄審查PR、GPT-5.6加速的Computer Use、同專案支援多repo。原桌面版改名 **ChatGPT Classic**。Chrome擴充功能同步更新可在側邊欄用。**Atlas瀏覽器將逐步淘汰**，導流到ChatGPT。

## 實測案例（數字）

| 公司 | 用途 | 成果 |
|------|------|------|
| Zapier | 每月審查數千筆銷售線索，自動產出高層dashboard | 挖出**七位數**潛在銷售額 |
| RingCentral | 每月產品上線檢查自動化 | 從支援1位PM → 支援約**50位**PM |
| Virgin Atlantic | 五年計畫的競品乘客體驗比較 | 數週分析壓縮到**數小時** |
| NVIDIA | GTC大會準備流程自動化 | 取代原本吃掉**40%**會前準備時間的Excel工作流 |
| OpenAI內部業務團隊 | 探索性對話轉PoC | 原本數週 → **24小時** |
| OpenAI內部財務團隊 | 月底結帳與預測 | 數天 → 數小時 |

## 安全與治理

- 建立在ChatGPT Enterprise既有安全/隱私/合規基礎上，管理員可管存取權限、內部資料使用、工具連接、可執行動作
- **Compliance API**：大規模檢視對話與動作，支援企業監督
- **Auto-review**：重要動作真正執行前，用最先進模型先審查，避免敏感資訊未經授權外流。紅隊測試中**擋下100%試圖萃取受保護資料的攻擊**（含訓練階段沒見過的攻擊手法）

## 上線時間與價格

- 網頁/手機版：今天起優先開放Pro/Enterprise/Edu，接下來擴大到Plus/Business
- 桌面版：今天起全球開放下載（Mac/Windows），**所有方案含免費方案**都能用Chat/Work/Codex三種模式
- 用量計算跟Codex相同結構，任務越複雜耗額度越多；Enterprise/Edu管理員可在Admin Console設支出控制

## 對應 Claude 是什麼？（派哥問，這段是我自己的分析，不是Gemini摘要出來的）

這篇文章講的，其實就是 OpenAI 在追平 **Claude Code 這一年多來已經在做的事**。逐項對照：

| ChatGPT Work 功能 | Claude 對應物 | 派哥你現在的實際狀況 |
|---|---|---|
| ChatGPT Work agent（Codex驅動） | **Claude Code**（我） | 你整個session都在用，長時間跑多步驟任務就是我今天在做的（cc_processor debug、save-sop流程優化） |
| Plugins（接Slack/Drive/CRM等） | **MCP (Model Context Protocol)** | 你已經接了 Gmail MCP、Google Drive MCP、Notion、Telegram plugin、bank-sqlite 等，概念完全一樣，Claude其實是MCP標準的原創者 |
| Skills（上傳skill md/zip、對話呼叫） | **Claude Skills** | 你今天一路在用的 save-sop、cangjie-skill、fubon-stock-update 全部都是這個東西，Claude Skills比ChatGPT早很多 |
| Sites（產出可分享互動網站） | **Artifact 工具** | 我可以直接發布HTML/Markdown成一個網址給你分享，同樣概念 |
| Scheduled Tasks | **launchd cron + CronCreate** | 你的 cc_processor 每天08:35自動跑、FirstTrade/Fubon更新排程，本質上就是這個 |
| 桌面版瀏覽器 | **claude-in-chrome** | 我能直接操作你的Chrome瀏覽器 |
| Computer Use | Claude的電腦操作能力 | 概念對應，實作方式不同 |
| Auto-review安全審查 | Claude Code的**hooks機制** | 你今天才剛裝的Stop hook（強制檢查reply tool有沒有呼叫）就是同一種「動作執行前先審查」的精神，只是換成你自己客製規則 |

**結論**：OpenAI 這次發布不是全新概念，是把 ChatGPT 整合成跟 Claude Code 的工作模式（agent+MCP+skill+排程+瀏覽器操作）越來越像的產品。派哥你今天做的所有事——存筆記、修cc_processor bug、裝Stop hook、遠端教朋友裝Claude Code——本質上就是「Claude Work」已經在跑的實例，只是沒有取這個行銷名字。

## 對派哥的參考價值

- 跟已存的 [[codex-plugins-openai]]（Codex plugin生態、173個插件）是同系列，那篇講的是Codex CLI本身的plugin系統，這篇講的是Codex技術被包進消費級/企業級的ChatGPT Work產品——同一個Codex技術兩種產品形態
- 「上傳Claude skill檔案到ChatGPT Work也成功」這件事值得留意：如果skill格式真的能跨平台通用，你寫的skill（save-sop、cc_processor相關）以後可能不只能在Claude Code用，值得之後找時間實測驗證
- Auto-review「100%擋下紅隊測試攻擊」這個數字要謹慎看待——這是OpenAI自己公布的行銷數字，沒有第三方驗證細節，跟你一貫「驗證才回報」的原則放在一起看會更有警覺心
