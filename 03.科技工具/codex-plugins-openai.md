# openai/plugins — 讓 Codex 自己裝外掛

> 來源：https://github.com/openai/plugins
> 儲存日期：2026-06-13
> 標籤：#codex #plugin #automation #openai #workflow

---

## 是什麼

OpenAI 官方的 Codex plugin 範例庫，173 個插件（截至 2026-06-13）。
每個插件放在 `plugins/<name>/`，包含：
- `.codex-plugin/plugin.json` — 插件 manifest
- `skills/` — Codex skill 定義
- `.mcp.json` — MCP server 設定
- `agents/`、`hooks.json` 等

---

## 對派哥特別有用的插件

| 插件 | 用途 |
|------|------|
| `notion` | 計劃、研究、會議記錄、知識管理 |
| `vercel` | 部署、CI/CD |
| `github` | PR、issue、code review |
| `gmail` | Gmail 自動化 |
| `google-calendar` | 行事曆 |
| `google-drive` | 文件管理 |
| `figma` | 設計→code（偶爾用） |
| `linear` | 待觀察 |

---

## 核心技巧：讓 Codex 自己選插件

不需要預先知道要裝哪個。打開 Codex 輸入：

```
請查看 openai/plugins、我的倉庫結構，以及我的實際工作方式，
判斷我應該安裝和配置哪些插件，並幫我完成設定。
```

Codex 會自己：
1. 掃 openai/plugins 173 個插件
2. 分析你的 repo 結構和工作流程
3. 選出最適合的插件
4. 自動完成安裝設定

---

## 評估（對派哥的用途）

✅ **有用**，理由：
- 派哥用 Codex 跑大型實作任務（`codex exec --full-auto`）
- notion/vercel/github 三個插件命中派哥主要工作流
- 讓 Codex 自己判斷比手動篩 173 個省時

⚠️ **注意**：
- 這是 Codex（OpenAI）的插件系統，不是 Claude Code skill
- 需要安裝 Codex CLI + 對應 plugin
- Plugin 和 Claude Code skill 是兩個不同系統，不互通

---

## 安裝方式

```bash
# 確認 Codex CLI 版本
codex --version

# 在 repo 目錄下，讓 Codex 自動選插件
codex "請查看 openai/plugins 並幫我選擇和安裝適合的插件"
```

---

## DevSpace MCP — 用 ChatGPT 額度補 Codex

> 來源：社群分享（TG 2026-06-22）
> GitHub: https://github.com/Waishnav/devspace

**原理**：OpenAI 的 ChatGPT 和 Codex 額度分開計算，DevSpace MCP 讓 ChatGPT 充當 Codex，額度等於翻倍。

```bash
npm install -g @waishnav/devspace
# 裝好後透過網路 tunnel 把 MCP server 暴露出去
```

**建議使用情境：**

| 場景 | 模型 | 用途 |
|------|------|------|
| 規劃/分析 | GPT-5.5 Pro / xHigh | 需求拆解、架構設計 |
| 實作 | 本地 Codex | 寫程式碼（主力） |
| Code Review | ChatGPT（透過 DevSpace） | 審查其他 coding agent 的輸出 |

**對派哥的應用：**
- Codex 額度見底時的緊急備援（不用停工）
- 用 ChatGPT 先做規劃書，再交 Codex 實作（類似 Gemini → Claude 的分工模式）

⚠️ **風險**：這屬於灰色玩法，OpenAI 可能隨時關閉。別依賴它作為主要工作流。

---

## Three.js Object Sculptor — 圖片轉3D模型的Codex外掛

> 來源：Facebook「Codex 中文社群」分享，2026-07-12
> GitHub: https://github.com/vinhhien112/Three.js-Object-Sculptor-Codex-Plugin
> ⚠️ 非 openai/plugins 官方庫的插件，第三方獨立專案

**做什麼**：附上一張物件照片，這個外掛會分析照片，產生一份「雕塑規格」(材質、光影、關節結構)，再自動寫出一整套**用程式碼構造**的 Three.js 3D 模型(不是輸出模型檔，是輸出可以動畫化的程式碼)，過程分八個階段逐步精修，還有 AI 視覺比對來檢查渲染出來的模型像不像原照片。

**用途**：網頁上的即時互動3D道具、會動的裝飾物、產品展示模型，適合遊戲/網頁3D場景。

**安裝**：`git clone`到本機外掛資料夾，走 `codex plugin add xxx@local` 流程，跟一般Codex plugin一樣（跟上面`openai/plugins`同一套安裝機制）。

### 評估（對派哥的用途）

⏸️ **暫時沒有立即用途**，理由：
- 派哥目前的專案(my-wallet-trip、insurance-tracker、investment-dashboard、cc_processor)都是資料/CRUD類型的網頁應用，沒有Three.js/3D/遊戲需求
- 這是解決「遊戲/3D網頁視覺化」這種很specific的問題，跟派哥現在的工作內容對不上

**先記著就好，不用現在包成skill**——這種一次性、有明確觸發情境才用得到的工具，等真的哪天想在某個網站加個好玩的3D小物件時，直接照README步驟裝就是了(不用預先花時間包裝，Ponytail原則：能不寫就不寫)。

---

## 相關筆記

- [[chatgpt-work-launch-2026-07]] — Codex技術被包進「ChatGPT Work」這個消費級/企業級產品（2026-07推出），跟這篇講的Codex CLI plugin生態是同一個Codex技術的兩種產品形態
