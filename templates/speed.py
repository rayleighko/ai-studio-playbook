"""Nightly silence metrics for a multi-session AI studio.

usage: python speed.py OWNER/REPO MMDD BOARD_ISSUE [MORE_ISSUES...]
Needs the GitHub CLI (gh) logged in. Counts, per role prefix, lines posted that day
and the longest silence between 09:00 and 22:00 local time (UTC+9 by default).
"""
import json, subprocess, sys
from datetime import datetime, timedelta, timezone

TZ = timezone(timedelta(hours=9))
ROLES = ["relay", "coordinator", "core", "ui", "art", "pix", "rbx"]

repo, day, issues = sys.argv[1], sys.argv[2], sys.argv[3:]
d0 = datetime(datetime.now().year, int(day[:2]), int(day[2:]), tzinfo=TZ)
since = d0.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
rows = []
for n in issues:
    out = subprocess.run(["gh", "api", f"repos/{repo}/issues/{n}/comments?per_page=100&since={since}", "--paginate"],
                         capture_output=True, text=True, encoding="utf-8").stdout.replace("][", ",")
    for c in (json.loads(out) if out.strip() else []):
        t = datetime.strptime(c["created_at"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).astimezone(TZ)
        if t >= d0:
            rows.append((t, c["body"].strip().lower()))

by = {}
for t, b in rows:
    role = next((r for r in ROLES if b.startswith(r) or b.startswith(f"[{r}]")), "other")
    by.setdefault(role, []).append(t)

end = min(d0.replace(hour=22), datetime.now(TZ))
print(f"{day}: {len(rows)} lines")
for role, ts in sorted(by.items()):
    pts = [d0.replace(hour=9)] + sorted(t for t in ts if 9 <= t.hour < 22) + [end]
    gap, at = max(((b - a).total_seconds() / 60, a) for a, b in zip(pts, pts[1:]))
    print(f"  {role:12} lines={len(ts):3}  longest silence={gap:4.0f} min from {at:%H:%M}")
