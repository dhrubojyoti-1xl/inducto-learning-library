"""
Find candidate videos by scraping YouTube's own search results.

Every video id returned here came out of a real search response, so nothing
can be invented. Each candidate is then confirmed against the oEmbed endpoint
before it is allowed near a deck.

    python ytsearch.py "how to write meeting minutes"
"""

import json
import re
import sys

import requests

UA = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 "
                  "Safari/537.36",
    "Accept-Language": "en-GB,en;q=0.9",
}
SEARCH = "https://www.youtube.com/results?search_query=%s&sp=EgIYAw%%253D%%253D"
# sp=EgIYAw== filters to videos under 4 minutes; we use the plain search and
# filter by duration ourselves instead, so keep the simple URL:
SEARCH = "https://www.youtube.com/results?search_query=%s"


def _walk(node, out):
    """Pull every videoRenderer out of YouTube's response blob."""
    if isinstance(node, dict):
        if "videoRenderer" in node:
            v = node["videoRenderer"]
            try:
                title = "".join(r["text"] for r in v["title"]["runs"])
            except Exception:
                title = v.get("title", {}).get("simpleText", "")
            length = (v.get("lengthText") or {}).get("simpleText")
            owner = ""
            try:
                owner = v["ownerText"]["runs"][0]["text"]
            except Exception:
                pass
            views = (v.get("viewCountText") or {}).get("simpleText", "")
            out.append({"id": v.get("videoId"), "title": title,
                        "channel": owner, "length": length, "views": views})
        for val in node.values():
            _walk(val, out)
    elif isinstance(node, list):
        for val in node:
            _walk(val, out)
    return out


def search(query, limit=14):
    r = requests.get(SEARCH % requests.utils.quote(query), headers=UA,
                     timeout=30)
    m = re.search(r"var ytInitialData = (\{.*?\});</script>", r.text)
    if not m:
        m = re.search(r'ytInitialData"\]\s*=\s*(\{.*?\});', r.text)
    if not m:
        return []
    data = json.loads(m.group(1))
    seen, out = set(), []
    for c in _walk(data, []):
        if not c["id"] or c["id"] in seen or not c["length"]:
            continue
        seen.add(c["id"])
        out.append(c)
        if len(out) >= limit:
            break
    return out


def secs(length):
    if not length:
        return None
    parts = [int(p) for p in length.split(":")]
    while len(parts) < 3:
        parts.insert(0, 0)
    return parts[0] * 3600 + parts[1] * 60 + parts[2]


def confirm(vid):
    """oEmbed check: proves the video is real, public and embeddable."""
    url = "https://www.youtube.com/watch?v=%s" % vid
    try:
        r = requests.get(
            "https://www.youtube.com/oembed?url=%s&format=json" % url,
            headers=UA, timeout=25)
    except Exception as exc:
        return None, str(exc)
    if r.status_code != 200:
        return None, "oembed HTTP %d" % r.status_code
    d = r.json()
    return {"title": d.get("title"), "channel": d.get("author_name"),
            "url": url}, None


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    q = sys.argv[1]
    maxs = int(sys.argv[2]) if len(sys.argv) > 2 else 900
    for c in search(q):
        s = secs(c["length"])
        if s is None or s > maxs or s < 120:
            continue
        print("%-13s %-7s %-30s %s" % (c["id"], c["length"],
                                       c["channel"][:30], c["title"][:74]))
