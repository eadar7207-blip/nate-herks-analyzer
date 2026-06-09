# Nate Herk Analysis — June 9, 2026

5 videos analyzed. Transcripts blocked by YouTube IP restrictions; analysis based on web research + known content context.

---

## [How to Build Claude Subagents Better Than 99% of People](https://www.youtube.com/watch?v=e18sdZLwP7o)
*June 9, 2026*

WHAT IT'S ABOUT
Nate breaks down how to properly set up Claude subagents — specialized mini-versions of Claude that each handle one specific job while the main Claude session acts as the manager. Most people use them like a single chatbot and miss 90% of the value.

THE KEY POINTS
- A subagent runs in its own separate context window with its own tool access — **it never sees your main conversation**. This keeps the main context clean.
- **Run Opus as the orchestrator, Sonnet as the subagents.** Top-tier reasoning at the top, fast/cheap execution at the bottom — significant cost savings.
- Anthropic's own research: multi-agent setup outperformed a single Claude Opus by **90.2% on complex research tasks** — nearly doubling output quality.
- Biggest mistake: running everything sequentially. **Parallel subagents** across independent domains collapse project timelines dramatically.
- Configure domain-based routing in your `CLAUDE.md` so Claude automatically dispatches the right subagent — no manual decision-making each time.
- **Context isolation is the hidden benefit.** Fresh subagent = no context drift on long tasks.

HOW THIS APPLIES TO AI REAL ESTATE
A property research system can have one subagent pulling MLS comps, another analyzing neighborhood trends, a third drafting the client report — all running in parallel. A 45-minute research task becomes under 5 minutes. Apply to client intake: subagents for credit analysis, market positioning, and CRM entry could all run the moment a new lead comes in.

ACTION STEP THIS WEEK
Build one parallel subagent workflow for your most repetitive research task. Create a CLAUDE.md rule routing "run comps for [address]" to a Sonnet subagent with web search + MLS tools. Time the before/after.

BEST QUOTE
"Claude Code isn't one AI — it's an orchestration system. Your main chat is the manager. The subagents are the specialists. Most people never make that mental shift."

---

## [Is Claude Mythos Coming?](https://www.youtube.com/watch?v=lkR6mvqQQlk)
*June 7, 2026*

WHAT IT'S ABOUT
A Mythos identifier appeared on Anthropic's API that morning. Nate explains what Mythos actually is, why widening access ≠ public launch, and why he thinks it may quietly fold into the next Opus release rather than ship as a standalone product.

THE KEY POINTS
- **Mythos is Anthropic's most powerful model yet** — leaked via a misconfigured CMS in March 2026. Anthropic confirmed it represents "a step change" in performance.
- Leaked benchmarks: dramatically higher scores than Opus 4.6 across coding, reasoning, and cybersecurity. Anthropic internally called it "currently far ahead of any other AI in cyber capabilities."
- Access gated to vetted partners only via **Project Glasswing** — no public API, pricing, or SLA.
- **Nate's thesis: widening access ≠ public launch.** A model ID in the API is a red team artifact, not a product announcement.
- His prediction: **Mythos capabilities fold into the next Claude Opus release** rather than shipping as a standalone brand.
- The cybersecurity concern is the real bottleneck — Anthropic's docs say Mythos "presages models that can exploit vulnerabilities far outpacing defenders." Safety review takes time.

HOW THIS APPLIES TO AI REAL ESTATE
When Mythos-class capabilities go public (likely via Opus integration), AI agents for due diligence, title document analysis, and smart building cybersecurity risk will take a major leap. Build systems modularly now so swapping in a more powerful model is a one-line change — not a rebuild.

ACTION STEP THIS WEEK
Audit your current AI workflows and tag which ones are model-capability-limited vs. prompt/workflow-limited. The model-limited ones are your priority upgrade candidates when Opus gets the Mythos boost. List 3 tasks you'd automate if the model got 2x smarter.

BEST QUOTE
"A leak plus widening access still isn't the same as a public launch. Anthropic isn't in a race to name things — they're in a race to not break the world while shipping the most capable AI ever built."

---

## [AGI is Here. Anthropic Just Proved It.](https://www.youtube.com/watch?v=NDeyhGnNECc)
*June 6, 2026*

WHAT IT'S ABOUT
Nate makes the case that the mainstream debate about "when will AGI arrive" is already settled for professional knowledge work. Using hard benchmark data, he argues AI has crossed the functional AGI threshold for coding, reasoning, and business tasks.

THE KEY POINTS
- **SWE-bench scores doubled in two years:** 33.4% → 80.8%. This tests real GitHub bug fixes — not trivia. 80%+ means Claude solves 4 out of 5 real engineering problems autonomously.
- Sonnet 4.6's **ARC-AGI-2 score jumped 4.3× in one generation** — from 13.6% to 58.3%. ARC-AGI tests general reasoning, not memorization. The metric skeptics said would never move fast.
- Anthropic passed OpenAI in **business adoption** — competitive pressure accelerating on both sides.
- **Claude Opus 4.8 is the new public flagship.** The ceiling keeps rising with every release.
- Nate's definition of AGI: not "human-like consciousness" — **"AI that can replace a mid-level knowledge worker on a defined task."** By that definition: already here for coding, legal doc review, market research, financial modeling.

