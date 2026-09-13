---
tags: [microsoft365, copilot, office, productivity, workplace]
source: Gemini API + Google Search grounding 整理，2026-07-26
date: 2026-07-26
related: esor-workflow-chaos-copilot-teaser-2026-07
---

# Copilot in Office 職場實戰指南

> 派哥丟了一支FB短片想找Copilot實戰教法，結果那支是預告片沒有實質內容（見[[esor-workflow-chaos-copilot-teaser-2026-07]]）。這篇改用Gemini搜尋整理出真正的操作技巧，補上這塊。

---

## 各應用程式最實用的功能

### Word
- **寫草稿**：輸入主題/需求提示，直接生成段落草稿，附語氣風格調整選項
- **摘要+潤稿**：長文件自動抓重點；選取文字後可要求強化、改寫、調整語氣
- **限制**：對表格和圖表的支援目前還有限

### Excel
- **不用會公式**：指令欄直接輸入分析需求（例如「檢查資料中的極端值」「預測銷售趨勢」），Copilot自己生成公式、跑計算
- **建圖表/樞紐分析表**：文字指令直接生成，例如「建立類別的長條圖」
- **⚠️ 前提**：必須開啟「自動儲存」，檔案要存在OneDrive，沒存檔的檔案用不了Copilot

### PowerPoint
- **從文字/Word文件直接生成整份簡報**：選「建立簡報」，貼主題或丟一份Word文件進去，自動生成含演講者備忘稿的完整簡報
- **事後調整**：「調整第三頁版面更視覺化」「幫全部投影片加統一動畫」這種指令都可以

### Outlook
- **一鍵摘要長信串**：讀取窗格上方按「由Copilot摘要」
- **草擬回信**：根據信件內容+附件生成回覆草稿，可調語氣調長短
- **收件匣分類**：休假回來可以問「幫我檢查今天有哪些重要郵件」，自動標出最緊急的

### Teams
- **會議即時摘要**：開會中隨時可以問「摘要目前討論內容」，遲到者秒懂進度
- **會議結束自動產會議記錄**：含決策、行動項目，自動寄給與會者，行動項目還會直接建成Outlook任務指派給負責人

---

## 四個具體職場情境範例

1. **寫報告**：「請幫我寫一份2026年Q1行銷活動回顧報告，包含三大活動成效、參與人數與後續建議」→ Copilot會抓公司現有相關文件/數據生成初稿
2. **整理跨部門會議記錄**：會議中/後要求「摘要本次重點和決策」+「列出所有行動項目及負責人」
3. **趕簡報**：手上已有Word文件時，直接「根據這份Word文件建立10頁發表簡報，含亮點/市場分析/競爭優勢/未來展望，附演講者備忘稿」
4. **處理客戶長信**：先「摘要」抓重點，再「根據這封信的內容和附件，草擬專業回覆逐一回答客戶問題」

---

## 限制與常見誤區（這段最重要，不要跳過）

- **Copilot是副駕駛不是自動駕駛**：生成內容一定要人工審核校對，尤其對外溝通/正式文件，AI可能講錯或語氣不對
- **提示詞品質決定結果品質**：模糊指令出爛結果，要講清楚內容/格式/語氣/風格，最好給具體範例
- **繁體中文效果不如英文**：Copilot支援48種語言，但官方優化的是簡體中文等幾個語言，繁中效果目前有落差
- **只能存取你原本就有權限的資料**：權限設定不對，Copilot就是看不到那份文件，不會繞過權限
- **不是所有訂閱都有完整功能**：個人/家庭版可能有但限量(AI點數制)，企業級訂閱才是完整無限制
- **資料不會被拿去訓練模型**：微軟承諾客戶資料不進AI訓練集，建立在M365既有的身份/存取控管+零信任原則上

---

## 對派哥的意義

派哥自己是Claude Code重度使用者，這套「摘要→草擬→人工校對」的三段式工作模式，跟派哥平常用Claude Code處理email/PDF/報表的邏輯完全一致，只是這篇是Office生態系的對應版本。如果要教朋友/同事在公司善用Copilot，上面「四個具體情境」可以直接當現成的話術範本教人下指令，「限制與常見誤區」那段是最容易被忽略但最重要的——尤其「提示詞品質決定結果品質」跟派哥自己「先問清楚情境再讓AI動手」的習慣是同一個道理。

---

## 晨間 Triage SOP：一進公司怎麼用 Copilot 整理 Teams / Outlook / 簽核清單（2026-09-13補）

> 派哥丟了一支 FB 短片（Tenten - Product Agency 的「Copilot Cowork」廣告），影片本身是行銷demo（老闆丟舊簡報→換版本/濃縮成10頁→順便把該回的客戶信草稿也做好），不是實際操作教學，而且影片是Reel格式讀不到完整逐格畫面（已知限制，Reel影片頁面會卡在一直緩衝）。以下改用官方文件+社群教學整理出真的能照做的步驟。

### 目標：一進辦公室，三件事自動有清單可看
1. Outlook 該回的信，依重要性排好序，甚至草稿都先擬好
2. Teams 昨晚到現在的未讀訊息/會議，有摘要不用逐則翻
3. 有哪些簽核（Approval）在等你，一目瞭然

### Part 1 — Outlook「該回覆清單」：排程一個每天早上自動跑的 Copilot prompt

這是核心，一次設定，之後每天早上都有一份現成清單，不用手動再問。

**步驟：**
1. 開 **Copilot Chat**：三個地方都可以，挑你最常開的——
   - 網頁：`https://m365.cloud.microsoft/chat`
   - Outlook 網頁版/桌面版右上角的 Copilot 圖示
   - Teams 左側 sidebar 的 Copilot Chat
