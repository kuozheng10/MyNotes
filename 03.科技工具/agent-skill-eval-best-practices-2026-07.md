---
tags: [ai-coding, claude-code, skill, eval, testing, google-deepmind]
source: 張維峰整理 Google DeepMind Philipp Schmid 演講，FB分享，https://www.facebook.com/share/p/1D3wE9pxEA/?mibextid=wwXIfr
date: 2026-07-31
related: cangjie-skill-distill-2026-07, jason-liu-codex-work-system-2026-07, caveman-token-saving-skill-2026-07
---

# Agent Skill 評估最佳實踐（Google DeepMind）

> **核心金句**：「You wouldn't merge code without tests, so why are we shipping skills without evals?」——程式碼不寫測試不會上線，但 skill 卻常常沒測試就發布。

---

## 核心問題

Skillsbench 分析超過 **50,000 個 Skill**，發現絕大多數沒有 Eval。後果：分不清「失敗是 skill 本身寫爛，還是任務本來就難」。

## 關鍵統計數據

| 數字 | 意義 |
|------|------|
| **15%** | Skill 平均效能提升幅度 |
| **50%** | 因 skill **未被正確觸發**導致的失敗比例（觸發精準度比skill本體品質更常是問題所在） |
| **500行** | Skill 檔案建議上限 |
| **117個** | Gemini Interactions API skill 的測試案例數 |
| **90%** | 該 API 最終正確率 |

---

## Skill 分類

- **Capability Skill**：教模型新能力，可以隨時間退役
- **Preference Skill**：編碼團隊偏好/規範，需要長期維護

## Progressive Disclosure（三層架構，決定成本結構）

1. **第一層**：標題與描述——**固定成本**，每次對話都要付（不管有沒有用到）
2. **第二層**：Skill 本體——**條件性成本**，觸發時才付
3. **第三層**：參考檔案——**深度探索時才付**

> 對應到派哥自己的 skill 庫：`~/.claude/skills/*.md` 的 description 欄位就是第一層，寫得越精準，越不會平白燒 token 又觸發不到。

## 觸發方式

- **Model-triggered**：模型自己判斷要不要用——面向客戶的場景必用
- **User-invoked**：使用者手動觸發（例如 `/save-sop`）——開發工作流適用

---

## 最佳做法十條

1. **Skill 描述最關鍵**，決定觸發精不精準
2. 用**指令式語氣**，不要用被動描述
3. 必須納入**負面測試案例**（不該觸發的情境）
4. 從 **10-20 個樣本**開始，不用一次求全
5. 測試**結果**，不是測試**執行路徑**
6. 用**隔離環境**跑測試，避免模型作弊（抄答案而非真的推理）
7. 每個案例跑 **3-6 次**衡量可靠性（不是跑一次就信）
8. **跨 Harness 測試**（Gemini、Claude Code 等都要測，不要只測一個環境）
9. Skill 退役時**保留 Eval 當監控工具**
10. **從第一個 skill 開始就建立 Eval**，不要等出問題才補

## Eval Harness 實作架構

- JSON 檔案定義測試案例：`prompt` + `預期語言` + `should_trigger` 標記 + `斷言`
- Python 腳本跑 Coding Agent，檢查輸出

**兩種斷言方式**：
| 方式 | 成本 | 用途 |
|------|------|------|
| Regex 斷言 | 低 | 檢查 SDK 版本、method 名稱是否正確 |
| LLM-as-Judge | 高但必要 | 評估完整流程、程式碼品質、品牌規範這類難用規則判斷的東西 |

## 關鍵數據發現

- **人類寫的 skill 表現最好**
- **AI 生成的 skill 可能有負面效果**——常常塞進 **No-op 指令**（講了等於沒講、不會改變行為的廢話指令），純粹浪費 token
- **50% 失敗來自觸發精準度不足**，不是 skill 本體邏輯錯

## Google DeepMind 內部回歸測試流程

每次改 skill 都自動跑 Eval，**修改必須讓測試結果變好、或新增測試案例，才准 merge**——品質只能升不能降。

## 具體行動方案（可直接照做）

1. 挑最常用的 skill，先寫 5 個測試 prompt
2. 檢查並移除 No-op 指令（作者有整理 GitHub 資源可參考規則）
3. 跑消融測試（Ablation Test）——拿掉這個 skill，任務表現差多少，藉此衡量它真正的價值

---

## 對派哥的意義

- 派哥的 skill 庫已經有一定規模（save-sop、notion-todo、gen-image-web、caveman 等），目前都是「寫完就上」，沒有 eval 機制——符合這篇講的「50,000個skill裡大多數的通病」
- 跟 [[cangjie-skill-distill-2026-07]] 對照：cangjie 的七階段流水線第6步「壓力測試」（含誘餌題）其實就是這篇講的 Eval 精神，只是應用在「從書/影片蒸餾skill」這個特定場景；這篇提供的是更通用、可套用到**所有既有skill**的評估框架
- 跟 [[jason-liu-codex-work-system-2026-07]] 對照：Jason的「self-improve skill」會分析哪個skill常被呼叫、找重複模式優化，這篇補上「怎麼知道優化後有沒有真的變好」的具體方法（regex斷言+LLM-as-judge+回歸測試）
- 具體可執行：下次派哥要新增或大改一個 skill 時，可以先問「這個skill要怎麼測試觸發準不準、輸出對不對」，而不是寫完就直接上線

---

## 相關筆記

- [[cangjie-skill-distill-2026-07]] — 把長內容蒸餾成skill的七階段流水線，第6步壓力測試是這篇Eval精神的其中一種應用
- [[jason-liu-codex-work-system-2026-07]] — self-improve skill實戰案例，這篇補上「怎麼驗證優化有效」的評估方法
- [[caveman-token-saving-skill-2026-07]] — 這篇提到的No-op指令浪費token問題，caveman skill的壓縮邏輯剛好是反面做法（明確量化、有測試基準的節省）
