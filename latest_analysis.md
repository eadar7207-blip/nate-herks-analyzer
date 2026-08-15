# Nate Herk Analysis — August 15, 2026

## [Never Miss a Customer Call Again (AI Receptionist)](https://www.youtube.com/shorts/MmrKvQxtlwE)
*August 14 — YouTube Short*

WHAT IT'S ABOUT

A quick demonstration showing how to set up an AI receptionist that answers every inbound customer call 24/7, captures leads, and books appointments automatically — even when you (or your client) aren't available. Nate targets the most expensive missed-call problem in service businesses: a ringing phone that goes to voicemail equals a lost customer.

THE KEY POINTS

- **Every missed call is a lost lead.** AI receptionists answer in under one second, any time of day, and never put a caller on hold.
- The setup handles: answering, qualifying (is this a real lead?), booking directly into a calendar, and sending a confirmation text.
- **No code required.** Tools like GHL (GoHighLevel), n8n, or dedicated platforms like Dialzara handle the heavy lifting with pre-built templates.
- This short shows a live demo — the AI answers a real call, routes it, and books an appointment in a single take.

HOW THIS APPLIES TO AI REAL ESTATE

Property inquiries come in at all hours — someone sees a listing at 10pm, calls, and goes to voicemail. Your competition answers. An AI receptionist for a real estate team means every inbound inquiry gets an immediate, intelligent response: qualifying questions (budget, timeline, property type), answers to basic listing questions, and a showing booked into the agent's calendar. Charge this as a bolt-on to any real estate client's AI package: $500/month added to your retainer for 24/7 AI call coverage.

ACTION STEP THIS WEEK

Sign up for a free trial on Dialzara or configure an inbound voice agent inside n8n. Script out 5 qualifying questions for a real estate inquiry (budget, timeline, property type, location, pre-approved?). Test it by calling your own number. This is a ready-to-sell service.

BEST QUOTE

"Every missed call is a missed client. An AI receptionist doesn't sleep, doesn't put people on hold, and never has a bad day."

---

## [I Made Codex and Claude Code Build the Same App. Only One Made Me Want to Keep Using It.](https://www.youtube.com/watch?v=WCrnS09vpfo)
*August 14*

WHAT IT'S ABOUT

Nate gives both Claude Code and Codex the exact same prompt to build a full-stack app and films the raw results side by side. This is a direct sequel to his "100 Hours Testing" article and resolves the "which tool should I use?" question with real build data — not theory.

THE KEY POINTS

- **The core difference is the mental model, not the output quality.** Claude Code puts you in *steer* mode — you guide each step, review output, redirect as needed. Codex puts you in *dispatch* mode — you assign a task, wait for a result, and demand proof of completion.
- **Codex lasts longer per session** because GPT-5.5 is extremely token-efficient compared to Claude.
- Claude Code produced better code quality for complex, interdependent logic. Codex was faster for well-defined, isolated tasks.
- **Best workflow: use both from the same directory.** Plan with Claude, dispatch to Codex, review back in Claude.
- Claude skills don't automatically transfer to Codex — you need portable context that works in both environments.

THE METHOD OR FRAMEWORK

Nate's two-tool workflow:
1. **Brainstorm & plan in Claude Code.** Use Claude's reasoning to map out architecture, edge cases, and dependencies.
2. **Dispatch isolated tasks to Codex.** Well-defined subtasks are faster in Codex with better token efficiency.
3. **Review and integrate in Claude Code.** Claude understands full context; use it to review Codex output and catch anything that doesn't fit.

HOW THIS APPLIES TO AI REAL ESTATE

If you're building AI tools for real estate clients (property analysis scripts, lead qualification bots, listing description generators), this framework saves build time and money. Use Claude to architect the system and define exactly what each piece should do. Use Codex to build those pieces in parallel as clear tasks. Review output in Claude. You'll ship faster, spend fewer tokens, and produce more reliable code.

ACTION STEP THIS WEEK

