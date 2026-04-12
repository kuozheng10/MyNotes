---
title: Oh My OpenAgent — 多模型 Agent 協作框架，反鎖定哲學
tags: [Agent, 多模型, OpenCode, 自動化, 開發工具, 架構設計, AI編程]
date: 2026-04-12
category: AI工具
source: https://github.com/code-yeongyu/oh-my-openagent
---

## 這是什麼

建在 OpenCode 上的多 Agent 協作框架（50.7k stars）。核心理念：**反鎖定（Anti-Vendor Lock-in）**，不強制你只用 Claude 或 GPT，根據任務類型自動路由到最合適的模型。

---

## 核心架構：Discipline Agents（專業分工）

| Agent | 模型 | 職責 |
|-------|------|------|
| Sisyphus | Claude Opus 4.6 / Kimi K2.5 | 主協調者：規劃、分派任務 |
| Hephaestus | GPT-5.4 | 深度執行：複雜多步驟任務 |
| Prometheus | — | 策略規劃：執行前先訪談確認意圖 |
| Oracle | — | 架構分析 + 除錯 |
| Librarian | — | 文件查詢 + code search |
| Explore | — | 快速 codebase 模式匹配 |

---

## 主要指令

```bash
ultrawork / ulw        # 一鍵啟動所有 agent 直到任務完成
ulw-loop               # 自我循環，直到 100% 完成（Ralph Loop）
/start-work            # Prometheus 訪談模式（先確認意圖再執行）
/init-deep             # 自動生成 AGENTS.md 層級文件
```

---

## 技術亮點

### Hash-Anchored Edit（Hashline）
- 用內容 hash（`LINE#ID`）而非行號定位修改點
- 解決 LLM 改 code 時「行號漂移」的老問題
- 確認 code 沒變才套用修改，防止 stale-line 錯誤

### 任務分類路由（Category-Based Delegation）

| 類別 | 路由 |
|------|------|
| `visual-engineering` | 前端/UI 設計 |
| `deep` | 自主研究 + 複雜執行 |
| `quick` | 單檔修改、小改動 |
| `ultrabrain` | 硬邏輯/架構（GPT-5.4 xhigh） |

不需手動選模型，系統自動分類。

### 內建 MCPs
- Exa：網路搜尋
- Context7：官方文件查詢
- Grep.app：GitHub code search

### 其他設計
- Background Agents：5+ 個專家平行執行，各自精簡 context window
- Todo Enforcer：防止 agent 閒置
- IntentGate：執行前分析真實意圖

---

## vs. 其他工具

| 工具 | 差異 |
|------|------|
| Claude Code | 單模型，Anthropic 生態系，OMO 可呼叫 Claude 但不鎖定 |
| Cursor | 封閉 IDE，OMO 開源無鎖定 |
| Codex | 只是 API，OMO 是完整協作框架 |

---

## 評估：對派哥有沒有用？

值得關注，但**目前不急**：

優點：
- 50.7k stars，社群大，有真實大規模使用案例（Google、Microsoft）
- 多模型路由概念很好：便宜模型跑小任務，貴模型跑硬邏輯
- Hash-anchored edit 解決真實痛點
- 一鍵 `ultrawork` 哲學和派哥想法一致

限制：
- 建在 OpenCode 上，不是 Claude Code（要切換工具）
- 目前派哥已有 Claude Code + Codex 分工，功能重疊
- v0 早期架構，穩定性待觀察

**建議觀察方向**：
- 如果 Claude Code 某天讓你很煩或太貴，OMO 是最強的替代候選
- Hash-Anchored Edit 這個概念值得借鑒到自己的工作流
- Discipline Agent 分工模式可參考，設計 Hermes 多 Bot 分工時有用
