---
title: Claude Code × Codex × GPT Image-2 串接輪播圖工作流
tags: [claude-code, codex, GPT-Image-2, 輪播圖, 工作流, 自動化, 圖像生成, 多AI串接]
date: 2026-04-28
category: AI工具
---

## 核心洞見

多 AI 串接補位才是接下來幾年 AI 使用者真正要練的功。
不是只用一個工具，而是各家有強項、互補協作。

---

## 舊工作流 vs 新工作流

**舊（4 個工具來回）：**
```
Claude Code 寫文 → HTML 排版 → Gemini API 生插圖 → Playwright 截圖 → 手動整合
耗時：1-2 小時
```

**新（1 行命令）：**
```
Claude Code 寫好指令 → 交付給 Codex → 等 10 分鐘 → 9 張一致風格輪播圖進資料夾
```

4 個工具 → 1 行命令

---

## 為什麼品質更好（不只是速度）

三個過去做不到的層級：
1. **繁中字筆劃精準**到可印刷級
2. **九張一起看的一致感**（風格/色調統一）
3. **版型穩定到 px 級**

HTML 排版 + 後製插圖的做法根本做不到這三件事。

---

## 適合誰自動化

不適合：偶爾生圖的人 → ChatGPT 點按鈕就夠

適合：
- 每週固定產出輪播圖
- 寫專欄、做模板
- 生成行銷素材的固定節奏

---

## Claude × Codex 的互補關係

| 工具 | 強項 |
|------|------|
| Claude Code | 規劃、寫文、架構、給 Codex 下指令 |
| Codex | 圖像生成（GPT Image-2）、程式碼互相 review |
| GPT Image-2 | 繁中字精準、高一致性、印刷級品質 |

**Codex 的另一個用途**：和 Claude 互相 review 對方寫的 code（之後可專文寫搭建指南）

---

## 更大的方向

GPT 5.5 + AI 自動操作電腦能力 + Claude 4.7 同級：
→ Agent 終於不只是 prompt 工程的延伸，是真的成立了
→ 可以自己 plan、自己 check、跨工具跑完整個任務
→ 原生同時處理文字/圖片/影片/聲音

---

## 對派哥的意義

- **現在**：你已有 Claude Code + Codex 分工，輪播圖工作流可以直接採用
- **輪播圖需求**：My Wallet Trip 行銷素材、個人品牌內容 → 這套流程值得投資
- **Codex 互相 review**：和閃卡 bot / RAG 專案結合，Codex 寫 code + Claude review 架構
- **GPT Image-2 prompt 庫**：參考 `awesome-gpt-image2-prompts.md`

---

## 連結筆記

- [[codex-image2-agent-sprite-forge]] — Codex Image-2 Sprite 生成
- [[codex-plugin-cc]] — Codex + Claude Code 整合
- [[awesome-gpt-image2-prompts]] — GPT Image-2 prompt 資源庫
- [[boris-parallel-claude-workflow]] — 多 Claude 並行工作流
