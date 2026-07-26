---
tags: [claude-code, mcp, ai-video, higgsfield, veo, image-gen]
source: Facebook Reel https://www.facebook.com/share/r/1DJ1tkT6MA/?mibextid=wwXIfr
date: 2026-07-26
related: gen-image-web
---

# Higgsfield MCP × Claude：聊天視窗裡直接生圖生影片

## 這是什麼

Higgsfield推出的MCP（Model Context Protocol）連接器，讓Claude對話視窗裡可以直接呼叫超過30個頂級AI生成模型，不用切換工具、不用自己申請各家API。

## 整合的模型

Soul、Cinema Studio、Seedance、Kling、Veo 3、Nano Banana Pro、GPT Image 2.0 等30+模型，全部透過同一個MCP連接器統一呼叫。

## 能力

- 輸入一句提示詞 → 最高4K圖片，或長達**15秒**的影片
- 可做「數字人風格」廣告，自訂角色能在不同場景保持一致外觀
- 適合DTC(直營品牌)行銷素材：完整行銷活動視覺、產品圖、社群版面

## 怎麼接（影片教學步驟）

1. 不用設定任何API key
2. Claude介面裡新增「Custom Connector」
3. 名稱填 `Higgsfield`，URL填Higgsfield MCP的位址（影片沒完整顯示，需要留言跟原po索取或查官網）
4. 前提是Higgsfield帳號本身要有點數(credit)才能生成

## 對派哥的意義：跟現有 veo-video-gen skill 的關係

派哥自己已經有 [[gen-image-web]] 系列 + `~/.claude/skills/veo-video-gen/SKILL.md`，用Veo 3.1 API直接生多鏡頭影片，這篇的Higgsfield MCP是另一條路——**差別在於「要不要自己寫程式碼」**：

- **veo-video-gen（現有方案）**：直接呼叫Veo API + 自己寫Python/ffmpeg拼接，全部在Claude Code裡跑，免費用同一把GEMINI_API_KEY，但要處理API細節(單次生成上限8秒、rai審查、參數限制等)
- **Higgsfield MCP（這篇）**：透過MCP連接器，在對話視窗裡直接下指令生成，不用寫程式碼，但要付Higgsfield的點數費用，且整合的是Higgsfield代理的模型集合(含Veo 3但不是直接呼叫Google API)

派哥現有的方案技術上更省錢(用API key而非買點數)，但門檻高一點；Higgsfield MCP門檻低很多，適合不想寫程式的情境，或想快速試多家模型比較效果時用。

## 派哥問的技術問題：能不能用code串接超過單次生成上限（例如39秒）？

**可以，而且派哥自己的veo-video-gen skill裡已經寫好這個做法了**：

Veo 3.1 API單次生成最長只有8秒，`duration_seconds`參數超過8會直接回400錯誤——但這個限制只針對「單次API呼叫」，不是「最終影片長度」。skill裡的解法是：把總秒數拆成多段4~8秒的clip（例如要20秒 = 8+8+4三段），每段各自呼叫API生成，生完之後用**ffmpeg concat**把多個clip檔案接成一支完整影片。

關鍵細節：
- 每段clip的prompt都要用同一份角色/風格描述開頭(人物外觀、服裝、場景、打光)，確保拼接後視覺一致，不會忽然換一個人
- 多段clip可以同時送出generation request，各自輪詢完成狀態，不用等前一段做完才生下一段，省時間

這個「單次生成有上限，但用code串接就能突破」的邏輯，不管換成Higgsfield、Veo、還是任何影片生成API都通用——限制永遠是「單次呼叫的長度」，不是「最終能做多長」，只要生成的clip之間銜接得夠自然，理論上能無限接下去。

## 相關筆記
- [[gen-image-web]] — 另一套省Codex額度的生圖方案，跟這篇同樣是「聊天介面直接生成」的思路
