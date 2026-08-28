---
tags: [claude-code, skill, plugin, marketplace, anthropic, eli5, ecosystem]
source: 工程師米奇 FB 貼文（2026-08-25）
url: https://www.facebook.com/share/1CmSFxJrGm/
references:
  - Thariq (@trq212) 推文 https://x.com/trq212/status/2090884854590382515
  - github.com/anthropics/claude-plugins-community/eli5
date: 2026-08-28
---

# ELI5 plugin 爆紅 — 重點不是 skill，是官方 plugin marketplace 成形

> 「最近 Claude Code 社群裡最火的東西不是新模型，是 #ELI5。」
> ELI5 的 SKILL.md 只有 10 行，真正值得看的是它背後的 pattern。

---

## ELI5 是什麼

Explain Like I'm 5 —— 把任何主題用「大圖 + 少字」的 HTML 視覺化方式解釋。
Claude 產出一個 HTML artifact，畫一張圖給你看，而不是寫一段文字。

Thariq（Claude Code 創造者）推薦，推文超過 **6.8 萬觀看**。是 Anthropic 內部工程師最近常用的技巧。

**用法：**

| 指令 | 場景 |
|------|------|
| `/eli5 什麼是 database index` | 學新概念 |
| `/eli5 這個模組怎麼運作` | 讀 code |
| `/eli5 我們為什麼要做這個權衡` | 決策說明 |
| `/eli5 這次事件是什麼原因造成的` | 事後檢討 |

**安裝：**

```bash
# 方法 A：Claude Code plugin 目錄搜 eli5 直接裝
claude plugin marketplace add anthropics/claude-plugins-community
claude plugin install eli5@claude-community
```

或從官方社群 repo：`github.com/anthropics/claude-plugins-community/eli5`

---

## 真正的重點：官方 plugin community marketplace

Anthropic 建了官方的 `anthropics/claude-plugins-community` marketplace：

1. 社群開發者提交 plugin
2. 通過審核後出現在 Claude Code 內建目錄
3. 使用者在 app 內搜尋就能安裝

**這跟 VS Code extension marketplace、npm、App Store 是同一個模式。** 一旦 marketplace 成形，生態系自我加速：
越多 plugin → 越多人用 Claude Code → 越多人做 plugin。

---

## Skills 生態系的演進三階段

| 階段 | 樣貌 | 代表 |
|------|------|------|
| **早期** | 每個人自己寫 CLAUDE.md / chatmode.md | 派哥自己的全域規範 |
| **中期** | 有人把 skill 打包成可安裝模組 | Emil Kowalski、Cloudflare |
| **現在** | Anthropic 開官方 marketplace，統一提交/安裝流程 | `claude-plugins-community` |

**對照 Boris AI Adoption Steps：**

- Step 1-2（個人使用）：自己寫 prompt 跟 skill
- Step 3-4（團隊 / 企業使用）：需要標準化 skill 格式 + 可搜尋目錄 + 版本控制

Marketplace 就是讓整個生態從「個人手工」走向「可規模化」的基礎設施。

---

## 對派哥的意義

- **可以直接裝 ELI5 來用**：解釋自動化流程給老婆看、事後檢討 cc_processor 出錯原因、學新的投資 / 技術概念，都適合丟 `/eli5`
- **marketplace 值得定期逛**：以前找 skill 要到處看推特 / GitHub，現在 `claude plugin marketplace` 一個指令。派哥現有的痛點（例如某個常做的手動流程）可能已經有人做成 plugin
- **自己的 skill 有機會標準化提交**：save-sop、handover、graphify 這些自製 skill，如果通用性夠，未來可考慮包成 community plugin

---

## 相關筆記

- [[anthropic-skill-three-layers-2026-06]] — Skill 三層架構（描述 / 指令 / 工具），ELI5 就是第三層做得極簡的例子
- [[claude-code-setup-plugin-2026-06]] — 官方 setup 外掛，幫你找出該建哪些 skill / hook
- [[emil-kowalski-design-eng-skills-2026-07]] — 中期階段「有人把 skill 打包」的代表案例
- [[boris-cherny-cleaner-maintainer-2026-07]] — Boris AI Adoption Steps 出處
- [[ecpay-api-skill-vendor-pattern-2026-08]] — 廠商把 skill 當對外產品介面，marketplace 成形後的延伸玩法
- [[claude-skill-social-post]] — Claude Code skill 社群分享
- [[hung-yi-lee-skill-2026-08]] — 同系列貼文，把一位老師的知識體系整包做成 skill 的範例（voidful）
