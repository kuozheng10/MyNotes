---
title: HTML Anything：徵用本機 AI CLI 把文字變成可交付 HTML 的開源編輯器
tags: [ai, tool, 設計, Claude Code, 開源, HTML, 簡報, 卡片]
source: https://github.com/nexu-io/html-anything
fb_source: https://www.facebook.com/share/184eTvhCi7/（陳盟升 2026-08-28）
date: 2026-08-30
category: AI工具
---

## 這是什麼

**Open Design 團隊（40k★）**出的新工具，聚焦「agent 時代的 HTML 編輯器」。
丟進任何輸入（Markdown / CSV / Excel / JSON / SQL / 純筆記）→ 本機的 AI agent 幾秒內產出
**可直接交付的單檔 HTML** → 一鍵送到微信 / X / 知乎 / 或下載 .html / .png。

核心主張：Markdown 是寫作中間態，**HTML 才是給人看的最終形態**。
（依據：Anthropic Claude Code 團隊宣布內部文件不再寫 Markdown、改交 HTML）

| Markdown | HTML |
|---|---|
| 對寫的人友善 | 對讀的人友善 |
| 排版被 renderer 綁死 | 排版自己決定 |
| 截圖貼推特很醜 | 本身就像設計過的圖 |
| 貼微信/知乎要重排 | 一鍵轉格式 |

## 關鍵特色

- **BYOA / 零 API Key**：開機掃 PATH，自動偵測你已登入的 9 個 coding-agent CLI
  （Claude Code · Cursor Agent · Codex · Gemini CLI · GitHub Copilot CLI · OpenCode · Qwen Coder · Aider · IBM Bob），
  直接複用現有訂閱 session，邊際成本 $0。掃描含 `~/.local/bin`、`~/.bun/bin`、`/opt/homebrew/bin`、`~/.npm-global/bin`
  這些 GUI 啟動的 Node 常漏掉的目錄。
- **75 個 skill 模板 × 9 種產出面向**：雜誌長文 / keynote deck（20 種）/ 履歷 / 海報 /
  小紅書卡 / 推特卡 / 網頁原型 / 資料報告 / Hyperframes 影片分鏡。
  每個 skill 是一個資料夾，照 Claude Code `SKILL.md` 慣例 + 擴充 frontmatter（mode·scenario·surface·preview·design_system），
  丟進 `next/src/lib/templates/skills/` 重啟就出現在選單。
- **SSE 串流渲染**：agent stdout 的 JSON-line 逐行解析 → 即時 append 進 sandboxed iframe，
  像看它在打字。方向不對可中斷重下 prompt，不用等整份生成完。
- **一鍵匯出（零二次排版）**：
  - 微信 → juice 把 CSS inline 進去，貼上樣式不跑掉
  - X / 微博 / 小紅書 → modern-screenshot 轉 2× PNG → ClipboardItem 直接貼
  - 知乎 → 同上 + 數學式換成 LaTeX 圖片佔位（知乎不 render KaTeX）
  - 下載 .html（單檔內嵌）/ .png（高 DPI）
- **硬約束防 AI slop**（寫死在每個 SKILL.md，紀律來自 huashu-design）：
  CJK 優先字體疊、8px baseline grid、圓角+柔陰影+不用純黑純白、對比 ≥ 4.5、每個互動元素有 :focus、
  **必須用使用者真實資料，禁 lorem ipsum**。
- **sandboxed iframe**：`sandbox="allow-scripts allow-same-origin"`，Tailwind CDN / Google Fonts / inline script 能跑，
  但 cookie / localStorage 隔離在 iframe 自己的 origin，不污染 host。

## 技術/部署

- pnpm workspace：`next/`（Next.js 16 + React 19 + Tailwind v4 + zustand）、`e2e/`（Playwright）
- `pnpm -F @html-anything/next dev` → localhost:3000
- 可部署 Vercel（web 層），但 **agent 永遠留在你的筆電本機**
- Security：`/api/convert` 用最寬鬆權限 spawn 你的 CLI，所以每個 `/api/*` 都有 Host header allowlist
  擋 DNS rebinding（預設只放行 127.0.0.1 / localhost / ::1）
- License：Apache-2.0

## 狀態

早期但可用。核心閉環（偵測 agent → 選 skill → SSE 串流 → sandboxed preview → 一鍵匯出）
對 8 個 CLI 都跑得通。skill 庫和 SKILL.md 硬約束穩定；多模板比較、Hyperframes→mp4 開發中；
瀏覽器擴充、版本 diff、skill marketplace 規劃中。

## 血緣（借用的開源專案）

- `nexu-io/open-design` — agent 偵測層、DESIGN.md schema、SKILL.md 協定（架構直接照搬）
- `alchaincyf/huashu-design` — 反 AI-slop 紀律（Junior-Designer mode + checklist）
- `mdnice/markdown-nice` — juice inline CSS → 微信/知乎貼上 pipeline
- `gcui-art/markdown-to-image` — iframe → 高 DPI PNG
- `op7418/guizang-ppt-skill` — 雜誌墨感 deck（原樣收進 `deck-guizang-editorial`）
- `tw93/kami` — 暖羊皮紙 editorial doc（`doc-kami-parchment`）
- `1weiho/open-slide` — 1920×1080 agent-native canvas（`deck-open-slide-canvas`）
- `heygen-com/hyperframes` + `remotion` — 影片分鏡 schema → 出 .mp4

## 對派哥的用途

- MyNotes 知識整理 → 一鍵做成雜誌風長文 / deck / 小紅書卡分享，不用手刻 CSS
- 複用已登入的 Claude Code 訂閱，不再另外燒 API key
- 跟 [[open-design-claude-design-opensource]] 同團隊、同 BYOA 理念，這個更聚焦「出 HTML 卡片/簡報」
- FB 留言有人說「Gemini 都亂做」→ 這工具的價值就在 SKILL.md 硬約束把模型框住

## 連結筆記

- [[open-design-claude-design-opensource]] — 同團隊，Claude Design 開源替代（偏完整設計工作流）
- [[guizang-ppt-skill]] — 被收進 html-anything 的雜誌風 deck skill
- [[huashu-design-claude-design-reverse]] — 反 AI-slop 紀律的來源
- [[karpathy-html-output-llm-tip]] — 「LLM 直接輸出 HTML」的觀念
- [[open-slide-codex-presentation]] — 被收進 html-anything 的 1920×1080 canvas
- [[agent-skills-standard]] — SKILL.md 安裝與管理規範
