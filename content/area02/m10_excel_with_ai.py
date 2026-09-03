# -*- coding: utf-8 -*-
"""DW-05 — Excel with AI. Content only."""

DECK = {
    "module_code": "DW-05",
    "area": "02-ai-daily-work",
    "filename": "02-05-excel-with-ai.pptx",
    "title": "Excel with AI",
    "subtitle": "Formulas written for you, messy data cleaned up, and every "
                "one of them tested on a single row first.",
    "duration_min": 19,
    "audience": "New joiners + staff",
    "motif": "flow",

    "why": {
        "title": "Suresh gives up on VLOOKUP again",
        "icon": "sheet",
        "scenario": "Suresh schedules maintenance for a Coimbatore plant. He "
                    "needs to match 600 machine codes against a service "
                    "history sheet. He knows what he wants. He has never got "
                    "VLOOKUP to work, so he does it by hand every quarter.",
        "cost": "Two days a quarter, matching rows by eye.",
        "fix": "Describe the match in plain English. Test it on one row.",
    },

    "outcomes": [
        ("sheet", "Describe what you want and get a working formula back"),
        ("check", "Test any formula on one row before applying it to a column"),
        ("cycle", "Fix a formula error without understanding the error message"),
        ("doc", "Clean messy data without retyping a single cell"),
        ("shield", "Get Excel help without pasting the actual data"),
    ],

    "sections": [
        ("Describe, do not remember", "Plain English to formula", "s_describe"),
        ("The one-row test", "Before you fill down", "s_test"),
        ("Fixing errors", "Paste the message, not the sheet", "s_fix"),
        ("Cleaning messy data", "Without retyping", "s_clean"),
        ("Do this now", "Solve one real Excel problem", "s_do"),
        ("Choose what you'd do", "A quarter-end decision", "scenario"),
        ("Watch this", "An 8-minute outside walkthrough", "video"),
    ],

    "slides": [
        {
            "anchor": "s_describe",
            "label": "Describe, do not remember",
            "title": "Describe it in plain English",
            "lead": "You do not need to remember the syntax. You need to "
                    "describe the job precisely.",
            "visual": {
                "type": "flow",
                "steps": [
                    ("Name the columns", "\"Machine code is in column A, dates "
                                         "in column D.\""),
                    ("Say what you want", "\"Find the last service date for "
                                          "each code.\""),
                    ("Say what if missing", "\"Show 'no record' rather than "
                                            "an error.\""),
                    ("Ask for one formula", "\"Give me the formula only, no "
                                            "explanation.\""),
                ],
            },
        },
        {
            "label": "Describe, do not remember",
            "title": "The formula prompt",
            "visual": {
                "type": "prompt",
                "text": "I have machine codes in column A of Sheet1, and a "
                        "service history in Sheet2 with codes in column A and "
                        "dates in column D. In Sheet1 column B I want the most "
                        "recent service date for each code, and the words \"no "
                        "record\" if there is no match. Give me the formula "
                        "only, for Excel, with no explanation.",
                "caption": "Columns, sheets, what you want, what if missing.",
                "why": [
                    "Naming sheets and columns removes all the guesswork.",
                    "Saying what to show when there is no match avoids "
                    "#N/A everywhere.",
                    "\"Formula only\" saves you scrolling past three "
                    "paragraphs.",
                ],
            },
        },
        {
            "anchor": "s_test",
            "label": "The one-row test",
            "title": "Test it on one row first",
            "visual": {
                "type": "steps",
                "items": [
                    "Paste the formula into a single cell, not the whole "
                    "column.",
                    "Pick a row where you already know the correct answer.",
                    "Check the result matches what you know, exactly.",
                    "Only then fill it down the column.",
                ],
                "prompt": "The formula you gave me returns 14 March for "
                          "machine code M-2201, but the service sheet shows 2 "
                          "April for that code. Tell me what is wrong with the "
                          "formula and give me a corrected version. Formula "
                          "only.",
                "caption": "Naming a row you know the answer for is the whole "
                           "technique.",
            },
        },
        {
            "label": "The one-row test",
            "title": "Why the one-row test matters",
            "visual": {
                "type": "beforeafter",
                "bad_tag": "Filled straight down",
                "bad": [
                    "The formula looks right and produces 600 dates.",
                    "It has matched on the wrong column, so 600 dates are "
                    "plausible and wrong.",
                    "The maintenance schedule is built on them before anyone "
                    "notices.",
                ],
                "good_tag": "One row first",
                "good": [
                    "You test it on M-2201, where you know the answer is 2 "
                    "April.",
                    "It returns 14 March, so you catch it in ten seconds.",
                    "One correction, then 600 correct dates.",
                ],
                "note": "A wrong formula does not error. It produces six "
                        "hundred confident, wrong answers.",
            },
        },
        {
            "anchor": "s_fix",
            "label": "Fixing errors",
            "title": "Paste the error, not the sheet",
            "gloss": ["Personal data"],
            "visual": {
                "type": "split",
                "left": {
                    "tag": "Safe to paste", "tone": "good",
                    "title": "About the structure",
                    "items": [
                        "The formula itself",
                        "The error message: #N/A, #REF!, #VALUE!",
                        "Column letters and what each holds",
                        "One made-up example row",
                    ],
                },
                "right": {
                    "tag": "Never paste", "tone": "bad",
                    "title": "The actual data",
                    "items": [
                        "Customer names against values",
                        "Employee names, salaries or attendance",
                        "Real account or invoice numbers",
                        "The whole sheet, \"so it has context\"",
                    ],
                },
            },
        },
        {
            "label": "Fixing errors",
            "title": "The error-fixing prompt",
            "visual": {
                "type": "prompt_out",
                "header": "Copy this error prompt",
                "text": "This formula returns #N/A: [paste the formula]. "
                        "Column A holds machine codes like M-2201 as text. "
                        "Column D holds dates. Tell me the two most likely "
                        "causes and give me a corrected formula for each. "
                        "Formulas only, one line of explanation each.",
                "caption": "Describe what the columns hold. Never paste what "
                           "is in them.",
                "out_title": "What comes back",
                "out": [
                    "Two likely causes, usually including a text-versus-number "
                    "mismatch.",
                    "A corrected formula for each, ready to test on one row.",
                    "No data left your laptop, because you described it "
                    "instead.",
                ],
            },
        },
        {
            "anchor": "s_clean",
            "label": "Cleaning messy data",
            "title": "Cleaning without retyping",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "SPLIT — \"separate the code from the description in "
                    "column A\"",
                    "STANDARDISE — \"make every date show as DD-MM-YYYY\"",
                    "TRIM — \"remove trailing spaces and double spaces\"",
                    "FLAG — \"mark rows where the code does not match the "
                    "pattern\"",
                ],
            },
        },
        {
            "label": "Cleaning messy data",
            "title": "Ask for the steps, not the result",
            "lead": "For cleaning, the instructions are more useful than an "
                    "answer, because you keep control of the sheet.",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "list", "label": "Ask for the method",
                     "sub": "\"Give me the Excel steps to split this column\" "
                            "beats pasting the column in."},
                    {"icon": "sheet", "label": "Ask for a formula",
                     "sub": "A formula you paste in works on all 600 rows "
                            "and leaves the data where it is."},
                    {"icon": "check", "label": "Test on one row",
                     "sub": "Same rule as always. One known answer before you "
                            "fill anything down."},
                ],
            },
        },
        {
            "anchor": "s_do",
            "label": "Do this now",
            "title": "Do this now: solve one problem",
            "visual": {
                "type": "steps",
                "items": [
                    "Think of the Excel job you currently do by hand.",
                    "Write down which columns hold what, using letters.",
                    "Paste the prompt on the right with your description in "
                    "it.",
                    "Test the formula on one row you already know the answer "
                    "to.",
                ],
                "prompt": "In Excel, [column letters and what each holds]. I "
                          "want [what you want to happen] in column "
                          "[letter]. If there is no match, show [what "
                          "instead]. Give me the formula only, no "
                          "explanation. Do not ask me to paste my data.",
                "caption": "Five brackets. Covers most lookup and matching "
                           "jobs.",
            },
        },
        {
            "label": "Do this now",
            "title": "Four habits with Excel and AI",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Describe your columns. Never paste their contents.",
                    "Always test on one row where you know the answer.",
                    "Say what should happen when there is no match.",
                    "Keep the formulas that worked in a notes file.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Five mistakes people really make",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Filling down before testing",
                     "A wrong formula does not error. It gives six hundred "
                     "plausible wrong answers."),
                    ("Pasting the sheet to \"give it context\"",
                     "Customer names, values and account numbers all leave in "
                     "one paste."),
                    ("Asking it to calculate instead of writing a formula",
                     "The formula is checkable and repeatable. Its arithmetic "
                     "is neither."),
                    ("Not saying what to do when there is no match",
                     "You get #N/A across half the column and assume the "
                     "formula is broken."),
                    ("Accepting a formula you cannot read at all",
                     "You do not need to write it, but you do need to be able "
                     "to test and describe it."),
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Formula or macro?",
            "visual": {
                "type": "tree",
                "question": "Will I need to do this again next month?",
                "yes": {
                    "path": "Yes", "tone": "good", "label": "Ask for a formula",
                    "detail": "A formula lives in the sheet, updates when the "
                              "data changes, and anyone can see what it does. "
                              "Save the prompt that produced it.",
                },
                "no": {
                    "path": "No", "tone": "neutral", "label": "Ask for steps",
                    "detail": "For a genuine one-off, the menu steps are "
                              "faster and leave nothing behind for a colleague "
                              "to puzzle over later.",
                },
            },
        },
        {
            "label": "Do this now",
            "title": "What good use looks like",
            "visual": {
                "type": "nested",
                "layers": [
                    {"label": "You describe the sheet",
                     "sub": "Column letters and what each one holds."},
                    {"label": "It writes the formula",
                     "sub": "Syntax you never have to memorise."},
                    {"label": "You test one row",
                     "sub": "The step that turns a guess into a result."},
                ],
                "note": "Two days of matching rows by eye becomes twenty "
                        "minutes, and the sheet still contains every check a "
                        "colleague would want to see.",
            },
        },
        {
            "label": "Do this now",
            "title": "The Excel rule",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "Describe the sheet. Never paste the sheet. Always "
                            "test one row.",
                "sub": "Those three habits cover every safe use of AI with a "
                       "spreadsheet.",
                "cols": 3,
                "items": [
                    "Columns described — safe.",
                    "Data pasted — a breach.",
                    "One row tested — trustworthy.",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Quarter-end, 11:00 am",
        "situation": "Six hundred machine codes need matching to their last "
                     "service date. You have the two sheets open and no idea "
                     "how to write the lookup.",
        "choices": [
            {
                "text": "Paste both sheets in and ask it to do the matching.",
                "tone": "bad",
                "headline": "Two problems, and one of them is permanent",
                "consequence": "Six hundred rows of asset data leave the "
                               "company, and the matching it returns was "
                               "produced as text rather than calculated. You "
                               "cannot check six hundred results, so you check "
                               "none of them.",
                "rule": "Never paste the sheet. Never accept a result the "
                        "sheet did not calculate.",
            },
            {
                "text": "Describe the columns, get a formula, test it on one "
                        "known row.",
                "tone": "good",
                "headline": "Twenty minutes, and the sheet does the work",
                "consequence": "You describe the two sheets in three lines. "
                               "The formula comes back, you test it on M-2201 "
                               "where you know the answer, correct one thing, "
                               "and fill down. Six hundred correct dates, and "
                               "nothing left your laptop.",
                "rule": "Describe the structure, test one row, then fill down.",
            },
            {
                "text": "Match them by hand again, as you did last quarter.",
                "tone": "ok",
                "headline": "Reliable, and it costs you two days",
                "consequence": "The result is right, because you checked every "
                               "row. It also takes two days every quarter, and "
                               "next quarter it will take two days again, "
                               "because nothing was left behind in the sheet.",
                "rule": "A formula is the version of the work that survives to "
                        "next quarter.",
            },
        ],
    },

    "video": {
        "url": "https://www.youtube.com/watch?v=Rj7yrivdPbc",
        "title": "Excel Tutorial for Beginners — Learn with Copilot AI (Free "
                 "Tool!)",
        "channel": "Kevin Stratvert",
        "duration": "7:35",
        "heading": "Eight minutes, shown on screen",
        "note": "An outside video, not company material. Follow this module's "
                "rules on what you may paste.",
        "how": [
            "Optional. The prompts in this deck work as written.",
            "Useful if you learn Excel better by watching than reading.",
            "It opens in your browser. Turn the sound on.",
        ],
    },

    "quiz": [
        {
            "q": "What must you do before filling down?",
            "remember": "Test one row where you know the answer.",
            "answers": [
                {"text": "Check the formula looks correct", "ok": False,
                 "why": "A formula that looks correct can match on the wrong "
                        "column and still return plausible dates for every "
                        "row. Looking is not testing."},
                {"text": "Test it on one row where you know the answer",
                 "ok": True,
                 "why": "Ten seconds, and it is the only step that "
                        "distinguishes a working formula from one producing "
                        "six hundred confident errors."},
                {"text": "Ask the tool whether the formula is right",
                 "ok": False,
                 "why": "It will say yes, in the same confident voice it used "
                        "to give you the formula. It cannot see your sheet or "
                        "your data."},
                {"text": "Save a backup of the file", "ok": False,
                 "why": "Sensible generally, but it does not tell you whether "
                        "the formula works. You would simply have a backup of "
                        "a file with wrong results in it."},
            ],
        },
        {
            "q": "What is safe to paste for Excel help?",
            "remember": "Describe the columns. Never their contents.",
            "answers": [
                {"text": "The whole sheet, so it has full context", "ok": False,
                 "why": "It never needs the contents to write a formula. What "
                        "leaves the company in that paste is every customer, "
                        "value and account number in the file."},
                {"text": "The formula, the error message and what each column "
                         "holds", "ok": True,
                 "why": "That is everything required to diagnose a formula "
                        "problem, and none of it identifies anyone or reveals "
                        "any commercial figure."},
                {"text": "Twenty representative rows", "ok": False,
                 "why": "Twenty real rows is still twenty real records. If you "
                        "genuinely need to show a row, invent one with the "
                        "same shape."},
                {"text": "Just the customer column", "ok": False,
                 "why": "That is a customer list. It is one of the most "
                        "sensitive single columns in the sheet, not the safest "
                        "one."},
            ],
        },
        {
            "q": "Why say what to show when no match?",
            "remember": "Otherwise half the column reads #N/A.",
            "answers": [
                {"text": "It makes the formula shorter", "ok": False,
                 "why": "It makes it slightly longer. The gain is that the "
                        "result is readable rather than a column of error "
                        "codes."},
                {"text": "Otherwise you get errors you cannot interpret",
                 "ok": True,
                 "why": "Without it, every unmatched row shows #N/A, and you "
                        "cannot tell whether the formula is broken or the code "
                        "genuinely has no service record."},
                {"text": "The tool will refuse without it", "ok": False,
                 "why": "It will happily give you a formula without it. You "
                        "then spend twenty minutes wondering why half your "
                        "column looks broken."},
                {"text": "It stops the formula being slow", "ok": False,
                 "why": "Speed is unaffected on any realistic sheet. The "
                        "benefit is entirely about being able to read the "
                        "result."},
            ],
        },
        {
            "q": "Formula or calculated answer?",
            "remember": "A formula is checkable and repeats itself.",
            "answers": [
                {"text": "Ask for the calculated answer — it is faster",
                 "ok": False,
                 "why": "It is faster once and wrong at unpredictable "
                        "intervals. It also leaves nothing in the sheet, so "
                        "next quarter you start again from nothing."},
                {"text": "Ask for a formula and put it in the sheet", "ok": True,
                 "why": "Excel does the arithmetic, so it is correct. It "
                        "updates when the data changes, a colleague can see "
                        "what it does, and next quarter is already solved."},
                {"text": "Ask for both and compare them", "ok": False,
                 "why": "The comparison tells you little, and you have now "
                        "spent longer than writing the formula would have "
                        "taken. Trust the sheet, not the text."},
                {"text": "Ask it to check your existing numbers", "ok": False,
                 "why": "It cannot check arithmetic reliably. If you want a "
                        "check, build a second formula that should agree with "
                        "the first."},
            ],
        },
        {
            "q": "The formula returns the wrong date.",
            "stem": "You tested it on a row where you know the answer, and it "
                    "does not match.",
            "remember": "Give it the row, the expected value and the actual "
                        "one.",
            "answers": [
                {"text": "Ask it to try a completely different approach",
                 "ok": False,
                 "why": "You throw away a formula that may be one argument "
                        "from correct, and invite a new one with a new set of "
                        "problems to diagnose."},
                {"text": "Tell it the code, what you expected and what you "
                         "got", "ok": True,
                 "why": "That is enough to identify the fault almost every "
                        "time — usually an exact-match argument or a text "
                        "versus number mismatch. Ask for the corrected formula "
                        "only."},
                {"text": "Paste the two sheets so it can see the problem",
                 "ok": False,
                 "why": "It cannot see your sheets in any useful way, and you "
                        "would be exporting the data to solve a formula "
                        "problem that needs three lines of description."},
                {"text": "Fill it down anyway and check a few rows", "ok": False,
                 "why": "You already know it is wrong on a row where you knew "
                        "the answer. Filling down multiplies a known error six "
                        "hundred times."},
            ],
        },
    ],

    "recap": {
        "title": "Excel with AI on one screen",
        "points": [
            ("Describe, do not remember",
             "Name the sheets, the columns and what you want. Syntax is its "
             "job."),
            ("Say what to do when nothing matches",
             "Otherwise half the column shows an error code you then "
             "misdiagnose."),
            ("Test one row, every time",
             "A wrong formula does not error. It returns six hundred plausible "
             "answers."),
            ("Paste the error, never the sheet",
             "The formula and the column descriptions are all it needs."),
            ("Prefer a formula to an answer",
             "It lives in the sheet, updates itself, and solves next quarter "
             "too."),
            ("Keep the ones that worked",
             "A notes file of five working formulas saves the same fight "
             "twice."),
        ],
        "oneliner": "Describe the sheet. Never paste the sheet. Always test "
                    "one row.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("sheet", "The formula prompt",
             "Columns, what you want, what if missing, formula only."),
            ("cycle", "The error-fixing prompt",
             "The formula, the error, and what the columns hold."),
            ("check", "The one-row test",
             "A row you know the answer to, before you fill down."),
        ],
        "links": [
            ("Microsoft Copilot", "https://copilot.microsoft.com"),
            ("ChatGPT", "https://chatgpt.com"),
            ("Google Gemini", "https://gemini.google.com"),
        ],
        "next": "Next module: DW-06, Presentations with AI. Getting a "
                "structure and a story before you open PowerPoint at all.",
    },

    "glossary": [
        ("Formula", "An instruction Excel calculates itself. Checkable, "
                    "repeatable and safe."),
        ("Lookup", "Matching a value in one sheet against a table in another, "
                   "such as VLOOKUP or XLOOKUP."),
        ("#N/A", "Excel's way of saying it found no match. Usually a text "
                 "versus number problem."),
        ("One-row test", "Checking a formula against a row whose answer you "
                         "already know, before filling down."),
        ("Personal data", "Anything identifying a person: a name, a phone "
                          "number, an account, an employee number."),
        ("Prompt", "Everything you type in: your column descriptions and what "
                   "you want to happen."),
    ],
}
