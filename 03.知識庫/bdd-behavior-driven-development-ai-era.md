---
title: BDD 不是測試框架——Dan North 親口澄清，AI Coding 時代更該搞懂
tags: [BDD, 測試策略, AI協作, SDD, 需求工程, Gherkin]
date: 2026-04-29
category: 測試與品質
---

## 這是什麼

BDD（Behavior-Driven Development，行為驅動開發）是 Dan North 發明的需求釐清方法論，核心不是測試工具或語法，而是「先講清楚，再寫程式」的習慣。

2026 年因 AI Coding（Claude Code、Cursor、Copilot）、Spec-Driven Development（SDD）、AWS Kiro 等工具興起，BDD 重新成為焦點——因為 **AI 會把含糊需求以一百倍速產出一百倍垃圾**。

---

## BDD 的本質

- 用具體例子說一個故事，讓 PM、工程師、設計師、QA 都看得懂同一份需求
- 再拿這個故事去驅動開發
- 核心不是 Cucumber、Gherkin，而是「建立共識」的過程

---

## BDD vs 傳統測試：五個關鍵差異

| 維度 | 傳統測試 | BDD |
|------|---------|-----|
| 切入點 | 寫完才驗證 | 動工前先講清楚 |
| 目的 | 抓 bug | 建立信心與共識 |
| 語言 | 工程師才看得懂 | 所有角色都看得懂 |
| 時間點 | 事後補測試 | 先畫藍圖再動工 |
| 寫太多 | 尚可 | 反而是災難（腳本冗長難維護） |

---

## Gherkin 語法範例

```gherkin
Scenario: 餘額不足時扣款應該失敗
  Given 用戶餘額為 50 元
  When 收到扣款 100 元的請求
  Then API 應回傳 HTTP 400
  And 錯誤代碼應為 'INSUFFICIENT_FUNDS'
```

PM、業務、客服全看得懂，同時可直接作為 AI prompt。

---

## AI Coding 時代，BDD 為何重要

**Given/When/Then 是天然的 prompt 格式**：結構化、無歧義、貼近自然語言，丟給 AI 的輸出品質遠高於「幫我做個登入功能」。

**可執行規格 = AI 的護欄**：AI 寫完程式必須通過這些測試，提供客觀驗收防線。Adrian Cockcroft 指出：「比起 unit test，AI 更難偽造 BDD 測試的結果，品質明顯更好。」

**規格變活文件**：Feature file 綁定測試，只要測試還會跑，文件就一定是最新的。

---

## 三個核心觀念

1. **BDD 是釐清需求的方法，不是測試框架**——核心是建立共識，測試只是副產品
2. **BDD 是必要條件（知道要做什麼），測試是充分條件（確認做對了）**——兩件事不能混為一談
3. **AI Coding 時代，BDD 是給 AI 的最佳輸入格式**——越早習慣 Given/When/Then，AI 回報越誇張

---

## 對派哥的意義

- cc_processor、My Wallet Trip 新功能開發前，可用 BDD 情境先對齊需求
- 搭配已有的 `SDD-vs-SBE.md` 筆記，形成完整的需求→規格→測試鏈路
- Claude Code 可直接吃 Feature file 當 prompt，比模糊描述精準十倍

---

## 補充（2026-07-19）：業界最新做法——AC 從工單附註變成規格文件的一層

> 來源：業界整理文章，講「驗收條件（Acceptance Criteria, AC）」在 AI coding 時代的地位轉變

### 三種失敗模式（為什麼 AC 的地位變了）

1. **意圖漂移（intent drift）**：「加上登入」這種指令嚴重欠缺規格，agent 挑的預設值很少符合團隊實際想要的
2. **脈絡衰減（context decay）**：程式庫超過 agent 的有效 context window，它會忘記早先決策，默默跟自己矛盾
3. **產出無法驗證（unverifiable output）**：沒有明確 AC，就沒辦法判斷 agent 的程式碼「對不對」，code review 變無底洞

