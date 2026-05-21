---
title: "Web-Design-Guidelines：Vercel Labs 官方合規審查 Skill"
tags: [claude-code, skill, vercel, wcag, accessibility, code-review, ui]
date: 2026-04-02
category: 03.科技工具
source: Facebook + skills.sh
---

## 是什麼

Vercel Labs 官方出品的 Skill，每次執行都從 GitHub 拉最新規則，逐行比對程式碼，輸出 `file:line` 格式直接告訴你哪裡違規。

GitHub：https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines
規則來源（每次 live fetch）：https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md

## 安裝

```bash
# 下載 zip
https://skills.sh/vercel-labs/agent-skills/web-design-guidelines

# 或從 GitHub 複製
gh api "repos/vercel-labs/agent-skills/contents/skills/web-design-guidelines/SKILL.md"
```

放到 `~/.claude/skills/web-design-guidelines/SKILL.md` 即可全域使用。

## 使用方式

```
/web-design-guidelines src/components/Button.tsx
/web-design-guidelines src/app/**/*.tsx
```

觸發關鍵字：「review my UI」、「check accessibility」、「audit design」、「check WCAG」

## 審查項目（12 大類）

| 類別 | 主要規則 |
|------|---------|
| **Accessibility** | icon button 要 `aria-label`；表單控件要有 label；語意化 HTML |
| **Focus States** | 不得 `outline-none` 沒有替代；用 `:focus-visible` 而非 `:focus` |
| **Forms** | input 要 `autocomplete`、正確 `type`；錯誤訊息 inline 顯示 |
| **Animation** | 需支援 `prefers-reduced-motion`；只 animate `transform`/`opacity` |
| **Typography** | 用彎引號、`…`、non-breaking space；數字欄位用 `tabular-nums` |
| **Content Handling** | flex 子元素需 `min-w-0`；處理空狀態和長文字溢位 |
| **Images** | 要有明確 `width`/`height`；below-fold lazy load |
| **Performance** | 超過 50 筆要虛擬化列表；避免 `transition: all` |
| **Navigation & State** | URL 反映狀態（filter、tab、pagination）；破壞性操作要確認 |
| **Touch & Layout** | 安全區域、原生 input 樣式 |
| **Dark Mode / i18n** | locale-aware 格式、hydration 安全 |
| **Hover & Copy** | hover 狀態、語氣一致性 |

## 輸出格式

```
src/components/Button.tsx:12  Missing aria-label on icon button
src/app/login/page.tsx:34     outline-none without focus-visible replacement
src/components/List.tsx ✓
```

VS Code 可直接點擊跳轉。

## vs Impeccable /audit

| | Web-Design-Guidelines | Impeccable /audit |
|--|--|--|
| **規則來源** | Vercel 官方，live fetch 最新 | 內建固定規則 |
| **強項** | WCAG 合規、a11y、精確 file:line | UX 設計品質整體評估 |
| **輸出** | 精準定位違規位置 | 評分 + 嚴重程度分類 |
| **互補** | ✅ | ✅ |

## 相關

- [[impeccable-design-skill]]
- [[ui-ux-pro-max-skill]]
- [[boris-15-claude-code-tips]]
