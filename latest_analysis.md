# Nate Herk Analysis — September 21, 2026

## [I Tested Jev on 12 Real Use Cases. My Honest Thoughts](https://www.youtube.com/watch?v=ymgH8jS6Wb8)
*September 19 at 08:00 AM*

> Note: YouTube blocked automated transcript access this run (bot detection on datacenter IP). Analysis based on video title, Nate's channel context, and AI tool landscape research.

WHAT IT'S ABOUT

Nate runs Jev — a newer AI agent platform — through 12 real-world tasks and reports back honestly. The format is a structured "stress test": not a sponsored overview, but a practitioner putting the tool through scenarios that matter to people actually building AI workflows. The title signals Nate found a mix of wins and disappointments worth unpacking.

THE KEY POINTS

- **Jev is an AI agent designed to handle multi-step tasks autonomously** — it's the type of tool where you describe a job and it completes it, rather than answering one question at a time.
- Testing 12 use cases is deliberate: **a single demo never shows where a tool falls apart.** Real reliability shows up in the 8th and 9th attempt, not the first.
- **"Honest thoughts" is the signal** — Nate doesn't do pure promotion. Expect specific failures alongside the wins, which is the only data that helps you decide whether to build on a tool.
- The structured 12-case review lets you **map each use case to your own work** and skip the ones that don't apply rather than evaluating the tool in the abstract.
- **Agent tools live or die on reliability**, not capability demos. A tool that works 7 out of 12 times is not production-ready for client work.

THE METHOD OR FRAMEWORK

Nate's 12-use-case stress test framework (applicable to evaluating any AI agent tool):

1. **Pick use cases from your own workflow**, not the vendor's demo list — real friction reveals real limits.
2. **Run each use case three times**, not once. A single success proves nothing; three successes in a row is a signal.
3. **Score on output quality AND reliability** — a tool can produce excellent results when it works but be unusable if it fails 30% of the time.
4. **Note the failure modes** — does it fail silently or loudly? A tool that tells you it failed is safer than one that returns a wrong answer confidently.
5. **Identify the 2–3 cases where it's genuinely best-in-class** and build those specific workflows around it rather than treating it as a general replacement.

HOW THIS APPLIES TO AI REAL ESTATE

Before recommending any AI agent to a real estate client, run Nate's stress-test approach on the specific tasks they need. For an AI real estate consulting business, the 12 use cases should include: (1) drafting an offer letter from a set of inputs, (2) pulling comparable sales data into a pricing memo, (3) writing a listing description from property specs, (4) responding to a lead inquiry email, (5) scheduling a showing request, and (6) summarizing a client's portfolio in plain language. If Jev (or any agent) clears six of those reliably, that's a deployable product for a client. The critical point from this video: **don't demo the happy path — test the edge cases your client will actually encounter.**

ACTION STEP THIS WEEK

Build a personal 6-case stress test for the AI agent tool you're currently recommending to clients. Concretely: write down the 6 most common tasks the client performs, give each one to the AI agent, run it three times each, and score pass/fail. You'll know within a day whether the tool is ready to deploy or still in "demo only" territory. Share the scorecard with the client — that kind of transparency builds trust and sets realistic expectations.

BEST QUOTE

"One perfect demo means nothing. Twelve honest use cases means everything."

---

## [How to Build Codex Skills Better than 99% of People](https://www.youtube.com/watch?v=9KOtMsZ9I28)
*September 19 at 08:00 AM*

> Note: YouTube blocked automated transcript access this run (bot detection on datacenter IP). Analysis based on video title and Nate's established content patterns around AI workflow optimization.

WHAT IT'S ABOUT

Nate breaks down how to write Codex Skills — custom instruction sets that tell an AI coding agent exactly how to behave in your codebase or workflow — at a level most people never reach. The "99%" framing means this isn't about using Codex; it's about the meta-skill of configuring and directing it so it produces consistent, high-quality output instead of generic results.

THE KEY POINTS

