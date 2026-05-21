---
title: "Caveman — Claude Code 省 Token 壓縮回覆 Skill"
url: "https://github.com/JuliusBrussee/caveman"
tags: [claude-code, skill, token, cost, optimization, prompt]
date: 2026-04-06
category: 03.科技工具
source: Telegram 分享
---

## 摘要

> Claude Code skill，讓 Claude 用「洞穴人語言」回覆，省掉廢話、語氣詞、客套句。
> 平均省 65% token，code block 和技術名詞保持原樣。
> ⭐ 2.5K stars

## 三種模式

| 模式 | 說明 | 省幅 |
|------|------|------|
| Lite | 專業但簡潔，適合正式場合 | 22–40% |
| Full | 標準洞穴人（預設） | ~65% |
| Ultra | 最大壓縮 | 最高 87% |

## 安裝

```bash
npx skills add JuliusBrussee/caveman
```

## 使用

```
/caveman          → 開啟（Full 模式）
/caveman lite     → 輕量版
/caveman ultra    → 最大壓縮
normal mode       → 關閉
```

## 評估：對派哥有用嗎？

**有用。** 派哥偏好「簡短直接的回答，不要廢話」，Caveman 就是把這件事自動化。
特別適合：
- 日常 Telegram 聊天（Ultra 或 Full）
- 做 code review / 研究時（Full）
- 正式 spec 或文件（Lite 或關閉）

**要不要包成 skill？** 它本身就是 skill，直接裝就好，不需要再包。

## 相關筆記

- [[agent-prompt-token-cost]] — Agent Prompt 省 Token 手法（主動端）
- [[boris-15-claude-code-tips]] — Claude Code 高頻技巧
