---
tags: [telegram, claude-code, launchd, debugging]
date: 2026-07-23
---

# Telegram Bot 同一 Token 雙 Process 衝突（getUpdates Conflict）

## 現象

2026-07-23 晚上，TG 跟 Claude Code 的連線斷了三四次。派哥回報「最近TG連線一直斷」。

## 排查過程

查 `~/claude-telegram-error.log` 跟 `~/claude-telegram.log`，抓到：

```
telegram.error.Conflict: terminated by other getUpdates request;
make sure that only one bot instance is running
```

`ps aux` 確認有兩個 process 同時在跑：

1. `~/Library/LaunchAgents/com.claude.telegram.plist`（launchd job，`KeepAlive=true`，開機自動啟動）跑 `~/Documents/MyClaude/tg-bot.py` — 這是很久以前「取代壞掉的 `--channels` TUI」寫的 standalone bot bridge，早就被 plugin 取代但一直沒清掉
2. Claude Code 的 Telegram plugin channel（`server.ts`/bun）

兩個都讀同一個 `~/.claude/channels/telegram/.env` 裡的 bot token，對 Telegram API 打 `getUpdates` 長輪詢。**Telegram 同一個 bot token 只允許一個 process 在 poll**，兩個同時搶就會互踢，一個成功另一個馬上收到 409 Conflict 斷線，過一陣子又反過來，造成看起來像「連線不穩」的假象。

## 根因

舊的 launchd 自動啟動 job 沒清掉，跟現在用的 plugin channel 撞在一起。這件事其實在 `project_telegram_reconnect` memory 裡本來就寫了「不用 launchd 自動啟動，避免跟 session 裡的 channels process 衝突」——但這個 plist 是更早期留下的殘留，繞過了這條規則。

## 處置

```bash
launchctl unload ~/Library/LaunchAgents/com.claude.telegram.plist
mv ~/Library/LaunchAgents/com.claude.telegram.plist \
   ~/Library/LaunchAgents/com.claude.telegram.plist.disabled
```

改名而非刪除，保留復原可能性。之後 tg-bot.py 不會再開機自動啟動。

## 一般化教訓

- Telegram bot 斷線／衝突，不要只當網路問題重連，先查 `ps aux | grep -i telegram` 有沒有不該存在的重複 process
- 同一個 bot token 的長輪詢（`getUpdates`）是互斥的，只要看到 log 裡有 `Conflict: terminated by other getUpdates request`，就是雙 process 撞車，不是網路或 Telegram 服務問題
- 舊的自動化（launchd/cron/systemd）被新方案取代後，一定要真的移除或停用，不能只是「換了新的就不管舊的」——殘留的自動啟動 job 是這類衝突最常見的來源
