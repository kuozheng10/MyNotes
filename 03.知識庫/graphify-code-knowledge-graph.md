---
title: Graphify：程式碼知識圖譜，讓 AI 理解「為什麼這樣寫」
tags: ["Claude Code", "工具", "AI", "Python"]
date: 2026-04-21
category: AI工具
source: https://github.com/safishamsi/graphify
---

## 這是什麼

把任何資料夾（程式碼、文件、論文、圖像、影片）轉成可查詢的知識圖譜，讓 AI 不只知道「這是什麼程式碼」，還能理解「當初為什麼這樣寫」。對幾十萬行的老舊專案價值最大。

安裝：`pip install graphifyy && graphify install`

## 核心技術

- **程式碼提取**：tree-sitter AST 分析、調用圖、docstring
- **語義分析**：Claude 子代理並行提取概念與關係
- **聚類**：NetworkX + Leiden 社群偵測（基於**圖邊緣密度**，不用 Embedding）
- **輸出**：互動式 HTML 圖、查詢 JSON、Markdown 報告

支援 25 種語言（Python、JS、TS、Go、Rust、Java、C/C++、Ruby、C# 等）

## 使用方式

```bash
/graphify .               # 分析當前目錄
/graphify query "問題"    # 查詢知識圖
/graphify add <URL>       # 加入論文或影片
graphify watch ./src      # 監視變更自動更新
```

Token 效益：相較直接讀原始檔，混合語料庫可減少 **71.5 倍** token 消耗。

## 質疑

- 前提假設：「圖邊緣密度比 Embedding 更好」適用於有明確調用關係的程式碼；對文件類、敘述型內容，Embedding 的語義相似度反而更準
- 適用邊界：老舊大型 codebase 效果最顯著；新專案、小型 repo 可能不值得建圖的成本
- 潛在反例：Claude 子代理提取關係時若誤判，圖譜錯誤會被後續查詢放大，比沒有圖譜更糟

## 對標

- **人類大腦的海馬迴**：海馬迴存的不是記憶本身，而是記憶之間的連結索引——Graphify 做的是同樣的事，存的是程式碼關係，不是程式碼本身
- **編譯器符號表**：符號表讓編譯器理解「這個變數從哪來」，Graphify 是讓 AI 理解「這個函式為什麼被這樣設計」的符號表

## 對派哥的啟示

不是要取代 CLAUDE.md，而是幫 AI 讀懂 CLAUDE.md 以外的「隱藏知識」。

對派哥的幾個 repo 最有用的情境：
- `sales-report-analysis/` — 業務業績統計.py 有多個樞紐分析，Graphify 可以讓 AI 理解各 sheet 之間的資料流
- 未來 My Wallet Trip 前端若複雜化，用 graphify watch 讓 AI 跟得上架構演化

## 連結筆記

- [[claude-code-powerup-guide]]
- [[llm-wiki-blog-compilation-three-steps]]
- [[ai-agent-system-design-over-prompt]]
- [[claude-md-optimization]]
