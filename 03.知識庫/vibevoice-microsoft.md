---
title: "VibeVoice — Microsoft 開源語音 AI"
tags: [microsoft, asr, tts, speech, transcription, open-source]
date: 2026-04-01
category: 03.科技工具
source: https://github.com/microsoft/VibeVoice
---

## 摘要

> Microsoft 出的開源語音 AI 框架，包含 ASR（語音轉文字）和 Realtime TTS（文字轉語音）兩個模型。

## 模型

### VibeVoice-ASR
- 單次處理最長 **60 分鐘**音訊
- 輸出：**誰 + 時間戳 + 內容**（speaker diarization）
- 50+ 語言，自動語言偵測，支援自訂 hotwords
- 已進 **Hugging Face Transformers v5.3**（`pip install transformers` 即可用）
- 支援 vLLM 加速推論 + finetuning

### VibeVoice-Realtime-0.5B
- 串流 TTS，首聲延遲約 **300ms**
- 支援長篇語音生成
- 9 種語言 + 11 種英文風格聲音

> TTS 原版（VibeVoice-TTS）因被用於語音仿冒，已從 repo 下架。

## 使用方式

### 最簡單：線上 Playground（不需安裝）
→ https://aka.ms/vibevoice-asr

### 輕量整合：Transformers
```python
pip install transformers
# 直接用 microsoft/VibeVoice-ASR
```

### 本機完整部署（需 NVIDIA GPU）
- 官方建議 NVIDIA Docker Container（CUDA）
- Mac M 系列可跑 CPU mode，但長音訊會很慢

## 與現有工具的關係

現有 `video_transcript.py` 用 `youtube_transcript_api` 抓 YouTube 內建字幕，速度快、免費。

**VibeVoice 適合 fallback 情境：**
- `NoTranscriptFound`（影片沒有字幕）
- 字幕品質差（自動生成）
- 需要 speaker diarization（多人對話）

→ 目前不需改動，有需要時加 fallback 即可。

## 相關

- [[video_transcript.py]]
