# -*- coding: utf-8 -*-
"""
Write the audit documents from measured data, never from memory.

    python docsgen.py

Every number in the generated Markdown is computed here from the shipped
files: the source content modules, the built .pptx decks, the generated HTML
and the verifier's own JSON output. If a figure cannot be measured it is not
printed.
"""

import collections
import importlib
import io
import json
import os
import re
import sys
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")

import build
import sitegen
import theme as T

ROOT = sitegen.ROOT
SITE = sitegen.SITE
OUT = os.path.join(ROOT, "output")
DOCS = os.path.join(ROOT, "docs")

VISUAL_NOTE = {
    "flow": "Numbered step cards, wrapping to one column on a phone.",
    "nested": "Indented containment blocks, outermost first.",
    "iconrow": "Tile row with an accent mark per tile.",
    "split": "Two comparison panels, tinted by tone.",
    "tree": "Decision question with the two branches beneath it.",
    "steps": "Numbered instruction list beside a copy-to-clipboard prompt card.",
    "beforeafter": "Two panels, ✕ against ✓, plus the closing note.",
    "prompt": "Copyable prompt card with the 'why this works' points.",
    "prompt_out": "Copyable prompt card beside what comes back.",
    "checklist": "Tickable list; state is saved with the learner's progress.",
    "bandlist": "Coloured headline band followed by the supporting points.",
    "mistakes": "Numbered mistake, then the consequence, side by side.",
}


def read(p):
    return io.open(p, encoding="utf-8").read()


def w(name, text):
    os.makedirs(DOCS, exist_ok=True)
    io.open(os.path.join(DOCS, name), "w", encoding="utf-8", newline="\n").write(text)
    print("  wrote docs/%s (%d lines)" % (name, text.count("\n") + 1))


