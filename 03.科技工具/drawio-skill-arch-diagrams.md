# drawio-skill — 一句話生成專業架構圖

> 來源：https://github.com/Agents365-ai/drawio-skill
> 儲存日期：2026-06-13
> 標籤：#diagram #architecture #draw.io #claude-skill #automation

---

## 是什麼

Claude Code skill，讓你用白話描述需求，直接生成 `.drawio` 格式圖表，並自動匯出 PNG/SVG/PDF/JPG。底層呼叫 draw.io desktop CLI 渲染。

2712 stars（截至 2026-06-13），活躍維護中。

---

## 支援圖類型（6 種 preset）

| 類型 | 適用場景 |
|------|---------|
| Architecture | 系統架構、微服務 |
| Flowchart | 流程、排程邏輯 |
| ERD | 資料庫 schema |
| UML Class | 物件繼承關係 |
| Sequence | API 互動時序 |
| ML/Deep Learning | 模型架構 |

---

## 核心功能

- **Codebase → 圖**：掃描 Python/JS/Go/Rust 專案，自動產生 import graph 或 class hierarchy
- **10,000+ 官方 icon**：AWS/GCP/Azure/K8s/UML/BPMN 圖示正確對應
- **321 個 AI/LLM logo**：OpenAI、Claude、Gemini、LangChain 等，draw.io 原生沒有的都有
- **自我驗證**：讀自己生成的 PNG 檢查 overlap/clipped label/edge crossing，最多 2 輪自動修
- **5 輪迭代**：不滿意就繼續說，技能會針對性修改
- **Style capture**：可以從現有 `.drawio` 或圖片擷取視覺風格，套用到新圖

---

## 安裝

```bash
# 前置：安裝 draw.io desktop CLI
brew install --cask drawio

# 安裝 skill（擇一）
git clone https://github.com/Agents365-ai/drawio-skill.git ~/.claude/skills/drawio-skill

# 或用 Claude Code plugin marketplace
# /plugin marketplace add Agents365-ai/365-skills
# /plugin install drawio
```

---

## 使用範例

```
畫一個交易系統架構圖，包含 Mobile/Web client、API Gateway、Auth/Order/Payment service、Kafka、Redis
```

```
把這個 Python 專案的 module 結構視覺化
```

---

## 評估（對派哥的用途）

✅ **有用**，以下場景直接受益：
- 解釋 cc_processor BankAdapter 架構給別人看
- 畫 investment DB ERD（transactions/positions/accounts 關係）
- launchd 排程流程圖（哪些 plist 跑哪些腳本）
- 跟別人說明複雜 sync 流程（notion_sync、bank sync）

⚠️ **前提**：需要 draw.io desktop app 安裝，才能用 CLI 渲染匯出
