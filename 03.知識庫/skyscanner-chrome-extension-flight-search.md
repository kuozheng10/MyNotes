---
title: 機票查詢進階 Workflow：Chrome Extension 抓 Skyscanner API 原始資料
source: 社群文章（2026-06-19 收藏）
tags: [機票, Skyscanner, Chrome Extension, 旅遊工具, 歐洲機票]
created: 2026-06-19
---

# 機票查詢進階 Workflow：Chrome Extension 抓 Skyscanner API

## 核心做法

**先抓取、後篩選** — 不靠 URL 參數篩選，直接透過 Chrome Extension 截取 Skyscanner 的原始 API response，全部拉回來後再用程式過濾。

優點：
- 不會有遺漏（URL 篩選有時會漏掉特定班次）
- 篩選彈性高：想看直飛就篩直飛，想轉機就篩轉機
- 支援：四腿、多段、來回、單程

## 2026 暑假歐洲票價參考（7/21-8/11 TPE→羅馬來回）

| 航空公司 | 價格 | 轉機點 |
|---------|------|-------|
| 阿提哈德 Etihad | **NT$22,698** | 阿布達比（一次轉機）|
| 土耳其航空 Turkish | **NT$26,963** | 伊斯坦堡 |

- 暑假飛羅馬不到三萬有找
- 土航伊斯坦堡轉機體驗不差，時間合理
- 對中東轉機有疑慮 → 土航是折衷選項

## 工具重點

- 工具類型：Chrome Extension（截取 API 原始資料）
- 目標：Skyscanner 的背後 API
- 可查：德國→台灣、台灣→歐洲等任意多段路線

## 延伸閱讀
- [[alaska-mileageplan-starlux-redemption]]
- [[eva-air-mile-redemption-guide-2026]]
- [[travel-hacks-trip-agoda-jcb-lounge]]
