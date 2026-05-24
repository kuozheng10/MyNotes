# Codex 50% 非技術任務 — OpenAI Tibo 訪談：Agent 日常使用與邊界

tags: #Codex #OpenAI #Agent #生產力 #AutoReview #VibeCoding #KnowledgeWorker

> 來源：OpenAI Tibo（負責 ChatGPT + Codex 主管）30 分鐘訪談
> 核心數據：Codex 上線三個月，>50% 任務為非技術類

---

## 一、Agent 技術成熟了，不再需要技術背景

**改變的是技術，不是人：**
- Agent 現在可在長時間任務中保持穩定
- 超過 100 個 plugin + computer use + browser use
- GPT-5.5 可靠度提升 → 一般人直接受益
- 以前：agent 出問題需進去調設定（需技術背景）→ 現在不需要了

---

## 二、知識工作者的日常會怎麼變

**Tibo 的核心思路：去看你每天花時間在哪裡**

可自動化的日常任務：
- 一小時市場研究
- 一小時整理 email
- 兩小時篩選潛在客戶

**非技術人可直接用的排程語法（自然語言）：**
> 「每 12 小時跑一次，做完市場研究寄 PDF 給我」→ 直接用 email 寄

**Tibo 自己的用法：**
| 任務 | 說明 |
|------|------|
| Coding | 開發任務 |
| 策略規劃 | 直接在 Codex 裡寫 |
| 當天筆記 | Codex 自動建立 memory |
| Email/Slack 追蹤 | 整理沒回覆的訊息 |
| 早晨報紙 | Slack 新聞每日整理 → 印到實體印表機配咖啡看 |

---

## 三、Auto Review：讓 Agent 自己檢查自己

**架構：**
- 主 Agent 執行任務
- 第二個 Agent 同步驗證所有動作（確認無風險行為）
- 來自 OpenAI safety team + alignment 研究團隊

**效果：**
- Agent 可更長時間自主運作
- 敏感資料更安全（不會把個人資訊寄給陌生人）

**Tibo 的預告：** 技術已存在，差的是產品包裝 → Morning Dashboard（起床看 agent 半夜做的事，逐一 approve）即將成現實

---

## 四、資料整理：本地檔案 → 雲端（三個月內）

**目前問題：** 筆電 + 多台 Mac 資料分散，筆電 agent 跟手機 agent 是兩個分開存在

**Tibo 說接下來三個月：**
- 本地檔案全部搬到雲端
- Agent 會管理自己的 memory + 幫管理雲端檔案
- 現有過渡方案：全部丟 Google Drive → 連接一個 Google Drive 資料夾（可行）

---

## 五、Agent 需要什麼檔案（資料餵食策略）

**Tibo 的建議：**
- 不要用文字解釋自己的語氣風格
- **直接放樣本**：過去寫過的 newsletter、錄音片段、發過的訊息（專業 + 私人都行）

**每個專案：**
- 開一個資料夾 → 放各種相關檔案
- 聯絡人資訊有幫助，但不用全部維護在檔案 → 可讓 Codex 自己去抓

---

## 六、用 vs. 不用 Agent 的生產力差距

**Tibo 的觀點：** 一到三年太遠（技術變太快），但願意適應的人確實會高出不少

**未來每人都有的小型個人助理：**
- 幫你報稅
- 設 email filter
- 幫你跟親友保持聯繫（特別強調這點）

---

## 七、人類仍然要負責（重要邊界）

**Tibo 的核心立場：**
- 思維是「擴充能力」，不是取代
- Agent 產出的程式碼 → 你要為它負責，壞了是你的責任
- Code review：**不能外包「理解」這件事**，人需要理解整個系統

**陷阱警告：**
> 有些人太早把所有事都交給 AI → 能力曲線不到位時投入太多 → 大腦超載
（這不一定是壞事，代表你在拓展邊界，知道什麼現在能做、什麼三到六個月後才行）

---

## 八、Vibe Coding 邊界

| 情境 | 建議 |
|------|------|
| 幾個人用、試試看、享受過程 | 自己用 agent 寫完全 OK |
| 規模化、服務幾十萬人 | 還是需要技術人員加入 |

**時間表：**
- 長期可維護性：6–9 個月內顯著進步
- 完全不需技術人員：感覺還有一段路

---

## 九、軟體工程師會變多還是變少

**Tibo 的觀點：**
- 基礎設施和 app 數量會大爆發
- 有 idea 就能蓋出來（實驗的好時機）
- 軟體需求問題一直在被發現 → 技術人才需求持續存在

---

## 十、Live Demo 展示

### Chief of Staff Prompt 範例
連接 Gmail + Calendar + Docs，說：
> 「當我的 chief of staff，整理我今天的 breakdown，告訴我什麼重要，幫我準備好。」

進階用法：
> 「我在哪裡浪費時間？應不應該請人處理某件事？還是建一個 app 來優化？」

**UI：** Floating widget 像小寵物可在螢幕拖動，查看每個 thread 進度

### Computer Use Demo（LinkedIn 數據下載）
1. 開啟 computer use 模式
2. Agent 直接控制瀏覽器 → 進 LinkedIn → 點擊導航 → 下載資料 → 建試算表
3. 耗時：5–10 分鐘
4. 支援語音補充需求 → Agent 繼續執行

### Skill Creator
- 喜歡某個 workflow → 讓 Codex 做成可重複執行的 skill
- 之後每天自動跑（排程化）

---

## 關鍵數字

| 數字 | 意義 |
|------|------|
| >50% | Codex 任務為非技術類（上線三個月） |
| >100 | 可用 plugin 數量 |
| 6–9 個月 | 長期可維護性預計顯著進步時間 |
| 3 個月內 | 本地檔案搬雲端、跨設備 agent 統一 |

---

## 十一、Tibo 的個人經歷

**職涯路徑：**
- PhD → 讀了兩週退學（四年綁定一個主題不適合他，想嘗試更多）
- Google Maps → Google 廣告 → DeepMind（黃金時期，一個接一個 grand challenge）
- DeepMind 後期變無聊 → OpenAI 證明 scaling transformers 可行 → 加入

**核心人生觀：**
> Follow your instincts，做給你能量的事。

---

## 十二、未來願景：Ambient Intelligence

**Tibo 的憂慮：** 現在你得到的 AI 好處跟 prompting 能力成正比 → 他認為未來不應該這樣

**願景：**
- 不管有沒有主動使用 AI，都能受益
- 不是 prompting 能力決定差異，而是「做你自己」

**裁縫比喻：**
> 好裁縫一眼看著你，就知道什麼衣服適合你
> 好的 AI 會像從好朋友那裡得到建議，在對的時間給對的幫助

**關鍵詞：** Ambient Intelligence（環繞式智慧）— 你不需要主動 prompt，AI 就在背景理解你的需求

---

## 相關筆記

- [[codex-computer-use-mac]] — Codex Computer Use 操作筆記
- [[claude-code-ai-dev-team-design]] — Agent 開發團隊設計
- [[ai-coding-agent-workflow-threshold]] — AI coding agent 適用邊界
- [[vibe-coding-architecture-debate]] — Vibe Coding 架構爭議
