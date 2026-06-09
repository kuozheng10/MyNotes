# claude-skill-social-post

> Claude Code skill：學你的 FB 語氣 → 排 14 天內容日曆 → 自動發 FB/IG/Threads/X
> 作者：駱君昊 (Hao) · v1.0.0（2026-05-31）
> GitHub：https://github.com/Hao0321/claude-skill-social-post

---

## 這個 skill 在幹嘛

1. **學語氣**：Claude 用 Chrome MCP 爬你的 FB 最近 20 篇，萃取口語/emoji/用字習慣，寫成 `style_profile.md`
2. **排日曆**：依目標（擴社群/轉換付費/品牌建立）＋頻率，用 viral 公式排 14 天每日內容
3. **生草稿 + 自動發**：「今天發一篇」→ 依日曆選公式 → 問題材 → 生草稿 → 你回「確認」→ 自動發四平台
4. **追蹤戰績**：每 2 小時查流量，寫進戰績表；每兩週 review，好公式加頻、差的換

## 實戰成效（作者自測，小帳號 <5K 粉）

| 變體 | 觀眾 | 讚 | 留言 | 非追蹤者 |
|------|------|-----|------|----------|
| Day 1 promo (F6b-A) | 75,071 | 380 | 457 | 96.5% |
| Day 6 復盤 (F6b-B) | 18,603 | 100 | 89 | 92.6% |
| 5/5 social proof (F6b-D) | 44,110 | 265 | 342 | 95.3% |

→ Line 群從 800 → 4,568+；3 次都跨 90% 非追蹤者天花板

## 7 個 Viral 公式

| # | 公式 | 平台 |
|---|------|------|
| F1 | Day-N 開發日誌（連載） | Threads |
| F2 | 截圖先丟再講（提升 dwell time） | FB/Threads |
| F3 | 實測翻車版（save 率高） | FB 長文 |
| F4 | 社群里程碑 + 投票 | FB |
| F5 | 工具對打（可被搜到） | X thread |
| F6a | 推廣 + 邀請碼 | FB/IG |
| **F6b** | **meta-ship（ship 自己做的東西）** | **FB/IG ← 最強** |
| F7 | POV 吐槽（回覆率 >5% 最大推送） | Threads |

## 安裝

```bash
git clone https://github.com/Hao0321/claude-skill-social-post.git
cp -r claude-skill-social-post/social-post ~/.claude/skills/social-post
cd ~/.claude/skills/social-post
mv style_profile.example.md style_profile.md
mv content_plan.example.md content_plan.md
```

需求：Claude Code + Chrome MCP 已裝 + Chrome 已登入社群帳號

## 使用指令

```
幫我學 FB 風格        # 爬 FB 20 篇 → 生 style_profile.md
幫我排社群內容日曆    # 排 14 天 → 存 content_plan.md
今天發一篇            # 按日曆生草稿 → 確認後自動發
```

## 版本

- v1.0.0（2026-05-31）：25 cases / 32 條規則 / 4 個 Mode（A/B/C/Thread F19）
- 姐妹 skill：[code-cleanup](https://github.com/Hao0321/claude-skill-code-cleanup) — codebase audit

## 限制

- FB DOM 常變，有 fallback 但非萬無一失
- IG 要圖，純文字貼文自動改發 Threads
- Threads 桌面版無帳號切換（需手機）
- 發文前硬規則要你回「確認」才執行

## 授權

MIT License
