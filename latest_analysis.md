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
