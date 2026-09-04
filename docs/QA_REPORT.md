# QA report

Produced by `python siteverify.py`. Every gate re-reads the shipped files; none of them trust the generator.

## Result

**PASS** — 0 failures, 0 warnings.

## Gates

| Gate | Checks | Result |
| --- | --- | --- |
| G1 | HTML tag balance on every page | PASS |
| G2 | No duplicate element ids | PASS |
| G3 | One `h1` per page, no heading level skipped | PASS |
| G4 | Every `img` has `alt` and intrinsic size | PASS |
| G5 | Every `iframe` has a title and lazy loading | PASS |
| G6 | Skip link, `title`, viewport meta and `lang` on every page | PASS |
| G7 | No unsubstituted template values in the output | PASS |
| G8 | Every internal link and fragment resolves | PASS |
| G9 | One page per source deck, bound to the right module id | PASS |
| G10 | Source-to-HTML content fidelity | PASS |
| G11 | No video id that is not in the source content | PASS |
| G12 | Every referenced image exists | PASS |
| G13 | Three-attempt assessment rule, and a single progress store | PASS |
| G14 | Company-input tokens counted, nothing invented in their place | PASS |
| G15 | Data file agrees with the pages; one correct answer per assessment question | PASS |
| G16 | External URLs return HTTP 200 (run with `--urls`) | not run in this pass |

## Measured

| Measure | Value |
| --- | ---: |
| HTML pages | 59 |
| Module pages | 39 |
| Internal links checked | 1363 |
| Distinct external URLs | 84 |
| Images referenced | 18 |
| Videos embedded | 39 |
| Videos in the source content | 39 |
| Search index rows | 1162 |
| Glossary terms | 148 |
| Assessment question pool | 15 |
| Source strings checked | 7125 |
| Source strings missing | 0 |
| Progress stores (must be 1) | 1 |
| `[COMPANY INPUT NEEDED]` tokens | 56 |
| Distinct company inputs required | 14 |

## Accessibility

- Skip link on every page, first in the tab order.
- Landmarks: `header`, `nav` (breadcrumb, section rail, module navigation), `main`, `footer`.
- Heading order verified by gate 3.
- Every interactive control is a real `button` or `a`, reachable by keyboard, with a visible `:focus-visible` ring.
- Target sizes measured in the browser on the deployed page: primary buttons, quiz options and checklist rows are 44px or taller; the small secondary buttons are 36px and the section-rail links 41px. Every non-inline target clears the 24px WCAG 2.2 minimum. Inline links inside a line of text (the breadcrumb) are exempt under that rule.
- Quiz and scenario feedback is announced through a polite live region (`#live`).
- Progress bars carry `role="progressbar"` with a live `aria-valuenow`.
- `prefers-reduced-motion` disables smooth scrolling and transitions.
- Colour is never the only signal: right and wrong answers also carry ✓ / ✕ and a worded heading.

## Responsive

Checked at 375px, 900px and 1280px. The section rail becomes a horizontal strip below 960px; the top bar drops the progress figure below 560px; all comparison grids collapse to one column.

## Performance

- One stylesheet, three small scripts, no framework and no build step.
- No web fonts: the type stack is Segoe UI with system fallbacks.
- YouTube embeds are `loading="lazy"` and use the `youtube-nocookie.com` domain.
- Images carry intrinsic `width` and `height`, so nothing shifts as the page loads.
- The data file is a plain script rather than a `fetch`, so the site also works opened straight from disk.

## Known limitation

Progress lives in the browser's `localStorage` under one key, `inducto.progress.v1`. It is per-device and per-browser, and clearing site data clears it. The store is written behind a single module (`site/js/progress.js`) whose `load()` and `save()` are the only two functions that would change if this were moved to a server.
