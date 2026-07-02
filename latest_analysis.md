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

---

# Nate Herk Analysis — June 28, 2026

## [I asked Claude Code to make me as much money as possible](https://www.youtube.com/watch?v=iTY8Q449YNQ)
*June 25 at 12:00 AM*

# WHAT IT'S ABOUT

Nate ran an experiment where he pushed Claude Code to its limits with one goal in mind: earn as much money as possible. The finding that surprised him — and should surprise most people — is that **Claude is designed by default to make you feel busy and productive, not to actually make you money.** He found four specific upgrades that fixed that, and claims they 3x'd his income in 30 days.

# THE KEY POINTS

- **Claude's default behavior is optimized for feeling productive, not for generating revenue — and without intervention, it will cheerfully burn your time and money.** This is the central insight and the whole reason for the video.
- He burned through half of his $200/month Claude subscription with a single workflow prompt, which forced him to rethink how he was using the tool entirely.
- **The CLAUDE.md file (a special instruction file that Claude reads at the start of every session) is the main lever for reorienting Claude toward money-making goals.** Changing what's in it changes Claude's entire approach.
- Token efficiency matters enormously: a tool called /caveman-compress shrinks your CLAUDE.md by ~46%, which saves money on every single future session permanently — like paying less rent forever.
- **"Capability Uplift" skills extend Claude beyond what it can do out of the box** — for example, giving it the ability to scrape websites with Firecrawl, generate real PDF files, or run automated browser tests with Playwright.
- The four upgrades shift Claude's behavior from "assistant trying to help" to "revenue-focused operator" — a meaningfully different operating mode.

# THE METHOD OR FRAMEWORK

Nate's four-upgrade framework works like reprogramming a helpful assistant into a revenue-focused operator:

1. **Rewrite your CLAUDE.md** — Give Claude a system prompt that explicitly frames every task through the lens of: does this make money, or does it waste time? Strip out anything that encourages over-explaining or padding.
2. **Compress your instructions** — Use /caveman-compress to shrink that instruction file. Smaller instructions = fewer tokens used = lower cost per session. Multiply that across hundreds of sessions.
3. **Add Capability Uplift skills** — Install specific Claude Code skills like Firecrawl (web scraping), PDF generation, and Playwright (browser automation). These unlock Claude to do work it otherwise literally cannot do.
4. **Use revenue-oriented workflow prompts** — Structure your prompts so Claude is always moving toward a client deliverable or product, not exploring or iterating endlessly.

# HOW THIS APPLIES TO AI REAL ESTATE

The lesson here maps directly to how you'd set up Claude Code for a real estate client. Right now, if you hand Claude a task like "analyze this neighborhood for a buyer," it will produce a thorough, thoughtful response — but one that's optimized to sound complete, not to close a deal. If you rewrite the CLAUDE.md for a real estate AI agent to say "your job is to help this agent send five qualified follow-up emails and book two showings today," Claude's outputs change fundamentally. Add a Firecrawl skill so it can pull live listing data, a PDF skill so it generates polished reports clients can actually receive, and you've turned a general AI assistant into a revenue-producing tool. That's the playbook Nate proved on himself.

# ACTION STEP THIS WEEK

Open Claude Code and create or rewrite your CLAUDE.md for a real estate workflow you already do (lead follow-up, CMA reports, listing descriptions). Add one explicit line: "Every response should move toward a client deliverable or a booked appointment — not explanation for its own sake." Then run your next five tasks through that updated instruction file and compare the outputs to what you got before.

# BEST QUOTE

"By default, Claude is tuned to make you feel productive, not to make you money — but 4 simple upgrades fix that."

---

## [Why Watching AI Videos Isn't Enough](https://www.youtube.com/watch?v=S2ME69hra-k)
*June 24 at 12:00 AM*

# WHAT IT'S ABOUT

Nate directly challenges the pattern he sees constantly in his community: people consuming enormous amounts of AI content — his videos, newsletters, threads, podcasts — but never actually building anything with what they learn. This video is a direct challenge to that pattern. **Watching is not doing.** He makes the case that a single implemented skill is worth more than a hundred videos watched.

# THE KEY POINTS

- **Passive consumption of AI content is a trap that feels like progress but produces nothing** — you can watch every video Nate has ever made and still have zero clients, zero automations, and zero income.
- The symptom is recognizable: constantly learning the "next thing" in AI before you've shipped the last thing you learned.
- **Implementation is the only thing that compounds.** Skills you actually use get better; skills you only watch about evaporate.
- Nate's own approach is a 4-stage blueprint — pick a niche, build one automation, land one client, then scale. Each stage requires doing, not watching.
- **The bar for starting is lower than most people believe** — you don't need to understand AI deeply to automate a real estate workflow; you need to run one workflow once and see what happens.
- Most people are one built project away from their first paying client, but they keep watching instead of building.

# THE METHOD OR FRAMEWORK

Nate's 4-Stage Blueprint (the framework this video argues you should be implementing, not just knowing):

