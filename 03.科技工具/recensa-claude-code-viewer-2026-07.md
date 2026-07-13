# Recensa — Claude Code 會話記錄本地查閱器（開源）

> 來源：GitHub https://github.com/S40911120/recensa
> 作者：Justin Chen (S40911120)
> 儲存日期：2026-07-13
> 標籤：#claude-code #open-source #self-hosted #docker #observability

---

## 解決的問題

Claude Code 每次執行的完整過程（對話、讀檔改檔、subagent 派工）都以 JSONL 格式存在 `~/.claude/projects/`，但格式不可讀，回顧「上次怎麼修的 bug」「改了哪些檔案」「燒了多少 token」很痛苦，只能捲終端機或放棄。

## 主要功能

- 全文搜尋所有歷史 session（含 CJK 字符），不只最近幾個
- Session 重放：JSONL → 可讀對話流，工具呼叫非同步結果配對顯示
- 檔案修改顯示紅綠 diff（編輯審計）
- Session 成本統計：工具使用分布、改檔數、model 混用、token 流量、估計美金花費
- 多 agent 派工樹：重建 subagent/隊友清單（類型/訊息數/model），一鍵跳到派工那句話
- 壓縮歷史追蹤：標記 compact 點，可重建壓縮前完整對話
- 釘選/標籤/重新命名/註解管理
- 手機可看，14 種 IDE 配色主題（Dracula/Tokyo Night/Nord/Catppuccin 等）

## 技術棧與安裝

- 前端 React（TS/JS），後端 Node.js/Express，SQLite + FTS5 全文搜尋
- JSONL 解析獨立成 npm 套件 `@recensa/claude-session`
- **需要 Docker**，一行啟動：
```bash
docker run -d --name recensa -p 127.0.0.1:7788:7788 \
  -v "$HOME/.claude:/data/claude" \
  -v recensa-data:/app/backend/data \
  -e RECENSA_PROJECTS_DIR=/data/claude/projects \
  s40911120/recensa
```
訪問 `http://localhost:7788`，首次索引數分鐘到數十分鐘

## 隱私/安全（作者原話）

「Your transcripts stay on your machine; nothing is uploaded anywhere」

- 預設僅綁定 127.0.0.1（迴路），無認證、無遙測、無外部網路呼叫
- 索引器/解析器只讀 JSONL，唯一會寫入的是刪除 session 這個動作（不可逆）
- 有防 DNS 重綁定的 Host/Origin 允許清單

## 現況

MIT 授權，v0.1.0（2026-07-12 首次公開發布），27 stars / 2 forks，還很新（一天內剛發布）

## 對派哥的價值評估

高度相關，直接對應到幾個既有痛點：
- cc_processor debug 時常需要回頭確認 Claude 到底改了哪些檔案 → diff 審計功能直接解決
- 平常會用 Agent tool 派 subagent（如這次的 fork/general-purpose）→ 派工樹視覺化有用
- [[feedback_quota_optimization]] 提到的額度/成本意識 → session 成本統計直接可查每次燒多少
- 全機同時維護多個專案（cc_processor、my-wallet-trip、MyNotes...）→ 跨 session 全文搜尋能省掉「這功能上次是哪個 session 做的」的翻找

風險低：本地 Docker、唯讀、無外部上傳，符合他一貫「資料不外流」的偏好。剛發布(v0.1.0)才一天，算早期版本，可能有 bug，建議先在非關鍵環境試跑。

## 建議

不需要包成 Claude skill（這是獨立的本地 Web 工具，不是 Claude Code 內的操作流程）。如果派哥想用，下一步是確認本機有沒有裝 Docker，然後跑上面那行指令試用。
