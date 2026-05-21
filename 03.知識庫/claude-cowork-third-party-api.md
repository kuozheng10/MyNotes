---
title: Claude Cowork 接第三方 API 與本地 LLM 設定指南
tags: [claude-desktop, cowork, ollama, openrouter, local-llm, litellm]
date: 2026-04-26
category: AI工具
---

## 是什麼

Claude Desktop 最新功能：**Cowork on Third-Party Platforms**
讓 Claude Cowork 可以接非 Anthropic 的模型，包含本地 LLM 和雲端替代方案。
付費與免費帳號都支援。

來源：https://www.koc.com.tw/archives/640513（Rocky，2026-04-25）

## 支援的連線方式

| 方案 | 說明 |
|------|------|
| Gateway | 相容 Ollama、OpenRouter、LiteLLM |
| Amazon Bedrock | AWS 方案 |
| Google Vertex | GCP 方案 |
| Azure AI Foundry | Microsoft 方案 |

## 設定步驟

### 前置
啟用 Developer Mode：Help → Troubleshooting → Enable Developer Mode

### Gateway 設定需填
- 完整 HTTPS endpoint URL
- API 憑證（不需要驗證則填任意文字）
- 認證方式（通常是 `bearer`）

## 兩個常用方案

### Ollama（本地跑）
- 需要用 Caddy 做 HTTPS reverse proxy
- 適合隱私需求高、不想上雲的場景

### OpenRouter（雲端）
- Base URL：`https://openrouter.ai/api`
- 不需要自建 proxy，最省事

## 注意

多一層呼叫 → 速度比直接用 Claude 原生模型慢。

## 適合用在哪

- 想在 Cowork 測試 Gemini / Mistral / Llama 等模型
- 想用本地 Ollama 跑任務（隱私考量）
- OpenRouter 多模型切換

## 值得做 Skill 嗎？

不急。這是一次性設定，不是重複工作流。
把這篇筆記存起來，需要設定時參考即可。
