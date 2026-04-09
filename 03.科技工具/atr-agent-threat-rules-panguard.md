---
title: ATR + PanGuard — 台灣製造的 AI Agent 資安規則層
tags: [資安, MCP, Agent, 工具, 開源, prompt-injection]
date: 2026-04-09
category: AI工具
source: 社群分享（Facebook）
---

## 這是什麼

台灣開發者自製的 **ATR（Agent Threat Rules）**：專門針對 AI Agent / MCP 工具的偵測規則集，已被 Cisco AI Defense 官方採用（PR #79）。

**PanGuard** = 掃描工具，基於 ATR 規則，可掃描本機安裝的 MCP skills。

---

## 為什麼需要

- `npm install` 一個 MCP skill 就能拿到：終端機、檔案系統、API keys、SSH keys 的權限
- 完全沒有 sandbox、沒有 review
- 傳統資安有 Snort / Sigma / YARA，但 AI Agent 沒有對應的偵測層

---

## ATR 規則特點

| 特點 | 說明 |
|------|------|
| 格式 | YAML（偵測什麼、嚴重程度、建議處理） |
| 執行方式 | AI 理解攻擊模式 → 結晶為 regex → 毫秒級掃描 |
| 涵蓋範圍 | OWASP Agentic Top 10，tool poisoning、prompt injection、多代理攻擊 |
| Threat Cloud | 社群匿名上傳 hash → 確認後自動產生新規則 |
| Recall | ~60%（誠實公開限制），Precision 高 |

---

## 快速安裝

```bash
npm install -g @panguard-ai/panguard && pga up
```

掃描目前安裝的 skills，60 秒，支援 24/7 monitoring。

---

## 相關連結

- ATR Repo：https://github.com/Agent-Threat-Rule/agent-threat-rules
- PanGuard：https://panguard.ai
- Cisco PR：https://github.com/cisco-ai-defense/skill-scanner/pull/79

---

## 對派哥的啟示

- **Claude Code / 一蘭 用了很多 MCP tools** → 考慮跑一次 PanGuard 掃描
- 安裝 skill 之前先確認來源（尤其 npm 安裝的）
- ATR 是開源 MIT，可以自己加規則
- SAFE-MCP 基金會（Anthropic + Google + OpenAI + AWS + GitHub + Microsoft）= 未來標準可能從這裡來

---

## 連結筆記
- [[claude-code-source-leak-insights]] — Claude Code 安全性相關
- [[agent-skills-standard]] — Skill 標準化（agentskills.io）