2. 用工作帳號（公司帳號）登入，**前提是公司有幫你開 Microsoft 365 Copilot 授權**，沒有的話這功能整套用不了，要先跟IT/主管確認
3. 在對話框輸入這句（英文效果比中文好，直接照抄）：
   ```
   Summarize my unread emails from the past 7 days. Prioritize them from 1–5 based on importance. Draft replies for any rated 4 or 5.
   ```
4. Copilot 回覆出來後，把滑鼠移到**這則回覆**上面，會出現 **「Schedule this prompt」** 的選項，點下去
5. 設定排程參數：
   - 開始日期/時間：例如「每天早上 8:00」（建議設在你實際會進辦公室之前10-15分鐘，讓它跑完）
   - 重複頻率：Daily 或只挑平日
   - 執行次數上限：系統預設會讓你設，最多可以連續跑到系統上限（不用一直手動重設）
   - 「Email notification」：建議打開，這樣跑完會寄信通知你，不用自己開 Copilot 才知道好了沒
6. 按 **Save**
7. **之後怎麼看結果**：打開 Copilot 視窗，左側「Conversations」清單裡，排程產生的對話會**用粗體+一個小圖示**標出來，點進去就是當天的摘要
8. **管理所有排程**：Copilot 視窗右上角「**…**」設定選單 → **Scheduled prompts**，可以看到/編輯/刪除所有排程（一個帳號最多可以建 **10 個**不同的排程 prompt）

**進階變化版**（同樣排程法，可以另外多排一個）：
```
Summarize today's tasks, meetings, and emails.
```
這句是「今日總覽版」，比較像晨報，跟上面那句「該回信件排序」互補，兩個都排也不衝突（沒超過10個上限就好）。

### Part 2 — Teams「未讀訊息/會議」摘要：不用排程，隨手問就好

Teams 這邊 Copilot 目前沒有像 Outlook 那種「排程自動生成摘要」的固定功能（查了官方文件跟教學都沒提到），但可以做到「一進公司主動問一句話就有摘要」：

**未讀聊天訊息：**
- 打開 Teams 左側 Copilot Chat（或任一聊天視窗右上角 Copilot 圖示）
- 輸入：`Summarize messages from [某人/某群組] over the past two weeks. Call out any important details, like deliverables, due dates, and action items for me.`
- 把 `[某人/某群組]` 換成實際名字，或問全部：`Summarize my recent unread messages.`

**昨天/上週開的會（如果有錄影+轉錄）：**
- 進到該場會議的聊天串
- 右上角點 **Copilot 圖示**（或如果會議有開轉錄，該會議聊天室裡會多一個 **Recap** 分頁，點進去也看得到 Copilot 摘要）
- 輸入 `Recap [會議名稱]`，或直接問 `這場會議討論了什麼重點跟決議？`
- ⚠️ 前提：會議當時要有開「轉錄」（Transcription）功能，沒開轉錄=Copilot事後看不到內容，這個要跟主辦會議的人提醒開

### Part 3 — Approvals（簽核）待辦清單：這個跟 Copilot 無關，是 Teams 內建功能

查了一輪，Approvals app 目前**沒有**跟 Copilot 整合出「AI摘要簽核清單」這種功能，但 Teams 原生就有現成清單可以看，設定一次之後每天點開就好：

**第一次設定（釘選到側邊欄，方便每天點）：**
1. Teams 左側 sidebar 最下面點 **「…」(More apps)**
2. 搜尋 **Approvals**，點開
3. 右鍵這個 app 圖示 → **Pin**，之後它就常駐在左側 sidebar，不用每次重新搜尋

**每天早上打開看什麼：**
- 點進 Approvals app，切到 **「Received」分頁** —— 這裡就是**別人送給你、等你簽核的清單**，一目瞭然（跟「Sent」分頁分開，Sent是你送出去等別人簽的，不用看那個）

### 小結：一進辦公室的實際動作

| 要看什麼 | 怎麼看 | 要不要事先設定 |
|---|---|---|
| 該回的信 + 草稿 | 開 Copilot Chat → 看排程好的那則對話 | ✅ 排程一次，之後自動跑 |
| 今日總覽（信/會議/任務） | 同上，另排一個 prompt | ✅ 排程一次 |
| Teams 未讀訊息摘要 | Copilot Chat 打一句話問 | ❌ 沒有排程功能，每天手動問一句 |
| 昨天開的會摘要 | 進會議聊天室看 Recap 分頁 | ⚠️ 開會當下要記得開轉錄 |
| 待簽核清單 | Approvals app（先釘選）→ Received 分頁 | ✅ 釘選一次，之後常駐 |

**Sources：**
- [Catch up on work quickly using Microsoft 365 Copilot Chat](https://support.microsoft.com/en-us/microsoft-365-copilot/catch-up-on-work-quickly-using-microsoft-365-copilot-chat)
- [Catch up on meetings with Microsoft Copilot in Teams](https://support.microsoft.com/en-us/teams/copilot/catch-up-on-meetings-with-microsoft-365-copilot-in-teams)
- [Schedule your most used Copilot prompts](https://support.microsoft.com/en-us/topic/schedule-copilot-prompts-29dfd5fb-211a-4515-88a6-730b8074e489)
- [Manage Scheduled Prompts for Microsoft Copilot - Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-365/copilot/scheduled-prompts)
- [Copilot Daily Prompts: Automate Outlook and Teams](https://databear.com/copilot-daily-prompts/)
- [What is Approvals? - Microsoft Support](https://support.microsoft.com/en-us/office/what-is-approvals-a9a01c95-e0bf-4d20-9ada-f7be3fc283d3)

## 相關筆記
- [[esor-workflow-chaos-copilot-teaser-2026-07]] — 原本想找這篇的Copilot教學結果是預告片，這篇補上真正的操作內容
