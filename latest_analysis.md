# Nate Herk Analysis — September 03, 2026

## [How Anthropic ACTUALLY Prompts Fable 5.1](https://www.youtube.com/watch?v=FBVNS1l5Vb8)
*September 02 at 09:53 PM*

WHAT IT'S ABOUT

This video is Nate Herk sharing four tips straight from Anthropic (the company that makes Claude, an AI assistant) on how to get better results from their newest AI model, called "Fable 5.1." He made it because a lot of people have been burning through their weekly usage limits too fast, and he wants to show you how to use this AI more efficiently so it works better and costs you less. He pulled all these tips directly from Anthropic's own official instruction documents.

THE KEY POINTS

- **The most important tip is to "tell it what done looks like" — give the AI the finish line and let it figure out the steps itself, instead of spelling out every single task.** Nate says to describe the outcome you want, why it matters, and any real limits, then get out of the way.

- **Context matters a lot — telling the AI *why* you're asking helps it connect your request to the right information** instead of guessing what you mean. This is why having a saved file of your goals and background (Nate calls this an "AIOS," basically a personal system that stores context about you) makes the AI much more powerful.

- **Old, overly-detailed instructions can actually slow the AI down.** If you built "skills" (reusable sets of instructions for the AI) that spell out every tiny step, that rigid detail can get in Fable 5.1's way and make it less efficient — this newer model does better with freedom.

- **You don't always need the AI at full power — match the effort level to how hard the task actually is.** There's an "effort slider" you can drag between low, medium, high, extra high, max, and ultra, and by default it sits on "high," which is often overkill.

- **Fable 5.1 on "low" is roughly as good as the older Fable 5 on medium or high, but cheaper** — so for everyday work, cranking everything to max is like using a blowtorch to light a cigarette.

- **On "low" effort, the AI is less likely to go search the internet and more likely to just answer from what it already knows** — which is great for brainstorming or quick idea-generating where you don't need heavy research.

- You can even change the effort level partway through a conversation depending on what you need at that moment.

THE METHOD OR FRAMEWORK

Here's Nate's simple system for using Fable 5.1 well:

1. **Define the finish line, not the tasks.** Instead of writing a long list of instructions, write one clear goal. Example: rather than listing ten steps for building a webpage, just say "Create an appealing landing page offering voice agent solutions tailored to our target audience" and let the AI figure out the steps.

2. **Give it context.** Tell it why the task matters and any real constraints, so it understands your intent.

3. **Refactor (rewrite) your old instructions.** If you have old "skills" that are too bossy and detailed, clean them up. Nate points to a tool command — `/claude API prompt-audit` — that automatically finds redundant, unneeded rules and removes them.

4. **Start at "high" effort, then test lower.** Run a task on high, then try it on medium. If medium works just as well, try low. Only use extra-high or max for genuinely heavy, deep-thinking work.

5. **Judge based on your own results ("evals").** An "eval" just means testing the AI on your actual work to see which effort level is good enough — don't copy someone else's setting, since their work may be totally different from yours.

HOW THIS APPLIES TO AI REAL ESTATE

If you run an AI real estate consulting business, this changes how you set up tools and control costs. Say you're building an AI assistant for a real estate agent that answers buyer questions, drafts listing descriptions, and organizes property data. Instead of writing a rigid 20-step instruction sheet, you'd give the AI a clear goal like "Write a warm, professional listing description that highlights this home's best features for young families" plus context about the agent's target market — and let it work. Then you'd match effort to the job: use "low" effort for quick, everyday stuff like drafting a follow-up email to a lead (saving money and usage), and save "max" effort for something heavy like analyzing a whole spreadsheet of neighborhood price trends. Over a month, this could dramatically cut your AI costs while keeping quality high — a real selling point when you pitch clients.

ACTION STEP THIS WEEK

Take one task you normally run at "high" effort — for example, drafting a property listing or a client email — and run the exact same task three times: once on high, once on medium, once on low. Compare the three results side by side and decide the lowest setting that still gives you good enough quality. Then make that your default for that type of task. Do this for your two or three most common tasks this week.

BEST QUOTE

