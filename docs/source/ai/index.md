(ai_for_optimization)=

# AI for Optimization

This section documents AMPL's AI-related resources and how to use them effectively for optimization work.

```{toctree}
:hidden:
:maxdepth: 1

AMPL Agentic Skill <ampl-agentic-skill>
Model Builder Demo <model-builder>
AMPL MCP Knowledge Server <mcp-server>
```

```{toctree}
:hidden:
:maxdepth: 1
:caption: Other Agentic AI tools

Gemini Notebook for AMPL <notebooklm>
AMPL for ChatGPT <amplbot-chatgpt>
AMPL for Gemini <gemini-assistant>
```

We provide AMPL-focused tools that work across the main LLM ecosystems, including platforms from OpenAI, Google, and Anthropic: an Agentic Skill, an interactive Model Builder, and an MCP server that connects any compatible assistant to AMPL's knowledge base, plus a grounded Gemini Notebook and custom assistants for ChatGPT and Gemini. The goal is to give optimization practitioners faster, more relevant guidance for AMPL modeling, solver usage, and AMPL+Python workflows, directly in the AI tools they already use.

If you already subscribe to one of these platforms, you can typically use the AMPL tools within that subscription instead of adding a separate AI tool. Paid tiers often offer better model quality, higher usage limits, and faster responses.

:::{note}
These tools include AMPL-specific knowledge, but hallucinations and incorrect responses may still occur. Always validate generated models, code, and recommendations.
:::

## Why use chatbots for optimization?

Chatbots bridge the gap between complex optimization problems and reliable, efficient code. Whether you are a student writing your first `.mod` file or a professional tuning solver parameters, an AMPL assistant provides instant, expert-level guidance.

- **Faster onboarding:** get help with syntax, environment setup, and `amplpy` integration in seconds.
- **Modeling best practices:** translate real-world constraints and business rules into clean formulations using AMPL's latest MP features.
- **Model explainability:** understand how requirements map to constraints, why the model works, how sensitive it is, and why data is infeasible.
- **Solver tuning:** get advice on selecting and configuring open-source and commercial solvers.

Code from AMPL-focused assistants is more reliable than code from generic models. In any case, make sure you understand what you add to your model.

## Available tools

Pick the tool that fits your workflow. Each card links to the tool and to its documentation.

::::{grid} 1 1 2 2
:gutter: 3

:::{grid-item-card} {octicon}`stack;1.2em;sd-mr-1` AMPL Agentic Skill
*Agent Skill · Claude, ChatGPT, Gemini and other skills-capable assistants*

Packages AMPL's modeling know-how: turns business logic into AMPL models and `amplpy` code, uses MP logical, piecewise and nonlinear operators where they fit, and knows solver options and callbacks. It suggests current best practices and still helps if you keep using `.dat` and `.run` files.

