---
title: Gemini 訂閱附帶的 Colab 算力——用 Codex 幫你在 Colab 架 Qwen 模型＋API
source: [FB 社團「MQTT 與 AIoT 整合運用」Tung-hsing Hsieh 貼文](https://www.facebook.com/share/p/1DLZ4mjYz5/?mibextid=wwXIfr)（2026-10-08）
tags: [Gemini, Google One, Colab, GPU, 自架模型, Qwen, llama.cpp, Codex, RAG, MiniMax]
date: 2026-10-13
category: AI工具
---

# Gemini 訂閱附帶的 Colab 算力，不用就可惜了

> 派哥丟連結說「save sop」。一句話：**如果你的 Google 訂閱方案（Gemini／Google AI 方案）有附 Colab 算力額度，可以先拿來試跑自架 AI 模型，不用急著買顯卡；設定交給 Codex 做。**

## 作者的做法

1. 開一個 Colab 筆記本
2. **用白話告訴 Codex 需求**（例如「把 Qwen 放上 Colab、接好固定網址」），讓 Codex 一步步幫你設定
3. 遇到錯誤 → 把錯誤訊息丟給 AI 排查，邊做邊學
4. 完成後其他程式可以**透過 API 呼叫**這個模型

截圖裡的實例：
- Colab 筆記本「Qwen3.8-27B-llama.cpp-API」，用 **llama.cpp** 跑 **Qwen3.8 27B**
- GPU：**NVIDIA A100-SXM4（80GB）**，High-RAM
- 輸出 `API_READY`，有一個固定的 base_url（/v1，OpenAI 相容格式）
- 右邊是 Codex 的對話：「幫我把 Qwen3.8-27B 放在一個新的 Colab」

## 可以拿來做什麼

| 想做 | 作者建議 |
|---|---|
| 影片 | **MiniMax H3**：準備角色參考圖，描述「走進畫面、揮手、介紹產品」，先生成一小段，再慢慢拼成完整故事（產品介紹、課程開場、角色動畫） |
| 客服 | **Qwen3.8 ＋ RAG**（先查資料再回答）：整理商品說明、保固規則、常見問題，讓系統先找相關資料再請模型回答；找不到依據就轉人工 |

## 注意（我補的）

- Colab 的 GPU 是**算力單位計費**、而且 session 會斷，適合「試做／短時間跑」，不適合當 24 小時常駐的服務
- 「固定網址」通常是透過 tunnel（例如 ngrok／cloudflared）暴露出來，要注意不要把沒有驗證的 API 公開在網路上
- 各方案附帶多少 Colab 算力，以自己的 Google 訂閱頁面為準（作者沒寫數字）

## 對派哥

- 派哥目前的 Gemini 是走 API key（`~/.npm-global/bin/gemini` wrapper），如果有 Google AI 訂閱方案，可以看一下帳戶有沒有附 Colab 算力
- 跟本機跑模型（[[apple-mlx-local-agent-2026-06]]）是兩條路：MLX 用自己的 Mac，Colab 借雲端 A100 跑更大的模型（27B）
- 想試 RAG 客服、或讓一蘭用自架模型時，可以先在 Colab 驗證可行性，再決定要不要買硬體

## 相關筆記

- [[apple-mlx-local-agent-2026-06]] — Mac 本機跑模型
- [[local-agent-mcp-strategy-2026-08]] — 本機 agent 策略
- [[local-rag-pageindex-2026-06]] — 本機 RAG
