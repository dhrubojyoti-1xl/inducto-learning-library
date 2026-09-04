# -*- coding: utf-8 -*-
"""SEC-03 — Multi-Factor Authentication. Content only."""

DECK = {
    "module_code": "SEC-03",
    "area": "05-security-privacy",
    "filename": "05-03-multi-factor-authentication.pptx",
    "title": "Multi-Factor Authentication",
    "subtitle": "The second lock that makes a stolen password almost useless — "
                "and the one way people still get past it.",
    "duration_min": 15,
    "audience": "Mandatory for all staff",
    "motif": "shield",
    "cover_image": "assets/hero-mfa-identity.jpg",

    "why": {
        "title": "Ayesha's password worked. It failed.",
        "icon": "lock",
        "scenario": "Ayesha handles HR records in Dubai. Her password leaked "
                    "in a breach at a site she had forgotten about. Someone "
                    "used it at 2am. They got the password right and still "
                    "could not get in, because a code went to her phone.",
        "cost": "Nothing at all — which is the entire point of the story.",
        "fix": "One extra step at login, and a stolen password stops being "
               "enough.",
    },

    "outcomes": [
        ("lock", "Explain what a second factor is, without jargon"),
        ("eye", "Choose the strongest option your systems offer"),
        ("warn", "Recognise an MFA fatigue attack and stop it correctly"),
        ("key", "Know what to do when you lose the phone with your codes"),
        ("shield", "Never approve a prompt you did not personally trigger"),
    ],

    "sections": [
        ("What a second factor is", "Something you have", "s_what"),
        ("Which type is strongest", "Not all are equal", "s_types"),
        ("The fatigue attack", "The one way past it", "s_fatigue"),
        ("Losing your phone", "Before it happens", "s_lost"),
        ("Do this now", "Check your own setup", "s_do"),
        ("Choose what you'd do", "A 2am decision", "scenario"),
        ("Watch this", "A 3-minute outside explainer", "video"),
    ],

    "slides": [
        {
            "anchor": "s_what",
            "label": "What a second factor is",
            "title": "Something you know, something you have",
            "lead": "Security people group proof of identity into three "
                    "kinds: something you know (a password), something you "
                    "have (your phone or a security key), and something you "
                    "are (a fingerprint or your face). MFA means adding a "
                    "second kind — in the systems you use day to day, "
                    "usually something you have.",
            "visual": {
                "type": "flow",
                "steps": [
                    ("You enter the password", "Something you know. It may "
                                               "already have leaked."),
                    ("A second proof is asked for", "Something you have, "
                                                    "usually your phone."),
                    ("Only you can supply it", "Because the phone is in your "
                                               "pocket, not in a leaked list."),
                    ("A stolen password fails", "Which is the whole point of "
                                                "the second step."),
                ],
            },
        },
        {
            "label": "What a second factor is",
            "title": "Why it matters so much",
            "visual": {
                "type": "split",
                "left": {
                    "tag": "Password only", "tone": "bad",
                    "title": "One thing between them and us",
                    "items": [
                        "A leaked password works immediately",
                        "You have no idea it has been used",
                        "It works from anywhere in the world",
                        "It keeps working until you change it",
                    ],
                },
                "right": {
                    "tag": "Password plus a factor", "tone": "good",
                    "title": "Two things, one of them physical",
                    "items": [
                        "A leaked password alone achieves nothing",
                        "You are told the moment somebody tries",
                        "They would need the phone in your pocket",
                        "You find out and change it the same day",
                    ],
                },
            },
        },
        {
            "anchor": "s_types",
            "label": "Which type is strongest",
            "title": "Not all factors are equal",
            "gloss": ["Authenticator app"],
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "STRONGEST — a security key or passkey, tied to the real "
                    "site",
                    "STRONG — an authenticator app showing a rotating code",
                    "WEAKER — a push notification you tap to approve",
                    "WEAKEST — a code sent by SMS, which can be intercepted",
                ],
            },
        },
        {
            "label": "Which type is strongest",
            "title": "Any factor beats none",
            "visual": {
                "type": "iconrow",
                "items": [
                    {"icon": "key", "label": "Use the best offered",
                     "sub": "If the system supports an app or a key, choose "
                            "that over SMS. It takes two minutes to set up."},
                    {"icon": "clock", "label": "SMS still helps",
                     "sub": "Weakest is not useless. A texted code still "
                            "defeats an attacker holding only your password."},
                    {"icon": "shield", "label": "Never turn it off",
                     "sub": "The inconvenience is a few seconds. The "
                            "protection is against the most common attack "
                            "there is."},
                ],
            },
        },
        {
            "anchor": "s_fatigue",
            "label": "The fatigue attack",
            "title": "The one way past it",
            "lead": "If they have your password, they can trigger approval "
                    "prompts on your phone. Over and over.",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Prompts arrive at 2am, repeatedly",
                     "The attacker is logging in with your password every few "
                     "seconds, hoping you tap once."),
                    ("You tap approve to stop the buzzing",
                     "That single tap is the entire breach. It is the only "
                     "step they could not do themselves."),
                    ("A call follows saying it is IT",
                     "\"We are testing, please approve the next one.\" IT will "
                     "never ask this."),
                    ("You approve while half asleep",
                     "Which is exactly why the prompts arrive at 2am rather "
                     "than at 2pm."),
                ],
            },
        },
        {
            "label": "The fatigue attack",
            "title": "What to do instead",
            "visual": {
                "type": "bandlist",
                "mark": "ban",
                "headline": "Never approve a prompt you did not personally "
                            "trigger, no matter how many arrive.",
                "sub": "An unexpected prompt means somebody already has your "
                       "password.",
                "cols": 3,
                "items": [
                    "Deny it, every time.",
                    "Change your password immediately.",
                    "Report it, even at 2am.",
                ],
            },
        },
        {
            "label": "The fatigue attack",
            "title": "The report wording",
            "visual": {
                "type": "prompt",
                "header": "Copy this wording",
                "text": "I am receiving repeated multi-factor approval prompts "
                        "that I did not trigger. I have denied all of them and "
                        "changed my password from a different device. The "
                        "prompts started at approximately [TIME] on [DATE]. "
                        "Please check for sign-in attempts on my account.",
                "caption": "Send this to your security contact, whatever the "
                           "hour.",
                "why": [
                    "It states clearly you denied them, which matters.",
                    "The time window is what they need to find the attempts.",
                    "It confirms the password was changed elsewhere, not on a "
                    "possibly compromised device.",
                ],
            },
        },
        {
            "anchor": "s_lost",
            "label": "Losing your phone",
            "title": "Before you lose the phone",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Save the backup codes somewhere offline, never on the "
                    "phone they unlock.",
                    "Register a second factor if the system allows it.",
                    "Know who to contact for a reset: [COMPANY INPUT NEEDED: "
                    "IT service desk route].",
                ],
            },
        },
        {
            "label": "Losing your phone",
            "title": "If it is lost or stolen",
            "visual": {
                "type": "steps",
                "items": [
                    "Report the loss to IT before you report it anywhere else.",
                    "Change your work password from a different device.",
                    "Ask for your authenticator registration to be reset.",
                    "Check your account's recent sign-in activity once you are "
                    "back in.",
                ],
                "prompt": "My phone with my authenticator app has been lost. "
                          "Please reset my multi-factor registration and check "
                          "for any sign-in attempts since [TIME] on [DATE]. I "
                          "have already changed my password from a different "
                          "device.",
                "caption": "Send this straight away. Speed matters far more "
                           "than tidiness.",
            },
        },
        {
            "anchor": "s_do",
            "label": "Do this now",
            "title": "Do this now: check your setup",
            "visual": {
                "type": "steps",
                "items": [
                    "Open your work account's security settings.",
                    "Check which second factor is registered against your "
                    "name.",
                    "If it is SMS and an app is offered, switch to the app.",
                    "Find your backup codes and store them away from your "
                    "phone.",
                ],
                "prompt": "Explain in plain English, for someone with no "
                          "technical background, the difference between "
                          "receiving a code by SMS, using an authenticator "
                          "app, and using a passkey. Six lines maximum. No "
                          "recommendations about specific products.",
                "caption": "Useful if you want to understand the choice before "
                           "making it.",
            },
        },
        {
            "label": "Do this now",
            "title": "Four habits worth having",
            "visual": {
                "type": "checklist",
                "cols": 2,
                "items": [
                    "Approve only prompts you triggered in the last few "
                    "seconds.",
                    "Deny anything unexpected, then change your password.",
                    "Never read a code aloud, to anyone, for any reason.",
                    "Keep backup codes somewhere that is not your phone.",
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "Five mistakes people really make",
            "visual": {
                "type": "mistakes",
                "items": [
                    ("Approving a prompt to make it stop",
                     "That tap is the only thing the attacker could not do "
                     "without you."),
                    ("Reading a code to somebody who rang",
                     "The call is the attack. Nobody legitimate has ever "
                     "needed your code."),
                    ("Turning MFA off because it is inconvenient",
                     "Seconds of friction against the most common attack "
                     "there is."),
                    ("Storing backup codes on the same phone",
                     "When the phone is lost, both factors are lost with it."),
                    ("Assuming a denied prompt needs no action",
                     "An unexpected prompt means your password is already "
                     "known. Change it."),
                ],
            },
        },
        {
            "label": "Do this now",
            "title": "An unexpected prompt means what?",
            "visual": {
                "type": "tree",
                "question": "Did I just try to log in, in the last minute?",
                "yes": {
                    "path": "Yes", "tone": "good", "label": "Approve it",
                    "detail": "You triggered it, it arrived immediately, and "
                              "it matches what you are doing. That is the only "
                              "situation in which approval is correct.",
                },
                "no": {
                    "path": "No", "tone": "bad", "label": "Deny and act",
                    "detail": "Somebody has your password and is using it "
                              "right now. Deny, change the password from "
                              "another device, and report it whatever the "
                              "time.",
                },
            },
        },
        {
            "label": "Do this now",
            "title": "The MFA rule",
            "visual": {
                "type": "bandlist",
                "tone": "accent",
                "headline": "Approve only what you started. An unexpected "
                            "prompt is a warning, not an annoyance.",
                "sub": "It is telling you, in real time, that your password is "
                       "already in somebody else's hands.",
                "cols": 3,
                "items": [
                    "You started it — approve.",
                    "You did not — deny and change.",
                    "Someone asks for the code — report.",
                ],
            },
        },
    ],

    "scenario": {
        "title": "Tuesday, 2:10 am",
        "situation": "Your phone buzzes with an approval prompt for your work "
                     "account. Then again. Then four more times in two "
                     "minutes. You are half asleep.",
        "choices": [
            {
                "text": "Approve one so the buzzing stops and deal with it in "
                        "the morning.",
                "tone": "bad",
                "headline": "That tap was the entire attack",
                "consequence": "The attacker already had your password — that "
                               "is why prompts were arriving. The one thing "
                               "they could not do was approve the second step. "
                               "You have just done it for them, and they are "
                               "now inside with your access.",
                "rule": "The prompts exist because they are stuck. Approving "
                        "unsticks them.",
            },
            {
                "text": "Deny them all, change your password from your laptop, "
                        "report it.",
                "tone": "good",
                "headline": "Three minutes at 2am, and nothing happens",
                "consequence": "Denying stops the attempts. Changing the "
                               "password from a different device removes the "
                               "thing they were relying on. The security "
                               "contact finds sign-in attempts from another "
                               "country and blocks them before morning.",
                "rule": "Deny, change elsewhere, report. In that order, at any "
                        "hour.",
            },
            {
                "text": "Turn the phone to silent and look at it after "
                        "breakfast.",
                "tone": "bad",
                "headline": "Six hours of unlimited attempts",
                "consequence": "The prompts continue all night. If you have "
                               "any other account using the same password, or "
                               "if a colleague approves something on a shared "
                               "system, the attacker gets in. By morning you "
                               "cannot tell what happened.",
                "rule": "Silence hides the alarm. It does not stop the "
                        "attempt.",
            },
        ],
    },

    # Title, channel and runtime were read back from YouTube
    # itself. See newvideos.json.
    "video": {
        "url": "https://www.youtube.com/watch?v=L3alw3iXaio",
        "title": "What is Multi-Factor Authentication",
        "channel": "IBM Technology",
        "duration": "3:02",
        "heading": "Three minutes on the second lock",
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
            "q": "What is a second factor?",
            "remember": "Something you have, not something you know.",
            "answers": [
                {"text": "A second, longer password", "ok": False,
                 "why": "Two passwords are two things you know, and both can "
                        "leak in the same way. The point is to add something "
                        "of a completely different kind."},
                {"text": "Something physical you have, like your phone",
                 "ok": True,
                 "why": "A leaked list can contain your password. It cannot "
                        "contain the phone in your pocket, which is why "
                        "stolen credentials stop being enough."},
                {"text": "A security question about your first school",
                 "ok": False,
                 "why": "Another thing you know, and usually findable on "
                        "social media. Security questions are among the "
                        "weakest protections there are."},
                {"text": "Logging in from the office network", "ok": False,
                 "why": "Location can be a useful signal for the security team "
                        "and it is not a factor you supply. It also fails "
                        "entirely for anyone working remotely."},
            ],
        },
        {
            "q": "Which factor is strongest?",
            "remember": "A key or passkey, then an app, then SMS.",
            "answers": [
                {"text": "A code sent by SMS", "ok": False,
                 "why": "The weakest of the common options, because numbers "
                        "can be redirected to another SIM. Still far better "
                        "than nothing, but choose an app if one is offered."},
                {"text": "A security key or passkey", "ok": True,
                 "why": "It checks the real address of the site, so it will "
                        "not work on a lookalike page at all. That defeats "
                        "phishing in a way codes cannot."},
                {"text": "An email to your other account", "ok": False,
                 "why": "If that account uses a leaked password too, you have "
                        "added no protection. It is also just another thing "
                        "you know, reached with a password."},
                {"text": "A security question", "ok": False,
                 "why": "Not really a factor at all. The answers are often "
                        "public, guessable, or already sitting in a previous "
                        "breach."},
            ],
        },
        {
            "q": "Six prompts arrive at 2am. Why?",
            "remember": "Somebody already has your password.",
            "answers": [
                {"text": "A system fault repeating a notification", "ok": False,
                 "why": "Possible in theory and rare in practice. Treat it as "
                        "an attack until somebody confirms otherwise — the "
                        "cost of being wrong is very one-sided."},
                {"text": "Somebody is logging in with your password right now",
                 "ok": True,
                 "why": "Prompts are only generated when the correct password "
                        "is entered. Repeated prompts mean repeated correct "
                        "entries, and none of them are yours."},
                {"text": "Your session expired overnight", "ok": False,
                 "why": "Expiry does not push approval prompts to your phone "
                        "at two in the morning. It asks you to sign in the "
                        "next time you use the system."},
                {"text": "Somebody is trying to guess your password",
                 "ok": False,
                 "why": "Wrong passwords never reach the second step. Reaching "
                        "your phone means the password stage has already been "
                        "passed."},
            ],
        },
        {
            "q": "Where do backup codes belong?",
            "remember": "Anywhere except the phone they unlock.",
            "answers": [
                {"text": "Saved in a note on the same phone", "ok": False,
                 "why": "When the phone is lost, both factors go with it. That "
                        "is precisely the situation the codes exist for."},
                {"text": "Somewhere offline and separate from your phone",
                 "ok": True,
                 "why": "A locked drawer at home, or an approved password "
                        "manager on a different device. The requirement is "
                        "that losing one does not lose both."},
                {"text": "Emailed to yourself", "ok": False,
                 "why": "Your email is one of the accounts they protect. If it "
                        "is compromised, the codes go with it, and email is "
                        "usually the first target."},
                {"text": "Shared with a colleague for emergencies", "ok": False,
                 "why": "That makes your account usable by somebody else "
                        "entirely, and destroys any record of who actually "
                        "signed in."},
            ],
        },
        {
            "q": "IT rings and asks you to approve.",
            "remember": "They never need it. Report the call.",
            "answers": [
                {"text": "Approve it — they are testing the system", "ok": False,
                 "why": "This is one of the most effective scripts there is, "
                        "because it explains the unexpected prompt. Real IT "
                        "can test without your approval and never asks for "
                        "it."},
                {"text": "Deny it, change your password, and report the call",
                 "ok": True,
                 "why": "The call plus the prompt together mean somebody has "
                        "your password and is trying to talk you past the "
                        "second step. Report the call as well as the prompts."},
                {"text": "Ask them to confirm your employee number first",
                 "ok": False,
                 "why": "They may well know it — employee numbers appear in "
                        "many documents. Verification questions do not help "
                        "when the caller has done their research."},
                {"text": "Approve it and then change your password", "ok": False,
                 "why": "Approval is instant and irreversible. Once you have "
                        "approved, they are inside, and changing the password "
                        "afterwards does not remove an active session."},
            ],
        },
    ],

    "recap": {
        "title": "MFA on one screen",
        "points": [
            ("Something you have",
             "A password can leak. The phone in your pocket cannot leak with "
             "it."),
            ("Pick the strongest offered",
             "Passkey or security key, then an authenticator app, then SMS."),
            ("Any factor beats none",
             "Even a texted code defeats an attacker holding only your "
             "password."),
            ("Approve only what you started",
             "An unexpected prompt means somebody already has your password."),
            ("Never read a code aloud",
             "There is no legitimate reason for anyone to ask for it."),
            ("Keep backup codes elsewhere",
             "Not on the phone they exist to replace."),
        ],
        "oneliner": "An unexpected prompt is not an annoyance. It is a warning "
                    "that your password is already in somebody else's hands.",
    },

    "toolkit": {
        "title": "Take these three things with you",
        "templates": [
            ("warn", "The fatigue-attack report",
             "Denied, password changed elsewhere, time window given."),
            ("key", "The lost-phone message",
             "Reset registration and check sign-ins since a stated time."),
            ("check", "The approve-or-deny test",
             "Did I start this in the last minute? If not, deny."),
        ],
        "links": [
            ("Check if your email has leaked", "https://haveibeenpwned.com"),
            ("India's data protection framework",
             "https://www.meity.gov.in/data-protection-framework"),
            ("UAE data protection laws", "https://u.ae/en/about-the-uae/"
                                         "digital-uae/data/data-protection-laws"),
        ],
        "next": "Next module: SEC-04, Data Protection Basics. What counts as "
                "personal data, and what the law expects us to do with it.",
    },

    "glossary": [
        ("Multi-factor authentication", "Proving who you are with two "
                                        "different kinds of proof: "
                                        "something you know, have or are — "
                                        "not a password alone."),
        ("Authenticator app", "An app showing a rotating code, tied to the "
                              "device rather than to a phone number."),
        ("Passkey", "A modern factor tied to the real website address, so it "
                    "cannot be used on a fake page."),
        ("MFA fatigue", "Flooding you with approval prompts until you tap one "
                        "to stop the noise."),
        ("Backup codes", "One-time codes for when you lose your phone. Stored "
                         "away from that phone."),
        ("One-time code", "A short code proving it is you. Never shared with "
                          "anyone, for any reason."),
    ],
}
