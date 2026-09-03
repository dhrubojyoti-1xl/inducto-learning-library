# Deployment report

## Where it is

| | |
| --- | --- |
| Live URL | <https://dhrubojyoti-1xl.github.io/inducto-learning-library/> |
| Repository | <https://github.com/dhrubojyoti-1xl/inducto-learning-library> |
| Visibility | public — GitHub Pages is free only on public repositories, and the user chose this over a private repository on 3 September 2026 |
| Hosting | GitHub Pages, `build_type: workflow` |
| Workflow | `.github/workflows/deploy.yml` — checkout, upload `site/`, deploy. No build step |
| Published directory | `site/` |

## How it was authenticated

Through the GitHub CLI, which the repository owner authenticated themselves
(`gh auth login --with-token`, token held in the OS keyring). No token, key or
credential appears anywhere in this repository, and none was passed on a
command line by the build. Before the first commit the working tree was scanned
for token-shaped strings, credential assignments and `.env` files; none were
found. Build intermediates and the 11 MB duplicate archive are excluded by
`.gitignore`.

## What was checked on the live site

Every URL below was requested from the deployed origin, not from disk.

| Check | Result |
| --- | --- |
| Pages deployment run | success |
| Live URLs requested | 48 |
| Non-200 responses | 0 |
| Pages covered | index, assessment, all 39 module pages |
| Assets covered | stylesheet, all four scripts, the data file, a hero image |
| Total transferred for those 48 requests | 1.8 MB |
| Index page weight | 6.1 KB of HTML |
| Browser console errors on load | none |
| Search tested live | "phishing" returns the SEC-02 module, its glossary term and its lessons, each deep-linked to the right section |

## What was verified before deploying

`python siteverify.py --urls` — 16 gates, **0 failures, 0 warnings**.

| | |
| --- | --- |
| HTML pages | 41 |
| Internal links and fragments resolved | 1133 |
| External URLs returning 200 | 84 of 84 |
| Source strings checked for fidelity | 7127 |
| Source strings missing from the HTML | 0 |
| Videos embedded / in source | 39 / 39 |
| Progress stores (must be exactly 1) | 1 |

Full detail in [QA_REPORT.md](QA_REPORT.md).

## Paths

The site is a GitHub Pages *project* site, so it is served from a
subdirectory. Every link, stylesheet, script and image reference in the build
is relative, so the same files work at the project URL, at a custom domain, on
a plain web server, and opened straight from disk.

## What is not deployed

- **No backend.** Progress lives in the learner's own browser. Nothing is sent
  anywhere, and the site sets no cookies.
- **No HR workflow.** The assessment records the three-attempt outcome and
  says that further action requires an HR decision. Connecting that to a real
  HR process is outside this build.
- **No tenant separation.** `window.INDUCTO_DATA.org` carries empty slots for
  organisation name, owner and tenant id, ready for a SaaS deployment; they are
  `null` today rather than filled with a guess.

## To redeploy

Push to `main`. The workflow runs on every push and can also be started by
hand from the Actions tab.

```bash
python sitegen.py && python siteverify.py && python docsgen.py
git add -A && git commit -m "..." && git push
```
