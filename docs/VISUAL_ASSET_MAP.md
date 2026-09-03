# Visual asset map

## Decision

The source decks draw their diagrams as native PowerPoint shapes. Those were **re-implemented as HTML and CSS components**, not exported as slide screenshots. A screenshot would be a fixed-width image that cannot reflow on a phone, cannot be read by a screen reader, and cannot be searched. Every diagram type below is therefore live markup.

## Diagram types carried over

| Source visual | Count | HTML component |
| --- | ---: | --- |
| `checklist` | 81 | Tickable list; state is saved with the learner's progress. |
| `bandlist` | 72 | Coloured headline band followed by the supporting points. |
| `prompt` | 52 | Copyable prompt card with the 'why this works' points. |
| `mistakes` | 51 | Numbered mistake, then the consequence, side by side. |
| `iconrow` | 44 | Tile row with an accent mark per tile. |
| `steps` | 44 | Numbered instruction list beside a copy-to-clipboard prompt card. |
| `tree` | 39 | Decision question with the two branches beneath it. |
| `beforeafter` | 39 | Two panels, ✕ against ✓, plus the closing note. |
| `split` | 38 | Two comparison panels, tinted by tone. |
| `flow` | 35 | Numbered step cards, wrapping to one column on a phone. |
| `prompt_out` | 26 | Copyable prompt card beside what comes back. |
| `nested` | 17 | Indented containment blocks, outermost first. |
| **Total** | **538** | |

## Photographs

18 of the 39 modules have a hero photograph. These are the same JPEG files used on the deck covers, copied unchanged into `site/assets/images/`.

| Module | Image file |
| --- | --- |
| AI-01 — AI Fundamentals | `hero-ai-fundamentals.jpg` |
| AI-02 — Generative AI | `hero-generative-ai.jpg` |
| AI-05 — Hallucinations & Fact-Checking | `hero-hallucinations.jpg` |
| DW-01 — Email Writing with AI | `hero-email-ai.jpg` |
| DW-04 — Data Analysis with AI | `hero-data-analysis.jpg` |
| DW-07 — Documentation with AI | `hero-documentation.jpg` |
| DW-08 — Meeting Notes & Follow-ups | `hero-meetings.jpg` |
| DW-11 — Automation Basics | `hero-automation.jpg` |
| PE-01 — Basic Prompting | `hero-prompting-basics.jpg` |
| PE-03 — Role-Based Prompts | `hero-role-prompts.jpg` |
| PE-06 — Reusable Prompts | `hero-prompt-library.jpg` |
| PS-04 — Time Management | `hero-time-management.jpg` |
| PS-06 — Problem-Solving | `hero-problem-solving.jpg` |
| PS-08 — Presentation Skills | `hero-presentation-skills.jpg` |
| PS-09 — Teamwork & Collaboration | `hero-teamwork.jpg` |
| SEC-03 — Multi-Factor Authentication | `hero-mfa-identity.jpg` |
| SEC-04 — Data Protection Basics | `hero-data-protection.jpg` |
| SEC-07 — What Never to Paste Into AI | `hero-safe-ai-use.jpg` |

**No images were generated for this build.** The 18 files above were already in `assets/` and were copied, not created.

The remaining 21 modules use a CSS motif band carrying the module code. It is drawn with gradients, so there is no image file behind it and it can never 404.

| Module | Motif |
| --- | --- |
| AI-03 — AI Capabilities | `flow` |
| AI-04 — AI Limitations | `layers` |
| DW-02 — Research with AI | `flow` |
| DW-03 — Report Preparation with AI | `layers` |
| DW-05 — Excel with AI | `flow` |
| DW-06 — Presentations with AI | `layers` |
| DW-09 — Brainstorming with AI | `network` |
| DW-10 — Planning with AI | `flow` |
| PE-02 — Instructions & Context | `prompt` |
| PE-04 — Examples & Structured Prompts | `prompt` |
| PE-05 — Advanced Prompting | `layers` |
| PE-07 — Evaluating AI Responses | `flow` |
| PS-01 — Business Communication | `layers` |
| PS-02 — Professional Email Writing | `layers` |
| PS-03 — English for the Workplace | `flow` |
| PS-05 — Productivity Systems | `flow` |
| PS-07 — Critical Thinking | `network` |
| SEC-01 — Password Security | `shield` |
| SEC-02 — Phishing & Social Engineering | `shield` |
| SEC-05 — Handling Confidential Information | `layers` |
| SEC-06 — Safe Use of AI at Work | `network` |
