# -*- coding: utf-8 -*-
"""SEC-04 — Data Protection Basics. Content only."""

DECK = {
    "module_code": "SEC-04",
    "area": "05-security-privacy",
    "filename": "05-04-data-protection-basics.pptx",
    "title": "Data Protection Basics",
    "subtitle": "What counts as personal data, what the law expects, and what "
                "that means for your inbox on an ordinary Tuesday.",
    "duration_min": 18,
    "audience": "Mandatory for all staff",
    "motif": "shield",
    "cover_image": "assets/hero-data-protection.jpg",

    "why": {
        "title": "Manoj forwards a list to his own email",
        "icon": "mail",
        "scenario": "Manoj handles sales admin in Kochi. He wants to finish a "
                    "report at home, so he forwards the customer contact list "
                    "to his personal email. Nothing bad happens. It is still "
                    "a reportable transfer of personal data out of the "
                    "company.",
        "cost": "A breach on paper, with no attacker and no bad intention.",
        "fix": "Four rules that cover almost every decision you will face.",
    },

    "outcomes": [
        ("person", "Say what counts as personal data, including the "
                   "surprising cases"),
        ("list", "Apply four rules that settle most day-to-day decisions"),
        ("ban", "Recognise the everyday habits that are technically breaches"),
        ("warn", "Know what triggers a reporting obligation, and how fast"),
        ("shield", "Handle a customer asking what data we hold on them"),
    ],

    "sections": [
        ("What counts as personal data", "Wider than you think", "s_what"),
        ("The four rules", "Enough for most decisions", "s_rules"),
        ("Everyday breaches", "No attacker required", "s_everyday"),
        ("When it goes wrong", "Reporting and the clock", "s_wrong"),
        ("Do this now", "Audit your own inbox", "s_do"),
        ("Choose what you'd do", "A Friday evening decision", "scenario"),
        ("Watch this", "A 3-minute regulator explainer", "video"),
    ],

    "slides": [
        {
            "anchor": "s_what",
            "label": "What counts as personal data",
            "title": "Wider than most people think",
            "lead": "If it points to one identifiable person, it is personal "
                    "data. A name is not required.",
            "gloss": ["Personal data"],
            "visual": {
                "type": "split",
                "left": {
                    "tag": "Obviously personal", "tone": "neutral",
                    "mark": "person",
                    "title": "Everyone gets these right",
                    "items": [
                        "Name, address and phone number",
                        "Email address and date of birth",
                        "Passport, Emirates ID or Aadhaar number",
                        "Salary, bank details and appraisal notes",
                    ],
                },
                "right": {
                    "tag": "Also personal", "tone": "bad",
                    "title": "The ones people miss",
                    "items": [
                        "A vehicle number plate on a gate pass",
                        "A photo of a person, or CCTV footage",
                        "An employee number with no name attached",
                        "A delivery address on its own",
                    ],
                },
            },
        },
        {
            "label": "What counts as personal data",
            "title": "Two laws, one habit",
            "gloss": ["DPDP Act"],
            "visual": {
                "type": "nested",
                "layers": [
                    {"label": "India — the DPDP Act",
                     "sub": "Consent, purpose limits, and breach notification."},
                    {"label": "UAE — federal data protection law",
                     "sub": "Similar principles, similar obligations on us."},
                    {"label": "What it means at your desk",
                     "sub": "Collect less, keep it inside, report fast."},
                ],
                "note": "You do not need to know the law in detail. You need "
                        "the four rules on the next slide, which is what both "
                        "of them come down to in practice.",
            },
        },
        {
            "anchor": "s_rules",
            "label": "The four rules",
            "title": "Four rules, most decisions",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "COLLECT LESS — if you do not need a field, do not ask for "
                    "it",
                    "USE IT FOR THE STATED PURPOSE — not for a new idea later",
                    "KEEP IT INSIDE — company systems only, never personal "
                    "accounts",
                    "DELETE IT WHEN DONE — old copies are the ones that leak",
                ],
            },
        },
        {
            "label": "The four rules",
            "title": "Collect less is the strongest",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "Collecting everything",
                "bad": [
                    "A visitor form asking for address, ID number and vehicle "
                    "details.",
                    "Kept in a folder for three years \"in case\".",
                    "Every one of those records is a liability with no "
                    "purpose.",
                ],
                "good_tag": "Collecting what is needed",
                "good": [
                    "Name, company, who they are visiting, time in and out.",
                    "Kept for the period we actually need, then destroyed.",
                    "Nothing held that we could not explain a reason for.",
                ],
                "note": "Data you never collected cannot leak, cannot be "
                        "requested and cannot be stolen. It is the only "
                        "perfect protection there is.",
            },
        },
        {
            "anchor": "s_everyday",
            "label": "Everyday breaches",
            "title": "No attacker required",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Forwarding a list to your personal email",
                     "Personal data has left our systems for one we cannot "
                     "audit, secure or delete."),
                    ("Using CC instead of BCC on a customer mailout",
                     "Every recipient now has every other customer's email "
                     "address."),
                    ("Leaving a printout on the shared printer",
                     "Anyone walking past has it. This is one of the most "
                     "common reported incidents."),
                    ("Keeping a spreadsheet from a project that ended in 2023",
                     "Still personal data, still our responsibility, and "
                     "nobody remembers it exists."),
                    ("Sending a file to the wrong Rajesh",
                     "Autocomplete picks the wrong contact. It happens weekly "
                     "somewhere in every company."),
                ],
            },
        },
        {
            "label": "Everyday breaches",
            "title": "The BCC habit",
            "visual": {
                "type": "bandlist",
                "mark": "ban",
                "headline": "One CC field on one mailout exposes every "
                            "customer address to every other customer.",
                "sub": "It is the single most common accidental disclosure "
                       "there is.",
                "cols": 3,
                "items": [
                    "More than one external recipient — use BCC.",
                    "Check the field before every send.",
                    "If in doubt, send them separately.",
                ],
            },
        },
        {
            "anchor": "s_wrong",
            "label": "When it goes wrong",
            "title": "The clock starts when you know",
            "lead": "Notification deadlines are measured from the moment "
                    "somebody in the company becomes aware. Not from when harm "
                    "appears.",
            "visual": {
                "type": "flow",
                "steps": [
                    ("Something goes wrong", "A wrong recipient, a lost "
                                             "laptop, a bad paste."),
                    ("You become aware", "The clock starts here, at this "
                                         "moment."),
                    ("You report it", "Same day, through the company's "
                                      "designated incident-reporting "
                                      "process, with what you know."),
                    ("They assess and notify", "Within the statutory window, "
                                               "if it qualifies."),
                ],
            },
        },
        {
            "label": "When it goes wrong",
            "title": "The report, ready to send",
            "visual": {
                "type": "prompt",
                "header": "Copy this wording",
                "text": "I need to report a possible data incident. What "
                        "happened: [one sentence]. When: [date and "
                        "approximate time]. What data was involved: [type and "
                        "rough number of people]. Who else knows: [names]. I "
                        "have not deleted anything. Please tell me what you "
                        "need from me next.",
                "caption": "Send it the same day. Incomplete and fast beats "
                           "complete and late.",
                "why": [
                    "\"I have not deleted anything\" matters — evidence is "
                    "needed.",
                    "A rough number is enough to start an assessment.",
                    "It ends with a question, so somebody has to respond.",
                ],
            },
        },
        {
            "anchor": "s_do",
            "label": "Do this now",
            "title": "Do this now: audit your inbox",
            "visual": {
                "type": "steps",
                "items": [
                    "Search your sent items for attachments sent outside the "
                    "company.",
                    "Search your personal email for anything work-related.",
                    "Delete work files from any personal account you find "
                    "them in.",
                    "Find one old spreadsheet of personal data and ask whether "
                    "we still need it.",
                ],
                "prompt": "I want to check whether a task involves personal "
                          "data. Ask me five short questions, one at a time, "
                          "then tell me whether it does and which of the four "
                          "handling rules apply. Do not ask me to paste any "
                          "actual data.",
                "caption": "Describe the task. Never paste the records "
                           "themselves.",
            },
        },
        {
            "label": "Do this now",
            "title": "When a customer asks what we hold",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Do not answer from memory, and do not delete anything.",
                    "Pass it to [COMPANY INPUT NEEDED: who handles data "
                    "requests] the same day.",
                    "Tell the customer it has been passed on and will be "
                    "answered.",
                    "Note the date they asked. The response clock has already "
                    "started.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Where data is allowed to live",
            "visual": {
                "type": "tree",
                "question": "Is this a company system somebody administers?",
                "yes": {
                    "path": "Yes", "tone": "good", "label": "Fine",
                    "detail": "Company email, the approved drive, the ERP, the "
                              "CRM. Backed up, access-controlled, and "
                              "deletable if we are ever asked.",
                },
                "no": {
                    "path": "No", "tone": "bad", "label": "Not allowed",
                    "detail": "Personal email, a personal cloud drive, a USB "
                              "stick, WhatsApp, an AI chat window. We cannot "
                              "secure it, audit it or delete it.",
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
                    "Check the To and CC fields before every external send.",
                    "Collect the minimum, and question any field you do not "
                    "use.",
                    "Never move work data to a personal account, for any "
                    "reason.",
                    "Delete old copies. They are the ones that leak.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "The data protection rule",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "Collect less, keep it inside, delete it when the "
                            "job is done.",
                "sub": "Three habits that cover the overwhelming majority of "
                       "what either law expects of you.",
                "cols": 3,
                "items": [
                    "Not collected — cannot leak.",
                    "Inside our systems — can be protected.",
                    "Deleted when done — no longer a risk.",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Friday, 6:15 pm",
        "situation": "You want to finish a customer report at home over the "
                     "weekend. The file has 300 customer names, phone numbers "
                     "and order values in it.",
        "choices": [
            {
                "text": "Email it to your personal address so you can open it "
                        "at home.",
                "tone": "bad",
                "headline": "A reportable transfer, with the best intentions",
                "consequence": "Three hundred people's details are now in an "
                               "account the company cannot secure, audit or "
                               "delete. If your personal email is ever "
                               "breached, so were they. Nothing bad has to "
                               "happen for this to be an incident.",
                "rule": "Good intentions do not change where the data ended "
                        "up.",
            },
            {
                "text": "Use the company's approved remote access from your "
                        "own laptop.",
                "tone": "good",
                "headline": "Same work, and the file never moves",
                "consequence": "You connect to the company system and work on "
                               "the file where it lives. Nothing is copied, "
                               "nothing leaves, and if a customer asks what we "
                               "hold on them next year, the answer is still "
                               "accurate.",
                "rule": "Move yourself to the data. Never move the data to "
                        "yourself.",
            },
            {
                "text": "Copy it to a USB stick and take that home instead.",
                "tone": "bad",
                "headline": "The same breach, in a more losable form",
                "consequence": "A USB stick is a company system that fits in a "
                               "pocket and has no password, no audit trail and "
                               "no backup. Lost sticks are among the most "
                               "common causes of reported data incidents "
                               "anywhere.",
                "rule": "A copy is a copy, whatever it is copied onto.",
            },
        ],
    },

    # Title, channel and runtime were read back from YouTube
    # itself. See newvideos.json.
    "video": {
        "url": "https://www.youtube.com/watch?v=YJInlE99vSs",
        "title": "Data protection explained in three minutes",
        "channel": "Information Commissioner's Office (ICO)",
        "duration": "2:54",
        "heading": "Three minutes from a regulator",
        "note": "From the UK's data protection regulator. The principles "
                "match India's DPDP Act and UAE law closely.",
        "how": [
            "Optional. Everything you need is already in this deck.",
            "Useful if you prefer watching to reading.",
            "It opens in your browser. Turn the sound on.",
        ],
    },

    "quiz": [
        {
            "q": "Which of these is personal data?",
            "remember": "Anything pointing to one identifiable person.",
            "answers": [
                {"text": "A vehicle number plate on a gate pass", "ok": True,
                 "why": "It identifies a vehicle, which identifies its keeper. "
                        "Number plates, employee numbers and delivery "
                        "addresses are all personal data even with no name "
                        "attached."},
                {"text": "The total number of visitors last month", "ok": False,
                 "why": "An aggregate figure with nobody identifiable in it. "
                        "Counts and totals are exactly what you should use "
                        "when you need to share something."},
                {"text": "Our published price list", "ok": False,
                 "why": "Commercial information, not personal data. It may be "
                        "confidential for other reasons, but no individual is "
                        "identifiable from it."},
                {"text": "The name of a supplier company", "ok": False,
                 "why": "A company is not a person. A named contact at that "
                        "company, with their direct line, certainly is."},
            ],
        },
        {
            "q": "Which rule prevents the most harm?",
            "remember": "Data you never collected cannot leak.",
            "answers": [
                {"text": "Encrypt everything", "ok": False,
                 "why": "Valuable and it protects data you are still holding. "
                        "It does nothing about the records you did not need to "
                        "collect in the first place."},
                {"text": "Collect less", "ok": True,
                 "why": "It is the only perfect protection. A field you never "
                        "asked for cannot leak, cannot be requested, cannot be "
                        "stolen and never needs deleting."},
                {"text": "Train everybody annually", "ok": False,
                 "why": "Necessary and insufficient on its own. Training "
                        "reduces mistakes; it does not reduce the amount of "
                        "data sitting there to be mistaken with."},
                {"text": "Keep backups of everything", "ok": False,
                 "why": "Backups protect against loss and increase your "
                        "exposure, because old copies of personal data are "
                        "exactly what leaks years later."},
            ],
        },
        {
            "q": "When does the reporting clock start?",
            "remember": "When you become aware.",
            "answers": [
                {"text": "When harm is confirmed", "ok": False,
                 "why": "Harm often never becomes visible, and waiting for it "
                        "is how deadlines get missed. The obligation does not "
                        "depend on anything actually going wrong."},
                {"text": "When somebody in the company becomes aware", "ok": True,
                 "why": "The moment you know is the moment the clock starts. "
                        "That is why reporting the same day matters, even when "
                        "you cannot answer every question yet."},
                {"text": "When the security team finishes investigating",
                 "ok": False,
                 "why": "They cannot start investigating until you tell them. "
                        "Delaying the report delays everything and eats the "
                        "window."},
                {"text": "When a customer complains", "ok": False,
                 "why": "Most incidents are never noticed by the people "
                        "affected. Waiting for a complaint means waiting for "
                        "the worst possible version of finding out."},
            ],
        },
        {
            "q": "A mailout to 200 customers. What field?",
            "remember": "BCC, every time.",
            "answers": [
                {"text": "CC, so everyone can see who else received it",
                 "ok": False,
                 "why": "That discloses every customer's email address to "
                        "every other customer, including competitors. It is "
                        "the most common accidental disclosure there is."},
                {"text": "BCC, so nobody sees any other address", "ok": True,
                 "why": "Each recipient sees only their own. Check the field "
                        "before you press send — this mistake is almost always "
                        "made in a hurry, not in ignorance."},
                {"text": "To, with all 200 addresses", "ok": False,
                 "why": "Identical exposure to CC, and it also looks careless. "
                        "Two hundred customers each receive a list of the "
                        "other 199."},
                {"text": "It does not matter for existing customers",
                 "ok": False,
                 "why": "Their email address is still their personal data, and "
                        "they did not consent to it being shared with your "
                        "other customers."},
            ],
        },
        {
            "q": "A customer asks what data we hold.",
            "remember": "Pass it on the same day. Delete nothing.",
            "answers": [
                {"text": "Answer from memory to be helpful", "ok": False,
                 "why": "You will be incomplete, and your answer becomes the "
                        "company's formal response. These requests have a "
                        "defined process for good reason."},
                {"text": "Pass it to the right person the same day",
                 "ok": True,
                 "why": "There is a statutory response period and it started "
                        "when they asked. Note the date, tell the customer it "
                        "has been passed on, and change nothing."},
                {"text": "Tidy up their record first, then respond", "ok": False,
                 "why": "Deleting or altering records after a request is a "
                        "serious matter in its own right, quite separate from "
                        "the original question."},
                {"text": "Ask them why they want it", "ok": False,
                 "why": "They do not have to say. Asking looks obstructive and "
                        "delays a clock that is already running."},
            ],
        },
    ],

    "recap": {
        "title": "Data protection on one screen",
        "points": [
            ("Personal data is wider than names",
             "Number plates, photos, employee numbers and addresses all "
             "count."),
            ("Collect less",
             "The only perfect protection. A field you never asked for cannot "
             "leak."),
            ("Keep it inside",
             "Company systems only. Never personal email, USB sticks or chat "
             "windows."),
            ("Delete when done",
             "Old copies from finished projects are what leak years later."),
            ("BCC, always",
             "One CC field exposes every customer address to every other "
             "customer."),
            ("Report the day you know",
             "The clock starts on awareness, not on harm. Incomplete and fast "
             "wins."),
        ],
        "oneliner": "Collect less, keep it inside, delete it when the job is "
                    "done.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("warn", "The incident report wording",
             "What, when, how many, who knows, nothing deleted."),
            ("list", "The four handling rules",
             "Collect less, stated purpose, keep inside, delete when done."),
            ("check", "The inbox audit",
             "Sent items, personal email, old spreadsheets."),
        ],
        "links": [
            ("India's data protection framework",
             "https://www.meity.gov.in/data-protection-framework"),
            ("UAE data protection laws", "https://u.ae/en/about-the-uae/"
                                         "digital-uae/data/data-protection-laws"),
            ("Check if your email has leaked", "https://haveibeenpwned.com"),
        ],
        "next": "Next module: SEC-05, Handling Confidential Information. The "
                "commercial material that is not personal data and still must "
                "not leave.",
    },

    "glossary": [
        ("Personal data", "Any information pointing to one identifiable "
                          "person, with or without a name attached."),
        ("DPDP Act", "India's Digital Personal Data Protection Act, covering "
                     "consent, purpose and breach notification."),
        ("Data minimisation", "Collecting only what you actually need. The "
                              "strongest protection available."),
        ("Data breach", "Personal data going somewhere it should not. No "
                        "attacker is required."),
        ("Subject access request", "A person asking what data we hold about "
                                   "them. It has a legal response period."),
        ("Retention", "How long we keep something. Old copies are the ones "
                      "that cause incidents."),
    ],
}
