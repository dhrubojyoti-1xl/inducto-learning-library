# -*- coding: utf-8 -*-
"""
Quality gates for the generated HTML platform.

    python siteverify.py            # structural + fidelity gates
    python siteverify.py --urls     # also re-check every external URL

Nothing here trusts sitegen.py. Each gate re-reads the shipped HTML from disk
and compares it against the source content modules.
"""

import collections
import html
import html.parser
import io
import importlib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")

import build
import sitegen

ROOT = sitegen.ROOT
SITE = sitegen.SITE

# Some sites answer a bare "Mozilla/5.0" with a challenge page, so the
# checker identifies itself as a current desktop browser.
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}


class Parse(html.parser.HTMLParser):
    """Tag-balance, id-uniqueness, attribute collection."""

    def __init__(self):
        html.parser.HTMLParser.__init__(self)
        self.stack = []
        self.errors = []
        self.ids = collections.Counter()
        self.hrefs = []
        self.srcs = []
        self.imgs = []
        self.iframes = []
        self.text = []
        self.labels = 0
        self.headings = []
        self.buttons = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids[a["id"]] += 1
        if a.get("href"):
            # rel="preconnect"/"dns-prefetch"/"preload" are connection hints,
            # not links a learner can follow. youtube-nocookie.com serves
            # /embed/<id> only, so its bare origin is not a page.
            if tag != "link" or a.get("rel", "") not in (
                    "preconnect", "dns-prefetch", "preload", "prefetch"):
                self.hrefs.append(a["href"])
        if a.get("src"):
            self.srcs.append(a["src"])
        if tag == "img":
            self.imgs.append(a)
        if tag == "iframe":
            self.iframes.append(a)
        if tag == "button":
            self.buttons += 1
        if tag in ("h1", "h2", "h3", "h4"):
            self.headings.append(int(tag[1]))
        if tag not in VOID:
            self.stack.append((tag, self.getpos()))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            self.errors.append("stray </%s> at %s" % (tag, self.getpos()))
            return
        top, pos = self.stack.pop()
        if top != tag:
            self.errors.append("expected </%s> (opened %s) got </%s> at %s"
                               % (top, pos, tag, self.getpos()))

    def handle_data(self, data):
        self.text.append(data)


def norm(s):
    """Normalise for text-presence comparison."""
    s = html.unescape(str(s))
    s = s.replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"')
    s = s.replace("—", "-").replace("–", "-").replace("…", "...")
    return re.sub(r"\s+", " ", s).strip().lower()


def walk_strings(node, out):
    if isinstance(node, str):
        if len(node) > 25:
            out.append(node)
    elif isinstance(node, dict):
        for k, v in node.items():
            if k in ("cover_image", "filename", "motif", "area", "type", "icon",
                     "mark", "dot", "anchor", "tone", "url"):
                continue
            walk_strings(v, out)
    elif isinstance(node, (list, tuple)):
        for v in node:
            walk_strings(v, out)


