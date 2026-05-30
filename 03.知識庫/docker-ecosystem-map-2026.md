# Docker 生態系地圖（2026）

> 來源：https://hackercat.org/container/docker-map （駭客貓咪，Docker Captain）
> 整理日期：2026-05-30

Docker 已經不是單一的 container tool，而是圍繞開發者工作流程的完整平台。

---

## 全景圖

```
本機開發          → Docker Desktop, Compose, Docker Debug
Image Build       → BuildKit/Buildx, Build Cloud
Image 管理        → Docker Hub, Docker Scout, Hardened Images (DHI)
測試              → Testcontainers (Desktop / Cloud)
擴充              → Docker Extensions
AI 模型           → Docker Model Runner, MCP Catalog & Toolkit
AI Agent 輔助     → Gordon (docker ai), Docker Sandboxes
雲端資源          → Docker Offload, Build Cloud
```

---

## 15 個產品一覽

### 本機開發

**1. Docker Desktop**
- 不只是 GUI，是開發者的 Docker 工作站
- 整合：CLI / Compose / Kubernetes / Extensions / Scout / Build / AI 功能
- 官方定位：unified development environment

**2. Docker Compose**
- 用 `compose.yaml` 描述多服務環境（app + db + redis...）
- 讓環境變成文件 → 可版本控制 → 降低溝通成本
- `Compose Watch`：監看檔案變更，自動 hot reload

**3. Docker Debug**
- 解決「slim image 無 bash 但需要 debug」的矛盾
- 不用把工具塞回 image，有獨立 debug workflow

---

### Image Build

**4. BuildKit / Buildx**
- Docker 現代 build backend，比 legacy builder 更快、更強
- 支援 multi-platform build：`--platform linux/amd64,linux/arm64`
- 支援 SBOM 與 provenance attestations（供應鏈安全）
  ```bash
  docker buildx build --sbom=true --provenance=mode=max -t my-app:secure .
  ```

**5. Docker Build Cloud**
- 把 build offload 到雲端，但 workflow 不變
- 解決：build 太慢 / multi-arch / cache 不共享 / CI runner 不足
- 重點不只是快，而是讓 build 環境一致

---

### Image 管理與安全

**6. Docker Hub**
- 不只是放 image 的地方，而是 image 管理 + 協作 + 驗證平台
- 重要概念：tag / digest / registry / official image / verified publisher / trusted content
- 提供 private repo / organization / access token / CI/CD 整合

**7. Docker Scout**
- image 安全掃描 + software supply chain security
- 分析套件漏洞、提供 remediation 建議
- 整合 Docker Desktop、Docker Hub、CI/CD
- 啟用後持續追蹤 image，新漏洞出現時重新計算

**8. Docker Hardened Images (DHI)**
- minimal + secure + production-ready base images
- 解決：各團隊亂選 base image（`FROM ubuntu:latest`）的治理問題
- 目標：把安全基線往前推到 base image 層級

---

### 測試

**9. Testcontainers**
- 測試時用真實 container 跑 PostgreSQL / Redis / Kafka，而不是 mock
- 讓 integration test 更貼近真實環境
- 支援 Java / Go / Python / Node.js 等
- **Testcontainers Cloud**：把 container 啟動 offload 到雲端，加速 CI

---

### 平台擴充

**10. Docker Extensions**
- 讓第三方工具整合進 Docker Desktop（marketplace）
- 可自建 Extension 透過 Extensions SDK

---

### AI 時代功能

**11. Docker Model Runner**
- 用 Docker CLI 管理與執行 AI 模型（LLM、其他 AI model）
- 來源：Docker Hub / OCI registry / Hugging Face
- 支援 OpenAI-compatible + Ollama-compatible APIs
- 模型以 OCI Artifact 發佈（GGUF、Safetensors）
- 把 AI model workflow 融入熟悉的 Docker workflow

**12. Docker MCP Catalog & Toolkit**
- 解決：MCP server 從哪裡來、怎麼驗證、怎麼管理
- 300+ verified MCP servers，包成 container images
- 企業重點：AI Agent 連 GitHub / Slack / DB 時的權限與安全管理

**13. Gordon（docker ai）**
- Docker 官方 AI 助理，針對 Docker workflow 設計
- 能做：解釋概念、讀寫 Dockerfile、debug container、管理資源
- 執行前要求 approval，不會自動修改
- 對新手：幫你找到 troubleshooting 方向

**14. Docker Sandboxes**
- 讓 AI coding agent 在隔離的 microVM sandbox 執行
- 每個 sandbox 有獨立 Docker daemon / filesystem / network
- Agent 可 build / install / modify，但不碰 host system
- 為 Codex / Claude Code / Gemini CLI 等工具的企業導入做準備

**15. Docker Offload**
- 本機 workflow（Desktop / CLI / Compose），但執行資源在雲端
- 適合：筆電效能不足 / VDI 環境 / 需要大 CPU/GPU / 統一開發環境
- 核心價值：不改變工程師習慣

---

## 核心洞察

> Docker 從「啟動容器的工具」 → 「開發者工作流程的完整平台」

- **AI 時代延伸**：Model Runner + MCP + Gordon + Sandboxes = 把 AI 工具納入 Docker 生態
- **供應鏈安全**：Scout + DHI + SBOM/provenance = DevSecOps 整合
- **雲端延伸**：Build Cloud + Offload = 本機習慣 + 雲端資源

---

## 相關筆記

- [[senior-dev-ai-era-harness-complexity]] — AI 時代的工程師角色
- [[vibe-coding-dodonov-stanley-ai-tool]] — Vibe Coding 案例
