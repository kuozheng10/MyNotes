# OfficeCLI — 讓 AI Agent 直接讀寫 Word/Excel/PowerPoint

> 來源：粉專分享文章 + 實地查證 GitHub repo
> 連結：https://github.com/iOfficeAI/OfficeCLI
> 儲存日期：2026-07-16

---

## 這是什麼

開源 CLI 工具，讓 AI agent（Claude Code、Cursor、VSCode Copilot 等）不用裝 Office，就能直接讀取、編輯、自動化 `.docx`/`.xlsx`/`.pptx`。單一執行檔，macOS/Linux/Windows 都能跑，內建 MCP server（`officecli mcp claude` 一行指令就能註冊進 Claude Code）。

## 查證結果（不是只信原文章行銷詞）

原文章說「14000+ stars」，實際查 repo 現在是 **18.2k stars**（比文章講的還多，數字沒灌水，只是文章寫的時候還沒漲到這麼多）。

| 查證項目 | 結果 |
|---|---|
| 授權 | Apache 2.0，真開源 |
| 維護狀態 | 5,795 commits、130 releases，最新版 v1.0.136（2026-07-14），非常活躍 |
| Open issues | 28 個，數量正常，不是棄坑專案 |
| Hacker News | 真的上過 HN 討論（news.ycombinator.com/item?id=48807225），不是自嗨行銷 |
| MCP 整合 | 內建，`officecli mcp claude\|cursor\|vscode\|lmstudio` 一行指令自動裝 skill file |

## 「真的讀得到、讀得好嗎」——誠實結論

**讀得到**：架構紮實，三層設計（高階 `view`、DOM層級 `get/query/set`、原始 XML `raw`），不是半調子的文字抽取。特別的是它有「渲染引擎」——可以把文件轉成 HTML/PNG 截圖讓 agent「看到」文件長怎樣（標題有沒有溢出、圖形有沒有疊在一起），這是很多同類工具沒做的，等於幫 agent 補上「寫完看不到結果」的盲點。

**讀得好嗎**：⚠️ 官方文件**沒有提供任何量化準確度數據**（沒有測試集、沒有錯誤率），對複雜表格合併儲存格、巢狀公式、疊層格式的準確度，只有 before/after 截圖當範例，沒有結構化驗證。所以「高保真」是官方說法，不是有第三方數據佐證的事實。

## 適合派哥的地方

- MyClaude 這邊常要處理 Excel 報表/PDF帳單，如果之後有需要「產生」Excel/Word報告（不只是讀取），這工具內建 350+ Excel函式（寫入自動運算）、樞紐分析表、圖表生成，可能比現有土炮方案好用
- 有 MCP 整合，理論上可以直接掛進 Claude Code 用，不用另外寫 wrapper

## 建議

工具本身可信（真開源、真活躍、真的上過HN），但「讀得好不好」這個核心賣點缺乏第三方驗證，屬於「值得先丟進沙盒試跑一次真實檔案」等級，還不到「直接換掉現有流程」的程度。

**下一步**：如果要驗證，建議拿一份 MyClaude 現有的 Excel/Word 檔案本地跑一次 `officecli view` 實測，看解析結果對不對，比空想準。