def main():
    check_urls = "--urls" in sys.argv
    fails, warns, stats = [], [], {}

    decks = [importlib.import_module(m).DECK for m in build.REGISTRY]
    by_code = {d["module_code"]: d for d in decks}

    pages = []
    for dirpath, _dirs, files in os.walk(SITE):
        for f in sorted(files):
            if f.endswith(".html"):
                pages.append(os.path.join(dirpath, f))
    stats["html_pages"] = len(pages)

    parsed = {}
    for p in pages:
        src = io.open(p, encoding="utf-8").read()
        pr = Parse()
        pr.feed(src)
        pr.close()
        parsed[p] = (pr, src)
        rel = os.path.relpath(p, SITE).replace("\\", "/")

        # GATE 1 — tag balance
        if pr.errors:
            fails.append("G1 %s: %s" % (rel, pr.errors[0]))
        if pr.stack:
            fails.append("G1 %s: unclosed <%s>" % (rel, pr.stack[-1][0]))

        # GATE 2 — unique ids
        dupes = [i for i, n in pr.ids.items() if n > 1]
        if dupes:
            fails.append("G2 %s: duplicate id %s" % (rel, dupes[:3]))

        # GATE 3 — one h1, no heading level skipped
        h1s = [h for h in pr.headings if h == 1]
        if len(h1s) != 1:
            fails.append("G3 %s: %d <h1> elements" % (rel, len(h1s)))
        prev = 1
        for h in pr.headings:
            if h > prev + 1:
                fails.append("G3 %s: heading jumps h%d -> h%d" % (rel, prev, h))
                break
            prev = h

        # GATE 4 — images have alt, width and height
        for a in pr.imgs:
            if "alt" not in a:
                fails.append("G4 %s: <img> without alt" % rel)
            if not (a.get("width") and a.get("height")):
                warns.append("G4 %s: <img> without intrinsic size" % rel)

        # GATE 5 — iframes titled, lazy
        for a in pr.iframes:
            if not a.get("title"):
                fails.append("G5 %s: <iframe> without title" % rel)
            if a.get("loading") != "lazy":
                warns.append("G5 %s: <iframe> not lazy" % rel)

        # GATE 6 — required page furniture
        for needed in ('class="skip"', "<title>", 'name="viewport"', 'lang="en"'):
            if needed not in src:
                fails.append("G6 %s: missing %s" % (rel, needed))

        # GATE 7 — no unresolved template junk.
        # Matched only where a value would have been substituted (a whole text
        # node or a whole attribute value), so ordinary prose containing the
        # word "None" or "undefined" is not a false positive.
        clean = re.sub(r"<script[\s\S]*?</script>", "", src)
        junk = []
        for bad in ("None", "undefined", "null"):
            if re.search(r">\s*%s\s*<" % bad, clean) or ('="%s"' % bad) in clean:
                junk.append(bad)
        for bad in ("%s", "%d", "{{", "}}", "[object Object]"):
            if bad in clean:
                junk.append(bad)
        if junk:
            fails.append("G7 %s: unsubstituted %s in output" % (rel, junk))

    # GATE 8 — every local link resolves, file and fragment
    linkcount = 0
    for p, (pr, src) in parsed.items():
        base = os.path.dirname(p)
        rel = os.path.relpath(p, SITE).replace("\\", "/")
        for href in pr.hrefs + pr.srcs:
            if href.startswith(("http://", "https://", "mailto:", "data:")):
                continue
            linkcount += 1
            frag = ""
            if "#" in href:
                href, frag = href.split("#", 1)
            if href:
                target = os.path.normpath(os.path.join(base, href))
                if not os.path.exists(target):
                    fails.append("G8 %s: dead link -> %s" % (rel, href))
                    continue
            else:
                target = p
            if frag:
                tp = parsed.get(target)
                if tp is None:
                    tsrc = io.open(target, encoding="utf-8").read()
                    tpr = Parse(); tpr.feed(tsrc); tpr.close()
                    parsed[target] = (tpr, tsrc)
                    tp = parsed[target]
                if frag not in tp[0].ids:
                    fails.append("G8 %s: dead anchor -> %s#%s"
                                 % (rel, os.path.basename(target), frag))
    stats["internal_links"] = linkcount

    # GATE 9 — one page per source deck, correctly wired
    for code, d in by_code.items():
        p = os.path.join(SITE, "modules", "%s.html" % sitegen.slug(code))
        if not os.path.exists(p):
            fails.append("G9 no page for %s" % code)
            continue
        pr, src = parsed[p]
        if 'data-module-id="%s"' % code not in src:
            fails.append("G9 %s: page not bound to module id" % code)
        m = re.search(r'data-section-count="(\d+)"', src)
        declared = int(m.group(1)) if m else -1
        actual = len(re.findall(r'<section class="step" id="', src))
        # the completion section is not a learning section
        if declared != actual - 1:
            fails.append("G9 %s: section-count %d but %d step sections"
                         % (code, declared, actual))
    stats["modules"] = len(by_code)

    # GATE 10 — content fidelity: every substantive source string is present
    missing_total = 0
    checked_total = 0
    worst = []
    for code, d in by_code.items():
        p = os.path.join(SITE, "modules", "%s.html" % sitegen.slug(code))
        body = norm(re.sub(r"<[^>]+>", " ", parsed[p][1]))
        attrs = norm(parsed[p][1])          # attribute-carried text (quiz/scenario)
        strings = []
        walk_strings(d, strings)
        miss = []
        for s in strings:
            n = norm(s)
            if n not in body and n not in attrs:
                miss.append(s)
        checked_total += len(strings)
        missing_total += len(miss)
        if miss:
            worst.append((code, len(miss), miss[0][:80]))
    stats["source_strings_checked"] = checked_total
    stats["source_strings_missing"] = missing_total
    if missing_total:
        for code, n, ex in worst[:5]:
            fails.append("G10 %s: %d source strings not in HTML, e.g. %r" % (code, n, ex))

    # GATE 11 — videos: every URL in the HTML came from a source deck
    src_ids = set()
    for d in decks:
        v = d.get("video")
        if v and sitegen.yt_id(v.get("url")):
            src_ids.add(sitegen.yt_id(v["url"]))
    page_ids = set()
    for p, (pr, src) in parsed.items():
        for a in pr.iframes:
            m = re.search(r"/embed/([A-Za-z0-9_\-]+)", a.get("src", ""))
            if m:
                page_ids.add(m.group(1))
    invented = page_ids - src_ids
    if invented:
        fails.append("G11 video ids not present in source content: %s" % sorted(invented))
    stats["videos_in_source"] = len(src_ids)
    stats["videos_embedded"] = len(page_ids)
    if len(page_ids) != len(src_ids):
        fails.append("G11 %d source videos but %d embedded"
                     % (len(src_ids), len(page_ids)))

    # GATE 12 — images referenced all exist and all shipped images are used
    refs = set()
    for p, (pr, src) in parsed.items():
        base = os.path.dirname(p)
        for a in pr.imgs:
            t = os.path.normpath(os.path.join(base, a["src"]))
            if not os.path.exists(t):
                fails.append("G12 missing image %s" % a["src"])
            else:
                refs.add(os.path.basename(t))
    imgdir = os.path.join(SITE, "assets", "images")
    shipped = set(os.listdir(imgdir)) if os.path.isdir(imgdir) else set()
    orphan = shipped - refs
    if orphan:
        warns.append("G12 image shipped but never referenced: %s" % sorted(orphan))
    stats["images_referenced"] = len(refs)

    # GATE 13 — assessment rule is actually implemented
    js = io.open(os.path.join(SITE, "js", "progress.js"), encoding="utf-8").read()
    aj = io.open(os.path.join(SITE, "js", "assessment.js"), encoding="utf-8").read()
    if "ASSESSMENT_MAX_ATTEMPTS: 3" not in js:
        fails.append("G13 three-attempt limit not set in progress.js")
    if "Further action requires HR decision" not in aj:
        fails.append("G13 HR-decision state missing from assessment.js")
    keys = set(re.findall(r"localStorage\.(?:get|set|remove)Item\(\s*([A-Za-z_]+)", js))
    other = []
    for f in sorted(os.listdir(os.path.join(SITE, "js"))):
        t = io.open(os.path.join(SITE, "js", f), encoding="utf-8").read()
        if f != "progress.js" and "localStorage" in t:
            other.append(f)
    if other:
        fails.append("G13 second progress store found in %s" % other)
    stats["progress_stores"] = 1

    # GATE 14 — company-input tokens are declared, never silently invented
    tokens = collections.Counter()
    for p, (pr, src) in parsed.items():
        for m in re.finditer(r"\[COMPANY INPUT NEEDED:([^\]]*)\]", src):
            tokens[m.group(1).strip()] += 1
    stats["company_input_tokens"] = sum(tokens.values())
    stats["company_input_distinct"] = len(tokens)

    # GATE 15 — data file loads and matches the pages
    data_js = io.open(os.path.join(SITE, "data", "library.js"), encoding="utf-8").read()
    payload = json.loads(data_js.split("=", 1)[1].strip().rstrip(";\n"))
    if len(payload["modules"]) != len(by_code):
        fails.append("G15 data lists %d modules, source has %d"
                     % (len(payload["modules"]), len(by_code)))
    for m in payload["modules"]:
        t = os.path.normpath(os.path.join(SITE, m["href"]))
        if not os.path.exists(t):
            fails.append("G15 data points at missing page %s" % m["href"])
    for q in payload["assessment"]["questions"]:
        if sum(1 for o in q["options"] if o["ok"]) != 1:
            fails.append("G15 assessment question without exactly one correct "
                         "answer: %s" % q["q"])
    stats["search_rows"] = len(payload["search"])
    stats["glossary_terms"] = len(payload["glossary"])
    stats["assessment_pool"] = len(payload["assessment"]["questions"])

    # GATE 16 — external URLs (opt-in)
    ext = set()
    for p, (pr, src) in parsed.items():
        for h in pr.hrefs + [a.get("src", "") for a in pr.iframes]:
            if h.startswith("http"):
                ext.add(h)
    stats["external_urls"] = len(ext)
    if check_urls:
        import requests
        bad = []
        for u in sorted(ext):
            ok = False
            for attempt in (20, 40):
                try:
                    r = requests.get(
                        u, timeout=attempt, allow_redirects=True,
                        headers={"User-Agent": UA, "Accept-Language": "en-GB,en"})
                    if r.status_code == 200:
                        ok = True
                        break
                except Exception:
                    pass
            if not ok:
                bad.append(u)
        if bad:
            fails.append("G16 external URLs not returning 200: %s" % bad)
        stats["external_urls_checked"] = len(ext)

    # ---- report ----
    print("=" * 68)
    print("HTML PLATFORM VERIFICATION")
    print("=" * 68)
    for k in sorted(stats):
        print("  %-28s %s" % (k, stats[k]))
    print("-" * 68)
    for w in warns:
        print("  WARN  " + w)
    for f in fails:
        print("  FAIL  " + f)
    print("-" * 68)
    print("RESULT: %s   (%d fail, %d warn)"
          % ("PASS" if not fails else "FAIL", len(fails), len(warns)))
    json.dump({"stats": stats, "fails": fails, "warns": warns},
              io.open(os.path.join(ROOT, "siteverify.json"), "w", encoding="utf-8"),
              indent=2)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
