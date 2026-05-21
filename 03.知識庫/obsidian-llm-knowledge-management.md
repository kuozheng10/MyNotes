---
title: "Obsidian × LLM 知識管理完全指南（9 單元課程摘要）"
tags: [obsidian, knowledge-management, markdown, zettelkasten, claude-code]
date: 2026-04-07
category: 03.科技工具
source: Telegram 分享（課程線上版）
---

## 一句話核心

> Obsidian 用 .md 純文字 + 雙向連結，天生適合 LLM 讀寫串連；第 9 單元直接示範 Obsidian × Claude Code。

## 為什麼 Obsidian 適合搭配 LLM

- 純 .md 格式 → Claude 直接讀寫，不需解析私有格式
- 雙向連結 `[[]]` → LLM 可自動偵測概念關聯
- Frontmatter YAML → 結構化元數據，方便 Dataview 查詢
- 本地檔案 → 可 git 備份、版本控制

## 9 個單元一覽

| 單元 | 主題 | 派哥相關度 |
|------|------|-----------|
| 1 | 快速入門（Vault/Note/Link/Graph） | ✅ 已在用 |
| 2 | Markdown 基礎 | ✅ 已熟悉 |
| 3 | 雙向連結 + Graph View | ⭐ 可加強 |
| 4 | 資料夾/標籤/Frontmatter 組織 | ⭐ 可加強 |
| 5 | 搜尋語法 + 模板系統 | ⭐ 可加強 |
| 6 | 外掛生態（Dataview/Templater/Git） | ✅ Git 已用 |
| 7 | Zettelkasten 卡片盒筆記法 | 📖 參考 |
| 8 | （未收錄）| — |
| 9 | **Obsidian × Claude Code** | 🔥 重點 |

## 關鍵觀念速查

### 雙向連結進階用法
```
[[筆記名稱]]           # 基本連結
[[筆記名稱#標題]]      # 連結到特定段落
[[實際名稱|顯示文字]]  # 自訂顯示文字
![[檔案名稱]]          # 嵌入內容
```

### 組織策略
- **資料夾**：大分類（PARA = Projects / Areas / Resources / Archive）
- **標籤**：跨領域屬性，支援巢狀（`#status/draft`、`#domain/AI`）
- **Frontmatter**：元數據 + Dataview 查詢用

### 圖形結構健康度
| 結構 | 代表意義 |
|------|----------|
| 星狀 | 有高度連結的中心筆記（好） |
| 群集 | 多主題各自聚落（正常） |
| 鏈狀 | 線性串聯（可優化） |
| 孤立節點 | 需要補連結（警示） |

### 必裝外掛
| 外掛 | 用途 |
|------|------|
| **Dataview** | 類 SQL 查詢筆記，變資料庫 |
| **Templater** | 進階模板，支援動態內容 |
| **Git** | 版本控制與同步 |
| **Calendar** | 日曆視圖管理每日筆記 |
| **QuickAdd** | 快速捕捉想法 |

## 單元七：知識管理方法

### Zettelkasten 卡片盒筆記法（Niklas Luhmann）
三種筆記類型：
1. **閃念筆記**：快速捕捉靈感，24–48 小時內處理
2. **文獻筆記**：閱讀後用自己的話重述，記錄來源
3. **永久筆記**：原創想法，每則一個概念，用完整句子，連結相關筆記

工作流程：捕捉 → 閱讀 → 思考 → 連結 → 發展 → 創作

### PARA 系統（Tiago Forte）
- **Projects**：有截止日期的短期任務
- **Areas**：需持續維護的責任範圍（健康、財務）
- **Resources**：感興趣的主題與參考資料
- **Archive**：已完成或不活躍的項目

> PARA + Zettelkasten 可並存：PARA 管「做什麼」，Zettelkasten 管「想什麼」

### MOC 地圖筆記
索引型筆記，組織某主題下的所有相關筆記。看全局、找缺口、快速導航。

## 單元九：Claude Code × Obsidian 架構（重點）

受 Andrej Karpathy 啟發的 AI 知識管理三件組：

```
Obsidian（瀏覽/視覺化）← .md 檔案 → Claude Code（撰寫/維護）
                                    ↕ git
                               GitHub（版本控制）
```

核心流程：LLM 將 raw data 編譯成 .md wiki → CLI 問答 → Obsidian 持續精煉

### 從零建立 AI 知識庫（6 步驟）
1. 選資料夾結構（PARA + AI 混合 或 主題分類）
2. 建立 `CLAUDE.md`：定義結構、協作方式、寫作風格
3. 建立 `MEMORY.md`：AI 長期記憶，記錄重要事件、決策、偏好
4. 設定每日記憶系統（`memory/` 資料夾日誌）
5. 建立核心筆記：專案清單、學習清單、技能樹、靈感收集
6. 連結 Claude Code：開啟知識庫測試對話

### 維護節奏
| 頻率 | 時間 | 內容 |
|------|------|------|
| 每日 | 5–10 分鐘 | 記錄工作想法、處理收件箱 |
| 每週 | 30–60 分鐘 | 整理學習筆記、清理臨時筆記 |
| 每月 | 2–3 小時 | 歸檔完成專案、優化 CLAUDE.md |
| 每季 | 半天 | 全面健檢、識別知識缺口 |

## 對 MyNotes 的啟示

派哥目前已在跑這套架構雛形，改進空間：

| 現況 | 改進 | 優先度 |
|------|------|--------|
| 雙向連結偏少 | 補 `[[]]` 連結，減少孤立節點 | ⭐⭐ |
| Frontmatter 無 status | 加 `status: draft\|published` | ⭐ |
| 無 Dataview | 裝後可自動索引標籤 | ⭐⭐ |
| 無 MOC | 建立主題地圖筆記（如 `00.索引/` 已有雛形） | ⭐ |
| MEMORY.md 已有 | 持續維護即可 | ✅ |

## 相關筆記

- [[llm-knowledge-base-karpathy]] — Karpathy 原版 LLM wiki 架構
- [[enterprise-ai-roles-prediction]] — Skills 規劃師 = 整理 Obsidian skills 的人
- [[addyosmani-agent-skills]] — SKILL.md 本身就是 Obsidian-friendly 格式
