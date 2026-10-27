from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import re

queue = Path("_queue")
posts = Path("_posts")
posts.mkdir(exist_ok=True)

def approved(text: str) -> bool:
    head = text.split("---", 2)
    return len(head) >= 3 and re.search(r"(?mi)^approved:\s*true\s*$", head[1]) is not None

candidates = sorted(p for p in queue.glob("*.md") if approved(p.read_text(encoding="utf-8")))
if not candidates:
    print("No approved drafts.")
    raise SystemExit(0)

src = candidates[0]
text = src.read_text(encoding="utf-8")
today = datetime.now(ZoneInfo("Asia/Tokyo")).strftime("%Y-%m-%d")
text = re.sub(r"(?mi)^date:\s*.*$", f"date: {today}", text, count=1)
text = re.sub(r"(?mi)^approved:\s*true\s*\n?", "", text, count=1)
slug = src.stem
if slug.startswith("draft-"):
    slug = slug[6:]
dst = posts / f"{today}-{slug}.md"
if dst.exists():
    raise SystemExit(f"Destination already exists: {dst}")
dst.write_text(text, encoding="utf-8")
src.unlink()
print(f"Published {dst}")
