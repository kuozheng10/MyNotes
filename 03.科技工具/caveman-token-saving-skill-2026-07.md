---
tags: [ai-coding, claude-code, skill, token-optimization, open-source, mit-license]
source: https://github.com/JuliusBrussee/caveman
date: 2026-07-04
category: 03.科技工具
---

# Caveman：開源免費 AI Coding Agent 省 Token Skill

> **一句話**：讓 AI 用「聰明穴居人」風格回應，砍掉贅字保留技術實質，官方測試平均省 65% 輸出 token。

> ⚠️ **派哥已經裝過了**：`~/.claude/skills/caveman/SKILL.md` 已存在，本地版本聲稱 ~75% 節省（比 GitHub 官方數字更高，可能是本地客製過的版本）。這篇筆記記錄官方版本的細節供對照。

---

## 核心特色

| 項目 | 內容 |
|------|------|
| 輸出 token 節省 | 平均 **65%**（10 項基準測試，範圍 22%~87%） |
| 壓縮等級 | 6 級：lite、full（預設）、ultra、wenyan（古文中文）等 |
| 保留範圍 | 程式碼、命令、錯誤訊息**完全保留**，只縮減語風贅字 |
| 記憶檔案壓縮 | `/caveman-compress` 指令，永久節省輸入 token 約 **46%** |
| 會話統計 | 即時追蹤節省數據 |

## 支援平台（30+ 個）

Claude Code（原生）、Gemini CLI、Cursor、Windsurf、Cline、Codex、GitHub Copilot 等。

## 安裝方式

```bash
curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.sh | bash
```
需求：Node ≥ 18。啟用：輸入 `/caveman` 或說 "talk like caveman"。

## 數據誠實聲明

專案在 `docs/HONEST-NUMBERS.md` 明確聲明：**節省的主要是輸出 token，輸入與推理 token不受影響**。數據來自 `benchmarks/` 與 `evals/` 目錄的實測紀錄，不是行銷話術。

## License 與社群

- **MIT License**（完全免費、可商用）
- **83.9k Stars**、154 Issues、201 PRs
- 官網：caveman.so
- 計畫中的 Caveman 2：團隊級 token 計量與驗證儀表板

---

## 派哥的吐槽（原始貼文脈絡）

派哥分享時提到：有 prompt 優化課老師在賣類似功能的付費課程，這個作者直接把同等技術開源出來。反映的現象：**AI 工具鏈的護城河越來越薄**——單一 skill/plugin 就能複製課程賣的核心價值，MIT 授權更是直接消除商業壁壘。

## 對派哥的意義

- 本地已有同名 skill 在跑，功能高度重疊，不需要重新安裝官方版
- 若本地版本效果不如預期，可以參考官方 repo 的 `benchmarks/` 方法論來源，或直接切換成官方版本比較
