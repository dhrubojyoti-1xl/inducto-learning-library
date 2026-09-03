# -*- coding: utf-8 -*-
"""AI-05 — AI Hallucinations & Fact-Checking. Content only."""

DECK = {
    "module_code": "AI-05",
    "area": "01-ai-general",
    "filename": "01-05-hallucinations-fact-checking.pptx",
    "title": "Hallucinations & Fact-Checking",
    "subtitle": "How to catch a confident wrong answer in under a minute, "
                "before it reaches a customer.",
    "duration_min": 18,
    "audience": "New joiners + staff",
    "motif": "network",
    "cover_image": "assets/hero-hallucinations.jpg",

    "why": {
        "title": "Kavita cites a clause that does not exist",
        "icon": "warn",
        "scenario": "Kavita answers support tickets for a Bengaluru team. A "
                    "customer disputes a charge. She asks an AI tool what the "
                    "policy says, and it quotes clause 7.3. She pastes the "
                    "clause into her reply. There is no clause 7.3.",
        "cost": "A customer holding a written quotation of a clause we never "
                "wrote.",
        "fix": "Four checks, under a minute, and this never leaves your desk.",
    },

    "outcomes": [
        ("warn", "Explain in one sentence why a hallucination happens"),
        ("eye", "Name the four answer types most likely to be invented"),
        ("check", "Run a four-step verification on any answer in under a minute"),
        ("chat", "Write a prompt that makes gaps visible instead of filled"),
        ("cycle", "Correct a wrong answer without losing the good parts"),
    ],

    "sections": [
        ("What a hallucination is", "Why the gap gets filled", "s_what"),
        ("Where they cluster", "The four risky answer types", "s_where"),
        ("The four-step check", "Under a minute, every time", "s_check"),
        ("Prompting for honesty", "Make gaps visible", "s_honest"),
        ("When you find one", "Correct, do not restart", "s_found"),
        ("Choose what you'd do", "A Tuesday morning decision", "scenario"),
        ("Watch this", "A 9-minute outside explainer", "video"),
    ],

    "slides": [
        {
            "anchor": "s_what",
            "label": "What a hallucination is",
            "title": "A gap does not stay a gap",
            "lead": "It is not lying. It has no concept of true. It is "
                    "completing a sentence in the most likely way.",
            "gloss": ["Hallucination"],
            "visual": {
                "type": "flow",
                "steps": [
                    ("Your question implies a fact", "\"What does clause 7.3 "
                                                     "say?\" assumes one exists."),
                    ("It has no such fact", "Nothing in its patterns matches "
                                            "your document."),
                    ("It builds a likely one", "A clause worded exactly like a "
                                               "real clause."),
                    ("It reads as a quotation", "Nothing marks it as "
                                                "constructed."),
                ],
            },
        },
        {
            "label": "What a hallucination is",
            "title": "Why it never says \"I don't know\"",
            "visual": {
                "type": "nested",
                "layers": [
                    {"label": "What it is doing",
                     "sub": "Choosing the most likely next piece of text."},
                    {"label": "What it is not doing",
                     "sub": "Checking anything against anything."},
                    {"label": "So a gap looks like",
                     "sub": "Just another place a likely word goes."},
                ],
                "note": "\"I do not know\" is a rare pattern in the text it "
                        "learned from. A confident answer is a very common "
                        "one. It produces the common pattern.",
            },
        },
        {
            "anchor": "s_where",
            "label": "Where they cluster",
            "title": "The four risky answer types",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "mark": "ban",
                "items": [
                    "QUOTES — clause numbers, policy wording, what someone "
                    "said",
                    "FIGURES — rates, prices, percentages, penalties, "
                    "totals",
                    "NAMES — people, products, suppliers, systems, standards",
                    "REFERENCES — circulars, sections, studies, page numbers",
                ],
            },
        },
        {
            "label": "Where they cluster",
            "title": "The tell-tale shape",
            "visual": {
                "type": "split",
                "left": {
                    "tag": "Higher risk", "tone": "bad",
                    "title": "Specific and unverifiable",
                    "items": [
                        "A clause number you cannot see on screen",
                        "A rate quoted to one decimal place",
                        "A named standard nobody in the room recognises",
                        "A date for a change you had not heard about",
                    ],
                },
                "right": {
                    "tag": "Lower risk", "tone": "good",
                    "title": "General and checkable",
                    "items": [
                        "An explanation of text you pasted in",
                        "A rewrite of your own sentences",
                        "A list of questions to go and ask",
                        "A structure or outline with no facts in it",
                    ],
                },
            },
        },
        {
            "anchor": "s_check",
            "label": "The four-step check",
            "title": "Four checks, under a minute",
            "lead": "Run these in order. Most answers fail or pass on step "
                    "two.",
            "visual": {
                "type": "steps",
                "items": [
                    "UNDERLINE — mark every number, name, date and quote in "
                    "the answer.",
                    "TRACE — for each one, ask: did I type this, or did it?",
                    "OPEN — for anything it produced, open the real source and "
                    "look.",
                    "CUT — delete anything you could not trace. Do not soften "
                    "it, cut it.",
                ],
                "prompt": "Rewrite this answer using only the facts I gave "
                          "you. Remove every number, name, date and quotation "
                          "that did not appear in my message. Where something "
                          "is missing, write [CHECK] instead of filling it in.",
                "caption": "Run this on any answer you are unsure about.",
            },
        },
        {
            "label": "The four-step check",
            "title": "What tracing looks like",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "Untraced answer",
                "bad": [
                    "\"As per clause 7.3, refunds are processed within 14 "
                    "working days.\"",
                    "You typed neither the clause number nor the 14 days.",
                    "Both were produced. Both read exactly like policy.",
                ],
                "good_tag": "Traced answer",
                "good": [
                    "You open the policy. There are six clauses and no 7.3.",
                    "The real processing time is 21 days, in clause 5.",
                    "Sixty seconds saved a written commitment you could not "
                    "keep.",
                ],
                "note": "The check is not clever. It is just refusing to send "
                        "anything you did not type or read.",
            },
        },
        {
            "anchor": "s_honest",
            "label": "Prompting for honesty",
            "title": "Make the gaps visible",
            "visual": {
                "type": "prompt",
                "header": "Copy this honesty prompt",
                "text": "Answer using only the text I have given you. If the "
                        "answer is not in that text, write \"not in the "
                        "supplied text\" rather than answering from general "
                        "knowledge. Do not add clause numbers, dates or "
                        "figures unless they appear in what I pasted.",
                "caption": "Put this above any question about a document.",
                "why": [
                    "It converts silent invention into a visible gap.",
                    "You then fill the gap correctly, from the real source.",
                    "It costs one sentence and catches the worst failures.",
                ],
            },
        },
        {
            "label": "Prompting for honesty",
            "title": "Grounding beats asking",
            "gloss": ["Grounding"],
            "visual": {
                "type": "tree",
                "question": "Is the source text on my screen right now?",
                "yes": {
                    "path": "Yes", "tone": "good", "label": "Paste and ask",
                    "detail": "Give it the actual text and ask about that. "
                              "Every sentence it produces can then be checked "
                              "against words you can see.",
                },
                "no": {
                    "path": "No", "tone": "bad", "label": "Go and get it first",
                    "detail": "Asking about a document it has never seen is "
                              "the single most reliable way to produce an "
                              "invented quotation. Find the file first.",
                },
            },
        },
        {
            "anchor": "s_found",
            "label": "When you find one",
            "title": "Correct, do not restart",
            "visual": {
                "type": "prompt_out",
                "text": "Two corrections. There is no clause 7.3 — the "
                        "relevant clause is 5. The processing time is 21 "
                        "working days, not 14. Keep the rest of the wording "
                        "exactly as it is and reissue the reply.",
                "caption": "Name the error, give the truth, protect the rest.",
                "out_title": "What comes back",
                "out": [
                    "The same reply, with clause 5 and 21 days in place of the "
                    "invented pair.",
                    "The tone and structure you already approved are "
                    "untouched.",
                    "One line of correction instead of ten minutes of "
                    "rewriting.",
                ],
            },
        },
        {
            "label": "When you find one",
            "title": "Four habits that catch them",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Never send a clause number you have not seen with your "
                    "own eyes.",
                    "Treat every figure as unverified until you open the "
                    "source.",
                    "Paste the document in rather than asking about it.",
                    "Ask for \"not in the supplied text\" instead of an answer.",
                ],
            },
        },
        {
            "label": "When you find one",
            "title": "Asking twice is not checking",
            "visual": {
                "type": "bandlist",
                "mark": "ban",
                "headline": "A second answer from the same tool is not "
                            "confirmation of the first.",
                "sub": "Both came from the same patterns, so they can agree "
                       "and both be wrong.",
                "cols": 3,
                "items": [
                    "Two agreeing answers prove nothing.",
                    "\"Are you sure?\" produces reassurance, not evidence.",
                    "Only the real source settles it.",
                ],
            },
        },
        {
            "label": "When you find one",
            "title": "Five mistakes people really make",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Quoting a clause number from an answer",
                     "It is the single most convincing invention there is, and "
                     "the easiest to disprove later."),
                    ("Checking only the parts that look odd",
                     "Hallucinations are designed by construction to look "
                     "exactly like everything around them."),
                    ("Asking the tool to verify itself",
                     "You get a confident second generation, which is not "
                     "evidence of anything."),
                    ("Softening a wrong figure instead of cutting it",
                     "\"Approximately 14 days\" is still a commitment built on "
                     "an invented number."),
                    ("Skipping the check because the answer reads well",
                     "Reading well is the failure mode, not a reassurance."),
                ],
            },
        },
        {
            "label": "When you find one",
            "title": "Where checking matters most",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "mail", "label": "Anything to a customer",
                     "sub": "It becomes a written commitment the moment you "
                            "press send. Check every figure and clause."},
                    {"icon": "sheet", "label": "Anything that enters a report",
                     "sub": "Numbers get reused for months. A wrong one "
                            "propagates quietly through every later pack."},
                    {"icon": "shield", "label": "Anything with a rule in it",
                     "sub": "Policy, tax, labour, safety. Wrong here is not an "
                            "embarrassment, it is exposure."},
                ],
            },
        },
        {
            "label": "When you find one",
            "title": "The fact-checking rule",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "If you did not type it and you have not opened "
                            "it, it does not go out.",
                "sub": "One sentence that removes almost every hallucination "
                       "risk in ordinary office work.",
                "cols": 3,
                "items": [
                    "You typed it — fine.",
                    "You opened the source — fine.",
                    "Neither — cut it.",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Tuesday, 10:15 am",
        "situation": "A customer disputes a delivery charge and asks which "
                     "term allows it. The AI answer quotes \"clause 7.3\" and "
                     "reads like the contract. You have not opened the "
                     "contract.",
        "choices": [
            {
                "text": "Paste the quoted clause into your reply — it reads "
                        "exactly right.",
                "tone": "bad",
                "headline": "You have now put it in writing",
                "consequence": "The customer forwards your email to their "
                               "legal team, who cannot find clause 7.3 either. "
                               "The dispute is no longer about a delivery "
                               "charge. It is about whether our written "
                               "statements can be relied on.",
                "rule": "Never quote a clause number you have not seen with "
                        "your own eyes.",
            },
            {
                "text": "Open the contract, find the real clause, then reply.",
                "tone": "good",
                "headline": "Ninety seconds, and the dispute stays small",
                "consequence": "The charge is covered by clause 5, worded "
                               "slightly differently. You paste the real "
                               "clause into the tool and ask for a plain "
                               "English explanation. The customer accepts it "
                               "the same morning.",
                "rule": "Bring the document to the tool. Never ask the tool "
                        "for the document.",
            },
            {
                "text": "Ask the AI whether it is sure about clause 7.3.",
                "tone": "ok",
                "headline": "You will get reassurance, not evidence",
                "consequence": "It confirms clause 7.3, possibly with extra "
                               "detail. The confirmation was generated exactly "
                               "the same way as the original claim, so you now "
                               "have two invented statements and more "
                               "confidence than before.",
                "rule": "A tool cannot check itself. Only the source settles "
                        "it.",
            },
        ],
    },

    "video": {
        "url": "https://www.youtube.com/watch?v=ZFKvTIADp0k",
        "title": "Tuning Your AI Model to Reduce Hallucinations",
        "channel": "IBM Technology",
        "duration": "8:54",
        "heading": "Nine minutes on why it invents",
        "note": "Aimed at people who build AI systems. Watch it for the "
                "mechanism, not for the daily rules — those are in this "
                "module.",
        "how": [
            "Optional. The four-step check above is what you need.",
            "Useful if you want to know why the gap gets filled.",
            "It opens in your browser. Turn the sound on.",
        ],
    },

    "quiz": [
        {
            "q": "Why does it invent a clause?",
            "remember": "It completes sentences. It does not check them.",
            "answers": [
                {"text": "It is programmed to sound helpful", "ok": False,
                 "why": "There is no instruction to be helpful at the expense "
                        "of truth. It simply has no mechanism for truth at "
                        "all — it is choosing likely words, and a clause "
                        "number is a likely word here."},
                {"text": "Your question implied one exists, so it produced one",
                 "ok": True,
                 "why": "That is the mechanism. \"What does clause 7.3 say?\" "
                        "makes a clause-shaped answer the most likely "
                        "continuation. It has nothing to compare that against."},
                {"text": "It found a similar contract online", "ok": False,
                 "why": "It did not go online. Nothing was retrieved. The "
                        "clause was constructed word by word, the same way as "
                        "the sentence around it."},
                {"text": "The contract was in its training data", "ok": False,
                 "why": "Your contract was never in its training data, and "
                        "even if a similar one had been, it does not store and "
                        "retrieve documents. It stores patterns."},
            ],
        },
        {
            "q": "Which answer needs checking hardest?",
            "remember": "Specific, unverifiable details carry the most risk.",
            "answers": [
                {"text": "A rewrite of an email you pasted in", "ok": False,
                 "why": "Low risk. Every fact came from you, so you can check "
                        "the whole thing against your own text in seconds."},
                {"text": "\"Refunds take 14 days under clause 7.3\"", "ok": True,
                 "why": "A number and a clause reference, neither of which you "
                        "supplied. It is specific enough to be believed and "
                        "quoted, and completely unverifiable without opening "
                        "the real document."},
                {"text": "A five-part outline for a proposal", "ok": False,
                 "why": "Pure structure with no facts in it. There is nothing "
                        "to invent, so nothing gets invented."},
                {"text": "A list of questions to ask a supplier", "ok": False,
                 "why": "Questions cannot be false in the way a figure can. "
                        "You read them, keep the useful ones, and discard the "
                        "rest."},
            ],
        },
        {
            "q": "What does step two actually ask?",
            "stem": "The four-step check is underline, trace, open, cut.",
            "remember": "Did I type this, or did it?",
            "answers": [
                {"text": "Does this sound plausible?", "ok": False,
                 "why": "Plausibility is the problem, not the test. Every "
                        "hallucination is plausible by construction — that is "
                        "precisely why it survives a quick read."},
                {"text": "Did I supply this, or did the tool?", "ok": True,
                 "why": "That is the only question that separates safe from "
                        "unsafe. Anything you typed can be trusted as far as "
                        "you trust yourself. Anything it produced needs a real "
                        "source."},
                {"text": "Is this the kind of thing AI gets wrong?", "ok": False,
                 "why": "Useful background, but too vague to act on line by "
                        "line. Tracing origin is a mechanical check anyone can "
                        "run in under a minute."},
                {"text": "Would my manager agree with this?", "ok": False,
                 "why": "Your manager cannot tell either, without the source. "
                        "Passing an unverified figure up the chain spreads the "
                        "problem rather than solving it."},
            ],
        },
        {
            "q": "You spot one wrong figure. Now what?",
            "remember": "Name the error, give the truth, keep the rest.",
            "answers": [
                {"text": "Start the whole draft again", "ok": False,
                 "why": "You would throw away wording that was fine and invite "
                        "a fresh set of inventions. One correction line fixes "
                        "the figure and protects everything else."},
                {"text": "Tell it the correct figure and ask it to reissue",
                 "ok": True,
                 "why": "Name what is wrong, supply the right value, and say "
                        "keep the rest. The tone and structure you already "
                        "approved survive intact."},
                {"text": "Change the figure yourself and send it", "ok": False,
                 "why": "Reasonable for one number, but if the tool invented "
                        "one figure it may have invented others. Fix it, then "
                        "re-run the trace over the whole answer."},
                {"text": "Add \"approximately\" in front of it", "ok": False,
                 "why": "The number is not imprecise, it is invented. "
                        "Softening the wording keeps a fabricated commitment "
                        "in the document and makes it harder to spot."},
            ],
        },
        {
            "q": "How do you confirm an answer?",
            "remember": "Only the real source settles it.",
            "answers": [
                {"text": "Ask the same tool again and compare", "ok": False,
                 "why": "Both answers come from the same patterns, so they can "
                        "agree perfectly and both be wrong. Agreement between "
                        "two generations is not corroboration."},
                {"text": "Open the document or system it refers to", "ok": True,
                 "why": "That is the only real confirmation. It usually takes "
                        "under a minute, and it is the difference between a "
                        "reply you can defend and one you cannot."},
                {"text": "Ask a different AI tool the same question",
                 "ok": False,
                 "why": "Better than asking the same one, but still two "
                        "generations rather than a source. Common patterns "
                        "produce common inventions across tools."},
                {"text": "Ask it to rate its own confidence", "ok": False,
                 "why": "A generated confidence score is produced the same way "
                        "as everything else. It is a sentence about certainty, "
                        "not a measurement of it."},
            ],
        },
    ],

    "recap": {
        "title": "Fact-checking on one screen",
        "points": [
            ("A gap never stays a gap",
             "It completes the sentence with something likely, rather than "
             "leaving a blank."),
            ("Four risky types",
             "Quotes, figures, names and references. These are where "
             "inventions cluster."),
            ("Underline, trace, open, cut",
             "Mark the details, ask who supplied them, check the source, "
             "delete the rest."),
            ("Paste the document in",
             "Grounding it in real text is far safer than asking about text it "
             "cannot see."),
            ("Asking twice proves nothing",
             "Two generations can agree and both be wrong. Only the source "
             "settles it."),
            ("Correct, do not restart",
             "Name the error, give the right value, and protect the wording "
             "that worked."),
        ],
        "oneliner": "If you did not type it and you have not opened it, it "
                    "does not go out. That one line prevents nearly all of it.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("shield", "The honesty prompt",
             "\"If it is not in the supplied text, say so.\""),
            ("eye", "The four-step check",
             "Underline, trace, open, cut. Under a minute."),
            ("cycle", "The correction line",
             "Name the error, give the truth, keep the rest."),
        ],
        "links": [
            ("Microsoft Copilot", "https://copilot.microsoft.com"),
            ("ChatGPT", "https://chatgpt.com"),
            ("Google Gemini", "https://gemini.google.com"),
        ],
        "next": "Next track: PE-01, Basic Prompting. Better questions produce "
                "fewer gaps to fill, which is the cheapest hallucination "
                "control there is.",
    },

    "glossary": [
        ("Hallucination", "A confident, invented answer. Usually a quote, a "
                          "figure, a name or a reference."),
        ("Grounding", "Giving the tool the actual source text, so its answer "
                      "has something real to stand on."),
        ("Training data", "The public text a model learned from, up to a fixed "
                          "cut-off date."),
        ("Prompt", "Everything you type in: the request plus the facts you "
                   "supply."),
        ("Output", "What comes back. Your draft, which you are responsible for "
                   "checking."),
        ("Source", "A document, system or person you can point at. A model is "
                   "never one."),
    ],
}
