---
title: threads-cli — 用 Rust 寫的 Threads 命令列工具
tags: [CLI, Rust, Threads, Meta, 自動化, 社群媒體, 排程]
date: 2026-04-12
category: AI工具
source: https://github.com/pukpuklouis/threads-cli
---

## 這是什麼

用 Rust 寫的 CLI 工具，可從終端機管理 Meta Threads：發文、建立 thread、排程、查看數據。
適合開發者、內容創作者、自動化愛好者。

---

## 安裝

```bash
# macOS/Linux 一鍵安裝
curl -fsSL https://raw.githubusercontent.com/pukpuklouis/threads-cli/main/install.sh | sh

# 或從 source 編譯（需 Rust 1.70+）
git clone https://github.com/pukpuklouis/threads-cli.git
cargo build --release
```

需要先在 Meta for Developers 建立 App，取得 App ID + App Secret。

---

## 主要功能

### 認證

```bash
threads-cli auth login    # OAuth 2.0 登入（本地 HTTPS callback: localhost:8420）
threads-cli auth logout
threads-cli auth status
```

### 發文

```bash
# 單篇貼文（含預覽確認）
threads-cli post "Hello Threads"

# Thread 串（用 --- 分隔，自動串連）
threads-cli post "第一則\n---\n第二則\n---\n第三則"

# 排程發文
threads-cli schedule --time "2026-04-13T09:00:00"
```

### Draft 草稿管理

- 支援 Markdown + YAML frontmatter 格式
- 本地存稿，確認後再發布

### 數據分析

```bash
threads-cli analytics    # 查看 impressions、互動數、回覆數
```

### 用戶資料

```bash
threads-cli profile      # 顯示帳號資訊、粉絲數
```

---

## 技術細節

- 語言：Rust（async/await + tokio）
- CLI：clap 4
- HTTP：reqwest + rustls（HTTPS）
- OAuth：local callback server on port 8420，支援 fallback URL
- 版本：v0.1.1，11 GitHub stars

---

## 評估：對派哥有沒有用？

目前用處有限，原因：

- 派哥目前沒有 Threads 帳號作業需求
- 需要自建 Meta Developer App（繁瑣）
- 功能基礎，v0.1.1 早期版本

**如果未來有這些需求才值得用**：
- 需要批次發 Threads 貼文（如每天推送 MyNotes 精華）
- 想把 TG → Threads 自動同步
- 想用 script 做排程社群發文

**更接近派哥現有需求的替代方案**：
- TG Bot（已有）→ 直接 Claude 回應
- Gmail 自動化（已有）→ 已用 Python + Gmail API
