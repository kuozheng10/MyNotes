---
title: AI Coding 時代的軟體測試全流程——從需求到 Production
tags: [AI測試, SDD, 軟體測試, AIOps, DevOps, QA, 測試左移, 測試右移, LLM-as-Judge, 規格驅動]
date: 2026-04-27
category: AI工具
---

## 核心框架

沿用 Agile 四大區塊骨架，但每格內部的 practices、執行者、工具全面翻新：

```
測試左移 → CI 主鏈 → Post Integration → 測試右移 → (production 回饋回左移)
```

---

## 一、流程入口：需求 Agent / MCP Server

**做什麼**：把 PM、客戶、會議紀錄的零散需求擷取成結構化格式
**MCP 的角色**：直接連 Jira / Notion / Slack / Email，主動拉需求，不等人整理
**執行者**：AI 主導，人類補 context（業務關聯、客戶痛點）
**時機**：持續運作，有新訊息就更新需求池

---

## 二、規格三件套（AI 寫 code 前必備）

### 可執行規格
- 格式：Gherkin / TLA+ / 結構化 YAML（機器可讀）
- **為什麼必須可執行**：AI 寫 code 速度太快，人來不及審查，規格必須能直接變成測試
- 執行者：人類主導（商業規則），AI 輔助（轉格式、補語法）

### Spec Review Agent
- 任務：審查規格的歧義，不審 code
- 例子：「連續登入失敗三次鎖定」→ 連續是時間還是次數？鎖多久？匿名算嗎？
- **AI 窮舉解讀，人類拍板採哪種**

### Property Tests
- 定義「不管輸入是什麼都該滿足的本質性質」
- 例：排序函式 → 長度不變、相鄰非遞減、集合不變、冪等
- 執行者：人類設計性質（需要抽象思考），AI 輔助發想

**時機**：每個新功能啟動時備齊，不是寫完才補

---

## 三、SDD + CI 主鏈（七步）

| 步驟 | Agent | 執行者 | 說明 |
|------|-------|--------|------|
| 1 | 代碼生成 Agent | AI 自主 | 接收規格三件套產出實作；最大不確定性來源 |
| 2 | 幻覺檢測 Agent | 工具自動 | 驗證 AI 引用的 API/函式/套件真的存在；最便宜的檢查 |
| 3 | 安全合規 Agent | AI 主導 + 安全團隊審核 | 掃漏洞、合規；值不值得擋發布需人判斷 |
| 4 | 數據隱私 Agent | AI 偵測 + 法務/DPO | 追蹤 PII 資料流向（GDPR/CCPA）；邏輯和安全不同 |
| 5 | 建構部署 Agent | 自動化工具 | 打包、部署到測試環境 |
| 6 | BVT Agent | AI 自主 | 根據本次 PR 改動範圍即時生成冒煙測試 |
| 7 | Bug 修復 Agent | AI 主導 + 人類介入重大修改 | 任何一站抓到問題自動產生修補 |

---

## 四、主鏈旁的三個關鍵角色

### Mutation Agent（測試你的測試）
- 故意修改 production code（`>` 改 `>=`、刪掉 if），看測試能不能抓到
- 如果改了還全綠 → 測試沒在驗證那段邏輯
- 時機：每次 PR 跑輕量版（針對改動範圍）+ 每週批次全量（輸出弱點報告）

### Differential Agent（用 AI 的不一致偵測規格漏洞）
- 多個 AI 各自實作同一 spec，大量輸入下比對輸出
- 三份一致 → 任務「夠收斂」；歧異 → spec 有模糊，退回需求區
- 時機：與代碼生成（步驟1）**並行**跑

### 人類檢視程式
- Code review + 判斷（特意用琥珀色標示，非 AI）
- **AI 時代人類角色**：從寫 code → 審 code；從執行者 → 把關者

---

## 五、治理 Agent（中央監督，非中央調度）

**它不排程主鏈**，只在以下情況介入：
- 某個 Agent 卡住
- Agent 之間有衝突判斷（安全合規說擋，代碼生成 Agent 又生新版）
- 某 Agent 輸出信心分數異常低
- 流程時間超出預期

