---
tags: [testing, e2e, playwright, popup, iframe, dialog, claude-code, automation]
source: DavidKo Learning Journey，FB分享 https://m.facebook.com/story.php?story_fbid=pfbid02jj2oesw6AXVUnbD7sqnCZwDCHQaX6Dma1cWcSMVcPPrYD9Htf2pGEi9Ew5RVZbual ／ [原文iThome鐵人賽Day17](https://ithelp.ithome.com.tw/articles/10403221)
date: 2026-08-17
related: playwright-trace-viewer-2026-08, ai-coding-e2e-test-speed-myth-2026-07, playwright-page-object-model-2026-08
---

# Playwright 四種難搞畫面元素：彈窗、iframe、新分頁、日期選擇器

> **系列**：「AI 時代下最值得投資的 UI 自動化：30 天用 Claude Code 學會寫 Playwright」Day 17（作者 kojenchieh，同系列另見 [[playwright-trace-viewer-2026-08]] Day10、[[playwright-page-object-model-2026-08]] Day21）
> **核心方法**：不用背 API，你負責「看懂場景、講清楚現象」，技術細節交給 AI。四種元素的共通點：都不在「目前這個網頁」的正常範圍裡，一般 locator 摸不到。

---

## 四個難搞元素，各自為什麼難

| 元素 | 難點 |
|------|------|
| 原生彈窗（alert/confirm/prompt）| 瀏覽器畫的，不是網頁內容；**沒先掛處理器，Playwright 預設會自動關掉它**，測試看起來有跑，其實什麼都沒確認 |
| iframe | 網頁裡嵌的另一個網頁（頁中頁），直接找會撲空 |
| 新分頁 | 點擊後另開一頁，操作對象換了，測試還盯著舊分頁 |
| 日期選擇器 | 跳出來的小月曆，本質上是幾十顆按鈕 |

**溝通訣竅**：跟 AI 描述時不用講術語，講「長相」就好——「點刪除會跳出瀏覽器那種灰灰的確認視窗」AI 立刻知道是原生 confirm；「付款表單看起來是嵌進來的」它會去試 iframe。

---

## 一、原生彈窗（5個場景）

```js
test('confirm 按確定：訂單消失並顯示已刪除', async ({ page }) => {
  page.once('dialog', dialog => dialog.accept());
  await page.locator('#order-1001').getByRole('button', { name: '刪除' }).click();
  await expect(page.locator('#order-1001')).toHaveCount(0);
  await expect(page.locator('#order-msg')).toHaveText('已刪除');
});

test('confirm 按取消：訂單仍在，也沒有出現刪除訊息', async ({ page }) => {
  page.once('dialog', dialog => dialog.dismiss());
  await page.locator('#order-1001').getByRole('button', { name: '刪除' }).click();
  await expect(page.locator('#order-1001')).toBeVisible();
  await expect(page.locator('#order-msg')).toHaveText('');
});
```

**關鍵陷阱**：`page.once('dialog', ...)` **一律寫在點擊之前**——原生彈窗是點下去瞬間跳出來的，處理器晚一步掛上就接不到。**完全沒掛處理器時，Playwright 會自動把彈窗關掉（等同按取消）**——所以「沒寫任何 dialog 處理，confirm 的測試卻全綠」不是好事，是警訊，很可能一直在測按取消的路徑。

**最容易漏測的**：按取消那條。兩個斷言方向剛好相反（訂單還在 + 訊息欄空字串），第二個斷言常被省略，「按取消也顯示已刪除」這種半吊子 bug 就溜過去了。

**alert 測試重點在 `dialog.message()`**：只寫 `accept()` 把視窗關掉，測試綠了但訊息寫錯字、筆數算錯全測不到。

**beforeunload 離開提醒也是 dialog 的一種**，同一套 `page.once('dialog')` 接得到，差別在觸發方式要用 `page.close({ runBeforeUnload: true })`。

## 二、網頁 Modal（對照組，3個場景）

網站自己做的漂亮版彈窗（不是瀏覽器原生的）——**是普通網頁元素，正常定位就找得到，不需要任何 dialog 處理**：

```js
test('按 ESC 關閉 Modal', async ({ page }) => {
  await page.getByRole('button', { name: '訂閱' }).click();
  await expect(page.locator('#newsletter-modal')).toBeVisible();  // 先確認真的開了
  await page.keyboard.press('Escape');
  await expect(page.locator('#newsletter-modal')).toBeHidden();
});
```

**判斷原生彈窗 vs 網頁Modal的土方法**：原生彈窗長得很陽春、樣式跟網站風格不搭、換瀏覽器長相會變。

## 三、iframe（兩層都進得去）