以前 AC 含糊，開發過程還有很多次人與人對話可以補救；現在 agent 拿到 AC 就開跑，中間沒有「欸這裡怪怪的，我問一下PO」這個環節。**驗證成本沒有消失，只是全部往後堆到 review 那一關。**

### Test Double 的協作流程：Three Amigos 沒有過時

1. 先寫兩份設計文件：一份講意圖（intent），一份講脈絡/限制/範例
2. 召開 Three Amigos 會議（產品、開發、測試三方）
3. 以兩份文件為輸入，協作產出 AC
4. AC 定案後，才讓 AI 開始實作

具體例子：「加上2FA」這個模糊需求，經過15–30分鐘協作討論，逼問成明確答案——哪些使用者需要2FA？（有留電話號碼的）驗證失敗怎麼辦？（導回登入頁並顯示錯誤）沿用哪段既有程式？（密碼重設流程的模式）怎麼知道做完了？（十二條Given/When/Then）

搭配 **Example Mapping**（Matt Wynne提出）：黃卡寫story、藍卡寫規則、綠卡寫範例、**紅卡寫當場沒人能回答的問題**。關鍵洞察：光有範例還不夠，規則也得在場，兩者互相印證才寫得出足夠的驗證。**紅卡沒清完，story就不該交給agent。**

### 規格做法：三個具體工具/語法

| 工具 | 核心做法 |
|---|---|
| **AWS Kiro** | 固定三文件結構：requirements.md（需求+AC）、design.md（設計）、tasks.md（任務拆解）。AC 用 **EARS語法**（Easy Approach to Requirements Syntax，源自航太業Rolls-Royce）：`WHEN 使用者連續三次輸入錯誤密碼 THE SYSTEM SHALL 鎖定帳號十五分鐘`，每條都有明確觸發條件+系統反應，歧義空間小 |
| **GitHub Spec Kit** | 規格變成版本化的Markdown文件，住在repo裡跟程式碼一起演進，每次開發session開始餵給agent當持久脈絡。解決脈絡衰減——資深工程師「本來就知道」的團隊慣例，agent每次都得被明確告知，除非固化進規格。**Spec是耐久資產，prompt是拋棄式的** |
| **amux 指南** | 一份spec包含Goal/Requirements/Constraints/Acceptance criteria四段。AC範例：`make test`全數通過、對同一事件呼叫兩次資料庫只留一筆、既有測試不能壞。三個特徵：**可機器判定**（沒有模糊空間）、**Constraints明講不准做什麼**（對agent必須白紙黑字，人類常識對agent不是常識）、**review對照AC而非感覺**（"review against acceptance criteria, not vibes"） |

這跟 SBE 的血緣關係很明顯：SBE的範例主要給人建立共識，SDD的AC同時要給機器當停止條件。兩者可疊合——用SBE的協作方式找出key examples，再寫進spec的AC段落。

### 完整性還是人的工作：AI補不了你沒問出來的問題

- **Key examples而非窮舉**：每條規則配代表性範例+會翻車的邊界，不窮舉所有組合（人看不完，agent context也塞不下）
- **測試設計技法當提問清單**：零/一/多、邊界值、狀態轉換、負向路徑、權限矩陣、並發——拿這些反問每條AC，漏洞自己浮出來
- **Lisa Crispin團隊的節奏**：會議限時一小時，固定在planning前兩個工作天舉行（紅卡問題才有時間拿回去問清楚），結果退件率下降、cycle time縮短。**AC定案和agent開工之間，要留出清紅卡的緩衝**

---

## 連結筆記

- [[SDD-vs-SBE]] — 規格驅動 vs 實例化需求的比較
- [[ai-era-testing-strategy]] — AI 時代的測試策略全貌
- [[ai-test-case-design-blind-spot]] — AI 無法設計測試案例的根本原因
- [[ai-coding-testing-management-10-issues]] — AI coding 測試管理十大問題
