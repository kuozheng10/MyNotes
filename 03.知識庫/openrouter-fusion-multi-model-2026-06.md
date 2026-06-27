---
tags: [fusion, multi-model, agent, code-review, openrouter, opencode, benchmark, draco]
source: https://github.com/KainHuang777/opencode_fusion
date: 2026-06-27
---

# OpenRouter Fusion — 多模型交叉審閱系統

> **核心概念**：不同架構模型有不同盲點。把同一任務平行派給多個模型，由 Judge 綜合，品質高於任何單一模型。
> **執行環境**：opencode-go（非 Claude Code），需要 OpenRouter API 或多 provider 支援。

---

## Fusion vs 單一模型 — DRACO Benchmark 數據

| 組合 | 分數 |
|------|------|
| Fusion 旗艦（Fable 5 + GPT-5.5） | **69.0%** |
| Fusion 三模型（Opus 4.8 + GPT-5.5 + Gemini 3.1 Pro） | **68.3%** |
| 單一最強 Claude Fable 5 | 65.3% |
| Fusion 平價（Gemini Flash + Kimi + DeepSeek） | **64.7%** |
| 單一 DeepSeek V4 Pro | 60.3% |

**結論**：Fusion 旗艦比最強單模型高 +3.7%；Fusion 平價比單模型 DeepSeek 高 +4.4%。

---

## 兩種 Fusion 模式

| 模式 | 適用環境 | 效果 |
|------|---------|------|
| **真多模型 Fusion** | 有多個 provider（opencode-go）| 最佳，不同架構盲點互補 |
| **Self-Fusion（同模型 ×2）** | 單一模型環境（Antigravity）| 次佳，靠角色化提示詞區分視角 |

Self-Fusion 數據：Opus 4.8 從 58.8% → 65.5%（+6.7%），仍優於單次直答。

---

## 核心設計原則

### 1. Judge 不能用同架構模型

同家族模型有偏差（+10~25 分的裁判偏心）。
- ✅ DeepSeek Panel → Judge 用 Kimi 或 Qwen
- ❌ DeepSeek Panel → Judge 用 DeepSeek（偏差）

### 2. 啞鈴型成本架構

```
廣度層（便宜專才，各自只評 2~3 維度）
  ├── Plot Editor：DS V4 Flash — 節奏/結構
  ├── Character Editor：Qwen3.7+ — 人物/對白
  └── Prose Editor：MiMo V2.5 — 文筆/意象
              ↓（精煉報告，不是全文）
深度層（貴的 Judge）
  └── Editor-in-Chief：DS V4 Pro — 綜合分析
```

關鍵：Judge 只看精煉報告，不通讀全文 → token 消耗低，品質高。

### 3. 審計模型選擇邏輯

作者觀點：Codex 審 Claude 的 code（不同架構互補盲點）

派哥的觀點：Claude 審 Codex 的 code（Claude 推理更強，適合審邏輯）

**實際應該依任務選**：
| 任務 | 建議 |
|------|------|
| Coding（邏輯/架構）| Claude 審 Codex（Claude 推理更強）|
| 網頁/前端 | Codex 審 Claude（Codex 對 UI pattern 更熟）|
| 研究分析 | 多模型平行，Judge 用最強的 |
| 小說 | 三專才（情節/人物/文筆）+ 總編 |

---

## Fiction Editor — 小說三位編輯模式

三種視角同時審稿，各司其職：

| 角色 | 模型 | 審查範圍 |
|------|------|---------|
| Plot Editor | DS V4 Flash | 節奏、結構、場景邏輯 |
| Character Editor | Qwen3.7+ | 人物一致性、情感、對白 |
| Prose Editor | MiMo V2.5 | 文筆、意象、句式 |
| Editor-in-Chief（Judge） | DS V4 Pro | 綜合改稿 |

Benchmark：fusion-budget 排第 5（8.44 分），成本極低；fusion-fiction-opus 排第 3（8.50 分）。

---

## 適用場景 vs 不適用

| 適合 | 不適合 |
|------|--------|
| 研究分析、架構決策（+5~10 分）| 簡單問答（無增益，增加延遲）|
| 小說章節編輯（+8~15 分）| 快速確認性任務 |
| 複雜策略評估（+3~7 分）| token 預算有限時 |

**代價**：延遲 2~3 倍（平行派遣可緩解）、成本增加。

---

## 對派哥現有工作流的關係

派哥現在的分工：Claude Code（架構/決策）+ Codex（實作）→ 已有分工，接近 Fusion 的精神。

要做到更完整的 Fusion：
```
Claude 寫初稿
    ↓
Codex 審（Panel）
    ↓
Claude 綜合（Judge）
```
→ 這就是 `/code-duo` skill 的概念，已有雛形。

---

## 工具與環境

- **opencode-go**：OpenRouter 提供的多模型 API 閘道
- **opencode CLI**：類似 Claude Code 的 AI coding 工具，支援多模型
- **DRACO Benchmark**：評測 Agent 能力的標準，arXiv:2602.11685

→ 相關筆記：[[three-provider-ai-routing-strategy]]、[[ai-coding-team-cld]]
