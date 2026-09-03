# -*- coding: utf-8 -*-
"""AI-04 — AI Limitations. Content only."""

DECK = {
    "module_code": "AI-04",
    "area": "01-ai-general",
    "filename": "01-04-ai-limitations.pptx",
    "title": "AI Limitations",
    "subtitle": "Where these tools break, why they break exactly there, and "
                "what to reach for instead.",
    "duration_min": 17,
    "audience": "New joiners + staff",
    "motif": "layers",

    "why": {
        "title": "Rajesh quotes a price that never existed",
        "icon": "warn",
        "scenario": "Rajesh handles purchase for an Ahmedabad unit. He asks an "
                    "AI tool for the current price of a steel grade. It "
                    "answers with a figure per tonne. He builds a quotation "
                    "around it. The real rate is 19 per cent higher.",
        "cost": "A quotation the company has to honour, or withdraw and "
                "explain.",
        "fix": "You will know which questions it cannot answer, before you "
               "ask one.",
    },

    "outcomes": [
        ("ban", "List the five things it structurally cannot do"),
        ("clock", "Explain what a training cut-off means for today's question"),
        ("warn", "Predict where an answer is most likely to be invented"),
        ("search", "Name the right tool for each thing AI cannot do"),
        ("check", "Design a question so its weak points cannot hurt you"),
    ],

    "sections": [
        ("The five hard limits", "What it structurally cannot do", "s_limits"),
        ("The cut-off date", "Why last month is missing", "s_cutoff"),
        ("Numbers and arithmetic", "Where confidence is highest", "s_numbers"),
        ("What to use instead", "The right tool per limit", "s_instead"),
        ("Designing around it", "Ask so it cannot hurt you", "s_design"),
        ("Choose what you'd do", "A Friday afternoon decision", "scenario"),
        ("Watch this", "A 9-minute outside explainer", "video"),
    ],

    "slides": [
        {
            "anchor": "s_limits",
            "label": "The five hard limits",
            "title": "Five things it cannot do",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("It cannot look anything up",
                     "Unless the tool visibly shows a link it visited, no page "
                     "was opened and no system was queried."),
                    ("It cannot know today's anything",
                     "Rates, stock, prices, news. Its knowledge stops at a "
                     "fixed date it will not always tell you."),
                    ("It cannot see our systems",
                     "No ERP, no CRM, no shared drive. Our order numbers and "
                     "clients simply do not exist for it."),
                    ("It cannot tell you it is unsure",
                     "Every answer arrives in the same confident tone, whether "
                     "solid or entirely invented."),
                    ("It cannot carry consequences",
                     "It will not be in the meeting when the number is wrong. "
                     "You will."),
                ],
            },
        },
        {
            "label": "The five hard limits",
            "title": "Why the gap gets filled",
            "lead": "It is built to produce the most likely next words. A gap "
                    "is just a place where something likely goes.",
            "visual": {
                "type": "flow",
                "steps": [
                    ("You ask something", "The question implies a fact should "
                                          "exist."),
                    ("It has no fact", "Nothing in its patterns matches your "
                                       "specific case."),
                    ("It builds a likely one", "A number, a name or a date "
                                               "shaped like a real one."),
                    ("It reads as certain", "Nothing in the wording marks it "
                                            "as a guess."),
                ],
            },
        },
        {
            "anchor": "s_cutoff",
            "label": "The cut-off date",
            "title": "Everything recent is missing",
            "gloss": ["Training data"],
            "visual": {
                "type": "nested",
                "layers": [
                    {"label": "Public text, up to a fixed date",
                     "sub": "Everything the model learned from. It stops there."},
                    {"label": "After that date",
                     "sub": "Circulars, rate changes, news, new products."},
                    {"label": "Your company, at any date",
                     "sub": "Never included, at all, ever."},
                ],
                "note": "Ask about a change from last month and it will not "
                        "say \"I do not know\". It will describe a change that "
                        "sounds about right.",
            },
        },
        {
            "label": "The cut-off date",
            "title": "The question to ask yourself",
            "visual": {
                "type": "tree",
                "question": "Could this have changed in the last year?",
                "yes": {
                    "path": "Yes", "tone": "bad", "label": "Do not ask AI",
                    "detail": "Duty rates, GST, prices, regulations, company "
                              "policy, who holds which role. These move, and "
                              "the tool will answer with the version it "
                              "learned.",
                },
                "no": {
                    "path": "No", "tone": "good", "label": "Reasonably safe",
                    "detail": "How a process generally works, what a term "
                              "means, how to phrase something. Stable "
                              "knowledge, and easy for you to sanity-check.",
                },
            },
        },
        {
            "anchor": "s_numbers",
            "label": "Numbers and arithmetic",
            "title": "Numbers are the weakest point",
            "lead": "A figure looks like evidence. That is exactly why an "
                    "invented one does the most damage.",
            "visual": {
                "type": "split",
                "left": {
                    "tag": "Never trust", "tone": "bad",
                    "title": "Numbers it produced",
                    "items": [
                        "Prices, rates, duties, penalties",
                        "Percentages quoted to a decimal place",
                        "Dates of rules, launches or changes",
                        "Any total it calculated from a long list",
                    ],
                },
                "right": {
                    "tag": "Safe to use", "tone": "good",
                    "title": "Numbers you supplied",
                    "items": [
                        "Figures you pasted in from a system",
                        "Dates you typed yourself",
                        "Totals you worked out in Excel",
                        "Anything you can point at a source for",
                    ],
                },
            },
        },
        {
            "label": "Numbers and arithmetic",
            "title": "Make it show its working",
            "visual": {
                "type": "prompt",
                "header": "Copy this checking prompt",
                "text": "For every number in your answer, tell me in brackets "
                        "whether it came from the text I gave you or from your "
                        "own general knowledge. If it came from your own "
                        "knowledge, say so plainly rather than presenting it "
                        "as a fact.",
                "caption": "This does not make it accurate. It makes the guess "
                           "visible.",
                "why": [
                    "Invented figures get labelled instead of blending in.",
                    "You see immediately which lines need a real source.",
                    "It costs one sentence and saves a wrong quotation.",
                ],
            },
        },
        {
            "anchor": "s_instead",
            "label": "What to use instead",
            "title": "The right tool per limit",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "A live rate or price — the official site or your supplier",
                    "A company figure — the ERP, the MIS, or the person who "
                    "owns it",
                    "A rule or a law — the published circular, or your "
                    "compliance contact",
                    "A judgement call — your manager, with the options laid "
                    "out",
                ],
            },
        },
        {
            "label": "What to use instead",
            "title": "Two minutes that save a quotation",
            "visual": {
                "type": "steps",
                "items": [
                    "Write down the one number the whole document depends on.",
                    "Ask yourself where that number actually lives.",
                    "Go and get it from there. It is usually two clicks.",
                    "Then hand the tool the number and ask for the wording.",
                ],
                "prompt": "Write a one-page quotation covering letter. The "
                          "rate is 62,400 per tonne, valid for 15 days, ex "
                          "works. Payment terms 30 days. Tone: confident and "
                          "brief. Under 180 words. Do not add any figures I "
                          "have not given you.",
                "caption": "Every number in it came from you. That is the "
                           "whole point.",
            },
        },
        {
            "anchor": "s_design",
            "label": "Designing around it",
            "title": "Ask so it cannot hurt you",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "Question that invites invention",
                "bad": [
                    "\"What is the notice period under UAE labour law?\"",
                    "It answers with a specific period, stated plainly and "
                    "without qualification.",
                    "You have no way to tell whether it is current, or ever "
                    "was.",
                ],
                "good_tag": "Question that cannot invent",
                "good": [
                    "\"Here is the clause from our contract. Explain it in "
                    "plain English.\"",
                    "It explains the words you actually pasted in.",
                    "Every sentence traces back to something on your screen.",
                ],
                "note": "Bring the fact to the tool. Never ask the tool to "
                        "bring the fact.",
            },
        },
        {
            "label": "Designing around it",
            "title": "Four ways to blunt the risk",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Paste the source text in, instead of asking about it.",
                    "Add \"do not add anything I have not given you\".",
                    "Ask for questions to check, not for answers to trust.",
                    "Say \"if you are unsure, list it as a gap\" and mean it.",
                ],
            },
        },
        {
            "label": "Designing around it",
            "title": "Where people get caught",
            "visual": {
                "type": "bandlist",
                "mark": "ban",
                "headline": "Every one of these produced a confident, wrong "
                            "answer for somebody last year.",
                "sub": "None of them looked risky at the moment of asking.",
                "cols": 2,
                "items": [
                    "\"What is the current GST rate on this category?\"",
                    "\"Summarise the new labour circular for me\"",
                    "\"What is the standard warranty in our industry?\"",
                    "\"Add up these forty line items and give me the total\"",
                ],
            },
        },
        {
            "label": "Designing around it",
            "title": "What it is still excellent at",
            "lead": "Limits are not a reason to avoid it. They are a map of "
                    "where to point it.",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "doc", "label": "Wording anything",
                     "sub": "Emails, summaries, explanations, refusals. The "
                            "facts come from you, the sentences from it."},
                    {"icon": "sheet", "label": "Restructuring",
                     "sub": "Long into short, list into table, dense into "
                            "plain. Nothing to invent, so nothing invented."},
                    {"icon": "list", "label": "Listing what to check",
                     "sub": "\"What should I verify before signing this?\" is "
                            "a question it answers genuinely well."},
                ],
            },
        },
        {
            "label": "Designing around it",
            "title": "Five mistakes people really make",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Believing a number because it is precise",
                     "62,417 reads as researched. It was generated the same "
                     "way as the sentence around it."),
                    ("Asking about \"the new\" anything",
                     "New means after the cut-off. It will still answer, and "
                     "the answer will be plausible fiction."),
                    ("Taking a legal answer at face value",
                     "It has no jurisdiction, no date and no liability. You "
                     "have all three."),
                    ("Letting it total a long list",
                     "It is producing likely text, not calculating. Long "
                     "arithmetic drifts and looks fine."),
                    ("Assuming a confident tone means a solid answer",
                     "Tone is constant by design. It is not a signal of "
                     "anything at all."),
                ],
            },
        },
        {
            "label": "Designing around it",
            "title": "The limitation rule",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "If the answer matters and you cannot check it, "
                            "you cannot use it.",
                "sub": "Not a rule about AI. A rule about anything you sign "
                       "your name to.",
                "cols": 3,
                "items": [
                    "Check it — then use it.",
                    "Cannot check it — go to the source.",
                    "No time to check — no time to send.",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Friday, 4:40 pm",
        "situation": "A quotation must go out before close. You need one "
                     "figure: the current import duty on a component. The "
                     "person who knows has already left for the day.",
        "choices": [
            {
                "text": "Ask the assistant for the current duty rate and use "
                        "it.",
                "tone": "bad",
                "headline": "It will answer. That is the problem.",
                "consequence": "You get a rate stated to one decimal place. It "
                               "reflects whatever was common in text before "
                               "the cut-off, not today's schedule. The "
                               "quotation goes out, is accepted, and the "
                               "difference comes out of your margin.",
                "rule": "A rate that can change is never a question for a "
                        "model.",
            },
            {
                "text": "Send the quotation with the duty line marked as \"to "
                        "be confirmed Monday\".",
                "tone": "good",
                "headline": "Honest, fast, and completely defensible",
                "consequence": "The customer gets everything else on Friday "
                               "and one clearly flagged line. Nobody is misled "
                               "and nothing has to be withdrawn. You confirm "
                               "the rate at 9 am Monday and send a one-line "
                               "update.",
                "rule": "A flagged gap costs nothing. A confident wrong number "
                        "costs the margin.",
            },
            {
                "text": "Use last quarter's duty rate from the old quotation.",
                "tone": "ok",
                "headline": "Better, but still a guess with a date on it",
                "consequence": "At least it came from a real document, so you "
                               "can show where it came from. But duty "
                               "schedules change, and \"it was right in March\" "
                               "is a weak position in June. Flag it as "
                               "indicative if you use it.",
                "rule": "An old real number still needs a date next to it.",
            },
        ],
    },

    # Title, channel and runtime were read back from YouTube
    # itself. See newvideos.json.
    "video": {
        "url": "https://www.youtube.com/watch?v=CB7NNsI27ks",
        "title": "Can AI Think? Debunking AI Limitations",
        "channel": "IBM Technology",
        "duration": "9:01",
        "heading": "Nine minutes on what it cannot do",
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
            "q": "Which question is it safe to ask?",
            "remember": "Stable and checkable. Not live and unverifiable.",
            "answers": [
                {"text": "\"What is today's exchange rate?\"", "ok": False,
                 "why": "It has no live data. It will produce a rate that "
                        "looks entirely normal and is simply whatever was "
                        "common in its training text. Use your bank's page."},
                {"text": "\"Explain what ex-works means for a buyer\"",
                 "ok": True,
                 "why": "A stable definition that has not changed in decades, "
                        "and one you can sanity-check in seconds. This is "
                        "solid ground for these tools."},
                {"text": "\"What did the circular last month change?\"",
                 "ok": False,
                 "why": "Last month is after its cut-off. It will not say so — "
                        "it will describe a change that sounds like the sort "
                        "of change such circulars make."},
                {"text": "\"How much stock do we hold of this part?\"",
                 "ok": False,
                 "why": "It has no connection to your systems and never will "
                        "unless someone builds one. Any figure it gives is "
                        "invented in full."},
            ],
        },
        {
            "q": "Why is a precise number dangerous?",
            "remember": "Precision is a style, not evidence.",
            "answers": [
                {"text": "Because precise numbers are usually rounded wrong",
                 "ok": False,
                 "why": "Rounding is not the issue. The issue is that the "
                        "number may have no relationship to reality at all, "
                        "however many decimal places it carries."},
                {"text": "Because precision makes an invention look researched",
                 "ok": True,
                 "why": "Exactly. \"About 60,000\" invites a check. \"62,417\" "
                        "reads as though somebody looked it up. Both were "
                        "produced the same way, by predicting likely text."},
                {"text": "Because the tool rounds to look confident",
                 "ok": False,
                 "why": "It is not choosing a presentation style to persuade "
                        "you. It produces the digits that fit the pattern, and "
                        "detailed figures are common in that kind of sentence."},
                {"text": "Because precise numbers are harder to check",
                 "ok": False,
                 "why": "They are no harder to check than any other. The "
                        "danger is that they do not feel like they need "
                        "checking, so nobody checks them."},
            ],
        },
        {
            "q": "What does the cut-off date mean?",
            "remember": "Recent means invented, not missing.",
            "answers": [
                {"text": "The tool stops working after that date", "ok": False,
                 "why": "It works perfectly well. What stops is what it "
                        "learned from. Everything after that date is outside "
                        "what it has ever seen."},
                {"text": "Anything newer will be answered from patterns, not "
                         "knowledge", "ok": True,
                 "why": "Right, and it will not warn you. You get a fluent "
                        "description of a circular, rate or product it has "
                        "never encountered, in the same tone as everything "
                        "else."},
                {"text": "It will refuse questions about recent events",
                 "ok": False,
                 "why": "Sometimes it will, and that is the good case. Very "
                        "often it answers anyway, which is the case that "
                        "reaches a customer."},
                {"text": "It only affects news, not business facts", "ok": False,
                 "why": "It affects everything that moves: duty rates, tax "
                        "rules, product ranges, regulations, and who holds "
                        "which role at a supplier."},
            ],
        },
        {
            "q": "How do you make a guess visible?",
            "remember": "Ask it to label what it did not get from you.",
            "answers": [
                {"text": "Ask it to be accurate", "ok": False,
                 "why": "There is nothing for it to act on. It cannot inspect "
                        "its own output for truth, so the instruction changes "
                        "nothing except the tone."},
                {"text": "Ask it to mark which numbers came from your text",
                 "ok": True,
                 "why": "This turns silent invention into a labelled line. It "
                        "does not make anything accurate, but you can see "
                        "instantly which figures need a real source."},
                {"text": "Ask the same question twice and compare", "ok": False,
                 "why": "Two generations can agree and both be wrong, because "
                        "they came from the same patterns. Agreement here is "
                        "not corroboration."},
                {"text": "Ask it how confident it is", "ok": False,
                 "why": "It will produce a confidence statement the same way "
                        "it produces everything else. A generated \"90 per "
                        "cent sure\" is not a measurement."},
            ],
        },
        {
            "q": "The deadline is in ten minutes.",
            "stem": "You are missing one figure and the person who knows it "
                    "has gone home for the weekend.",
            "remember": "A flagged gap beats a confident invention.",
            "answers": [
                {"text": "Ask the AI and use whatever it gives you", "ok": False,
                 "why": "The deadline does not change what the tool can know. "
                        "You would be putting an unverifiable number into a "
                        "document that binds the company, to save ten minutes."},
                {"text": "Send it with that line clearly marked as to be "
                         "confirmed", "ok": True,
                 "why": "Everything else lands on time, nobody is misled, and "
                        "nothing has to be withdrawn on Monday. A visible gap "
                        "is a normal part of business; a wrong number is not."},
                {"text": "Hold the whole document until Monday", "ok": False,
                 "why": "Safe but unnecessary. The other nine-tenths of the "
                        "document is ready and useful, and delaying all of it "
                        "for one line helps nobody."},
                {"text": "Estimate it yourself and note it as approximate",
                 "ok": False,
                 "why": "Better than an AI guess because you can explain your "
                        "reasoning, but in a binding document an estimate "
                        "still needs to be labelled and agreed, not slipped "
                        "in."},
            ],
        },
    ],

    "recap": {
        "title": "AI Limitations on one screen",
        "points": [
            ("It cannot look anything up",
             "No pages, no systems, no live data, unless the tool visibly "
             "shows you otherwise."),
            ("Recent means invented",
             "Anything after the cut-off gets a plausible answer rather than "
             "an honest blank."),
            ("Numbers are the weak point",
             "A precise figure reads as researched. It was produced like every "
             "other word."),
            ("Confidence is not a signal",
             "The tone never changes, whether the answer is solid or entirely "
             "made up."),
            ("Bring the fact to the tool",
             "Paste the clause, the figure, the circular. Then ask for "
             "wording."),
            ("If you cannot check it, do not use it",
             "That is a rule about anything you sign, not a rule about AI."),
        ],
        "oneliner": "It never says \"I do not know\". That single missing "
                    "behaviour is the source of almost every AI problem at "
                    "work.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("eye", "The source-labelling prompt",
             "Mark every number as mine or yours, plainly."),
            ("doc", "The quotation-letter prompt",
             "Your figures, your terms, and no invented numbers."),
            ("check", "The could-it-have-changed test",
             "If yes, it is not a question for a model."),
        ],
        "links": [
            ("Microsoft Copilot", "https://copilot.microsoft.com"),
            ("ChatGPT", "https://chatgpt.com"),
            ("Google Gemini", "https://gemini.google.com"),
        ],
        "next": "Next module: AI-05, Hallucinations & Fact-Checking. It gives "
                "you a four-step routine for catching a confident wrong answer "
                "before it reaches a customer.",
    },

    "glossary": [
        ("Cut-off date", "The point where a model's training text stops. "
                         "Nothing after it was ever seen."),
        ("Training data", "The public text a model learned from, up to that "
                          "cut-off date."),
        ("Hallucination", "A confident, invented answer. Usually a name, a "
                          "number, a date or a policy."),
        ("Grounding", "Giving the tool the actual source text so its answer "
                      "has something real to stand on."),
        ("Prompt", "Everything you type in: the request plus the facts you "
                   "supply."),
        ("Output", "What comes back. Your draft, which you are responsible for "
                   "checking."),
    ],
}
