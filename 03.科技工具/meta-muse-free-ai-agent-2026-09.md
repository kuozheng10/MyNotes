---
title: Meta Muse——免費的AI私人管家Agent
source: [老狐狸的信用卡日記 FB貼文](https://www.facebook.com/share/p/1EgnpRFSs4/?mibextid=wwXIfr)
tags: [ai-agent, meta, muse, chatgpt-work, grok-bot, claude-comparison]
date: 2026-09-16
category: 科技工具
related: chatgpt-work-launch-2026-07
---

# Meta Muse——免費的AI私人管家Agent

> 起因：派哥丟連結問「你做的到？」——這篇跟已存的 [[chatgpt-work-launch-2026-07]] 是同系列(消費級AI Agent大戰)，這次是Meta的產品。

## 三家消費級AI Agent現況（2026-09）

| 公司 | 產品 | 收費 |
|------|------|------|
| OpenAI | ChatGPT Work | 見 [[chatgpt-work-launch-2026-07]] |
| Grok | Grok Bot | 付費（原PO因此沒用） |
| Meta | **Muse**（本篇主角，上週剛推出） | 免費但有每週用量上限 |

## Meta Muse 是什麼

定位是 **AI私人管家**，偏向「一個AI管你的生活」，不是工作導向的專案工具（跟ChatGPT Work偏工作導向不同）。

**核心能力**：
- 有自己的 **Secure VM + browser**（獨立雲端環境，不佔用你自己的電腦資源）
- 可連 email、calendar、Instagram 等服務
- 能自己上網、填表、購物、處理客服、追蹤長期目標(goals)
- **關掉App後仍會繼續執行任務**（背景持續跑，不需要你的手機/電腦開著）
- 舉例用法：設定它幫你追蹤機票價錢、每天定時查有沒有放出哩程票/點數房
- 若願意給更多帳戶權限，還能幫你寫信給酒店客服等更進階的事

⚠️ **作者提醒**：AI Agent對很多人是新科技，建議先不要給太多權限，避免AI做出你不希望的事。

## 費用與推薦機制

- 免費版有**每週使用上限**，一般人應該夠用
- 不夠用可以用推薦連結：**一個推薦拿10億token，一個帳戶最多10個推薦(共100億token)**
- 下載：https://muse.ai/join （原PO自己的推薦碼是 `ZR5DIC`，用不用自己判斷，不代表派哥背書）

## 網友實測留言（值得注意）

有留言者（廖唯誠）分享：「把Claude上簡單的任務offload在muse上，設定很簡單」——代表已經有人拿Muse當Claude Code的輔助/分流，處理不需要Claude Code那麼強能力的簡單背景任務，省Claude的額度。

## 對應Claude是什麼？（派哥問「你做的到？」，這段是我自己的分析）

逐項對照，誠實講清楚哪些我能做、哪些做不到：

| Muse功能 | 我(Claude Code)能不能做 | 說明 |
|---|---|---|
| 上網瀏覽/填表/操作瀏覽器 | ✅ 能 | claude-in-chrome工具可以直接操作你登入的Chrome，點擊/填表/截圖都行 |
| 連email/calendar | ✅ 能 | 你已經接了Gmail MCP + Google Calendar，我今天才剛用這個幫你排YOASOBI搶票提醒 |
| 追蹤機票價錢/定時查哩程放票 | ✅ 能，但要另外搭排程 | 我可以寫類似你investment排程watchdog的腳本，配合launchd/cron定時跑，邏輯上完全可行 |
| 連Instagram | ⚠️ 沒有現成整合 | 沒有專屬Instagram API/MCP，只能靠claude-in-chrome在瀏覽器裡操作你登入的IG網頁版，比Muse原生整合麻煩 |
| **關掉App後持續在背景跑** | ❌ 這個是關鍵差異 | Muse跑在Meta自己的雲端Secure VM，跟你的手機/電腦開不開機無關；我的排程任務需要**你的Mac開機**才能被cron/launchd觸發，Mac關機或睡眠期間排程不會執行。這是Muse對我的結構性優勢 |
| 免費、不用自己架設 | ❌ 相反 | Muse是Meta代管、你不用管基礎設施；我這邊所有排程/自動化都是你自己的Mac在跑，需要你自己維護環境 |

**結論給派哥**：單純比「能不能做同樣的事」，我透過claude-in-chrome+MCP+launchd排程，功能上大部分都做得到，甚至客製化程度更高（你的cc_processor/investment自動化本來就比通用Agent更貼合你的實際需求）。但**Muse最大的優勢是「跑在別人的伺服器上」**——不用你的Mac開機、不用你自己維護排程環境，這點我做不到，除非你去租一台雲端主機常駐跑Claude Code（你之前討論過Claude 5hr視窗重置那類機制，本質上都還是依賴你自己的機器）。

如果只是想要「簡單的背景小任務、不想耗Claude額度」，網友那句「把Claude的任務offload到Muse」的用法值得參考：簡單/低風險的任務（追蹤機票價格這類）丟給免費的Muse，複雜/客製化的自動化留給我來做。

## 對派哥的意義

- 你已經有的自動化基礎設施（cc_processor、investment排程watchdog、seats.aero提醒）本質上就是「自架的Muse」，只是要你的Mac開機
- 如果想試水溫免費AI Agent的「持續在背景幫你做事」體驗，Muse是低成本的入門選項，尤其適合拿去做機票/哩程放票這種你已經在關注的事
- ⚠️ 權限給予要謹慎，這點跟你一貫的AI安全意識（見CLAUDE.md「任何AI自動讀取email/PDF/外部資料的流程都是indirect prompt injection攻擊面」）一致，Muse連了email/calendar/IG之後同樣要注意這個風險

## 2026-09-25補：實測案例——用Muse查酬賓機位/哩程票

> 來源：[Threads貼文](https://www.threads.com/share/BAQbS91QSs/)，派哥丟連結問「你做不到？」

貼文分享用Muse查詢哩程機票(frequent flyer award seats)的心得，講了4個優勢：
1. **高度客製化**：能針對個人需求做精細的票務搜尋
2. **自動每日刷新**：系統會每天自動重新查詢
3. **Prompt優化省時間**：用對提示詞能大幅節省力氣
4. **資料視覺化**：能生成互動式圖表呈現查詢結果

作者認為「目前市場上還沒有競爭者」，並以此當投資Meta股票的理由。**注意**：貼文沒有附具體案例(哪條航線/哪個艙等/實際查到什麼)，比較像整體使用心得而非技術細節展示，加上作者本身把這個拿來當股票多方論點的一部分，帶有立場，數字/優勢描述無法交叉驗證。

**跟Claude(我)的落差評估**：貼文列的4項裡，「客製化查詢」「每日自動刷新」「資料視覺化」這幾件事，我透過claude-in-chrome+排程腳本+寫程式產生圖表，邏輯上都做得到（跟上面表格分析一致），差別還是同一個結構性問題——Muse跑在Meta雲端不用派哥的Mac開機，我的排程要Mac開機才會跑。「Prompt優化省時間」比較像是使用心得不是技術優勢，不算獨有能力。

## 2026-09-25補：在台灣怎麼註冊Muse

> 來源：[Threads貼文](https://www.threads.com/share/BAV4odemi3/)，社群實測的偏方，非官方保證

**官方現況**：Muse目前只開放**美國(US-only)**，台灣還沒有官方申請管道（2026-09查證）。

**社群偏方（透過Google Gemini Pro的Spark遠端瀏覽器繞過地區限制）**：
1. 需要有 Google Gemini Pro 訂閱
2. 準備一個**從沒用過Muse**的全新Google帳號
3. 在Gemini Pro裡找「**Spark**」這個遠端瀏覽器功能，透過它的（美國端）環境去完成Muse註冊
4. ⚠️ 非官方保證，成功率看帳號方案/地區/IP/Meta政策隨時可能改變，Gemini裡看不到Spark功能通常代表帳號方案或地區資格還沒開通

## 2026-09-27補：實用案例——用Muse管理信用卡每季退額提醒

> 來源：[FB「點數旅人」貼文](https://www.facebook.com/share/p/1KUvEkefNr/?mibextid=wwXIfr)，派哥丟連結說「save sop 你學一下」。作者以前用自己的Google表單管理，現在改用Muse。

### 操作步驟（作者實測）

1. **告訴Muse你有哪些卡**：只講卡片清單，Muse就能自動查到每張卡9/30有哪些季度福利快過期、去哪裡用、且是正確的。⚠️但**它不知道非官方的使用方式**（例如某些退額的變通花法）
2. **告訴Muse你希望的提醒頻率**：可以設定「不忙的時候每兩週提醒一次，最後一個月每週提醒一次，最後一週每天提醒」這種漸進式頻率，不是固定單一頻率
3. **告訴Muse你已經用掉什麼**：手動跟它說一聲，它就不會再為那筆重複提醒
4. **不只季度福利**：半年/月/年這幾種頻率的福利都能請它提醒（作者沒請它提醒月頻的，只是說明它支援）
5. **Membership Year類福利**：某些退額是按「持卡週年」(Card Anniversary date)而非日曆年計算，要告訴Muse你的週年日它才能算準

**作者自己的取捨**：其他AI agent其實也做得到這件事，但作者主要拿Muse做哩程機位查詢+放票通知，決定把這幾件事整合到同一個工具，不是說Muse在這件事上獨有優勢。他也提到目前不打算把主帳號(email/calendar等)交給它，只給了含哩程/點數資料的次要帳號。

### 對派哥的意義（我的反思，因為派哥要我「學一下」）

- 這個模式（依卡片清單自動算退額截止日+漸進式提醒頻率+用掉就消音+分辨日曆年vs持卡週年）本質上就是派哥現有的Notion Todo提醒系統少的那一塊——現在的系統只做**信用卡繳款**跟**回饋點數到期**兩種提醒(`upsert_cc_payment`/`upsert_points_expiry`)，還沒有「退額補助(credit)」這個第三類提醒
- 已存的[[us-credit-card-credits-checklist-2026-09]]是靜態表格(手動查、手動記)，如果比照這篇的邏輯做成自動化，等於把那張表格變成可執行的提醒系統——這是可行的擴充方向，但**要不要做、值不值得投入，要先問派哥**（照CLAUDE.md「改動前先問Spec」，不會自己直接動手），如果派哥想做，下次可以另外討論：卡片退額清單哪裡維護、頻率規則怎麼設、要不要用Notion Todo同一套資料庫多加一個「類型」

## 相關筆記

- [[chatgpt-work-launch-2026-07]] — 同系列的ChatGPT Work分析，逐項對照Claude對應功能
- [[us-credit-card-credits-checklist-2026-09]] — 派哥現有的信用卡退額靜態總表，這篇Muse技巧如果要落地，會是把這張表變成自動提醒系統的參考做法
