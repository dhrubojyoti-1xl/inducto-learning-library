# -*- coding: utf-8 -*-
"""SEC-07 — What you must never paste into an AI tool. Content only."""

DECK = {
    "module_code": "SEC-07",
    "area": "05-security-privacy",
    "filename": "05-07-never-paste-into-ai.pptx",
    "title": "What Never to Paste Into AI",
    "subtitle": "The five red lines, the two-second test, and exactly what to "
                "type instead when you are in a hurry.",
    "duration_min": 16,
    "audience": "Mandatory for all staff",
    "motif": "shield",
    "cover_image": "assets/hero-safe-ai-use.jpg",

    "why": {
        "title": "One paste, and it is out of our hands",
        "icon": "lock",
        "scenario": "Farhan in accounts needs a payment-reminder letter. He "
                    "pastes the customer ageing report — 340 names, phone "
                    "numbers and outstanding amounts — into a free AI site. "
                    "The letter that comes back is excellent. The report is "
                    "now on a server we do not control.",
        "cost": "We cannot retrieve it, cannot delete it, and cannot tell an "
                "auditor where it went.",
        "fix": "You will know in two seconds whether something is safe to "
               "paste — and exactly what to type instead.",
    },

    "outcomes": [
        ("ban", "Name the five kinds of information that must never go into an "
                "AI tool"),
        ("shield", "Strip a real request down to facts that are safe to share, "
                   "in under a minute"),
        ("eye", "Tell an approved tool from a personal account at a glance"),
        ("warn", "Explain what actually happens after a bad paste, not just "
                 "that it is banned"),
        ("key", "Know what to do in the first hour if you have already pasted "
                "something"),
    ],

    "sections": [
        ("The five red lines", "What never goes in, and why", "s_lines"),
        ("What goes wrong", "The part people do not expect", "s_why"),
        ("Strip it down", "Turn a file into safe facts", "s_strip"),
        ("Approved or personal?", "The account changes everything", "s_tool"),
        ("If you already have", "The first hour matters most", "s_oops"),
        ("Choose what you'd do", "A Thursday afternoon deadline", "scenario"),
        ("Watch this", "A 7-minute outside warning", "video"),
    ],

    "slides": [
        # ---------------- The five red lines ----------------
        {
            "anchor": "s_lines",
            "label": "The five red lines",
            "title": "Five things that never go in",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Customer or employee personal data",
                     "Names with phone numbers, addresses, ID numbers, "
                     "salaries. This is the one regulators count."),
                    ("Anything lifted from a signed contract",
                     "Prices, terms, penalty clauses. The client agreed to "
                     "share those with us, not with a third party."),
                    ("Financial records and pricing",
                     "Margins, cost sheets, bank details, unpublished "
                     "results. A competitor would pay for these."),
                    ("Login details of any kind",
                     "Passwords, API keys, one-time codes. A prompt box is "
                     "not a password manager."),
                    ("Anything marked confidential or internal",
                     "Board papers, legal advice, unannounced plans. If it "
                     "carries a marking, the marking is your answer."),
                ],
            },
        },
        {
            "label": "The five red lines",
            "title": "Why one paste is hard to undo",
            "lead": "People expect a paste to behave like a draft email they "
                    "can unsend. It does not.",
            "visual": {
                "type": "flow",
                "steps": [
                    ("You paste", "The text leaves your laptop and travels to "
                                  "the tool's servers."),
                    ("It is stored", "Most services keep the conversation. "
                                     "Free accounts usually keep it longest."),
                    ("It may be reused", "On consumer accounts, chats can be "
                                         "used to improve the service unless "
                                         "you switch that off."),
                    ("You cannot recall it", "No delete button reaches every "
                                             "copy. This is the part people "
                                             "do not expect."),
                ],
            },
        },

        # ---------------- What goes wrong ----------------
        {
            "anchor": "s_why",
            "label": "What goes wrong",
            "title": "What actually goes wrong",
            "gloss": ["Data breach", "DPDP Act"],
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "warn", "label": "A reportable incident",
                     "sub": "Under India's DPDP Act and UAE data protection "
                            "law, personal data leaving our control is an "
                            "incident we may be required to report."},
                    {"icon": "person", "label": "A client relationship",
                     "sub": "Clients ask how their data is handled. \"An "
                            "employee pasted it into a chatbot\" is not an "
                            "answer that survives a renewal meeting."},
                    {"icon": "eye", "label": "It can resurface",
                     "sub": "Text used for training can, rarely, appear in "
                            "another user's answer. You have no way to check "
                            "whether yours did."},
                ],
            },
        },
        {
            "label": "What goes wrong",
            "title": "The test that takes two seconds",
            "visual": {
                "type": "tree",
                "question": "Could this text identify a person or a customer?",
                "yes": {
                    "path": "Yes", "tone": "bad", "label": "Do not paste it",
                    "detail": "Take out the names, numbers and addresses "
                              "first, or describe the situation in your own "
                              "words instead. The tool does not need to know "
                              "who it is to write well.",
                },
                "no": {
                    "path": "No", "tone": "good", "label": "Safe to paste",
                    "detail": "Dates, quantities, reasons, general "
                              "descriptions. Everything it needs to write "
                              "with, and nothing that could harm anyone if it "
                              "leaked tomorrow.",
                },
            },
        },

        # ---------------- Strip it down ----------------
        {
            "anchor": "s_strip",
            "label": "Strip it down",
            "title": "Turn a file into safe facts",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "What Farhan pasted",
                "bad": [
                    "The full ageing report: 340 rows with names, phone "
                    "numbers, credit limits and outstanding amounts.",
                    "Plus the covering note naming the two largest "
                    "defaulters.",
                    "Every one of those names is now outside the company, "
                    "permanently.",
                ],
                "good_tag": "What he should have typed",
                "good": [
                    "\"Write a firm payment-reminder letter for an invoice 45 "
                    "days overdue.\"",
                    "\"Second reminder. Long-standing client, we want to keep "
                    "the relationship.\"",
                    "Nothing identifying anyone — and the letter that comes "
                    "back is just as good.",
                ],
                "note": "The tool never needed the names. It only ever needed "
                        "the situation.",
            },
        },
        {
            "label": "Strip it down",
            "title": "Do this now: strip a real request",
            "visual": {
                "type": "steps",
                "items": [
                    "Open something you were genuinely about to paste this "
                    "week.",
                    "Delete every name, phone number, address and ID number.",
                    "Replace exact amounts with a range, and exact dates with "
                    "\"45 days overdue\".",
                    "Paste what is left. Add the real details yourself "
                    "afterwards, in Outlook.",
                ],
                "prompt": "Write a firm but polite payment reminder for an "
                          "invoice that is 45 days overdue. This is the second "
                          "reminder. The client is long-standing and we want "
                          "to keep the relationship. Under 130 words. Include "
                          "one clear sentence asking them to confirm a payment "
                          "date.",
                "caption": "No name, no invoice number, no amount. It still "
                           "writes the whole letter.",
            },
        },
        {
            "label": "Strip it down",
            "title": "Say it in your own words instead",
            "lead": "Describing a situation takes about fifteen seconds and "
                    "removes the risk entirely.",
            "visual": {
                "type": "prompt_out",
                "text": "I need to reply to a customer complaint. A delivery "
                        "arrived three days late and two cartons were damaged. "
                        "We accept the delay. We want to offer a replacement "
                        "for the damaged cartons but not a discount. Draft a "
                        "120-word reply, apologetic but not grovelling.",
                "caption": "Everything the tool needs. Nothing it should not "
                           "have.",
                "out_title": "What comes back",
                "out": [
                    "A complete reply covering the delay, the damage and the "
                    "replacement offer.",
                    "No customer name, no invoice number and no address went "
                    "in — because none of it was needed.",
                    "You add the name yourself, in Outlook, where it belongs.",
                ],
            },
        },

        # ---------------- Approved or personal ----------------
        {
            "anchor": "s_tool",
            "label": "Approved or personal?",
            "title": "Approved account or personal?",
            "gloss": ["Approved tool"],
            "visual": {
                "type": "split",
                "left": {
                    "tag": "Personal account", "tone": "bad",
                    "title": "Your own login on a free AI site",
                    "items": [
                        "Chats are usually kept, and may be used to improve "
                        "the service",
                        "The company has no record of what was shared",
                        "Nobody can delete it on your behalf",
                        "If it goes wrong, it traces back to you personally",
                    ],
                },
                "right": {
                    "tag": "Approved account", "tone": "good",
                    "title": "[COMPANY INPUT NEEDED: name of the approved AI "
                             "tool]",
                    "items": [
                        "Signed in with your work account, under a company "
                        "agreement",
                        "Covered by terms somebody here has actually read",
                        "Data handling is known and can be explained to a "
                        "client",
                        "Real support exists if something is pasted by mistake",
                    ],
                },
            },
        },
        {
            "label": "Approved or personal?",
            "title": "Signs you are in the wrong place",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "You signed in with a personal email rather than your work "
                    "address.",
                    "There is no company logo and no single sign-on screen.",
                    "The site offered you a free trial, or asked for a card.",
                    "You found it through a search result or a social media "
                    "post.",
                ],
            },
        },

        # ---------------- If you already have ----------------
        {
            "anchor": "s_oops",
            "label": "If you already have",
            "title": "If you have already pasted",
            "lead": "The first hour is worth more than the next month. Here is "
                    "the whole procedure.",
            "visual": {
                "type": "steps",
                "items": [
                    "Stop. Do not delete the conversation — it may be needed "
                    "as a record.",
                    "Write down what you pasted, into which tool, and roughly "
                    "when.",
                    "Tell your manager and [COMPANY INPUT NEEDED: who to "
                    "report a data incident to] the same day.",
                    "If it involved customer or staff data, say so plainly. "
                    "The reporting clock may already be running.",
                ],
            },
        },
        {
            "label": "If you already have",
            "title": "Reporting early is not the problem",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "Nearly every incident that became serious became "
                            "serious because somebody waited.",
                "sub": "The paste is recoverable. The silence afterwards "
                       "usually is not.",
                "cols": 3,
                "items": [
                    "An hour after the paste, real options still exist.",
                    "A month later, the only option is explaining it to the "
                    "client.",
                    "[COMPANY INPUT NEEDED: the company's stated position on "
                    "reporting your own mistake]",
                ],
            },
        },
        {
            "label": "If you already have",
            "title": "Four habits that keep you clear",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Type facts, never paste files. If your hand is reaching "
                    "for Ctrl+V, stop.",
                    "Strip names before anything else. Names are what "
                    "regulators actually count.",
                    "Use the work account every time, even for a \"quick\" "
                    "question.",
                    "If you would not read it aloud in a client's office, do "
                    "not paste it.",
                ],
            },
        },
        {
            "label": "If you already have",
            "title": "What is fine to paste",
            "lead": "This module is not asking you to stop using AI. Most of "
                    "what you need help with is perfectly safe.",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "doc", "label": "Your own draft",
                     "sub": "Something you wrote yourself, names removed. Ask "
                            "it to shorten it, or fix the English."},
                    {"icon": "search", "label": "Public information",
                     "sub": "A published circular, a public spec sheet, "
                            "anything already sitting on the open internet."},
                    {"icon": "chat", "label": "A situation, described",
                     "sub": "\"A delivery was three days late and two cartons "
                            "were damaged.\" No names, and no meaning lost."},
                ],
            },
        },
        {
            "label": "If you already have",
            "title": "The one-line test",
            "visual": {
                "type": "bandlist",
                "mark": "list",
                "headline": "Would I be comfortable if this exact text landed "
                            "in a competitor's inbox tomorrow?",
                "sub": "If the answer is anything other than a clear yes, it "
                       "does not go in.",
                "cols": 3,
                "items": [
                    "A clear yes — paste it and carry on.",
                    "Not sure — strip the names, then ask yourself again.",
                    "No — describe the situation in your own words instead.",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Thursday, 3:20 pm",
        "situation": "A tender response is due at 6. The approved assistant on "
                     "your laptop is down. The tender document runs to 40 "
                     "pages and you need the eligibility criteria summarised.",
        "choices": [
            {
                "text": "Open a free AI site on your phone with your personal "
                        "login and paste the tender in.",
                "tone": "bad",
                "headline": "The fastest route to a reportable incident",
                "consequence": "The tender carries our pricing approach, our "
                               "client references and the authority's terms. "
                               "It now sits in a personal account, under an "
                               "agreement nobody here has read, with no record "
                               "that it happened. The deadline was met. The "
                               "problem was not.",
                "rule": "A deadline is not an exception. No deadline has ever "
                        "been worth an uncontrolled disclosure.",
            },
            {
                "text": "Read the eligibility section yourself — it is four "
                        "pages out of forty.",
                "tone": "good",
                "headline": "Twelve minutes, and no exposure at all",
                "consequence": "Eligibility criteria are almost always one "
                               "short section. You read four pages, list the "
                               "six criteria, and use the assistant only to "
                               "tidy the wording of the six lines you typed "
                               "yourself. No document ever left your control.",
                "rule": "Ask the tool for wording. Do the reading yourself.",
            },
            {
                "text": "Ask a colleague to run it through their approved "
                        "account.",
                "tone": "ok",
                "headline": "Sensible — but check one thing first",
                "consequence": "This is often the right call. What you have to "
                               "confirm is that their account really is the "
                               "approved one, and not their own personal "
                               "login. Handing a confidential document to a "
                               "colleague does not make an unapproved tool "
                               "approved.",
                "rule": "Approved means the company's agreement — not a "
                        "colleague's goodwill.",
            },
        ],
    },

    # Title, channel and runtime were read back from YouTube
    # itself. See newvideos.json.
    "video": {
        "url": "https://www.youtube.com/watch?v=57wFvOqzBvg",
        "title": "Don’t share your SECRETS with ChatGPT, protect your "
                 "PRIVACY",
        "channel": "David Bombal",
        "duration": "7:17",
        "heading": "Seven minutes on what leaks",
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
            "q": "Which of these is safe to paste?",
            "stem": "You are drafting a reply to a customer whose order "
                    "arrived two cartons short.",
            "remember": "Describe the situation. Never forward the document.",
            "answers": [
                {"text": "The customer's email, exactly as they sent it",
                 "ok": False,
                 "why": "Their email carries their name, their signature "
                        "block and usually a phone number and address. All of "
                        "it goes outside the company for no benefit — the tool "
                        "does not need to know who they are to write well."},
                {"text": "A description of what happened, with no names",
                 "ok": True,
                 "why": "This is the habit to build. \"An order was short by "
                        "two cartons and the customer wants a credit note.\" "
                        "Everything it needs to write, nothing that could harm "
                        "anyone if it leaked."},
                {"text": "The customer's email with the name deleted",
                 "ok": False,
                 "why": "Better, but not enough. Signature blocks, order "
                        "numbers, addresses and phone numbers survive that "
                        "edit, and any one of them identifies the customer. "
                        "Rewriting the situation is faster than sanitising a "
                        "real email."},
                {"text": "The full order history, so it has proper context",
                 "ok": False,
                 "why": "Far more data for no extra quality. Every extra row "
                        "is more personal information outside our control, and "
                        "none of it changes the four paragraphs you get back."},
            ],
        },
        {
            "q": "Why is a personal account worse?",
            "remember": "The account you use decides who is accountable.",
            "answers": [
                {"text": "It gives worse answers", "ok": False,
                 "why": "The answers are usually similar — which is exactly "
                        "why people reach for it. The problem is not the "
                        "output, it is that nobody can account for what went "
                        "in."},
                {"text": "It gives up the company's contractual, security "
                         "and audit controls", "ok": True,
                 "why": "That is the real difference. A work account brings "
                        "an agreement, a record, and somebody who can act "
                        "when a mistake happens. A personal account may "
                        "provide none of that, and the trail ends at you."},
                {"text": "It is slower", "ok": False,
                 "why": "Speed was never the issue. A personal account is "
                        "often quicker to open, which is precisely why this "
                        "mistake is so common on a busy afternoon."},
                {"text": "There is no real difference if you are careful",
                 "ok": False,
                 "why": "Care does not create a contract. Even a perfect paste "
                        "into a personal account leaves the company unable to "
                        "tell a client or an auditor what happened to their "
                        "data."},
            ],
        },
        {
            "q": "You pasted a client list. What now?",
            "stem": "An hour later you realise the file you pasted held about "
                    "200 customer names.",
            "remember": "The clock starts when you know, not when it hurts.",
            "answers": [
                {"text": "Delete the conversation and move on", "ok": False,
                 "why": "Deleting the chat removes your evidence, not their "
                        "copy. The text was transmitted and stored an hour "
                        "ago. You have made the incident harder to assess and "
                        "easier to misjudge."},
                {"text": "Wait and see whether anything actually happens",
                 "ok": False,
                 "why": "Nothing visible will happen, and that is the trap. "
                        "Reporting windows are counted in days from the moment "
                        "you knew — not from the moment harm shows up."},
                {"text": "Write down what happened and report it the same day",
                 "ok": True,
                 "why": "Right. What you pasted, into which tool, roughly "
                        "when. Reported today there are still options. "
                        "Reported next month the only option left is "
                        "explaining it to the client."},
                {"text": "Tell a colleague, so at least someone else knows",
                 "ok": False,
                 "why": "Kind, but it starts nothing. A colleague cannot "
                        "notify a regulator, contact the vendor or assess the "
                        "scope. It has to reach the person who handles "
                        "incidents."},
            ],
        },
        {
            "q": "Which is not personal data?",
            "remember": "If it points to one person, it is personal data.",
            "answers": [
                {"text": "A customer's mobile number", "ok": False,
                 "why": "A phone number identifies a person on its own. It is "
                        "personal data in India, in the UAE and almost "
                        "everywhere else, whether or not a name sits next to "
                        "it."},
                {"text": "\"A delivery was three days late\"", "ok": True,
                 "why": "A fact about an event, not about a person. Nobody can "
                        "be identified from it, so it carries no privacy risk "
                        "— and the tool can still write you a full reply."},
                {"text": "An employee's payroll number", "ok": False,
                 "why": "It points to one named individual in our systems. An "
                        "identifier does not stop being personal data because "
                        "it happens to be a number rather than a name."},
                {"text": "A photo of a delivery note showing the address",
                 "ok": False,
                 "why": "The address identifies a household, and these tools "
                        "read images as easily as text. Cropping it out is not "
                        "an optional extra — it is the whole task."},
            ],
        },
        {
            "q": "What is the first thing you do?",
            "stem": "You are about to ask an AI assistant for help with "
                    "something from work.",
            "remember": "Right tool, right account, then type.",
            "answers": [
                {"text": "Open the tool and start typing", "ok": False,
                 "why": "This is how almost every bad paste begins — not with "
                        "a decision but with the absence of one. Two seconds "
                        "of checking is what separates a normal Tuesday from "
                        "an incident report."},
                {"text": "Check you are in the approved tool, on your work "
                         "account", "ok": True,
                 "why": "It costs two seconds and it settles everything that "
                        "follows: whether an agreement exists, whether a "
                        "record exists, and whether anyone can help you if "
                        "something goes wrong."},
                {"text": "Paste everything in, so it has full context",
                 "ok": False,
                 "why": "Past a point, more context does not improve the "
                        "answer — but it always increases exposure. Give it "
                        "the situation, never the source documents."},
                {"text": "Ask a colleague whether it is allowed", "ok": False,
                 "why": "Your colleague is guessing too. The rule is in this "
                        "module, and you never need permission to describe a "
                        "situation without names in it."},
            ],
        },
    ],

    "recap": {
        "title": "Never-paste rules on one screen",
        "points": [
            ("Five things never go in",
             "Personal data, contract terms, financials, logins, anything "
             "marked confidential."),
            ("Facts, not files",
             "Describe the situation. Do not paste the document the situation "
             "came from."),
            ("Names come out first",
             "Names, numbers and addresses before anything else. Those are "
             "what regulators count."),
            ("The account decides accountability",
             "Work account, under a company agreement, every single time."),
            ("You cannot recall a paste",
             "No delete button reaches every copy. Prevention is the only "
             "control you have."),
            ("Report it the same day",
             "An hour later there are options. A month later there is only an "
             "apology."),
        ],
        "oneliner": "Would I be happy for this exact text to arrive in a "
                    "competitor's inbox tomorrow? If not, it does not go in.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("shield", "The two-second test",
             "Could this text identify a person or a customer? If yes, strip "
             "it before it goes in."),
            ("mail", "The safe payment-reminder prompt",
             "Situation, days overdue, tone. No names, no invoice number, no "
             "amount."),
            ("clip", "The first-hour checklist",
             "What, where, when — written down and reported the same day."),
        ],
        "links": [
            ("India's data protection framework",
             "https://www.meity.gov.in/data-protection-framework"),
            ("UAE data protection laws", "https://u.ae/en/about-the-uae/"
                                         "digital-uae/data/data-protection-laws"),
            ("Check if your email has leaked", "https://haveibeenpwned.com"),
        ],
        "next": "Companion module: SEC-06, Safe Use of AI at Work. It covers "
                "which tools are approved, which settings to switch off, and "
                "how to keep a trail you can explain.",
    },

    "glossary": [
        ("Personal data", "Any information that points to one identifiable "
                          "person — a name, a phone number, an ID, sometimes "
                          "an address on its own."),
        ("PII", "Personally Identifiable Information. Another term for "
                "personal data, used mostly in US and UAE documents."),
        ("DPDP Act", "India's Digital Personal Data Protection Act. It sets "
                     "out how personal data must be handled and when a breach "
                     "must be reported."),
        ("Data breach", "Personal data going somewhere it should not. It does "
                        "not need a hacker — one paste is enough."),
        ("Approved tool", "The tool, account and use the company has "
                          "actually approved — not just any work login."),
        ("Prompt", "Everything you type into an AI tool. It leaves your device "
                   "and is usually stored."),
    ],
}
