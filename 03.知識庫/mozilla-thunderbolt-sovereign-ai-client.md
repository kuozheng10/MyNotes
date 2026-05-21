---
title: Mozilla Thunderbolt：開源主權 AI 客戶端，自架企業 AI 的選項
tags: ["工具", "開源", "LLM", "自動化", "Agent"]
date: 2026-04-23
category: AI工具
source: http://slash-invest.com/mozilla-thunderbolt-open-source-sovereign-ai-client-2026/
---

## 這是什麼

Mozilla MZLA Technologies 2026/4 推出的開源企業 AI 對話平台。核心主張：AI You Control — 多模型支援、資料留在自己機器、無廠商綁定。

GitHub：github.com/thunderbird/thunderbolt（Alpha，3,481 stars，安全稽核進行中）

## 核心功能

- 多模型切換：Claude、GPT、Mistral、Ollama、llama.cpp、任何 OpenAI 相容 API
- 企業搜尋：跨 Notion、Confluence、SharePoint 的 RAG 問答
- 排程自動化：條件觸發任務（每日摘要、警報）= 初步 Agent 功能
- 本機推論：原生 Ollama 支援，zero external data transfer

## 安裝（3步 Docker Compose）

```bash
# 1. 裝 Ollama（本機模型）
ollama pull llama3

# 2. Clone repo
git clone https://github.com/thunderbird/thunderbolt

# 3. 啟動
docker compose up -d
# → localhost:8080
```

## 與競品比較

| 面向 | Thunderbolt | ChatGPT Enterprise | Microsoft Copilot |
|------|-------------|-------------------|-------------------|
| 授權 | 開源 MPL 2.0 | 商業訂閱 | 商業訂閱 |
| 資料位置 | 自有機房 | OpenAI 伺服器 | Azure 租戶 |
| 模型選擇 | 多元 | 限 OpenAI | 限 Microsoft |
| 本機推論 | ✅ | ❌ | ❌ |

## 質疑

- 前提假設：「資料主權」是核心賣點，但個人用戶和小團隊不太需要這個；法律/醫療/金融才是目標客群
- 適用邊界：Alpha 階段，安全稽核未完成；生產環境建議等 2026 底再評估
- 潛在反例：多模型切換聽起來很好，但實際上大多數人只會用一兩個模型，「支援多元」帶來的是設定複雜度，不是直接價值

## 對標

- **Firefox 對 IE**：Mozilla 一貫的策略——用開源打破單一大廠壟斷，Thunderbolt 試圖對 ChatGPT Enterprise 做同樣的事
- **VLC 播放器**：開源、跨平台、什麼格式都支援——功能全但不是最精緻的使用體驗

## 對派哥的啟示

**不能取代一蘭，不需要裝。**

差異：

| | Thunderbolt | 一蘭（OpenClaw）|
|--|-------------|----------------|
| 定位 | 通用 AI 聊天 UI | 派哥客製化工作流 Agent |
| 有 SOUL.md/skills | ❌ | ✅ |
| 有晨報/交班/存文章 | ❌ | ✅ |
| 排程自動化 | 初步 | 成熟 |
| 需要 Docker/Ollama | ✅（成本） | ❌ |
| Alpha 階段 | ✅（風險） | 穩定運作中 |

Thunderbolt 適合：需要資料主權的企業 IT、想在內網跑多模型的場景。

觀察時間點：2026/12 安全稽核完成、首個企業公開案例出現後再重新評估。

## 連結筆記

- [[ai-agent-hermes-openab-openclaw-comparison]]
- [[openclaw-hermes-collaboration]]
- [[hermes-agent-vs-openclaw-comparison]]
