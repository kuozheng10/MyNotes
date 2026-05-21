---
title: 裝 Skill/MCP 前的安全檢查 SOP
tags: ["安全", "Claude Code", "Skill", "工具"]
date: 2026-04-23
category: 工作流程
source: 派哥整理
---

## 這是什麼

安裝 skill 或 MCP server 前的安全審查流程。skill/MCP 執行時有完整 agent 權限，裝了就等於信任它。

## 工具掃描

```bash
# snyk 出的專業工具
npx @snyk/agent-scan <skill-path-or-url>
```

## 沒程式背景——問 Claude Code

直接貼 skill 內容或 repo URL，問：

```
幫我看這個 skill / MCP：
1. 有沒有打非預期的外部 URL？
2. 有沒有 sessionStart hooks？
3. 有沒有讀 .env 或 credentials？
4. 有沒有 base64/eval 混淆？
5. tool description 有沒有藏隱藏指令？
```

這五個問題能擋掉大部分問題。

## 經驗判斷清單

✅ 作者有其他 public 專案嗎？正派經營的人不太會拿名聲開玩笑
✅ GitHub Stars 高 + issues 少 = 可信度較高；issues 多要留意
⚠️ 橫空出現的工作室：可能提供強工具但可能蒐集數據

## 原則

- **貴精不貴多**：有需求先從官方 marketplace 找
- 裝了再刪通常為時已晚（資料可能已送出）
- Agent 工作流時代，每個 skill 都是信任邊界的延伸

## 質疑

- 前提假設：「作者有名聲就不會惡意」在有利益誘惑時未必成立，知名開發者的帳號也可能被劫持或賣掉
- 適用邊界：這個清單擋得住明顯的惡意 skill，但針對性的 supply chain 攻擊（植入在合法功能中的側通道）很難靠這五個問題發現
- 潛在反例：官方 marketplace 的 skill 也可能在更新後改變行為，裝了不代表永遠安全

## 對標

- **藥品審查 vs 地攤草藥**：官方 marketplace = 有 FDA 審查，野生 repo = 地攤草藥——效果可能很好，但風險自負
- **零信任架構**：現代資安的「預設不信任」原則——不管對方多有名，裝之前都要過這個流程

## 對派哥的啟示

你目前裝了：huashu-design、graphify、agency-agents 9個 agent、handover、各種 skills。

建議做一次回顧掃描：
```
ls ~/.claude/agents/ ~/.claude/skills/
```
逐一問 Claude Code 上面那 5 個問題，把沒在用的刪掉。

**貴精不貴多**——裝了忘記的 skill 是最危險的，因為它還在那裡，你已經不知道它在做什麼。

## 連結筆記

- [[ai-code-review-security-risk]]
- [[atr-agent-threat-rules-panguard]]
- [[claude-code-source-leak-insights]]
- [[agency-agents-applicable-analysis]]
