---
title: Claude Code + Codex CLI 生圖工作流 — 吃 ChatGPT Pro 額度不用 API Key
tags: [codex, gpt-image-2, claude-code, skill, 圖像生成, 工作流]
date: 2026-04-29
category: 03.科技工具
---

## 核心優勢

不用 OpenAI API Key，直接吃 ChatGPT Pro 訂閱額度（Codex CLI 0.125+）。

| 方式 | 問題 |
|------|------|
| OpenAI API | 需要 Key、另外付費、管理 quota |
| ChatGPT 網頁 | 手動下載、不可批次 |
| **Codex CLI + Claude Code** | ✅ 用訂閱額度、檔案直落專案目錄、可批次可腳本化 |

---

## 基本指令

```bash
codex exec -C "$(pwd)" -s workspace-write \
  --skip-git-repo-check \
  "用 image generation tool 生成 XXX，存到 ./images/foo.png"
```

---

## 工作流

Claude 拆任務 + 拼 prompt → Codex 呼叫 gpt-image-2 出圖 → 圖落指定路徑

適合場景：
- 結構化內容（場景表、產品 mockup 列表、簡報草稿）逐項批次出圖
- 一條龍出整批素材

---

## Skill 設定

`~/.claude/skills/gen-image/SKILL.md`：

```yaml
---
name: gen-image
description: 用 Codex CLI 的 gpt-image-2 生圖，存到當前目錄 ./image/。
  觸發詞：生圖、畫一張、來張圖、generate image
allowed-tools: Bash(codex:*) Bash(mkdir:*) Bash(ls:*)
---
```

Skill 執行步驟：
1. 確認當前工作目錄
2. 從 prompt 提取圖像描述、自動取英文檔名
3. 跑 `codex exec -C "$(pwd)" -s workspace-write --skip-git-repo-check "請使用 image generation tool..."`
4. `ls` 確認檔案，回報絕對路徑

重點：
- `description` 寫清楚觸發詞，Claude 才知道什麼時候用它
- `allowed-tools` 限縮權限，避免誤觸其他 Bash

---

## 對派哥的意義

Codex CLI 已在環境中，可直接測試。My Wallet Trip 需要封面圖時，比開瀏覽器下載更快。

---

## 連結筆記

- [[codex-image2-claude-carousel-workflow]] — Codex + Claude 輪播圖工作流
- [[codex-image2-agent-sprite-forge]] — Codex 批次生圖 Sprite
- [[awesome-gpt-image2-prompts]] — GPT-Image-2 prompt 庫
