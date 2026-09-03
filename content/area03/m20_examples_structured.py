# -*- coding: utf-8 -*-
"""PE-04 — Examples & Structured Prompts. Content only."""

DECK = {
    "module_code": "PE-04",
    "area": "03-prompt-engineering",
    "filename": "03-04-examples-and-structured-prompts.pptx",
    "title": "Examples & Structured Prompts",
    "subtitle": "Showing one good example beats three paragraphs describing "
                "what good looks like.",
    "duration_min": 18,
    "audience": "New joiners + staff",
    "motif": "prompt",

    "why": {
        "title": "Aditya explains the format four times",
        "icon": "sheet",
        "scenario": "Aditya prepares payment summaries for a Mumbai finance "
                    "team. He describes the format he wants in three "
                    "sentences. The answer comes back close but wrong. He "
                    "describes it again. And again. On the fourth try he "
                    "pastes one finished example instead.",
        "cost": "Twelve minutes of describing, when showing took twenty "
                "seconds.",
        "fix": "One worked example does what a paragraph of description "
               "cannot.",
    },

    "outcomes": [
        ("clip", "Turn a format you keep re-explaining into a single example"),
        ("sheet", "Get the same layout back every time, without editing"),
        ("list", "Use two examples to fix a tone you cannot describe"),
        ("check", "Write a fill-in-the-blanks prompt that cannot drift"),
        ("cycle", "Build a structured prompt you reuse without rewriting"),
    ],

    "sections": [
        ("Show, do not describe", "Why one example wins", "s_show"),
        ("One example, done well", "The worked pattern", "s_one"),
        ("Two examples fix tone", "What description cannot reach", "s_two"),
        ("Fill-in-the-blanks", "Structure that cannot drift", "s_blank"),
        ("Do this now", "Turn a repeat job into a template", "s_do"),
        ("Choose what you'd do", "A month-end decision", "scenario"),
        ("Watch this", "A 5-minute outside explainer", "video"),
    ],

    "slides": [
        {
            "anchor": "s_show",
            "label": "Show, do not describe",
            "title": "Why one example wins",
            "lead": "Describing a format is a translation step. An example "
                    "removes it entirely.",
            "gloss": ["Few-shot"],
            "visual": {
                "type": "flow",
                "steps": [
                    ("You describe a format", "Three sentences about columns "
                                              "and order."),
                    ("It interprets them", "Its reading of your words, not "
                                           "your picture."),
                    ("You correct it", "Twice, usually, and it drifts back."),
                    ("Or you show one", "The pattern is now unambiguous."),
                ],
            },
        },
        {
            "label": "Show, do not describe",
            "title": "Describing versus showing",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "Described",
                "bad": [
                    "\"Give me a short summary line for each invoice, with the "
                    "amount at the end in brackets.\"",
                    "You get full sentences, amounts in the middle, and a "
                    "heading you did not ask for.",
                    "Three rounds of correction later it is nearly right.",
                ],
                "good_tag": "Shown",
                "good": [
                    "\"Follow this exact pattern: Ashirwad Traders — 45 days "
                    "overdue, second reminder sent (₹2,40,000)\"",
                    "You get twelve lines in that shape, first time.",
                    "Nothing to correct, because nothing was open to "
                    "interpretation.",
                ],
                "note": "An example is not a hint. It is the specification, "
                        "written in the only language that cannot be "
                        "misread.",
            },
        },
        {
            "anchor": "s_one",
            "label": "One example, done well",
            "title": "The one-example prompt",
            "visual": {
                "type": "prompt",
                "text": "Rewrite each line below to follow this exact pattern, "
                        "and nothing else: Ashirwad Traders — 45 days overdue, "
                        "second reminder sent (₹2,40,000). Keep the same "
                        "punctuation, the same order and the brackets. No "
                        "heading, no introduction, one line per entry.",
                "caption": "Then paste your messy lines underneath it.",
                "why": [
                    "The example fixes order, punctuation and bracket style at "
                    "once.",
                    "\"No heading, no introduction\" stops the usual "
                    "additions.",
                    "You can check twelve lines against one pattern in "
                    "seconds.",
                ],
            },
        },
        {
            "label": "One example, done well",
            "title": "What makes an example work",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "It is complete — no gaps for the tool to interpret.",
                    "It is real — an actual line you would have written.",
                    "It shows edge details — punctuation, casing, brackets.",
                    "It is followed by \"same pattern, nothing else\".",
                ],
            },
        },
        {
            "anchor": "s_two",
            "label": "Two examples fix tone",
            "title": "Two examples fix a tone",
            "lead": "Tone is the thing people describe worst and recognise "
                    "instantly. Show it twice.",
            "visual": {
                "type": "prompt_out",
                "header": "Copy this two-example prompt",
                "text": "Match the tone of these two examples exactly. "
                        "Example one: \"Thanks — noted. I will confirm the "
                        "revised date by Thursday.\" Example two: \"Understood. "
                        "We will cover the freight difference on this "
                        "consignment.\" Now write a reply to the message "
                        "below, in that same tone.",
                "caption": "Short, warm, no padding. Far easier to show than "
                           "to describe.",
                "out_title": "What comes back",
                "out": [
                    "A reply in the same clipped, decisive register as your "
                    "two examples.",
                    "No \"I hope this finds you well\", because neither "
                    "example had one.",
                    "Tone matched without you ever finding a word for it.",
                ],
            },
        },
        {
            "label": "Two examples fix tone",
            "title": "How many examples to give",
            "visual": {
                "type": "split",
                "left": {
                    "tag": "One example", "tone": "neutral", "mark": "list",
                    "title": "Fixes structure",
                    "items": [
                        "Layout, order and punctuation",
                        "Field names and their sequence",
                        "Line length and bracket style",
                        "Enough for most formatting jobs",
                    ],
                },
                "right": {
                    "tag": "Two or three", "tone": "accent", "mark": "check",
                    "title": "Fixes tone and judgement",
                    "items": [
                        "Register — clipped, warm, formal",
                        "What to include and what to drop",
                        "How to handle an awkward case",
                        "Worth it for anything customer-facing",
                    ],
                },
            },
        },
        {
            "anchor": "s_blank",
            "label": "Fill-in-the-blanks",
            "title": "Structure that cannot drift",
            "visual": {
                "type": "prompt",
                "header": "Copy this structured prompt",
                "text": "Fill in this exact structure and change nothing else. "
                        "SITUATION: one sentence. WHAT CHANGED: one sentence. "
                        "IMPACT ON THE CUSTOMER: one sentence. WHAT WE ARE "
                        "DOING: two sentences. NEXT UPDATE: a date. Use only "
                        "the facts below and write [CHECK] where a fact is "
                        "missing.",
                "caption": "Headings in capitals are followed far more "
                           "reliably.",
                "why": [
                    "The shape is fixed, so every answer is comparable.",
                    "[CHECK] makes a missing fact visible instead of invented.",
                    "Anyone on the team can read it the same way.",
                ],
            },
        },
        {
            "label": "Fill-in-the-blanks",
            "title": "Where structure pays off most",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "cycle", "label": "Anything repeated",
                     "sub": "A weekly update, a site report, a delay note. The "
                            "shape stops being a decision every time."},
                    {"icon": "person", "label": "Anything compared",
                     "sub": "Five supplier assessments in the same five "
                            "fields can actually be read side by side."},
                    {"icon": "list", "label": "Anything handed over",
                     "sub": "A colleague picking it up knows exactly where "
                            "each piece of information lives."},
                ],
            },
        },
        {
            "anchor": "s_do",
            "label": "Do this now",
            "title": "Do this now: build one template",
            "visual": {
                "type": "steps",
                "items": [
                    "Find a document you produce more than once a month.",
                    "Take the best one you have ever written and open it.",
                    "Paste it in with the prompt on the right.",
                    "Save what comes back. That is your template from now on.",
                ],
                "prompt": "Below is a good example of a document I write "
                          "regularly. Turn it into a reusable template: keep "
                          "the structure and the headings exactly, and replace "
                          "every specific fact with a clearly marked bracket "
                          "saying what belongs there. Do not change the "
                          "wording around the brackets.",
                "caption": "Your own best work becomes the specification.",
            },
        },
        {
            "label": "Do this now",
            "title": "Never put these in an example",
            "visual": {
                "type": "bandlist",
                "mark": "ban",
                "headline": "An example is pasted text. Everything in it "
                            "leaves the company with it.",
                "sub": "Use a realistic invented case, or strip the real one "
                       "first.",
                "cols": 2,
                "items": [
                    "A real customer's name, site or contact details",
                    "Real prices, margins or contract wording",
                    "A colleague's name beside performance or pay",
                    "Account numbers, references or internal system names",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Four habits with examples",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Show one example before describing anything.",
                    "Follow it with \"same pattern, nothing else\".",
                    "Use capitals for structure headings you want obeyed.",
                    "Strip names and figures out of the example first.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Five mistakes people really make",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Describing a format in three sentences",
                     "You are asking it to imagine your picture. Showing the "
                     "picture takes twenty seconds."),
                    ("Giving a half-finished example",
                     "Every gap in the example becomes a decision it makes for "
                     "you, differently each time."),
                    ("Pasting a real customer record as the example",
                     "The format was the point. The name, address and amount "
                     "went with it."),
                    ("Using five examples when one would do",
                     "Long prompts dilute the instruction. One complete "
                     "example beats five partial ones."),
                    ("Forgetting \"nothing else\"",
                     "You get your format plus a heading, an introduction and "
                     "a closing line."),
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Describe or show?",
            "visual": {
                "type": "tree",
                "question": "Could I show what I want in under five lines?",
                "yes": {
                    "path": "Yes", "tone": "good", "label": "Show it",
                    "detail": "Layouts, tone, line formats, table shapes. An "
                              "example is shorter than the description and "
                              "cannot be misread.",
                },
                "no": {
                    "path": "No", "tone": "neutral", "label": "Describe it",
                    "detail": "Long documents and complex judgements. Describe "
                              "the structure in capitals, then show one "
                              "section as an example.",
                },
            },
        },
        {
            "label": "Do this now",
            "title": "The example rule",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "If you have explained the format twice, stop "
                            "explaining and paste an example.",
                "sub": "The second explanation is always slower than the "
                       "example would have been.",
                "cols": 3,
                "items": [
                    "One example — structure fixed.",
                    "Two examples — tone fixed.",
                    "Zero examples — you will explain it again.",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Month-end, 5:10 pm",
        "situation": "You need twenty overdue-account lines in a specific "
                     "format for tomorrow's review. You have described the "
                     "format twice and the answer is still not right.",
        "choices": [
            {
                "text": "Describe the format a third time, more carefully.",
                "tone": "ok",
                "headline": "It may work. It will not work reliably.",
                "consequence": "The third description gets you closer, and the "
                               "twentieth line still drifts. You end up "
                               "hand-editing six of them, which is exactly the "
                               "work you were trying to avoid, twelve minutes "
                               "later than you started.",
                "rule": "A third description is the signal to switch to an "
                        "example.",
            },
            {
                "text": "Write one perfect line yourself and say \"follow this "
                        "exactly\".",
                "tone": "good",
                "headline": "Twenty seconds, and twenty correct lines",
                "consequence": "You write one line the way you want it, using "
                               "an invented company name. You add \"same "
                               "pattern, nothing else, one line per entry\". "
                               "All twenty come back correct, and you check "
                               "them against the pattern in under a minute.",
                "rule": "Show the pattern once. Never describe it three "
                        "times.",
            },
            {
                "text": "Paste last month's finished report as the example.",
                "tone": "bad",
                "headline": "Right method, wrong file",
                "consequence": "The format lands perfectly. So do twenty real "
                               "customer names, their outstanding amounts and "
                               "their payment histories, into a tool the "
                               "company cannot audit. The formatting problem "
                               "is solved and a much larger one has started.",
                "rule": "Show the shape with invented data. Never with a real "
                        "record.",
            },
        ],
    },

    "video": {
        "url": "https://www.youtube.com/watch?v=9qdgEBVkWR4",
        "title": "Discover Few-Shot Prompting | Google AI Essentials",
        "channel": "Grow with Google",
        "duration": "4:31",
        "heading": "Five minutes on few-shot",
        "note": "From Google's own AI Essentials course. The worked "
                "examples above are the version you will actually use.",
        "how": [
            "Optional. The prompts in this deck already work as written.",
            "Useful if you like watching a method demonstrated.",
            "It opens in your browser. Turn the sound on.",
        ],
    },

    "quiz": [
        {
            "q": "Why does an example beat a description?",
            "remember": "A description has to be interpreted. An example does "
                        "not.",
            "answers": [
                {"text": "Examples are shorter", "ok": False,
                 "why": "They usually are, but that is a side benefit. A long "
                        "example still beats a short description, because "
                        "there is nothing left to interpret."},
                {"text": "A description must be interpreted; an example cannot "
                         "be", "ok": True,
                 "why": "Exactly. Your three sentences about layout become its "
                        "reading of your sentences. An example is the picture "
                        "itself, so the translation step disappears."},
                {"text": "The tool copies examples word for word", "ok": False,
                 "why": "It does not copy — it follows the pattern. That is "
                        "what you want, because your new content is different "
                        "while the shape stays fixed."},
                {"text": "Examples stop it inventing facts", "ok": False,
                 "why": "Different problem. Examples fix format and tone. "
                        "Invented facts are controlled by supplying the facts "
                        "and saying \"add nothing\"."},
            ],
        },
        {
            "q": "How many examples for tone?",
            "remember": "One fixes structure. Two fix tone.",
            "answers": [
                {"text": "One is always enough", "ok": False,
                 "why": "One is enough for layout, where the pattern is "
                        "visible in a single line. Tone is a range, and one "
                        "sample can be read as a one-off."},
                {"text": "Two or three, so the pattern is clearly a range",
                 "ok": True,
                 "why": "Two samples show what stays constant across different "
                        "content, which is precisely what tone is. Three is "
                        "the sensible upper limit before the prompt bloats."},
                {"text": "As many as you can find", "ok": False,
                 "why": "Long prompts dilute your actual instruction. Past "
                        "three, you are adding length without adding clarity."},
                {"text": "None — just describe the tone you want", "ok": False,
                 "why": "Tone is the single hardest thing to describe and the "
                        "easiest to demonstrate. \"Professional but warm\" "
                        "means something different to everyone."},
            ],
        },
        {
            "q": "What must follow your example?",
            "remember": "\"Same pattern, nothing else.\"",
            "answers": [
                {"text": "\"Do your best\"", "ok": False,
                 "why": "It gives the tool nothing to act on, and it leaves "
                        "the door open for a heading, an introduction and a "
                        "closing line you did not ask for."},
                {"text": "\"Follow this exactly, nothing else\"", "ok": True,
                 "why": "The second half is what stops the extras. Without it "
                        "you reliably get your format plus a friendly "
                        "introduction and a summary you then delete."},
                {"text": "\"Make it better than the example\"", "ok": False,
                 "why": "Now you have invited it to change the very thing you "
                        "were fixing. The example is the specification, not a "
                        "starting point to improve on."},
                {"text": "\"Use similar formatting\"", "ok": False,
                 "why": "\"Similar\" is an invitation to drift. By line twelve "
                        "you will be looking at three different layouts."},
            ],
        },
        {
            "q": "What goes into a good example?",
            "remember": "Complete, realistic, and carrying no real data.",
            "answers": [
                {"text": "A real record, so it is definitely accurate",
                 "ok": False,
                 "why": "The format is what you are demonstrating, and it "
                        "works identically with invented data. A real record "
                        "sends a real customer's details out of the company."},
                {"text": "A complete invented case with all the edge details",
                 "ok": True,
                 "why": "Complete means no gaps for it to fill differently "
                        "each time. Invented means nothing leaves the company. "
                        "Edge details mean punctuation and brackets land "
                        "right."},
                {"text": "A rough sketch of the layout", "ok": False,
                 "why": "Every gap in a sketch becomes a decision the tool "
                        "makes for you, and it will make it differently on "
                        "line nine than on line two."},
                {"text": "Three partial examples", "ok": False,
                 "why": "Three incomplete patterns give it three different "
                        "signals. One complete example is clearer than three "
                        "half ones."},
            ],
        },
        {
            "q": "What does [CHECK] do in a template?",
            "remember": "It turns an invented fact into a visible gap.",
            "answers": [
                {"text": "It tells the tool to search for the answer",
                 "ok": False,
                 "why": "It cannot search. The marker is not an instruction to "
                        "find anything — it is an instruction to stop and "
                        "flag."},
                {"text": "It makes a missing fact visible instead of filled",
                 "ok": True,
                 "why": "Without it, a gap gets closed with something "
                        "plausible and you never see that it happened. With "
                        "it, you get a marker you can go and resolve "
                        "properly."},
                {"text": "It marks text for your manager to review", "ok": False,
                 "why": "You could use it that way, but its real job is "
                        "earlier: stopping the tool from quietly inventing the "
                        "missing piece in the first place."},
                {"text": "It shortens the output", "ok": False,
                 "why": "Length is unaffected. What changes is honesty — a gap "
                        "appears as a gap rather than as a confident sentence."},
            ],
        },
    ],

    "recap": {
        "title": "Examples on one screen",
        "points": [
            ("Show, do not describe",
             "A description must be interpreted. An example cannot be "
             "misread."),
            ("One example fixes structure",
             "Layout, order, punctuation and bracket style, all in one line."),
            ("Two examples fix tone",
             "Register is easy to recognise and almost impossible to describe."),
            ("Always add \"nothing else\"",
             "Otherwise you get your format plus a heading and an "
             "introduction."),
            ("Use capitals for structure",
             "SITUATION, IMPACT, NEXT UPDATE. Headings in capitals get "
             "followed."),
            ("Never show a real record",
             "The format works with invented data. A real one leaks a real "
             "customer."),
        ],
        "oneliner": "If you have explained the format twice, stop explaining "
                    "and paste an example.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("clip", "The one-example prompt",
             "One perfect line, then \"same pattern, nothing else\"."),
            ("chat", "The two-example tone prompt",
             "Two short samples, then your new message."),
            ("sheet", "The fill-in-the-blanks structure",
             "Capital headings, one sentence each, [CHECK] for gaps."),
        ],
        "links": [
            ("ChatGPT", "https://chatgpt.com"),
            ("Microsoft Copilot", "https://copilot.microsoft.com"),
            ("Google Gemini", "https://gemini.google.com"),
        ],
        "next": "Next module: PE-05, Advanced Prompting. Breaking a big job "
                "into steps, and setting constraints the answer has to respect.",
    },

    "glossary": [
        ("Few-shot", "Giving one or two worked examples before your request, "
                     "so the pattern is shown rather than described."),
        ("Zero-shot", "Asking without any example. Fine for simple jobs, weak "
                      "for formats and tone."),
        ("Template", "A reusable prompt with brackets where the specifics go."),
        ("Structured prompt", "A prompt with fixed headings the answer must "
                              "fill in, so every result is comparable."),
        ("Prompt", "Everything you type in: context plus instructions plus "
                   "your facts."),
        ("Output", "What comes back. Your draft, which you are responsible for "
                   "checking."),
    ],
}
