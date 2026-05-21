---
title: AI 為何不會設計 Test Case — 訓練資料根本不存在這件事
tags: [ai-coding, testing, QA, test-design, LLM盲點]
date: 2026-04-28
category: 03.科技工具
---

## 核心洞見

> AI 不會設計 test case，不是因為不夠聰明，是因為人類從來沒把「如何設計 test case」大規模寫下來給它學。

「寫測試程式」和「設計測試案例」是兩件完全不同的事：

| | 寫測試程式 | 設計測試案例 |
|--|-----------|------------|
| 本質 | 體力活 | 腦力活 |
| AI 能力 | 強到爆 | 很弱 |
| 來源 | GitHub/Stack Overflow | 資深 QA 的腦袋裡 |

---

## 為什麼 AI 學不到測試設計

測試設計的思考過程存在哪裡？

- 資深 QA 腦袋裡
- Code review 時的口頭對話
- 白板上畫完就擦掉的等價類
- Bug triage 的即席討論
- 公司內部不外流的 test plan

這些從來沒有被大規模寫成公開文字。LLM 的訓練資料有海量測試程式碼，但「測試設計過程」的比例極低。**模型變大也解決不了，因為這不是容量問題，是資料根本不存在。**

---

## AI 會寫「鏡像測試」

訓練資料裡 test 大多跟 implementation 同時出現，AI 學到的是：
- 「測試 = 描述實作做什麼」
- 而不是「測試 = 獨立驗證需求」

```python
def add(a, b):
    return a - b   # bug！

# AI 生成的測試：
def test_add():
    assert add(2, 3) == -1   # 把 bug 當規格驗證進去了
```

研究數據：AI 生成測試在 mutation testing 上的得分，平均比資深工程師低 30-50%。

---

## 正確用法：AI 當副駕駛

### 1. 先寫測試名稱，再叫 AI 補內容

命名階段 = 設計階段。能寫出這幾行，設計已完成 80%：

```
test_order_total_excludes_cancelled_items
test_order_total_applies_member_discount_before_tax
test_order_total_rejects_negative_quantity
```

AI 補實作很好，但這幾行命名不能外包給 AI。

### 2. 給 AI 起點，不給終點

❌「幫我設計測試」
✅「我想到 5 個 case，請補類似的 5 個」

### 3. 用 AI brainstorm，人來篩選

問：「這個 function 有哪些邊界情況我沒想到？」
→ AI 列 20 個 → 你篩 5 個 → 不要全收

### 4. 外化測試思考

寫 PR description 時記錄「為什麼選這幾個 case」→ 團隊知識資產積累。

---

## 對派哥的意義

cc_processor / My Wallet Trip 的 API 串接（Notion、Google、Telegram）是邊界點，最容易出現 AI 預測不到的錯誤。
- 整合測試案例要自己設計，不能全交給 AI 生成
- 新功能前先列測試名稱（等同 SBE 情境），再叫 Claude 補實作

---

## 連結筆記

- [[ai-coding-qa-myths]] — AI 時代品質管理迷思
- [[genai-pretotyping-wrong-direction]] — AI 加速但做錯方向
- [[exploratory-testing-sbtm]] — 探索性測試
- [[SDD-vs-SBE]] — 規格由範例 vs 規格驅動開發