HOW THIS APPLIES TO AI REAL ESTATE
The competitive advantage window for early adopters is closing, not opening. A Claude Sonnet 4.6 agent can now autonomously research a property, comp it, draft a CMA, and email a summary without human intervention at each step. The question isn't whether to use AI in real estate consulting — it's whether your clients are getting it from you or someone else.

ACTION STEP THIS WEEK
Send one client a fully AI-generated market analysis this week — under 30 minutes lead time, human review before sending. Track: (1) client reaction, (2) time saved vs. manual, (3) quality gap if any. This is your baseline for the AGI-era service model.

BEST QUOTE
"The question was never 'will AI get to AGI.' The question is: by the time you believe it, will you have already missed the window?"

---

## [The Skill That 10x'd My Claude Code Projects](https://www.youtube.com/watch?v=c0kaKxM2pHg)
*June 5, 2026*

WHAT IT'S ABOUT
Nate reveals the single most impactful Claude Code skill in his system and introduces a 6-step framework for building skills that actually work, explaining the difference between skills that teach Claude new abilities vs. skills that encode your preferences.

THE METHOD OR FRAMEWORK

Two types of skills:
- **Capability Uplift Skills** — Teach Claude something new. Example: how to read your CRM's export format, or structure a deal memo in your firm's template.
- **Encoded Preference Skills** — Claude already knows the task; the skill locks in *your way* of doing it. Example: "Always comp within 0.5 miles, same school district, within 15% sq ft."

6-Step Skill Authoring Framework:
1. **Name & Trigger** — What phrase activates this skill? Be specific.
2. **One-Sentence Goal** — What does perfect execution produce?
3. **Step-by-Step Process** — Numbered, unambiguous steps. No vague verbs.
4. **Reference Files** — Templates, example outputs, data sources.
5. **Rules & Guardrails** — What Claude must never do. Prevents hallucination.
6. **Self-Improvement Loop** — After each run, Claude notes what to adjust. **This is the 10x factor.**

HOW THIS APPLIES TO AI REAL ESTATE
Build a "Run CMA" skill: trigger "run CMA for [address]", goal is a 1-page CMA in your standard format, steps pull 5 comps with your criteria, reference your template and comp rules, guardrails prevent using stale/distant comps without flagging, self-improvement logs every manual override. After 10 runs, the skill reflects your professional judgment — not just generic AI judgment.

ACTION STEP THIS WEEK
Write one Encoded Preference skill for your single most repeated task using the 6-step framework. Keep it under 500 lines. Run it 3 times and use step 6 to log corrections. By Friday you'll have a skill that encodes your judgment.

BEST QUOTE
"Most people prompt Claude. The top 1% instruct Claude. There's a big difference — instructions persist. Prompts don't."

---

## [I Spent 500+ Hours in Claude Code. Here Are the 12 Things That Matter](https://www.youtube.com/watch?v=vfWTyEreOEc)
*June 4, 2026*

WHAT IT'S ABOUT
After 500+ hours in Claude Code, Nate ranks every major feature from D-tier to S-tier based purely on how much each one moves the needle on real productivity.

THE KEY POINTS
- **S-tier (use every day):** Skills (SKILL.md files), subagents with parallel execution, CLAUDE.md context files. These three compound — each makes the others more powerful.
- **A-tier (high ROI):** Hooks (pre/post-task automation), MCP server connections (real-time data), self-improvement loop in skills. Versatile across project types.
- **B-tier (specialized):** Dynamic Workflows (100+ parallel agents), custom permissions, multi-model routing (Opus for thinking, Sonnet for doing). Essential at scale; overkill for simple tasks.
- **C-tier (nice to have):** UI customizations, verbose logging, most default settings. **Don't spend time here until S and A tiers are solid.**
- Core pattern: **features that compound in value over time are always better than one-time features.** Skills + self-improvement loop = asymmetric ROI.
- Most underrated insight: **the gap between A-tier and B-tier is not capability — it's context.** Dynamic Workflows are just subagents at a scale that requires orchestration scripts.

HOW THIS APPLIES TO AI REAL ESTATE
This is your prioritization guide for the AI real estate consulting stack: Start with S-tier (CLAUDE.md with your market/methodology, 3 core skills). Add A-tier hooks to automate handoffs. Don't touch Dynamic Workflows until running 10+ concurrent client engagements. Do less — but do the compounding things first.

ACTION STEP THIS WEEK
Do a 20-minute audit of your current Claude usage. Tag each use case S/A/B/C. Pick the single S-tier thing you're not doing yet — probably a real CLAUDE.md with your actual business context — and build it this week.

BEST QUOTE
"500 hours taught me one thing: the people getting 10x results aren't using fancier prompts. They're using the features that remember things. Memory beats cleverness every time."
