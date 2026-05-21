---
title: AI Agent 三套比較 — Hermes / OpenAB / OpenClaw
tags: [Agent, Hermes, OpenAB, OpenClaw, AI工具, 系統設計]
date: 2026-04-13
category: AI工具
source: 社群文章（作者不明，轉自 goodarticle）
---

## 核心選擇框架

選哪套 agent，本質是哲學問題：**你怎麼看「AI 該學什麼」**。

| 類型 | 代表 | 一句話 |
|------|------|--------|
| 成長型 | Hermes Agent | 做完任務自動產生可重用 skill |
| 團隊型 | OpenAB | Discord 多人共用 coding agent |
| 記憶型 | OpenClaw | 長期記憶架構，Obsidian + dreaming |

---

## Hermes Agent — 概念美，容易撞牆

- 設計：複雜任務完成後自動產出可重用 skill，越用越強
- 問題：失敗時不換策略，傻傻重試同一面牆，燒 token
- token 問題：2h 輕度使用 400 萬 tokens；Telegram 用量是 CLI 的 2-3 倍
- 優點：skill 分層載入（平常只吃 ~3000 tokens 看清單），可從 OpenClaw 一鍵遷移
- 定位：**成長型**，潛力在，現在還不穩定

→ https://github.com/nousresearch/hermes-agent

---

## OpenAB — 只做一件事，做到最快

**定位與其他兩套完全不同：解的是「多人 ↔ 一個 agent」**，不是一人一 agent。

架構極簡：Discord ↔ OpenAB (Rust) ↔ ACP-compatible CLI（Kiro/Claude Code/Codex/Gemini），全走 stdio JSON-RPC，不開額外 port。

亮點：
- Edit-streaming 每 1.5 秒更新 Discord 訊息，體感極快
- 後端可插拔（換 CLI 只改 config）
- k8s 原生部署，有 Zeabur 一鍵模板
- 台灣開源（Pahud 主導），創辦人哲學：「AI 時代做加法太容易，我們要做減法」

→ https://github.com/openabdev/openab

---

## OpenClaw — 記憶架構最完整

記憶差異化：
- Obsidian vault 存長期記憶
- Crontab + dreaming 每晚自動整理 context
- Linear 串任務進度
- 多 Agent 各司其職

**agent 強不強，取決於餵它的記憶結構好不好。**

---

## 派哥的組合建議

作者自己的做法：OpenClaw 當主力大腦 + OpenAB 給團隊用，兩套互補。

對派哥：
- OpenClaw 已是主力 → 繼續
- OpenAB 值得關注：如果未來有多人協作 coding 需求
- Hermes 現在還不穩，先觀望
