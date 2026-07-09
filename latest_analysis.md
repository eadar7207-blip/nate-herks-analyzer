# Nate Herk Analysis — July 9, 2026

## [Fable 5 Just Built Me a Business With One Prompt](https://www.youtube.com/watch?v=R0qF17BVl9w)
*July 8, 2026*

WHAT IT'S ABOUT
Nate demonstrates the /goal command in Claude Code — a single instruction that lets Fable 5 (Claude's most capable model) work entirely on its own from start to finish. He gave Fable 5 one high-level prompt to build a business, left to go to the gym, and came back to find the whole thing complete — landing page copy, business structure, a demo video, and even sound effects. The video is a live proof-of-concept showing what "autonomous AI" actually looks like in practice, not just in theory.

THE KEY POINTS
- **The /goal command turns Fable 5 into an autonomous agent.** You give it one high-level objective — "build me a business" — and it plans sub-tasks, executes each one, checks its own output, and delivers a finished result. You don't type another word.
- **One prompt, complete output.** Nate didn't give follow-up instructions. Fable 5 broke the goal down itself, decided what to build, built it, and produced a deliverable — including sound effects for a video.
- **The bottleneck is no longer execution — it's deciding what to build.** When one prompt generates a full business output, the skill that matters is knowing which goal to give the model, not how to operate it step by step.
- **Fable 5 is still free on Claude plans through July 12.** Running /goal experiments now costs nothing — that window closes in days.
- **This is the "go to the gym" workflow.** Start the task, leave, come back to a deliverable. It's the closest thing to delegation without hiring anyone.

THE METHOD OR FRAMEWORK
Step 1 — Write one complete goal prompt: what you want built, who it's for, what "done" looks like, and any hard constraints. Front-load everything — the more specific the goal, the tighter the output.

Step 2 — Type /goal [your prompt] in Claude Code with Fable 5 active. The model takes over: it plans sub-tasks, executes each one, reviews its own work, and loops until the goal is satisfied.

Step 3 — Come back when it's done. Review the output, refine the goal if needed, and ship or iterate.

HOW THIS APPLIES TO AI REAL ESTATE
The /goal workflow is exactly what an AI real estate business needs for high-leverage deliverables. Instead of walking Claude through each step of a market analysis, type: "/goal Build a buyer's market analysis for [neighborhood] — 90-day sold comps, price-per-sqft trends, days on market, and a 3-paragraph executive summary for a first-time buyer. Format as a client-ready email, 400 words." Come back to a finished report. That shifts your role from operator (typing prompts step by step) to director (deciding which reports to run and for whom). At scale: 10 client reports before lunch, each started with one prompt.

ACTION STEP THIS WEEK
Before July 12 (free Fable 5 closes): Open Claude Code, switch to Fable 5 with /model fable. Write one /goal prompt for a deliverable you produce repeatedly — a neighborhood overview, a buyer brief, a listing description set. Example: /goal Write a market snapshot for [your target neighborhood] — median price, days-on-market trend, inventory vs. last year, and 3 buyer talking points. Client email tone, 400 words. Run it. Save the output as your starter template. That one test run becomes your proof of concept to show the first client.

BEST QUOTE
"I gave it a /goal prompt, went to the gym, and came back to this. Even the sound effects."

---

# Nate Herk Analysis — July 8, 2026

## [How I Make Opus Think Like Fable (5 easy steps)](https://www.youtube.com/watch?v=XTBWVVcF3Pk)
*July 7, 2026*

# WHAT IT'S ABOUT

Fable 5 costs twice as much as Opus 4.8, but Nate discovered that most of what makes Fable 5 feel smarter isn't in the model — it's in how it structures its reasoning. This video shows how to extract that reasoning pattern into a reusable Claude Code skill called "Fable Mode," so Opus 4.8 follows the same staged execution discipline as Fable 5. The result: Fable-quality outputs at half the price. He also walks through how to actually use effort levels and how to build a simple model routing table so each tier of model handles only the work it's priced for.

# THE KEY POINTS

- **The 5 gates are: Scope → Evidence → Attack → Verify → Report.** Each gate forces the model to complete one phase before moving to the next, eliminating the most common AI failure mode: diving into execution before the problem is defined.
- **Scope first, always.** The #1 reason AI outputs fail isn't capability — it's starting with the wrong problem definition. Scope forces the model to state what it's solving and what's out of scope before touching the task.
- **Evidence forces grounding before action.** Rather than reasoning from memory or guesses, the model must gather and cite its sources before forming conclusions — a habit Fable 5 has built in, which you can now install into Opus.
- **Verify can actually fail.** Unlike a soft "does this look right?" check, the Verify gate tests output against the success criteria from the Scope gate — it's binary pass/fail, not a subjective review.
- **The model routing table is the cost control layer.** Fable 5 for complex orchestration → Opus 4.8 + Fable Mode for deep single tasks → Sonnet 5 for standard execution → Haiku for high-volume repetitive work. Each tier only handles work it's priced for.
- **This is a skill, not a prompt.** Install it once as a Claude Code slash command or CLAUDE.md rule and it applies automatically to every future task.

# THE METHOD OR FRAMEWORK

Step 1 — **Scope**: Before touching the task, write out what you're solving, what counts as success, and what is explicitly out of scope.

Step 2 — **Evidence**: Gather the information, data, or context needed. The model doesn't guess or rely on training memory — it finds it.

Step 3 — **Attack**: Execute using only the scoped definition and gathered evidence. No freelancing beyond the scope.

Step 4 — **Verify**: Test the output against the success criteria from Step 1. Binary — pass or fail. If it fails, loop back to Evidence or Attack.

Step 5 — **Report**: Deliver the result with references to the evidence used and a clear statement of what was solved vs. what was out of scope.

Installation: search GitHub for "fable-mode claude skill" — it's a single markdown file you add to your Claude Code skills directory.

# HOW THIS APPLIES TO AI REAL ESTATE

Real estate analysis is exactly where models go wrong by skipping the Scope step. "What's a good price for this neighborhood?" produces generic answers unless you force scoping first: which city, which price tier, which property type, what comparison period, what's the client's exit strategy. Install Fable Mode in your real estate workflow and run every CMA through it: Scope the property analysis (neighborhood, bed/bath count, sold-in-90-days comparable criteria), Evidence (pull comps, days-on-market, price-per-sqft trends), Attack (run the valuation), Verify (does the recommendation match the comps — pass or fail?), Report (deliver to client with source citations). You now have a repeatable, auditable process for every CMA — and because it runs on Opus 4.8 instead of Fable 5, you're cutting your AI costs in half on every engagement.

# ACTION STEP THIS WEEK

Search GitHub for "fable-mode claude skill" (or "mrtooher/fable-mode"). Download the skill markdown file. Add it to your Claude Code skills directory. Run your next CMA through it with this Scope: "Find comparable 3-bed properties in [target neighborhood] sold in the last 90 days, within 10% of [target price]. Success = at least 3 valid comps with price/sqft variance under 15%." Compare the output to your usual approach. The structure alone will catch gaps you'd normally miss.

# BEST QUOTE

"Fable 5 is strong, but it's double the price of Opus — and most of what makes it feel smarter isn't in the model weights, it's in how it structures its reasoning. You can install that structure yourself."

---

# Nate Herk Analysis — July 6, 2026

## [Fable 5 + Karpathy's LLM Wiki is Basically Cheating](https://www.youtube.com/watch?v=hQvwMj7IJe4)
*July 3, 2026*

# WHAT IT'S ABOUT

Nate shows how to build a persistent, self-improving AI knowledge base — called an LLM Wiki — using Claude Code, Obsidian (a free note-taking app), and Andrej Karpathy's pattern for AI memory. The core insight: instead of feeding Claude raw files and watching it rediscover your knowledge every session, you let it write and maintain a cross-linked wiki once, then query that wiki forever. He fed all 36 of his YouTube video transcripts in one batch and Claude built the entire knowledge base in 14 minutes. He then uses Fable 5 as the reasoning layer on top.

# THE KEY POINTS

- **The wiki is a persistent artifact — it compounds.** Every new source you add makes it smarter. Knowledge doesn't disappear between sessions; it accumulates.
- **Token cost drops by ~95% vs. querying raw files.** One user consolidated 383 files and 100+ meeting transcripts; their Claude query costs fell by 95% because the wiki is far more compact than raw source material.
- Claude Code auto-generates cross-linked pages for every tool, technique, and concept — you don't write any of the wiki yourself.
- **Fable 5 as orchestrator, not workhorse.** Put Fable 5 in charge of reasoning over the wiki; cheaper models handle routine queries.
- The full build takes about 5 minutes to set up and 14 minutes to process 36 video transcripts.
- Obsidian is the interface — files live locally, no subscriptions, no lock-in.

# THE METHOD OR FRAMEWORK

Step 1 — Drop sources into a folder. Transcripts, PDFs, meeting notes, video content — anything you want Claude to know.

Step 2 — Claude Code reads and writes wiki pages. It creates one page per concept/tool/technique, with backlinks between related pages.

Step 3 — Add routing rules. Tell Claude which types of queries draw from which sections of the wiki.

Step 4 — Query the wiki, not the files. Future questions are answered from the structured wiki, which is far smaller and more precise than the raw sources.

Step 5 — Feed new sources as they arrive. The wiki updates itself; it never forgets what it already built.

# HOW THIS APPLIES TO AI REAL ESTATE

A real estate AI consulting business runs on repeated knowledge: local market data, property types, client needs, past analyses, scripts that worked, comparables databases. Right now that knowledge likely lives in scattered files — spreadsheets, PDFs, past Claude sessions that vanish. Build an LLM wiki for your real estate practice. Feed it: every CMA you've run, every listing description you've written, every client Q&A, your local market research. Claude Code builds a cross-linked knowledge base. When a new client asks "what's the cap rate trend in downtown Phoenix this year?" — Claude answers from your curated wiki, not from a cold search. It's like having a junior analyst who has read every file you've ever touched and can find anything in seconds. Show a client this system in action and you have an immediate differentiator: "Our AI knows this market from the inside."

# ACTION STEP THIS WEEK

Open Claude Code. Create a folder called /real-estate-wiki. Drop in your last 5 CMAs, your top 3 listing descriptions, and any market research notes you have. Run: "Read all files in this folder. Create a wiki with one page per concept — neighborhoods, property types, pricing methods, client objections. Add backlinks between related pages." You'll have a working knowledge base in under an hour that every future session can draw from.

# BEST QUOTE

"Instead of asking an LLM to rediscover your knowledge from raw files every time, you let it maintain a persistent wiki that keeps improving as new sources come in."

---

## [How Claude is Creating a New Generation of Millionaires](https://www.youtube.com/watch?v=pbrln2TVeh4)
*July 3, 2026*

# WHAT IT'S ABOUT

Nate drops the theory and shows real outcomes: people who acted on AI automation skills are winning contracts, running companies without engineers, and scaling to seven figures — using Claude as their execution layer. He makes a pointed argument: the wealth window is open right now, but it is closing fast as the market gets more educated. This is not a "someday" video — it's a "this week" video.

# THE KEY POINTS

- **A 3-person team just won a state government contract by building with Claude** — a deal that previously required a large technical team. The competitive edge was AI execution speed, not headcount.
- Founders are running full companies without writing a line of code — Claude Code handles technical execution; the founder handles the relationship and direction.
- **The opportunity window is closing.** Early movers capture the largest contracts before the market normalizes. Nate himself built an AI automation agency to $100K+/month, then sold it.
- The 5-step playbook doesn't require a technical background — niche selection and client relationships are the real skills.
- **The constraint is not capability — it's speed to market.** Claude can build what you need. The question is whether you ship before the market catches up.
- Nate's community has 350,000+ members; the video features student success stories, not hypotheticals.

# THE METHOD OR FRAMEWORK

Step 1 — Pick a niche. One specific type of business (real estate agents, property managers, mortgage brokers). Narrow beats broad.

Step 2 — Build one automation. A lead follow-up sequence, a listing data puller, a document formatter — one real workflow, automated end-to-end.

Step 3 — Land one client. Show one person in that niche the time savings. Charge for the outcome, not the hours.

Step 4 — Productize. Turn what you built into a repeatable package with a fixed price.

Step 5 — Scale. Use templates and SOPs to deliver the same product to more clients without starting from scratch each time.

# HOW THIS APPLIES TO AI REAL ESTATE

Real estate is the perfect niche for this playbook — it has clear, repeated workflows, agents who are not technical, and a strong willingness to pay for time savings. The 3-person state contract story is directly analogous: an AI real estate consulting firm of 1–3 people can now compete for enterprise-level clients (large brokerages, property management companies, REITs) that previously required large teams. The move is to productize one high-value workflow — for example, a fully automated CMA report that an agent can generate in 2 minutes — and price it as a monthly service. The brokerage pays $500/month, you deliver 50 CMAs, you make $25K/month at scale. The window is right now: most agents still think AI is a novelty.

# ACTION STEP THIS WEEK

Contact one real estate agent you know. Tell them: "I'm piloting an AI service that cuts CMA prep time from 45 minutes to under 5. I'll run your next 3 CMAs for free in exchange for feedback." Run the CMAs using Claude. Track the actual time difference. That case study is your sales asset. You now have proof, not a pitch.

# BEST QUOTE

"From a three-person team winning a state contract to founders running whole companies without writing code — this is the real story behind a new wave of wealth being built with Claude."

---

# Nate Herk Analysis — July 2, 2026

## [6 Simple Rules That Change How Fable 5 Works](https://www.youtube.com/watch?v=vcU85OrwuV0)
*July 2, 2026*

# WHAT IT'S ABOUT

Fable 5 is Anthropic's most capable model yet — and at 2× the price of Opus 4.8 ($10/$50 per million tokens), it's also the easiest to overspend on. Nate's six rules are designed to get Fable-level results without burning through budget before the free window closes July 7th. The central insight: most people use Fable 5 exactly like they used Sonnet, and that's where the waste happens.

# THE KEY POINTS

- **Effort level is the biggest cost lever — not model choice.** The `/effort` parameter (low → medium → high → xhigh → max) controls reasoning turns. Max effort uses roughly 6× the turns of low effort — a swing larger than the entire Sonnet-to-Opus price gap.
- **Give Fable 5 the right context upfront.** It front-loads reasoning on the first pass. Sparse context wastes expensive turns on clarifying questions. Front-load with role, goal, constraints, and format.
- **Fable 5 finishes faster than you expect** — often completing in fewer turns than a comparable Opus task, offsetting the 2× sticker price on the right jobs.
- **Know when it quietly hands off to Opus.** Safeguard-flagged requests get rerouted to Opus 4.8 internally — at Opus rates, not Fable rates.
- **The newer shared tokenizer produces up to 35% more tokens per the same text** vs pre-Opus-4.7 models — factor this into client cost estimates.
- **Use Fable 5 as an orchestrator, not a workhorse.** Put it in charge of the plan; let Sonnet 5 or Haiku execute sub-tasks.

# HOW THIS APPLIES TO AI REAL ESTATE

Use Fable 5 as an orchestrator for client engagement plans: strategy and task decomposition at Fable-level quality, execution (listing descriptions, follow-ups, CMAs) routed to Sonnet 5. Before July 7, run your most complex real estate workflow through Fable 5 at high effort to establish a quality baseline for client pitching.

# ACTION STEP THIS WEEK

Before July 7 (free window closes), pick your most complex real estate workflow. Run it through Fable 5 at `/effort high`, then again through Opus 4.8. Compare quality and token cost. You'll have a concrete data point for when Fable 5 is worth paying for — and can build it into your client pricing model.

# BEST QUOTE

"Fable 5 is strong, but it's double the price of Opus, and it's only free on Claude plans through July 7 — these are the rules that keep your costs in check."

---

## [Stanford's Method Turns Claude Into a PHD Level Research Team](https://www.youtube.com/watch?v=Tj3018n5MVg)
*July 2, 2026*

# WHAT IT'S ABOUT

Nate introduces the Stanford STORM method (from NAACL 2024 — a top academic NLP conference) and packages it as a free Claude Code skill. STORM runs a topic through five expert mindsets, maps where they disagree, then synthesizes a fully cited briefing — in about 5 minutes. Peer-reviewed testing showed this approach produces outputs 25% more organized than the next best method. Nate benchmarks it head-to-head against Claude Code's built-in Deep Research.

# THE METHOD OR FRAMEWORK

STORM works as a 4-prompt sequence:

1. **Multi-Perspective Scan** — Spin up five expert lenses: The Practitioner (daily experience), The Academic (peer-reviewed evidence), The Skeptic (counterarguments), The Economist (financial incentives), The Historian (precedent). Each delivers its own position, evidence, and unique insights.
2. **Contradiction Map** — Find where those five voices conflict. "The fights are where real understanding lives." Surfaces which perspective has the strongest evidence, what remains genuinely unresolved, and what blind spots the entire field shares.
3. **Synthesis** — Consolidate into a briefing: executive summary, ranked key findings, hidden connections, actionable insights, frontier questions.
4. **Peer Review** — Claude critiques its own output: confidence scores per claim, flags weak assertions, overall reliability grade.

The entire sequence completes in ~5 minutes vs 40–60 hours of human research.

# HOW THIS APPLIES TO AI REAL ESTATE

When a client asks "should I buy in this neighborhood?", a single Claude prompt gives one perspective. STORM gives five — practitioner (agent on the ground), academic (market research), skeptic (what could go wrong), economist (interest rate dynamics), historian (what happened in 2008, 2020) — then synthesizes them into a defensible recommendation. The "peer review" step is especially valuable: it flags claims Claude isn't confident in, giving client deliverables built-in uncertainty disclosure. No competing agent produces this.

# ACTION STEP THIS WEEK

Install Nate's free STORM Claude Code skill (linked in video description). Pick a real estate market question you hear often — e.g., "Is [your city] a buyer's or seller's market right now?" Run the full 4-prompt STORM sequence. Save the output as a PDF. You now have a demo to show any potential client as proof of your AI consulting's research quality.

# BEST QUOTE

"This one skill instantly levels up Claude's ability to research — it runs five expert brains on your topic, maps where they fight, and hands you a briefing no single prompt can touch."
