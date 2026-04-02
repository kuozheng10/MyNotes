---
title: "Expo Skills for Claude Code"
tags: [expo, react-native, claude-code, skills, mobile-ui]
date: 2026-04-03
category: 03.科技工具
source: https://github.com/expo/skills
---

## 摘要

> Expo 官方出品的 Claude Code Skills 套件，12 個 skill 涵蓋 React Native / Expo 開發全流程。如果在做 App（非網頁），這組 skill 很值得裝。

## 安裝

```bash
# Claude Code
/plugin marketplace add expo/skills
/plugin install expo

# 或用 bun
bunx skills add expo/skills
```

## 12 個 Skills 一覽

### UI 開發（最實用）

| Skill | 說明 |
|-------|------|
| `building-native-ui` | Expo Router、元件、導航、動畫、Apple HIG 最佳實踐 |
| `expo-ui-swift-ui` | iOS SwiftUI 原生元件 |
| `expo-ui-jetpack-compose` | Android Jetpack Compose 原生元件 |
| `expo-tailwind-setup` | NativeWind v5 + Tailwind CSS v4 整合 |

### 資料 & 後端

| Skill | 說明 |
|-------|------|
| `expo-api-routes` | Expo Router API routes + EAS Hosting |
| `native-data-fetching` | 網路請求、快取、離線支援 |
| `use-dom` | 在 Native 裡跑 Web 程式碼（webview DOM）|

### 部署 & DevOps

| Skill | 說明 |
|-------|------|
| `expo-deployment` | 上架 iOS App Store / Android Play Store |
| `expo-cicd-workflows` | EAS workflow YAML CI/CD |
| `expo-dev-client` | 本機或 TestFlight 測試版部署 |

### 維護

| Skill | 說明 |
|-------|------|
| `upgrading-expo` | SDK 版本升級與依賴修復 |

## 適用情境

- ✅ 做 React Native / Expo App UI 必裝 `building-native-ui`
- ✅ 需要跨平台原生元件 → `expo-ui-swift-ui` / `expo-ui-jetpack-compose`
- ✅ 想用 Tailwind 寫 Native → `expo-tailwind-setup`
- ✅ 要上架 → `expo-deployment`
- ❌ 純網頁開發不需要

## 備註

- MIT License，開源免費
- Skills 自動根據上下文觸發，不用手動指定
- 與 Vercel plugin 同樣機制，放在 Claude Code plugin marketplace
