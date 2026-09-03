---
title: Codex 內建圖表技能：45 種可直接生成的圖表類型
source: https://www.facebook.com/story.php?story_fbid=1526005012886916&id=100064322940906
author: Will 保哥的技術交流中心（FB，2026-09-02）
tags: [ai, codex, 圖表, diagram, 架構圖, 視覺化, skill]
date: 2026-09-03
category: AI工具
---

# Codex 內建圖表技能：45 種可直接生成的圖表

Will 保哥整理：Codex CLI **內建**的圖表 skill 能直接生成以下 45 種圖表，不用另外裝 skill。
Hashtag「#其他家的也可以啦」= Claude Code / Gemini 等也做得到，這份清單當「可以叫 AI 畫哪些圖」的提示詞備忘。

## 完整清單（45 種）

**架構 / 系統**
1. 前後對比圖 Before-and-After Diagram
2. 因果圖 Cause-and-Effect Chart
3. 系統架構圖 System Architecture Diagram
4. 網路拓樸圖 Network Map
5. 資料流程圖 Data-Flow Diagram
6. 資訊流程圖 Information-Flow Diagram
7. 飛輪模型 Flywheel
8. 回饋迴路 Feedback Loop
9. 層級結構圖 Hierarchy Chart
10. 組織架構圖 Organization Chart

**心智 / 關係**
11. 心智圖 Mind Map
12. 概念圖 Concept Map
13. 關係圖 Relationship Map
14. 生態系統圖 Ecosystem Map
15. 利害關係人地圖 Stakeholder Map
16. 依賴關係圖 Dependency Map

**流程 / 時程**
17. 旅程地圖 Journey Map
18. 使用者流程圖 User-Flow Diagram
19. 路線圖 Roadmap
20. 里程碑圖 Milestone Chart
21. 甘特圖式圖表 Gantt-Style Chart
22. 泳道圖 Swimlane Diagram
23. 桑基流程圖 Sankey-Style Flow Chart

**分析 / 比較**
24. 范氏圖 Venn Diagram
25. 比較表 Comparison Table
26. 比較矩陣 Comparison Matrix
27. 象限圖 Quadrant Chart
28. 優缺點對照表 Pros-and-Cons Chart
29. 金字塔圖 Pyramid Diagram
30. 分層圖 Layer Diagram
31. 光譜圖 Spectrum Chart
32. 成熟度模型 Maturity Model
33. 進程圖 Progression Chart
34. 計分卡 Scorecard
35. 數據統計卡片 Statistic Cards

**統計**
36. 長條圖 Bar Chart
37. 折線圖 Line Chart
38. 環形圖 Donut Chart
39. 散佈圖 Scatter Plot
40. 熱點圖 Heat Map

**技術說明**
41. 註解介面圖 Annotated Interface Diagram
42. 爆炸視圖介面圖 Exploded Interface Diagram
43. 程式碼至成果關聯圖 Code-to-Outcome Diagram
44. 運作原理說明圖 How-It-Works Explainer
45. 事件重組圖 Incident Reconstruction Diagram

## 對派哥的用途

- 直接跟 Codex / Claude Code 說「幫我畫一張 XX 圖」就好，這 45 個名詞就是關鍵字
- 已想到的實際場景：
  - #3 系統架構圖 / #22 泳道圖 → cc_processor BankAdapter、investment 排程分派
  - #16 依賴關係圖 → 哪個 plist 跑哪個 script（剛做完 watchdog 那批）
  - #45 事件重組圖 → 排程停 2 天那種故障事後說明
  - #26 比較矩陣 / #24 范氏圖 → 買借死 vs 75/25、IB01 vs SGOV 這類對照
- 跟 [[drawio-skill-arch-diagrams]] 的差別：那個要裝 draw.io desktop 才能匯出，走 .drawio XML；這個是 AI 直接吐圖（多半是 HTML/SVG/mermaid），不用額外安裝

## 連結筆記

- [[drawio-skill-arch-diagrams]] — drawio-skill，一句話生成架構圖（需 draw.io desktop）
- [[architecture-diagram-generator-skill]] — 另一個架構圖生成 skill
- [[next-ai-drawio-diagram-tool]] — Next AI 的 drawio 工具
- [[codex-custom-instructions-token-review-2026-07]] — Codex 使用心得
