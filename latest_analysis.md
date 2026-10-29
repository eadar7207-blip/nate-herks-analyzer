# Nate Herk Analysis — October 29, 2026

## [/roast-room: How I Use Claude to Think Like the Top 1%](https://www.youtube.com/watch?v=DSS1Yqb6-qE)
*October 22 at 02:18 PM*

WHAT IT'S ABOUT

Nate shows off a tool he built called "Roaster Room" (or "Rooster Room") that uses Claude, an AI assistant made by Anthropic, to simulate a panel of famous business minds — people like Jeff Bezos, Warren Buffett, and Alex Hormozi — who all critique your business ideas from their own unique angles. The point is to help you think like top-tier entrepreneurs by having AI versions of them argue, poke holes in your plans, and give you a final recommendation. He made the video to demonstrate how the system works under the hood and to share the free setup so others can use it.

THE KEY POINTS

- You ask the system a business question with multiple-choice answers, and a virtual "board" of famous business figures critiques your idea. **Each board member focuses on one specific angle, so you get many expert viewpoints at once instead of just one.**

- The board members actually debate each other on screen — for example, Bezos arguing with Gary Vee — which makes it feel like a real heated discussion rather than a single flat answer. **The disagreement between advisors is the value, because it forces you to see weaknesses in your idea.**

- After a few rounds of debate, the system gives a final verdict (like "Option C") and lets you download a PDF to review or share with your team. **You get a clear decision plus a document you can keep, not just a vague conversation.**

- The visual panel you see is just a pretty layer on top of what's really happening inside Claude Code (Anthropic's tool for coding with AI), where "subagents" — smaller AI helpers each given one job — act out each board member. **The flashy visuals are optional; the real work happens in the background code.**

- The whole thing is fully customizable — you can add, remove, or create new advisors. He starts with 11 figures (seven standard plus Naval, Cody Sanchez, Sarah Blakely, and Leila Hormozi) and plans to add more. **You can build a board of literally anyone you admire.**

- Each advisor is built from two files: an "agent file" (a plain text document, called markdown, describing how they talk and think) and a "brain" (a deeper folder of their books, frameworks, principles, quotes, and real sources). **The AI isn't guessing — it's pulling from real interviews, books, and talks each person actually gave.**

- For example, Leila Hormozi's AI "brain" was built from 48 sources, about half a million words, 14 interviews, and 34 of her own videos. **The quality of the advice depends on feeding the AI a large pile of that person's real material.**

- He added a "New Rooster" skill (a built-in command) that automatically creates a brand-new advisor — he demonstrates by generating an Elon Musk version, complete with brain, agent file, sources, and even a cartoon character. **You can clone any new expert in minutes without doing the setup by hand.**

THE METHOD OR FRAMEWORK

Here's how the Roaster Room system works, step by step in plain English:

1. **Set up your advisors.** Each "board member" is made of two parts: an agent file (a short text file saying how that person speaks, debates, and sees the world) and a "brain" folder (a bigger collection of their real books, frameworks, principles, positions on topics like pricing or debt, and actual quotes and stories).

2. **Ask your question.** You type in a business question and give a few multiple-choice answers to pick from.

3. **Let the board debate.** The system launches a subagent (a small, focused AI helper) for each advisor. Each one looks at your question through their specialty — Buffett looks at cash and long-term value, Hormozi looks at whether people will pay, Wickman looks at whether the business can run without you.

4. **Watch them argue.** The advisors challenge each other over several rounds, exposing flaws in your idea.

5. **Get the verdict and PDF.** The system picks a recommended option and gives you a downloadable document.

6. **Scale it.** Use the "New Rooster" command to automatically add any new expert you want, and the system builds their brain and character for you.

HOW THIS APPLIES TO AI REAL ESTATE

This is a powerful blueprint for an AI real estate consulting business because it shows how to turn expert knowledge into an AI "advisor panel" that clients can consult anytime. Imagine building a Roaster Room for real estate decisions, stocked with "brains" trained on real material from top investors and brokers — a Grant Cardone-style multifamily expert, a cash-flow-focused rental investor, a flipping specialist, and a 1031-exchange tax strategist. A client comes to you asking, "Should I buy this fourplex, do a fix-and-flip, or hold my cash and wait?" Your AI board debates it: the cash-flow advisor warns the rent won't cover the mortgage at current rates, the flipper questions the renovation budget, and the tax expert flags a missed exchange opportunity. The client walks away with a reasoned recommendation and a downloadable PDF they can show their partner or lender. You've just packaged elite-level thinking into a repeatable, sellable service.

ACTION STEP THIS WEEK

Build one single AI advisor this week. Pick one real estate expert you respect (say, a well-known investor with lots of public content). Gather their material — grab transcripts from 5 to 10 of their YouTube videos and notes from any book or framework they teach. Then open Claude (or ChatGPT) and create one document describing how they think, their key frameworks, and their positions on common deals. Test it by asking your new "advisor" a real investment question and see if the answer sounds like something that expert would actually say. This gives you the first building block of your own Roaster Room.

BEST QUOTE

"You just ask a question with multiple choice answers, and all these board members come together, blast your idea to the ground, and help you look at it from a different angle."
