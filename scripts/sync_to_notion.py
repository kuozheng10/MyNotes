#!/usr/bin/env python3
"""
Sync changed Markdown files in MyNotes repo to Notion database.
Triggered by GitHub Actions on push to main.
"""

import os
import subprocess
import frontmatter
from pathlib import Path
from notion_client import Client

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
DATABASE_ID = os.environ["NOTION_DATABASE_ID"]

notion = Client(auth=NOTION_TOKEN)


def get_changed_md_files():
    """Get list of MD files to sync.
    On workflow_dispatch (SYNC_ALL=true), returns all MD files.
    On push, returns only files changed in last commit.
    """
    if os.environ.get("SYNC_ALL") == "true":
        files = [str(p) for p in Path(".").rglob("*.md")
                 if p.name != "README.md"]
        return files

    result = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=AM", "HEAD~1", "HEAD"],
        capture_output=True, text=True
    )
    files = [f for f in result.stdout.strip().split("\n")
             if f.endswith(".md") and f != "README.md" and f]
    return files


def md_to_blocks(text):
    """Convert markdown text to Notion block objects (basic)."""
    blocks = []
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]

        # Code block
        if line.startswith("```"):
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                code_lines.append(lines[i])
                i += 1
            blocks.append({
                "object": "block",
                "type": "code",
                "code": {
                    "rich_text": [{"type": "text", "text": {"content": "\n".join(code_lines)}}],
                    "language": "plain text"
                }
            })

        # Heading 2
        elif line.startswith("## "):
            blocks.append({
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [{"type": "text", "text": {"content": line[3:]}}]
                }
            })

        # Heading 3
        elif line.startswith("### "):
            blocks.append({
                "object": "block",
                "type": "heading_3",
                "heading_3": {
                    "rich_text": [{"type": "text", "text": {"content": line[4:]}}]
                }
            })

        # Bullet point
        elif line.startswith("- ") or line.startswith("• "):
            blocks.append({
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [{"type": "text", "text": {"content": line[2:]}}]
                }
            })

        # Divider
        elif line.strip() in ("---", "***", "___"):
            blocks.append({"object": "block", "type": "divider", "divider": {}})

        # Non-empty paragraph
        elif line.strip():
            blocks.append({
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{"type": "text", "text": {"content": line}}]
                }
            })

        i += 1

    return blocks


def find_existing_page(title):
    """Search for an existing Notion page with this title."""
    response = notion.databases.query(
        database_id=DATABASE_ID,
        filter={"property": "Name", "title": {"equals": title}}
    )
    results = response.get("results", [])
    return results[0]["id"] if results else None


def sync_file(filepath):
    """Sync one MD file to Notion."""
    post = frontmatter.load(filepath)
    title = post.get("title") or Path(filepath).stem
    content = post.content
    tags = post.get("tags", [])
    source = post.get("source", "")
    date = str(post.get("date", ""))

    # Build properties
    properties = {
        "Name": {"title": [{"text": {"content": title[:2000]}}]},
    }
    if tags:
        properties["Tags"] = {
            "multi_select": [{"name": str(t)[:100]} for t in tags[:10]]
        }
    if date:
        properties["Date"] = {"rich_text": [{"text": {"content": date}}]}
    if source:
        properties["Source"] = {"url": source} if source.startswith("http") else \
                               {"rich_text": [{"text": {"content": source}}]}

    # Convert content to blocks (Notion limit: 100 blocks per request)
    blocks = md_to_blocks(content)[:100]

    existing_id = find_existing_page(title)

    if existing_id:
        # Update properties
        notion.pages.update(page_id=existing_id, properties=properties)
        # Clear old content and rewrite
        old_blocks = notion.blocks.children.list(block_id=existing_id).get("results", [])
        for block in old_blocks:
            try:
                notion.blocks.delete(block_id=block["id"])
            except Exception:
                pass
        if blocks:
            notion.blocks.children.append(block_id=existing_id, children=blocks)
        print(f"  Updated: {title}")
    else:
        # Create new page
        page = notion.pages.create(
            parent={"database_id": DATABASE_ID},
            properties=properties,
            children=blocks
        )
        print(f"  Created: {title}")

    return True


def main():
    changed_files = get_changed_md_files()
    if not changed_files:
        print("No changed MD files found.")
        return

    print(f"Syncing {len(changed_files)} file(s) to Notion...")
    for filepath in changed_files:
        path = Path(filepath)
        if not path.exists():
            print(f"  Skipped (deleted): {filepath}")
            continue
        try:
            sync_file(path)
        except Exception as e:
            print(f"  Error syncing {filepath}: {e}")

    print("Done.")


if __name__ == "__main__":
    main()
