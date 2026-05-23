---
title: vscode.dev/agents——用瀏覽器遠端連回本機開發（GitHub 版龍蝦方案）
tags: [VSCode, 遠端開發, GitHub Copilot, AI Agent, Claude Code替代]
date: 2026-05-23
category: 科技工具
---

## 這是什麼

VS Code 的雲端遠端開發服務，透過 **VS Code Tunnel** 從任何瀏覽器連回你的本機電腦。

入口：https://vscode.dev/agents

---

## 能做什麼

- 人在外面（公司/咖啡廳/公用電腦）→ 連回家裡的 Mac 開發
- GitHub Copilot 作為 AI Agent 幫你執行任務
- 可開 Terminal 下指令，跟在本機完全一樣
- 支援行動版網頁 → **手機也能寫 Code**

---

## 如何啟用

1. 本機安裝 VS Code
2. 在本機執行 VS Code Tunnel（`code tunnel` 指令）
3. 用瀏覽器開 https://vscode.dev/agents 連回本機

---

## 跟龍蝦（Claude Code）的比較

| | vscode.dev/agents | Claude Code（龍蝦）|
|--|--|--|
| AI | GitHub Copilot | Claude |
| 介面 | VS Code 瀏覽器版 | CLI / Desktop App |
| 遠端存取 | ✅ VS Code Tunnel | ✅ 需自己架（SSH / Tailscale）|
| 手機使用 | ✅ 行動版瀏覽器 | ⚠️ CLI 不友善 |
| 離家工作 | ✅ 內建解法 | 需額外設定 |

本質上是 GitHub 版的龍蝦方案，AI 換成 Copilot，介面換成網頁 VS Code。

---

## 對派哥的評估

- 你主要在 Mac 前工作，Claude Code CLI 是主力
- 如果需要「外出時遠端跑任務」，vscode.dev/agents 是最低阻力的方案
- 不需要換掉現有工作流，偶爾出門用得到時再開 Tunnel

---

## 相關

- [[codex-computer-use-mac]] — 另一個桌面 AI 控制工具
