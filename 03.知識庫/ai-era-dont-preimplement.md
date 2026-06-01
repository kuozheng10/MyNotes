# AI 時代的「不用急著實作」原則

> 來源：Facebook 貼文（#markven #ainative）
> 整理日期：2026-06-01

---

## 核心洞見

> 做太快了，有時候等等，官方就會推出來了。

在 AI 原生時代，許多你想自己造的輪子，大語言模型廠商很快就會原生支援。

---

## 真實案例

**背景**：想讓 Agent 工作更順，嘗試自己實作 clustering 分散式分工：
- 多併發任務
- 分配工作 → 合併處理

**結果**：實作完沒多久，Claude Code 推出 **Dynamic Workflows** 原生功能：
- 協調邏輯由 Claude 寫成 JavaScript 腳本、在背景自動執行
- 最多 1,000 個 subagent、同時 16 個並發
- 這就是很典型的分散式 clustering 分工方法

---

## 傳統 CS 架構 → LLM 框架

很多在傳統領域用過的架構，現在都可以在 LLM 框架下嘗試複製：

| 傳統領域 | LLM 類比 |
|---------|---------|
| 分散式 clustering | Dynamic Workflows subagents |
| Computer Vision 3D 建模精度提升 | 多 agent 交叉驗證（批次解題 + 反駁） |
| MapReduce 分工合併 | JS 腳本協調多 subagent → 合併結果 |

---

## 操作原則

1. **有想法先觀望**：LLM 廠商在快速追上各種架構模式，等 2-4 週看看
2. **DIY 仍有價值**：過程中學到的原理，能幫助更快理解官方功能的設計邏輯
3. **實作 vs. 等待的判斷**：
   - 需求緊迫、商業壓力 → 自己做
   - 純研究、探索性 → 考慮等官方

---

## 相關筆記

- [[claude-code-dynamic-workflows-multi-agent]] — Dynamic Workflows 技術細節與操作方式
- [[senior-dev-ai-era-harness-complexity]] — AI 時代架構師的角色與 Harness 思維
