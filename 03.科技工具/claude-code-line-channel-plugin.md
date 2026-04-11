---
title: Claude Code LINE Channel Plugin — 透過 LINE 遠端操控 Claude Code
tags: [claude-code, line, plugin, 遠端操控, 行動化]
date: 2026-04-11
category: AI工具
source: https://chennaicheng.notion.site/Claude-Code-LINE-Channel-Plugin-33f2d00e283a816c853ddd813c1432ea
---

## 這是什麼

開源 Plugin，把 Claude Code 整合進 **LINE**。
透過 LINE 聊天室遠端下指令給 Claude Code，實現跨裝置 AI 輔助開發。

---

## 主要功能

- **遠端操控**：在 LINE 輸入自然語言，遙控 Claude Code 執行分析/修復/生成
- **即時通知**：耗時任務完成後透過 LINE 推送結果
- **權限管控**：綁定特定 LINE User ID，只有授權用戶能操作
- **上下文同步**：LINE 與本地終端機之間的對話上下文一致

---

## 安裝方式

```bash
npm install -g claude-code-line-plugin
claude-code-line init
```

需要：
1. LINE Developers Console 建立 Messaging API Channel
2. 取得 `Channel Secret` + `Channel Access Token`
3. 設定 Webhook

---

## vs Telegram Plugin（派哥現在用的）

| | LINE Plugin | Telegram Plugin |
|--|------------|-----------------|
| 台灣普及度 | 極高 | 較低 |
| 設定難度 | 需 LINE Dev Console | 較簡單 |
| 功能 | 類似 | 類似 |
| 派哥現狀 | 未裝 | 已用，穩定 |

---

## 對派哥的評估

**結論：不需要換，維持 Telegram。**

理由：
- Telegram Plugin 已穩定運作，TG 有加密 + Bot API 比 LINE 彈性
- LINE Plugin 多一層 Developers Console 設定，維護成本高
- 如果家人/同事只用 LINE 不用 TG，才值得考慮

---

## 連結筆記
- [[claude-code-powerup-guide]] — Claude Code 10 大功能
- [[claude-notebooklm-mcp-5scenarios]] — 行動化：手機下指令電腦執行
