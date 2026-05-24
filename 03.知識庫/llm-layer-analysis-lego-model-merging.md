---
title: LLM 黑盒拆解——23 個模型全攤開，中段層通用、邊緣層特異
tags: [LLM, 模型合併, 逆向工程, 架構分析, 蒸餾, AI研究]
date: 2026-05-24
category: 科技工具
source: github.com/norika1207-lab/mercury-mcp / doi.org/10.5281/zenodo.20352085
---

## 這是什麼

一個人拆開 23 個 LLM（13 個 architecture family），觀測每一層的「熱點指紋」，
得出最大的結論：

> **中段層通用，邊緣層特異**

---

## 核心發現

### 1. 中段層跨家族相似（最重要）

- qwen-7B 第 15 層 vs falcon-7B 第 16 層：functional fingerprint 相似度 0.868（滿分 1）
- 84 對跨家族比對，54 對中段層 sim > 0.7
- 結論：不管哪家訓，模型中段（深度 50~60%）都在做類似的事

→ **這是「LLM 樂高化」的物理基礎**：從不同模型各取一段中間層，理論上能接起來

### 2. Anchor 指紋會跟著蒸餾走

- DeepSeek-R1 70B 用 llama 70B 當底蒸餾，anchor 卻比 llama 還像 qwen（比隨機高 44.7 倍）
- 蒸餾不只搬走能力，連「指紋」都搬走
- **應用：可以鑑定「自研 LLM」到底是誰蒸的**

### 3. 各家族的特徵

| 家族 | 特徵 |
|------|------|
| qwen | 3B~32B anchor 位置幾乎一樣，骨幹穩定 |
| Phi3 | dim 4271~4366 連續集中，Microsoft 印章 |
| Falcon3 | dim 2030~2040 連續 9 個 anchor |
| IBM Granite | 低位 dim 442~454 |
| Mistral | anchor 跟 qwen 完全無交集，但中段功能對齊 → 可「不衝突合併」|
| OLMo2 | 完全獨立訓練，仍出現 qwen anchor（比隨機高 29.8 倍）→ transformer 架構可能有「收斂座標」|

---

## 實際應用

**你不需要從零訓 LLM：**
- 找到你要的能力 → 對應模型拆出那幾層 → 疊起來 → 接 projection adapter
- 訓練成本可能比 fine-tune 通用 LLM 還少

**模型合併：**
- 中段層跨家族相容 → 混合不同模型的層是可行的
- 需要 projection adapter 處理 hidden size 差異（qwen 3584, llama 4096, phi3 5120）

**模型血統鑑定：**
- anchor 結構是蒸餾指紋
- 可以鑑定公司宣稱「自研」的模型實際血統

---

## 方法論誠實揭露

作者自己發現一個問題：
- 兩種觀測方法（看輸出層 vs 看每層內部）對同一模型給出不同結論
- 「dim 11 跨家族通用」可能只是 tokenizer 副作用
- 但中段層 fingerprint 對齊（0.868）是用第二種方法量的，跟 tokenizer 無關

---

## 對派哥的評估

你使用 LLM 作為工具，不做模型研究。**直接應用價值偏低。**

知道就好的部分：
- RAG 通常比自訓 LLM 更適合企業專屬知識（跟作者的動機相反）
- 「自研 LLM」宣稱可以用指紋鑑定，下次聽到可以存疑

---

## 資料來源

- GitHub：github.com/norika1207-lab/mercury-mcp
- DOI：doi.org/10.5281/zenodo.20352085
- MIT 開源 / CC-BY-4.0 資料授權
