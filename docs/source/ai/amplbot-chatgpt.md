# AMPL for ChatGPT

AMPL for ChatGPT is AMPL's specialized AI assistant for optimization, available on the ChatGPT platform as a custom GPT.

For common questions about capabilities, usage, and limits, see the [AMPL for ChatGPT FAQ](faq-amplbot.md).

Use AMPL for ChatGPT to speed up your workflow from first model draft to production-ready optimization apps:

- Learn AMPL syntax and modeling concepts.
- Turn natural-language problem descriptions into structured AMPL models.
- Bridge models to Python applications with `amplpy`.
- Troubleshoot infeasibilities, unboundedness, and solver-performance issues.
- Improve model quality with cleaner formulations and best practices.

Try it here: [AMPL for ChatGPT](https://l.ampl.com/https://chatgpt.com/g/g-68c00de8b030819185be6db190ad7bce-amplbot). Registered and paying ChatGPT accounts may get better performance.

## Why use AMPL for ChatGPT instead of a general-purpose LLM?

AMPL for ChatGPT is focused on optimization modeling with AMPL and practical AMPL+Python workflows. It is designed to provide more reliable guidance for AMPL use cases, from modeling and debugging to deployment patterns.

It references internal documentation, which reduces the probability of hallucinations in its answers. In any case, you should understand and verify the assistant's output.

## Typical prompts

- "Help me formulate a production planning model in AMPL from this business description."
- "Why is my model infeasible? Help me debug it."
- "Convert this AMPL workflow into a Python app using amplpy."
- "Suggest solver options to improve runtime on this problem."

## Notes

- **Code execution:** AMPL for ChatGPT helps you write and improve optimization code but does not execute your model.
- **Verification:** As with any LLM, review generated code and recommendations before using them in production.
- **Other tools:** For day-to-day modeling in your own environment, see the [AMPL Agentic Skill](ampl-agentic-skill.md) and the [AMPL MCP Knowledge Server](mcp-server.md).

For detailed FAQ entries, see the [AMPL for ChatGPT FAQ](faq-amplbot.md).

```{toctree}
:hidden:
:maxdepth: 1

FAQ <faq-amplbot>
```
