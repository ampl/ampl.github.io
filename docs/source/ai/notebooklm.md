# Gemini Notebook for AMPL

The AMPL Notebook is a dedicated, document-grounded AI assistant for mathematical programming and optimization with AMPL, available in Gemini Notebook.

It draws directly from official AMPL literature, including the AMPL book, the `amplpy`, `ampls-api`, and AMPL/MP documentation, solver callback tutorials, and the official style guides. It is designed to accelerate your work from a business problem to a mathematical formulation and on to production-ready Python code.

Use the AMPL Notebook to enhance your optimization workflow:

- **Turn Business Logic into a Model:** Describe your decision problem in plain language and get a formulation with sets, parameters, variables, constraints, and an objective.
- **Write `amplpy` Code:** Connect AMPL models to the Python data ecosystem with `amplpy`, loading pandas DataFrames and other native Python data structures and retrieving results.
- **Master Advanced Syntax:** Learn how to express complex mathematical concepts, such as piecewise-linear functions, logical constraints, and nonlinear programs.
- **Advanced Solver Features:** Search hundreds of solver options for custom runs, or get step-by-step guidance on setting up solver callbacks for solvers like Gurobi, CPLEX, or HiGHS using `ampls-api`.
- **Write Professional Code:** Keep your models readable and scalable by applying the official AMPL naming conventions and formatting best practices.

Try it here: [AMPL Notebook in Gemini Notebook](https://notebooklm.google.com/notebook/cae69bfc-18cf-4ffc-8c44-ca8141a1670f).

## Why use the AMPL Notebook instead of a general-purpose LLM?

Unlike general-purpose LLMs that rely on broad and sometimes outdated training data, the AMPL Notebook offers specific advantages when working with AMPL's documentation:

- **Grounded Answers:** The notebook answers only from the official AMPL source documents loaded into it, which reduces hallucinated AMPL syntax or functions.
- **Verifiable Citations:** Technical claims, syntax rules, and API methods in a response include inline citations. You can click through to the original documentation (such as the AMPL Book or the `amplpy` reference) to verify the context yourself.
- **Focused Context:** The notebook keeps its context on AMPL's ecosystem, so you get specialized answers about `amplpy`, `ampls-api`, and exact solver behaviors.
- **Learning Material:** Beyond chat, you can turn the documentation into study flashcards, structured reports, or audio and video overviews to help your team learn optimization concepts.

## Typical Prompts

- "Formulate a model for this business problem: we ship products from 3 plants to 12 customers and want to minimize cost while meeting demand."
- "Based on the style guide, what are the best practices for naming sets, parameters, and variables in a new model?"
- "Show me how to use `amplpy` to load a pandas DataFrame into my AMPL model."
- "Explain the syntax for declaring a piecewise-linear objective function with multiple slopes."
- "How do I set up a generic Python callback to track MIP node progress in CPLEX?"

## Notes

- **Larger Coding Projects:** The AMPL Notebook can generate models and `amplpy` code. For larger optimization projects, where the assistant works across many files in your own environment, the [AMPL Skill](claude-skills.md) or the [AMPL MCP Knowledge Server](mcp-server.md) may fit better.
- **Verification:** Grounding reduces hallucinations, but you should always review the generated syntax and logic, and run and validate the model, before deploying it to production.
