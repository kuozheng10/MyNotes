---
tags: [claude-code, ai-coding, usage-limit, automation, launchd]
source: FB分享，https://www.facebook.com/share/p/17PGpoGSKS/?mibextid=wwXIfr
date: 2026-07-31
related: ai-token-cost-governance-tesla-2026-07, codex-custom-instructions-token-review-2026-07, feedback_quota_optimization
---

# Claude 5小時額度視窗重置技巧

> 計時規則：從發出**第一道指令**起算，滿5小時額度就重置。

## 核心策略

上班前2小時，用極輕量任務（傳「嗨」、查天氣）先觸發一次 Claude，提早開啟計時視窗，讓視窗在中午前重置，下午能拿到全新的5小時額度。

## 範例時間表

| 時間 | 動作 |
|------|------|
| 早上 7:00 | 執行輕量任務（觸發視窗開始） |
| 9:00-12:00 | 正常工作（3小時） |
| 12:00 | 第一次重置完成 |
| 13:00-18:00 | 第二個5小時週期啟動 |

效果：只用3小時工作時間，卻能完整使用兩個5小時週期。

留言區：有人已採用此法、設定重置2次；GitHub上已有自動喚醒工具可簡化操作；也有評論質疑「這樣是不是對AI依賴過頭」。

---

## 派哥的實作（2026-07-31）

查證派哥原本的兩個晨報自動化（`daily-briefing` 06:00、`hermes-morning` 08:00）都是純 Python 腳本直接打 API，沒有經過 `claude` CLI，**不會**觸發這個視窗重置——確認他原本沒有這個設定。

已新增 `~/Library/LaunchAgents/com.kuochengchen.claude-window-reset.plist`：
- 每天 **06:57** 執行 `claude -p "回覆兩個字就好：早安"`
- log：`~/Library/Logs/claude-window-reset.log`
- 技術細節：`claude -p` 必須走 OAuth/keychain 認證（不能加 `--bare`，那個 flag 強制要求 API key）；launchd 預設 PATH 太窄要手動補上 `.local/bin`/`.bun/bin`/`/usr/local/bin`，否則 claude 內部呼叫 node 的 hook 會失敗

## 注意

這招只是重置「5小時額度視窗」的計時起點，**不會**繞過更高層的**週用量上限**（weekly cap）——如果本來就常常撞到weekly上限，這招沒用，該檢查的是 agentic loop 呼叫次數（參考 [[ai-token-cost-governance-tesla-2026-07]]），不是視窗重置時機。
