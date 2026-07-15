# Nate Herk Analysis — July 15, 2026

## [What Codex 5.6 is amazing at!](https://www.youtube.com/watch?v=6osxCi89ET4)
*July 11, 2026*

WHAT IT'S ABOUT
Nate ran GPT-5.6 Sol (the model powering OpenAI's Codex 5.6) head-to-head against Fable 5 (Claude's flagship model) on real work — browser games, interactive websites, open-ended builds, and quick API tasks. His verdict is clear: Fable 5 is the better manager and more creative model; Sol is a faster, cheaper worker that ships concrete tasks reliably at roughly half the price. The video shows which tool to reach for depending on the type of work, and includes a live content creation demo where Sol built a full YouTube video autonomously across multiple specialized tools.

THE KEY POINTS
- **Fable 5 wins at strategy and creative direction; Sol wins at speed and execution cost.** In a head-to-head browser bike game build: Fable 5 = 21:37, $14.22 vs Sol = 23:00, $4.50 — similar output quality, 3× the price difference.
- **The real comparison is Sol vs Opus 4.8, not Sol vs Fable 5.** Both Sol and Opus 4.8 cost ~$5/million input tokens. Framing it as Sol vs Fable 5 sets up a false choice.
- **Sol is best for tasks with a visible finish line** — browser interfaces, video processing, workflow automation, long-running builds where speed and token efficiency matter.
- **The routing rule: Fable for ambiguity; Sol for execution.** Use a high-judgment model to define the product, acceptance criteria, and creative bar; use Sol to execute, run tools, inspect results, and close the gap.
- **Content creation automation is production-ready.** Sol researched the GPT-5.6 launch, drafted a script in Nate's voice, generated audio via ElevenLabs, created an avatar via HeyGen, and edited with HyperFrames — all in one autonomous run.
- **Parallel agents multiply machine spend fast.** Running Ultra + parallel agents for a short video cost ~$300. Track your token burn before you parallelize at scale.

THE METHOD OR FRAMEWORK
Step 1 — Define: Write the outcome, constraints, reference material, and acceptance tests before the model touches anything.
Step 2 — Build: Let the model create a complete first pass without interruption. Don't micromanage the middle.
Step 3 — Inspect: Run the app, watch the video, open the files, check logs. Observe real output before giving feedback.
Step 4 — Feedback: Describe observable failures only. Don't debug for the model — show it what broke.
Step 5 — Verify: Rerun tests and confirm the fix didn't create a regression.
Step 6 — Stop: End when acceptance criteria pass or the budget is exhausted.

HOW THIS APPLIES TO AI REAL ESTATE
The Fable/Sol routing table maps directly to a real estate AI consulting workflow. Use Fable 5 or Opus 4.8 to define and plan each deliverable: write the outcome, the comps criteria, what the client email should look like. Then hand the execution to Sol: pull the data, format the comps, write the draft. You get Fable-quality strategy at Sol execution costs. For content: run your weekly market update newsletter through Sol as the production model — it drafts in your voice, formats for email, and can generate a talking-head video via HeyGen if you wire up the tool chain. A full newsletter cycle could run autonomously for under $5.

ACTION STEP THIS WEEK
Pick one task you repeat weekly — a market update email, a listing description, a CMA summary. Write the Define step first: outcome, constraints, what "done" looks like. Save it as your task template. Run it once through Sol (GPT-5.6 in Codex) and once through Opus 4.8. Compare speed, cost, and output quality. You'll know within one test which model to route that task to permanently — and you'll have a reusable template to deploy every week with no setup.

BEST QUOTE
"Fable is the better manager and the more creative, capable model. Sol is a really good worker that ships fast and costs a fraction of the price."

---

## [Claude Code for Non-Coders (6 Hour Course)](https://www.youtube.com/watch?v=jdbOVepEtUE)
*July 11, 2026*

WHAT IT'S ABOUT
Nate drops a free 6-hour course aimed directly at people who have never written code — agents, consultants, small business owners — who want to use Claude Code for real, repeatable work. The course builds from the very first prompt all the way to cloud automations that run while you sleep. Unlike a crash course, this is a complete curriculum with step-by-step builds, producing AI systems that actually do work for you by the end. The target learner is the business owner who finds every "beginner" AI resource still assumes you know how to code.

THE KEY POINTS
- **No coding required — this is built for the non-technical business owner.** Nate designed it for the real estate agent, the consultant, the entrepreneur who wants to use AI but can't get past the assumption that coding is a prerequisite.
- **The progression is the curriculum:** First prompt → Skills → Sub-agents → Second Brain → Cloud Automations. Each stage makes the previous one more powerful.
- **Skills (slash commands) are the first real leverage point.** One skill file turns a one-off prompt into a repeatable command that any future session can call in seconds. That's the shift from "using AI" to "operating AI."
- **Sub-agents unlock parallelism without needing to manage it.** You define a high-level goal; the agent spawns and coordinates the execution. One prompt, many simultaneous outputs.
- **A Second Brain persists your knowledge between sessions.** No more starting cold — the wiki stores everything the model needs across every future run.
- **Cloud automations remove you from the operator role entirely.** Once built and scheduled, the workflow runs whether you're at your desk or not. This is the "go to the gym" principle applied to every recurring task.

THE METHOD OR FRAMEWORK
Stage 1 — First Prompt: Learn the anatomy of a good prompt — role, context, task, constraints, output format. One well-structured prompt beats ten vague ones every time.
Stage 2 — Skills: Build slash commands for anything you repeat. /cma-report, /listing-description, /market-snapshot. Saves setup time and removes human error from recurring tasks.
Stage 3 — Sub-agents: Define a goal at the top level; let sub-agents decompose and execute in parallel. Scales one person's throughput to a team's.
Stage 4 — Second Brain: Feed your source material — CMAs, client notes, market research — and let Claude build a cross-linked wiki. Every future session draws from the wiki, not cold memory.
Stage 5 — Cloud Automations: Wire the workflow into a scheduled process that triggers, runs, and delivers results with no human present.

HOW THIS APPLIES TO AI REAL ESTATE
This course is the onboarding curriculum for an AI real estate consulting practice. Walk any agent client through these 5 stages with real estate examples and you've delivered a full consulting engagement: Stage 1 is their first CMA session. Stage 2 gives them a /cma-report skill they run in under a minute. Stage 3 lets one person manage 10 concurrent client analyses via sub-agents. Stage 4 builds a neighborhood knowledge base from 12 months of market data. Stage 5 runs a weekly market digest for every active client automatically. That's a productized service, not a one-off help session — and the 6-hour course is the free asset you use to pre-educate clients before they hire you.

ACTION STEP THIS WEEK
Start Stage 2 today: pick one task you do every week (neighborhood market summary, comp data pull, listing description). Write a markdown skill file that tells Claude exactly how to execute it — what inputs it needs, what format the output should take, what "done" looks like. Save it to your Claude Code skills directory. Next week, run /your-skill-name instead of writing the prompt from scratch. That one file is your first productizable deliverable — and the proof of concept you can show the next client.

BEST QUOTE
"By the end of this, you'll have AI systems that actually do work for you — not tools you have to babysit."

---

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
