---
title: Beeper MCP：讓 Claude Code 讀寫 Messenger、IG 私人帳號訊息
tags: ["工具", "Claude Code", "MCP", "Messenger", "Instagram", "自動化"]
date: 2026-04-24
category: AI工具
source: https://youtu.be/-HOakZC7Vps
video: https://youtu.be/-HOakZC7Vps
duration: "10:41"
---

## 影片主旨

AgentCrew Academy（Dustin）示範如何用 Beeper 這個合規的通訊整合工具，搭配本機 MCP，讓 Claude Code 直接讀取並回覆 Messenger 和 Instagram 的**私人帳號**訊息——不用瀏覽器自動化，也不用違反服務條款的逆向 API。

## 重點摘要

- 官方 API 只開放商業帳號（粉絲專頁、LINE 官方帳號），私人帳號不支援
- 瀏覽器 MCP 可行但慢、耗 token
- 逆向工程私有 API 違反服務條款，風險封號
- Beeper = 中間路線：合規公司 + 本機 bridge，Claude 透過 MCP 存取

## 核心工具：Beeper

- 把多個通訊服務整合進一個 inbox 的正規公司
- 大部分程式碼開源，已被上市公司收購
- 免費版：最多綁 5 個帳號（一個服務一個）
- 目前支援：WhatsApp、Twitter、Telegram、LinkedIn、iMessage、Email、Facebook、Instagram
- **不支援 LINE**

## 安裝流程

1. 下載並安裝 Beeper（目前只支援 Mac）
2. 在 Beeper APP 加入帳號（登入 FB/IG），勿開 VPN（避免 Meta 誤判可疑流量）
3. Beeper 設定 → Developers → 開啟 Desktop API
4. 複製設定文字貼給 Claude，請他設定 MCP
5. 在 Developers 下方建立 API Token（設定到期日，開啟「發送訊息」權限）
6. 重開 Claude session（MCP 在 session 開始時載入）
7. 確認 MCP Connected，可讀取多帳號訊息

## 安全注意事項

- **API Token 不要貼在 Claude 對話裡**（留在記錄中等於洩露）
- 請 Claude「教你如何安全地設定 key」，用系統指令設定，不要直接貼
- 若 Token 已洩露 → 立刻去 Developers 取消舊 Token、重建新的
- 所有連線跑在本機，Beeper 程式關掉 MCP 就失效

## 風險評估（Dustin 判斷：低風險）

| 風險 | 說明 |
|------|------|
| 非官方認證 | Meta 改版可能暫時壞掉，但 Beeper 修復快 |
| 自動化偵測 | Meta 可能要求重新驗證身份（非永久封號） |
| 非全加密 | 部分對話不加密 |
| Token 外流 | 自己管理，不貼在 Claude 對話裡 |

技術開源、公司合規、官方聲稱資料只有用戶自己看得到。

## 對派哥的啟示

**實用性高**，但目前派哥不需要。

有用的場景：
- 用 Claude 處理大量 IG/Messenger 客服訊息
- 自動整理對話、草擬回覆

限制：
- 只支援 Mac（派哥的 mac mini 可以，但需常開 Beeper）
- 不支援 LINE（台灣主力通訊工具）
- Beeper 要一直開著，關掉就失效

等支援 LINE 再認真評估。

## 連結筆記

- [[claude-code-chrome-builtin]] — 瀏覽器 MCP 的替代方案
- [[skill-mcp-security-check]] — MCP 安全掃描 SOP
- [[vibe-coding-rce-heredoc-three-rules]] — Token 安全管理
