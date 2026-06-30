---
tags: [docker, container, apple-silicon, mac, ai-coding, devops, swift]
source: https://github.com/apple/container
date: 2026-06-30
---

# Apple 官方 Container 工具：取代 Docker Desktop

> **一句話**：蘋果親自下場做容器工具，用 Swift 重寫、不套 Docker 殼，針對 Apple Silicon 深度優化，比 Docker Desktop 快又輕。

---

## 背景

隨著 AI Coding 爆發，越來越多人在 Mac 本地跑容器、部署 Agent 後端。但 Docker Desktop 一直被嫌：啟動慢、吃資源、風扇狂轉，開幾個服務整台電腦就變鈍。

蘋果在 GitHub 開源官方容器工具 **Container**，上線不久就衝高：

| 指標 | 數字 |
|------|------|
| Stars | 45,300（單週暴漲 7,000+） |
| Forks | 1,300 |
| Open Issues | 264 |
| Open PRs | 134 |
| Latest Release | 1.0.0（2026-06-09） |
| License | Apache-2.0 |

---

## 核心特色

- **97.9% Swift 寫成**，不是套殼 Docker，是重寫
- **針對 Apple Silicon 深度優化**，不走 Docker 那套厚重中間層
- 直接呼叫 **macOS 最新虛擬化能力**，用輕量級 VM 跑 Linux 容器
- **OCI 相容**：可跟任何標準容器登錄處（registry）互動，指令跟 Docker 幾乎一比一相容
- 實際體驗：啟動快很多、資源輕很多，沒有 Docker Desktop 越開越卡的感覺

---

## 系統需求 ⚠️

- **必須是 Apple Silicon Mac**（Intel Mac 不支援）
- **macOS 26 或更新版本**

> 派哥如果要用，先確認自己 macOS 版本是不是 26+。

---

## 安裝 / 使用

```bash
brew install container
```

或從 GitHub Release 頁面下載簽署過的安裝程式，雙擊安裝。

啟動系統服務：
```bash
container system start
```

跑容器：
```bash
container run hello-world
```

---

## 跟 Docker 的差異

| | Docker Desktop | Apple Container |
|---|---|---|
| 底層 | 厚重中間層 + Linux VM（QEMU/HyperKit） | 直接呼叫 macOS 虛擬化框架，輕量 VM |
| 寫成語言 | Go | Swift |
| 平台限制 | 跨平台 | 只支援 Apple Silicon + macOS 26+ |
| 啟動速度 / 資源 | 較重、較慢 | 明顯更輕更快 |
| 指令相容性 | — | 跟 Docker CLI 幾乎一比一相容 |

---

## 開發狀態

積極開發中，目前穩定性只在 patch 版本（如 0.1.1→0.1.2）內保證，**minor 版本可能有破壞性變更**，正式環境採用前要注意。

---

## 對派哥的意義

- 本地跑 AI Agent / 部署微服務 / AI Coding 開發 → 可以評估從 Docker Desktop 換過來，省資源
- 前提：手上 Mac 要先升到 macOS 26+
- 還在早期（v1.0.0 剛發），正式取代 Docker 前建議先小範圍試用觀察穩定性

---

## 來源

- https://github.com/apple/container
