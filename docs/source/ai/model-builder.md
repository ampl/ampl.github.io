# AMPL Model Builder

The AMPL Model Builder is an interactive demo that transforms plain-language business logic directly into optimization models. Powered by AMPL's specialized optimization agent, it guides you through designing, translating, and formulating decision problems in real time.

Try it here: [AMPL Model Builder demo](https://ampl.com/model-builder-demo/). It runs on ampl.com, with nothing to install.

## What you can do

- **Start from a business description:** describe your decision problem in plain language, without writing any mathematical notation first.
- **Design the model with the agent:** the agent helps you identify the structure of the problem: what is decided, what is given, what must hold, and what is optimized.
- **Translate it into a formulation:** go from business rules to sets, parameters, variables, constraints, and an objective.
- **Test AI-drafted models:** explore and adjust the structures, variables, and constraints the agent proposes, instead of starting from scratch.

## When to use it

The Model Builder is best for drafting a first model, especially when the problem is still described in business terms. Once you have a formulation, continue in your own environment:

- Use the [AMPL Skill](claude-skills.md) in your AI assistant to turn the draft into an AMPL model and `amplpy` code, and to refine it.
- Connect the [AMPL MCP Knowledge Server](mcp-server.md) to get source-cited answers while you extend and debug the model.
- Use the [Gemini Notebook for AMPL](notebooklm.md) to look up the AMPL syntax and features the model uses.

## Notes

- **Demo:** the Model Builder is a demonstration of AMPL's optimization agent. To discuss using the agent on your own problems, [contact AMPL](https://ampl.com/contact/sales/).
- **Validation:** AI-drafted formulations can contain mistakes. Check that every constraint matches your business rules, then run the model in your own environment and validate the results before relying on them. Free AMPL and solver licenses are available at [ampl.com/ce](https://ampl.com/ce).
