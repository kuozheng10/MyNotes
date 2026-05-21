---
title: Faster Whisper：無顯卡也能跑的本地語音辨識
tags: [語音辨識, Whisper, 本地部署, AI工具, CTranslate2, 資安, 離線]
date: 2026-05-08
category: AI工具
---

## 這是什麼

OpenAI Whisper 的高效優化版，由 SYSTRAN 開發。透過 CTranslate2 引擎加速，速度提升 4 倍、記憶體需求大幅降低，純 CPU 也能跑。

**GitHub**：https://github.com/SYSTRAN/faster-whisper

---

## 核心優勢

- 速度：比原版 Whisper 快 4 倍
- 硬體門檻低：無 GPU 的迷你電腦也能運作（搭配量化模式）
- 離線運作：不需上傳音訊到雲端，資料不外洩
- 免費：省去 API 費用

---

## 使用方式

```bash
pip install faster-whisper
```

```python
from faster_whisper import WhisperModel

model = WhisperModel("tiny", device="cpu", compute_type="int8")
segments, info = model.transcribe("audio.mp3")
for segment in segments:
    print(segment.text)
```

模型大小選擇：
- `tiny` / `base`：CPU 適用，速度快，準確度較低
- `small` / `medium`：平衡選擇
- `large-v3`：最高精準度，需較多資源

---

## 對派哥的應用

| 場景 | 說明 |
|------|------|
| 會議錄音轉逐字稿 | 本地跑，機密不外洩 |
| 影片字幕生成 | 搭配 cc_processor 或自動化流程 |
| 語音輸入 Claude Code | 已在迷你電腦用 `tiny` 模型實測可行 |

安裝建議：讓 Claude Code 協助安裝，比用本地弱模型（Gemma 26b）快很多。

---

## 連結參考

- [[claude-code-computer-use]] — 語音輸入整合 Claude Code
- [[self-hosted-scraper-solution]] — 本地部署架構
