(ai_for_optimization)=

# AI for Optimization

This section documents AMPL's AI-related resources and how to use them effectively for optimization work.

```{toctree}
:hidden:
:maxdepth: 1

AMPL Agentic Skill <ampl-agentic-skill>
AMPL MCP Knowledge Server <mcp-server>
Model Builder Demo <model-builder>
Other Agentic AI tools <other-tools>
```

Our AI tools focus on agentic development: AI agents that work alongside you in your own environment to build, debug, and improve optimization models. We provide two building blocks that plug into the agents and assistants you already use, from Anthropic, OpenAI, Google, and others:

- **[AMPL Agentic Skill](ampl-agentic-skill.md):** packages AMPL's modeling know-how and best practices as an Agent Skill, so your agent writes AMPL models and `amplpy` code the way AMPL is meant to be written today.
- **[AMPL MCP Knowledge Server](mcp-server.md):** connects any MCP-capable assistant or IDE to AMPL's curated knowledge base, so answers are grounded in AMPL sources and cite them.

To see AI-assisted modeling in action with nothing to install, try the free [Model Builder demo](model-builder.md) on ampl.com. Custom assistants for ChatGPT and Gemini, and a grounded Gemini Notebook, are still available under [Other Agentic AI tools](other-tools.md).

If you already subscribe to an AI platform, you can typically use the AMPL tools within that subscription instead of adding a separate AI tool. Paid tiers often offer better model quality, higher usage limits, and faster responses.

:::{note}
These tools include AMPL-specific knowledge, but hallucinations and incorrect responses may still occur. Always validate generated models, code, and recommendations.
:::

## Why use agentic AI for optimization?

AI agents bridge the gap between complex optimization problems and reliable, efficient code. Working inside your project, an agent can read your existing models and data, write `.mod` files and `amplpy` scripts, run them in your environment, and iterate on the results. Whether you are a student writing your first `.mod` file or a professional tuning solver parameters, an agent equipped with AMPL's tools provides expert-level guidance.

- **Faster onboarding:** get help with syntax, environment setup, and `amplpy` integration in seconds.
- **Modeling best practices:** translate real-world constraints and business rules into clean formulations using AMPL's latest MP features.
- **Model explainability:** understand how requirements map to constraints, why the model works, how sensitive it is, and why data is infeasible.
- **Solver tuning:** get advice on selecting and configuring open-source and commercial solvers.

Code from AMPL-focused tools is more reliable than code from generic models. In any case, make sure you understand what you add to your model.

## Agentic AI tools for development

Use the Skill and the MCP server separately or together: the Skill gives your agent AMPL's modeling know-how, and the MCP server adds live, source-cited answers from AMPL's knowledge base.

::::{grid} 1 1 2 2
:gutter: 3

:::{grid-item-card} {octicon}`stack;1.2em;sd-mr-1` AMPL Agentic Skill
*Agent Skill · Claude, Codex, Cursor and other skills-capable agents*

Packages AMPL's modeling know-how: turns business logic into AMPL models and `amplpy` code, uses MP logical, piecewise and nonlinear operators where they fit, and knows solver options and callbacks. It suggests current best practices and still helps if you keep using `.dat` and `.run` files.

**Best for:** day-to-day modeling and coding with the agent you already use.
+++
[Get the Skill ↗](https://skill.ampl.com) · [Documentation](ampl-agentic-skill.md)
:::

:::{grid-item-card} {octicon}`server;1.2em;sd-mr-1` AMPL MCP Knowledge Server
*MCP server · any MCP-capable client*

Connects your own assistant or IDE to AMPL's curated knowledge base, with cited sources and known-error corrections. Available for on-premises deployment.

**Best for:** grounded, source-cited answers in your own AI tools, and teams with strict security requirements.
+++
[Connect ↗](mcp-server.md#connect-your-assistant) · [Documentation](mcp-server.md)
:::
::::

## Try it free: Model Builder Demo

::::{grid} 1 1 2 2
:gutter: 3

:::{grid-item-card} [{octicon}`dependabot;1.2em;sd-mr-1`](https://ampl.com/model-builder-demo/) Model Builder Demo
*Free interactive demo · ampl.com*

Transforms plain-language business logic into an optimization model, guiding you through design and formulation in real time. Runs in your browser, with nothing to install.

**Best for:** discovering how optimization applies to your business, and drafting a first model without starting from scratch.
+++
[Try the demo ↗](https://ampl.com/model-builder-demo/) · [Documentation](model-builder.md)
:::
::::

## Other Agentic AI tools

AMPL-focused assistants that run inside a specific AI platform. For development work, we recommend the Skill and the MCP server above; use these if you already work in that platform.

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
| Build and debug models with a coding agent in your project | [AMPL Agentic Skill](https://skill.ampl.com), [MCP Knowledge Server](mcp-server.md) |
| Get AMPL model and `amplpy` code | AMPL Agentic Skill, MCP Knowledge Server |
| Debug an infeasible or slow model | AMPL Agentic Skill, MCP Knowledge Server |
| Write logical constraints with MP operators | AMPL Agentic Skill, MCP Knowledge Server |
| Get answers that cite the AMPL documentation | MCP Knowledge Server, [Gemini Notebook](https://notebooklm.google.com/notebook/cae69bfc-18cf-4ffc-8c44-ca8141a1670f) |
| Set up solver callbacks | AMPL Agentic Skill, Gemini Notebook |
| Use your own AI client or IDE | [MCP Knowledge Server](mcp-server.md) |
| Keep everything on your own servers | [MCP Knowledge Server, on-premises](mcp-server.md#on-premises-deployment) |
| Turn business logic into a model, free and with nothing to install | [Model Builder demo](https://ampl.com/model-builder-demo/) |
| Create study material for a team | Gemini Notebook, MCP Knowledge Server |
| Get AMPL help inside ChatGPT or Gemini | [AMPL for ChatGPT](amplbot-chatgpt.md), [AMPL for Gemini](gemini-assistant.md) |

Performance is not uniform across AI platforms. The underlying LLM is usually the main factor in response quality, reasoning, and accuracy. Because there is no standard way to work with generative AI, we provide AMPL tools that work across several ecosystems so you can choose the one that fits your workflow.

## Validate before you use results

1. Run the generated model and script in your own local or cloud environment. The AMPL tools do not execute models themselves; a coding agent can run them in your environment if you allow it.
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
