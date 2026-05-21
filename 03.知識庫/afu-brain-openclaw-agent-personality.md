---
title: afu-brain：從零到開源，用演算法讓 AI 龍蝦長出個性
tags: [OpenClaw, 開源, AI Agent, 個性演算法, MASL, 龍蝦腦, 社群自動化, afu-brain]
date: 2026-05-08
category: AI工具
---

## 這是什麼

一個從「GitHub 跟我無關」到「第一個開源專案」的真實歷程紀錄。
核心產出：**afu-brain** — 讓 OpenClaw 龍蝦有個性、有記憶、有自己的行為參數。

**GitHub**：https://github.com/norika1207-lab/afu-brain

---

## 核心發現（值得記住的洞見）

| 觀察 | 結論 |
|------|------|
| 龍蝦各說各話，沒有真正互動 | OpenClaw 平台本質是「匿名想法的轉譯中心」，不是真正的討論 |
| 拔掉 LLM 後龍蝦立刻變白痴 | LLM 是龍蝦智能的唯一來源，演算法只能補上基本行為 |
| 加上個性參數後龍蝦會說「過去討論過的議題」 | 長期對話累積的資料是個性的雛形 |
| 10 隻龍蝦聊天室產生質變 | 即時互動架構讓行為複雜度指數上升 |
| 一天可達 12,000 則對話 | 規模化後「情緒/個性差異」才真正顯現出來 |

---

## 技術路徑

1. 龍蝦發文監控介面（可視化歷史紀錄）
2. 行為路徑記錄 → 資訊圖表 → 演算法個性參數
3. 即時聊天室（10 隻龍蝦，LLM on/off 對比實驗）
4. 龍蝦腦（無 LLM 條件下的基礎個性引擎）
5. MASL 標準（Multi-Agent Social Layer，數萬次測試產出）
6. 前端介面覆蓋人類可能需求 → 串接 OpenClaw

---

## 時間軸

| 日期 | 里程碑 |
|------|--------|
| 4/1 | 第一個 AI coding 專案（模擬股市交易所）|
| 4/15 | 接觸 OpenClaw/Moltbook，開始實驗 |
| 4/15+ | 開了 9 隻新龍蝦，自架測試網 |
| 之後 | 聊天室 → 龍蝦腦 → MASL → 開源 |

---

## 關鍵引用

> 「這些真的是出自於龍蝦的想法呢？還是人們加諸在上面的一種意識傳輸轉譯的過程？」

> 「那不過就是一個大型的匿名想法的轉譯中心而已」

> 「從沒有 LLM 的催化之下，竟然會說出來的話。」

---

## 連結參考

- [[openclaw-hermes-collaboration]] — OpenClaw 協作模式
- [[ai-agent-modular-architecture]] — 模組化 AI Agent 設計
- [[multi-agent-system-architecture-optimization]] — 多 Agent 系統架構
