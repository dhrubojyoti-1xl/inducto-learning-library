# -*- coding: utf-8 -*-
"""PS-02 — Professional Email Writing. Content only."""

DECK = {
    "module_code": "PS-02",
    "area": "04-professional-skills",
    "filename": "04-02-professional-email-writing.pptx",
    "title": "Professional Email Writing",
    "subtitle": "The mechanics — subject lines, openings, tone, and knowing "
                "when not to send at all.",
    "duration_min": 17,
    "audience": "New joiners + staff",
    "motif": "layers",

    "why": {
        "title": "Pooja's email starts a fight",
        "icon": "mail",
        "scenario": "Pooja handles customer service in Kochi. She writes "
                    "\"As per my previous email, kindly do the needful "
                    "urgently.\" She means it neutrally. The customer reads it "
                    "as sarcasm and escalates to her director.",
        "cost": "A routine query turned into a complaint about her.",
        "fix": "Four phrases to retire, and one structure that never reads "
               "badly.",
    },

    "outcomes": [
        ("chat", "Write an opening line that is not throat-clearing"),
        ("ban", "Retire four phrases that read worse than you intend"),
        ("person", "Keep tone neutral when you are annoyed"),
        ("clock", "Know the three times you should not send at all"),
        ("check", "Run a ten-second check before every external email"),
    ],

    "sections": [
        ("The opening line", "Delete the first sentence", "s_open"),
        ("Phrases to retire", "They read worse than you mean", "s_phrases"),
        ("Tone when annoyed", "Neutral is a skill", "s_tone"),
        ("When not to send", "Three situations", "s_dont"),
        ("Do this now", "Fix one real email", "s_do"),
        ("Choose what you'd do", "A Monday morning decision", "scenario"),
        ("Watch this", "A 7-minute outside guide", "video"),
    ],

    "slides": [
        {
            "anchor": "s_open",
            "label": "The opening line",
            "title": "Delete the first sentence",
            "lead": "The first sentence of most work emails carries no "
                    "information. Try deleting it and see if anything is lost.",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "Throat-clearing",
                "bad": [
                    "\"I hope this email finds you well.\"",
                    "\"I am writing to you regarding the below matter.\"",
                    "\"Further to our earlier correspondence on this "
                    "subject...\"",
                ],
                "good_tag": "Straight in",
                "good": [
                    "\"Your order 4471 will now arrive on 15 March.\"",
                    "\"I need your approval on the revised quote by Thursday.\"",
                    "\"Two cartons were damaged. We are replacing them this "
                    "week.\"",
                ],
                "note": "Warmth comes from what you say and how you close, not "
                        "from a sentence everybody skips.",
            },
        },
        {
            "label": "The opening line",
            "title": "The four-part email",
            "visual": {
                "type": "flow",
                "steps": [
                    ("The point", "What has happened, or what you need."),
                    ("The detail", "Dates, numbers, references. Short."),
                    ("The ask", "One thing, with a date on it."),
                    ("The close", "Where the warmth goes, in one line."),
                ],
            },
        },
        {
            "anchor": "s_phrases",
            "label": "Phrases to retire",
            "title": "Four phrases to retire",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("\"As per my previous email\"",
                     "Reads as an accusation, whatever you intended. Say "
                     "\"following up on\" instead."),
                    ("\"Kindly do the needful\"",
                     "Says nothing about what you actually want done. Name the "
                     "action and the date."),
                    ("\"Please revert\"",
                     "In most of the world this means go back to a previous "
                     "state. Say \"please reply\"."),
                    ("\"Urgent\" in every subject line",
                     "It stops meaning anything after the second use, and "
                     "hides the ones that are."),
                ],
            },
        },
        {
            "label": "Phrases to retire",
            "title": "Say what you want instead",
            "visual": {
                "type": "split",
                "left": {
                    "tag": "Vague", "tone": "bad",
                    "title": "Reader has to guess",
                    "items": [
                        "\"Kindly do the needful\"",
                        "\"Please look into this\"",
                        "\"Awaiting your revert\"",
                        "\"Treat as most urgent\"",
                    ],
                },
                "right": {
                    "tag": "Specific", "tone": "good",
                    "title": "Reader knows exactly",
                    "items": [
                        "\"Please approve the revised quote\"",
                        "\"Please confirm the new date\"",
                        "\"A yes or no by Thursday would help\"",
                        "\"We need this before the 3pm dispatch\"",
                    ],
                },
            },
        },
        {
            "anchor": "s_tone",
            "label": "Tone when annoyed",
            "title": "Neutral is a skill",
            "lead": "When you are annoyed, the email you write will read "
                    "angrier than you meant. Every time.",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Remove every \"you\" that assigns blame. Use \"the "
                    "order\", not \"your team\".",
                    "Delete adverbs. \"Repeatedly\", \"clearly\", \"again\" "
                    "all sharpen the tone.",
                    "State facts with dates. Facts do not need heat to land.",
                    "Write it, then send it thirty minutes later.",
                ],
            },
        },
        {
            "label": "Tone when annoyed",
            "title": "The neutral chaser",
            "visual": {
                "type": "prompt",
                "header": "Copy this wording",
                "text": "Following up on the revised drawings. These were due "
                        "on the 8th and we have not received them yet. The "
                        "install team is booked for the 19th, so we would need "
                        "them by the 14th at the latest. Could you confirm a "
                        "date today?",
                "caption": "Two missed deadlines, and not one word of heat in "
                           "it.",
                "why": [
                    "Dates do the work that adjectives would have done badly.",
                    "No \"you\" appears, so nobody is being accused.",
                    "It ends with a small, easy request rather than a "
                    "complaint.",
                ],
            },
        },
        {
            "anchor": "s_dont",
            "label": "When not to send",
            "title": "Three times not to send",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "warn", "label": "When you are angry",
                     "sub": "Write it, save it, reread it after lunch. You "
                            "will change three things, every time."},
                    {"icon": "person", "label": "When it is about a person",
                     "sub": "Performance, conduct, capability. Those "
                            "conversations happen face to face."},
                    {"icon": "chat", "label": "When it needs a discussion",
                     "sub": "If it will take four emails, it is a five-minute "
                            "call you have not made yet."},
                ],
            },
        },
        {
            "label": "When not to send",
            "title": "The reply-all question",
            "visual": {
                "type": "tree",
                "question": "Does everyone on this thread need my reply?",
                "yes": {
                    "path": "Yes", "tone": "good", "label": "Reply all",
                    "detail": "A decision the group is waiting on, or "
                              "information that stops others duplicating work. "
                              "Rare, and genuinely useful when it applies.",
                },
                "no": {
                    "path": "No", "tone": "bad", "label": "Reply to sender",
                    "detail": "\"Thanks\", \"Noted\", or anything only the "
                              "sender needs. Twelve people receiving "
                              "\"Thanks\" is twelve interruptions for "
                              "nothing.",
                },
            },
        },
        {
            "anchor": "s_do",
            "label": "Do this now",
            "title": "Do this now: fix one email",
            "visual": {
                "type": "steps",
                "items": [
                    "Open a sent email you were slightly unhappy with.",
                    "Delete the first sentence and see whether anything is "
                    "lost.",
                    "Remove every \"you\" that assigns blame, and every "
                    "adverb.",
                    "Check the subject line names the decision and the date.",
                ],
                "prompt": "Rewrite this email to be neutral in tone. Remove "
                          "any wording that assigns blame, delete adverbs, and "
                          "state the facts with dates instead. Keep the same "
                          "meaning and the same request. Under 100 words. Do "
                          "not add an apology.",
                "caption": "Use this on anything you wrote while irritated.",
            },
        },
        {
            "label": "Do this now",
            "title": "The ten-second check",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Is the recipient right, and is anyone in CC unnecessary?",
                    "Does the subject line name the decision and the date?",
                    "Is there exactly one ask, with a date on it?",
                    "Would I be comfortable if this were forwarded to their "
                    "director?",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Five mistakes people really make",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Writing while annoyed and sending immediately",
                     "It always reads sharper than you meant, and it is on the "
                     "record forever."),
                    ("Reply-all with \"Thanks\"",
                     "Twelve interruptions for a message eleven of them did "
                     "not need."),
                    ("Marking everything urgent",
                     "The flag stops meaning anything, including on the one "
                     "that genuinely is."),
                    ("Burying the ask in paragraph three",
                     "The reader stopped at paragraph two and meant to come "
                     "back."),
                    ("Copying somebody's manager to apply pressure",
                     "It is read as an escalation, and it usually ends "
                     "cooperation immediately."),
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "The close does the warmth",
            "visual": {
                "type": "prompt",
                "header": "Copy these closes",
                "text": "\"Thanks — shout if anything is unclear.\"  /  \"Happy "
                        "to talk it through if that is easier.\"  /  \"Thanks "
                        "for turning this around quickly.\"  /  \"Let me know "
                        "if the date is a problem and we will work around it.\"",
                "caption": "One line at the end does more than three at the "
                           "start.",
                "why": [
                    "It arrives after the reader has the information.",
                    "It offers something, rather than performing politeness.",
                    "It works even when the news in the middle was bad.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Writing across cultures",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "Our email goes between India, the UAE and "
                            "clients elsewhere. Plain and specific travels "
                            "best.",
                "sub": "Idiom, sarcasm and heavy formality all read "
                       "differently in different offices.",
                "cols": 3,
                "items": [
                    "Short sentences, one idea each.",
                    "Dates written in full, never 03/04.",
                    "No idiom, no jokes about delays.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "The email rule",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "Say the thing, give the date, make one ask, and "
                            "put the warmth at the end.",
                "sub": "That order works for good news, bad news and "
                       "everything routine in between.",
                "cols": 3,
                "items": [
                    "Point first.",
                    "One ask, one date.",
                    "Warmth in the close.",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Monday, 9:05 am",
        "situation": "A supplier has missed a drawing deadline for the second "
                     "time. Your install team is booked for the 19th. You are "
                     "annoyed and you need the drawings by the 14th.",
        "choices": [
            {
                "text": "Write it now while it is fresh, and copy their "
                        "manager.",
                "tone": "bad",
                "headline": "Two mistakes in one message",
                "consequence": "Written while annoyed, it carries three "
                               "adverbs and two accusations you would not have "
                               "used after lunch. Copying their manager reads "
                               "as an escalation on a second missed deadline, "
                               "and cooperation stops immediately.",
                "rule": "Never send angry, and never escalate before you have "
                        "asked once, clearly.",
            },
            {
                "text": "Send a neutral, dated chaser to your contact only.",
                "tone": "good",
                "headline": "Two missed deadlines, no heat at all",
                "consequence": "\"These were due on the 8th. Install is booked "
                               "for the 19th, so we would need them by the "
                               "14th. Could you confirm a date today?\" You "
                               "get a date by eleven, and the relationship is "
                               "intact for the next project.",
                "rule": "Dates do the work that anger would have done badly.",
            },
            {
                "text": "Ring them, then confirm the agreed date in writing.",
                "tone": "good",
                "headline": "Often the fastest route of all",
                "consequence": "Two minutes on the phone finds out that the "
                               "drawings are waiting on an approval at their "
                               "end. You agree the 13th, and your one-line "
                               "confirmation email creates the record. Nothing "
                               "escalated and nothing was written in anger.",
                "rule": "After a second miss, a call beats a better email.",
            },
        ],
    },

    "video": {
        "url": "https://www.youtube.com/watch?v=1XctnF7C74s",
        "title": "8 Email Etiquette Tips - How to Write Better Emails at Work",
        "channel": "Harvard Business Review",
        "duration": "7:00",
        "heading": "Seven minutes on the basics",
        "note": "An outside video, not company material. Where it differs from "
                "this module, follow this module.",
        "how": [
            "Optional. The four-part structure above is the core.",
            "Useful if you like hearing the reasoning behind the rules.",
            "It opens in your browser. Turn the sound on.",
        ],
    },

    "quiz": [
        {
            "q": "What should the first line contain?",
            "remember": "The point, not a greeting about wellbeing.",
            "answers": [
                {"text": "A polite enquiry about the reader", "ok": False,
                 "why": "Everybody skips it, and it delays the information by "
                        "a line. Warmth belongs in the close, where it is "
                        "actually read."},
                {"text": "The point — what happened or what you need",
                 "ok": True,
                 "why": "The reader knows immediately whether the message "
                        "concerns them. It also makes the email findable and "
                        "forwardable later."},
                {"text": "A reference to your previous email", "ok": False,
                 "why": "\"As per my previous email\" reads as an accusation "
                        "however you meant it. If you must refer back, say "
                        "\"following up on\"."},
                {"text": "The full background to the situation", "ok": False,
                 "why": "Background belongs below the ask, for the minority "
                        "who want it. Leading with it loses the majority."},
            ],
        },
        {
            "q": "Why avoid \"kindly do the needful\"?",
            "remember": "It never says what you actually want.",
            "answers": [
                {"text": "It is too informal", "ok": False,
                 "why": "It is if anything over-formal. The problem is not "
                        "register, it is that the reader is left guessing what "
                        "action is required."},
                {"text": "It never states the actual action required",
                 "ok": True,
                 "why": "The reader has to infer what needful means here, and "
                        "different people infer differently. Name the action "
                        "and the date and the ambiguity disappears."},
                {"text": "It is grammatically incorrect", "ok": False,
                 "why": "It is grammatical. The objection is entirely "
                        "practical — it transfers the work of deciding what to "
                        "do onto the reader."},
                {"text": "Customers find it offensive", "ok": False,
                 "why": "Most do not. They find it unclear, which costs you a "
                        "round of emails rather than any goodwill."},
            ],
        },
        {
            "q": "You are annoyed. What helps most?",
            "remember": "Remove blame and adverbs; state dates.",
            "answers": [
                {"text": "Being very formal", "ok": False,
                 "why": "Heavy formality when annoyed reads as cold anger, "
                        "which is worse than plain irritation. It also makes "
                        "the message longer."},
                {"text": "Deleting every \"you\" that assigns blame, and every "
                         "adverb", "ok": True,
                 "why": "\"Your team repeatedly failed\" becomes \"the "
                        "drawings were due on the 8th\". The fact is unchanged, "
                        "the accusation is gone, and it is harder to argue "
                        "with."},
                {"text": "Adding an apology to soften it", "ok": False,
                 "why": "You have nothing to apologise for, and apologising "
                        "for chasing makes the request read as optional."},
                {"text": "Copying their manager", "ok": False,
                 "why": "That is an escalation, not a tone adjustment. It "
                        "usually ends cooperation and should come much later, "
                        "if at all."},
            ],
        },
        {
            "q": "When should you reply all?",
            "remember": "Only when everyone needs the reply.",
            "answers": [
                {"text": "Whenever you were included in the original",
                 "ok": False,
                 "why": "Being in the To field does not mean everyone needs "
                        "your answer. This habit is why people stop reading "
                        "group threads at all."},
                {"text": "When the whole group is waiting on the decision",
                 "ok": True,
                 "why": "That is genuinely useful — it stops others chasing or "
                        "duplicating work. Everything else, including "
                        "\"Thanks\", goes to the sender only."},
                {"text": "When you want visibility for your work", "ok": False,
                 "why": "It is transparent and it costs everybody else "
                        "attention. Visibility is better earned in the "
                        "messages people actually needed."},
                {"text": "When the thread is short", "ok": False,
                 "why": "Length is irrelevant. The test is whether each "
                        "recipient needs your specific reply to do something."},
            ],
        },
        {
            "q": "Which email should not be sent at all?",
            "remember": "Anything about a person's performance.",
            "answers": [
                {"text": "A delivery date confirmation", "ok": False,
                 "why": "Factual and worth having in writing. Email is exactly "
                        "the right channel for it."},
                {"text": "Feedback on a colleague's performance", "ok": True,
                 "why": "It concerns a person, tone is unreadable in text, and "
                        "it becomes a permanent record of a conversation that "
                        "should have been two-way. Have it face to face."},
                {"text": "A price correction", "ok": False,
                 "why": "Commercially important and needs a record. Write it, "
                        "and make sure the correction is stated plainly rather "
                        "than buried."},
                {"text": "A meeting summary", "ok": False,
                 "why": "One of the most valuable emails there is, as long as "
                        "it carries decisions, owners and dates rather than "
                        "discussion."},
            ],
        },
    ],

    "recap": {
        "title": "Email writing on one screen",
        "points": [
            ("Delete the first sentence",
             "It almost always carries no information. Start with the point."),
            ("Retire four phrases",
             "\"As per my previous\", \"do the needful\", \"revert\", "
             "\"urgent\" everywhere."),
            ("Warmth goes at the end",
             "One line in the close does more than three in the opening."),
            ("Dates instead of adverbs",
             "\"Due on the 8th\" lands harder than \"repeatedly delayed\"."),
            ("Never send angry",
             "Write it, wait thirty minutes, and change the three things you "
             "will spot."),
            ("Reply-all almost never",
             "Only when the whole group is genuinely waiting on your answer."),
        ],
        "oneliner": "Say the thing, give the date, make one ask, and put the "
                    "warmth at the end.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("chat", "The neutral chaser",
             "Dates, no blame, one small request at the end."),
            ("cycle", "The de-escalation rewrite",
             "Removes blame and adverbs, keeps the meaning."),
            ("check", "The ten-second check",
             "Recipients, subject, one ask, forwardable."),
        ],
        "links": [
            ("Microsoft Copilot", "https://copilot.microsoft.com"),
            ("ChatGPT", "https://chatgpt.com"),
            ("Google Gemini", "https://gemini.google.com"),
        ],
        "next": "Next module: PS-03, English & Grammar for the Workplace. The "
                "handful of patterns that cause most misunderstandings at "
                "work.",
    },

    "glossary": [
        ("Throat-clearing", "An opening sentence that carries no information. "
                            "Usually safe to delete."),
        ("Tone", "How a message reads, as distinct from what it says. Text "
                 "reads sharper than speech."),
        ("Escalation", "Involving somebody's manager. A real step, and rarely "
                       "the second one."),
        ("Reply all", "Sending to everyone on a thread. Appropriate only when "
                      "all of them need it."),
        ("Close", "The final line, where warmth belongs. It is read; the "
                  "opening often is not."),
        ("Ask", "The one action you need, with a date attached."),
    ],
}
