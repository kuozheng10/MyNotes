#!/usr/bin/env python3
"""
Sync Markdown files in MyNotes repo to Notion database.
Uses requests directly to avoid notion-client version issues.
"""

import os
import subprocess
import json
import requests
import frontmatter
from pathlib import Path

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
DATABASE_ID = os.environ["NOTION_DATABASE_ID"]

HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
}


def notion_get(path):
    r = requests.get(f"https://api.notion.com/v1{path}", headers=HEADERS)
    r.raise_for_status()
    return r.json()


def notion_post(path, data):
    r = requests.post(f"https://api.notion.com/v1{path}", headers=HEADERS, json=data)
    r.raise_for_status()
    return r.json()


def notion_patch(path, data):
    r = requests.patch(f"https://api.notion.com/v1{path}", headers=HEADERS, json=data)
    r.raise_for_status()
    return r.json()


def notion_delete(path):
    r = requests.delete(f"https://api.notion.com/v1{path}", headers=HEADERS)
    return r.json()


def get_md_files():
    if os.environ.get("SYNC_ALL") == "true":
        return [str(p) for p in Path(".").rglob("*.md") if p.name != "README.md"]
    result = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=AM", "HEAD~1", "HEAD"],
        capture_output=True, text=True
    )
    return [f for f in result.stdout.strip().split("\n")
            if f.endswith(".md") and f != "README.md" and f]


def parse_inline(text):
    """Convert markdown inline formatting to Notion rich_text array."""
    import re
    parts = []
    pattern = re.compile(r'\*\*(.+?)\*\*|\*(.+?)\*|`(.+?)`')
    last = 0
    for m in pattern.finditer(text):
        if m.start() > last:
            parts.append({"type": "text", "text": {"content": text[last:m.start()]}})
        if m.group(1):  # bold
            parts.append({"type": "text", "text": {"content": m.group(1)},
                          "annotations": {"bold": True}})
        elif m.group(2):  # italic
            parts.append({"type": "text", "text": {"content": m.group(2)},
                          "annotations": {"italic": True}})
        elif m.group(3):  # inline code
            parts.append({"type": "text", "text": {"content": m.group(3)},
                          "annotations": {"code": True}})
        last = m.end()
    if last < len(text):
        parts.append({"type": "text", "text": {"content": text[last:]}})
    return parts or [{"type": "text", "text": {"content": text}}]


def md_to_blocks(text):
    blocks = []
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                code_lines.append(lines[i])
                i += 1
            blocks.append({
                "object": "block", "type": "code",
                "code": {"rich_text": [{"type": "text", "text": {"content": "\n".join(code_lines)[:2000]}}], "language": "plain text"}
            })
        elif line.startswith("## "):
            blocks.append({"object": "block", "type": "heading_2",
                           "heading_2": {"rich_text": parse_inline(line[3:200])}})
        elif line.startswith("### "):
            blocks.append({"object": "block", "type": "heading_3",
                           "heading_3": {"rich_text": parse_inline(line[4:200])}})
        elif line.startswith("- ") or line.startswith("• "):
            blocks.append({"object": "block", "type": "bulleted_list_item",
                           "bulleted_list_item": {"rich_text": parse_inline(line[2:2000])}})
        elif line.strip() in ("---", "***", "___"):
            blocks.append({"object": "block", "type": "divider", "divider": {}})
        elif line.strip():
            blocks.append({"object": "block", "type": "paragraph",
                           "paragraph": {"rich_text": parse_inline(line[:2000])}})
        i += 1
    return blocks[:100]


def find_existing_page(title):
    data = notion_post(f"/databases/{DATABASE_ID}/query", {
        "filter": {"property": "Name", "title": {"equals": title}}
    })
    results = data.get("results", [])
    return results[0]["id"] if results else None


def sync_file(filepath):
    post = frontmatter.load(filepath)
    title = str(post.get("title") or Path(filepath).stem)[:255]
    content = post.content
    tags = post.get("tags", [])
    source = str(post.get("source", ""))
    date = str(post.get("date", ""))
    category = str(post.get("category", ""))

    properties = {
        "Name": {"title": [{"text": {"content": title}}]},
        "Tags": {"multi_select": [{"name": str(t)[:100]} for t in (tags or [])[:10]]},
        "Date": {"rich_text": [{"text": {"content": date[:100]}}]},
        "Category": {"rich_text": [{"text": {"content": category[:100]}}]},
    }
    if source.startswith("http"):
        properties["Source"] = {"url": source[:2000]}
    else:
        properties["Source"] = {"url": None}

    blocks = md_to_blocks(content)
    existing_id = find_existing_page(title)

    if existing_id:
        notion_patch(f"/pages/{existing_id}", {"properties": properties})
        old_blocks = notion_get(f"/blocks/{existing_id}/children").get("results", [])
        for b in old_blocks:
            notion_delete(f"/blocks/{b['id']}")
        if blocks:
            notion_post(f"/blocks/{existing_id}/children", {"children": blocks})
        print(f"  Updated: {title}")
    else:
        notion_post("/pages", {
            "parent": {"database_id": DATABASE_ID},
            "properties": properties,
            "children": blocks
        })
        print(f"  Created: {title}")


def main():
    files = get_md_files()
    if not files:
        print("No MD files to sync.")
        return
    print(f"Syncing {len(files)} file(s) to Notion...")
    for f in files:
        p = Path(f)
        if not p.exists():
            print(f"  Skipped (deleted): {f}")
            continue
        try:
            sync_file(p)
        except Exception as e:
            print(f"  Error syncing {f}: {e}")
    print("Done.")


if __name__ == "__main__":
    main()
