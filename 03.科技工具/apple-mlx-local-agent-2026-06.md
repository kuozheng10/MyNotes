---
tags: [mlx, local-llm, apple-silicon, agent, mac, huggingface, qwen, privacy]
source: https://www.koc.com.tw/archives/647214
original: Apple WWDC 2026，MLX 團隊工程師 Angelos 示範
date: 2026-06-27
---

# Apple 官方教學：Mac 本地 AI Agent（MLX）

> **一句話**：蘋果自己出的工具，讓 Mac 在完全不上雲的情況下跑 AI Agent。
> 不需要 API Key、不需要訂閱、不需要網路，資料完全留在本機。

---

## 這是什麼？

Apple WWDC 2026 推出的本地 AI Agent 開發方案。
Apple Silicon（M 系列晶片）有自己的矩陣運算加速，MLX 就是把這個能力包成工具，讓你可以在 Mac 上跑大型語言模型，速度和記憶體效率都比一般 Python 框架好。

---

## 技術四層結構

| 層次 | 工具 | 功能 |
|------|------|------|
| 底層運算 | **MLX** | Apple Silicon 專用陣列框架，Metal GPU 加速 |
| 模型執行 | **MLX LM** | 載入 / 量化 / 微調，支援 Hugging Face 數千個模型 |
| 本地 API | **MLX LM Server** | 跑出一個 OpenAI 相容的 HTTP 伺服器 |
| Agent 層 | Xcode / OpenCode / PyAgent | 任何支援 OpenAI Chat Completions 的框架都能接 |

---

## 三步快速啟動

```bash
# 1. 安裝
pip install mlx-lm

# 2. 啟動本地模型伺服器（以 Qwen3 4B 為例）
mlx_lm.server --model mlx-community/Qwen-3.5-4B-8bit

# 3. 把 Agent 工具指向 http://127.0.0.1:8080 即可
```

完全離線，跑起來後等於有個私人 ChatGPT API 在本機。

---

## 適合跑什麼模型？（依 RAM 估算）

| 統一記憶體 | 建議模型大小 | 範例 |
|-----------|------------|------|
| 8 GB | 3B–4B（8bit） | Qwen3 4B、Phi-4 mini |
| **16 GB** | **4B–8B（8bit）** | **Qwen3 8B、Llama 3.1 8B、Gemma 3 9B** |
| 32 GB | 8B–14B（8bit） | Qwen2.5 14B |
| 64 GB+ | 30B–70B | Llama 3 70B |

---

## 應用案例

- 從零建立 SwiftUI iPad 繪圖 App（Xcode 整合）
- 程式碼除錯與修復（本地模型直接接 Xcode）
- 企業內部文件問答（不怕資料外洩）

---

## 和其他本地 LLM 方案比較

| 方案 | 特色 | 限制 |
|------|------|------|
| **MLX（本篇）** | Apple 官方、最佳化 M 晶片、原生 Metal 加速 | 僅限 Apple Silicon |
| Ollama | 最容易上手、跨平台 | 速度略遜 MLX |
| LM Studio | GUI 友善 | 底層也是 llama.cpp，非 MLX 原生 |

→ 相關筆記：[[local-rag-pageindex-2026-06]]

---

## 延伸功能（M5 特有，M4 無）

- M5 神經加速器：提示詞處理 4 倍加速
- 分散式推理（4 台 Mac 透過 Thunderbolt RDMA 串聯 → 3 倍效能）

M4 沒有這些加速，但 MLX 本身在 M4 上仍完全可用，跑 4B–8B 模型沒問題。
