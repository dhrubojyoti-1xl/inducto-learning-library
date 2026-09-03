# -*- coding: utf-8 -*-
"""DW-03 — Report Preparation with AI. Content only."""

DECK = {
    "module_code": "DW-03",
    "area": "02-ai-daily-work",
    "filename": "02-03-report-preparation-with-ai.pptx",
    "title": "Report Preparation with AI",
    "subtitle": "Turning what you already know into a report somebody actually "
                "reads to the end.",
    "duration_min": 18,
    "audience": "New joiners + staff",
    "motif": "layers",

    "why": {
        "title": "Ravi writes reports nobody finishes",
        "icon": "doc",
        "scenario": "Ravi is a site engineer covering three plants near Pune. "
                    "His visit reports are thorough and eleven pages long. His "
                    "manager reads the first page and rings him for the rest, "
                    "every single time.",
        "cost": "Six hours of writing, and the same phone call anyway.",
        "fix": "The answer first, in one paragraph. The detail underneath it.",
    },

    "outcomes": [
        ("list", "Put the answer in the first paragraph, every time"),
        ("doc", "Turn rough site notes into a readable report in ten minutes"),
        ("sheet", "Keep one report structure your team recognises on sight"),
        ("eye", "Cut a report in half without losing anything that matters"),
        ("check", "Make sure every number in it traces to something real"),
    ],

    "sections": [
        ("Answer first", "Why page eleven is too late", "s_first"),
        ("The five-part shape", "One structure, every report", "s_shape"),
        ("Notes into report", "Ten minutes, grounded", "s_notes"),
        ("Cutting it in half", "Without losing substance", "s_cut"),
        ("Do this now", "Rewrite one real report", "s_do"),
        ("Choose what you'd do", "A month-end decision", "scenario"),
        ("Watch this", "A 9-minute outside walkthrough", "video"),
    ],

    "slides": [
        {
            "anchor": "s_first",
            "label": "Answer first",
            "title": "Page eleven is too late",
            "lead": "Most work reports are written in the order the work "
                    "happened. Nobody reads in that order.",
            "visual": {
                "type": "split",
                "left": {
                    "tag": "Written in order", "tone": "bad",
                    "title": "How the work happened",
                    "items": [
                        "Background and scope of the visit",
                        "What was inspected, area by area",
                        "Observations in the sequence found",
                        "Conclusion and recommendation, page eleven",
                    ],
                },
                "right": {
                    "tag": "Answer first", "tone": "good",
                    "title": "How it gets read",
                    "items": [
                        "The recommendation, in one paragraph",
                        "The three findings behind it",
                        "What happens next, and who does it",
                        "Everything else, for whoever wants it",
                    ],
                },
            },
        },
        {
            "label": "Answer first",
            "title": "The one paragraph that matters",
            "visual": {
                "type": "prompt",
                "header": "Copy this opening-paragraph prompt",
                "text": "Write the opening paragraph of a report, under 80 "
                        "words. It must state the conclusion, the single most "
                        "important reason for it, and what I am asking the "
                        "reader to do. Use only the facts below. Do not add "
                        "background, and do not describe what the report "
                        "contains.",
                "caption": "If your reader stops after this paragraph, they "
                           "still know what to do.",
                "why": [
                    "\"Do not describe what the report contains\" kills the "
                    "usual filler.",
                    "Conclusion, reason, ask — the three things a manager "
                    "needs.",
                    "Eighty words forces a real decision about what matters.",
                ],
            },
        },
        {
            "anchor": "s_shape",
            "label": "The five-part shape",
            "title": "One shape for every report",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "WHAT I FOUND — the conclusion, in one paragraph",
                    "WHY IT MATTERS — the impact, in numbers where possible",
                    "WHAT I RECOMMEND — one clear action, with an owner",
                    "WHAT I SAW — the evidence, as long as it needs to be",
                ],
            },
        },
        {
            "label": "The five-part shape",
            "title": "Why a fixed shape helps",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "clock", "label": "Faster to write",
                     "sub": "The structure stops being a decision, so you "
                            "spend your time on content instead."},
                    {"icon": "eye", "label": "Faster to read",
                     "sub": "Your manager learns where things live and stops "
                            "hunting for the recommendation."},
                    {"icon": "sheet", "label": "Comparable",
                     "sub": "Six site reports in the same shape can be read "
                            "side by side. Six freeform ones cannot."},
                ],
            },
        },
        {
            "anchor": "s_notes",
            "label": "Notes into report",
            "title": "Rough notes into a report",
            "visual": {
                "type": "prompt_out",
                "text": "Turn these site notes into a report using this exact "
                        "structure: WHAT I FOUND, WHY IT MATTERS, WHAT I "
                        "RECOMMEND, WHAT I SAW. Use only my notes. Add no "
                        "causes, no numbers and no recommendations I have not "
                        "written. Where something is missing, write [CHECK]. "
                        "Under 400 words.",
                "caption": "Then paste your notes underneath, however rough "
                           "they are.",
                "out_title": "What comes back",
                "out": [
                    "A four-part report in the shape your team already "
                    "recognises.",
                    "[CHECK] wherever your notes were thin, instead of an "
                    "invented cause.",
                    "Six hours of writing becomes twenty minutes of checking "
                    "and editing.",
                ],
            },
        },
        {
            "label": "Notes into report",
            "title": "The line that protects you",
            "visual": {
                "type": "bandlist",
                "mark": "ban",
                "headline": "\"Add no causes I have not written\" is the most "
                            "important line in a report prompt.",
                "sub": "Reports are where invented explanations do the most "
                       "damage, because people act on them.",
                "cols": 3,
                "items": [
                    "It will suggest a cause if you let it.",
                    "The cause will sound reasonable.",
                    "Somebody will fix the wrong thing.",
                ],
            },
        },
        {
            "anchor": "s_cut",
            "label": "Cutting it in half",
            "title": "Cut it without losing it",
            "visual": {
                "type": "prompt",
                "header": "Copy this cutting prompt",
                "text": "Cut this report to half its length. Keep every "
                        "number, date, name of a location and recommendation "
                        "exactly as written. Remove background, repetition and "
                        "anything that describes the report itself. Do not "
                        "rewrite the conclusions.",
                "caption": "Naming what to protect is what makes cutting "
                           "safe.",
                "why": [
                    "Without the protection list it cuts numbers first.",
                    "Background and self-description are usually a third of "
                    "it.",
                    "The conclusions stay in your words, not its paraphrase.",
                ],
            },
        },
        {
            "label": "Cutting it in half",
            "title": "What to cut, what to keep",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "Eleven pages",
                "bad": [
                    "Two pages of background the reader already knows.",
                    "Every area inspected, including the ones with nothing to "
                    "report.",
                    "The recommendation on page eleven, in a paragraph about "
                    "next steps.",
                ],
                "good_tag": "Four pages",
                "good": [
                    "Recommendation in the first eighty words.",
                    "Three findings that actually changed something.",
                    "Full evidence still there, at the back, for whoever wants "
                    "it.",
                ],
                "note": "Nothing was lost. It was reordered so that stopping "
                        "early still leaves the reader informed.",
            },
        },
        {
            "anchor": "s_do",
            "label": "Do this now",
            "title": "Do this now: rewrite one",
            "visual": {
                "type": "steps",
                "items": [
                    "Open the last report you wrote that got a phone call "
                    "back.",
                    "Find your recommendation and move it to the top.",
                    "Paste it in with the cutting prompt and a word limit.",
                    "Compare the two. Send the short one next time.",
                ],
                "prompt": "Rewrite this report so the conclusion and "
                          "recommendation come first, in under 80 words, "
                          "followed by the three findings that support them, "
                          "then everything else. Keep all numbers and dates "
                          "exactly. Change no conclusions. Mark anything "
                          "unclear as [CHECK].",
                "caption": "The fastest improvement most people can make to "
                           "their writing.",
            },
        },
        {
            "label": "Do this now",
            "title": "Before it leaves your desk",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Every number traces to a note, a system or a photo.",
                    "No cause is stated that you did not personally establish.",
                    "The recommendation names one owner and one date.",
                    "Someone reading only the first paragraph knows what to "
                    "do.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Five mistakes people really make",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Letting it explain why something happened",
                     "It was not there. A plausible cause sends somebody to "
                     "fix the wrong machine."),
                    ("Writing in the order the work happened",
                     "Your reader is not retracing your day. They want the "
                     "answer and then the proof."),
                    ("Asking for \"a professional report\"",
                     "You get headings, filler and an executive summary that "
                     "summarises nothing."),
                    ("Cutting without protecting the numbers",
                     "Told simply to shorten, it drops figures before it drops "
                     "adjectives."),
                    ("Keeping the self-describing paragraph",
                     "\"This report sets out the findings of...\" is fifty "
                     "words that inform nobody."),
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Reports you should not automate",
            "visual": {
                "type": "tree",
                "question": "Does this report make a judgement about a person?",
                "yes": {
                    "path": "Yes", "tone": "neutral", "label": "Write it "
                                                              "yourself",
                    "detail": "Performance, conduct, capability, incident "
                              "reports involving individuals. Your judgement, "
                              "in your words. Use AI to check clarity "
                              "afterwards at most.",
                },
                "no": {
                    "path": "No", "tone": "good", "label": "Draft it with AI",
                    "detail": "Site visits, monthly summaries, project "
                              "updates, technical findings. You supply the "
                              "observations and it supplies the structure and "
                              "the sentences.",
                },
            },
        },
        {
            "label": "Do this now",
            "title": "What a good report does",
            "visual": {
                "type": "nested",
                "layers": [
                    {"label": "First paragraph",
                     "sub": "The reader knows what to do, and can stop here."},
                    {"label": "Next half page",
                     "sub": "They know why, and can defend it to someone else."},
                    {"label": "The rest",
                     "sub": "Evidence, available if anyone challenges it."},
                ],
                "note": "Almost nobody reads a report end to end. Writing for "
                        "the reader who stops early is not dumbing down — it "
                        "is the whole craft.",
            },
        },
        {
            "label": "Do this now",
            "title": "The report rule",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "You supply the findings. It supplies the "
                            "structure. Nobody supplies the causes but you.",
                "sub": "Findings and causes are different things, and only one "
                       "of them can be observed.",
                "cols": 3,
                "items": [
                    "Observations — yours.",
                    "Structure and wording — its job.",
                    "Causes — only what you established.",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Month-end, 6:20 pm",
        "situation": "Your site report is due tonight. You have four pages of "
                     "rough notes, two photographs and a manager who reads "
                     "only the first page.",
        "choices": [
            {
                "text": "Ask it to write the report and explain the "
                        "rejection trend.",
                "tone": "bad",
                "headline": "It will explain something it never saw",
                "consequence": "The report is well written and confidently "
                               "attributes the trend to operator changeover. "
                               "Your notes say nothing about changeover. "
                               "Maintenance spend two days on the wrong line, "
                               "citing your report.",
                "rule": "It can order your observations. It cannot know why "
                        "they happened.",
            },
            {
                "text": "Ask for the four-part structure, using only your "
                        "notes, with [CHECK] for gaps.",
                "tone": "good",
                "headline": "Twenty minutes, and it says only what you saw",
                "consequence": "You get the report in the shape your manager "
                               "recognises, with three [CHECK] markers where "
                               "your notes were thin. You fill two from memory "
                               "and flag the third as needing a follow-up "
                               "visit. Sent at 6:45.",
                "rule": "A marked gap is worth more than a smooth invention.",
            },
            {
                "text": "Type the whole report yourself, as usual.",
                "tone": "ok",
                "headline": "Accurate, and you will be here until nine",
                "consequence": "Everything in it is true, because you wrote "
                               "every word. It is also eleven pages in the "
                               "order the day happened, so your manager reads "
                               "page one and rings you tomorrow, exactly as "
                               "always.",
                "rule": "Writing it yourself protects accuracy, not "
                        "readability.",
            },
        ],
    },

    # Title, channel and runtime were read back from YouTube
    # itself. See newvideos.json.
    "video": {
        "url": "https://www.youtube.com/watch?v=1QY5HtuvTaw",
        "title": "📑 Effortless report writing with AI! 🚀",
        "channel": "Astranti",
        "duration": "9:17",
        "heading": "Nine minutes on report writing",
        "note": "An outside video, not company material. Where it differs "
                "from this module, follow this module.",
        "how": [
            "Optional. Everything you need is already in this deck.",
            "Useful if you prefer watching to reading.",
            "It opens in your browser. Turn the sound on.",
        ],
    },

    "quiz": [
        {
            "q": "Where does the recommendation go?",
            "remember": "First paragraph, always.",
            "answers": [
                {"text": "At the end, after the evidence", "ok": False,
                 "why": "That is the order the work happened, not the order it "
                        "gets read. Your reader reaches page one and rings you "
                        "for the answer."},
                {"text": "In the first paragraph, with the reason and the ask",
                 "ok": True,
                 "why": "If they stop after eighty words they still know what "
                        "you found, why it matters and what you want them to "
                        "do. Everything after that is supporting evidence."},
                {"text": "In a separate covering email", "ok": False,
                 "why": "Then the report and its conclusion get separated the "
                        "first time either is forwarded, and the report on its "
                        "own reads as inconclusive."},
                {"text": "In the middle, after the context", "ok": False,
                 "why": "The middle is where attention is lowest. It is the "
                        "worst place for the one paragraph that has to "
                        "survive a skim."},
            ],
        },
        {
            "q": "Which line protects a report most?",
            "remember": "\"Add no causes I have not written.\"",
            "answers": [
                {"text": "\"Make it professional\"", "ok": False,
                 "why": "It produces headings and filler. It does nothing "
                        "about the one real risk, which is an invented "
                        "explanation people then act on."},
                {"text": "\"Add no causes I have not written\"", "ok": True,
                 "why": "Reports are where invented causes do real damage, "
                        "because somebody schedules work against them. This "
                        "line turns a smooth explanation into an honest gap."},
                {"text": "\"Keep it under 400 words\"", "ok": False,
                 "why": "Useful for readability, and it does nothing about "
                        "accuracy. A short report can carry an invented cause "
                        "just as easily as a long one."},
                {"text": "\"Use formal language\"", "ok": False,
                 "why": "Style only. Formal language arguably makes an "
                        "invented cause more convincing, not less."},
            ],
        },
        {
            "q": "How do you cut a report safely?",
            "remember": "Name what must survive.",
            "answers": [
                {"text": "Ask it to shorten the report", "ok": False,
                 "why": "Told only to shorten, it drops specifics before it "
                        "drops adjectives. You lose figures and dates and keep "
                        "the background."},
                {"text": "Say what to protect: numbers, dates, recommendations",
                 "ok": True,
                 "why": "A protection list changes what gets cut. Background, "
                        "repetition and self-description go, and everything "
                        "load-bearing stays exactly as you wrote it."},
                {"text": "Cut it yourself, line by line", "ok": False,
                 "why": "Reliable and slow. Worth doing for a board paper; "
                        "unnecessary for a routine report where a protection "
                        "list does the same job in seconds."},
                {"text": "Ask for bullet points instead", "ok": False,
                 "why": "That changes the format rather than the length, and "
                        "bullets often lose the reasoning that connected the "
                        "findings."},
            ],
        },
        {
            "q": "Which report should you write alone?",
            "remember": "Anything judging a person.",
            "answers": [
                {"text": "A monthly production summary", "ok": False,
                 "why": "Repeated, factual and structured. The ideal case for "
                        "a stored prompt, as long as you supply every figure."},
                {"text": "A conduct report about a named employee", "ok": True,
                 "why": "It concerns a person, it may be read in a formal "
                        "process, and it must carry your judgement in your "
                        "words. Their name should also never be typed into the "
                        "tool at all."},
                {"text": "A site visit report", "ok": False,
                 "why": "Observations you made, structured by the tool. Just "
                        "make sure it adds no causes you did not personally "
                        "establish."},
                {"text": "A project status update", "ok": False,
                 "why": "Routine and repeated. A fixed structure makes six "
                        "months of updates comparable, which is worth more "
                        "than freeform prose."},
            ],
        },
        {
            "q": "What does [CHECK] achieve in a draft?",
            "remember": "A visible gap instead of a smooth invention.",
            "answers": [
                {"text": "It tells the tool to research the point", "ok": False,
                 "why": "It cannot research anything. The marker is an "
                        "instruction to stop and flag, not to go and find."},
                {"text": "It marks where your notes were thin, instead of "
                         "filling it", "ok": True,
                 "why": "Without it, a gap in your notes is closed with "
                        "something plausible and you never see it happen. With "
                        "it, you get a marker you can resolve properly or flag "
                        "for a follow-up."},
                {"text": "It hides incomplete sections from the reader",
                 "ok": False,
                 "why": "The opposite. It makes them visible, to you first and "
                        "then to your reader if you choose to leave it in."},
                {"text": "It shortens the report", "ok": False,
                 "why": "Marginally, and that is not the point. The value is "
                        "honesty about what you actually established."},
            ],
        },
    ],

    "recap": {
        "title": "Report writing on one screen",
        "points": [
            ("Answer first, always",
             "Conclusion, reason and ask in the first eighty words."),
            ("One shape every time",
             "Found, matters, recommend, saw. Faster to write and to read."),
            ("Never let it supply causes",
             "It was not there. An invented cause sends people to fix the "
             "wrong thing."),
            ("Mark gaps with [CHECK]",
             "A visible gap is worth far more than a smooth invention."),
            ("Protect before you cut",
             "Name the numbers, dates and recommendations that must survive."),
            ("Write for the reader who stops",
             "Almost nobody reaches the end. Design for the first page."),
        ],
        "oneliner": "You supply the findings. It supplies the structure. "
                    "Nobody supplies the causes but you.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("doc", "The notes-into-report prompt",
             "Four-part structure, no invented causes, [CHECK] for gaps."),
            ("list", "The opening-paragraph prompt",
             "Conclusion, reason and ask in under eighty words."),
            ("cycle", "The safe-cutting prompt",
             "Half the length, with numbers and dates protected."),
        ],
        "links": [
            ("Microsoft Copilot", "https://copilot.microsoft.com"),
            ("ChatGPT", "https://chatgpt.com"),
            ("Google Gemini", "https://gemini.google.com"),
        ],
        "next": "Next module: DW-04, Data Analysis with AI. Getting a straight "
                "answer out of a spreadsheet without letting it invent the "
                "arithmetic.",
    },

    "glossary": [
        ("Executive summary", "The opening paragraph carrying the conclusion, "
                              "the reason and the ask."),
        ("Finding", "Something you observed. Different from a cause, which is "
                    "an explanation of it."),
        ("Cause", "Why something happened. Only you can establish this, and "
                  "only if you checked."),
        ("[CHECK]", "A marker the tool writes where a fact is missing, instead "
                    "of inventing one."),
        ("Prompt", "Everything you type in: your notes, the structure and the "
                   "constraints."),
        ("Output", "What comes back. Your draft, which you are responsible for "
                   "checking."),
    ],
}
