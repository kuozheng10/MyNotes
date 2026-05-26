---
title: "Netflix Canary + Kayenta：AI 時代的效能測試 SOP"
tags: [canary, kayenta, performance-testing, devops, CI-CD, netflix, 效能測試, rollback, ai-coding]
date: 2026-05-27
category: 03.知識庫
source: Telegram 派哥分享
---

## 核心問題

AI 寫程式速度變快，但測試環境模擬的是「你想像中的使用者行為」，不是真實流量。  
真實使用者帶來的資料、操作順序、流量分佈，測試環境還原不了。

---

## Netflix 的解法：三組叢集

| 叢集 | 說明 | 流量 |
|------|------|------|
| Production | 現有生產環境，跑很久的版本 | ~98% |
| Canary | 新版本 | ~1% |
| Baseline | **重點**：同時新開的舊版本，起跑點跟 canary 一樣 | ~1% |

### 為什麼要 Baseline？

跑很久的 Production 已經 JVM warm up、cache 熱、connection pool 就位。  
拿剛開的 Canary 跟熱的 Production 比 → Canary 一定看起來慢，但跟程式碼無關。

**結論：必須拿同時新開的 Baseline 跟 Canary 比，起跑點一樣才公平。**

---

## Kayenta：自動化 Canary 分析工具

Netflix + Google 共同開源，整合在 Spinnaker。

### 工作流程
1. 收集 Canary 和 Baseline 的所有指標（延遲、錯誤率、CPU、記憶體）
2. 跑統計檢定，比較兩邊差異
3. 算出 0~100 分數，自動判斷：
   - **Success**：放行，繼續往全量推
   - **Failure**：擋下，自動 rollback
   - **Marginal**：叫人來看

Netflix 一天跑上千次這種判斷。

### 最關鍵設計：相對比較，不訂絕對門檻

- 傳統做法：p95 < 200ms → 容易誤報，工程師很快把告警關掉
- Kayenta 做法：新版本跟同時間的 Baseline 比，有沒有退步

> 重點不是「現在跑多快」，而是「新舊版本比起來有沒有退步」。

統計方法：不假設常態分佈（延遲資料的尾部是偏的），比兩組資料的**相對排序**，比 t 檢定更貼近真實。

---

## Kayenta 的限制

Kayenta 不是「沒有門檻」，而是把單一指標的絕對門檻換成整體的相對比較。

但你還是要決定：
- 看哪些指標？
- 延遲比錯誤率重要嗎？
- 哪些指標是 critical（變差就直接判死）？
- 分數多少算 failure？

這些得對自己的系統夠熟才能設定好。**導入 Kayenta 前要先把這些想清楚，否則只是把錯誤的判斷標準自動化。**

---

## 正確導入順序

```
Step 1：PR 階段先有效能 gate（例如 k6 接 CI/CD）
         → 把「程式碼本身變慢」的明顯問題擋在合併前

Step 2：等團隊習慣之後，再往 Canary 走
         → 此時 Canary 才用來抓「程式碼本身沒變慢，但碰到真實流量就出包」的坑
```

**如果連基本效能 CI gate 都沒有，直接導入 Canary 會讓工程師每天改 bug 改到崩潰。**

---

## 給 AI 寫程式團隊的建議

- AI 讓寫程式變快，但驗證要更聰明，不是更隨便
- 光靠測試環境壓測不夠（模擬不出真實行為）
- 光靠監控不夠（看到問題時使用者已受影響）
- Canary 解決的是中間那塊：真上線、只給 1%、有問題自動撤

---

## 參考資料

- Netflix Tech Blog: Automated Canary Analysis at Netflix with Kayenta
- Spinnaker 官方文件: How canary judgment works / Best practices for configuring canary
- Google Cloud: Introducing Kayenta
