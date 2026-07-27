---
title: Matt Pocock skills repo 實戰——從想法到交付的完整SDD流程
tags: [claude-code, agent-skills, sdd, ddd, tdd, code-review, matt-pocock]
date: 2026-07-27
category: AI工具
source: 派哥貼文分享 + YouTube影片 https://youtu.be/M6mYodf0dJM
related: matt-pocock-ai-code-is-not-cheap, agent-skill-creator-auto-generate-skills, tootiredbear-agent-skills-intro
---

## 這是什麼

Matt Pocock（16.2萬星、750萬下載量的技能儲存庫`mattpocock/skills`）介紹自己這套Claude Code skill組合的核心使用流程「Idea to Ship」。派哥丟這篇時是分享自己把SDD skill從Spectra換成這套的心得，這篇筆記整理影片本身講的完整流程 + 對照上方已存的Matt Pocock哲學筆記。

## 六個核心skill

| Skill | 作用 |
|-------|------|
| `/ask Matt` | 代表Matt本人，回答「怎麼開始/該用什麼流程」 |
| `/grill with docs` | 流程起點，「面試」使用者釐清模糊想法，做Domain Modeling(定義詞彙在這個context裡的意思)，記錄進`context.md`+ADRs |
| `/prototype` | 需要可執行答案時用(影片未詳細演示) |
| `/to spec` | 把grill討論(範例中46.1k tokens)壓縮成詳細spec文件，發布到Issue Tracker，定義「最終產品長怎樣」 |
| `/to tickets` | 把spec拆解成多個小任務(範例：拆成11個sub-issues)，每個ticket大小設計為單一context window可完成 |
| `/implement` | 執行實作，自動觸發code review(由**子代理**執行，避免主代理審查自己剛寫的code有偏見) |

## 完整流程

1. 前置：裝Node.js，執行`NPX skills at latest add mattpocock/skills`(Vercel CLI安裝器)
2. 安裝時選：技能範圍(project團隊共用 / global個人用)、安裝方式(推薦symlink)、要用哪個agent(Claude Code需額外勾選)
3. 專案設定：`/set up Mac Pocock skills`，選Issue Tracker(GitHub/local markdown/Jira/Linear都支援)、Domain Documentation用single context(99%情境夠用)
4. 開發：`/grill with docs`釐清想法 → 若工作量大需跨多session：`/to spec`→`/to tickets`；若單session能做完直接`/implement this`
5. 實作前建議清context，`/implement this @tickets`執行
6. Code Review自動跑，兩軸：對照原始spec驗收標準 + 符合專案coding standard(沒有的話套Fowler 12個code smell)
7. 審查過 → 自動commit到當前分支

## 關鍵設計理念

- **使用者主動呼叫**，不是自動塞進context(所有skill描述加起來只佔約660 tokens，負擔很輕)
- **140k tokens是LLM的「smart zone」**：超過容易attention degradation跟幻覺，所以整套流程設計成把大任務拆到能在單一context window內完成
- **子代理做code review**：避免「AI審查自己剛寫的code」的偏見問題
- **Agent中立、Issue Tracker中立**：不綁定特定工具，Claude Code/Cursor/Codex都能用，Issue Tracker可以是GitHub/Jira/Linear/純local markdown

## 派哥從Spectra換過來的理由(原文重點)

1. Spectra留下的spec文件會跟code不一致，容易讓Claude誤解——這套改成**把user story跟測試情境直接寫在單元測試註解裡，code本身就是single source of truth**，不會有兩份文件互相打架的問題
2. Spectra自己用還行，但沒辦法擴充成團隊協作模式；這套換手給新工程師/團隊協作比較容易水平擴展

## 跟已存筆記的關係

這篇是[[matt-pocock-ai-code-is-not-cheap]]那篇哲學論述的**具體實作版**——那篇講「AI越強，好架構越重要」的抽象原則，這篇是Matt自己把原則落地成的六個skill的實際操作手冊。特別是：
- 那篇提到「grill me已在知識庫，這篇說明了它存在的理由」——這裡的`/grill with docs`正是同一個概念的正式產品化版本，多了「輸出到context.md+ADRs」這個具體落地動作
- 那篇的「Ubiquitous Language：CLAUDE.md/skill文件=你和Claude的共用詞彙」——這裡的Domain Modeling(定義詞彙在context裡的意思)是同一個概念的操作步驟

## 對派哥「要不要包成skill」的建議

**不建議直接npx裝一整包**，理由：

1. 派哥現在的Claude Code環境**已經有一組結構高度相似的skill**：`spec-driven-development`(≈to spec)、`planning-and-task-breakdown`(≈to tickets)、`incremental-implementation`(≈implement)、`code-review-and-quality`(≈code review)、`idea-refine`(≈grill with docs)——生態位幾乎一一對應，直接疊裝一整包容易跟現有skill重疊、互相打架，觸發「叫哪個」的混淆
2. 真正值得**單獨借鏡、補進現有skill**的兩個具體點子：
   - **測試即spec，寫進單元測試註解，不要留獨立spec文件跟code分裂**——這條可以直接補進現有`test-driven-development`或`spec-driven-development`skill的說明裡
   - **Code review用子代理執行，不要用主代理審查自己剛寫的code**——這條可以檢查現有`code-review-and-quality`skill有沒有已經這樣做，沒有的話值得補
3. `context.md`+ADRs+Domain Modeling這套如果派哥自己沒有正式的多人協作codebase(目前MyClaude是個人自動化腳本為主)，價值沒那麼高——這套設計是為了**團隊協作水平擴展**，派哥自己一人維護的話，現有CLAUDE.md/memory系統已經在做類似的事

如果要分享給「有在應用AI+軟體開發流程的朋友」(原文的推薦對象)，這套完整、成熟、有真實使用者驗證(16萬星)，值得推薦；但對派哥自己的Claude Code環境，比較好的做法是「偷點子補進現有skill」而不是整包重裝。

## 相關筆記
- [[matt-pocock-ai-code-is-not-cheap]] — 同作者的架構哲學論述，這篇是具體落地實作版
- [[agent-skill-creator-auto-generate-skills]] — 另一套skill自動產生工具，跟這篇的「模組化skill」設計理念可對照
