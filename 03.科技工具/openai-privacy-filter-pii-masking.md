---
title: OpenAI Privacy Filter：AI 處理前先遮個資
tags: [OpenAI, 隱私, PII, AI工具, 資料安全, RAG, 企業AI]
date: 2026-04-26
category: AI工具
source: Garfield_Investment
video: https://youtu.be/xAozuLQdYEA
duration: "7:39"
---

## 影片主旨

OpenAI 於 2026/04/22 發布 Privacy Filter：一個在文字資料進入 AI 系統之前，自動偵測並遮罩個人可識別資訊（PII）的本機小模型。不是聊天 AI，而是企業 AI 資料流的「安檢門」。

---

## 重點摘要

- 不是 LLM，而是 token classifier（逐段判斷哪些文字含 PII）
- 開源（GitHub + Hugging Face），授權 Apache 2.0，可商業部署
- 可在筆電、瀏覽器、內部機房跑，最敏感資料不必離開本機
- 8 大遮罩類別：私人姓名、地址、Email、電話、URL、日期、帳號號碼、**secret（含 API key/token）**
- 保留上下文（不是整段刪掉），讓後續系統仍能讀懂內容
- 效能：F1 96%（修正標註後 97.43%）；1.5B 總參數、50M active、128K context
- 少量 fine-tuning 可針對特定領域（醫療、金融、法務）調整

---

## 詳細內容

### 架構

從自回歸預訓練 checkpoint 轉成**雙向 token classifier**，用 constrained Viterbi 解成連續 span。一次掃過輸入找出遮罩區段，不是逐字生成回答——對大量資料處理效率更高。

### 遮罩示範

原文：有姓名、日期、專案號碼、Email、電話
→ 處理後：`PRIVATE_PERSON`、`PRIVATE_DATE`、`ACCOUNT_NUMBER`、`PRIVATE_EMAIL`、`PRIVATE_PHONE`

### 安裝與使用

```bash
# 下載 repo 後取得 opf 指令
opf "含個資的文字"

# 可接 Unix pipe、批次讀整個檔案
cat log.txt | opf
```

### 限制

- **不是匿名化保證，不是合規證書**
- 高敏感場景（醫療、法務、金融、人資）仍需人工 review
- 當成隱私設計裡的「一層」，不是唯一防線

---

## 對派哥的應用

三個最值得嵌入的位置：

1. **RAG indexing 前**：清洗客服紀錄、合約、會議逐字稿的個資再建向量索引
2. **客服/工單摘要前**：遮罩個資再送 AI 摘要
3. **log/錯誤回報前**：自動抓出 API key、token 再送 AI 分析（cc_processor 最相關）

---

## 結論

Privacy Filter 的定位是「可下載、可檢查、可本機部署的隱私基礎元件」。未來每個 AI workflow 可能都需要這種 filter，就像網站需要 HTTPS 一樣。對正在把 AI 接進企業資料流的團隊，現在就值得實測。
