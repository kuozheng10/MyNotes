---
tags: [context-compression, token-reduction, claude-code, mcp, ai-agent, proxy]
source: https://github.com/chopratejas/headroom
date: 2026-06-20
stars: 38747
---

# Headroom — AI Agent 的 Context 壓縮層

> 60–95% fewer tokens, same answers.
> 壓縮 tool output、logs、RAG chunks、files、對話歷史，送進 LLM 前先縮水。

## 核心價值

| 模式 | 用法 | 適合場景 |
|------|------|---------|
| **wrap（包 agent）** | `headroom wrap claude` | 最快上手，不改任何 code |
| **proxy（代理）** | `headroom proxy --port 8787` | 任何語言，zero code change |
| **library** | `from headroom import compress` | 嵌入自己的 app |
| **MCP server** | `headroom mcp install` | Claude Desktop / MCP 生態 |

## 實際壓縮數據

| 工作類型 | Before | After | 省了 |
|---------|-------:|------:|-----:|
| Code search (100 results) | 17,765 | 1,408 | **92%** |
| SRE incident debug | 65,694 | 5,118 | **92%** |
| GitHub issue triage | 54,174 | 14,761 | **73%** |
| Codebase exploration | 78,502 | 41,254 | **47%** |

準確率驗證：GSM8K、TruthfulQA、SQuAD v2 均持平（±0%）。

## 壓縮引擎架構

```
Tool outputs / logs / RAG chunks / files
    ↓
ContentRouter → 依內容類型路由
  ├── SmartCrusher   (JSON)
  ├── CodeCompressor (AST)
  └── Kompress-base  (text, HuggingFace model)
    ↓
CacheAligner → 穩定 prefix，讓 provider KV cache 命中
    ↓
CCR (Cached Content Retrieval) → 原件 local cache，LLM 可按需取回
```

## Output Token 也能壓

不只壓輸入，也能壓**輸出**（Opus output 比 input 貴 5x）：

```bash
export HEADROOM_OUTPUT_SHAPER=1
headroom proxy --port 8787
```

- **Verbosity steering** — 在 system prompt 尾端加「精簡回覆」指示（不破壞 prompt cache）
- **Effort routing** — tool result resume 時降低 thinking effort；新問題/錯誤維持原力

自動學習適合你的簡潔程度：
```bash
headroom learn --verbosity          # 預覽
headroom learn --verbosity --apply  # 套用
```

## headroom learn — 自動更新 CLAUDE.md

```bash
headroom learn          # 掃 failed sessions，寫 corrections 到 CLAUDE.md / AGENTS.md
```

讓 agent 自動從失敗中學習，補強 system instructions。

## 快速安裝

```bash
pip install "headroom-ai[all]"   # Python 3.10+
headroom wrap claude              # 最快路徑
headroom perf                     # 看省了多少
```

## 跨 Agent Memory

同一個 memory store 在 Claude Code / Codex / Gemini 間共享，自動去重。

## 對派哥的評估

**高度相關**，理由：

1. 派哥大量使用 Claude Code，長 session 是常態 → context compression 直接降成本
2. `headroom wrap claude` 一行搞定，不動任何 code
3. Output shaper 對 Opus 特別有感（output 費是 input 5x）
4. `headroom learn` 能自動從 session 學習 → 補 CLAUDE.md，跟派哥的 GBrain 理念一致
5. MCP 模式可整進現有 MCP 工作流

**注意事項**：
- 本地運行（data stays local），不怕隱私問題
- CCR reversible：原件 cache 在 local，LLM 需要時可取回，不會遺失資訊
- Stars 38k，熱度高，社群活躍

## 是否包成 skill？

建議：**可包，但優先級中等**。
- 安裝路徑夠簡單，手動做一次即可
- 若要整進 `headroom wrap claude` + `HEADROOM_OUTPUT_SHAPER=1` 的標準啟動流程，可建 `~/bin/start-claude-headroom.sh`
- 未來若啟用 `headroom learn --apply`，再建 skill 做自動化更值得
