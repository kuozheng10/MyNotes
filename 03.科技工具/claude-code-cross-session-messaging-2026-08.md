---
tags: [claude-code, cross-session-messaging, sendmessage, listagents, multi-window, anthropic]
source: [Facebook - 張維峰](https://www.facebook.com/share/v/1BTipNFoE8/?mibextid=wwXIfr) + [官方文件](https://code.claude.com/docs/en/cross-session-messaging)
date: 2026-08-08
---

# Claude Code 跨會話訊息（Cross-Session Messaging）

> **一句話**：同一台電腦開兩個 Claude Code 視窗，一個做完事可以自己傳一句話通知另一個，不用你自己複製貼上。

---

## 是什麼問題

以前同時開兩個 Claude Code 視窗做不同的事（例如一個改資料庫、一個改網站），它們彼此不知道對方進度。現在其中一個可以直接傳一句話給另一個——左邊改完資料庫欄位名稱，可以自動跟右邊說「資料庫改好了，欄位名稱換成 tenant_id」，不用你手動搬過去講。

底層機制：Claude 用 `ListAgents` 找出能傳訊息的對象，用 `SendMessage` 把訊息送過去。同一組工具也用在單一 session 內跟 subagent／agent team 隊友溝通，但這篇專講「兩個獨立 session 之間」的用法。

---

## 開啟條件（不用手動設定，滿足以下就自動開）

| 條件 | 說明 |
|------|------|
| Claude Code 版本 | 2.1.224 以上（`claude --version` 查） |
| 作業系統 | Mac 或 Linux（**Windows 原生不支援**，WSL2 上的 Linux 可以） |
| 帳號類型 | 一般 Claude 帳號；**不支援** AWS Bedrock、Google Cloud Agent Platform、Microsoft Foundry 等企業版通道 |
| 環境變數 | 若設了 `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`、`DISABLE_TELEMETRY`、`DO_NOT_TRACK`、`DISABLE_GROWTHBOOK` 任一個，功能會被關掉，需要的話要取消設定 |

**確認方式**：Claude Code 裡打 `/list-agents`（別名 `/peers`）。
- 有反應（列出視窗清單）→ 支援
- 回「不認得這個指令」→ 這台不符合條件，先查版本、再查是不是 Windows

---

## 基本用法

不用學新指令，正常講話即可：

- 「幫我問另一個視窗那邊，資料轉檔跑完了沒」
- 「把我們剛剛改的東西跟正在做網站那邊的 Claude 說一聲」

Claude 自己判斷要傳給誰、自己決定內容怎麼寫。**Claude 也會自己主動判斷有必要時就傳，不用你開口**。

### 訊息什麼時候會被讀到

- 對方閒著：訊息一到馬上處理
- 對方忙著：訊息排隊，等對方現在這個動作做完的空檔才讀（**不會打斷正在跑的 tool call**）
- 送達後算用量，跟你自己打一句話一樣

---

## 安全設計（官方文件補充細節）

- **不能代替你按同意**：另一個 session 傳來的訊息不算你本人授權，該問的權限還是會問你
- **不能改設定**：不會因為對方訊息內容就去動權限設定或 CLAUDE.md
- **訊息裡的指令不會執行**：就算內容寫了 `/compact`，對方只當純文字看，不會真的跑
- **只傳一句話，不傳對話記錄或檔案**：想搬整段對話去另一個視窗接著做，要用 `--continue`／`--resume`，不是這個功能
- **權限邊界各自獨立**：Claude 被要求絕不會因為另一個 session 說了什麼，就去做自己這邊被拒絕/擋掉的動作，會退回來問你

---

## 跨電腦使用：只能單向

| 對方在哪 | 訊息怎麼走 | 你這邊能做什麼 |
|---------|-----------|---------------|
| 同一台電腦 | 走本機 per-session socket，不經過網路/Anthropic伺服器 | 可以主動傳、也可以回覆 |
| 你的另一台電腦 | 經過 Anthropic 伺服器，透過對方的 Remote Control 連線送達 | **只能回覆**，不能主動先開頭 |
| Claude Code on the web（雲端版）| 經過 Anthropic 伺服器直達雲端 session | **只能回覆** |

跨電腦要用，對方那台需要開著 **Remote Control**（手機/其他裝置遙控 Claude Code 的功能）。回覆需要「回覆地址」，如果回覆的那個 session 沒連 Remote Control，訊息會送出去但沒有回覆地址，對方沒辦法再回你。

想強制「任何訊息離開這台電腦前都要你同意」，設定檔加：
```json
{ "isolatePeerMachines": true }
```

---

## 三種自訂收訊模式（`crossSessionInbound`）

在設定檔設定：

| 值 | 行為 |
|----|------|
| `accept` | 直接收，不問 |
| `hold` | 每則跳通知詢問，**5分鐘未回應自動丟棄**；approve才會真的送進去 |
| `refuse` | 直接丟棄，不通知 |

```json
{ "crossSessionInbound": "refuse" }
```

**沒特別設定時的預設邏輯**：依雙方 session 的權限模式（bypass permission prompts vs 一般跳權限詢問）分兩類——
- 收訊方是「一般會跳權限詢問」的 session → 預設直接收；只有當**發送方**是 bypass 模式時才會 hold 起來問你
- 收訊方本身是 bypass 模式 → 預設每則都 hold 問你；只有發送方也是 bypass 模式才直接收

**完全不想被傳/也不想傳出去**：在權限設定的 deny 清單加 `SendMessage` 跟 `ListAgents`（兩個工具都要加，只填工具名不用參數）。組織管理者也能在 managed settings 統一關閉全體。

---

## 名字辨識與撞名

- Session 預設名字取自資料夾名稱（如 `myapp-3f`），容易撞名
- 想自己取名：`/rename` 指令，取一個好認的名字（例如「資料庫」「網站」），之後叫 Claude 傳訊息時比較好指定對象
- `/list-agents` 輸出會顯示各 session 的工作目錄，撞名時可以靠這個分辨，Claude 自己內部也會加短ID來區分

---

## 常見問題排查

| 現象 | 原因 |
|------|------|
| `/list-agents` 說不認得這個指令 | 不符合前面的版本/作業系統/帳號條件，或環境變數關掉了功能 |
| `/list-agents` 看得到對方，但訊息傳過去沒反應 | 功能本身是好的，卡在別處：可能對方設成 hold/refuse、或對方在另一台機器上（那邊只能回不能收新訊息）|
| 清單裡兩個 session 名字一樣 | 撞名，用 `/rename` 自己取名 |

---

## 技術限制

- **只能傳純文字**：Agent Team 內部的結構化協定訊息不會外流到跨 session 通道
- **訊息迴圈會被節流**：Claude Code 會對同一發送者的重複訊息限流，短時間內完全相同的重複訊息會被丟棄，待讀訊息上限每 session 50 則，防止兩個 session 互傳造成無窮迴圈
- **Headless (`claude -p`) session**：正常模式下能收訊息；用 `--bare` 模式啟動的不會綁定 inbox socket，收不到也不會出現在名單裡。要讓無人值守的 `-p` worker 能收訊息，要在它的 `--settings` 裡把 `crossSessionInbound` 設成 `accept`

---

## 對派哥的意義

這個功能跟目前用的 Agent/fork 機制不太一樣——`SendMessage`/`ListAgents` 是給**手動開的、彼此獨立的多個 Claude Code 視窗**互通消息用的，不是自動化 pipeline（cc_processor/investment 排程那些）會用到的東西。適合的場景：如果派哥同時開好幾個終端機視窗，一個在改程式、一個在跑很久的資料處理，需要跨視窗互相通知進度時可以用；跟現在這種單一 TG 對話 session 裡處理任務的模式是不同的使用情境。

官方文件：https://code.claude.com/docs/en/cross-session-messaging
