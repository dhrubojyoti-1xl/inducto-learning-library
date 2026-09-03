# Content coverage report

## Method

`siteverify.py` gate 10 walks every string of more than 25 characters in every source `DECK` dictionary — the same dictionaries that build the PowerPoint files — and looks for each one in the generated HTML, after unescaping entities and normalising whitespace and curly punctuation. A string counts as covered only if it is present in the page's text or in an attribute the page reads back (quiz and scenario feedback lives in `data-` attributes).

## Result

| Measure | Value |
| --- | ---: |
| Source strings checked | 7127 |
| Source strings not found in the HTML | 0 |
| Coverage | 100.0% |
| Module pages | 39 |
| Lesson blocks | 538 |
| Glossary terms | 148 |
| Search index rows | 1162 |

## What was deliberately not carried across

- **Slide furniture.** Slide numbers, footers, the persistent Menu button and the deck's own navigation hints. The web page has a section rail and a browser, so these have no job to do.
- **Layout-only text.** Nothing. Every caption, note and label in the source is on the page.

## What was added, and why

- Progress tracking, the resume card and the completion state — a deck cannot remember where you were.
- A cross-library search over modules, lessons, glossary terms, recap rules and toolkit items (1162 rows).
- The formal assessment. It draws one question per module from the existing module quizzes, so nothing on the test is untaught.

No training content was written for the HTML build. Every sentence a learner reads comes from `content/areaNN/*.py`.
