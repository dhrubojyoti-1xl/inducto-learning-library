# -*- coding: utf-8 -*-
"""PS-03 — English & Grammar for the Workplace. Content only."""

DECK = {
    "module_code": "PS-03",
    "area": "04-professional-skills",
    "filename": "04-03-english-and-grammar.pptx",
    "title": "English for the Workplace",
    "subtitle": "The handful of patterns that cause almost every "
                "misunderstanding at work — and how to sidestep them.",
    "duration_min": 17,
    "audience": "New joiners + staff",
    "motif": "flow",

    "why": {
        "title": "Sneha's update is read two ways",
        "icon": "chat",
        "scenario": "Sneha supervises a line near Pune. She writes: \"The "
                    "machine is running since morning.\" Her manager reads it "
                    "as \"it has been running all morning\". The night "
                    "supervisor reads it as \"it started this morning after "
                    "being down\".",
        "cost": "Two people planning around two different situations.",
        "fix": "Six patterns, and a habit of writing one idea per sentence.",
    },

    "outcomes": [
        ("chat", "Write one idea per sentence, without sounding blunt"),
        ("clock", "Use the tense that removes ambiguity about time"),
        ("eye", "Spot the six patterns that cause most confusion at work"),
        ("check", "Proofread your own writing in under a minute"),
        ("person", "Sound polite without adding words that hide the meaning"),
    ],

    "sections": [
        ("One idea per sentence", "The single biggest win", "s_one"),
        ("Tense and time", "Where the confusion lives", "s_tense"),
        ("Six patterns", "The ones that cost time", "s_six"),
        ("Polite without padding", "Short is not rude", "s_polite"),
        ("Do this now", "Proofread something real", "s_do"),
        ("Choose what you'd do", "A shift-handover decision", "scenario"),
        ("Watch this", "A 10-minute outside exercise", "video"),
    ],

    "slides": [
        {
            "anchor": "s_one",
            "label": "One idea per sentence",
            "title": "One idea per sentence",
            "lead": "Long sentences are where meaning gets lost. This is true "
                    "in every language, and it is the fastest thing to fix.",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "One long sentence",
                "bad": [
                    "\"As the material which was ordered last week has not yet "
                    "arrived and the line is scheduled for Thursday we may "
                    "need to reschedule unless it comes tomorrow.\"",
                    "Thirty-four words, four ideas, one breath.",
                    "The reader has to work out what depends on what.",
                ],
                "good_tag": "Four short ones",
                "good": [
                    "\"The material ordered last week has not arrived.\"",
                    "\"The line is scheduled for Thursday.\"",
                    "\"If it does not come tomorrow, we will reschedule.\"",
                ],
                "note": "Nobody has ever complained that a work email was too "
                        "easy to read.",
            },
        },
        {
            "label": "One idea per sentence",
            "title": "The full-stop test",
            "visual": {
                "type": "flow",
                "steps": [
                    ("Read your sentence aloud", "In your head is enough."),
                    ("Did you need a breath?", "If yes, it is too long."),
                    ("Find the and, or which", "That is usually where it "
                                               "splits."),
                    ("Put a full stop there", "Two clear sentences beat one "
                                              "clever one."),
                ],
            },
        },
        {
            "anchor": "s_tense",
            "label": "Tense and time",
            "title": "Where the confusion lives",
            "visual": {
                "type": "split",
                "left": {
                    "tag": "Ambiguous", "tone": "bad",
                    "title": "Two readings possible",
                    "items": [
                        "\"The machine is running since morning\"",
                        "\"I am working on this from yesterday\"",
                        "\"We are waiting the material\"",
                        "\"He is having the file\"",
                    ],
                },
                "right": {
                    "tag": "Clear", "tone": "good",
                    "title": "One reading only",
                    "items": [
                        "\"The machine has been running since 6am\"",
                        "\"I started this yesterday and I am still on it\"",
                        "\"We are waiting for the material\"",
                        "\"He has the file\"",
                    ],
                },
            },
        },
        {
            "label": "Tense and time",
            "title": "Add the time, remove the doubt",
            "lead": "When in doubt about tense, add the actual time. A "
                    "timestamp fixes almost any ambiguity.",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "\"Since 6am\" instead of \"since morning\"",
                    "\"By Thursday 5pm\" instead of \"by Thursday\"",
                    "\"Started on the 8th, still open\" instead of \"from the "
                    "8th\"",
                    "\"On 3 April\" instead of \"03/04\", which reads two "
                    "ways",
                ],
            },
        },
        {
            "anchor": "s_six",
            "label": "Six patterns",
            "title": "Six patterns that cost time",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("\"Revert\" for \"reply\"",
                     "Outside South Asia, revert means go back to a previous "
                     "state. It confuses customers."),
                    ("\"Prepone\"",
                     "Not used outside South Asia at all. Say \"move earlier\" "
                     "or \"bring forward\"."),
                    ("\"Discuss about\" and \"reply back\"",
                     "The extra word is redundant. \"Discuss\" and \"reply\" "
                     "carry it already."),
                    ("\"Same\" as a noun",
                     "\"Please send the same\" leaves the reader guessing. "
                     "Name the thing."),
                    ("Missing \"the\" and \"a\"",
                     "\"Send report to client\" reads as a telegram. Two small "
                     "words soften it a great deal."),
                ],
            },
        },
        {
            "label": "Six patterns",
            "title": "The date format problem",
            "visual": {
                "type": "bandlist",
                "mark": "ban",
                "headline": "03/04 means 3 April here and 4 March to plenty of "
                            "our customers.",
                "sub": "We work across India, the UAE and clients elsewhere. "
                       "Write the month as a word.",
                "cols": 3,
                "items": [
                    "Write \"3 April 2026\".",
                    "Never 03/04/26.",
                    "Add the day name for deadlines.",
                ],
            },
        },
        {
            "anchor": "s_polite",
            "label": "Polite without padding",
            "title": "Short is not rude",
            "lead": "Politeness comes from what you offer, not from how many "
                    "words you use to ask.",
            "visual": {
                "type": "split",
                "left": {
                    "tag": "Padded", "tone": "neutral", "mark": "chat",
                    "title": "Longer, and less clear",
                    "items": [
                        "\"It would be greatly appreciated if you could "
                        "kindly...\"",
                        "\"I was wondering whether it might be possible...\"",
                        "\"Please do the needful at the earliest\"",
                        "The request is now hard to find",
                    ],
                },
                "right": {
                    "tag": "Direct and warm", "tone": "good",
                    "title": "Shorter, and friendlier",
                    "items": [
                        "\"Could you send the revised quote by Thursday?\"",
                        "\"Would Friday work instead?\"",
                        "\"Thanks — this one is holding up the install.\"",
                        "The request and the reason are both visible",
                    ],
                },
            },
        },
        {
            "label": "Polite without padding",
            "title": "Three phrases that carry warmth",
            "visual": {
                "type": "prompt",
                "header": "Copy these phrases",
                "text": "\"Thanks for turning this around quickly.\"  /  "
                        "\"Happy to talk it through if that is easier.\"  /  "
                        "\"Let me know if the date is a problem and we will "
                        "work around it.\"  /  \"No rush on this one — end of "
                        "next week is fine.\"",
                "caption": "One of these at the end does the work of a "
                           "paragraph at the start.",
                "why": [
                    "Each offers something rather than performing politeness.",
                    "They work in every register, from supplier to director.",
                    "They are short, so they do not bury the request.",
                ],
            },
        },
        {
            "anchor": "s_do",
            "label": "Do this now",
            "title": "Do this now: proofread one",
            "visual": {
                "type": "steps",
                "items": [
                    "Take an email you are about to send.",
                    "Read it aloud, quietly. Mark anywhere you needed a "
                    "breath.",
                    "Split those sentences at the \"and\" or the \"which\".",
                    "Replace every vague time with a real one.",
                ],
                "prompt": "Rewrite the text below into short sentences, one "
                          "idea each. Keep my meaning and my facts exactly. "
                          "Replace vague times with the specific ones I have "
                          "given. Do not make it more formal and do not add "
                          "anything. Plain business English.",
                "caption": "\"Do not make it more formal\" is the important "
                           "instruction.",
            },
        },
        {
            "label": "Do this now",
            "title": "The one-minute proofread",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Any sentence over about twenty words — split it.",
                    "Any date written as numbers — spell the month.",
                    "Any \"same\", \"revert\" or \"needful\" — name the thing.",
                    "Any vague time — replace with a real one.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Using tools without losing yourself",
            "visual": {
                "type": "tree",
                "question": "Does the corrected version still sound like me?",
                "yes": {
                    "path": "Yes", "tone": "good", "label": "Send it",
                    "detail": "Grammar tools and AI are genuinely useful for "
                              "catching slips. If the meaning and the voice "
                              "are yours, the help was worth having.",
                },
                "no": {
                    "path": "No", "tone": "bad", "label": "Pull it back",
                    "detail": "If it now reads like somebody else, change "
                              "three words back. A message that does not sound "
                              "like you is harder to have a conversation "
                              "about.",
                },
            },
        },
        {
            "label": "Do this now",
            "title": "Confidence, not perfection",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "check", "label": "Clear beats correct",
                     "sub": "A short sentence with one small error is far "
                            "better than a perfect one nobody can parse."},
                    {"icon": "person", "label": "Nobody is counting",
                     "sub": "Colleagues remember whether you were clear and "
                            "on time, not whether an article was missing."},
                    {"icon": "cycle", "label": "It improves by writing",
                     "sub": "Six months of short sentences does more than any "
                            "grammar course."},
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "The English rule",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "One idea per sentence, a real time instead of a "
                            "vague one, and the month spelled out.",
                "sub": "Three habits that remove most of the "
                       "misunderstandings work English causes.",
                "cols": 3,
                "items": [
                    "One idea, one full stop.",
                    "Real times, not vague ones.",
                    "Months as words.",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Shift handover, 6:00 am",
        "situation": "You are writing the handover note for the incoming "
                     "supervisor. The main machine stopped, was repaired, and "
                     "is now running. You have two minutes.",
        "choices": [
            {
                "text": "Write \"Machine is running since morning, no issue "
                        "now.\"",
                "tone": "bad",
                "headline": "Two supervisors, two different pictures",
                "consequence": "One reads it as running all night without "
                               "trouble. The other reads it as started this "
                               "morning after a stoppage. The second "
                               "supervisor does not check the repair, because "
                               "he did not know there had been one.",
                "rule": "\"Since morning\" has two meanings. A clock time has "
                        "one.",
            },
            {
                "text": "Write three short sentences with actual times in "
                        "them.",
                "tone": "good",
                "headline": "Twenty seconds longer, and no ambiguity",
                "consequence": "\"The machine stopped at 2:10am. It was "
                               "repaired and restarted at 4:40am. It has run "
                               "normally since then.\" The incoming supervisor "
                               "knows exactly what happened, what to watch, "
                               "and what to tell maintenance.",
                "rule": "Three short sentences with times beat one sentence "
                        "with none.",
            },
            {
                "text": "Write a long, careful paragraph covering everything.",
                "tone": "ok",
                "headline": "Complete, and read at six in the morning",
                "consequence": "All the information is there, in one "
                               "forty-word sentence at the end of a night "
                               "shift. The incoming supervisor skims it and "
                               "takes away the first half. Completeness is not "
                               "the same as being understood.",
                "rule": "Handovers are read tired. Write them for that.",
            },
        ],
    },

    # Title, channel and runtime were read back from YouTube
    # itself. See newvideos.json.
    "video": {
        "url": "https://www.youtube.com/watch?v=QNZ8uty99Fc",
        "title": "Can You Correct the Mistakes in These Business Emails?",
        "channel": "Derek Callan - English for Professionals",
        "duration": "9:40",
        "heading": "Ten minutes, spot the mistakes",
        "note": "An outside English lesson, not company material. Try to "
                "spot each error before he explains it.",
        "how": [
            "Optional. The six patterns above are the working set.",
            "Best watched as a test rather than a lecture.",
            "It opens in your browser. Turn the sound on.",
        ],
    },

    "quiz": [
        {
            "q": "What is the fastest improvement?",
            "remember": "One idea per sentence.",
            "answers": [
                {"text": "Using more formal vocabulary", "ok": False,
                 "why": "Formality usually makes sentences longer and harder, "
                        "which is the opposite of what helps. Plain words are "
                        "clearer for everyone."},
                {"text": "One idea per sentence", "ok": True,
                 "why": "It costs nothing to apply, works in any language, and "
                        "removes most ambiguity immediately. Nobody has ever "
                        "complained that a work email was too easy to read."},
                {"text": "Perfect punctuation", "ok": False,
                 "why": "Worth having, and it barely affects whether you are "
                        "understood. A clear short sentence with a missing "
                        "comma communicates fine."},
                {"text": "Longer, more detailed explanations", "ok": False,
                 "why": "More words usually means more chances to be "
                        "misunderstood, and a reader who stops earlier."},
            ],
        },
        {
            "q": "Why is \"since morning\" a problem?",
            "remember": "It has two readings. A clock time has one.",
            "answers": [
                {"text": "It is too informal for work", "ok": False,
                 "why": "Register is not the issue. The problem is that two "
                        "readers can take two different meanings from it and "
                        "both act confidently."},
                {"text": "It can mean \"all morning\" or \"starting this "
                         "morning\"", "ok": True,
                 "why": "Both readings are natural. On a shift handover that "
                        "difference decides whether the next supervisor checks "
                        "a repair or not."},
                {"text": "It is grammatically incorrect", "ok": False,
                 "why": "The grammar is not the practical problem. Even "
                        "corrected to \"has been running since morning\", the "
                        "vagueness about which morning event remains."},
                {"text": "Customers dislike it", "ok": False,
                 "why": "This is mostly an internal clarity issue. The cost is "
                        "operational confusion, not customer perception."},
            ],
        },
        {
            "q": "How should you write a date?",
            "remember": "Spell the month.",
            "answers": [
                {"text": "03/04/26 — it is shortest", "ok": False,
                 "why": "It means 3 April to us and 4 March to plenty of our "
                        "customers and colleagues. On a deadline that "
                        "difference is a month."},
                {"text": "3 April 2026", "ok": True,
                 "why": "One reading only, anywhere in the world. For "
                        "deadlines, adding the day name — \"Friday 3 April\" — "
                        "catches errors as well."},
                {"text": "The 3rd", "ok": False,
                 "why": "Fine within a conversation about a known month, and "
                        "ambiguous the moment the email is forwarded or read "
                        "two weeks later."},
                {"text": "Next Friday", "ok": False,
                 "why": "One of the genuinely ambiguous phrases in English. On "
                        "a Monday, half of people mean this week's Friday and "
                        "half mean the following one."},
            ],
        },
        {
            "q": "Which is politer, in practice?",
            "remember": "Warmth comes from offering, not padding.",
            "answers": [
                {"text": "\"It would be greatly appreciated if you could "
                         "kindly send the quote\"", "ok": False,
                 "why": "Longer, and the request is now harder to find. "
                        "Padding often reads as distance rather than warmth, "
                        "particularly across cultures."},
                {"text": "\"Could you send the quote by Thursday? Thanks — "
                         "it is holding up the install.\"", "ok": True,
                 "why": "Clear request, real deadline, and a reason that shows "
                        "you are not asking arbitrarily. The warmth is in the "
                        "explanation, which is where people feel it."},
                {"text": "\"Send quote Thursday.\"", "ok": False,
                 "why": "Clear and genuinely abrupt. Two small words and a "
                        "reason cost nothing and change how it lands."},
                {"text": "\"Please do the needful regarding the quote.\"",
                 "ok": False,
                 "why": "Polite in form and unclear in substance. The reader "
                        "does not know what is wanted or when."},
            ],
        },
        {
            "q": "A tool rewrote your email. What now?",
            "remember": "If it no longer sounds like you, pull it back.",
            "answers": [
                {"text": "Send it — the grammar is now perfect", "ok": False,
                 "why": "Perfect grammar in somebody else's voice makes the "
                        "next conversation harder. People notice when a "
                        "colleague suddenly writes differently."},
                {"text": "Check it still sounds like you, and change words "
                         "back if not", "ok": True,
                 "why": "Use the tool for slips and clarity, then reclaim the "
                        "voice. Three words is usually enough to make it yours "
                        "again."},
                {"text": "Never use tools for your writing", "ok": False,
                 "why": "They are genuinely useful for catching errors, "
                        "especially when English is not your first language. "
                        "The skill is keeping control, not abstaining."},
                {"text": "Ask it to make the email more formal too",
                 "ok": False,
                 "why": "Formality usually lengthens sentences and buries the "
                        "request. It is the opposite direction from clarity."},
            ],
        },
    ],

    "recap": {
        "title": "Workplace English on one screen",
        "points": [
            ("One idea per sentence",
             "The fastest improvement available, and it costs nothing."),
            ("Read it aloud",
             "If you needed a breath, split it at the \"and\" or the "
             "\"which\"."),
            ("Real times, not vague ones",
             "\"Since 6am\" removes an ambiguity that \"since morning\" "
             "creates."),
            ("Spell the month",
             "03/04 means two different things across the offices we work "
             "in."),
            ("Short is not rude",
             "Warmth comes from offering something, not from adding words."),
            ("Clear beats correct",
             "A short sentence with a small slip beats a perfect one nobody "
             "can parse."),
        ],
        "oneliner": "One idea per sentence, a real time instead of a vague "
                    "one, and the month spelled out.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("chat", "The short-sentences rewrite",
             "One idea each, same meaning, no added formality."),
            ("list", "The one-minute proofread",
             "Long sentences, numeric dates, vague times, \"same\"."),
            ("person", "Three warm closes",
             "Offer something instead of padding the opening."),
        ],
        "links": [
            ("Microsoft Copilot", "https://copilot.microsoft.com"),
            ("ChatGPT", "https://chatgpt.com"),
            ("Google Gemini", "https://gemini.google.com"),
        ],
        "next": "Next module: PS-04, Time Management. Protecting the hours "
                "where your real work actually gets done.",
    },

    "glossary": [
        ("Ambiguity", "A sentence with two possible meanings. The main cost of "
                      "unclear writing at work."),
        ("Tense", "How a verb shows time. Adding a clock time removes most "
                  "tense problems entirely."),
        ("Padding", "Extra words added for politeness that make the request "
                    "harder to find."),
        ("Register", "How formal a message is. Plain and warm travels better "
                     "than heavy formality."),
        ("Handover", "A note written for the person taking over. Read tired, "
                     "so written short."),
        ("Article", "\"The\" and \"a\". Small words that make instructions "
                    "read less abrupt."),
    ],
}