1. **Pick a niche** — Choose one specific type of business (e.g., real estate agents, property managers, mortgage brokers) and commit to building automations for that type only. Narrow beats broad.
2. **Build your first automation** — Doesn't need to be perfect. Pick one repetitive workflow that business does and automate it. A lead follow-up sequence, a listing data puller, a document formatter — anything real.
3. **Land your first client** — Go talk to one person in that niche and show them what you built. Offer to run it for their business. This forces real-world learning faster than any video.
4. **Scale with systems** — Once you have a working product and a paying client, build repeatable systems (templates, SOPs, team) so you can deliver the same thing to more clients without starting from scratch each time.

# HOW THIS APPLIES TO AI REAL ESTATE

This video is the most directly actionable one for an AI real estate consulting business. The people watching Nate's videos are likely stuck in the same trap: learning but not shipping. The antidote is embarrassingly simple — pick one real estate workflow you understand (say, pulling comparable sales and writing a CMA summary), automate it with Claude, and show it to one agent this week. That single conversation will teach you more about what agents actually need than three months of AI newsletters. The video is essentially Nate giving permission to stop optimizing your learning and start optimizing your output.

# ACTION STEP THIS WEEK

Pick one task a real estate agent does repeatedly that takes them 30–60 minutes (examples: writing a listing description from notes, summarizing showing feedback for a seller, drafting a follow-up email after an open house). Build a single Claude prompt that does that task in under 2 minutes. Test it on a real example. Then contact one agent and show them the before/after time comparison. Don't pitch a service yet — just show the demo.

# BEST QUOTE

"Tired of watching the AI revolution unfold from the sidelines, consuming video after video, thread after thread, newsletter after newsletter, while never acting."

---

# Nate Herk Analysis — June 25, 2026

## [I Battle Tested Sakana Fugu's Fable Killer](https://www.youtube.com/watch?v=GpSqBjW6hR4)
*June 23 at 12:26 AM*

# WHAT IT'S ABOUT

Nate made this video to test out a brand-new AI tool called **Sakana Fugu** (made by a Japanese company — "Sakana" means fish). The big claim is that Fugu matches the performance of top-tier AI models without being one single super-smart model itself. Instead, it's a clever system that takes your request, splits it into pieces, and hands each piece to the AI model that's best at that specific job. Nate ran it through 38 tests against Claude Opus (a leading AI model from Anthropic) to see if it actually lives up to the hype.

# THE KEY POINTS

- **Fugu is not one giant smart AI — it's a "multi-agent system delivered as one model," meaning it's a single tool that secretly coordinates several different AI models behind the scenes.** You send your request to one place, and it routes the work to the best model for each task.

- The way it works is simple: a small "manager" model breaks your task into parts, then hands each part to a specialist. **For example, it might use Claude for writing, GPT for coding and fixing bugs, and Gemini for research and facts.**

- **This idea is nothing new — Nate stresses that each AI model is good at one specific thing, and the real magic is chaining their outputs together.** Fugu just automates the hand-offs so you don't have to manage them yourself.

- Nate gave it one big prompt and after almost an hour it built him a full YouTube dashboard (a screen showing his channel stats) with live data, AI analysis, and recommendations — all from a single command.

- **It's different from another similar tool (Open Router's Fusion API), which sends your prompt to three models at once and then picks the best blend — whereas Fugu actually splits up the task and assigns pieces.** Both approaches tend to give better results because you get multiple AI "perspectives."

- **The big downside is cost and speed — getting multiple AIs involved is expensive and slower.** Nate burned through his $200/month plan fast, hitting 34% of his weekly limit in just one 5-hour session.

# THE METHOD OR FRAMEWORK

Nate explains the "orchestration" idea (the system of deciding which AI does what) as boiling down to two simple questions:

1. **Who does each part?** If you have a big job with tasks A, B, and C, the system decides which AI model handles each one — sending the writing to one model, the coding to another, and so on.

2. **How do we combine everything?** Once each model finishes its piece, another AI (a "language model," meaning an AI that understands and produces text) stitches all the answers together and gives you one clean final result.

He also describes a spectrum of control: on one end, *you* manually decide who does what; on the other end, a tool like Fugu does all that deciding automatically for you.

# HOW THIS APPLIES TO AI REAL ESTATE

The core lesson here — that **each AI is good at one narrow job, and you get the best results by routing tasks to the right specialist** — is exactly how you'd build smart tools for a real estate business. Imagine you build an AI system for a real estate agent that handles incoming leads. Instead of using one AI for everything, you'd route tasks: one model writes warm, friendly follow-up emails to buyers; another pulls and analyzes neighborhood market data and pricing; another drafts the property listing descriptions; and a final one reviews everything for accuracy before it goes out. You don't necessarily need an expensive all-in-one tool like Fugu — you can build this delegation yourself and keep costs low. The takeaway for your consulting clients: don't pay for fancy "do-everything" AI when you can chain together cheaper, specialized steps that each do one thing extremely well.

# ACTION STEP THIS WEEK

Pick one repeatable task in a real estate workflow — for example, turning raw property details into a finished listing. This week, break that task into 2–3 clear sub-steps (1: write the description, 2: fact-check the details, 3: format for posting). Then test running each step through a *different* AI model and compare the final result against using one model for the whole thing. Write down which combination gave the cleanest output. This gives you a concrete, tested example to show clients.

# BEST QUOTE

"Each AI does one thing really well, one very specific thing, and that is how you achieve great results by chaining those outputs into the next."
