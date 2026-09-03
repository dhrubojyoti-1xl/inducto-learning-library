# -*- coding: utf-8 -*-
"""PS-01 — Business Communication. Content only."""

DECK = {
    "module_code": "PS-01",
    "area": "04-professional-skills",
    "filename": "04-01-business-communication.pptx",
    "title": "Business Communication",
    "subtitle": "Getting a decision out of people who are busy, in messages "
                "they read to the end.",
    "duration_min": 17,
    "audience": "New joiners + staff",
    "motif": "layers",

    "why": {
        "title": "Gopal writes 400 words and waits",
        "icon": "mail",
        "scenario": "Gopal manages operations near Nagpur. He needs a decision "
                    "on overtime by Friday. He writes a careful 400-word email "
                    "explaining the background, the options and the costs. By "
                    "Wednesday, nobody has replied.",
        "cost": "Four days lost, and the decision still not made.",
        "fix": "The ask in the first line, and everything else underneath it.",
    },

    "outcomes": [
        ("chat", "Put the ask in the first line, every time"),
        ("list", "Write one message with one decision in it"),
        ("person", "Choose the right channel instead of defaulting to email"),
        ("clock", "Say what happens if nobody replies, and mean it"),
        ("eye", "Rewrite a message that got no response, in two minutes"),
    ],

    "sections": [
        ("Ask first", "Why 400 words fail", "s_ask"),
        ("One message, one ask", "Two questions get one answer", "s_one"),
        ("Choosing the channel", "Email is not always right", "s_channel"),
        ("The silent default", "What happens if nobody replies", "s_default"),
        ("Do this now", "Rewrite one real message", "s_do"),
        ("Choose what you'd do", "A Wednesday afternoon decision", "scenario"),
        ("Watch this", "A 4-minute outside guide", "video"),
    ],

    "slides": [
        {
            "anchor": "s_ask",
            "label": "Ask first",
            "title": "Put the ask in line one",
            "lead": "Most people read the first line and the last. Everything "
                    "you buried in the middle was never read.",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "Background first",
                "bad": [
                    "Four paragraphs of context, then the question.",
                    "The reader stops after two, meaning to come back.",
                    "They never come back, and you are chasing on Thursday.",
                ],
                "good_tag": "Ask first",
                "good": [
                    "\"I need a yes or no on weekend overtime by Friday "
                    "midday.\"",
                    "Then the context, for whoever wants it.",
                    "The reader knows in four seconds whether this needs "
                    "them.",
                ],
                "note": "Front-loading is not rudeness. It is the only way a "
                        "busy person can triage twenty messages before a "
                        "meeting.",
            },
        },
        {
            "label": "Ask first",
            "title": "The four-part message",
            "visual": {
                "type": "flow",
                "steps": [
                    ("The ask", "What you need, and by when. One sentence."),
                    ("Why it matters", "The consequence if it does not "
                                       "happen."),
                    ("The options", "Two or three, not seven."),
                    ("The detail", "For anyone who wants it. Most will not."),
                ],
            },
        },
        {
            "anchor": "s_one",
            "label": "One message, one ask",
            "title": "Two questions get one answer",
            "visual": {
                "type": "split",
                "left": {
                    "tag": "Three asks", "tone": "bad",
                    "title": "One long message",
                    "items": [
                        "Approve the overtime, confirm the shift pattern, and "
                        "sign the PO",
                        "The reader answers the easiest one",
                        "You chase the other two separately anyway",
                        "Nobody can tell what is outstanding",
                    ],
                },
                "right": {
                    "tag": "One ask each", "tone": "good",
                    "title": "Three short messages",
                    "items": [
                        "Each has one subject line and one question",
                        "Each can be answered in ten seconds",
                        "Each can be forwarded to the right person",
                        "You can see instantly what is still open",
                    ],
                },
            },
        },
        {
            "label": "One message, one ask",
            "title": "The message, ready to use",
            "visual": {
                "type": "prompt",
                "header": "Copy this structure",
                "text": "I need [a decision / a document / an approval] on "
                        "[subject] by [day and time]. If we do not have it by "
                        "then, [what happens]. The options are [A] or [B]. "
                        "Background is below if you need it, but the question "
                        "is just A or B.",
                "caption": "Five brackets. Fill them in and stop writing.",
                "why": [
                    "The deadline is stated, so it is not a suggestion.",
                    "The consequence makes the deadline real.",
                    "\"The question is just A or B\" makes replying trivial.",
                ],
            },
        },
        {
            "anchor": "s_channel",
            "label": "Choosing the channel",
            "title": "Email is not always right",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "EMAIL — a decision you will need a record of, later",
                    "CALL — anything with disagreement or bad news in it",
                    "CHAT — a quick factual question with no consequence",
                    "IN PERSON — anything about a person's performance",
                ],
            },
        },
        {
            "label": "Choosing the channel",
            "title": "The escalation ladder",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "mail", "label": "First: a clear email",
                     "sub": "One ask, a deadline, and a stated consequence. "
                            "Most things end here."},
                    {"icon": "chat", "label": "Then: a short call",
                     "sub": "After one missed deadline. Two minutes on the "
                            "phone beats a third email."},
                    {"icon": "person", "label": "Then: involve a manager",
                     "sub": "With the email trail attached, factually, without "
                            "complaint or commentary."},
                ],
            },
        },
        {
            "anchor": "s_default",
            "label": "The silent default",
            "title": "Say what silence means",
            "lead": "A deadline with no consequence attached is a suggestion, "
                    "and everybody treats it as one.",
            "visual": {
                "type": "prompt",
                "header": "Copy this wording",
                "text": "If I do not hear back by Thursday 5pm, I will assume "
                        "we are proceeding with option A and will book the "
                        "shift accordingly. Please tell me before then if that "
                        "is not what you want.",
                "caption": "Use it only when you can genuinely act on the "
                           "default.",
                "why": [
                    "It removes the cost of not replying, which was the "
                    "problem.",
                    "It gives the reader an easy way to stop you.",
                    "It converts silence into a decision instead of a delay.",
                ],
            },
        },
        {
            "label": "The silent default",
            "title": "When not to use a default",
            "visual": {
                "type": "bandlist",
                "mark": "ban",
                "headline": "A silent default only works if you can honestly "
                            "act on it, and if the reader could reasonably "
                            "object in time.",
                "sub": "Used wrongly it reads as a threat, or as a decision "
                       "taken behind somebody's back.",
                "cols": 3,
                "items": [
                    "Never for spending somebody else's budget.",
                    "Never with under 24 hours' notice.",
                    "Never for anything involving a person.",
                ],
            },
        },
        {
            "anchor": "s_do",
            "label": "Do this now",
            "title": "Do this now: rewrite one",
            "visual": {
                "type": "steps",
                "items": [
                    "Find a message you sent that never got a reply.",
                    "Delete everything except the actual question.",
                    "Put the deadline and the consequence in the first line.",
                    "Send it again, with a subject line naming the decision.",
                ],
                "prompt": "Rewrite the message below so the ask, the deadline "
                          "and the consequence are all in the first two "
                          "sentences. Move everything else below a line "
                          "marked \"Background\". Keep it under 120 words. Do "
                          "not add anything I have not written.",
                "caption": "Two minutes, and a message people can actually "
                           "answer.",
            },
        },
        {
            "label": "Do this now",
            "title": "The subject line does work",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "Weak subject",
                "bad": [
                    "Subject: Overtime",
                    "Says nothing about what is needed or by when.",
                    "Sits in a list of forty other one-word subjects.",
                ],
                "good_tag": "Working subject",
                "good": [
                    "Subject: Decision needed by Fri 12pm — weekend overtime, "
                    "A or B",
                    "Readable without opening. Filterable. Findable in June.",
                    "The reader knows immediately whether it is theirs.",
                ],
                "note": "A subject line naming the decision and the deadline "
                        "does more for your response rate than anything in the "
                        "body.",
            },
        },
        {
            "label": "Do this now",
            "title": "Four habits worth having",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "One message, one decision. Split anything with two.",
                    "Deadline and consequence in the first two sentences.",
                    "Subject line names the decision, not the topic.",
                    "After one missed deadline, pick up the phone.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Five mistakes people really make",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Explaining before asking",
                     "The reader stops in paragraph two, meaning to come back. "
                     "They do not come back."),
                    ("Three questions in one email",
                     "You get an answer to the easiest one and chase the other "
                     "two for a week."),
                    ("A deadline with no consequence",
                     "It reads as a preference. Nobody has ever missed a "
                     "preference and felt anything."),
                    ("Using email for a disagreement",
                     "Tone is unreadable in text, and both sides reread it "
                     "uncharitably."),
                    ("Chasing by sending the same email again",
                     "It was not read the first time. Sending it twice mostly "
                     "annoys people."),
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Writing for someone senior",
            "visual": {
                "type": "tree",
                "question": "Do they need to decide, or just to know?",
                "yes": {
                    "path": "Decide", "tone": "good", "label": "Ask first",
                    "detail": "Lead with the decision, the deadline and two "
                              "options. Recommend one of them — people rarely "
                              "resent a recommendation, and always resent a "
                              "shapeless choice.",
                },
                "no": {
                    "path": "Just know", "tone": "neutral",
                    "label": "Say so at the top",
                    "detail": "\"No action needed — for information only.\" It "
                              "takes four words and it stops a senior person "
                              "reading carefully for a request that is not "
                              "there.",
                },
            },
        },
        {
            "label": "Do this now",
            "title": "The communication rule",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "Every message should answer three things in the "
                            "first two sentences: what, by when, and what "
                            "happens if not.",
                "sub": "Everything else is background, and background belongs "
                       "underneath.",
                "cols": 3,
                "items": [
                    "What you need.",
                    "By when.",
                    "What happens if not.",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Wednesday, 3:00 pm",
        "situation": "You emailed on Monday asking for an overtime decision by "
                     "Friday. Nobody has replied. The shift has to be booked "
                     "with the contractor by Friday evening.",
        "choices": [
            {
                "text": "Forward the original email with \"Any update?\" on "
                        "top.",
                "tone": "bad",
                "headline": "It was not read the first time",
                "consequence": "The same 400 words arrive again, with two more "
                               "words on top. Whoever skipped it on Monday "
                               "skips it again on Wednesday, and now finds the "
                               "chasing slightly irritating. Friday arrives "
                               "with no decision.",
                "rule": "Resending an unread message mostly resends the "
                        "problem.",
            },
            {
                "text": "Send a three-line message with the ask, the deadline "
                        "and the default.",
                "tone": "good",
                "headline": "Three lines, answered in eleven minutes",
                "consequence": "\"I need a yes or no on weekend overtime by "
                               "Friday midday. If I do not hear back, I will "
                               "book option A. Cost difference is about "
                               "₹18,000.\" You get a one-word reply before "
                               "half past three.",
                "rule": "Short, with a stated default, is far easier to answer "
                        "than long and open.",
            },
            {
                "text": "Ring them and confirm in writing afterwards.",
                "tone": "good",
                "headline": "Also right, and often faster",
                "consequence": "Two minutes on the phone settles it, and a "
                               "one-line email afterwards gives you the "
                               "record. This is the correct move after one "
                               "missed deadline, and better than a third "
                               "email.",
                "rule": "After one missed deadline, change channel rather than "
                        "repeating yourself.",
            },
        ],
    },

    # Title, channel and runtime were read back from YouTube
    # itself. See newvideos.json.
    "video": {
        "url": "https://www.youtube.com/watch?v=LBNF6l2n3YM",
        "title": "How to Write Email with Military Precision",
        "channel": "Harvard Business Review",
        "duration": "4:02",
        "heading": "Four minutes on writing sharply",
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
            "q": "Where should the ask go?",
            "remember": "First line, with the deadline.",
            "answers": [
                {"text": "At the end, after the reasoning", "ok": False,
                 "why": "Almost nobody reaches the end of a work email. Your "
                        "question sits below the point where the reader "
                        "stopped, meaning to come back later."},
                {"text": "In the first sentence, with the deadline", "ok": True,
                 "why": "The reader can decide in four seconds whether this "
                        "needs them, and can answer without reading anything "
                        "else. Background belongs below, for the few who want "
                        "it."},
                {"text": "In the middle, after the context", "ok": False,
                 "why": "The middle is where attention is lowest. It is the "
                        "worst place in the message for the one sentence that "
                        "has to be read."},
                {"text": "In a separate follow-up message", "ok": False,
                 "why": "Now there are two messages and it is unclear which "
                        "one to reply to. One message with one ask is the goal."},
            ],
        },
        {
            "q": "Why one ask per message?",
            "remember": "Two questions get one answer.",
            "answers": [
                {"text": "It is more polite", "ok": False,
                 "why": "Politeness is not the issue. The issue is that people "
                        "answer the easiest question and forget the rest, "
                        "which leaves you chasing."},
                {"text": "People answer one and forget the others", "ok": True,
                 "why": "Reliably. Three asks in one email produces one "
                        "answer, and you cannot tell from the reply which of "
                        "the other two were even read."},
                {"text": "Long emails break spam filters", "ok": False,
                 "why": "Not a real consideration for internal mail. The "
                        "problem is entirely about how people actually read "
                        "and reply."},
                {"text": "It looks more professional", "ok": False,
                 "why": "It does read better, and that is a side effect. The "
                        "practical reason is that each one becomes separately "
                        "trackable and answerable."},
            ],
        },
        {
            "q": "Which needs a call, not an email?",
            "remember": "Disagreement and bad news.",
            "answers": [
                {"text": "Confirming a delivery slot", "ok": False,
                 "why": "Factual, uncontroversial and worth having in writing. "
                        "Email is exactly right, and a call would need "
                        "confirming afterwards anyway."},
                {"text": "Telling a supplier we are rejecting their claim",
                 "ok": True,
                 "why": "Bad news and likely disagreement. Tone is unreadable "
                        "in text and both sides reread it uncharitably. Call "
                        "first, then confirm the outcome in writing."},
                {"text": "Sharing next month's schedule", "ok": False,
                 "why": "Information people need to refer back to. Writing is "
                        "the point, and a call would leave nothing to check "
                        "against."},
                {"text": "Asking for a document", "ok": False,
                 "why": "A small, factual request. Chat or email is fine, and "
                        "a call for this would be more interruption than it is "
                        "worth."},
            ],
        },
        {
            "q": "When is a stated default fair?",
            "remember": "Only when you can honestly act on it.",
            "answers": [
                {"text": "Any time you need a fast answer", "ok": False,
                 "why": "Used as a general pressure tactic it reads as a "
                        "threat, and it stops working once people notice you "
                        "never actually act on the default."},
                {"text": "When you genuinely can proceed and they have time to "
                         "object", "ok": True,
                 "why": "Both conditions matter. If you could not really "
                        "proceed, it is a bluff. If they have four hours' "
                        "notice, it is not a real opportunity to object."},
                {"text": "When your manager is away", "ok": False,
                 "why": "Absence is not authority. If the decision is theirs, "
                        "it stays theirs, and a default cannot manufacture "
                        "permission."},
                {"text": "When the cost is small", "ok": False,
                 "why": "Small cost helps, and it is not sufficient. The test "
                        "is whether you could act on the default honestly, "
                        "whatever the amount."},
            ],
        },
        {
            "q": "What makes a subject line work?",
            "remember": "The decision and the deadline.",
            "answers": [
                {"text": "It is short", "ok": False,
                 "why": "\"Overtime\" is very short and tells the reader "
                        "nothing. A longer subject that names the decision "
                        "and the date is far more useful."},
                {"text": "It names the decision and when it is needed",
                 "ok": True,
                 "why": "\"Decision needed by Fri 12pm — weekend overtime, A "
                        "or B\" is readable without opening, filterable, and "
                        "findable months later."},
                {"text": "It matches the first line of the email", "ok": False,
                 "why": "Duplication wastes the one line most likely to be "
                        "read. Use it to carry information the body then "
                        "builds on."},
                {"text": "It marks the message as urgent", "ok": False,
                 "why": "Urgency flags stop working after the second use, and "
                        "they make the genuinely urgent messages invisible."},
            ],
        },
    ],

    "recap": {
        "title": "Business communication on one screen",
        "points": [
            ("Ask first, always",
             "What you need and by when, in the first sentence. Background "
             "below."),
            ("One message, one ask",
             "Two questions reliably produce one answer and a week of "
             "chasing."),
            ("Say what happens if not",
             "A deadline with no consequence is read as a preference."),
            ("Subject lines carry the decision",
             "Name the decision and the date, not the topic."),
            ("Change channel, do not repeat",
             "After one missed deadline, a two-minute call beats a third "
             "email."),
            ("Disagreement goes on the phone",
             "Tone is unreadable in text, and both sides reread it "
             "uncharitably."),
        ],
        "oneliner": "What you need, by when, and what happens if not — in the "
                    "first two sentences.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("mail", "The five-bracket message",
             "Ask, deadline, consequence, options, background below."),
            ("clock", "The stated default",
             "\"If I do not hear by Thursday, I will proceed with A.\""),
            ("list", "The channel test",
             "Record, disagreement, quick question, or a person."),
        ],
        "links": [
            ("Microsoft Copilot", "https://copilot.microsoft.com"),
            ("ChatGPT", "https://chatgpt.com"),
            ("Google Gemini", "https://gemini.google.com"),
        ],
        "next": "Next module: PS-02, Professional Email Writing. The "
                "mechanics — subject lines, openings, and knowing when not to "
                "send at all.",
    },

    "glossary": [
        ("Ask", "The one thing you need the reader to do. It belongs in the "
                "first sentence."),
        ("Stated default", "What you will do if nobody replies. It turns "
                           "silence into a decision."),
        ("Channel", "Email, call, chat or in person. Choosing deliberately "
                    "prevents most communication problems."),
        ("Escalation", "Moving a stalled request to a call, then to a manager, "
                       "factually and without complaint."),
        ("Front-loading", "Putting the conclusion and the request before the "
                          "reasoning."),
        ("Background", "Context for the few readers who want it. Always below "
                       "the ask."),
    ],
}
