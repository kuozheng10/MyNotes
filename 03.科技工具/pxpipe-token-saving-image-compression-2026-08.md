---
tags: [claude-code, token-saving, pxpipe, ai-tools, cost-optimization]
source: [Facebook - 陳盟升](https://www.facebook.com/share/p/1LHHGYoLjs/?mibextid=wwXIfr) ／ [GitHub - teamchong/pxpipe](https://github.com/teamchong/pxpipe)
date: 2026-08-18
related: local-agent-mcp-strategy-2026-08, gpt-claude-gemini-20usd-comparison-2026-08
---

# pxpipe：把文字轉圖片省 Token 的本地代理工具

> ⚠️ **派哥評估結論：不建議用在目前的自動化工作流上**，見下方「對派哥的意義」——精確字串（Notion頁面ID/帳號/交易序號）有靜默出錯風險，跟現有 cc_processor/investment 工作流衝突。

---

## 是什麼

本地代理（proxy）工具，把 Claude Code 要送出的大量文字內容（系統提示、工具文件、對話歷史）**壓縮成 PNG 圖片**再送出——因為圖片消耗的 token 比大量純文字少，達到省 token/省費用的效果。開源 MIT 授權：https://github.com/teamchong/pxpipe

## 支援模型

| 模型 | 支援狀況 |
|------|---------|
| Claude Opus 5 | 支援 |
| Claude Fable 5 | 支援，表現最佳 |
| Google Gemini Flash 3.7 | 支援 |
| GPT（技術上可行） | **官方不推薦**——GPT 5.6 Sol 圖片識別精度低、易產生幻覺 |

需要**訂閱制 Claude Code 方案**才能用。

## 安裝與使用

```bash
# 最快試用（30秒）
npx pxpipe-proxy

# 搭配 Claude Code
ANTHROPIC_BASE_URL=http://127.0.0.1:47821 claude

# warp 模式（不用手動設環境變數）
pxpipe warp -- claude
```

離線批次導出（不用開代理）：
```bash
npx pxpipe-proxy export src/              # 導出目錄
cat prompt.txt | npx pxpipe-proxy export --stdin
npx pxpipe-proxy export --git             # 導出 git diff
```

監控／統計：
```bash
pxpipe stats            # 人類可讀報告
pxpipe stats --json     # JSON格式
```
內建網頁儀表板：http://127.0.0.1:47821/，可看每筆請求省了多少 token、文字vs圖片轉換前後對比、一鍵關閉開關。

## 效益數字（官方測試）

- 端到端費用降低約 **59～70%**
- Token 壓縮率：原始請求大小減少 **60～65%**
- 密度提升：同樣 1M token 窗口可容納約 **4.7～5.0 倍**文本內容
- FB貼文範例：Opus 5 情境省下 46% token，約 $27.55 美元

## ⚠️ 已知限制與風險（關鍵，決定能不能用的地方）

### 1. 精確字串會「靜默出錯」——最大風險

官方自己測試：**12碼十六進制字串，在 Sol 模型上正確率是 0/15**，Fable 5 上是 13/15。這種錯誤不會跳出錯誤訊息，是圖片還原成文字時悄悄讀錯——**字節級精確值（ID、雜湊、金鑰）官方自己都寫明「必須保持為文字」，不要靠圖片壓縮**。

### 2. 模型依賴性差異大

不同模型表現落差明顯（Fable 5 算術100/100、十六進制13/15 vs Opus 4 算術93/100、十六進制0/15）。Grok/Sol 預設不啟用，要手動開。

### 3. 語言支援限制

**ASCII/Latin-1 充分測試；CJK（中文/日文/韓文）「保守」**——不是完全驗證過的狀態。

### 4. 效能取捨

PNG 編碼在大請求送出前會增加延遲；稀疏散文內容（低密度純文字）反而可能增加成本而非省錢，不是每種內容都適合。

---

## 對派哥的意義

**評估結論：不建議現在混進日常自動化工作流**。

理由：派哥每天在做的事——cc_processor 寫 Notion 頁面ID、投資帳戶對帳、記錄車牌/保單號碼、Gmail message ID 比對——全部都是「精確字串一錯，整筆資料錯位」的操作類型，剛好踩中 pxpipe 最大的已知風險區。加上中文支援官方自己標「保守」，而派哥的工作內容幾乎全是繁體中文，兩個扣分項疊加，跟能省下的那點 token 費用不成比例。

如果只是拿來做**跟精確ID無關、單純腦力激盪/一般對話**的場景，可以考慮試用省token，但目前主要工作流建議先不碰。

## 相關筆記

- [[local-agent-mcp-strategy-2026-08]] — 同作者：地端Agent+MCP分工策略
- [[gpt-claude-gemini-20usd-comparison-2026-08]] — 同作者：三家AI $20方案比較
