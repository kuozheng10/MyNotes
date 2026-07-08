---
tags: [ai-agent, agentic-ai, claude-code, framework, harness, orchestration, mcp, skills]
source: jamesCodeLab (X/Twitter 貼文)
date: 2026-07-09
---

# Agent Framework vs Agent Harness — 沒人宣佈的代班

## 核心論點

> 2025 年出貨的一半「AI 代理商」是模型已經不再需要的 3,000 行編排代碼。

框架（Framework）與利用（Harness）是兩種根本不同的技術站位，大多數團隊還站在舊的那一邊而不自知。

---

## 兩者定義

| | Agent Framework | Agent Harness |
|---|---|---|
| **本質** | 施工包（Kit）— 你自己蓋循環 | 完成品運行時 — 供應商擁有循環 |
| **代表** | LangGraph, CrewAI, Google ADK, Microsoft Agent Framework | Claude Code, Codex CLI, Gemini CLI |
| **你要做的事** | 寫編排邏輯、狀態機、工具呼叫、重試、記憶體、終止條件 | 設定 + 延伸：skills、MCP server、hooks、plugins、custom tools |
| **智慧所在** | 你的架構本身 | 模型 + Harness 整體 |
| **已內建** | 無，自己組 | context 管理、工具執行、權限閘、沙箱、subagent、compaction |

---

## 分裂的六個維度

1. **循環所有權** — 你寫它 vs 供應商運送它
2. **延伸方式** — 寫代碼 vs 配置（skills / MCP / hooks）
3. **抽象層級** — 原始元件 vs 第一天就是能工作的 agent
4. **失敗發生的地方** — 編排邏輯的 bug vs context 與權限設計的疏漏
5. **模型升級時** — 框架：升級後你要重新調校（反應堆式）；Harness：改良免費抵達（自動吃到紅利）
6. **控制 vs 能力** — 完全控制 vs 用邊界換取能力，harness 拿走完全控制換取免費的能力提升

---

## 時代轉折（沒人正式宣佈）

- **2023–2024｜框架時代**：模型能力弱，需要精心編排來補償缺陷
- **2025–2026｜Harness 時代**：模型已強到「好 harness ＋ 精心設計的 context」勝過大多數客製編排

> 教訓：你手工搭的棚架，會被下面那層（更強的模型 + 更好的 harness）直接吸收掉。

**連框架供應商自己都在往這個方向靠：**
- 微軟把 AutoGen 和 Semantic Kernel 合併成統一的 Agent Framework
- Oracle 把 agent 執行時直接搬進資料庫
- 整體趨勢：往「更少、更深」的迴圈收斂，而不是更多客製迴圈

**框架仍然有贏的場景**：需要真正客製化的工作流（pipeline、確定性保證、深度系統整合）——但這個真正需要框架的類別，比大家想像的小很多。

---

## 對派哥的意義

派哥的工作流（cc_processor、投資追蹤、Notion 自動化）幾乎全部建立在 **Claude Code（harness）+ skills/hooks/subagent** 上，沒有自建 LangGraph/CrewAI 那類編排框架——這正好站在文章說的「對的一邊」。

真正該問的問題不再是「要用哪個框架？」，而是：

> 我需要的這個迴圈，Harness 是不是已經內建了？——還是我真的要蓋一個新代理商，或是為既有 Harness 打造更合適的環境（context/skills/hooks）？

實務對應：
- 想加新自動化 → 先問「這是 skill/hook/MCP 能解決的配置問題，還是真的需要一個獨立編排迴圈？」
- 91% 情況下，答案是前者（延伸 harness），不要重造循環

---

## 相關筆記
[[claude-code-setup-plugin-2026-06]] · [[agentic-sop-to-work]] · [[anthropic-skill-three-layers-2026-06]] · [[ai-engineering-evolution]]
