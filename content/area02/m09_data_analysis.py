# -*- coding: utf-8 -*-
"""DW-04 — Data Analysis with AI. Content only."""

DECK = {
    "module_code": "DW-04",
    "area": "02-ai-daily-work",
    "filename": "02-04-data-analysis-with-ai.pptx",
    "title": "Data Analysis with AI",
    "subtitle": "Getting a straight answer out of your numbers, without "
                "letting it do the arithmetic.",
    "duration_min": 18,
    "audience": "New joiners + staff",
    "motif": "flow",
    "cover_image": "assets/hero-data-analysis.jpg",

    "why": {
        "title": "Deepa's total is out by nine lakh",
        "icon": "sheet",
        "scenario": "Deepa pastes forty rows of dispatch values into an AI "
                    "tool and asks for the total and the top five customers. "
                    "The answer is instant, formatted beautifully, and the "
                    "total is wrong by about nine lakh rupees.",
        "cost": "A number that reached the MIS pack before anyone re-added it.",
        "fix": "Let it describe and structure. Let Excel do the arithmetic.",
    },

    "outcomes": [
        ("sheet", "Split a task into the arithmetic part and the language part"),
        ("check", "Never let a model add up a column again"),
        ("eye", "Ask questions of data that AI can genuinely answer"),
        ("doc", "Turn a set of figures into a summary that states no causes"),
        ("shield", "Analyse company numbers without exposing customers"),
    ],

    "sections": [
        ("Why totals go wrong", "It predicts, it does not calculate", "s_why"),
        ("The safe split", "Excel calculates, AI explains", "s_split"),
        ("Questions it can answer", "About shape, not about truth", "s_ask"),
        ("Describing without explaining", "Movements, never causes", "s_desc"),
        ("Do this now", "Summarise a real set of figures", "s_do"),
        ("Choose what you'd do", "A Monday morning decision", "scenario"),
        ("Watch this", "A 12-minute outside walkthrough", "video"),
    ],

    "slides": [
        {
            "anchor": "s_why",
            "label": "Why totals go wrong",
            "title": "It predicts, it does not add",
            "lead": "A total is text to it, produced the same way as a "
                    "sentence. Short sums usually work. Long ones drift.",
            "visual": {
                "type": "flow",
                "steps": [
                    ("You paste forty rows", "It reads them as text, not as a "
                                             "column."),
                    ("It produces a total", "The most likely number-shaped "
                                            "answer."),
                    ("It looks exactly right", "Correct digit count, sensible "
                                               "magnitude."),
                    ("Nobody re-adds it", "Because it came back formatted and "
                                          "confident."),
                ],
            },
        },
        {
            "label": "Why totals go wrong",
            "title": "Where the arithmetic breaks",
            "visual": {
                "type": "split",
                "left": {
                    "tag": "Usually fine", "tone": "neutral", "mark": "check",
                    "title": "Small and simple",
                    "items": [
                        "Adding four or five numbers",
                        "A percentage of one figure",
                        "Comparing two values",
                        "Converting one unit to another",
                    ],
                },
                "right": {
                    "tag": "Do not trust", "tone": "bad",
                    "title": "Long or layered",
                    "items": [
                        "Totalling a column of forty rows",
                        "Averages across grouped categories",
                        "Percentage change across many periods",
                        "Anything that feeds a report or an invoice",
                    ],
                },
            },
        },
        {
            "anchor": "s_split",
            "label": "The safe split",
            "title": "Excel calculates, AI explains",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "TOTALS AND AVERAGES — Excel, every single time",
                    "SORTING AND RANKING — Excel, then paste the top five",
                    "DESCRIBING MOVEMENTS — AI, using your calculated figures",
                    "WRITING THE SUMMARY — AI, with no causes added",
                ],
            },
        },
        {
            "label": "The safe split",
            "title": "The two-minute workflow",
            "visual": {
                "type": "steps",
                "items": [
                    "Do the sums in Excel. SUM, AVERAGE, a pivot if you need "
                    "one.",
                    "Copy out only the handful of results that matter.",
                    "Paste those results into the tool, not the raw rows.",
                    "Ask for the summary, with no causes and no extra figures.",
                ],
                "prompt": "Below are calculated figures from our monthly pack. "
                          "Write a 150-word summary naming the three largest "
                          "movements and nothing else. Do not calculate "
                          "anything. Do not suggest causes. Do not add any "
                          "figure that is not in my list.",
                "caption": "\"Do not calculate anything\" is the line that "
                           "keeps this safe.",
            },
        },
        {
            "anchor": "s_ask",
            "label": "Questions it can answer",
            "title": "Questions it answers well",
            "lead": "Anything about the shape of the data, once you have "
                    "supplied the numbers.",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "chat", "label": "How do I say this?",
                     "sub": "\"Describe a fall from 1.4 to 2.1 per cent "
                            "without sounding alarmist.\""},
                    {"icon": "list", "label": "What should I check?",
                     "sub": "\"What would you want to see before accepting "
                            "this trend as real?\""},
                    {"icon": "sheet", "label": "What shape is this?",
                     "sub": "\"Turn these eight results into a table with "
                            "three columns and no commentary.\""},
                ],
            },
        },
        {
            "label": "Questions it can answer",
            "title": "The questions-to-check prompt",
            "visual": {
                "type": "prompt_out",
                "header": "Copy this challenge prompt",
                "text": "Here are the figures and the conclusion I have drawn "
                        "from them. List the five questions a sceptical "
                        "manager would ask before accepting this conclusion. "
                        "Do not answer them and do not comment on whether my "
                        "conclusion is right.",
                "caption": "It cannot verify your data. It is very good at "
                           "predicting the questions.",
                "out_title": "What comes back",
                "out": [
                    "Five questions, usually including one about sample size "
                    "or period.",
                    "No opinion on your conclusion, because you ruled that "
                    "out.",
                    "You go and answer two of them before the meeting, not "
                    "during it.",
                ],
            },
        },
        {
            "anchor": "s_desc",
            "label": "Describing without explaining",
            "title": "Movements, never causes",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "Let it explain",
                "bad": [
                    "\"Rejections rose to 2.1 per cent, likely due to operator "
                    "changeover during the shift pattern change.\"",
                    "Your data contains no shift information at all.",
                    "Maintenance investigate changeover for two days.",
                ],
                "good_tag": "Describe only",
                "good": [
                    "\"Rejections rose from 1.4 to 2.1 per cent, the largest "
                    "movement in the pack.\"",
                    "Every word traces to a figure you calculated.",
                    "You then ring the line supervisor and find the real "
                    "cause.",
                ],
                "note": "Describing is arithmetic you already did. Explaining "
                        "is a claim about the world, and it was not there.",
            },
        },
        {
            "label": "Describing without explaining",
            "title": "What must never be pasted",
            "visual": {
                "type": "bandlist",
                "mark": "ban",
                "headline": "A data extract usually carries customers, not "
                            "just numbers.",
                "sub": "Aggregate first. Paste the summary, never the raw "
                       "table.",
                "cols": 2,
                "items": [
                    "Customer or account names against values",
                    "Employee names against output or attendance",
                    "Anything with a phone number, address or ID column",
                    "Unpublished financial results or margins",
                ],
            },
        },
        {
            "anchor": "s_do",
            "label": "Do this now",
            "title": "Do this now: summarise figures",
            "visual": {
                "type": "steps",
                "items": [
                    "Open the last set of numbers you had to write about.",
                    "In Excel, produce the six results that actually mattered.",
                    "Replace any customer names with \"Customer A, B, C\".",
                    "Paste those six lines with the prompt on the right.",
                ],
                "prompt": "Here are six calculated results. Write a 120-word "
                          "summary for a manager. Name the three biggest "
                          "movements in order of size. Do not calculate, do "
                          "not suggest causes, do not add any figure I have "
                          "not given you. Plain sentences, no bullet points.",
                "caption": "Six lines in, a usable paragraph out, nothing "
                           "identifying anyone.",
            },
        },
        {
            "label": "Do this now",
            "title": "Four checks before it goes out",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Every figure in the text matches my spreadsheet exactly.",
                    "No cause is stated that I did not establish myself.",
                    "No customer or employee is identifiable in the summary.",
                    "The tool calculated nothing — I did all the arithmetic.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Five mistakes people really make",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Pasting the raw table and asking for a total",
                     "The number comes back formatted and wrong, and it looks "
                     "exactly like a real total."),
                    ("Letting it name a cause",
                     "It will offer one confidently. Somebody then spends two "
                     "days on the wrong line."),
                    ("Pasting customer names with values",
                     "That is a customer list with commercial data attached, "
                     "leaving the company."),
                    ("Trusting a percentage it produced",
                     "Percentages are calculations. If you did not work it "
                     "out, do not print it."),
                    ("Asking it to \"analyse this data\"",
                     "Vague in, vague out. You get an essay about the general "
                     "shape of numbers."),
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "When to use a chart tool instead",
            "visual": {
                "type": "tree",
                "question": "Do I need a number, or a sentence about a number?",
                "yes": {
                    "path": "A sentence", "tone": "good", "label": "Use AI",
                    "detail": "Describing a movement, drafting the commentary, "
                              "shaping a table, listing what a sceptic would "
                              "ask. All language work.",
                },
                "no": {
                    "path": "A number", "tone": "bad", "label": "Use Excel",
                    "detail": "Totals, averages, percentages, rankings, "
                              "variances. Anything that will be printed, "
                              "invoiced or reported as a figure.",
                },
            },
        },
        {
            "label": "Do this now",
            "title": "What good analysis looks like",
            "visual": {
                "type": "nested",
                "layers": [
                    {"label": "The spreadsheet",
                     "sub": "Every figure calculated, checkable and yours."},
                    {"label": "The six results",
                     "sub": "Aggregated, anonymised, pasted in."},
                    {"label": "The paragraph",
                     "sub": "Written by the tool, describing only those six."},
                ],
                "note": "Each layer is smaller and safer than the one before "
                        "it. By the time anything reaches the tool, there is "
                        "nothing left to get wrong or to leak.",
            },
        },
        {
            "label": "Do this now",
            "title": "The data rule",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "If it will be printed as a number, a spreadsheet "
                            "must have produced it.",
                "sub": "AI writes the sentence around the number. It never "
                       "produces the number.",
                "cols": 3,
                "items": [
                    "Arithmetic — Excel.",
                    "Wording — the tool.",
                    "Causes — you, having checked.",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Monday, 9:30 am",
        "situation": "The MIS pack needs a commentary by eleven. You have a "
                     "forty-row dispatch table with customer names and values, "
                     "and no commentary written.",
        "choices": [
            {
                "text": "Paste the whole table and ask for totals and a "
                        "summary.",
                "tone": "bad",
                "headline": "Two problems in one paste",
                "consequence": "The total comes back wrong by nine lakh, "
                               "beautifully formatted, and nobody re-adds it. "
                               "At the same time, forty customer names with "
                               "their monthly values have left the company in "
                               "a single message.",
                "rule": "Never paste a raw table. Never accept a total you did "
                        "not calculate.",
            },
            {
                "text": "Total it in Excel, anonymise, then ask for the "
                        "commentary.",
                "tone": "good",
                "headline": "Ten minutes, and both problems disappear",
                "consequence": "Excel gives you the total, the top five and "
                               "the movements. You replace names with "
                               "Customer A to E and paste six lines. The "
                               "commentary comes back in 120 words, describing "
                               "only what you gave it. Sent at 10:15.",
                "rule": "Aggregate, anonymise, then ask for language.",
            },
            {
                "text": "Write the commentary yourself from the Excel totals.",
                "tone": "ok",
                "headline": "Correct, and slower than it needs to be",
                "consequence": "Every figure is right because you calculated "
                               "them. The writing takes forty minutes, and the "
                               "part that took forty minutes was the part a "
                               "tool does safely in twenty seconds once the "
                               "numbers are settled.",
                "rule": "Keep the arithmetic. Hand over the sentences.",
            },
        ],
    },

    # Title, channel and runtime were read back from YouTube
    # itself. See newvideos.json.
    "video": {
        "url": "https://www.youtube.com/watch?v=FKLr3ft8ea0",
        "title": "Master Data Analysis with ChatGPT (in just 12 minutes)",
        "channel": "Jeff Su",
        "duration": "11:54",
        "heading": "Twelve minutes, shown on screen",
        "note": "An outside video, not company material. Follow this "
                "module's rule on aggregating and anonymising before you "
                "paste.",
        "how": [
            "Optional. Excel still does the arithmetic.",
            "Useful for seeing the workflow demonstrated.",
            "It opens in your browser. Turn the sound on.",
        ],
    },

    "quiz": [
        {
            "q": "Why is a long total unreliable?",
            "remember": "It predicts text. It does not calculate.",
            "answers": [
                {"text": "The tool rounds aggressively", "ok": False,
                 "why": "Rounding is not what happens. The number is produced "
                        "as text, in the same way a sentence is, and over "
                        "forty rows that process drifts."},
                {"text": "It produces a likely number, not a computed one",
                 "ok": True,
                 "why": "Exactly. There is no addition happening. The result "
                        "has the right shape and magnitude, which is precisely "
                        "why nobody re-adds it."},
                {"text": "Long columns exceed its input limit", "ok": False,
                 "why": "Forty rows is well within any modern limit. The "
                        "problem is not that it cannot see the numbers, it is "
                        "that it does not add them."},
                {"text": "It sorts before adding", "ok": False,
                 "why": "It is not performing operations in any order. Nothing "
                        "resembling a calculation takes place at all."},
            ],
        },
        {
            "q": "Which task belongs in Excel?",
            "remember": "Anything that will be printed as a figure.",
            "answers": [
                {"text": "Describing a movement in plain English", "ok": False,
                 "why": "That is language work, and it is the part worth "
                        "handing over once the numbers are settled."},
                {"text": "The top five customers by value", "ok": True,
                 "why": "A ranking is a calculation. Sort in Excel, then paste "
                        "the five results if you need commentary on them — "
                        "with the names replaced."},
                {"text": "Listing what a sceptic would ask", "ok": False,
                 "why": "No arithmetic involved. Predicting the likely "
                        "questions is something these tools do genuinely "
                        "well."},
                {"text": "Turning six results into a table layout", "ok": False,
                 "why": "Formatting, not calculation. As long as you supply "
                        "the six numbers, reshaping them is safe."},
            ],
        },
        {
            "q": "What must you never let it add?",
            "remember": "Causes are claims about the world.",
            "answers": [
                {"text": "The order of the movements", "ok": False,
                 "why": "Ordering figures you supplied by size is safe, and "
                        "easy for you to check at a glance."},
                {"text": "An explanation of why a number moved", "ok": True,
                 "why": "It was not there and your figures contain no causes. "
                        "A plausible explanation gets acted on, and people "
                        "spend days fixing something that was never the "
                        "problem."},
                {"text": "A plain-English description of the change",
                 "ok": False,
                 "why": "Describing what you already calculated is the whole "
                        "point of using it here. Just check the figures match "
                        "your sheet."},
                {"text": "A heading for the summary", "ok": False,
                 "why": "Harmless formatting. Read it, as you would read any "
                        "line, but there is no risk peculiar to it."},
            ],
        },
        {
            "q": "How do you paste data safely?",
            "remember": "Aggregate first, anonymise second.",
            "answers": [
                {"text": "Paste the table but remove the header row",
                 "ok": False,
                 "why": "The header was never the problem. The customer names "
                        "in the first column are, and they are still there."},
                {"text": "Paste only calculated results, with names replaced",
                 "ok": True,
                 "why": "Six aggregated lines with Customer A to E carry "
                        "everything the tool needs to write a commentary and "
                        "nothing that identifies anyone."},
                {"text": "Paste it all — the numbers are meaningless without "
                         "context", "ok": False,
                 "why": "They are not meaningless. A customer list with "
                        "monthly values attached is commercially sensitive and "
                        "personal data in most jurisdictions we operate in."},
                {"text": "Paste it into a personal account instead", "ok": False,
                 "why": "That makes it worse, not better. The account is the "
                        "part that removes any record, control or ability to "
                        "delete."},
            ],
        },
        {
            "q": "Which question suits AI best?",
            "remember": "About shape and language, not about truth.",
            "answers": [
                {"text": "\"What is the total of this column?\"", "ok": False,
                 "why": "Arithmetic. It will answer, the answer will look "
                        "right, and over forty rows it will frequently be "
                        "wrong."},
                {"text": "\"What would a sceptical manager ask about this?\"",
                 "ok": True,
                 "why": "Predicting likely objections is language work drawn "
                        "from very common patterns. Even an imperfect list "
                        "makes you better prepared for the meeting."},
                {"text": "\"Is this trend statistically significant?\"",
                 "ok": False,
                 "why": "A calculation requiring your full dataset and a "
                        "method. It will produce a confident verdict with no "
                        "computation behind it."},
                {"text": "\"What caused this variance?\"", "ok": False,
                 "why": "It has no access to anything that would explain your "
                        "variance. You will get a plausible cause that "
                        "somebody then investigates."},
            ],
        },
    ],

    "recap": {
        "title": "Data analysis on one screen",
        "points": [
            ("It does not calculate",
             "A total is produced as text. Over a long column it drifts, and "
             "looks fine."),
            ("Excel first, always",
             "Totals, averages, percentages and rankings before anything is "
             "pasted."),
            ("Paste results, not raw rows",
             "Six aggregated lines instead of forty rows with customers "
             "attached."),
            ("Describe, never explain",
             "It can word a movement. It cannot know why the movement "
             "happened."),
            ("Anonymise before pasting",
             "Customer A to E works perfectly well and exposes nobody."),
            ("Check every figure back",
             "Each number in the text must match your spreadsheet exactly."),
        ],
        "oneliner": "If it will be printed as a number, a spreadsheet must "
                    "have produced it.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("sheet", "The results-into-summary prompt",
             "Three movements, no calculating, no causes."),
            ("eye", "The sceptical-manager prompt",
             "Five questions they would ask, unanswered."),
            ("shield", "The aggregate-and-anonymise habit",
             "Excel first, Customer A to E, then paste."),
        ],
        "links": [
            ("Microsoft Copilot", "https://copilot.microsoft.com"),
            ("ChatGPT", "https://chatgpt.com"),
            ("Google Gemini", "https://gemini.google.com"),
        ],
        "next": "Next module: DW-05, Excel with AI. Getting the formula "
                "written for you, and testing it on one row before you trust "
                "the column.",
    },

    "glossary": [
        ("Aggregate", "A calculated summary — a total, an average, a top five "
                      "— rather than the underlying rows."),
        ("Anonymise", "Replacing names and identifiers with labels like "
                      "Customer A, so nobody can be identified."),
        ("Movement", "A change between two periods. Something you calculate "
                     "and the tool describes."),
        ("Cause", "Why something changed. Only established by you, never by "
                  "the tool."),
        ("Prompt", "Everything you type in: your calculated figures and the "
                   "constraints."),
        ("Output", "What comes back. Your draft, which you are responsible for "
                   "checking."),
    ],
}