Pick one automation you're building. Break it into 3-5 clearly defined modules. Plan the architecture in Claude Code. Then dispatch one module to Codex as a specific task and compare the output speed vs. doing it all in Claude.

BEST QUOTE

"Claude Code and Codex aren't competing tools. They train two opposite habits: steer the work, or dispatch it and demand proof."

---

## [Codex's Browser Agent Automates Literally Anything](https://www.youtube.com/watch?v=CB5bG4mvnS0)
*August 13*

WHAT IT'S ABOUT

Nate tests Codex's browser agent — a feature that lets Codex see a webpage, decide where to click, type into fields, stay signed in to logged-in sites, and save the entire process as a reusable skill. He calls it "probably the best browser operator I've tested" and shows it completing a multi-step financial workflow on the first attempt.

THE KEY POINTS

- **Codex can now operate browsers like a human:** it sees the page visually, understands what's clickable, navigates authenticated portals, and completes multi-step sequences.
- The demo: asked it to open Accounts, find Statements, download CSVs for two accounts, and file them in the correct folder. **Completed the entire workflow on the first attempt** and saved the process as a reusable skill.
- Saved skills mean you run it once, and Codex repeats the same browser sequence on demand — without you present.
- **The decision hierarchy for automation:** Use an API first (most reliable). Use a deterministic macro second. Use AI browser automation only when the task genuinely requires vision or human-like judgment.
- This closes the "I can't automate that" gap — any website with a login and a clickable UI is now automatable.

THE METHOD OR FRAMEWORK

Nate's three-tier automation decision tree:
1. **API first.** If the platform has an API, use it. Faster, cheaper, more reliable.
2. **Deterministic macro second.** If no API, use keyboard shortcuts, Selenium, or scripted clicks.
3. **AI browser agent last.** Only when the task requires vision or dynamic navigation. Codex's browser agent slots in here.

HOW THIS APPLIES TO AI REAL ESTATE

Real estate workflows are full of manual web tasks with no API: pulling property records from county assessor sites, downloading rent rolls from landlord portals, checking MLS for status changes. Every one of these is now a candidate for a Codex browser agent. Build a skill that logs into a county assessor portal, pulls recent sales in a target zip code, and files them into a spreadsheet — fully automated, on a schedule. That's a service real estate investors will pay for monthly.

ACTION STEP THIS WEEK

Identify one manual web task in a real estate workflow that has no API and is done repeatedly. Write out the exact click-by-click steps a human takes. That's your Codex browser agent spec. You don't need to build it yet — the spec is what you sell first.

BEST QUOTE

"It can see a page, decide where to click, type into fields, stay signed in to websites, and save the whole process as a reusable skill. Completed the whole workflow on the first attempt."

---

## [I Deleted All My Claude Skills... And Claude Got Smarter](https://www.youtube.com/watch?v=XNQBCRcwXV4)
*August 12*

WHAT IT'S ABOUT

Nate introduces a framework for thinking about Claude Code skills — then makes a surprising move: he deleted most of his installed skills and found Claude performed the same or better without them. The lesson is about understanding which type of skill actually adds value as Claude's base model improves.

THE KEY POINTS

