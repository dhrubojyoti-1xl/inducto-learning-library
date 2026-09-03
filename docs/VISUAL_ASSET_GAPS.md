# Visual asset gaps

Modules with no photograph of their own. Nothing was substituted, and no stand-in image was generated — each of these uses the CSS motif band described in `VISUAL_ASSET_MAP.md`, so no page shows a broken or misleading image.

| Module | Title | Track | Motif in use |
| --- | --- | --- | --- |
| AI-03 | AI Capabilities | AI Courses | `flow` |
| AI-04 | AI Limitations | AI Courses | `layers` |
| DW-02 | Research with AI | AI for Day-to-Day Work | `flow` |
| DW-03 | Report Preparation with AI | AI for Day-to-Day Work | `layers` |
| DW-05 | Excel with AI | AI for Day-to-Day Work | `flow` |
| DW-06 | Presentations with AI | AI for Day-to-Day Work | `layers` |
| DW-09 | Brainstorming with AI | AI for Day-to-Day Work | `network` |
| DW-10 | Planning with AI | AI for Day-to-Day Work | `flow` |
| PE-02 | Instructions & Context | Prompt Engineering | `prompt` |
| PE-04 | Examples & Structured Prompts | Prompt Engineering | `prompt` |
| PE-05 | Advanced Prompting | Prompt Engineering | `layers` |
| PE-07 | Evaluating AI Responses | Prompt Engineering | `flow` |
| PS-01 | Business Communication | Professional Skills | `layers` |
| PS-02 | Professional Email Writing | Professional Skills | `layers` |
| PS-03 | English for the Workplace | Professional Skills | `flow` |
| PS-05 | Productivity Systems | Professional Skills | `flow` |
| PS-07 | Critical Thinking | Professional Skills | `network` |
| SEC-01 | Password Security | Security & Data Privacy | `shield` |
| SEC-02 | Phishing & Social Engineering | Security & Data Privacy | `shield` |
| SEC-05 | Handling Confidential Information | Security & Data Privacy | `layers` |
| SEC-06 | Safe Use of AI at Work | Security & Data Privacy | `network` |

**21 of 39 modules are affected.**

To close a gap, drop a 16:7 JPEG into `assets/`, add `"cover_image": "assets/<file>.jpg"` to that module's `DECK`, and re-run `python sitegen.py`. The generator refuses to build if a declared image file is missing, so a broken reference cannot ship.
