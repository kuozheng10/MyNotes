---
tags: [AI工具, 自動化, Playwright, Codex, 生圖, 省成本]
來源: TG貼文（無URL，全文貼上）
儲存日期: 2026-07-22
---

# 用 Playwright + Cookie 注入操控 ChatGPT 網頁版生圖，0 API/Codex 額度

## 核心概念

原本用 Agent 生圖都是走 Codex 的 API 憑證接口，每生成一張圖就在燒 Codex 額度。
這個做法改用 **Playwright 自動化 + 匯出的登入 Cookie**，讓 Agent 直接繼承已登入的 ChatGPT 網頁版帳號狀態，改用網頁版的生圖額度（跟 API/Codex 額度分開算），達到「Codex 專心寫程式、生圖走網頁版」的分工。

## 實作原理

1. 用 Playwright 啟動 Chromium，載入平時匯出的 ChatGPT 登入 Cookie 檔
2. 不用手動輸密碼、不會卡驗證碼（繼承已登入 session）
3. Agent 在網頁版操作對話框輸入生圖指令
4. 生圖完成後從 DOM 抓 `<img>` 標籤原始連結，或直接 fetch 圖片網域下載，存到本地資料夾

## 兩個關鍵除錯坑

| 坑 | 解法 |
|---|---|
| ChatGPT 網頁版側邊欄/對話框常有透明懸浮遮罩，一般 click 會被攔截 | 點擊動作加 `force: true` 直接繞過遮罩 |
| 生圖後要自動下載存檔 | 從 DOM 抓 `img` src，或對圖片網域發 fetch 下載存本地 |

## 效益

- 0 Codex 額度消耗（Codex 額度留給寫程式用）
- 網頁版訂閱額度跟 API/Codex 額度分開計算，等於多一份用量
- 全流程自動化：指令→生圖→下載歸檔不用手動點擊

## 對派哥的應用評估

現有 [[../.claude/skills/gen-image/SKILL.md|gen-image skill]] 是走 **Codex CLI 呼叫 gpt-image-2 API**（會燒 Codex 額度）。
這篇的技術可以做成備援/平行方案：網頁版額度用完 API，或想省 Codex 額度時，改走 Playwright + Cookie 注入操控 ChatGPT 網頁版。

**風險/取捨**：
- Cookie 會過期，需要重新匯出，比 API key 麻煩
- 屬於「繞過官方 API 用網頁自動化」的灰色作法，穩定性不如官方 API（頁面改版就要重寫 selector）
- 只適合「量大、不趕時間、想省錢」的情境；急件/高可靠度需求還是走 API 較穩

## 後續動作

尚未實作，等派哥決定要不要做成新 skill 或加進現有 gen-image skill 的 fallback 邏輯。若要動手，屬於「純實作、跨多個檔案（cookie 管理 + playwright 腳本 + selector 除錯）」，適合丟給 Codex 寫（見 Ponytail 原則），Claude 負責架構決策 + review。
