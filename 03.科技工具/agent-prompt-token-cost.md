---
title: "Agent Prompt 中文 Token 爆量問題與省錢手法"
tags: [agent, prompt, token, cost, 中文, system-prompt, optimization]
date: 2026-04-02
category: 03.科技工具
source: OpenClaw 中文社群 Facebook
---

## 核心問題

寫 agent system prompt 用中文，token 消耗是英文的 **2–3 倍**。

**台灣用戶常見雙重傷害：**
- 🔥 System prompt 全中文 → input token 爆量
- 💡 Agent 自動回覆也是中文 → output token 也翻倍
- ⚡ 長對話每輪都在燒，累積超可觀

**實際案例：** 朋友 agent 每天燒 $8 美金，system prompt 3000 字全中文；換成中英混寫後同樣功能，token 砍 40%。

## 推薦做法

| 做法 | 說明 |
|------|------|
| System prompt 核心邏輯寫英文 | 只有面向用戶的部分才用中文 |
| 常用指令抽成短 key | 例如 `REPLY_STYLE` 取代一大段中文描述 |
| 設 token budget alert | 超過就自動通知，防止意外爆量 |

## 為什麼中文更貴

中文每個字通常對應 1–2 個 token（BPE tokenizer 對 CJK 不友好），英文一個常用詞約 1 token。相同語意，中文版 prompt 往往 2–3 倍 token。

## 應用原則

```
# 不好的寫法（純中文）
你是一個助手，請用繁體中文回覆用戶的問題，
保持友善且專業的語氣，並在每次回覆結束時確認用戶是否需要更多協助。

# 好的寫法（英文邏輯 + 中文輸出指令）
You are a helpful assistant.
- Respond in Traditional Chinese
- Tone: friendly and professional
- End each reply by asking if user needs more help
```

## 相關

- [[boris-15-claude-code-tips]]
- [[claude-hidden-combo]]
