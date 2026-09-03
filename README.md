# Inducto Learning & Knowledge Library

Thirty-nine self-guided learning modules on AI, prompting, professional
skills and data security, shipped two ways from **one** source of content:

* an **interactive web platform** in `site/`, deployed to GitHub Pages
* a **PowerPoint library** in `output/` — 39 topic decks plus a master index

Both are generated from the same Python dictionaries in `content/`, so the
two cannot drift apart. No training content is written anywhere else.

---

## Quick start

```bash
python build.py        # rebuild all 40 .pptx files into output/
python verify.py       # 14 quality gates over the decks
python sitegen.py      # rebuild the HTML platform into site/
python siteverify.py   # 16 quality gates over the HTML
python docsgen.py      # regenerate docs/ from measured data
```

Add `--urls` to either verifier to re-check every external link, and `--pp`
to `verify.py` to open each deck in PowerPoint and confirm it needs no repair.

To read the site locally:

```bash
python -m http.server 8765 --directory site
```

---

## What the learner gets

| | |
| --- | --- |
| Modules | 39, across 5 tracks |
| Learning time | about 11 hours |
| Lesson blocks | 538 |
| Glossary terms | 148 |
| Videos | 39, one per module, each verified against YouTube |
| Assessment | one formal test, **three attempts**, then an HR decision |

Every module runs the same spine: why it matters → what you will be able to
do → the lessons → a branching scenario → a video → a knowledge check →
recap → toolkit → glossary. Wrong answers get their own explanation rather
than a generic "incorrect".

## Progress

There is exactly one progress model, in `site/js/progress.js`, stored under
the single key `inducto.progress.v1`. The library page, every module page
and the assessment all read and write that one record. Nothing else in the
codebase touches `localStorage`; `siteverify.py` gate 13 fails the build if
anything starts to.

Moving to a server-backed, multi-tenant deployment means replacing `load()`
and `save()` in that one file. The stored shape already carries the fields a
tenant would need, and `window.INDUCTO_DATA.org` holds the per-company
metadata slots.

## Assessment rule

Three attempts. On the third unsuccessful attempt the learner is told that
**further action requires an HR decision**, and the attempt history is kept.
The knowledge check inside each module is practice: unlimited retries, and
it never counts towards the three.

No HR workflow is connected in this build. The site records the outcome; the
follow-up happens outside it.

## Company inputs still needed

The content deliberately never invents company policy, tool names, people or
figures. Where a real detail is required it carries a
`[COMPANY INPUT NEEDED: …]` token. There are 14 distinct inputs outstanding —
`output/manifest.json` lists every one with the deck it appears in.

## Layout

```
content/            the single source of truth, one file per module
theme.py            design tokens shared by both outputs
components.py       PowerPoint slide builders
visuals.py          PowerPoint diagram builders
build.py            deck build
verify.py           deck quality gates
sitegen.py          HTML platform build
siteverify.py       HTML quality gates
docsgen.py          audit documents, from measured data
site/               the deployed platform
output/             the built PowerPoint library
docs/               audit and QA documents
assets/             hero photographs
```

## Documents

| File | What it answers |
| --- | --- |
| [docs/SOURCE_CONTENT_INVENTORY.md](docs/SOURCE_CONTENT_INVENTORY.md) | What was in the PowerPoint library first |
| [docs/SOURCE_TO_HTML_MAP.md](docs/SOURCE_TO_HTML_MAP.md) | Where each deck and each deck element went |
| [docs/CONTENT_COVERAGE_REPORT.md](docs/CONTENT_COVERAGE_REPORT.md) | How much of the source text reached the HTML, and how that was measured |
| [docs/VISUAL_ASSET_MAP.md](docs/VISUAL_ASSET_MAP.md) | Every diagram and photograph, and how it was handled |
| [docs/VISUAL_ASSET_GAPS.md](docs/VISUAL_ASSET_GAPS.md) | Modules with no photograph of their own |
| [docs/VIDEO_GAPS.md](docs/VIDEO_GAPS.md) | Video coverage, and how the URLs were verified |
| [docs/QA_REPORT.md](docs/QA_REPORT.md) | The 16 HTML gates, accessibility, responsive and performance |
| [docs/DEPLOYMENT_REPORT.md](docs/DEPLOYMENT_REPORT.md) | What was deployed, where, and what was checked live |
