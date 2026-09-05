# -*- coding: utf-8 -*-
"""AI-01 — AI Fundamentals. Content only. No rendering code here."""

DECK = {
    "module_code": "AI-01",
    "area": "01-ai-general",
    "filename": "01-01-ai-fundamentals.pptx",
    "title": "AI Fundamentals",
    "subtitle": "What AI actually is, in plain language — and what it changes "
                "on your desk on Monday morning.",
    "duration_min": 18,
    "audience": "New joiners + staff",
    "motif": "network",
    "cover_image": "assets/hero-ai-fundamentals.jpg",

    "why": {
        "title": "Ramesh loses two hours every Friday",
        "icon": "clock",
        "scenario": "Ramesh runs dispatch at the Bhiwandi warehouse. Every "
                    "Friday he writes delay notes for the shipments that "
                    "missed their date. He already knows every order number, "
                    "every reason, every new date. What takes him two hours is "
                    "finding the words.",
        "cost": "Two hours a week. Around 100 hours a year. Spent on typing, "
                "not on dispatch.",
        "fix": "You hand over the facts. A clean draft comes back in a "
               "minute. Your time goes into checking it, not typing it.",
    },

    "outcomes": [
        ("chat", "Explain in one sentence what an AI assistant is doing when "
                 "it answers you"),
        ("search", "Choose correctly between a search engine and an AI "
                   "assistant for the task in front of you"),
        ("warn", "Spot an answer that sounds completely sure and is completely "
                 "wrong"),
        ("doc", "Write a prompt that gives you a usable draft on the first try"),
        ("lock", "Name what you must never type into an AI tool at work, and "
                 "why it matters"),
    ],

    "sections": [
        ("What AI actually is", "The one idea behind every AI tool", "s_what"),
        ("Search or assistant?", "Two different tools, two different jobs", "s_vs"),
        ("Your first two minutes", "Do it now, with the exact words", "s_first"),
        ("Where it helps, where it breaks", "Pick the right task", "s_fit"),
        ("Using it safely", "The habits that keep you out of trouble", "s_safe"),
        ("Choose what you'd do", "A real Monday morning decision", "scenario"),
        ("Watch this", "A 7-minute outside explainer", "video"),
    ],

    "slides": [
        # ---------------- Section: what AI actually is ----------------
        {
            "anchor": "s_what",
            "label": "What AI actually is",
            "title": "It predicts the next word",
            "lead": "By default, an AI assistant does not look up an answer. "
                    "It reads your words and predicts what should come next, "
                    "one small piece at a time, thousands of times a second. "
                    "Some tools can search the web when enabled — but unless "
                    "it shows a page it opened, treat the answer as "
                    "generated, not looked up.",
            "gloss": ["Token", "Model"],
            "visual": {
                "type": "flow",
                "steps": [
                    ("You type", "Your request goes in as plain text."),
                    ("It splits your text", "Words become small pieces called "
                                            "tokens."),
                    ("It predicts", "It picks the most likely next piece, then "
                                    "the next, then the next."),
                    ("You get an answer", "Sentences appear that fit the shape "
                                          "of what you asked for."),
                ],
            },
        },
        {
            "label": "What AI actually is",
            "title": "It knows nothing about our company",
            "lead": "Everything it can say came from text it read before a "
                    "fixed cut-off date. None of your company's files were in "
                    "that text.",
            "visual": {
                "type": "nested",
                "layers": [
                    {"label": "Public text it was trained on",
                     "sub": "Books, websites, manuals, forums — up to a fixed date."},
                    {"label": "What it can discuss confidently",
                     "sub": "General knowledge, language, structure, formatting."},
                    {"label": "What it knows about our company",
                     "sub": "Nothing at all, unless you type it in yourself."},
                ],
                "note": "This is why it can write a perfectly worded dispatch "
                        "note and still invent the client's name. It is filling "
                        "a gap in a sentence, not remembering a fact.",
            },
        },
        {
            "label": "What AI actually is",
            "title": "Three words you will hear daily",
            "gloss": ["Prompt", "Output"],
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "model", "label": "Model",
                     "sub": "The trained system that produces the answer. "
                            "ChatGPT, Copilot and Gemini are apps built around "
                            "a model."},
                    {"icon": "chat", "label": "Prompt",
                     "sub": "Everything you type in. Your request, plus any "
                            "facts you decide to give it."},
                    {"icon": "doc", "label": "Output",
                     "sub": "What comes back. Always a draft you are "
                            "responsible for. Never a source you can quote."},
                ],
            },
        },

        # ---------------- Section: search vs assistant ----------------
        {
            "anchor": "s_vs",
            "label": "Search or assistant?",
            "title": "Search finds pages. AI writes text.",
            "visual": {
                "type": "split",
                "left": {
                    "tag": "Search engine",
                    "title": "Google, Bing, the company intranet",
                    "tone": "neutral", "mark": "search",
                    "items": [
                        "Returns links to pages that other people wrote",
                        "Right choice when you need a source you can quote",
                        "Everyone who searches the same words sees the same list",
                        "Will not rewrite your email or shorten your report",
                    ],
                },
                "right": {
                    "tag": "AI assistant",
                    "title": "Copilot, ChatGPT, Gemini, Claude",
                    "tone": "accent", "mark": "chat",
                    "items": [
                        "Returns new text written for your exact request",
                        "Right choice when you need a draft, summary or rewrite",
                        "Gives a slightly different answer every time you ask",
                        "Cannot promise that any fact inside it is correct",
                    ],
                },
            },
        },
        {
            "label": "Search or assistant?",
            "title": "Which one do I open?",
            "visual": {
                "type": "tree",
                "question": "Do I need a page someone else wrote, or new text "
                            "of my own?",
                "no": {
                    "path": "A page", "tone": "good", "label": "Open search",
                    "detail": "A GST circular, a supplier's spec sheet, a "
                              "government notification, a news report. You need "
                              "the actual page, because you will have to show "
                              "it to someone.",
                },
                "yes": {
                    "path": "New text", "tone": "good",
                    "label": "Open the AI assistant",
                    "detail": "A reply to an unhappy client, a summary of a "
                              "12-page site report, a first draft of an SOP. "
                              "You already have the facts and only need the "
                              "wording.",
                },
            },
        },

        # ---------------- Section: your first two minutes ----------------
        {
            "anchor": "s_first",
            "label": "Your first two minutes",
            "title": "Do this now: your first 90 seconds",
            "visual": {
                "type": "steps",
                "items": [
                    "Open your approved AI assistant. On most company laptops "
                    "this is Microsoft Copilot, in Edge or inside Teams.",
                    "Click into the message box at the bottom of the screen.",
                    "Select the whole prompt on the right, copy it, paste it "
                    "in, and press Enter.",
                    "Read what comes back. Notice that it used every fact you "
                    "gave it, and invented nothing.",
                ],
                "prompt": "Write a short, polite email to a customer whose "
                          "delivery is late. Facts: order 4471, promised 12 "
                          "March, now expected 15 March, delayed by a transport "
                          "strike. Tone: apologetic but calm. Under 120 words. "
                          "End with \"Regards, Dispatch Team\".",
                "caption": "This works exactly as written. Swap in your own "
                           "order number and dates afterwards.",
            },
        },
        {
            "label": "Your first two minutes",
            "title": "The same job, asked two ways",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "Vague request",
                "bad": [
                    "You type:  write email about late delivery",
                    "You get back a six-paragraph letter with no order number, "
                    "no dates, and an apology for \"any inconvenience caused\".",
                    "You now spend ten minutes repairing it. You could have "
                    "written it yourself in eight.",
                ],
                "good_tag": "Specific request",
                "good": [
                    "You type the prompt from the last slide: order number, "
                    "both dates, the reason, the tone, the word limit.",
                    "You get back a 110-word email with the correct dates, one "
                    "clear apology and a firm new delivery date.",
                    "You spend 60 seconds checking the dates against the "
                    "tracking sheet, then send it.",
                ],
                "note": "The difference was not the AI tool. It was the four "
                        "facts you took ten seconds to type.",
            },
        },
        {
            "label": "Your first two minutes",
            "title": "Turn rough notes into a report",
            "lead": "This is the most useful thing most people do with AI all "
                    "week. You already made the notes. You just need them in "
                    "sentences.",
            "visual": {
                "type": "prompt_out",
                "text": "Turn these site-visit notes into a 180-word report for "
                        "my manager. Keep every fact. Do not add anything I "
                        "have not written. Notes: visited Chakan plant 4 March; "
                        "two of six machines idle; operator says spare part on "
                        "order since 20 Feb; production down about 30 percent; "
                        "supervisor asking for a follow-up visit next week.",
                "caption": "Paste it as-is to see the shape, then replace the "
                           "notes with your own.",
                "out_title": "What comes back",
                "out": [
                    "A 180-word report with a one-line summary at the top, the "
                    "five facts in order, and a closing line about the "
                    "follow-up visit.",
                    "Every number in it — six machines, 20 February, 30 per "
                    "cent — came from your notes, because you told it to add "
                    "nothing.",
                    "Your job now is 60 seconds of checking, not 30 minutes of "
                    "writing.",
                ],
            },
        },
        {
            "label": "Your first two minutes",
            "title": "When it is 80% right, correct it",
            "visual": {
                "type": "prompt",
                "header": "Copy this correction prompt",
                "text": "Keep the structure and the tone exactly as they are. "
                        "Change three things: the delivery date is 15 March, "
                        "not 12 March; delete the final paragraph; make the "
                        "apology one sentence instead of two.",
                "caption": "Say what to keep, then say what to change. In that "
                           "order.",
                "why": [
                    "Starting again gives you a different answer with the same "
                    "gaps, because the gaps came from your first prompt.",
                    "Naming what to keep stops it rewriting the good 80%.",
                    "Three specific changes work far better than \"make it "
                    "better\", which it cannot act on.",
                ],
            },
        },

        # ---------------- Section: where it helps, where it breaks -------
        {
            "anchor": "s_fit",
            "label": "Where it helps, where it breaks",
            "title": "Three things it is good at",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "doc", "label": "Turning facts into text",
                     "sub": "Emails, summaries, SOP drafts, meeting notes. You "
                            "supply the facts, it supplies the sentences."},
                    {"icon": "sheet", "label": "Reshaping what you give it",
                     "sub": "A long report into five bullets. A Hindi note into "
                            "English. A messy list into a clean table."},
                    {"icon": "bulb", "label": "Getting you unstuck",
                     "sub": "Ten subject lines to choose from. Questions to ask "
                            "a supplier. A structure for a proposal you are "
                            "staring at blankly."},
                ],
            },
        },
        {
            "label": "Where it helps, where it breaks",
            "title": "Where it breaks",
            "gloss": ["Hallucination"],
            "visual": {
                "type": "bandlist",
                "headline": "It can be completely wrong and still sound "
                            "completely sure.",
                "sub": "There is no warning sign, no change of tone, no "
                       "\"I think\". Every answer arrives with the same "
                       "confidence.",
                "items": [
                    "Numbers you did not give it — prices, GST rates, stock "
                    "levels, distances, penalties",
                    "Anything after its cut-off date — this month's circular, "
                    "yesterday's rate change",
                    "Our own facts — client names, internal policies, system "
                    "names, who approves what",
                    "Legal, tax or medical points you would act on without a "
                    "human checking them",
                ],
            },
        },
        {
            "label": "Where it helps, where it breaks",
            "title": "Should I use AI for this task?",
            "visual": {
                "type": "tree",
                "question": "Do I already know the facts, and can I check the "
                            "answer?",
                "yes": {
                    "path": "Yes", "tone": "good", "label": "Go ahead",
                    "detail": "You give the facts, it gives the wording, you "
                              "check it before it leaves your desk. This covers "
                              "most of the writing in an ordinary office week.",
                },
                "no": {
                    "path": "No", "tone": "bad",
                    "label": "Get the facts first",
                    "detail": "If you cannot check the answer, you cannot use "
                              "it. Take the real number from the system, the "
                              "circular or your manager, and then come back to "
                              "the assistant.",
                },
            },
        },

        # ---------------- Section: using it safely ----------------
        {
            "anchor": "s_safe",
            "label": "Using it safely",
            "title": "Four habits that keep you safe",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Give it facts, never files. Type the order number and the "
                    "dates. Do not paste the contract.",
                    "Check every number, name and date yourself before the text "
                    "goes anywhere.",
                    "Treat the output as your draft that you edited. Never "
                    "present it as a source.",
                    "Use the tool the company has approved: [COMPANY INPUT "
                    "NEEDED: name of the approved AI assistant]. A personal "
                    "login puts our text on someone else's account.",
                ],
            },
        },
        {
            "label": "Using it safely",
            "title": "Four checks before you press send",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Every date and number matches a system or document you "
                    "actually opened.",
                    "Every name is spelled the way the customer spells it, not "
                    "the way it sounds.",
                    "Nothing has been added that you did not supply — read once "
                    "looking only for that.",
                    "You would be comfortable if the customer could see the "
                    "prompt you typed.",
                ],
            },
        },
        {
            "label": "Using it safely",
            "title": "Five mistakes people really make",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Pasting a full customer contract in \"just to summarise it\"",
                     "Client data leaves the company. Reportable under India's "
                     "DPDP Act and UAE data protection law."),
                    ("Asking for a live figure — today's GST rate, current stock",
                     "It answers from memory. A confidently wrong number lands "
                     "in the monthly MIS."),
                    ("Sending the first draft without reading it",
                     "Invented dates and order numbers reach the client with "
                     "your name at the bottom."),
                    ("Typing four words, getting a vague answer, giving up",
                     "You decide \"AI is useless\". The prompt was the problem, "
                     "not the tool."),
                    ("Using a personal ChatGPT login for company work",
                     "No record, no control, and no way to delete the data if "
                     "we are ever asked to."),
                ],
            },
        },
    ],

    "scenario": {
        "title": "Monday, 9:40 am",
        "situation": "A client in Sharjah emails: \"Your team promised delivery "
                     "on the 12th. Nothing has arrived. Explain.\" You have the "
                     "tracking sheet open. Your manager is in a meeting until 11.",
        "choices": [
            {
                "text": "Paste the client's email and the full tracking sheet "
                        "into ChatGPT and ask it to write the reply for you.",
                "tone": "bad",
                "headline": "You just sent client data outside the company",
                "consequence": "The tracking sheet carries the client's name, "
                               "address and order values — plus every other "
                               "customer on the page. Once it sits in a "
                               "personal AI account, the company cannot "
                               "retrieve it, delete it, or tell an auditor "
                               "where it went.",
                "rule": "Facts, not files. Type the two dates and the reason. "
                        "The document stays where it is.",
            },
            {
                "text": "Type only the three facts you already know into the "
                        "approved assistant and ask for a 100-word reply.",
                "tone": "good",
                "headline": "Correct — this is exactly the right use",
                "consequence": "You gave it the order number, the promised "
                               "date and the reason. A calm 100-word reply came "
                               "back in 20 seconds. You checked both dates "
                               "against the tracking sheet, added the new "
                               "delivery date, and sent it at 9:44.",
                "rule": "You supply the facts and the final check. The "
                        "assistant supplies the sentences in between.",
            },
            {
                "text": "Wait for your manager to come out of the meeting "
                        "before replying to the client.",
                "tone": "ok",
                "headline": "Safe — but the client waits two hours",
                "consequence": "Nothing goes wrong, and nothing goes right. "
                               "The client sends a sharper email at 11:15. Your "
                               "manager now has an escalation to handle instead "
                               "of a delay — and you had every fact you needed "
                               "at 9:40.",
                "rule": "Use AI for the drafting. Use your manager for the "
                        "decisions — not for the typing.",
            },
        ],
    },

    # Runtime, title and channel below were read back from YouTube itself,
    # not copied from any list. See linkcheck.json.
    "video": {
        "url": "https://www.youtube.com/watch?v=SAaDOUhrdXc",
        "title": "The 7-Minute Guide to Understanding Artificial Intelligence",
        "channel": "Windows Developer",
        "duration": "7:13",
        "heading": "Seven minutes, the same ideas",
        "note": "This is an outside video, not company material. If anything "
                "in it differs from this module, follow this module.",
        "how": [
            "Optional. Everything you need is already in this deck.",
            "Best watched after you have tried the prompt yourself.",
            "It opens in your browser. Turn the sound on.",
        ],
    },

    "quiz": [
        {
            "q": "What should you assume?",
            "stem": "You asked an AI assistant for a courier's customer care "
                    "number. It replied with a ten-digit number, straight away.",
            "remember": "Sounding sure and being right are two different things.",
            "answers": [
                {"text": "It looked it up on the website just now", "ok": False,
                 "why": "It did not open any website. Unless the tool visibly "
                        "shows you a link it visited, it produced that number "
                        "the same way it produces a sentence — by predicting "
                        "what a courier helpline number usually looks like. "
                        "Digits are exactly the kind of detail this goes wrong on."},
                {"text": "It is probably right, because it sounded certain",
                 "ok": False,
                 "why": "Certainty is not evidence. The tool writes every "
                        "answer in the same confident tone, whether it is "
                        "repeating something it saw a million times or filling "
                        "a gap. There is no built-in \"I am unsure\" signal for "
                        "you to look for."},
                {"text": "It may be invented — check it on the official site "
                         "before using it", "ok": True,
                 "why": "Correct. Treat any number, name or date in an AI "
                        "answer as unverified until you have seen it at the "
                        "source. Ten seconds on the official website stops a "
                        "wrong number going into a client email under your name."},
                {"text": "AI tools are not able to produce phone numbers",
                 "ok": False,
                 "why": "They will produce one happily, and that is the "
                        "problem. It will have the right number of digits, the "
                        "right format and the right area code, and still be "
                        "wrong. Nothing about it will look suspicious."},
            ],
        },
        {
            "q": "Which task fits AI best?",
            "stem": "You have four jobs on your desk this morning. Only one of "
                    "them plays to what an AI assistant is actually good at.",
            "remember": "You bring the facts. It brings the sentences.",
            "answers": [
                {"text": "\"Tell me our current stock of 40mm bearings\"",
                 "ok": False,
                 "why": "It has no connection to your stock system and never "
                        "will unless someone builds one. It will either refuse, "
                        "or produce a number that looks completely plausible "
                        "and is completely made up. Get this from the system."},
                {"text": "\"Turn these six bullet points from my site visit "
                         "into a 200-word report\"", "ok": True,
                 "why": "This is the sweet spot. You already hold every fact. "
                        "The tool only has to do the wording, and you can check "
                        "each line against your own bullets in under a minute."},
                {"text": "\"Decide whether we should terminate this supplier\"",
                 "ok": False,
                 "why": "This is a judgement with money, contracts and "
                        "relationships attached. The tool has none of the "
                        "history, none of the contract, and carries none of the "
                        "consequences. Ask it to list the questions worth "
                        "considering — never to make the call."},
                {"text": "\"Tell me what the new circular from Head Office says\"",
                 "ok": False,
                 "why": "It has never seen that circular, so anything it says "
                        "about it is invented. If the circular is not "
                        "confidential you can paste the text in and ask for a "
                        "summary — that turns it into a task it can actually do."},
            ],
        },
        {
            "q": "Which of these is safe to type in?",
            "stem": "You are about to paste something into an approved AI "
                    "assistant to help you draft a reply.",
            "remember": "Give it enough to write with. Never enough to "
                        "identify anyone.",
            "answers": [
                {"text": "The customer's signed contract, so it can summarise it",
                 "ok": False,
                 "why": "That contract holds names, prices and terms the "
                        "customer trusted us with. Pasting it copies all of "
                        "that onto a system the company does not control and "
                        "cannot audit. This is the most common serious mistake "
                        "people make."},
                {"text": "A colleague's salary, to check whether a raise is fair",
                 "ok": False,
                 "why": "Salary is personal data about a named person. Moving "
                        "it outside the systems approved for HR data is a "
                        "privacy breach by itself, whatever the AI answers. The "
                        "answer is not the problem — the paste is."},
                {"text": "The two dates and the reason for a delay, with no "
                         "names", "ok": True,
                 "why": "Facts without identifiers. The tool has everything it "
                        "needs to write the email and nothing that could harm "
                        "anyone if it leaked. Make this your default habit and "
                        "you will rarely have to think about it again."},
                {"text": "Nothing at all — AI is too risky to use", "ok": False,
                 "why": "This is a mistake in the other direction. Refusing to "
                        "use an approved tool costs you hours every week and "
                        "leaves you behind colleagues who use it well. The "
                        "skill is knowing what to leave out, not avoiding the "
                        "tool."},
            ],
        },
        {
            "q": "The answer is 80% right. Now what?",
            "stem": "The structure and tone are exactly what you wanted, but "
                    "one date is wrong and the last paragraph is not needed.",
            "remember": "Correct it. Do not restart it.",
            "answers": [
                {"text": "Rewrite the whole thing yourself", "ok": False,
                 "why": "You just threw away 80% of finished work. Tell it what "
                        "is wrong instead: \"Keep the structure, but the date is "
                        "15 March not 12 March, and remove the last paragraph.\" "
                        "That takes ten seconds."},
                {"text": "Send it — 80% is good enough for an internal note",
                 "ok": False,
                 "why": "The missing 20% is exactly where the wrong dates live. "
                        "Internal notes get forwarded. Wrong facts travel "
                        "further than you expect, and your name stays attached "
                        "to them the whole way."},
                {"text": "Tell it what is wrong and ask for a corrected version",
                 "ok": True,
                 "why": "This is the whole skill. The second attempt is almost "
                        "always the good one. Be specific about what to keep as "
                        "well as what to change, or it will rewrite the parts "
                        "that were already fine."},
                {"text": "Send the same prompt again and hope for a better answer",
                 "ok": False,
                 "why": "You will get a different answer with the same gaps, "
                        "because the gaps came from the prompt. Repeating an "
                        "unchanged prompt is the most common way people waste "
                        "time with these tools."},
            ],
        },
        {
            "q": "Where did that figure come from?",
            "stem": "Your manager points at a number in your monthly report and "
                    "asks where it came from. It came from an AI answer.",
            "remember": "AI output is a draft. It is never a source.",
            "answers": [
                {"text": "Tell her the AI assistant provided it", "ok": False,
                 "why": "\"The AI said so\" is not a source. Your manager cannot "
                        "act on it, cannot defend it to a client, and if the "
                        "figure is wrong the report is still yours. Find the "
                        "real source before the report goes out."},
                {"text": "Find the figure in the real system or document and "
                         "quote that", "ok": True,
                 "why": "Right. Every number in anything you sign should be "
                        "traceable to a system, a document or a named person. "
                        "AI can help you write the sentence around the number. "
                        "It cannot be the reason the number is there."},
                {"text": "Say you calculated it yourself", "ok": False,
                 "why": "This turns a checkable mistake into a false statement. "
                        "If the figure is later found to be wrong, the problem "
                        "is no longer the figure — it is that you said "
                        "something untrue about where it came from."},
                {"text": "Remove the figure from the report", "ok": False,
                 "why": "Better than inventing a source, but you have thrown "
                        "away information the report needed. The real figure "
                        "almost certainly exists somewhere — spend two minutes "
                        "finding it rather than deleting the line."},
            ],
        },
    ],

    "recap": {
        "title": "AI Fundamentals on one screen",
        "points": [
            ("By default it predicts, it does not look up",
             "Built from patterns in text. Some tools search first — "
             "assume nothing was looked up unless shown otherwise."),
            ("Search finds pages, AI writes text",
             "Need something you can quote? Search. Need a draft, summary or "
             "rewrite? Assistant."),
            ("You bring the facts",
             "It has none of our order numbers, clients, policies or systems "
             "until you type them in."),
            ("Check every number and name",
             "A confident tone is not evidence. Verify before anything leaves "
             "your desk."),
            ("Facts, never files",
             "Type the order number. Never paste the contract, the salary "
             "sheet or the client list."),
            ("Correct it, don't restart it",
             "Say what to keep and what to change. The second answer is "
             "usually the one you send."),
        ],
        "oneliner": "You supply the facts and the final check. The assistant "
                    "supplies the sentences in between.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("mail", "The late-delivery email prompt",
             "Order number, both dates, reason, tone, word limit. Works as "
             "written."),
            ("doc", "The notes-into-report prompt",
             "Six rough bullets in, a 180-word report out, with nothing added."),
            ("cycle", "The correction prompt",
             "Say what to keep, then name three specific changes."),
        ],
        "links": [
            ("Microsoft Copilot", "https://copilot.microsoft.com"),
            ("ChatGPT", "https://chatgpt.com"),
            ("Google Gemini", "https://gemini.google.com"),
        ],
        "next": "Next module: PE-01, Basic Prompting. It gives you the six-part "
                "shape that turns a vague request into a usable draft every "
                "time — not just when you get lucky.",
    },

    "glossary": [
        ("Token", "A small piece of text, roughly three quarters of a word. AI "
                  "tools read and write in tokens, not in letters."),
        ("Model", "The trained system that produces the answer. ChatGPT, "
                  "Copilot and Gemini are apps built around a model."),
        ("Prompt", "Everything you type in: your request plus any facts you "
                   "choose to supply."),
        ("Output", "What comes back. Always a draft you are responsible for, "
                   "never a source you can quote."),
        ("Hallucination", "A confident answer that is simply made up. Usually "
                          "a name, a number or a date."),
        ("Training data", "The public text the model learned from, up to a "
                          "fixed cut-off date. Our files were never in it."),
    ],
}
