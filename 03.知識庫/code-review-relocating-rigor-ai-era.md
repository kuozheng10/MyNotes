# Code Review in the AI Era — Relocating Rigor（嚴謹搬家）

> 來源：派哥 2026-06-05 工作心得
> 主題：AI 時代的 code review 哲學，從 Synology 逐行 review 到現在的架構師視角

---

## 核心概念：嚴謹度不會消失，只是搬位置

Chad Fowler 的說法：**Relocating Rigor**
— 嚴謹往兩頭搬，中間那層交給 AI

```
以前：  [Spec] → [逐行 Code Review ← 嚴謹集中這裡] → [Release]

現在：  [Spec/Intention ← 嚴謹] → [AI 實作] → [Verification ← 嚴謹]
                                        ↑
                               Cross Model / Cross Context review
```

---

## 三層架構

### 1. 上游：Intention & Spec Review（最重要，人工不可外包）
- 在 AI 動手前，確認 spec 對不對、業務需求有沒有抓到
- 先在腦袋裡（或一張圖上）把方案 review 完，才放 agent 去做
- Addy Osmani：reviewer 角色更像 editor 或 architect，不是 inspector

### 2. 中間：Cross Model + Cross Context Review
- **Cross Context**：review 的 agent 不給它產出時的對話歷史，讓它在乾淨 session 裡只看最終產物
  - Claude Code 的 sub-agent 天生就是 clean context
  - 研究依據：CCR（Cross-Context Review）— 切開 context 後抓錯能力上升
- **Cross Model**：換一個 model 來看，不同架構 blind spot 不同
  - 用 Codex review Claude 寫的，反過來也行

### 3. 下游：架構級 Verification（看圖不看 code）
- 要求 AI 先產出 **Conceptual Map**（純文字架構圖），看骨架對不對
- Technical Architect 視角：擴展性、穩定性、延遲、高流量
- 只有 AI 卡很久做不出來時，才下去逐行翻 code
- Martin Fowler 的 **Refinement Code Review**：review 不是 merge 前的閘門，是持續精煉 codebase 健康的活動

---

## Conceptual Map 是什麼？

**純文字的高層架構圖**，目的是讓人用 30 秒看懂系統骨架，不用讀 code。

通常長這樣（tree 或 outline 格式）：
```
UserService
├── Auth (JWT + refresh token)
│   └── 依賴 Redis session store
├── CRUD (Postgres)
│   └── 軟刪除，無硬刪
└── Event (→ Kafka)
    └── 訂閱者：NotificationService
```

不是 UML，不是流程圖，就是一份讓你能 review 架構邏輯的文字樹狀圖。

---

## 防止 AI 偷懶：Acceptance Metrics 先寫

- AI 會 rationalization（合理化沒做完的事）和 hallucination
- 對付方法：Cross Session 驗證 + 驗收指標要先定義清楚
- 指標夠明確 → AI 沒有模糊空間敷衍；指標含糊 → 它用最省力方式交差

---

## 現在的落地三件事

1. **腦力集中在 intention 跟業務邊界** — 怎麼定義意圖、切乾淨業務邏輯
2. **AI 動手前，先把架構原型看過一遍** — 它是照著我已點頭的方案在跑
3. **後期 code review 大幅簡化** — 只確認 bounded context 有沒有守住、邊界有沒有跑掉

---

## 相關概念

- [[addy-osmani-harness-engineering-deep-dive]] — AI 工程哲學
- [[agent-skills-standard]] — Claude Code sub-agent 架構
- [[agentic-orchestration-cognitive-load-theory]] — 認知負荷理論
