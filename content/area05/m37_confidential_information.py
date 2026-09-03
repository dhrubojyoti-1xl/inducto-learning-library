# -*- coding: utf-8 -*-
"""SEC-05 — Handling Confidential Information. Content only."""

DECK = {
    "module_code": "SEC-05",
    "area": "05-security-privacy",
    "filename": "05-05-handling-confidential-information.pptx",
    "title": "Handling Confidential Information",
    "subtitle": "The commercial material that is not personal data, and still "
                "must never leave the building.",
    "duration_min": 16,
    "audience": "Mandatory for all staff",
    "motif": "layers",

    "why": {
        "title": "Divya shows a slide with a real price",
        "icon": "eye",
        "scenario": "Divya supports the legal team in Bengaluru. She reuses an "
                    "old slide in a supplier presentation. It still carries "
                    "the discount structure agreed with a different supplier. "
                    "Nobody notices in the room. The photograph circulates.",
        "cost": "One supplier now knows exactly what we give another.",
        "fix": "Four classes of information, and a habit of checking the "
               "slide.",
    },

    "outcomes": [
        ("list", "Sort information into four classes in a few seconds"),
        ("eye", "Spot confidential material hidden in reused documents"),
        ("shield", "Share what a third party needs without over-sharing"),
        ("ban", "Know what never leaves, regardless of who is asking"),
        ("person", "Handle the request that comes from inside the company"),
    ],

    "sections": [
        ("Four classes", "Public to restricted", "s_classes"),
        ("Where it hides", "Reused files and old slides", "s_hides"),
        ("Sharing outside", "Need to know, not nice to know", "s_share"),
        ("Requests from inside", "Colleagues are not automatic", "s_inside"),
        ("Do this now", "Classify five real documents", "s_do"),
        ("Choose what you'd do", "A supplier-meeting decision", "scenario"),
        ("Watch this", "A 4-minute outside explainer", "video"),
    ],

    "slides": [
        {
            "anchor": "s_classes",
            "label": "Four classes",
            "title": "Four classes, few seconds",
            "lead": "Most companies use some version of this. The names matter "
                    "less than the habit of asking.",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "PUBLIC — already published. The website, a brochure",
                    "INTERNAL — fine inside, awkward outside. Org charts, "
                    "processes",
                    "CONFIDENTIAL — damaging outside. Prices, margins, "
                    "contracts",
                    "RESTRICTED — damaging even inside. Salaries, "
                    "acquisitions, legal cases",
                ],
            },
        },
        {
            "label": "Four classes",
            "title": "Restricted means inside too",
            "visual": {
                "type": "nested",
                "layers": [
                    {"label": "Public",
                     "sub": "Anyone, anywhere. Already published by us."},
                    {"label": "Internal and confidential",
                     "sub": "Colleagues who need it for their work."},
                    {"label": "Restricted",
                     "sub": "A named few. Not the whole department."},
                ],
                "note": "The mistake people make is assuming a colleague "
                        "automatically qualifies. Restricted material is "
                        "restricted from most of us, which is what the word "
                        "means.",
            },
        },
        {
            "anchor": "s_hides",
            "label": "Where it hides",
            "title": "It hides in reused files",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("An old slide left in a reused deck",
                     "Discount structures, margins and named accounts survive "
                     "in slides nobody scrolled to."),
                    ("Hidden columns in a shared spreadsheet",
                     "Hiding a column does not remove it. Anyone can unhide it "
                     "in one click."),
                    ("Tracked changes and comments in a document",
                     "The internal argument about pricing is still in the file "
                     "you sent out."),
                    ("File properties and the file name itself",
                     "\"Margin analysis v4 FINAL confidential.xlsx\" tells a "
                     "story before it is opened."),
                    ("A photograph of a whiteboard",
                     "The other half of the board is usually still legible in "
                     "the picture."),
                ],
            },
        },
        {
            "label": "Where it hides",
            "title": "Check before it leaves",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Scroll the whole deck, including slides after the last "
                    "one you use.",
                    "Unhide every row and column before sending a "
                    "spreadsheet.",
                    "Accept or reject all changes and delete all comments.",
                    "Rename the file to something you would be happy to see "
                    "quoted.",
                ],
            },
        },
        {
            "anchor": "s_share",
            "label": "Sharing outside",
            "title": "Need to know, not nice to know",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "Sending the whole file",
                "bad": [
                    "A supplier asks for last quarter's volumes for their "
                    "product.",
                    "You send the whole volume report, covering every "
                    "product and supplier.",
                    "They now know what their competitors ship to us.",
                ],
                "good_tag": "Sending the answer",
                "good": [
                    "You copy out the three lines that concern their product.",
                    "Into a fresh document, with nothing else in it.",
                    "They get a better answer, faster, and learn nothing "
                    "else.",
                ],
                "note": "Sending the whole file is almost always laziness "
                        "rather than generosity. The extract takes two "
                        "minutes.",
            },
        },
        {
            "label": "Sharing outside",
            "title": "The extract habit",
            "visual": {
                "type": "prompt",
                "header": "Copy this wording",
                "text": "Thanks — I can share the figures for your product "
                        "line. I will send those as a separate extract rather "
                        "than the full report, since the report covers other "
                        "suppliers as well. You will have it within the hour.",
                "caption": "Nobody has ever objected to this. Most people "
                           "expect it.",
                "why": [
                    "It says yes, which keeps the relationship easy.",
                    "It explains why, so it does not read as suspicion.",
                    "It commits to a time, so it is not a soft refusal.",
                ],
            },
        },
        {
            "anchor": "s_inside",
            "label": "Requests from inside",
            "title": "Colleagues are not automatic",
            "lead": "Being employed here is not the same as needing to know. "
                    "Most internal leaks start as a helpful favour.",
            "visual": {
                "type": "tree",
                "question": "Do they need this for work they are actually "
                            "doing?",
                "yes": {
                    "path": "Yes", "tone": "good", "label": "Share it",
                    "detail": "Their job requires it. Send the part they "
                              "need, not the whole file — exactly as you "
                              "would externally.",
                },
                "no": {
                    "path": "Curious", "tone": "bad", "label": "Point them on",
                    "detail": "\"That one sits with Finance.\" Not a "
                              "refusal — it puts the decision with whoever "
                              "owns the data.",
                },
            },
        },
        {
            "label": "Requests from inside",
            "title": "Saying no without friction",
            "visual": {
                "type": "prompt",
                "header": "Copy this wording",
                "text": "I do not think I am the right person to share that "
                        "one — it sits with [TEAM] and they will know what can "
                        "go out. Happy to introduce you if that helps. If they "
                        "are fine with it, send it over and I will work from "
                        "it.",
                "caption": "Redirects rather than refuses. Almost nobody "
                           "pushes back.",
                "why": [
                    "It puts the decision with whoever owns the information.",
                    "It offers help, so it does not read as obstruction.",
                    "It keeps you out of a judgement that is not yours.",
                ],
            },
        },
        {
            "anchor": "s_do",
            "label": "Do this now",
            "title": "Do this now: classify five",
            "visual": {
                "type": "steps",
                "items": [
                    "Open the five documents you have used most this week.",
                    "Put each into one of the four classes, out loud.",
                    "For any confidential one, check who currently has "
                    "access.",
                    "Remove anyone who no longer needs it.",
                ],
                "prompt": "I will describe a document without showing it to "
                          "you. Ask me four short questions, then tell me "
                          "whether it is public, internal, confidential or "
                          "restricted, and who should be able to open it. Do "
                          "not ask me to paste the contents.",
                "caption": "Describe the type of document. Never paste the "
                           "document.",
            },
        },
        {
            "label": "Do this now",
            "title": "What never leaves, ever",
            "visual": {
                "type": "bandlist",
                "mark": "ban",
                "headline": "Some material does not leave regardless of who is "
                            "asking or why.",
                "sub": "If somebody insists, that itself is worth reporting.",
                "cols": 2,
                "items": [
                    "Pricing or margin structures agreed with another party",
                    "Salaries, appraisals or disciplinary records",
                    "Legal advice, live disputes or draft settlements",
                    "Unannounced acquisitions, closures or product plans",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Marking things properly",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "doc", "label": "Mark it once",
                     "sub": "A single word in the header. The reader then "
                            "knows without asking anybody."},
                    {"icon": "person", "label": "Say who it is for",
                     "sub": "\"Confidential — Finance and Directors only\" is "
                            "far more useful than \"Confidential\"."},
                    {"icon": "clock", "label": "Say when it stops",
                     "sub": "\"Restricted until the announcement on 12 May\" "
                            "prevents permanent over-caution."},
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Five mistakes people really make",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Reusing a deck without scrolling to the end",
                     "The slide you forgot is the one somebody photographs."),
                    ("Sending a whole report to answer one question",
                     "Generosity that hands over every other supplier's "
                     "position."),
                    ("Assuming a colleague qualifies",
                     "Employment is not need-to-know. Most internal leaks "
                     "start as a favour."),
                    ("Discussing figures in a public place",
                     "Airports, cafés and shared taxis. Somebody is always "
                     "close enough."),
                    ("Marking everything confidential",
                     "When everything is marked, nothing is. People stop "
                     "reading the label."),
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "The confidentiality rule",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "Send the answer, not the file it came from.",
                "sub": "That habit covers external sharing, internal favours "
                       "and reused documents all at once.",
                "cols": 3,
                "items": [
                    "Extract, do not forward.",
                    "Need to know, not nice to know.",
                    "Scroll to the end before sending.",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Supplier meeting, Wednesday",
        "situation": "You are presenting to a supplier and reusing last "
                     "quarter's internal deck. You have ten minutes before the "
                     "meeting and have not opened it since March.",
        "choices": [
            {
                "text": "Present it as it is — you only need the first six "
                        "slides.",
                "tone": "bad",
                "headline": "Slide 14 is still in the file",
                "consequence": "You never reach slide 14, but you scroll past "
                               "it to get back to slide 3 during a question. "
                               "It shows the discount structure agreed with "
                               "their competitor. Somebody in the room "
                               "photographs the screen.",
                "rule": "A file you present is a file you have shared, all of "
                        "it.",
            },
            {
                "text": "Copy the six slides into a fresh deck and present "
                        "that.",
                "tone": "good",
                "headline": "Five minutes, and nothing else exists in the file",
                "consequence": "A new file containing exactly six slides. "
                               "Nothing to scroll past, nothing hidden, "
                               "nothing to photograph. It also loads faster "
                               "and looks deliberate rather than recycled.",
                "rule": "Build the file you are actually presenting.",
            },
            {
                "text": "Delete the later slides from the original and present "
                        "it.",
                "tone": "ok",
                "headline": "Works, if you actually check",
                "consequence": "Reasonable and it depends entirely on you "
                               "scrolling to the very end. People routinely "
                               "miss hidden slides, notes pages and comments. "
                               "A fresh file removes the need to be thorough "
                               "under time pressure.",
                "rule": "Deleting requires care. Starting fresh does not.",
            },
        ],
    },

    # Title, channel and runtime were read back from YouTube
    # itself. See newvideos.json.
    "video": {
        "url": "https://www.youtube.com/watch?v=gquCNKKhJE0",
        "title": "Data Protection: Data Classification: Public, Internal, "
                 "Confidential and Restricted - Lesson 4",
        "channel": "Experts Academy",
        "duration": "3:32",
        "heading": "Four minutes on the four classes",
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
            "q": "What does restricted actually mean?",
            "remember": "Restricted from most colleagues too.",
            "answers": [
                {"text": "Cannot leave the company", "ok": False,
                 "why": "That describes confidential. Restricted goes further "
                        "— it also cannot circulate freely inside the "
                        "company."},
                {"text": "Only a named few can see it, inside or out",
                 "ok": True,
                 "why": "Salaries, live legal matters and unannounced plans "
                        "are restricted from most employees. Being employed "
                        "here does not qualify anyone."},
                {"text": "Needs a password to open", "ok": False,
                 "why": "A control that may be used, not a definition. "
                        "Classification is about who should see it; passwords "
                        "are one way of enforcing that."},
                {"text": "Must be deleted after use", "ok": False,
                 "why": "Retention is a separate question. Plenty of "
                        "restricted material is kept for years by the few "
                        "people entitled to it."},
            ],
        },
        {
            "q": "A supplier asks for volume figures.",
            "remember": "Send the extract, never the report.",
            "answers": [
                {"text": "Send the full report — it is easier", "ok": False,
                 "why": "It hands them every other supplier's volumes as well. "
                        "The two minutes you saved could cost a negotiating "
                        "position that took months to build."},
                {"text": "Copy their three lines into a fresh document",
                 "ok": True,
                 "why": "They get a clearer answer faster, and learn nothing "
                        "about anyone else. Say plainly that you are sending "
                        "an extract — it reads as professional, not "
                        "suspicious."},
                {"text": "Refuse — volumes are confidential", "ok": False,
                 "why": "Their own volumes are not confidential from them. A "
                        "blanket refusal damages a relationship for no "
                        "protective benefit."},
                {"text": "Send it with the other columns hidden", "ok": False,
                 "why": "Hiding is not removing. Anyone can unhide a column in "
                        "one click, and most people eventually do."},
            ],
        },
        {
            "q": "A colleague asks for the margin file.",
            "remember": "Need to know, not employment.",
            "answers": [
                {"text": "Send it — they work here", "ok": False,
                 "why": "Employment is not need-to-know. Most internal leaks "
                        "begin as a helpful favour between colleagues who "
                        "trust each other."},
                {"text": "Ask what they need it for, and point them at the "
                         "owner", "ok": True,
                 "why": "If it is genuinely for their work, the owner will "
                        "release it. If it is curiosity, the question ends the "
                        "matter politely without you refusing anything."},
                {"text": "Refuse and say nothing further", "ok": False,
                 "why": "Creates friction for no reason. Redirecting to "
                        "whoever owns the data is just as safe and far easier "
                        "to work with."},
                {"text": "Send an older version instead", "ok": False,
                 "why": "Still confidential, and now also out of date. You "
                        "have shared the material and created a second problem "
                        "on top."},
            ],
        },
        {
            "q": "Where does confidential material hide?",
            "remember": "In files you reused without scrolling.",
            "answers": [
                {"text": "In the first three slides", "ok": False,
                 "why": "Those are the ones everybody checks. Risk lives where "
                        "attention does not."},
                {"text": "In slides after the last one you present", "ok": True,
                 "why": "Along with hidden columns, tracked changes, comments "
                        "and the file name. All survive reuse and none of them "
                        "get looked at."},
                {"text": "In the file's colour scheme", "ok": False,
                 "why": "Formatting carries no information. It is content in "
                        "unexamined places that causes the problem."},
                {"text": "Only in files marked confidential", "ok": False,
                 "why": "Marking is often missing, especially on reused "
                        "internal decks. The absence of a label proves "
                        "nothing at all."},
            ],
        },
        {
            "q": "Why not mark everything confidential?",
            "remember": "When everything is marked, nothing is.",
            "answers": [
                {"text": "It slows down email", "ok": False,
                 "why": "There is no technical cost. The problem is entirely "
                        "about how people respond to the label."},
                {"text": "People stop reading the label", "ok": True,
                 "why": "If the canteen menu is marked confidential, the "
                        "marking on the acquisition paper carries no weight. "
                        "Over-marking destroys the signal you actually need."},
                {"text": "It is against the law", "ok": False,
                 "why": "It is not unlawful, merely ineffective. The issue is "
                        "practical rather than legal."},
                {"text": "It makes files bigger", "ok": False,
                 "why": "A header adds nothing measurable. The cost is "
                        "attention, not storage."},
            ],
        },
    ],

    "recap": {
        "title": "Confidential information on one screen",
        "points": [
            ("Four classes",
             "Public, internal, confidential, restricted. Ask which, in a few "
             "seconds."),
            ("Restricted excludes most colleagues",
             "Salaries, legal matters and unannounced plans are not "
             "department-wide."),
            ("It hides in reused files",
             "Extra slides, hidden columns, tracked changes, file names, "
             "whiteboard photos."),
            ("Send the answer, not the file",
             "Extracting three lines takes two minutes and reveals nothing "
             "else."),
            ("Employment is not need-to-know",
             "Redirect to the owner rather than refusing. Nobody takes "
             "offence."),
            ("Do not mark everything",
             "When every file is confidential, the label stops meaning "
             "anything."),
        ],
        "oneliner": "Send the answer, not the file it came from.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("shield", "The extract wording",
             "Says yes, explains why, commits to a time."),
            ("person", "The internal redirect",
             "Points at the owner without refusing anything."),
            ("check", "The before-sending check",
             "Scroll to the end, unhide, clear comments, rename."),
        ],
        "links": [
            ("India's data protection framework",
             "https://www.meity.gov.in/data-protection-framework"),
            ("UAE data protection laws", "https://u.ae/en/about-the-uae/"
                                         "digital-uae/data/data-protection-laws"),
            ("Check if your email has leaked", "https://haveibeenpwned.com"),
        ],
        "next": "Next module: SEC-06, Safe Use of AI at Work. Which tools are "
                "approved, which settings to switch off, and how to keep a "
                "trail you can explain.",
    },

    "glossary": [
        ("Classification", "Deciding which of the four classes a document "
                           "belongs to, and who may open it."),
        ("Need to know", "The test for sharing: does this person require it "
                         "for work they are actually doing?"),
        ("Restricted", "Material limited to a named few, including inside the "
                       "company."),
        ("Extract", "A fresh document containing only the part somebody "
                    "actually needs."),
        ("Metadata", "Information about a file: its name, author, comments and "
                     "tracked changes."),
        ("Confidential", "Damaging if it leaves the company, even though no "
                         "individual is identifiable."),
    ],
}