**Best for:** day-to-day modeling and coding in the assistant you already use.
+++
[Get the Skill ↗](https://skill.ampl.com) · [Documentation](ampl-agentic-skill.md)
:::

:::{grid-item-card} [{octicon}`dependabot;1.2em;sd-mr-1`](https://ampl.com/model-builder-demo/) Model Builder Demo
*Interactive demo · ampl.com*

Transforms plain-language business logic into an optimization model, guiding you through design and formulation in real time.

**Best for:** drafting a first model without starting from scratch.
+++
[Try the demo ↗](https://ampl.com/model-builder-demo/) · [Documentation](model-builder.md)
:::

:::{grid-item-card} {octicon}`server;1.2em;sd-mr-1` AMPL MCP Knowledge Server
*MCP server · any MCP-capable client*

Connects your own assistant or IDE to AMPL's curated knowledge base, with cited sources and known-error corrections. Available for on-premises deployment.

**Best for:** teams with their own AI tools or strict security requirements.
+++
[Connect ↗](mcp-server.md#connect-your-assistant) · [Documentation](mcp-server.md)
:::
::::

## Other Agentic AI tools

AMPL-focused assistants that run inside a specific AI platform. Use them if you already work in that platform.

::::{grid} 1 1 2 2
:gutter: 3

:::{grid-item-card} {octicon}`book;1.2em;sd-mr-1` Gemini Notebook for AMPL
*Grounded notebook · Gemini Notebook*

Answers only from official AMPL documents, with inline citations. Turns business logic into a model, writes `amplpy` code, and generates flashcards, reports, and audio overviews.

**Best for:** learning, lookup, and solver callbacks with `ampls-api`.
+++
[Open notebook ↗](https://notebooklm.google.com/notebook/cae69bfc-18cf-4ffc-8c44-ca8141a1670f) · [Documentation](notebooklm.md)
:::

:::{grid-item-card} {octicon}`comment-discussion;1.2em;sd-mr-1` AMPL for ChatGPT
*Custom GPT · ChatGPT*

AMPL's optimization assistant inside ChatGPT. Turns problem descriptions into AMPL models, bridges them to Python with `amplpy`, and helps troubleshoot infeasibility and solver performance.

**Best for:** ChatGPT users who want AMPL guidance without leaving ChatGPT.
+++
[Open in ChatGPT ↗](https://l.ampl.com/https://chatgpt.com/g/g-68c00de8b030819185be6db190ad7bce-amplbot) · [Documentation](amplbot-chatgpt.md)
:::

:::{grid-item-card} {octicon}`sparkle-fill;1.2em;sd-mr-1` AMPL for Gemini
*Custom Gem · Google Gemini*

AMPL's optimization consultant inside Gemini. Formulates and debugs models with an `amplpy`-first approach and relates answers to the AMPL Book and official documentation.

**Best for:** Gemini users who want AMPL guidance without leaving Gemini.
+++
[Open in Gemini ↗](https://gemini.google.com/gem/1u6aK9nY_4HUERmBtPSH58WJiFQfR7uLa?usp=sharing) · [Documentation](gemini-assistant.md)
:::
::::

## Which tool should I use?

| If you want to… | Use |
| --- | --- |
| Turn business logic into a model | [Model Builder](https://ampl.com/model-builder-demo/), [AMPL Agentic Skill](https://skill.ampl.com) |
| Get AMPL model and `amplpy` code | [AMPL Agentic Skill](https://skill.ampl.com), [MCP Knowledge Server](mcp-server.md) |
| Debug an infeasible or slow model | AMPL Agentic Skill, MCP Knowledge Server |
| Get answers that cite the AMPL documentation | [Gemini Notebook](https://notebooklm.google.com/notebook/cae69bfc-18cf-4ffc-8c44-ca8141a1670f), MCP Knowledge Server |
| Write logical constraints with MP operators | AMPL Agentic Skill, MCP Knowledge Server |
| Set up solver callbacks | Gemini Notebook, AMPL Agentic Skill |
| Create study material for a team | Gemini Notebook, MCP Knowledge Server |
| Get AMPL help inside ChatGPT or Gemini | [AMPL for ChatGPT](amplbot-chatgpt.md), [AMPL for Gemini](gemini-assistant.md) |
| Use your own AI client or IDE | [MCP Knowledge Server](mcp-server.md) |
| Keep everything on your own servers | [MCP Knowledge Server, on-premises](mcp-server.md#on-premises-deployment) |

Performance is not uniform across AI platforms. The underlying LLM is usually the main factor in response quality, reasoning, and accuracy. Because there is no standard way to work with generative AI, we provide AMPL tools that work across several ecosystems so you can choose the one that fits your workflow.

## Validate before you use results

1. Run the generated model and script in your own local or cloud environment. The AI tools do not execute models.
2. Check the solve status before reading any results.
3. Verify feasibility and bounds: constraints hold and variables stay in expected ranges.
4. Sanity-check key numbers against what the business expects.
5. Make sure you understand each constraint before it reaches production.

## How to get better answers

Generic prompts produce generic output. Include concrete model context, explicit requirements, and, if possible, verifiable examples.

- **State the optimization type:** LP, MIP, NLP, MINLP, CP, multi-objective.
- **Provide data shape and units:** indices, dimensions, and expected value ranges.
- **Request diagnostics explicitly:** infeasibility checks, bound-tightening ideas, and alternative formulations.
- **Ask for executable artifacts:** a `.mod` file plus an `amplpy` script and a short validation checklist.
- **Ask for explicit assumptions,** numbered.
- **Ask for a post-solve validation checklist:** feasibility, bound checks, sanity checks.

Example of a strong prompt:

> "Build a weekly workforce scheduling MIP. I have 7 days, 3 shifts/day, 42 employees, and coverage requirements by shift. Hard constraints: labor law rest windows and max weekly hours. Soft constraint: fairness in weekend shifts. Return a clean `.mod` model and an `amplpy` script that loads pandas DataFrames, solves with HiGHS, reports IIS if infeasible, and prints staffing shortfalls."
