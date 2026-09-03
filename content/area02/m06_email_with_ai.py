# -*- coding: utf-8 -*-
"""DW-01 — Email Writing with AI. Content only."""

DECK = {
    "module_code": "DW-01",
    "area": "02-ai-daily-work",
    "filename": "02-01-email-writing-with-ai.pptx",
    "title": "Email Writing with AI",
    "subtitle": "Thirty emails a day, written in a third of the time, without "
                "sounding like a robot wrote them.",
    "duration_min": 18,
    "audience": "New joiners + staff",
    "motif": "flow",
    "cover_image": "assets/hero-email-ai.jpg",

    "why": {
        "title": "Imran writes thirty emails a day",
        "icon": "mail",
        "scenario": "Imran coordinates logistics from Sharjah. Most of his day "
                    "is emails: chasing a truck, explaining a delay, refusing "
                    "a discount, confirming a slot. He knows what to say every "
                    "time. Finding the words is what takes the day.",
        "cost": "Roughly two and a half hours a day, on wording alone.",
        "fix": "Four email shapes, ready to paste, that cover most of a week.",
    },

    "outcomes": [
        ("mail", "Draft any routine work email in under 60 seconds"),
        ("chat", "Set a tone deliberately instead of hoping it lands right"),
        ("cycle", "Turn a long thread into a reply without reading it twice"),
        ("shield", "Write about a customer without ever naming them"),
        ("clip", "Keep four email prompts you will use every week"),
    ],

    "sections": [
        ("The four email shapes", "What most of your week is", "s_shapes"),
        ("Setting the tone", "Firm, warm, or neutral", "s_tone"),
        ("Replying to a long thread", "Without reading it twice", "s_thread"),
        ("The subject line", "Where most emails fail", "s_subject"),
        ("Do this now", "Write a real one", "s_do"),
        ("Choose what you'd do", "A Tuesday morning decision", "scenario"),
        ("Watch this", "A 6-minute outside walkthrough", "video"),
    ],

    "slides": [
        {
            "anchor": "s_shapes",
            "label": "The four email shapes",
            "title": "Four shapes cover your week",
            "lead": "Almost every routine work email is one of these. Each has "
                    "a prompt you fill in once and reuse.",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "BAD NEWS — a delay, a shortage, a price rise",
                    "CHASING — a payment, a document, a decision",
                    "REFUSING — a discount, a deadline, a special request",
                    "CONFIRMING — a slot, a change, an agreement",
                ],
            },
        },
        {
            "label": "The four email shapes",
            "title": "What every shape needs",
            "visual": {
                "type": "flow",
                "steps": [
                    ("The facts", "Order number, dates, amounts, the actual "
                                  "reason."),
                    ("Your position", "What you will and will not offer."),
                    ("The tone", "Firm, warm or neutral. Choose it on purpose."),
                    ("The ask", "One clear thing you want them to do next."),
                ],
            },
        },
        {
            "anchor": "s_tone",
            "label": "Setting the tone",
            "title": "Choose the tone on purpose",
            "visual": {
                "type": "split",
                "left": {
                    "tag": "Vague tone", "tone": "bad",
                    "title": "\"Make it professional\"",
                    "items": [
                        "Produces the same neutral letter every time",
                        "Over-apologises when you did nothing wrong",
                        "Softens a refusal until it reads as a maybe",
                        "Adds pleasantries nobody reads",
                    ],
                },
                "right": {
                    "tag": "Named tone", "tone": "good",
                    "title": "\"Firm, no apology, warm close\"",
                    "items": [
                        "Firm — states the position without hedging",
                        "Warm — acknowledges the person, not the problem",
                        "Neutral — facts only, for a record",
                        "Apologetic — once, specifically, then move on",
                    ],
                },
            },
        },
        {
            "label": "Setting the tone",
            "title": "The bad-news email prompt",
            "visual": {
                "type": "prompt",
                "text": "Write an email telling a customer their delivery has "
                        "slipped. Facts: promised 12 March, now 15 March, "
                        "delayed by a transport strike, no cost to them. Tone: "
                        "apologetic once and then factual, not grovelling. "
                        "Under 110 words. End by confirming the new date. No "
                        "opening pleasantries.",
                "caption": "Works as written. Swap in your own dates and "
                           "reason.",
                "why": [
                    "\"Apologetic once\" stops the triple apology.",
                    "\"No opening pleasantries\" removes forty wasted words.",
                    "Ending on the new date is what the customer wants first.",
                ],
            },
        },
        {
            "anchor": "s_thread",
            "label": "Replying to a long thread",
            "title": "The twelve-message thread",
            "lead": "You have been added to a thread with a decision buried in "
                    "it. You have four minutes.",
            "visual": {
                "type": "prompt_out",
                "header": "Copy this thread prompt",
                "text": "Below is an email thread. Tell me three things and "
                        "nothing else. One: what has actually been agreed. "
                        "Two: what is still open. Three: what I am being asked "
                        "to do. Use one short line for each. Do not summarise "
                        "the whole conversation.",
                "caption": "Strip the names out of the thread before you paste "
                           "it.",
                "out_title": "What comes back",
                "out": [
                    "Three short lines instead of twelve messages.",
                    "The open question you would have missed on a fast read.",
                    "Four minutes of reading turned into forty seconds.",
                ],
            },
        },
        {
            "label": "Replying to a long thread",
            "title": "Strip it before you paste it",
            "visual": {
                "type": "bandlist",
                "mark": "ban",
                "headline": "A pasted thread carries every name, address and "
                            "signature block in it.",
                "sub": "Describe the situation, or delete the identifying "
                       "lines first.",
                "cols": 2,
                "items": [
                    "Signature blocks with phone numbers and addresses",
                    "Customer names in every quoted reply",
                    "Internal comments colleagues added along the way",
                    "Attachments, prices and account references",
                ],
            },
        },
        {
            "anchor": "s_subject",
            "label": "The subject line",
            "title": "Where most emails fail",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "Vague subject",
                "bad": [
                    "Subject: Update",
                    "Sits unopened for two days in a full inbox.",
                    "When it is opened, nobody knows what is being asked.",
                ],
                "good_tag": "Specific subject",
                "good": [
                    "Subject: Order 4471 — new delivery date 15 March, no "
                    "action needed",
                    "The whole message is readable without opening it.",
                    "It gets filed correctly and found again in June.",
                ],
                "note": "A good subject line says what it is about and whether "
                        "the reader has to do anything.",
            },
        },
        {
            "label": "The subject line",
            "title": "Ask for ten, keep one",
            "visual": {
                "type": "prompt",
                "header": "Copy this subject-line prompt",
                "text": "Give me ten subject lines for the email below. Each "
                        "under nine words. Each must say what it is about and "
                        "whether the reader needs to act. Number them. No "
                        "explanation and no commentary.",
                "caption": "Choosing from ten takes ten seconds. Inventing one "
                           "takes two minutes.",
                "why": [
                    "Ten options cost the same as one.",
                    "\"Whether the reader needs to act\" is the useful half.",
                    "Numbered lines make picking one instant.",
                ],
            },
        },
        {
            "anchor": "s_do",
            "label": "Do this now",
            "title": "Do this now: write a real one",
            "visual": {
                "type": "steps",
                "items": [
                    "Open the email you have been putting off since yesterday.",
                    "Write down the facts, your position, the tone and the "
                    "ask.",
                    "Paste the prompt on the right with those four things in "
                    "it.",
                    "Check the dates, add the name yourself in Outlook, send.",
                ],
                "prompt": "Write a work email. Facts: [dates, numbers, what "
                          "happened]. My position: [what I will and will not "
                          "offer]. Tone: [firm / warm / neutral], one apology "
                          "at most. Under [number] words. End with one clear "
                          "ask. No opening pleasantries, no restating my "
                          "request.",
                "caption": "Four brackets. This is the only email prompt most "
                           "people need.",
            },
        },
        {
            "label": "Do this now",
            "title": "Four habits that keep it human",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Read it aloud in your head before sending. Robotic "
                    "sentences are obvious.",
                    "Cut the first sentence. It is almost always throat-"
                    "clearing.",
                    "Put the name and greeting in yourself, in Outlook.",
                    "If it sounds nothing like you, change three words until "
                    "it does.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Five mistakes people really make",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Pasting the customer's email to \"give context\"",
                     "Their name, address and phone number leave the company "
                     "to save you thirty seconds."),
                    ("Sending it without reading the middle",
                     "The invented commitment is never in the first line or "
                     "the last."),
                    ("Asking for \"a professional email\"",
                     "You get the same neutral letter every time, and it "
                     "matches no situation exactly."),
                    ("Letting it apologise three times",
                     "A triple apology reads as an admission. Say \"one "
                     "apology at most\"."),
                    ("Keeping the AI subject line unread",
                     "\"Update Regarding Your Recent Order\" is how an email "
                     "goes unopened for two days."),
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "When not to use it at all",
            "visual": {
                "type": "tree",
                "question": "Would I want this read out in a dispute?",
                "yes": {
                    "path": "Yes", "tone": "neutral", "label": "Write it "
                                                              "yourself",
                    "detail": "Disciplinary matters, contract commitments, "
                              "anything about a person. Use the tool to check "
                              "the wording afterwards, not to compose it.",
                },
                "no": {
                    "path": "No", "tone": "good", "label": "Draft it with AI",
                    "detail": "Delays, confirmations, chasers, routine "
                              "refusals. This is most of your inbox, and it is "
                              "exactly where the time goes.",
                },
            },
        },
        {
            "label": "Do this now",
            "title": "What good use looks like",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "clock", "label": "Sixty seconds",
                     "sub": "Facts in, draft out, dates checked, sent. Not "
                            "five minutes of staring at a blank reply."},
                    {"icon": "chat", "label": "Tone you chose",
                     "sub": "Firm when firm is right, warm when it is not. "
                            "Decided on purpose rather than by mood."},
                    {"icon": "person", "label": "Still sounds like you",
                     "sub": "Three words changed and your greeting added is "
                            "usually all it takes."},
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "The email rule",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "You supply the facts, the position and the ask. "
                            "It supplies the sentences.",
                "sub": "Every good AI email comes from that split. Every bad "
                       "one comes from skipping it.",
                "cols": 3,
                "items": [
                    "Facts and position — yours.",
                    "Wording and tone — its job.",
                    "The final read — always yours.",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Tuesday, 8:40 am",
        "situation": "A customer emails at length, unhappy that a shipment is "
                     "short by two cartons. They want a credit note today. Your "
                     "policy is replacement, not credit.",
        "choices": [
            {
                "text": "Forward their whole email into the tool and ask for a "
                        "reply.",
                "tone": "bad",
                "headline": "The reply is good. The paste was not.",
                "consequence": "Their name, company, site address, phone "
                               "number and order history all leave the company "
                               "in one paste. The reply you get back could have "
                               "been produced from three lines of description "
                               "with none of that in it.",
                "rule": "Describe the situation. Never forward the email.",
            },
            {
                "text": "Type the facts, your position and the tone, with no "
                        "names.",
                "tone": "good",
                "headline": "Ninety seconds, and nothing left the building",
                "consequence": "\"Shipment short by two cartons. We will "
                               "replace, not credit. Customer is annoyed and "
                               "long-standing. Firm but warm, one apology, "
                               "under 100 words, end by confirming the "
                               "replacement date.\" The reply lands first "
                               "time.",
                "rule": "Facts, position, tone, ask. Nothing that identifies "
                        "anyone.",
            },
            {
                "text": "Write it yourself, as you always have.",
                "tone": "ok",
                "headline": "Fine, and it will take eleven minutes",
                "consequence": "The email is good, because you know the "
                               "situation. It also takes eleven minutes you "
                               "did not have on a Tuesday morning, and the "
                               "same conversation happens four more times this "
                               "week.",
                "rule": "Save your own writing for the emails that genuinely "
                        "need it.",
            },
        ],
    },

    "video": {
        "url": "https://www.youtube.com/watch?v=bCvWzct5SCc",
        "title": "Write Better Emails to Your Boss with AI",
        "channel": "w/KMo",
        "duration": "5:51",
        "heading": "Six minutes, watched over the shoulder",
        "note": "An outside video, not company material. Where it differs from "
                "this module, follow this module.",
        "how": [
            "Optional. The prompts in this deck work as written.",
            "Useful if you prefer seeing someone do it live.",
            "It opens in your browser. Turn the sound on.",
        ],
    },

    "quiz": [
        {
            "q": "What should never go in the prompt?",
            "remember": "Describe the situation. Never paste the email.",
            "answers": [
                {"text": "The delivery dates", "ok": False,
                 "why": "Dates are exactly what it needs and they identify "
                        "nobody. Without them you get a vague apology with no "
                        "commitment in it."},
                {"text": "The customer's original email, pasted whole",
                 "ok": True,
                 "why": "It carries their name, company, address, phone number "
                        "and signature block. All of that leaves the company, "
                        "and none of it improves the reply you get back."},
                {"text": "Your position on the discount", "ok": False,
                 "why": "Essential. Without it the tool guesses, and it "
                        "usually guesses generously, which is a difficult "
                        "email to unsend."},
                {"text": "The tone you want", "ok": False,
                 "why": "One of the most useful lines in the prompt. Without "
                        "it you get the same neutral register regardless of "
                        "the situation."},
            ],
        },
        {
            "q": "Which tone instruction works?",
            "remember": "Name the register, and cap the apologies.",
            "answers": [
                {"text": "\"Make it professional\"", "ok": False,
                 "why": "Professional means something different to everyone, "
                        "including the tool. You get its neutral default, "
                        "which fits no particular situation well."},
                {"text": "\"Firm, one apology at most, warm close\"",
                 "ok": True,
                 "why": "Three specific instructions it can act on. The "
                        "apology cap is the important one — without it a "
                        "routine delay note apologises three times and reads "
                        "as an admission."},
                {"text": "\"Sound friendly\"", "ok": False,
                 "why": "Friendly usually arrives as pleasantries and "
                        "exclamation marks. If you mean warm, say warm, and "
                        "say what to leave out."},
                {"text": "\"Use business English\"", "ok": False,
                 "why": "It already does. This instruction spends words "
                        "without changing anything about the output."},
            ],
        },
        {
            "q": "What makes a good subject line?",
            "remember": "What it is about, and whether they must act.",
            "answers": [
                {"text": "It is short", "ok": False,
                 "why": "Short and empty is worse than slightly longer and "
                        "specific. \"Update\" is very short and tells the "
                        "reader nothing at all."},
                {"text": "It names the topic and says if action is needed",
                 "ok": True,
                 "why": "\"Order 4471 — new date 15 March, no action needed\" "
                        "can be read without opening the email, filed "
                        "correctly, and found again months later."},
                {"text": "It sounds urgent", "ok": False,
                 "why": "Manufactured urgency stops working after the second "
                        "time, and it makes the genuinely urgent ones "
                        "invisible."},
                {"text": "It matches the first line of the email", "ok": False,
                 "why": "Duplication wastes the one line most likely to be "
                        "read. The subject should carry information the first "
                        "line then builds on."},
            ],
        },
        {
            "q": "Twelve-message thread. Best move?",
            "remember": "Ask for agreed, open, and your action.",
            "answers": [
                {"text": "Ask for a summary of the whole thread", "ok": False,
                 "why": "You get a fair summary weighted to whatever was "
                        "longest. The decision you actually needed is usually "
                        "one line in the middle of it."},
                {"text": "Ask for what is agreed, what is open, what you must "
                         "do", "ok": True,
                 "why": "Three specific questions produce three usable lines. "
                        "It also surfaces the open item, which is the thing "
                        "people miss on a fast read."},
                {"text": "Read all twelve messages properly", "ok": False,
                 "why": "Thorough, and it costs you four minutes you may not "
                        "have. Use the three-question prompt, then read only "
                        "the message it points you at."},
                {"text": "Reply to the last message and hope", "ok": False,
                 "why": "The last message is rarely where the decision is. "
                        "This is how open questions sit unanswered for another "
                        "week."},
            ],
        },
        {
            "q": "Which email should you write yourself?",
            "remember": "Anything about a person, or anything binding.",
            "answers": [
                {"text": "A delay notification", "ok": False,
                 "why": "Routine, factual and repeated. This is the ideal case "
                        "for a stored prompt — you supply four facts and check "
                        "two dates."},
                {"text": "A note about a colleague's performance", "ok": True,
                 "why": "It concerns a named person, it may be read back in a "
                        "formal process, and it should carry your judgement in "
                        "your words. Use the tool to check the wording "
                        "afterwards at most."},
                {"text": "A slot confirmation", "ok": False,
                 "why": "Three facts and a confirmation. Exactly the sort of "
                        "email that eats a morning and should take forty "
                        "seconds."},
                {"text": "A payment chaser", "ok": False,
                 "why": "Routine and easily templated, as long as you describe "
                        "the situation rather than pasting the account "
                        "statement."},
            ],
        },
    ],

    "recap": {
        "title": "Email with AI on one screen",
        "points": [
            ("Four shapes cover the week",
             "Bad news, chasing, refusing, confirming. One prompt each."),
            ("Facts, position, tone, ask",
             "Give it all four and the first draft is usually sendable."),
            ("Name the tone, cap the apologies",
             "\"Firm, one apology at most\" beats \"make it professional\"."),
            ("Never paste the customer's email",
             "Describe the situation instead. The reply is just as good."),
            ("Subject lines carry the message",
             "Topic plus whether they must act. Ask for ten, keep one."),
            ("Read the middle before sending",
             "Openings and closings get checked. Middles carry the invented "
             "line."),
        ],
        "oneliner": "You supply the facts, the position and the ask. It "
                    "supplies the sentences in between.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("mail", "The four-bracket email prompt",
             "Facts, position, tone, ask. Covers most of a week."),
            ("list", "The thread prompt",
             "Agreed, open, my action. Three lines, forty seconds."),
            ("chat", "The ten subject lines prompt",
             "Under nine words each, action or no action."),
        ],
        "links": [
            ("Microsoft Copilot", "https://copilot.microsoft.com"),
            ("ChatGPT", "https://chatgpt.com"),
            ("Google Gemini", "https://gemini.google.com"),
        ],
        "next": "Next module: DW-02, Research with AI. How to use it to find "
                "the questions worth asking, without letting it invent the "
                "answers.",
    },

    "glossary": [
        ("Tone", "The register of a message: firm, warm, neutral, apologetic. "
                 "Name it rather than hoping."),
        ("Thread", "An email conversation with replies stacked inside it. "
                   "Full of names and signature blocks."),
        ("Prompt", "Everything you type in: the facts, your position, the tone "
                   "and the ask."),
        ("Template", "A prompt with brackets where the specifics go, so you "
                     "reuse it without rewriting."),
        ("Personal data", "Anything identifying a person: a name, a phone "
                          "number, an address, an account."),
        ("Output", "What comes back. Your draft, which you are responsible for "
                   "checking."),
    ],
}