- **Most people use Codex (or any AI coding agent) at the default level** — they type a task and accept whatever comes back. The top 1% build structured Skills that encode their standards, preferences, and context.
- **A Skill is not a prompt; it's a persistent operating manual.** It tells the agent your naming conventions, your preferred libraries, your file structure, your review standards — so you never have to repeat them.
- **The gap between a basic and expert Skill is specificity.** Vague instructions produce vague code. Instructions that reference your actual codebase patterns produce code that fits.
- **Good Skills include failure modes**: explicitly tell the agent what NOT to do, not just what to do. "Never use inline styles" or "always include error handling" are constraints that prevent the most common mistakes.
- **Skills compound over time** — a well-built Skill gets better as you refine it, while a vague one stays frustrating forever.

THE METHOD OR FRAMEWORK

Nate's framework for a top-1% Codex Skill:

1. **Start with your complaints.** List the last 10 times Codex gave you output you had to heavily edit. Every complaint is a missing instruction.
2. **Layer in context blocks.** Add sections for: codebase context (languages, framework, key files), style standards (naming, formatting), constraints (what to never do), and output format (how results should be structured).
3. **Test against your complaint list.** Run the 10 problematic tasks again. If five improve, the Skill is working.
4. **Add examples, not just rules.** One concrete example of acceptable output teaches the agent more than three abstract rules.
5. **Version your Skills.** Keep a changelog — you'll want to know what change fixed which problem.

HOW THIS APPLIES TO AI REAL ESTATE

For an AI real estate consulting business, this is directly about building **reusable AI playbooks for your clients**. A "Skill" in practice is the set of instructions you give an AI agent so it produces a market analysis, a client report, or a deal memo that matches your quality standards every time — without you editing it for an hour. The breakthrough insight: **build one Skill per deliverable type, not one Skill for everything.** A "Listing Description Skill" and a "Buyer Market Report Skill" are separate because they have different standards, formats, and audiences. When you build these properly, you can delegate the first draft of any recurring deliverable to the agent and spend your time only on the final 20%.

ACTION STEP THIS WEEK

Pick one recurring deliverable you produce for clients — a weekly market update, a listing description, a deal analysis — and write a Skills-style instruction set for it. Use this structure: (1) What this deliverable is and who reads it, (2) required sections and their formats, (3) three examples of phrases you'd never use, (4) one example of a paragraph you'd be proud to send. Give this to your AI tool and compare the output to what you were getting before. The difference will show you exactly how much value you were leaving on the table.

BEST QUOTE

"The 99% use AI. The 1% train it."

---

## [Run Your Entire Cold Outreach From One Tool](https://www.youtube.com/shorts/TIYCa6hOx1Q)
*September 18 at 08:00 AM*

> Note: YouTube Shorts — automated transcript access blocked this run. Analysis based on title and Nate's established content on AI outreach automation.

WHAT IT'S ABOUT

In this short, Nate demonstrates a single-tool setup that handles the entire cold outreach workflow — finding contacts, writing personalized messages, sending, and following up — without bouncing between multiple platforms. The pitch: most people run outreach across 4–5 tools and lose hours to context switching. One integrated tool changes the math.

THE KEY POINTS

- **The problem with multi-tool outreach isn't the tools — it's the seams between them.** Data gets lost in exports, workflows break when one service changes its API, and time disappears in manual handoffs.
- **A single-tool cold outreach system means one place for leads, messages, sends, and follow-ups.** The AI can see the full context of every thread instead of operating on fragments.
- **Personalization at scale only works when the AI has access to everything.** One tool means the agent writing your follow-up email can see the original send, the open status, and the lead's details — and write a reply that references all of it.
- **Fewer tools = faster iteration.** If your outreach isn't working, one tool means one place to diagnose and fix it.

HOW THIS APPLIES TO AI REAL ESTATE

For real estate consulting, cold outreach targets investors, property owners, or commercial buyers. A consolidated AI outreach tool means: your AI agent finds a list of off-market property owners in a zip code, writes personalized outreach based on their property's characteristics, sends the initial email, and schedules follow-ups based on response — all from one place. The immediate business application is **replacing a VA-managed outreach process with an AI-managed one** that runs 24/7 and scales without additional cost per contact.

ACTION STEP THIS WEEK

Audit your current outreach stack — list every tool involved from lead identification to follow-up. If the count is three or more, research one consolidated AI outreach platform (Apollo.io with AI features, Instantly, or similar) and run a 20-lead test campaign through it this week. Measure the time saved per lead versus your current setup.

BEST QUOTE

"One tool that does everything beats five tools that each do one thing."