- Nate defines two categories: **Capability Uplift** skills (teach Claude something it genuinely couldn't do before) and **Encoded Preference** skills (encode how *you* want Claude to do something it already knows how to do).
- **Capability uplift skills have a lifespan:** as the base model improves, Claude learns those capabilities natively and the skill stops adding value. They're doomed by the next model release.
- **Encoded preference skills never go stale** because they encode your judgment — your NDA review checklist, your commit message format, your code review standards — not Claude's missing knowledge.
- The experiment: Nate deleted his capability uplift skills, ran the same tasks, and found Claude 5's base model had already caught up. Those skills were adding noise rather than capability.
- The surviving skills that actually matter are all encoded preferences: his standards, his voice, his checklists.

THE METHOD OR FRAMEWORK

Skill audit process:
1. List every Claude skill you have installed.
2. For each one, ask: "Is this teaching Claude a new *ability*, or encoding my specific *preference* for how to do something it already knows?"
3. If it's a capability skill, test whether Claude 5 can do the same task without it. Often it can.
4. Delete capability skills that no longer add value. Keep all preference skills.
5. What survives is a lean, high-signal skill set that gets better with each model release rather than fighting it.

HOW THIS APPLIES TO AI REAL ESTATE

Audit your current Claude skills: a skill that "teaches Claude to write listing descriptions" is a capability skill that newer models handle natively. A skill that encodes *your* specific listing description format — your bullet structure, your headline formula, your local market tone — is a preference skill that will always add value. Every real estate workflow has standards that should be codified: how to analyze a CMA, how to structure a client report, what to include in a due diligence summary. Those become permanent, compounding assets in your AI stack.

ACTION STEP THIS WEEK

Audit your Claude skills this week. For each one, classify it as capability uplift or encoded preference. Test your capability skills by running the same task without them on Claude 5. Delete the ones that don't add anything. Write one new encoded preference skill that documents a real estate standard you hold that Claude doesn't know yet.

BEST QUOTE

"Capability uplift skills are doomed by the next model release. Encoded preference skills compound. Know which is which."

---

## [Grok Bot is For Real. What You Need to Know.](https://www.youtube.com/watch?v=PQBYZQqan2g)
*August 12*

WHAT IT'S ABOUT

xAI launched Grok Bot on August 11, 2026 — a persistent AI teammate product that goes beyond chat or coding tools. Nate breaks down what Grok Bot actually is, how it differs from every other AI agent product, and why he thinks it's the most credible new competitor to established automation workflows. He built a multi-agent website workflow in 20 minutes to demonstrate.

THE KEY POINTS

- **Grok Bot is not a chatbot — it's a persistent AI teammate.** Each bot gets its own cloud computer, its own saved logins, and keeps working after you close your device.
- **Agent computers:** every Grok Bot runs on a dedicated virtual machine with memory, a browser, and the ability to stay signed in to your tools.
- **Teachable skills:** train a bot by demonstrating a workflow once. The bot saves the skill and can repeat it on demand or on a schedule.
- **Scheduled routines:** bots can run tasks automatically — daily reports, weekly audits, nightly data pulls — without any trigger from you.
- **Slack integration and multi-agent messaging:** bots can be triggered from Slack and can message each other to hand off tasks (Researcher → Writer → Publisher pipeline).
- Pricing: approximately **$200/month** on the SuperGrok tier (launched August 11, 2026).
- Key limitation: still in beta, occasional reliability issues. Not production-ready for mission-critical workflows yet.

THE METHOD OR FRAMEWORK

Nate's 20-minute Grok Bot setup for a multi-agent workflow:
1. **Define the output** — what does the completed task look like?
2. **Break it into agent roles** — each becomes a separate bot with a clear job.
3. **Assign persistent credentials** — give each bot the logins it needs.
4. **Set the handoff signal** — one bot messages another in Slack when its job is done.
5. **Schedule the trigger** — set the first bot to start at a specific time; the pipeline runs itself.

HOW THIS APPLIES TO AI REAL ESTATE

This opens a new service category: *persistent AI agents that run client workflows around the clock*. A concrete example: a Grok Bot fleet for a property management company — one bot monitors rental listing platforms and flags new comparable listings each morning, a second bot pulls maintenance request tickets and drafts response templates, a third bot generates a weekly owner report. All three run on a schedule, hand off to each other, and drop the final report into the owner's inbox every Friday. Build it once, charge $5K setup and $3K/month retainer. This is a new recurring revenue line that didn't exist two weeks ago.

ACTION STEP THIS WEEK

Sign up for SuperGrok ($200/mo) and build one Grok Bot that handles a single, repeatable task for your business or a client's. Start small: a bot that monitors a specific real estate data source and sends you a daily summary in Slack. Get comfortable with the teachable skills interface. Early familiarity is the advantage here.

BEST QUOTE

"A Grok Bot isn't a chat window. It's a teammate with its own computer, its own logins, and a job it keeps doing after you log off."
