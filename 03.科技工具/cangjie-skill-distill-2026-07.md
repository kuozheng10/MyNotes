---
tags: [ai-coding, claude-code, skill, knowledge-management, open-source, mit-license]
source: https://github.com/kangarooking/cangjie-skill
date: 2026-07-10
category: 03.科技工具
---

# 倉頡.Skill（cangjie-skill）：把書/長影片/播客蒸餾成可調用的 AI Skill

> **一句話**：讀完、看完、聽完之後，帶走一套 AI agent 真的能調用的方法論，而不是一篇躺在收藏夾裡積灰的摘要。

## 解決的痛點

- 看了很多書/長影片/播客但用不起來——知識停在「看過/聽過」層面，無法在真實決策中被調用
- 摘要、筆記、字幕整理只是壓縮，不是結構化復用——看完還是不知道「什麼時候該用什麼」
- 高價值內容裡真正值得變成工具的只有一小部分，需要嚴格篩選，不是照單全收
- 現有讀書法/筆記法都是給人看的，不是給 agent 用的

## 核心方法：RIA-TV++ 七階段流水線

| 階段 | 內容 |
|------|------|
| 1. 整體理解 | Mortimer Adler 分析閱讀法（結構/解釋/批判/應用四步）→ 產出 `BOOK_OVERVIEW.md` |
| 2. 並行提取 | 5 個專項提取器同時跑：框架、原則、案例、反例、術語 |
| 3. 三重驗證篩選 | 每個候選需通過：①原文至少 2 處跨域佐證 ②能回答書中未明說的新問題（預測力）③不是常識（獨特性）。**通過率通常只有 25-50%** |
| 4. RIA++ 構造 | R原文引用 / I自己重寫 / A1書中案例 / A2未來觸發場景 / E可執行步驟 / B邊界盲點 |
| 5. Zettelkasten 鏈接 | 找 skill 間依賴/對比/組合關係，生成 `INDEX.md` |
| 6. 壓力測試 | 每個 skill 設計含誘餌題的測試案例（含跨 skill 混淆測試），沒過回爐重做 |
| 7. 交付 | 產出 `DIGEST.md` 精華長文 + 安裝到 Claude Code / Cursor 的 skills 目錄 |

名稱拆解：RIA（趙周《這樣讀書就夠了》便籤拆書法）+ TV（Triple Verification 三重驗證）+ ++（E執行步驟 + B邊界，面向 agent 執行的擴展）

**不只適用於書**：只要內容有字幕/轉寫文本（長影片、播客、訪談、演講、課程），都能蒸餾。建議搭配作者另一個 skill [video-downloader](https://github.com/kangarooking/kangarooking-skills/tree/main/video-downloader) 先下載字幕/轉寫，再交給 cangjie-skill 做方法論抽取。

## 已生成的 skill packs（節錄，共 20+ 個倉庫）

| 倉庫 | 來源 | Skills 數 |
|------|------|-----------|
| buffett-letters-skill | 巴菲特致股東的信（1957-2023） | 20 |
| poor-charlies-almanack-skill | 《窮查理寶典》 | 12 |
| duan-yongping-skill | 段永平投資問答錄 | 15 |
| first-principles-skill | 《第一性原理》 | 10 |
| influence-skill | 《影響力》 | 12 |
| contagious-skill | 《瘋傳》 | 15 |
| ai-for-everyone-skill | 吳恩達《AI for Everyone》影片課程 | 25 |
| loop-engineering-skill | Loop Engineering 長影片合集 | 8 |

外部貢獻來源：book2startup（精益創業/孫子兵法/莊子/易經）、book2skill（纏論/茶經）

## 生態定位

三個相關 skill 咬合：
- [nuwa-skill](https://github.com/alchaincyf/nuwa-skill) — 蒸餾**人**（思維方式、表達 DNA，例：馬斯克 skill、巴菲特 skill）
- **cangjie-skill** — 蒸餾**內容**（書/長影片/播客的方法論、框架、原則）
- [darwin-skill](https://github.com/alchaincyf/darwin-skill) — 讓這些 skill 持續**進化**

作者：袋鼠帝 kangarooking，公眾號「袋鼠帝 AI 客栈」主理人。專案 MIT license，2270+ stars（截至 2026-07-10）。

## 對派哥的參考價值

- 跟 [[caveman-token-saving-skill-2026-07]] 一樣是「開源 skill 生態」的一環，可以看這類專案怎麼組織 SKILL.md / 多階段驗證的做法
- MyNotes 目前是「筆記留存」型知識庫，cangjie-skill 走的是「筆記→可執行 skill」的下一步，跟派哥「跑 SOP」流程（研究→評估→存筆記→**建議包成 skill**）的最後一步概念很接近，值得參考它的三重驗證篩選邏輯（不是每篇筆記都值得包成 skill，要有跨域佐證+預測力+獨特性）
- 若之後想把某本書/某個長 YouTube 影片系統性蒸餾成派哥自己可調用的 skill（而不只是存一篇 MD 筆記），可以直接拿這個工具跑

## 來源二：一人公司研究所 FB 短片

FB 短片連結（`facebook.com/share/v/195AV7QyCu`）本身讀不到完整影片內容——Facebook 擋在登入牆後面，Claude 的抓取工具（WebFetch / Playwright）都只能看到貼文說明文字，看不到影片畫面或字幕。貼文說明文字：

> 倉頡.Skill 這個開源工具，讓你可以蒸餾任何影片。所謂蒸餾，就是把一部長影片的精華濃萃出來。以前這件事要靠人工看完、做筆記、再整理，現在 AI 直接幫你搞定。

發布帳號：一人公司研究所。內容應該就是在介紹上面這個 cangjie-skill 工具，跟 GitHub 連結是同一件事，只是換了個宣傳角度。