```js
test('在 iframe 裡填卡號並付款', async ({ page }) => {
  const frame = page.frameLocator('#payment-frame');
  await frame.locator('#card-number').fill('4242424242424242');
  await frame.getByRole('button', { name: '付款' }).click();
  await expect(frame.locator('#pay-msg')).toHaveText('付款成功');  // 斷言也要掛在frame底下
});

// 巢狀 iframe：像剝洋蔥，一層一個串下去
test('巢狀 iframe：再進一層做 3D 驗證', async ({ page }) => {
  const otp = page.frameLocator('#payment-frame').frameLocator('#otp-frame');
  await otp.locator('#otp-code').fill('123456');
  await otp.getByRole('button', { name: '驗證' }).click();
  await expect(otp.locator('#otp-msg')).toHaveText('驗證成功');
});
```

**最常見錯誤**：進了 frame 填表，斷言卻寫回主頁面的 `page` 上，永遠找不到元素。**原則：進了哪一頁，就在哪一頁驗。**

**跨網域第三方 iframe 的策略性限制**（不是工具做不到）：第三方金流頁的內部不是你的受測物，對它斷言等於把測試命綁在別人改版上。實務做法：用金流商的測試模式（沙盒卡號），驗證點放在流程回到自己網站之後（訂單狀態、成功頁），不要斷言別人頁面裡的元素。

## 四、新分頁與彈出視窗（3個場景）

```js
test('等新分頁事件，再到新分頁上斷言', async ({ page, context }) => {
  const pagePromise = context.waitForEvent('page');  // 先建 promise，再點擊
  await page.locator('#report-link').click();
  const reportPage = await pagePromise;
  await reportPage.waitForLoadState();  // 等載入完再斷言
  await expect(reportPage.locator('#total')).toContainText('總營收');
});
```

`window.open` 彈出視窗跟新分頁在 Playwright 眼裡是同一種東西（`context` 裡多出來的一個 page），程式碼幾乎一樣。

**新分頁的決策點**：重點是「報表內容」就直接 `goto` 報表網址測內容，跳過開分頁動作更快更穩；如果「在新分頁開啟」本身就是需求（怕蓋掉使用者填到一半的表單），才需要走「等新分頁事件」那條——**這個判斷自動化不會幫你做**。

## 五、日期選擇器（4個場景）

```js
test('能直接填就直接填', async ({ page }) => {
  await page.locator('#start-date').fill('2026-08-01');  // type=date 欄位直接 fill，不用點月曆
  await page.locator('#end-date').fill('2026-08-15');
  ...
});

test('跨月選日期', async ({ page }) => {
  await page.locator('#effective-date').click();
  await page.locator('#cal-next').click();
  await page.locator('#cal-next').click();
  await expect(page.locator('#cal-title')).toHaveText('2026 年 10 月');  // 中途斷言：切月成功了嗎
  await page.locator('#cal-days').getByRole('button', { name: '15', exact: true }).click();  // exact:true必須加
  await expect(page.locator('#effective-date')).toHaveValue('2026-10-15');
});
```

- `type="date"` 欄位用 `fill` 塞 `yyyy-mm-dd` 就結束，瀏覽器原生小月曆點不到（跟原生彈窗同類，不在網頁DOM裡），fill 是正解不是繞路
- 自製月曆才需要點擊，`exact: true` 不能省（月曆同時有「1」跟「15」，包含比對會點錯）
- 多步驟測試在關卡處放中途斷言（如切月後先驗證標題），失敗時能直接定位死在哪一步

## 業界常見場景檢核表：兩個不該補的例外

- **跨網域第三方 iframe**：限制在策略不在工具（見上方 iframe 章節）
- **時區與日期格式**：限制在環境不在場景——CI主機UTC、本機台北，`new Date()` 接 `toISOString()` 會差一天。解法不是多寫UI測試，是在 `playwright.config.ts` 設 `use: { timezoneId: 'Asia/Taipei' }` 固定時區

---

## 撲空時的除錯口訣

測試說找不到元素但你明明看得到？先想三個：
1. 是不是在 iframe 裡？
2. 是不是在新分頁上？
3. 是不是原生彈窗？

把口訣連同錯誤訊息丟給 Claude Code，通常一輪破案。

---

## 對派哥的意義

跟同系列 Day10（Trace Viewer）合起來看：Day10 教「測試失敗後怎麼查根因」，這篇教「哪些元素一開始就容易讓測試卡住」——如果派哥用 Playwright 測 Vercel 部署（[[feedback_test_against_prod]]）時遇到「明明肉眼看得到，測試點不到」，先套上面的除錯口訣（iframe/新分頁/原生彈窗三選一），比亂猜快很多。

## 相關筆記

- [[playwright-trace-viewer-2026-08]] — 同系列Day10：測試失敗時用Trace Viewer查根因
- [[ai-coding-e2e-test-speed-myth-2026-07]] — 同作者：AI時代UI測試變快的真正原因
- [[playwright-page-object-model-2026-08]] — 同系列Day21：用Claude Code做Page Object Model重構
