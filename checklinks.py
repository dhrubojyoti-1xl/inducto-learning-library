"""
Validate proposed YouTube links.

A watch URL returns HTTP 200 even for a dead or non-existent video id, so
HTTP status alone proves nothing. This uses YouTube's oEmbed endpoint, which
404s for ids that do not exist, are private, or are not embeddable, and
returns the REAL title and channel for ones that do.

We can prove a video exists and report what it actually is. We cannot prove
its content matches a curriculum topic — that stays a human check.
"""

import json
import sys

import requests

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
OEMBED = "https://www.youtube.com/oembed?url=%s&format=json"


def check(url):
    try:
        r = requests.get(OEMBED % url, headers=UA, timeout=25)
    except Exception as exc:
        return {"status": "NETWORK-ERROR", "detail": str(exc)}
    if r.status_code == 200:
        try:
            d = r.json()
        except Exception:
            return {"status": "BAD-JSON", "detail": r.text[:120]}
        return {"status": "LIVE", "title": d.get("title"),
                "channel": d.get("author_name")}
    if r.status_code in (401, 403):
        return {"status": "NOT-EMBEDDABLE",
                "detail": "exists but blocks embedding (HTTP %d)" % r.status_code}
    if r.status_code == 404:
        return {"status": "DEAD", "detail": "no such video (HTTP 404)"}
    return {"status": "HTTP-%d" % r.status_code, "detail": r.reason}


def main(path):
    with open(path, encoding="utf-8") as fh:
        items = json.load(fh)
    out = []
    for it in items:
        res = check(it["url"])
        res.update({"claimed": it["claimed"], "url": it["url"],
                    "topic": it.get("topic", "")})
        out.append(res)
        print("%-16s %-34s %s" % (res["status"], it["topic"][:34],
                                  res.get("title") or res.get("detail", "")))
    with open("linkcheck.json", "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2, ensure_ascii=False)
    live = sum(1 for o in out if o["status"] == "LIVE")
    print("\n%d/%d resolve to a real, public, embeddable video" % (live, len(out)))


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    main(sys.argv[1])
