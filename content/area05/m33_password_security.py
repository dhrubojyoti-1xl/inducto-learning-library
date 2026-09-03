# -*- coding: utf-8 -*-
"""SEC-01 — Password Security. Content only."""

DECK = {
    "module_code": "SEC-01",
    "area": "05-security-privacy",
    "filename": "05-01-password-security.pptx",
    "title": "Password Security",
    "subtitle": "Why one reused password is the most likely way this company "
                "gets broken into.",
    "duration_min": 16,
    "audience": "Mandatory for all staff",
    "motif": "shield",

    "why": {
        "title": "Sanjay used the same password twice",
        "icon": "key",
        "scenario": "Sanjay runs stores at a Nashik unit. Six years ago he "
                    "used one password for a shopping site. He uses the same "
                    "one at work. The shopping site was breached in 2021. "
                    "Nobody told him, and the password still works here.",
        "cost": "An attacker does not need to guess. They already have it.",
        "fix": "Different passwords everywhere, remembered by a manager, not "
               "by you.",
    },

    "outcomes": [
        ("key", "Explain why reuse matters more than complexity"),
        ("eye", "Check in 30 seconds whether your own details have leaked"),
        ("shield", "Build a password you can remember and nobody can guess"),
        ("lock", "Use a password manager without trusting your memory at all"),
        ("warn", "Know what to do in the first hour after a password is "
                 "exposed"),
    ],

    "sections": [
        ("How accounts get taken", "Not by guessing", "s_how"),
        ("Reuse is the real risk", "One breach, every account", "s_reuse"),
        ("Building a strong one", "Length beats symbols", "s_build"),
        ("Letting software remember", "Password managers", "s_manager"),
        ("Do this now", "Check and change one", "s_do"),
        ("Choose what you'd do", "A Tuesday morning decision", "scenario"),
        ("Watch this", "A 3-minute outside explainer", "video"),
    ],

    "slides": [
        {
            "anchor": "s_how",
            "label": "How accounts get taken",
            "title": "Nobody sits and guesses",
            "lead": "The film version is somebody typing guesses. The real "
                    "version is a list of passwords that already leaked.",
            "visual": {
                "type": "flow",
                "steps": [
                    ("A website is breached", "Somewhere you signed up, years "
                                              "ago, possibly forgotten."),
                    ("The list is sold", "Email addresses and passwords, "
                                         "millions at a time."),
                    ("Software tries them", "Automatically, against every "
                                            "well-known service."),
                    ("One of them works", "Because it was reused. That is the "
                                          "whole attack."),
                ],
            },
        },
        {
            "label": "How accounts get taken",
            "title": "What actually gets used",
            "visual": {
                "type": "split",
                "left": {
                    "tag": "What people worry about", "tone": "neutral",
                    "mark": "search",
                    "title": "Guessing your password",
                    "items": [
                        "Someone trying combinations by hand",
                        "Needing to know your dog's name",
                        "Symbols and capitals stopping them",
                        "Rare, slow and mostly fictional",
                    ],
                },
                "right": {
                    "tag": "What actually happens", "tone": "bad",
                    "title": "Trying passwords that leaked",
                    "items": [
                        "Your real password, from another site",
                        "Tried automatically against hundreds of services",
                        "Symbols and capitals do not help at all",
                        "Common, fast and completely routine",
                    ],
                },
            },
        },
        {
            "anchor": "s_reuse",
            "label": "Reuse is the real risk",
            "title": "One breach, every account",
            "gloss": ["Credential stuffing"],
            "visual": {
                "type": "nested",
                "layers": [
                    {"label": "One password you reuse",
                     "sub": "Chosen once, years ago, still in use."},
                    {"label": "Every site you used it on",
                     "sub": "Shopping, forums, an old email account."},
                    {"label": "Including work",
                     "sub": "The weakest of those sites decides our security."},
                ],
                "note": "Your work account is only as safe as the least "
                        "careful website you ever signed up to. That is what "
                        "reuse actually means.",
            },
        },
        {
            "label": "Reuse is the real risk",
            "title": "Small changes do not help",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Adding a number at the end",
                     "Attack software tries the obvious variations "
                     "automatically. It is the first thing it does."),
                    ("Changing one letter to a symbol",
                     "Replacing a with @ has been in every cracking list for "
                     "twenty years."),
                    ("Using the same base word everywhere",
                     "Once one is known, the pattern is known, and the rest "
                     "follow in seconds."),
                    ("Changing it only when forced to",
                     "A password that leaked in 2021 stays valid until the "
                     "day you change it."),
                ],
            },
        },
        {
            "anchor": "s_build",
            "label": "Building a strong one",
            "title": "Length beats symbols",
            "lead": "Three or four unrelated words are harder to break and far "
                    "easier to type than eight random characters.",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "THREE OR FOUR WORDS — \"copper-lantern-quiet-mango\"",
                    "UNRELATED — not your city, employer, family or team",
                    "LONG — aim for sixteen characters or more",
                    "UNIQUE — used on exactly one account, ever",
                ],
            },
        },
        {
            "label": "Building a strong one",
            "title": "Weak, medium, strong",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "Feels strong, is not",
                "bad": [
                    "Nashik@2024",
                    "Eleven characters, a capital, a symbol and a number.",
                    "It is a place name and a year. Both are in every list.",
                ],
                "good_tag": "Looks simple, is strong",
                "good": [
                    "copper-lantern-quiet-mango",
                    "Twenty-six characters, four unrelated words, easy to "
                    "type.",
                    "Nothing about you appears in it and nothing is "
                    "guessable.",
                ],
                "note": "Complexity rules made passwords hard for humans and "
                        "barely harder for software. Length is what works.",
            },
        },
        {
            "anchor": "s_manager",
            "label": "Letting software remember",
            "title": "Stop trying to remember",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "lock", "label": "One password to learn",
                     "sub": "You memorise one long phrase. The manager holds "
                            "every other password for you."},
                    {"icon": "cycle", "label": "Different everywhere",
                     "sub": "It generates a unique password per site, so a "
                            "breach anywhere affects nothing else."},
                    {"icon": "eye", "label": "It spots fakes",
                     "sub": "It will not fill your password into a lookalike "
                            "site, because the address does not match."},
                ],
            },
        },
        {
            "label": "Letting software remember",
            "title": "Where passwords must never live",
            "visual": {
                "type": "bandlist",
                "mark": "ban",
                "headline": "If it is written somewhere a colleague can read "
                            "it, it is not a password any more.",
                "sub": "Use the manager approved here: [COMPANY INPUT NEEDED: "
                       "approved password manager].",
                "cols": 2,
                "items": [
                    "A note under the keyboard or in a desk drawer",
                    "A spreadsheet called passwords, shared or not",
                    "A WhatsApp message to yourself or a colleague",
                    "An AI chat window, ever, for any reason",
                ],
            },
        },
        {
            "anchor": "s_do",
            "label": "Do this now",
            "title": "Do this now: check and change",
            "visual": {
                "type": "steps",
                "items": [
                    "Open the breach-check site listed in your toolkit.",
                    "Type your work email address. It tells you which breaches "
                    "included it.",
                    "If your work password matches any personal one, change it "
                    "today.",
                    "Set the new one as four unrelated words, and store it in "
                    "the manager.",
                ],
                "prompt": "Give me eight passphrases, each four unrelated "
                          "common English words joined by hyphens. No names, "
                          "no places, no dates, no themes connecting the "
                          "words. Numbered list, nothing else.",
                "caption": "Pick one you like the sound of. Never reuse one "
                           "shown to anybody.",
            },
        },
        {
            "label": "Do this now",
            "title": "If a password is exposed",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Change it on the work account first, then everywhere "
                    "else it was used.",
                    "Tell [COMPANY INPUT NEEDED: who to report a security "
                    "concern to] the same day.",
                    "Check your sent items and rules for anything you did not "
                    "create.",
                    "Do not wait to see whether anything happens. It already "
                    "has.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Five mistakes people really make",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Using a work password on a personal site",
                     "That site's security is now our security, and we have no "
                     "say in it."),
                    ("Sharing a login \"just for today\"",
                     "Shared logins remove any record of who did what, "
                     "permanently."),
                    ("Keeping a password because it is strong",
                     "Strength is irrelevant once it has leaked. Reuse is the "
                     "problem, not weakness."),
                    ("Storing passwords in the browser on a shared machine",
                     "Anyone who sits at that desk has every account you have "
                     "saved."),
                    ("Assuming an old account does not matter",
                     "The forgotten account is usually the one that leaked and "
                     "gave up the password."),
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Sharing an account is never fine",
            "visual": {
                "type": "tree",
                "question": "Does somebody else need access to this system?",
                "yes": {
                    "path": "Yes", "tone": "good", "label": "Get them an "
                                                           "account",
                    "detail": "Their own login, their own password. It takes a "
                              "day and it means every action has a name "
                              "against it if anything is ever questioned.",
                },
                "no": {
                    "path": "Sharing yours", "tone": "bad",
                    "label": "Never do this",
                    "detail": "Anything they do appears as you. If money "
                              "moves or data leaves, the record says you did "
                              "it, and you cannot prove otherwise.",
                },
            },
        },
        {
            "label": "Do this now",
            "title": "Four habits worth having",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "One password per account. Never a second use, anywhere.",
                    "Four unrelated words, not a word plus a number.",
                    "Let the manager remember them. Learn one phrase only.",
                    "Change it the day you hear of a breach, not the month "
                    "after.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "The password rule",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "Unique matters far more than complicated.",
                "sub": "A simple password used once is safer than a complex "
                       "one used twice.",
                "cols": 3,
                "items": [
                    "Unique — the only thing that stops reuse attacks.",
                    "Long — sixteen characters or more.",
                    "Stored — by software, not by memory.",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Tuesday, 9:15 am",
        "situation": "You get an alert that an old shopping site you used "
                     "years ago was breached. You are fairly sure you used a "
                     "similar password at work.",
        "choices": [
            {
                "text": "Ignore it — the site is nothing to do with work.",
                "tone": "bad",
                "headline": "The attacker does not care whose site it was",
                "consequence": "The leaked list contains your email address "
                               "and password. Software tries that pair against "
                               "hundreds of well-known services within days. "
                               "Your work login is one of them, and it is "
                               "still valid because nothing was changed.",
                "rule": "A breach anywhere is a breach here, if the password "
                        "was reused.",
            },
            {
                "text": "Change the work password today and report it.",
                "tone": "good",
                "headline": "Ten minutes, and the risk is closed",
                "consequence": "You change the work password to four unrelated "
                               "words and store it in the manager. You tell "
                               "the security contact so they can watch for "
                               "unusual sign-ins. Nothing further happens, "
                               "which is exactly the point.",
                "rule": "Change it first, then report it. Both, the same day.",
            },
            {
                "text": "Change it, but add a number to the end of the old "
                        "one.",
                "tone": "bad",
                "headline": "You changed almost nothing",
                "consequence": "The obvious variations are the first thing "
                               "attack software tries. Adding a digit or "
                               "swapping a letter for a symbol has been "
                               "standard in cracking tools for two decades. "
                               "The account is essentially as exposed as it "
                               "was.",
                "rule": "A new password means new words, not a new ending.",
            },
        ],
    },

    "video": {
        "url": "https://www.youtube.com/watch?v=xUp5S0nBnfc",
        "title": "How to make passwords more secure",
        "channel": "IBM Technology",
        "duration": "2:56",
        "heading": "Three minutes on stronger passwords",
        "note": "An outside video, not company material. Where it differs "
                "from this module, follow this module.",
        "how": [
            "Optional. The rules in this deck are what you need.",
            "Useful for background on how attacks actually work.",
            "It opens in your browser. Turn the sound on.",
        ],
    },

    "quiz": [
        {
            "q": "How do accounts usually get taken?",
            "remember": "Reused passwords from other breaches.",
            "answers": [
                {"text": "Someone guesses the password", "ok": False,
                 "why": "Almost never. Guessing is slow, usually blocked after "
                        "a few attempts, and unnecessary when millions of real "
                        "passwords are already available in leaked lists."},
                {"text": "A password leaked elsewhere is tried here", "ok": True,
                 "why": "This is the standard attack. Your email and password "
                        "from a breached site are tried automatically against "
                        "hundreds of services. If you reused it, one of them "
                        "works."},
                {"text": "The password was too short", "ok": False,
                 "why": "Length matters against guessing, which is rarely how "
                        "it happens. A twenty-character password that leaked "
                        "is just as usable to an attacker as a short one."},
                {"text": "Someone watched you type it", "ok": False,
                 "why": "It happens, and it is a tiny fraction of cases. The "
                        "overwhelming majority need nobody anywhere near your "
                        "desk."},
            ],
        },
        {
            "q": "Which password is strongest?",
            "remember": "Length and unrelated words beat symbols.",
            "answers": [
                {"text": "Nashik@2024", "ok": False,
                 "why": "A place name and a year, with the two most predictable "
                        "decorations. Every element of it appears in standard "
                        "cracking lists."},
                {"text": "copper-lantern-quiet-mango", "ok": True,
                 "why": "Twenty-six characters of unrelated words. Nothing "
                        "connects to you, nothing follows a pattern, and it is "
                        "far easier to type than eight random characters."},
                {"text": "P@ssw0rd!23", "ok": False,
                 "why": "The most substituted word in the world with the most "
                        "predictable substitutions. This is tried in the first "
                        "second of any attack."},
                {"text": "Xk9#mQ2", "ok": False,
                 "why": "Random but far too short, and impossible to remember, "
                        "so it ends up written down somewhere. Seven "
                        "characters is not enough regardless of what they are."},
            ],
        },
        {
            "q": "Why is reuse worse than weakness?",
            "remember": "A leak elsewhere becomes a key here.",
            "answers": [
                {"text": "Reused passwords are usually shorter", "ok": False,
                 "why": "Length is unrelated to reuse. A long, complex "
                        "password used on two sites carries exactly the same "
                        "risk as a short one."},
                {"text": "One breach anywhere hands over every account",
                 "ok": True,
                 "why": "Your work account becomes only as secure as the least "
                        "careful website you ever signed up to. You have no "
                        "visibility of their security and no control over it."},
                {"text": "Reuse makes passwords easier to guess", "ok": False,
                 "why": "Guessing is not involved. The attacker already has "
                        "the exact password — reuse simply means it opens more "
                        "than one door."},
                {"text": "It breaches company policy", "ok": False,
                 "why": "It usually does, and that is a consequence rather "
                        "than the reason. The reason is that it genuinely "
                        "hands your work account to whoever breached that "
                        "other site."},
            ],
        },
        {
            "q": "Where should passwords be stored?",
            "remember": "In a manager, not in your memory or a note.",
            "answers": [
                {"text": "In your memory, so nothing is written down",
                 "ok": False,
                 "why": "Memory forces reuse, because nobody remembers thirty "
                        "unique long passwords. The result is one password "
                        "everywhere, which is the actual risk."},
                {"text": "In an approved password manager", "ok": True,
                 "why": "You learn one long phrase and it holds a unique "
                        "password for every account. It also refuses to fill "
                        "your password into a lookalike site, which stops a "
                        "whole class of phishing."},
                {"text": "In a spreadsheet only you can open", "ok": False,
                 "why": "A file on a shared drive or laptop is readable by "
                        "anyone with access to that machine or backup, and it "
                        "gives no protection against fake sites."},
                {"text": "In your browser on any machine you use", "ok": False,
                 "why": "Acceptable on a personal device you alone use. On a "
                        "shared machine it hands every saved account to "
                        "whoever sits down next."},
            ],
        },
        {
            "q": "A colleague needs access today.",
            "remember": "Their own account, never yours.",
            "answers": [
                {"text": "Share your password just for today", "ok": False,
                 "why": "Everything they do is recorded as you. If data leaves "
                        "or money moves, the record names you, and you have no "
                        "way to show it was somebody else."},
                {"text": "Request an account for them", "ok": True,
                 "why": "It takes a day and it keeps every action traceable to "
                        "a person. That traceability is the entire reason "
                        "individual accounts exist."},
                {"text": "Share it and change it afterwards", "ok": False,
                 "why": "The window may be short and the record is still "
                        "wrong. Anything done during that period is attributed "
                        "to you permanently."},
                {"text": "Log in for them and leave the session open",
                 "ok": False,
                 "why": "Identical problem with an extra risk: an unattended "
                        "logged-in session is available to anyone who walks "
                        "past that desk."},
            ],
        },
    ],

    "recap": {
        "title": "Password security on one screen",
        "points": [
            ("Nobody guesses",
             "They use passwords that already leaked from other sites, tried "
             "automatically."),
            ("Reuse is the whole risk",
             "Your work account is as safe as the least careful site you ever "
             "joined."),
            ("Length beats symbols",
             "Four unrelated words beat eight clever characters, every time."),
            ("Small changes are not changes",
             "Adding a digit or swapping a letter is the first thing attackers "
             "try."),
            ("Let software remember",
             "One phrase you learn, and a unique password for everything else."),
            ("Never share a login",
             "Their actions become your record, and you cannot prove "
             "otherwise."),
        ],
        "oneliner": "Unique matters far more than complicated. A simple "
                    "password used once beats a complex one used twice.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("key", "The passphrase generator prompt",
             "Eight four-word phrases, no names, no dates."),
            ("eye", "The breach check",
             "Type your address and see which leaks included it."),
            ("shield", "The exposure checklist",
             "Change work first, report the same day, check your rules."),
        ],
        "links": [
            ("Check if your email has leaked", "https://haveibeenpwned.com"),
            ("India's data protection framework",
             "https://www.meity.gov.in/data-protection-framework"),
            ("UAE data protection laws", "https://u.ae/en/about-the-uae/"
                                         "digital-uae/data/data-protection-laws"),
        ],
        "next": "Next module: SEC-02, Phishing & Social Engineering. How "
                "people get talked into handing over the password in the first "
                "place.",
    },

    "glossary": [
        ("Credential stuffing", "Trying leaked email and password pairs "
                                "automatically against many services at once."),
        ("Breach", "A site losing its user list, usually including email "
                   "addresses and passwords."),
        ("Passphrase", "A password made of several unrelated words. Long, "
                       "memorable and hard to break."),
        ("Password manager", "Software that stores a unique password for every "
                             "account, behind one phrase you learn."),
        ("Shared account", "One login used by several people. It destroys any "
                           "record of who did what."),
        ("Multi-factor", "A second proof of identity beyond the password. "
                         "Covered in SEC-03."),
    ],
}
