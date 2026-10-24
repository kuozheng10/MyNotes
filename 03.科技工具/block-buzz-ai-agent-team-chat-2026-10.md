---
title: Buzz：讓多個 AI 員工在同一個群組分工交接（Block 開源）
tags: [AI-agent, multi-agent, Buzz, Block, Nostr, Claude-Code, Codex, 自架, Hostinger]
date: 2026-10-24
category: 03.科技工具
source: https://youtu.be/kNSHESEOwRw
author: Apple Mei（YouTube，2026-10-17，17 分鐘，Hostinger 業配）
---

> 派哥丟 YouTube 連結說「研究一下」。影片內容由 Gemini 看影片整理；Buzz 背景由 Gemini 搜尋查證（2026-10-24）。

## Buzz 是什麼

- **Block**（Jack Dorsey 的公司）2026-07-21 推出，**Apache-2.0 開源**，`github.com/block/buzz`
- 長得像 Discord／LINE 群組：**真人跟好幾個 AI 在同一個群組裡**，分頻道工作（選題、腳本、業配、行政…），對話跟檔案都留在該頻道
- AI 會互相 @ 交接：一個做完，下一個自動接手；一個寫稿、一個審稿，不合格就退回重寫
- 底層用 **Nostr** 協定：人跟 AI 各有一把加密身分金鑰，所有訊息、審批、動作都是簽過名的事件紀錄
- 預設三個 AI：Fizz（做事）、Honey（寫作）、Pollen／Bumble（研究）
- **可以接 Claude Code、OpenAI Codex、Block 的 Goose**（透過 ACP 橋接），也可以用內建的 Buzz Agent 直接接 OpenAI／Anthropic API
- 免費；成本只有主機費＋模型 API 費

## 影片示範（Apple Mei 的用法）

| 頻道 | 做什麼 |
|---|---|
| 選題 | @Pollen 找 Apple＋AI 新聞挑 5 則，標出「還沒查證」的資訊，再交給 @Honey |
| 腳本 | @Honey 寫 60 秒短影音腳本 → @Pollen 逐句審（數字、來源）→ Honey 改 |
| 業配 | 上傳廠商 brief，@Pollen 逐句審腳本給 PASS／FAIL＋理由 |
| 行政 | @Fizz 查行事曆；寫 email **等她說 OK 才寄** |
| 剪輯 | 上傳影片，AI 整理審片意見成修改清單 |

還有 Canvas 功能：把整理好的重點存成頻道裡的頁面。

### 架設步驟（業配段落 1:54–8:22）

1. Hostinger VPS **KVM 2**：$8.99/月（2 vCPU、8GB RAM、100GB NVMe）；優惠碼 APPLEMEI 打 9 折
2. 下載 Buzz 桌面 App → 建立身分金鑰（私鑰要自己備份）→ 選「Join a community」，複製 public ID
3. Hostinger Docker 管理器 → 一鍵部署 Buzz 模板 → `RELAY_OWNER_PUBKEY` 填 public ID（要用 NostrTool 轉成 64 位 hex），`BUZZ_REQUIRE_RELAY_MEMBERSHIP` 改 `true` → 部署
4. 把容器網址貼回 App → Agents 頁設定預設 provider（OpenAI／Anthropic API key）→ Start 三個 AI
5. 也可以架在自己電腦上（資料都在本機），缺點是關機就停

## 已知缺點（查證）

- 還在 **v0.5 早期**：手機版、推播、完整審批流程發布時都還沒做好
- **很吃 token**：簡單打招呼也燒很多
- AI 可能做到一半卡住，要人去推
- **沒有端對端加密**：主機管理員看得到所有訊息，包含私訊
- 權限很粗：加入的 AI 看得到整個工作區，沒辦法開只給部分 AI 看的私密頻道
- AI 本身如果有開檔案、Shell、瀏覽器權限，Buzz 身分不會幫你限制這些

## 對派哥

派哥現在的架構其實已經是「一群 AI 分工」：Claude Code（TG 主窗口）＋ Codex（實作）＋ Gemini（研究／審查）＋ 一蘭 OpenClaw（排程）。差別是現在由 Claude 居中轉派，Buzz 是把大家放進同一個群組直接互相 @。

| | 評估 |
|---|---|
| 會不會比現在好 | 「寫稿＋審稿互退」這種互審流程很方便；但派哥現在 Claude 寫 → Gemini 審已經在做 |
| 風險 | 要換掉 TG 主窗口就碰到「TG 連線架構不要亂動」的紅線；v0.5 不穩、吃 token、沒加密，財務資料不適合放 |
| 建議 | **先不換**。有興趣的話在本機 Docker 開一個沙盒，接 Claude Code＋Codex 試一個非敏感的流程（例如 save-sop 研究＋審稿），不放帳單、投資資料 |

## 相關筆記

- [[ai-team-os-multi-agent-meeting-2026-06]] — 多 agent 開會／團隊 OS 的另一種做法
- [[claude-code-cross-session-messaging-2026-08]] — Claude Code session 之間互傳訊息
- [[local-agent-mcp-strategy-2026-08]] — 本機 agent 策略
