# Claude Code Dynamic Workflows：大型任務多代理編排

> 來源：Facebook 貼文整理
> 整理日期：2026-06-01
> 版本：Claude Opus 4.8（2026年5月底推出）

---

## 背景：AI 自動化工具演進

```
提示詞工程 → Vibe Coding → 自動化 Workflow
```

真正的需求不一定是做產品，而是**建立自己的自動化工作流**：
- 每晚 Agent 抓新聞 → 早上出分析報告
- Agent 自動掃信箱 → 擬回信 + 排序重要性

傳統 RPA（Make、n8n）門檻高，各大 AI 廠開始做更易用的方案：

| 廠商 | 工具 | 特色 |
|------|------|------|
| OpenAI | Codex `/goal` | 規劃→執行→驗證循環，直到達成目標 |
| Anthropic | Claude Code Workflow | 工程場景自動化，JS 編排腳本 |
| Google | Antigravity 2.0 | 自動安裝/撰寫工具達成目標 |

---

## Claude Code Dynamic Workflows 核心概念

**不是多開幾個 subagent，而是即時產生 JavaScript 編排腳本，由背景 runtime 執行。**

腳本負責：
- 迴圈與分支
- 任務拆解
- 結果協調

Session 執行中仍可互動。

---

## Subagent vs Workflow 比較

| 維度 | Subagent | Dynamic Workflow |
|------|----------|-----------------|
| 適合規模 | 中等，步驟明確 | 超大型，超出單一 context window |
| 編排方式 | Claude 逐輪啟動 | JS 腳本控制迴圈/分支 |
| 中間結果 | 回到主對話 context | 保留在腳本變數 |
| Claude context 負擔 | 高（中間結果都要接） | 低（只接最終答案） |
| 最大並發 agent | 有限 | **最多 1,000 個，同時 16 個** |
| 驗證機制 | 無內建 | 一批 agent 解題 + 另一批反駁驗證，有歧異繼續迭代 |
| 成本 | 較低 | **較高（更多 token）** |

---

## 啟動方式（三種）

1. **Prompt 中要求**：直接要求建立 workflow
2. **內建指令**：`/deep-research`
3. **自動判斷**：`/effort ultracode` → Claude 自動決定是否用 Workflow

> 首次執行前會顯示計畫並要求確認。

---

## 管理 Workflow

```bash
/workflows          # 查看階段、agent 數量、token 用量、個別輸出
                    # 也可暫停、恢復、停止
```

**儲存可重複使用的 Workflow**：
```
專案層級：.claude/workflows/
個人層級：~/.claude/workflows/
```
儲存後可用 slash command 再次執行。

---

## 適合場景

- 全庫安全稽核
- 大型框架或 API 遷移
- 語言移植（程式語言轉換）
- 需要交叉驗證的研究任務

---

## 官方案例

**Jarred Sumner（Bun 作者）**：
- 任務：將 Bun 從 Zig 移植到 Rust
- 時間：11 天
- 產出：~75 萬行程式碼
- 結果：通過 99.8% 既有測試

---

## 使用原則

> **簡單任務用 Subagent，複雜大型任務才用 Workflow。**

- 任務簡單、拆解方式已知 → Subagent 或 Skill（成本低、易維護）
- 超出 context window 的大型問題、需要交叉驗證 → Workflow

---

## 相關筆記

- [[senior-dev-ai-era-harness-complexity]] — AI 時代架構師角色
- [[ai-coding-harness-contract-first-andrew]] — ralph-loop 概念（Workflow 的前身思維）
- [[vibe-coding-dodonov-stanley-ai-tool]] — 對比：沒有 guardrails 的極端案例