"Tell Fable the outcome, tell it why it matters, tell it what done means, and tell it if there are any real constraints."

## [Fable 5.1 Just Dropped. It Looks Unreal.](https://www.youtube.com/watch?v=8IyORt-7rOQ)
*September 01 at 06:49 PM*

WHAT IT'S ABOUT

Nate made this video to give a quick first look at two new AI models from Anthropic (the company behind the Claude AI assistant): Fable 5.1 and Mythos 5.1. These are AI models built for coding (writing computer programs) and "knowledge work" (thinking, reasoning, and problem-solving tasks). The big news is that Fable 5.1 is supposedly smarter than the older Fable 5 while also being cheaper to run, and Nate is starting to test it out live to see if the hype holds up.

THE KEY POINTS

- **Fable 5.1 is claimed to be the most capable AI model Nate has ever used**, beating the older Fable 5 while also being about 25% cheaper for normal use.

- The price per unit of text hasn't changed (it's still $10 per million "input" words and $50 per million "output" words), but **the new model is more efficient, meaning it uses fewer "tokens" — the small chunks of text an AI reads and writes — so you spend less money overall.**

- The savings come partly from cheaper "cache reads," which is when the AI re-reads text it already processed and saved before, and **for heavily automated tasks the savings could reach up to 50%.**

- There's a new privacy option for big companies called EFS, which **lets businesses choose to have none of their data stored or kept, which matters a lot for companies worried about keeping their information private.**

- Anthropic says they've improved safety "safeguards" to reduce "false positives" — meaning the AI wrongly blocking or refusing normal requests it thinks are dangerous.

- The company's benchmark charts (standardized tests that score AI performance) show **Fable 5.1 on its lowest effort setting still beating Fable 5 on its highest setting — while costing less.** Nate warns to take these charts with a grain of salt until tested in real life.

- Mythos 5.1 is basically the same as Fable 5.1 but with looser safety limits, and it's **only available to vetted groups in cybersecurity and life sciences through special approval programs.**

- In a quick real test, Nate asked both models to build a spinning 3D cartoon bear on a bike, and **Fable 5.1 produced better shadows, more realistic physics, and cost about a dollar less than Fable 5.**

THE METHOD OR FRAMEWORK

There's no real framework in this video — it's a first-impressions news update. But Nate does show a simple way to test and compare AI models yourself:

1. Give both the old and new model the exact same prompt (the instruction you type in), like "build me a rotating 3D cartoon bear riding a bike."
2. Compare the quality of the results side by side (in his case, the shadows and physics).
3. Use the built-in cost command (he typed "/cost" or "/usage") to see exactly how much money and time each model spent on the same task.
4. Judge whether the newer model gives you better results for less money.

HOW THIS APPLIES TO AI REAL ESTATE

For an AI real estate consulting business, the "cheaper and smarter" angle here matters directly to your profit and your clients' costs. Since these models charge by tokens (chunks of text), a more efficient model means you can run the same AI tools for less money. Concrete example: say you build an AI assistant for a real estate agency that reads long property listings, writes custom email replies to buyers, and drafts listing descriptions all day. If that assistant runs on Fable 5.1 and it's 25% cheaper for typical work — or up to 50% cheaper for automated back-and-forth tasks — then a client paying $400 a month in AI costs might drop to $200-$300, while getting sharper, more human-sounding writing. That's a real selling point you can pitch: "I can upgrade your system to a smarter model that also cuts your monthly AI bill." The privacy option (EFS) is also worth mentioning to clients nervous about their buyer and seller data being stored somewhere.

ACTION STEP THIS WEEK

Run your own head-to-head test like Nate did. Take one real task from your consulting work — for example, "write a warm follow-up email to a lead who toured a home but hasn't responded in a week" — and run that exact prompt through both Fable 5 and Fable 5.1. Then type the cost command to see how much each one spent. Write down which one gave the better email and which was cheaper. By the end of the week you'll have real proof you can show clients, instead of just repeating benchmark claims.

BEST QUOTE

"Fable 5.1 on low is better than the strongest Fable 5 on max or high or ex-high, and it's cheaper."
