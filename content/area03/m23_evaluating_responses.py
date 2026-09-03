# -*- coding: utf-8 -*-
"""PE-07 — Evaluating AI Responses. Content only."""

DECK = {
    "module_code": "PE-07",
    "area": "03-prompt-engineering",
    "filename": "03-07-evaluating-ai-responses.pptx",
    "title": "Evaluating AI Responses",
    "subtitle": "A thirty-second way to decide whether to send it, fix it or "
                "throw it away.",
    "duration_min": 17,
    "audience": "New joiners + staff",
    "motif": "flow",

    "why": {
        "title": "Neha sends a draft she half-read",
        "icon": "eye",
        "scenario": "Neha writes training notes for a Noida team. The AI draft "
                    "reads well, so she skims it and sends it. Two paragraphs "
                    "in, it describes a sign-off step the company does not "
                    "have. Fourteen people follow it for a fortnight.",
        "cost": "A fortnight of a process nobody actually approved.",
        "fix": "Four questions, thirty seconds, before anything is sent.",
    },

    "outcomes": [
        ("check", "Score any answer against four questions in thirty seconds"),
        ("cycle", "Decide correctly between send, fix and throw away"),
        ("chat", "Write a correction that keeps the good 80 per cent"),
        ("eye", "Notice when a fluent answer is quietly avoiding your question"),
        ("list", "Compare two answers without re-reading both in full"),
    ],

    "sections": [
        ("The four questions", "Thirty seconds, every time", "s_four"),
        ("Send, fix or bin", "Choosing correctly", "s_decide"),
        ("Writing the correction", "Keep what worked", "s_fix"),
        ("Fluent but empty", "The answer that dodges", "s_dodge"),
        ("Do this now", "Score a real answer", "s_do"),
        ("Choose what you'd do", "A Friday afternoon decision", "scenario"),
        ("Watch this", "A 7-minute outside explainer", "video"),
    ],

    "slides": [
        {
            "anchor": "s_four",
            "label": "The four questions",
            "title": "Four questions, thirty seconds",
            "lead": "Ask these in order. Most answers fail on question two, "
                    "and you stop there.",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "TRACEABLE — is every fact one I supplied?",
                    "COMPLETE — did it answer what I actually asked?",
                    "USABLE — could I send this without rewriting it?",
                    "SAFE — would I be happy for anyone to read the prompt?",
                ],
            },
        },
        {
            "label": "The four questions",
            "title": "Why fluency fools people",
            "visual": {
                "type": "flow",
                "steps": [
                    ("It reads well", "Clean sentences, confident tone, no "
                                      "hedging."),
                    ("You relax", "Good writing signals care, in every other "
                                  "context."),
                    ("You skim", "You check the wording rather than the "
                                 "content."),
                    ("The middle slips through", "Where the invented line "
                                                 "usually is."),
                ],
            },
        },
        {
            "anchor": "s_decide",
            "label": "Send, fix or bin",
            "title": "Send, fix or throw away",
            "visual": {
                "type": "tree",
                "question": "Is the structure right and only the details "
                            "wrong?",
                "yes": {
                    "path": "Yes", "tone": "good", "label": "Fix it",
                    "detail": "Name what to keep, name what to change, supply "
                              "the correct fact. One line of correction beats "
                              "any amount of rewriting.",
                },
                "no": {
                    "path": "No", "tone": "bad", "label": "Throw it away",
                    "detail": "If the shape is wrong, the prompt was wrong. "
                              "Correcting it round by round costs more than "
                              "one better prompt would.",
                },
            },
        },
        {
            "label": "Send, fix or bin",
            "title": "The three-way test in practice",
            "visual": {
                "type": "split",
                "left": {
                    "tag": "Fix it", "tone": "good",
                    "title": "Structure right, details wrong",
                    "items": [
                        "Correct shape, one wrong date",
                        "Right tone, forty words too long",
                        "Good order, one invented line",
                        "Almost there, missing the closing ask",
                    ],
                },
                "right": {
                    "tag": "Start again", "tone": "bad",
                    "title": "It answered a different question",
                    "items": [
                        "Written for the wrong reader entirely",
                        "General advice where you wanted specifics",
                        "Ignored the constraint you cared most about",
                        "Three rounds in and still drifting",
                    ],
                },
            },
        },
        {
            "anchor": "s_fix",
            "label": "Writing the correction",
            "title": "Keep, change, supply",
            "visual": {
                "type": "prompt",
                "header": "Copy this correction pattern",
                "text": "Keep the structure, the tone and the first two "
                        "paragraphs exactly as they are. Change two things: "
                        "the review step in paragraph three does not exist, so "
                        "remove it; and the deadline is 15 March, not 12 "
                        "March. Reissue the whole thing.",
                "caption": "Keep, change, supply — in that order, every time.",
                "why": [
                    "Naming what to keep stops it rewriting the good part.",
                    "Two specific changes work far better than \"fix this\".",
                    "Supplying the right date means nothing gets invented.",
                ],
            },
        },
        {
            "label": "Writing the correction",
            "title": "Corrections that do not work",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("\"Make it better\"",
                     "There is no scale for better. You get a different draft "
                     "with a different set of problems."),
                    ("\"That is wrong, try again\"",
                     "It does not know which part. Usually it rewrites the "
                     "part that was fine."),
                    ("\"Shorter\"",
                     "It picks an amount. You will be back in a minute asking "
                     "again. Give a number."),
                    ("Listing eight changes at once",
                     "The first three land, the rest drift. Two or three per "
                     "round is the reliable limit."),
                ],
            },
        },
        {
            "anchor": "s_dodge",
            "label": "Fluent but empty",
            "title": "The answer that dodges",
            "lead": "Some answers are perfectly written and contain nothing. "
                    "They are the easiest to miss.",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "Fluent and empty",
                "bad": [
                    "You asked: \"Should we accept a 45-day payment term?\"",
                    "You got: three balanced paragraphs on the general "
                    "considerations around payment terms.",
                    "Nothing in it referred to your cash position or your "
                    "customer.",
                ],
                "good_tag": "Fluent and useful",
                "good": [
                    "You asked again with your facts and a forced answer.",
                    "\"Given the figures below, give one recommendation and "
                    "two reasons. No balanced overview.\"",
                    "You got a position you could argue with, which is what "
                    "you needed.",
                ],
                "note": "Balance is what it produces when it has nothing "
                        "specific to say. Ask for a position and it stops.",
            },
        },
        {
            "label": "Fluent but empty",
            "title": "Three signs of an empty answer",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "list", "label": "It lists considerations",
                     "sub": "\"There are several factors to weigh.\" You "
                            "already knew that. You wanted the weighing."},
                    {"icon": "cycle", "label": "It restates your question",
                     "sub": "A paragraph explaining what you asked is a "
                            "paragraph with no answer in it."},
                    {"icon": "chat", "label": "It hedges both ways",
                     "sub": "\"It depends on your circumstances\" is true, "
                            "useless and infinitely repeatable."},
                ],
            },
        },
        {
            "anchor": "s_do",
            "label": "Do this now",
            "title": "Do this now: score one answer",
            "visual": {
                "type": "steps",
                "items": [
                    "Open the last AI answer you actually used at work.",
                    "Run the four questions on it: traceable, complete, "
                    "usable, safe.",
                    "Mark any sentence you could not trace to your own input.",
                    "Send yourself the corrected version and notice how long "
                    "it took.",
                ],
                "prompt": "Score your own last answer against four questions "
                          "and reply in four short lines. One: which facts came "
                          "from my message and which from you. Two: which part "
                          "of my question you did not answer. Three: what you "
                          "would need from me to improve it. Four: nothing "
                          "else.",
                "caption": "A useful second pass, not a substitute for reading "
                           "it yourself.",
            },
        },
        {
            "label": "Do this now",
            "title": "Comparing two answers fast",
            "visual": {
                "type": "prompt_out",
                "header": "Copy this comparison prompt",
                "text": "Below are two versions of the same message. List only "
                        "the differences in substance — facts, commitments, "
                        "dates and numbers. Ignore differences in wording and "
                        "style completely. Use one line per difference.",
                "caption": "Saves re-reading two long drafts line by line.",
                "out_title": "What comes back",
                "out": [
                    "A short list of the real differences, usually three or "
                    "four.",
                    "No commentary about which version reads better.",
                    "You choose on substance in under a minute.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Four habits before you send",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Read the middle first. That is where problems hide.",
                    "Point at each number and name its source out loud.",
                    "Ask \"did it answer my question, or a nearby one?\"",
                    "If it is round four, throw it away and rewrite the "
                    "prompt.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "The round-four rule",
            "visual": {
                "type": "bandlist",
                "mark": "ban",
                "headline": "If you are on the fourth correction, the prompt "
                            "is the problem, not the answer.",
                "sub": "Rewriting the prompt takes two minutes. Round five "
                       "takes longer and usually fails too.",
                "cols": 3,
                "items": [
                    "Round one to two — normal.",
                    "Round three — check your prompt.",
                    "Round four — start again.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Five mistakes people really make",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Judging an answer by how well it reads",
                     "Fluency is constant. It tells you nothing about whether "
                     "the content is right."),
                    ("Checking the first and last paragraphs",
                     "The invented line is almost always in the middle, where "
                     "attention drops."),
                    ("Accepting a balanced overview as an answer",
                     "Balance is the default when it has nothing specific. Ask "
                     "for a position."),
                    ("Correcting the same draft five times",
                     "Three rounds of drift means the prompt was wrong. Fix "
                     "that instead."),
                    ("Asking the tool whether its answer is good",
                     "It will say yes, at length, in the same confident "
                     "voice."),
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "The evaluation rule",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "Judge it on what it says, never on how well it "
                            "says it.",
                "sub": "Every AI answer is well written. That is the one "
                       "signal you can safely ignore.",
                "cols": 3,
                "items": [
                    "Traceable and complete — send it.",
                    "Right shape, wrong details — fix it.",
                    "Wrong question answered — bin it.",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Friday, 3:45 pm",
        "situation": "You asked for a process note for a new joiner. The draft "
                     "is clear and confident. It also describes a sign-off "
                     "step you do not recognise, in paragraph three.",
        "choices": [
            {
                "text": "Send it — the rest is excellent and it is nearly five.",
                "tone": "bad",
                "headline": "Fourteen people now follow a step we do not have",
                "consequence": "The note goes into the induction pack. New "
                               "joiners follow the invented sign-off for a "
                               "fortnight, chasing an approval from someone "
                               "who does not give it. Unpicking it takes "
                               "longer than the whole document did.",
                "rule": "A process note becomes policy the moment it is "
                        "distributed.",
            },
            {
                "text": "Send one correction naming what to keep and what to "
                        "remove.",
                "tone": "good",
                "headline": "Ninety seconds, and the note is right",
                "consequence": "\"Keep everything except paragraph three. "
                               "There is no sign-off step — the supervisor "
                               "checks it at the end of shift instead. "
                               "Reissue.\" You get the same clean note with "
                               "one corrected paragraph, and send it at 3:52.",
                "rule": "Keep, change, supply. One round fixes almost "
                        "everything.",
            },
            {
                "text": "Ask the tool whether paragraph three is accurate.",
                "tone": "ok",
                "headline": "You will get a confident yes",
                "consequence": "It confirms the step, possibly adding detail "
                               "about why it exists. The confirmation was "
                               "generated exactly like the original claim, so "
                               "you now have two invented statements and more "
                               "confidence than you started with.",
                "rule": "It cannot check itself. You know the process — you "
                        "are the source here.",
            },
        ],
    },

    # Title, channel and runtime were read back from YouTube
    # itself. See newvideos.json.
    "video": {
        "url": "https://www.youtube.com/watch?v=gQx973zsOOw",
        "title": "Evaluating GenAI Output",
        "channel": "UBC LEARN",
        "duration": "6:32",
        "heading": "Seven minutes on judging output",
        "note": "Made for a university audience. The tests it teaches are "
                "the same ones you need at work.",
        "how": [
            "Optional. Everything you need is already in this deck.",
            "Useful if you prefer watching to reading.",
            "It opens in your browser. Turn the sound on.",
        ],
    },

    "quiz": [
        {
            "q": "What does question two ask?",
            "stem": "The four questions are traceable, complete, usable, safe.",
            "remember": "Did it answer my question, or a nearby one?",
            "answers": [
                {"text": "Is it long enough?", "ok": False,
                 "why": "Length is a formatting matter and easy to fix in one "
                        "line. Completeness is about whether your actual "
                        "question was addressed at all."},
                {"text": "Did it answer what I actually asked?", "ok": True,
                 "why": "This is where most answers fail. You asked whether to "
                        "accept a payment term; you received a balanced "
                        "overview of payment terms. Fluent, relevant, and not "
                        "an answer."},
                {"text": "Is the grammar correct?", "ok": False,
                 "why": "It essentially always is. Grammar is the one thing "
                        "you never need to check, and checking it distracts "
                        "from the things you do."},
                {"text": "Does it sound professional?", "ok": False,
                 "why": "It always sounds professional. That constant tone is "
                        "precisely why it cannot be used as a signal of "
                        "anything."},
            ],
        },
        {
            "q": "When should you throw it away?",
            "remember": "Wrong shape means a wrong prompt.",
            "answers": [
                {"text": "When one date is wrong", "ok": False,
                 "why": "That is a one-line fix. Naming what to keep and "
                        "supplying the right date takes ten seconds and "
                        "preserves everything that already worked."},
                {"text": "When it answered a different question", "ok": True,
                 "why": "If the shape is wrong, the prompt was wrong. "
                        "Correcting round by round from a wrong starting point "
                        "costs far more than writing one better prompt."},
                {"text": "When it is too long", "ok": False,
                 "why": "\"Cut to 120 words, keep both dates\" fixes that "
                        "immediately. Length is the cheapest thing to correct."},
                {"text": "When the tone is slightly off", "ok": False,
                 "why": "Tone corrects easily, especially if you show two short "
                        "examples of the register you want instead of "
                        "describing it."},
            ],
        },
        {
            "q": "What makes a correction work?",
            "remember": "Keep, change, supply.",
            "answers": [
                {"text": "Saying \"that is wrong, try again\"", "ok": False,
                 "why": "It has no idea which part. In practice it rewrites "
                        "the section that was fine and leaves the error where "
                        "it was."},
                {"text": "Naming what to keep, what to change, and the right "
                         "value", "ok": True,
                 "why": "All three parts matter. Keep protects the good "
                        "eighty per cent, change is specific enough to act on, "
                        "and supplying the value means nothing is invented to "
                        "replace it."},
                {"text": "Listing every problem you noticed", "ok": False,
                 "why": "Two or three changes land reliably. Beyond that the "
                        "later items drift, and you end up correcting the "
                        "correction."},
                {"text": "Asking it to review its own work", "ok": False,
                 "why": "You get a confident second generation praising the "
                        "first. It has no independent view to offer about "
                        "anything it produced."},
            ],
        },
        {
            "q": "Why is a balanced answer a warning?",
            "remember": "Balance is the default when it has nothing specific.",
            "answers": [
                {"text": "Balanced answers are usually wrong", "ok": False,
                 "why": "They are rarely wrong. They are usually true and "
                        "useless, which is a different and more slippery "
                        "problem."},
                {"text": "It is what it produces when it has nothing specific",
                 "ok": True,
                 "why": "With no facts of yours to work from, listing "
                        "considerations is the safest and most likely "
                        "continuation. Supply the figures and demand one "
                        "recommendation, and it stops."},
                {"text": "It means the tool is being cautious", "ok": False,
                 "why": "There is no caution happening. It is producing the "
                        "most likely text, and \"there are several factors to "
                        "consider\" is extremely likely text."},
                {"text": "Balance means the answer is incomplete", "ok": False,
                 "why": "It is complete as a piece of writing. What is missing "
                        "is any engagement with your particular situation, "
                        "which is what you asked about."},
            ],
        },
        {
            "q": "Where do problems usually hide?",
            "remember": "In the middle, where attention drops.",
            "answers": [
                {"text": "In the opening line", "ok": False,
                 "why": "You read the opening carefully, every time. Almost "
                        "nothing gets past a first line, which is exactly why "
                        "problems do not live there."},
                {"text": "In the middle paragraphs", "ok": True,
                 "why": "Attention drops after the opening and returns for the "
                        "close. Invented steps, dates and clauses survive in "
                        "the middle because that is where skimming happens."},
                {"text": "In the closing sentence", "ok": False,
                 "why": "You read the close too, because it usually carries "
                        "the ask or the next step. It gets checked almost as "
                        "reliably as the opening."},
                {"text": "In the subject line", "ok": False,
                 "why": "Short, prominent and read by everyone including you. "
                        "Errors there are caught immediately."},
            ],
        },
    ],

    "recap": {
        "title": "Evaluating answers on one screen",
        "points": [
            ("Four questions, thirty seconds",
             "Traceable, complete, usable, safe. Most answers fail on the "
             "second."),
            ("Ignore how well it reads",
             "Fluency is constant, so it carries no information about quality."),
            ("Read the middle first",
             "That is where the invented step or date survives a skim."),
            ("Keep, change, supply",
             "Protect the good part, name two changes, give the right value."),
            ("Balance means it has nothing",
             "Ask for one recommendation and two reasons instead."),
            ("Round four means rewrite",
             "Three rounds of drift is a prompt problem, not an answer "
             "problem."),
        ],
        "oneliner": "Judge it on what it says, never on how well it says it.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("check", "The four questions",
             "Traceable, complete, usable, safe. Thirty seconds."),
            ("cycle", "The correction pattern",
             "Keep this, change that, here is the right value."),
            ("list", "The comparison prompt",
             "Differences in substance only, one line each."),
        ],
        "links": [
            ("ChatGPT", "https://chatgpt.com"),
            ("Microsoft Copilot", "https://copilot.microsoft.com"),
            ("Google Gemini", "https://gemini.google.com"),
        ],
        "next": "Next track: DW-01, Email Writing with AI. The same "
                "evaluation habits, applied to the thing most people write "
                "twenty times a day.",
    },

    "glossary": [
        ("Evaluation", "Deciding whether an answer can be sent, needs fixing, "
                       "or should be thrown away."),
        ("Traceable", "Every fact in the answer can be pointed back to "
                      "something you supplied."),
        ("Correction", "A follow-up naming what to keep, what to change, and "
                       "the correct value."),
        ("Hedging", "Answering both ways at once. Usually a sign it has "
                    "nothing specific to say."),
        ("Prompt", "Everything you type in: context plus instructions plus "
                   "your facts."),
        ("Output", "What comes back. Your draft, which you are responsible for "
                   "checking."),
    ],
}
