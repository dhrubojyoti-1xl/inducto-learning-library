# -*- coding: utf-8 -*-
"""SEC-02 — Phishing & Social Engineering. Content only."""

DECK = {
    "module_code": "SEC-02",
    "area": "05-security-privacy",
    "filename": "05-02-phishing-and-social-engineering.pptx",
    "title": "Phishing & Social Engineering",
    "subtitle": "How people get talked into handing over the password, the "
                "payment or the file — and the pause that stops it.",
    "duration_min": 18,
    "audience": "Mandatory for all staff",
    "motif": "shield",

    "why": {
        "title": "Rekha pays the wrong bank account",
        "icon": "warn",
        "scenario": "Rekha handles accounts payable in Gurugram. An email "
                    "arrives from a regular supplier saying their bank details "
                    "have changed. The signature, the logo and the invoice "
                    "format are all correct. She updates the record and pays.",
        "cost": "One payment, to an account nobody at that supplier controls.",
        "fix": "One phone call to a number you already had. That is the whole "
               "defence.",
    },

    "outcomes": [
        ("eye", "Name the four pressure signals that appear in almost every "
                "attack"),
        ("chat", "Use one verification habit that defeats a convincing email"),
        ("warn", "Recognise an attack that arrives by phone or WhatsApp"),
        ("ban", "Know why a real-looking sender proves nothing at all"),
        ("shield", "Report a suspected attempt without worrying about being "
                   "wrong"),
    ],

    "sections": [
        ("It is not about spelling", "Modern attacks look perfect", "s_look"),
        ("The four pressure signals", "What every attack needs", "s_signals"),
        ("The verification habit", "One call, a number you had", "s_verify"),
        ("Phone, WhatsApp and in person", "Not just email", "s_channels"),
        ("Do this now", "Test one real message", "s_do"),
        ("Choose what you'd do", "A Thursday afternoon decision", "scenario"),
        ("Watch this", "A 9-minute outside guide", "video"),
    ],

    "slides": [
        {
            "anchor": "s_look",
            "label": "It is not about spelling",
            "title": "They do not look wrong any more",
            "lead": "The badly spelled email is twenty years out of date. "
                    "Modern attempts are copied from real correspondence.",
            "visual": {
                "type": "split",
                "left": {
                    "tag": "What we teach people", "tone": "neutral",
                    "mark": "search",
                    "title": "Look for the mistakes",
                    "items": [
                        "Poor spelling and odd grammar",
                        "A strange-looking email address",
                        "Generic greetings like \"Dear Customer\"",
                        "Obviously fake logos",
                    ],
                },
                "right": {
                    "tag": "What actually arrives", "tone": "bad",
                    "title": "Copied from the real thing",
                    "items": [
                        "Perfect English, often AI-written",
                        "A real display name, sometimes a real address",
                        "Your name, your order number, your supplier",
                        "The exact logo and invoice layout",
                    ],
                },
            },
        },
        {
            "label": "It is not about spelling",
            "title": "A sender name proves nothing",
            "visual": {
                "type": "flow",
                "steps": [
                    ("The name is typed in", "Display names are free text. "
                                             "Anyone can put anything there."),
                    ("The address can be close", "One character different, "
                                                 "or a lookalike domain."),
                    ("Replies go elsewhere", "The reply-to address can differ "
                                             "from the one shown."),
                    ("So looking is not checking", "Only a separate channel "
                                                   "actually verifies."),
                ],
            },
        },
        {
            "anchor": "s_signals",
            "label": "The four pressure signals",
            "title": "Four signals in every attack",
            "lead": "Attacks do not need you to be careless. They need you to "
                    "be busy and to feel pushed.",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "mark": "ban",
                "items": [
                    "URGENCY — today, before close, immediately",
                    "AUTHORITY — from a director, a bank, a regulator",
                    "SECRECY — do not discuss this with the team yet",
                    "A CHANGE — new bank details, new address, new process",
                ],
            },
        },
        {
            "label": "The four pressure signals",
            "title": "One is enough to make you check",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "shield", "label": "A change, on its own, "
                     "is reason enough",
                     "sub": "New bank details, a new process, a new address — "
                            "verify that alone, even with no urgency and no "
                            "pressure attached to it."},
                    {"icon": "clock", "label": "Urgency plus authority",
                     "sub": "\"The director needs this paid before five.\" A "
                            "common combination, and an easy one to notice."},
                    {"icon": "lock", "label": "Secrecy plus a change",
                     "sub": "\"Do not mention this yet — the new account is "
                            "confidential.\" Nothing legitimate needs both."},
                ],
            },
        },
        {
            "anchor": "s_verify",
            "label": "The verification habit",
            "title": "One call, a number you had",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "Verifying inside the message",
                "bad": [
                    "You ring the number in the email signature.",
                    "You reply to the email asking \"is this really you?\"",
                    "Both reach whoever sent it. Confirmation is worthless.",
                ],
                "good_tag": "Verifying outside it",
                "good": [
                    "You ring the number already in your contacts or on the "
                    "invoice you had before.",
                    "You walk to the person's desk, or message them on Teams.",
                    "Any channel they did not choose defeats the whole "
                    "attempt.",
                ],
                "note": "The rule is not \"verify\". It is \"verify somewhere "
                        "the sender does not control\".",
            },
        },
        {
            "label": "The verification habit",
            "title": "The wording, ready to use",
            "visual": {
                "type": "prompt",
                "header": "Copy this wording",
                "text": "Hello, I have an email asking me to change the bank "
                        "details on your account. Before I touch anything I "
                        "need to confirm it with you directly. Can you confirm "
                        "whether that request came from your side? I am "
                        "calling the number we already had on file.",
                "caption": "Nobody legitimate has ever been offended by this "
                           "call.",
                "why": [
                    "It states plainly that you are using an old number.",
                    "It asks a yes-or-no question they can answer in seconds.",
                    "It costs two minutes and stops the entire attack.",
                ],
            },
        },
        {
            "anchor": "s_channels",
            "label": "Phone, WhatsApp and in person",
            "title": "Not only email",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("A call from \"IT support\"",
                     "Asking you to read out a code or install a remote-access "
                     "tool. Nobody real does this."),
                    ("A WhatsApp from your manager's \"new number\"",
                     "Urgent, brief, and asking for a payment or a gift card. "
                     "Ring the old number."),
                    ("A visitor who follows you through the door",
                     "Holding boxes and looking rushed. Politely ask them to "
                     "sign in at reception."),
                    ("A supplier asking for a document \"resent\"",
                     "Testing whether you will send a file to a new address "
                     "without checking."),
                ],
            },
        },
        {
            "label": "Phone, WhatsApp and in person",
            "title": "The code that is never shared",
            "visual": {
                "type": "bandlist",
                "mark": "ban",
                "headline": "Nobody legitimate will ever ask you to read out a "
                            "one-time code.",
                "sub": "Not IT, not the bank, not a director, not a supplier. "
                       "There is no exception.",
                "cols": 3,
                "items": [
                    "A code on your phone stays on your phone.",
                    "Anyone asking for it is attacking you.",
                    "Report it, even if you did not give it.",
                ],
            },
        },
        {
            "anchor": "s_do",
            "label": "Do this now",
            "title": "Do this now: test one message",
            "visual": {
                "type": "steps",
                "items": [
                    "Open the last message that asked you to do something "
                    "financial.",
                    "Count how many of the four pressure signals it contains.",
                    "Find a number for the sender that did not come from the "
                    "message.",
                    "If you cannot find one independently, that is your "
                    "answer.",
                ],
                "prompt": "I received a message asking me to act. Ask me six "
                          "short questions, one at a time, to work out whether "
                          "it shows signs of a phishing or impersonation "
                          "attempt. Do not ask me to paste the message. At the "
                          "end give me a verdict and one action.",
                "caption": "Describe the message. Never paste it, and never "
                           "paste any attachment.",
            },
        },
        {
            "label": "Do this now",
            "title": "If you already clicked",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Disconnect from the network, but do not switch the "
                    "machine off.",
                    "Change the password from a different device.",
                    "Tell [COMPANY INPUT NEEDED: who to report a security "
                    "concern to] within the hour.",
                    "Say exactly what you clicked and what you typed. All of "
                    "it.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Reporting a false alarm is free",
            "visual": {
                "type": "tree",
                "question": "Am I sure enough to be worth someone's time?",
                "yes": {
                    "path": "Not sure", "tone": "good", "label": "Report it "
                                                                "anyway",
                    "detail": "A false alarm costs somebody two minutes. A "
                              "real attempt that nobody reported costs "
                              "considerably more, and usually arrives at four "
                              "other people's desks as well.",
                },
                "no": {
                    "path": "Certain it is fake", "tone": "good",
                    "label": "Report it and delete",
                    "detail": "Reporting matters even when you spotted it. If "
                              "it reached you, it reached colleagues, and some "
                              "of them are busier than you were.",
                },
            },
        },
        {
            "label": "Do this now",
            "title": "Why smart people get caught",
            "visual": {
                "type": "nested",
                "layers": [
                    {"label": "It arrives when you are busy",
                     "sub": "Late afternoon, month end, during a deadline."},
                    {"label": "It looks completely routine",
                     "sub": "A supplier you know, an invoice you expected."},
                    {"label": "It asks for one small thing",
                     "sub": "Update a field, confirm a code, resend a file."},
                ],
                "note": "Nobody is caught by an obvious scam. People are "
                        "caught by an ordinary request on a busy afternoon, "
                        "which is exactly what these are designed to be.",
            },
        },
        {
            "label": "Do this now",
            "title": "The phishing rule",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "Anything that changes where money or data goes "
                            "gets verified on a channel the sender did not "
                            "choose.",
                "sub": "That single habit defeats nearly every version of this "
                       "attack.",
                "cols": 3,
                "items": [
                    "Bank details change — call an old number.",
                    "Urgent and secret — verify twice.",
                    "One-time code requested — report it.",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Thursday, 4:30 pm",
        "situation": "An email from a regular supplier says their bank details "
                     "have changed and an overdue invoice needs paying today. "
                     "The layout, logo and signature all look exactly right.",
        "choices": [
            {
                "text": "Reply to the email asking them to confirm the new "
                        "details.",
                "tone": "bad",
                "headline": "You asked the attacker whether they are real",
                "consequence": "The reply goes wherever the sender chose. "
                               "Within ten minutes you have a polite "
                               "confirmation, possibly with a scanned letter "
                               "attached. You now feel more confident than "
                               "before, which is precisely the point of the "
                               "exchange.",
                "rule": "Never verify inside the channel the request arrived "
                        "on.",
            },
            {
                "text": "Ring the supplier on the number you already had on "
                        "file.",
                "tone": "good",
                "headline": "Two minutes, and the attack ends",
                "consequence": "The number from your existing records reaches "
                               "the real supplier, who confirms they have not "
                               "changed anything. You report the email, and "
                               "the same message is found sitting in three "
                               "other inboxes.",
                "rule": "Use a number you had before the message arrived.",
            },
            {
                "text": "Pay it — the invoice is genuinely overdue and it "
                        "looks right.",
                "tone": "bad",
                "headline": "The money leaves and does not come back",
                "consequence": "The payment reaches an account nobody at the "
                               "supplier controls. Recovery depends on how "
                               "fast the bank is told, and after a few hours "
                               "it is usually gone. The real invoice is still "
                               "outstanding.",
                "rule": "Overdue is pressure. Pressure is one of the four "
                        "signals.",
            },
        ],
    },

    # Title, channel and runtime were read back from YouTube
    # itself. See newvideos.json.
    "video": {
        "url": "https://www.youtube.com/watch?v=UuLjQ-LWM9Y",
        "title": "How to Spot Phishing Emails | Cyber Security Awareness "
                 "for Employees",
        "channel": "UK Cyber Hub",
        "duration": "8:51",
        "heading": "Nine minutes on spotting them",
        "note": "An outside video using UK examples. The signals are "
                "identical here; the reporting route is ours.",
        "how": [
            "Optional. Everything you need is already in this deck.",
            "Useful if you prefer watching to reading.",
            "It opens in your browser. Turn the sound on.",
        ],
    },

    "quiz": [
        {
            "q": "What proves an email is genuine?",
            "remember": "Nothing inside the message.",
            "answers": [
                {"text": "The sender's name and address look right", "ok": False,
                 "why": "Display names are free text and addresses can be "
                        "lookalikes or genuinely compromised. Looking right is "
                        "the entire design goal of the message."},
                {"text": "Nothing in the message. Only a separate channel",
                 "ok": True,
                 "why": "Every element of an email can be copied or "
                        "controlled by the sender. A phone call to a number "
                        "you already had is outside their control, which is "
                        "why it works."},
                {"text": "The logo and invoice format match exactly",
                 "ok": False,
                 "why": "Those are copied from real correspondence, often from "
                        "a genuine earlier email. A perfect match is evidence "
                        "of effort, not of authenticity."},
                {"text": "They knew your order number", "ok": False,
                 "why": "Order numbers appear in emails, attachments and "
                        "sometimes breached systems. Knowing details makes the "
                        "message convincing, not legitimate."},
            ],
        },
        {
            "q": "Which of these is reason enough to verify, on its own?",
            "remember": "A change to where money or data goes — no second signal needed.",
            "answers": [
                {"text": "A request to change bank details or payment "
                         "instructions", "ok": True,
                 "why": "A change is reason enough by itself. It does not need "
                        "urgency or secrecy attached to it — waiting for a "
                        "second signal before verifying is exactly the gap "
                        "this kind of attack is built to use."},
                {"text": "A long email with an attachment", "ok": False,
                 "why": "Perfectly normal in most jobs. Length and attachments "
                        "are not signals in themselves."},
                {"text": "An email arriving late in the day", "ok": False,
                 "why": "Timing alone is not a signal, although attacks do "
                        "favour busy periods. It matters only alongside an "
                        "actual pressure signal such as a change."},
                {"text": "A supplier you have not heard from recently",
                 "ok": False,
                 "why": "Common and usually innocent. What matters is whether "
                        "they are asking you to change where money or data "
                        "goes."},
            ],
        },
        {
            "q": "Who may ask for a one-time code?",
            "remember": "Nobody. There is no exception.",
            "answers": [
                {"text": "Your IT team, when fixing your account", "ok": False,
                 "why": "They never need it. IT can reset access through their "
                        "own systems, and any request for a code from you is "
                        "somebody impersonating them."},
                {"text": "Nobody — not IT, your bank, or your manager",
                 "ok": True,
                 "why": "The code exists to prove it is you. Anyone asking you "
                        "to read it out is asking you to prove you are them. "
                        "There is no legitimate version of that request."},
                {"text": "Your bank's fraud department", "ok": False,
                 "why": "This is the single most common impersonation there "
                        "is. Real banks state clearly that they will never ask "
                        "for a code, and attackers rely on you not "
                        "remembering that."},
                {"text": "Your manager, if it is urgent", "ok": False,
                 "why": "Urgency plus authority is the classic pairing. A "
                        "manager has no reason to need your code, and a real "
                        "one will understand completely when you decline."},
            ],
        },
        {
            "q": "You clicked. What comes first?",
            "remember": "Disconnect, change password elsewhere, report within "
                        "the hour.",
            "answers": [
                {"text": "Switch the machine off immediately", "ok": False,
                 "why": "Powering off can destroy information the security "
                        "team needs to see what happened. Disconnect from the "
                        "network instead and leave it running."},
                {"text": "Disconnect from the network and report it within the "
                         "hour", "ok": True,
                 "why": "Disconnecting stops anything in progress, keeping it "
                        "powered preserves evidence, and reporting quickly is "
                        "what turns an incident into a contained one."},
                {"text": "Wait to see whether anything odd happens", "ok": False,
                 "why": "Nothing visible will happen, and the useful window "
                        "closes. By the time something is obvious, credentials "
                        "have been used elsewhere."},
                {"text": "Delete the email so nobody else clicks", "ok": False,
                 "why": "You have removed the evidence and left the copies in "
                        "everyone else's inbox. Report it first — that is what "
                        "gets it pulled from other mailboxes."},
            ],
        },
        {
            "q": "Should you report a false alarm?",
            "remember": "Yes. It costs two minutes.",
            "answers": [
                {"text": "No — it wastes the security team's time", "ok": False,
                 "why": "Two minutes of theirs against a possible incident is "
                        "not a close call. Teams would far rather see ten "
                        "false alarms than miss one real attempt."},
                {"text": "Yes, always. The cost of being wrong is tiny",
                 "ok": True,
                 "why": "If it reached you it reached colleagues, some busier "
                        "than you. Reporting is what gets it removed from "
                        "other inboxes before somebody acts on it."},
                {"text": "Only if you clicked something", "ok": False,
                 "why": "Reporting the attempt matters even when you spotted "
                        "it perfectly. The value is in warning everyone else "
                        "who received the same thing."},
                {"text": "Only if it involves money", "ok": False,
                 "why": "Credential and document requests are just as serious, "
                        "and are usually the first step towards the payment "
                        "request that follows."},
            ],
        },
    ],

    "recap": {
        "title": "Phishing on one screen",
        "points": [
            ("They do not look wrong",
             "Perfect English, real logos, your order number. Spelling is not "
             "the test."),
            ("Four pressure signals",
             "Urgency, authority, secrecy, a change. One alone is reason enough to verify."),
            ("Verify outside the channel",
             "A number you already had, not one from the message."),
            ("Never a one-time code",
             "Nobody legitimate asks. There is genuinely no exception."),
            ("If you clicked, disconnect and report",
             "Leave it powered on, change the password elsewhere, report "
             "within the hour."),
            ("Report false alarms too",
             "It reached your colleagues as well, and some of them are "
             "busier."),
        ],
        "oneliner": "Anything that changes where money or data goes gets "
                    "verified on a channel the sender did not choose.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("chat", "The verification call wording",
             "Confirms directly, on a number you already had."),
            ("list", "The four-signal check",
             "Urgency, authority, secrecy, a change. Any one alone is "
             "reason enough."),
            ("shield", "The first-hour checklist",
             "Disconnect, change elsewhere, report within the hour."),
        ],
        "links": [
            ("Check if your email has leaked", "https://haveibeenpwned.com"),
            ("India's data protection framework",
             "https://www.meity.gov.in/data-protection-framework"),
            ("UAE data protection laws", "https://u.ae/en/about-the-uae/"
                                         "digital-uae/data/data-protection-laws"),
        ],
        "next": "Next module: SEC-03, Multi-Factor Authentication. The second "
                "lock that makes a stolen password nearly useless.",
    },

    "glossary": [
        ("Phishing", "A message designed to make you hand over access, money "
                     "or a document."),
        ("Social engineering", "Manipulating a person rather than attacking a "
                               "system. The pressure signals are the tools."),
        ("Spoofing", "Making a message appear to come from somebody else. "
                     "Display names are free text."),
        ("Business email compromise", "An attacker using a real or lookalike "
                                      "account to redirect a payment."),
        ("One-time code", "A short code proving it is you. Never shared with "
                          "anyone, for any reason."),
        ("Out-of-band", "Checking through a different channel the sender does "
                        "not control."),
    ],
}
