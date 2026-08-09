---
tags: [testing, e2e, playwright, trace-viewer, claude-code, debugging, automation]
source: DavidKo Learning Journey，FB分享 https://www.facebook.com/share/p/1AHjecRzBu/?mibextid=wwXIfr ／ [原文iThome鐵人賽Day10](https://ithelp.ithome.com.tw/articles/10402215)
date: 2026-08-10
related: ai-coding-e2e-test-speed-myth-2026-07, ui-test-layers-2026-06
---

# Playwright Trace Viewer：測試失敗時讓證據說話

> **系列**：「AI 時代下最值得投資的 UI 自動化：30 天用 Claude Code 學會寫 Playwright」Day 10（作者 kojenchieh，同系列另見 [[ai-coding-e2e-test-speed-myth-2026-07]]）
> **核心結論**：CI 上測試失敗常常無法重現（尤其十次掛一次那種），Trace 是當下唯一能留下的完整犯罪現場，養成看 trace 的習慣比事後猜原因有效率得多。

---

## Trace 是什麼

測試執行過程的完整側錄，精確到毫秒。一份 trace 包含四類證據：

| 證據 | 用途 |
|------|------|
| 時間軸 | 每步動作何時發生、花了多久 |
| 每步截圖 | 失敗前每個瞬間畫面長什麼樣 |
| 網路請求 | API 被呼叫了什麼、回了什麼，有沒有 500 錯誤 |
| Console 訊息 | 網頁前端有沒有噴錯 |

**各自的破案時機**：
- 時間軸：某步花 28 秒才過，雖沒失敗但抓出效能異常前兆
- 截圖：「找不到按鈕」一看畫面，被沒見過的公告彈窗蓋住了
- 網路請求：畫面只顯示「發生錯誤」，網路面板那條 500 直接指出哪支 API 掛了
- Console：畫面看起來沒反應，console 的 JS 錯誤說明前端根本炸了

---

## 什麼時候會錄到 trace（常踩的坑）

錄製時機由設定檔的 `trace` 選項決定：

```js
// playwright.config.js
use: { trace: 'on-first-retry' },
// 'off'                 完全不錄
// 'on'                  每次都錄（檔案大，適合除錯）
// 'retain-on-failure'   全部都錄，只留下失敗的那些
// 'on-first-retry'      第一次失敗不錄，重試時才錄（專案初始化預設值）
```

⚠️ **陷阱**：`on-first-retry` 平常很夠用，但本機執行預設不重試，所以第一次失敗就結束了，那次執行**不會留下 trace**。想保證錄到，執行時加參數：

```bash
npx playwright test --trace on
```

不確定專案目前設定，可以直接叫 Claude Code 讀設定檔解釋。

---

## 打開 trace report 的三條路

**HTML 報告是否自動跳出**由 reporter 的 `open` 選項控制：
```js
reporter: [['html', { open: 'on-failure' }]],
// 'on-failure'（預設）有失敗才自動開；'always' 每次都開；'never' 從不自動開
```
沒自動開/想看上一次的：`npx playwright show-report`

**進 Trace Viewer 三條路**：
1. **從報告點進去**（日常最順，九成走這）：開報告 → 進失敗測試的詳情頁 → 點 Traces 區塊縮圖
2. **指令直接開檔案**：trace 是個 zip 檔，放在 `test-results/<測試資料夾>/` 下
   ```bash
   npx playwright show-trace test-results/<測試資料夾>/trace.zip
   ```
   懶得找路徑：跟 Claude Code 說「幫我打開剛才失敗那個測試的 trace」，它會自己定位執行
3. **網頁版**：`trace.playwright.dev`，把 trace.zip 拖進去就能看，完整功能且對方電腦不用裝任何東西——**適合附在缺陷單裡給開發者看**

---

## 分析的終點：產品 bug 還是測試 bug？

- **產品問題**：截圖顯示錯誤頁，網路面板有一條回 500 的請求 → 拿 trace 去報缺陷，證據齊全到開發者說不出「無法重現」
- **測試問題**：畫面一切正常，只是元素文字改了，測試還在找舊文字 → 回頭修測試

這個判斷是測試人員的核心價值，**AI 可以協助但不該代替你拍板**——實務好用法是先自己看過 trace，再把觀察丟給 Claude Code 一起研判。

---

## 實作範例（TodoMVC 破案流程）

1. 請 Claude Code 寫一個會失敗的測試：「新增兩筆待辦，點『Clear completed』清除已完成項目，驗證清單仍有2筆」
2. 帶著錄 trace 執行：`npx playwright test --trace on`
3. 報告自動跳出（`on-failure`），進失敗測試詳情頁，先看 Errors + Test Steps（紅色那步等了近30秒）
4. 進 Trace Viewer，往下捲找 Traces 區塊點縮圖
5. 對照四個區塊辦案：
   - 時間軸抓紅色那步
   - 動作清單顯示 click 'Clear completed' 耗時 30.0s（其他步都0.1秒，這步等好等滿）
   - **截圖是破案關鍵**：兩筆待辦好好躺在清單上，但清單底部根本沒有 Clear completed 按鈕
   - Call Log 解釋這30秒內 Playwright 反覆做了什麼

**真相**：Clear completed 按鈕只有在「至少一筆已完成項目」時才出現，流程新增了兩筆但忘了先勾完成，按鈕自然不存在——不是產品bug，是測試流程漏了一步（點按鈕前要先勾第一筆完成）。

> 破案關鍵是那張截圖：不用讀程式，看畫面就知道按鈕不在。Trace 對不寫程式的人特別友善的地方，就是證據是視覺的。

---

## 對派哥的意義

呼應 [[ai-coding-e2e-test-speed-myth-2026-07]] 同系列的觀點：AI/Claude Code 在測試流程裡的定位是「協助生成腳本、協助判讀證據」，不是「取代人的判斷」。這篇補的是「CI失敗後怎麼查根因」的具體工具流程——如果派哥之後用 Playwright 測 Vercel 部署（[[feedback_test_against_prod]]）遇到「本機好好的，CI/排程跑就是失敗」這種間歇性問題，第一步就是確認 `trace: 'on'` 或用 `--trace on` 執行，不要單純加 print/log 用猜的除錯。

## 相關筆記

- [[ai-coding-e2e-test-speed-myth-2026-07]] — 同系列：AI時代UI測試變快的真正原因（架構不是AI）
- [[ui-test-layers-2026-06]] — 測試分層責任邊界