用**虛線**連接（監督關係），非實線（執行流）
執行者：AI 主導，SRE / 工程主管設定治理規則

---

## 六、Post Integration 智能持續測試

> AI 時代，整合之後的工作量比整合之前還重

| Agent | 執行者 | 特點 |
|-------|--------|------|
| 功能測試 Agent | AI 自主 | 驗證業務規則 |
| 非功能 Agent | AI 自主 | 效能 / 負載 / 壓力 |
| **探索測試** | **人類主導** | 資深 QA 的直覺、好奇心；AI 目前做不到 |
| 回歸 Agent | AI 自主 | 風險導向選擇，分析影響範圍動態決定跑哪些 |
| 驗收測試 Agent | AI 自主 | 模擬真實用戶端到端流程 |
| **自我修復測試** | AI 自主 | UI/API 變動時語意理解自動更新測試，防止測試成為發布瓶頸 |

**觸發時機**：每次 PR 通過主鏈後自動觸發

---

## 七、測試右移：Production 為主戰場

| 機制 | 執行者 | 說明 |
|------|--------|------|
| 影子流量 / Canary 部署 | 部署工具自動（Service mesh / LaunchDarkly） | 影子流量複製真實請求不回應用戶；Canary 小比例放量 |
| Chaos Agent | AI 自主，SRE 設定範圍時段 | 主動注入故障（關服務、模擬延遲、異常流量），測韌性 |
| 線上監控 Agent | AIOps 平台（Datadog Watchdog / New Relic AI）| 非固定 threshold，AI 分析 log/trace/metric 異常模式 |
| LLM-as-Judge | LLM 評分，人類定期抽樣校準 | AI 產品特有；評估 chatbot / 文案 / 推薦等無二元答案的輸出品質 |
| Drift Detection | MLOps 平台（Evidently AI / WhyLabs）| 偵測模型漂移、資料漂移、行為漂移 |
| 自動修復 Agent | AI 自主，SRE 設定 threshold | 偵測異常時觸發回滾或熱修補 |

---

## 八、最重要的線：Production → Spec（橘色虛線）

**production 數據回饋更新 spec** — 整張圖的靈魂

傳統做法：線上發現 bug → 修 patch → 結案

**AI 時代做法**（三件事同時做）：
1. 加 property test 防止這類錯誤再發生
2. 更新可執行規格補上這個情境
3. 更新給 AI 的 prompt，讓未來生成類似 code 時自動考慮這個情境

沒有這條線 → 只是把人寫 code 換成 AI 寫 code，效率提升但本質沒變
有這條線 → 系統開始具備「**組織記憶**」，越用越聰明

---

## 九、底層：Prompt 版控與 Agent 配置

| 資產 | 說明 |
|------|------|
| Prompt 版控 | Prompt 是 AI 時代的「設計文件」，需進 Git、review、diff、回溯 |
| Agent 配置 | Agent 的行為參數需版控 |
| 評估資料集 | LLM-as-Judge 的校準基準 |
| MCP Server 註冊表 | 工具清單與版本管理 |

**維護者**：平台工程團隊（不是 application 工程師）
**類比**：就像過去的 CI/CD 基礎設施，需要專人專責維護

---

## 對派哥的意義

- **cc_processor**：已有排程 + Agent Loop 概念，可對照「治理 Agent + 主鏈七步」補強錯誤處理
- **MyNotes 健檢**：可對應「Mutation Agent」概念——定期測試「筆記系統是否真的在運作」
- **個人自動化 SOP**：「Prompt 版控」很重要；目前派哥的 CLAUDE.md / skill 就是這層，要持續維護

---

## 連結筆記

- [[ai-era-testing-strategy]] — AI 時代測試策略（舊筆記，本篇為深度延伸）
- [[SDD-vs-SBE]] — 規格驅動開發 vs 實例化需求
- [[exploratory-testing-sbtm]] — 探索測試方法論
- [[anthropic-agent-infra-strategy]] — Anthropic 的 Agent Infra 戰略
- [[ai-agent-system-design-over-prompt]] — 系統設計勝過 Prompt 工程
