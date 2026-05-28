# AMPL Modeling Language in NotebookLM

The AMPL Modeling Language Notebook is a dedicated, document-grounded AI assistant for mathematical programming and optimization.

Drawing directly from official AMPL literature—including the comprehensive AMPL book, `amplpy` and `ampls-api` documentation, solver callback tutorials, and official style guides—this environment is designed to accelerate your development from initial mathematical formulation to production-ready Python applications.

Use this NotebookLM environment to enhance your optimization workflow:

- **Master Advanced Syntax:** Learn how to express complex mathematical concepts, such as piecewise-linear functions, network flow constraints, and non-linear programs.
- **Integrate with Python:** Seamlessly connect AMPL models to Python data science ecosystems using `amplpy` to handle Pandas DataFrames and dictionaries.
- **Implement Advanced Solver Features:** Get step-by-step guidance on setting up custom solver callbacks for Gurobi and CPLEX using the `ampls-api`.
- **Write Professional Code:** Ensure your models are readable and scalable by applying official AMPL naming conventions and formatting best practices.

Try it here: [AMPL Workspace on NotebookLM](https://notebooklm.google.com/notebook/cae69bfc-18cf-4ffc-8c44-ca8141a1670f).

## Why use NotebookLM instead of a general-purpose LLM?

Unlike typical LLMs that rely on vast, generalized, and sometimes outdated training data, NotebookLM offers specific advantages tailored for complex technical tasks like AMPL modeling:

- **Zero Hallucination Grounding:** NotebookLM restricts its knowledge strictly to the 29 official source documents loaded into this notebook. It will not invent deprecated functions or hallucinate non-existent AMPL syntax.
- **Verifiable Citations:** Every technical claim, syntax rule, or API method provided in a response includes an inline citation. You can click directly through to the original documentation (like the AMPL Book or the `amplpy` reference) to verify the context yourself.
- **Focused Context Window:** The AI retains deep, persistent context about AMPL's specific ecosystem, meaning you get highly specialized answers regarding `amplpy`, `ampls-api`, and exact solver behaviors.
- **Custom Artifact Generation:** Beyond just chat, you can instantly transform the uploaded documentation into customized study flashcards, structured markdown reports, or even audio/video overviews to help your team learn optimization concepts.

## Typical Prompts

- "Based on the style guide, what are the best practices for naming sets, parameters, and variables in a new model?"
- "Show me how to use `amplpy` to load a Pandas DataFrame into my AMPL model."
- "Explain the syntax for declaring a piecewise-linear objective function with multiple slopes."
- "How do I set up a generic Python callback to track MIP node progress in CPLEX?"
- "What is the difference between the `ampl.eval()` and `ampl.read()` methods when loading a model?"

## Notes

- **Static Code Generation:** the notebook is designed to synthesize documentation, teach concepts, and write optimization code, but it cannot natively compile or execute your AMPL models or Python scripts.
- **Verification:** While NotebookLM reduces hallucinations by grounding its answers in the provided texts, you should always review the generated syntax and logic before deploying models to production environments.
- **Requirements:** you have to be logged in with a google account to use it.