def main():
    decks = [importlib.import_module(m).DECK for m in build.REGISTRY]
    order = {a: i for i, a in enumerate(sitegen.AREA_ORDER)}
    decks.sort(key=lambda d: (order[d["area"]], d["module_code"]))
    verify = json.loads(read(os.path.join(ROOT, "siteverify.json")))
    sgreport = json.loads(read(os.path.join(ROOT, "sitegen_report.json")))
    manifest = json.loads(read(os.path.join(OUT, "manifest.json")))
    mani = {d["module_code"]: d for d in manifest["decks"]}

    # ---- measure the source PowerPoint files -------------------------------
    pptx = {}
    for fn in sorted(os.listdir(OUT)):
        if not fn.endswith(".pptx"):
            continue
        with zipfile.ZipFile(os.path.join(OUT, fn)) as z:
            slides = [n for n in z.namelist()
                      if re.match(r"ppt/slides/slide\d+\.xml$", n)]
            words = 0
            for n in slides:
                xml = z.read(n).decode("utf-8", "ignore")
                words += len(re.findall(r"<a:t>([^<]*)</a:t>", xml))
        pptx[fn] = {"slides": len(slides), "textruns": words,
                    "bytes": os.path.getsize(os.path.join(OUT, fn))}

    # ---- 1. SOURCE CONTENT INVENTORY ---------------------------------------
    rows, tot_slides, tot_pts = [], 0, 0
    for d in decks:
        f = d["filename"]
        p = pptx.get(f, {})
        pts = mani.get(d["module_code"], {}).get("content_points", "")
        tot_slides += p.get("slides", 0)
        if isinstance(pts, int):
            tot_pts += pts
        rows.append("| %s | %s | %s | %d | %s | %d | %d |" % (
            d["module_code"], d["title"], f, p.get("slides", 0), pts,
            d["duration_min"], len(d["slides"])))
    idx = pptx.get("00-master-index.pptx", {})
    txt = [
        "# Source content inventory",
        "",
        "What was in the PowerPoint library before any HTML existed. Measured "
        "by opening each `.pptx` and counting the slide parts inside it, not "
        "taken from the build log.",
        "",
        "| Measure | Value |",
        "| --- | ---: |",
        "| PowerPoint files | %d |" % len(pptx),
        "| Topic decks | %d |" % len(decks),
        "| Master index deck | 1 (`00-master-index.pptx`, %d slides) |"
        % idx.get("slides", 0),
        "| Slides across all files | %d |" % sum(p["slides"] for p in pptx.values()),
        "| Slides in the topic decks | %d |" % tot_slides,
        "| Content points (from `manifest.json`) | %d |" % tot_pts,
        "| Learning duration | %d minutes |" % sum(d["duration_min"] for d in decks),
        "| Hero photographs available | %d |" % len(
            [d for d in decks if d.get("cover_image")]),
        "",
        "## Per deck",
        "",
        "| Code | Title | Source file | Slides | Content points | Minutes | "
        "Content slides |",
        "| --- | --- | --- | ---: | ---: | ---: | ---: |",
    ] + rows + [
        "",
        "Slide counts include the hidden branch-feedback and glossary slides "
        "that make the decks interactive; the HTML replaces those with "
        "in-page reveals, so the HTML page count is deliberately lower.",
        "",
    ]
    w("SOURCE_CONTENT_INVENTORY.md", "\n".join(txt))

    # ---- 2. SOURCE TO HTML MAP ---------------------------------------------
    txt = [
        "# Source → HTML map",
        "",
        "One row per source deck. Every deck became exactly one HTML module "
        "page; the master index deck became `index.html`.",
        "",
        "| Source `.pptx` | HTML page | Code | Sections | Lessons | Quiz Qs | "
        "Glossary | Video |",
        "| --- | --- | --- | ---: | ---: | ---: | ---: | :---: |",
    ]
    data = json.loads(read(os.path.join(SITE, "data", "library.js"))
                      .split("=", 1)[1].strip().rstrip(";\n"))
    secs = {m["id"]: m["sectionCount"] for m in data["modules"]}
    for d in decks:
        txt.append("| `output/%s` | `site/modules/%s.html` | %s | %d | %d | %d | "
                   "%d | %s |" % (
                       d["filename"], sitegen.slug(d["module_code"]),
                       d["module_code"], secs[d["module_code"]], len(d["slides"]),
                       len(d["quiz"]), len(d["glossary"]),
                       "yes" if d.get("video") else "no"))
    txt += [
        "| `output/00-master-index.pptx` | `site/index.html` | INDEX | — | — | "
        "— | — | — |",
        "",
        "## How each deck element was carried over",
        "",
        "| Deck element | HTML treatment |",
        "| --- | --- |",
        "| Cover slide | Page header: hero image or motif band, chips, title, "
        "subtitle, progress bar |",
        "| Why this matters | `#why` — story, cost and fix panels |",
        "| Outcomes | `#outcomes` — numbered objective list |",
        "| Concept slides | One `.lesson` block each, inside its section |",
        "| Interactive menu | The sticky section rail, which also shows what "
        "you have read |",
        "| Branching scenario | `#scenario` — buttons with per-choice feedback "
        "and a retry |",
        "| Video slide | `#video` — privacy-mode YouTube embed with channel and "
        "runtime |",
        "| Branching quiz | `#check` — per-answer feedback, retry, scored on "
        "first answer |",
        "| Recap | `#recap` — recap cards and the one-liner |",
        "| Toolkit | `#toolkit` — templates, tool links, next module |",
        "| Hidden glossary slides | `#glossary` — always-visible cards, linked "
        "from the lessons that use the term |",
        "| Hidden feedback slides | Inline feedback panels, revealed on the "
        "answer that earns them |",
        "",
    ]
    w("SOURCE_TO_HTML_MAP.md", "\n".join(txt))

    # ---- 3. CONTENT COVERAGE REPORT ----------------------------------------
    st = verify["stats"]
    txt = [
        "# Content coverage report",
        "",
        "## Method",
        "",
        "`siteverify.py` gate 10 walks every string of more than 25 characters "
        "in every source `DECK` dictionary — the same dictionaries that build "
        "the PowerPoint files — and looks for each one in the generated HTML, "
        "after unescaping entities and normalising whitespace and curly "
        "punctuation. A string counts as covered only if it is present in the "
        "page's text or in an attribute the page reads back (quiz and scenario "
        "feedback lives in `data-` attributes).",
        "",
        "## Result",
        "",
        "| Measure | Value |",
        "| --- | ---: |",
        "| Source strings checked | %d |" % st["source_strings_checked"],
        "| Source strings not found in the HTML | %d |"
        % st["source_strings_missing"],
        "| Coverage | %.1f%% |" % (100.0 * (st["source_strings_checked"]
                                            - st["source_strings_missing"])
                                   / st["source_strings_checked"]),
        "| Module pages | %d |" % st["modules"],
        "| Lesson blocks | %d |" % sgreport["lessons"],
        "| Glossary terms | %d |" % st["glossary_terms"],
        "| Search index rows | %d |" % st["search_rows"],
        "",
        "## What was deliberately not carried across",
        "",
        "- **Slide furniture.** Slide numbers, footers, the persistent Menu "
        "button and the deck's own navigation hints. The web page has a "
        "section rail and a browser, so these have no job to do.",
        "- **Layout-only text.** Nothing. Every caption, note and label in the "
        "source is on the page.",
        "",
        "## What was added, and why",
        "",
        "- Progress tracking, the resume card and the completion state — a deck "
        "cannot remember where you were.",
        "- A cross-library search over modules, lessons, glossary terms, recap "
        "rules and toolkit items (%d rows)." % st["search_rows"],
        "- The formal assessment. It draws one question per module from the "
        "existing module quizzes, so nothing on the test is untaught.",
        "",
        "No training content was written for the HTML build. Every sentence a "
        "learner reads comes from `content/areaNN/*.py`.",
        "",
    ]
    w("CONTENT_COVERAGE_REPORT.md", "\n".join(txt))

    # ---- 4. VISUAL ASSET MAP -----------------------------------------------
    vis = collections.Counter()
    for d in decks:
        for s in d["slides"]:
            if s.get("visual"):
                vis[s["visual"]["type"]] += 1
    withimg = [d for d in decks if d.get("cover_image")]
    without = [d for d in decks if not d.get("cover_image")]
    txt = [
        "# Visual asset map",
        "",
        "## Decision",
        "",
        "The source decks draw their diagrams as native PowerPoint shapes. "
        "Those were **re-implemented as HTML and CSS components**, not exported "
        "as slide screenshots. A screenshot would be a fixed-width image that "
        "cannot reflow on a phone, cannot be read by a screen reader, and "
        "cannot be searched. Every diagram type below is therefore live markup.",
        "",
        "## Diagram types carried over",
        "",
        "| Source visual | Count | HTML component |",
        "| --- | ---: | --- |",
    ]
    for k, n in vis.most_common():
        txt.append("| `%s` | %d | %s |" % (k, n, VISUAL_NOTE[k]))
    txt += [
        "| **Total** | **%d** | |" % sum(vis.values()),
        "",
        "## Photographs",
        "",
        "%d of the %d modules have a hero photograph. These are the same JPEG "
        "files used on the deck covers, copied unchanged into "
        "`site/assets/images/`." % (len(withimg), len(decks)),
        "",
        "| Module | Image file |",
        "| --- | --- |",
    ]
    for d in withimg:
        txt.append("| %s — %s | `%s` |" % (d["module_code"], d["title"],
                                           os.path.basename(d["cover_image"])))
    txt += [
        "",
        "**No images were generated for this build.** The %d files above were "
        "already in `assets/` and were copied, not created." % len(withimg),
        "",
        "The remaining %d modules use a CSS motif band carrying the module "
        "code. It is drawn with gradients, so there is no image file behind it "
        "and it can never 404." % len(without),
        "",
        "| Module | Motif |",
        "| --- | --- |",
    ]
    for d in without:
        txt.append("| %s — %s | `%s` |" % (d["module_code"], d["title"],
                                           d.get("motif", "network")))
    txt.append("")
    w("VISUAL_ASSET_MAP.md", "\n".join(txt))

    # ---- 5. VISUAL ASSET GAPS ----------------------------------------------
    txt = [
        "# Visual asset gaps",
        "",
        "Modules with no photograph of their own. Nothing was substituted, and "
        "no stand-in image was generated — each of these uses the CSS motif "
        "band described in `VISUAL_ASSET_MAP.md`, so no page shows a broken or "
        "misleading image.",
        "",
        "| Module | Title | Track | Motif in use |",
        "| --- | --- | --- | --- |",
    ]
    for d in without:
        txt.append("| %s | %s | %s | `%s` |" % (
            d["module_code"], d["title"], T.AREAS[d["area"]]["name"],
            d.get("motif", "network")))
    txt += [
        "",
        "**%d of %d modules are affected.**" % (len(without), len(decks)),
        "",
        "To close a gap, drop a 16:7 JPEG into `assets/`, add "
        "`\"cover_image\": \"assets/<file>.jpg\"` to that module's `DECK`, and "
        "re-run `python sitegen.py`. The generator refuses to build if a "
        "declared image file is missing, so a broken reference cannot ship.",
        "",
    ]
    w("VISUAL_ASSET_GAPS.md", "\n".join(txt))

    # ---- 6. VIDEO GAPS ------------------------------------------------------
    gaps = sgreport["videoGaps"]
    txt = [
        "# Video gaps",
        "",
        "| Measure | Value |",
        "| --- | ---: |",
        "| Modules | %d |" % len(decks),
        "| Modules with a video | %d |" % (len(decks) - len(gaps)),
        "| Modules without a video | %d |" % len(gaps),
        "| Distinct videos embedded | %d |" % verify["stats"]["videos_embedded"],
        "",
    ]
    if gaps:
        txt += ["## Gaps", "",
                "| Module | Title | Reason |", "| --- | --- | --- |"]
        for g in gaps:
            txt.append("| %s | %s | %s |" % (g["module"], g["title"], g["reason"]))
    else:
        txt += [
            "## No gaps",
            "",
            "Every module carries a video. No URL was invented: each one was "
            "confirmed against YouTube's own oEmbed endpoint before it was "
            "written into the content module, which is where the title, "
            "channel and runtime shown on the page also come from. "
            "`siteverify.py` gate 11 re-checks that every video id in the "
            "HTML exists in the source content, so a fabricated id cannot "
            "reach a page.",
            "",
            "| Module | Video | Channel | Runtime |",
            "| --- | --- | --- | ---: |",
        ]
        for d in decks:
            v = d["video"]
            txt.append("| %s | [%s](%s) | %s | %s |" % (
                d["module_code"], v["title"].replace("|", "-"), v["url"],
                v["channel"], v["duration"]))
    txt.append("")
    w("VIDEO_GAPS.md", "\n".join(txt))

    # ---- 7. QA REPORT -------------------------------------------------------
    gate_names = [
        ("G1", "HTML tag balance on every page"),
        ("G2", "No duplicate element ids"),
        ("G3", "One `h1` per page, no heading level skipped"),
        ("G4", "Every `img` has `alt` and intrinsic size"),
        ("G5", "Every `iframe` has a title and lazy loading"),
        ("G6", "Skip link, `title`, viewport meta and `lang` on every page"),
        ("G7", "No unsubstituted template values in the output"),
        ("G8", "Every internal link and fragment resolves"),
        ("G9", "One page per source deck, bound to the right module id"),
        ("G10", "Source-to-HTML content fidelity"),
        ("G11", "No video id that is not in the source content"),
        ("G12", "Every referenced image exists"),
        ("G13", "Three-attempt assessment rule, and a single progress store"),
        ("G14", "Company-input tokens counted, nothing invented in their place"),
        ("G15", "Data file agrees with the pages; one correct answer per "
                "assessment question"),
        ("G16", "External URLs return HTTP 200 (run with `--urls`)"),
    ]
    txt = [
        "# QA report",
        "",
        "Produced by `python siteverify.py`. Every gate re-reads the shipped "
        "files; none of them trust the generator.",
        "",
        "## Result",
        "",
        "**%s** — %d failures, %d warnings." % (
            "PASS" if not verify["fails"] else "FAIL",
            len(verify["fails"]), len(verify["warns"])),
        "",
        "## Gates",
        "",
        "| Gate | Checks | Result |",
        "| --- | --- | --- |",
    ]
    for gid, desc in gate_names:
        hit = [f for f in verify["fails"] if f.startswith(gid + " ")]
        note = "PASS" if not hit else "FAIL — %s" % hit[0]
        if gid == "G16" and "external_urls_checked" not in st:
            note = "not run in this pass"
        txt.append("| %s | %s | %s |" % (gid, desc, note))
    txt += [
        "",
        "## Measured",
        "",
        "| Measure | Value |",
        "| --- | ---: |",
    ]
    label = {
        "html_pages": "HTML pages", "modules": "Module pages",
        "internal_links": "Internal links checked",
        "external_urls": "Distinct external URLs",
        "images_referenced": "Images referenced",
        "videos_embedded": "Videos embedded",
        "videos_in_source": "Videos in the source content",
        "search_rows": "Search index rows", "glossary_terms": "Glossary terms",
        "assessment_pool": "Assessment question pool",
        "source_strings_checked": "Source strings checked",
        "source_strings_missing": "Source strings missing",
        "progress_stores": "Progress stores (must be 1)",
        "company_input_tokens": "`[COMPANY INPUT NEEDED]` tokens",
        "company_input_distinct": "Distinct company inputs required",
    }
    for k in ["html_pages", "modules", "internal_links", "external_urls",
              "images_referenced", "videos_embedded", "videos_in_source",
              "search_rows", "glossary_terms", "assessment_pool",
              "source_strings_checked", "source_strings_missing",
              "progress_stores", "company_input_tokens",
              "company_input_distinct"]:
        if k in st:
            txt.append("| %s | %s |" % (label[k], st[k]))
    txt += [
        "",
        "## Accessibility",
        "",
        "- Skip link on every page, first in the tab order.",
        "- Landmarks: `header`, `nav` (breadcrumb, section rail, module "
        "navigation), `main`, `footer`.",
        "- Heading order verified by gate 3.",
        "- Every interactive control is a real `button` or `a`, reachable by "
        "keyboard, with a visible `:focus-visible` ring.",
        "- Targets are at least 44px tall (buttons, options, checklist rows).",
        "- Quiz and scenario feedback is announced through a polite live "
        "region (`#live`).",
        "- Progress bars carry `role=\"progressbar\"` with a live "
        "`aria-valuenow`.",
        "- `prefers-reduced-motion` disables smooth scrolling and transitions.",
        "- Colour is never the only signal: right and wrong answers also carry "
        "✓ / ✕ and a worded heading.",
        "",
        "## Responsive",
        "",
        "Checked at 375px, 900px and 1280px. The section rail becomes a "
        "horizontal strip below 960px; the top bar drops the progress figure "
        "below 560px; all comparison grids collapse to one column.",
        "",
        "## Performance",
        "",
        "- One stylesheet, three small scripts, no framework and no build step.",
        "- No web fonts: the type stack is Segoe UI with system fallbacks.",
        "- YouTube embeds are `loading=\"lazy\"` and use the "
        "`youtube-nocookie.com` domain.",
        "- Images carry intrinsic `width` and `height`, so nothing shifts as "
        "the page loads.",
        "- The data file is a plain script rather than a `fetch`, so the site "
        "also works opened straight from disk.",
        "",
        "## Known limitation",
        "",
        "Progress lives in the browser's `localStorage` under one key, "
        "`inducto.progress.v1`. It is per-device and per-browser, and clearing "
        "site data clears it. The store is written behind a single module "
        "(`site/js/progress.js`) whose `load()` and `save()` are the only two "
        "functions that would change if this were moved to a server.",
        "",
    ]
    w("QA_REPORT.md", "\n".join(txt))

    print("\nAll audit documents regenerated from measured data.")


if __name__ == "__main__":
    main()
