# AMPL Optimization Skill for Claude

The AMPL Optimization Skill is a custom Agent Skill that turns Claude into an expert collaborator for Mathematical Optimization and the AMPL modeling ecosystem. It packages AMPL Optimization's own modern best practices into a self-contained skill that Claude loads automatically whenever you work on an optimization problem, so the models and code you receive reflect how AMPL is meant to be written today rather than the outdated patterns scattered across the public web.

Built for operations research analysts, developers, and engineers, the skill guides Claude to formulate, implement, and debug optimization models with the precision and technical rigor expected in production work.

Get it here: [AMPL Optimization Skill](https://github.com/ampl/claude-for-ampl).

## Key Capabilities

Use the skill to enhance and accelerate your mathematical programming workflows:

- **Modern Two-File Workflow:** Produces a clean `.mod` file containing the model definition and a separate `amplpy` Python file for data loading, solving, and result retrieval, with no legacy `.dat` or `.run` files.
- **Python-First Integration:** Treats Python as the orchestration layer, loading data directly from pandas DataFrames or dictionaries and returning results as DataFrames ready for downstream analysis.
- **Modeling Without Big-M:** Leverages AMPL's MP expression layer (logical, conditional, counting, piecewise-linear, and nonlinear operators) so constraints are expressed directly instead of being manually linearized.
- **Solver-Aware Guidance:** Defaults to open-source HiGHS while knowing when to reach for Gurobi, CPLEX, COPT, Xpress, Mosek, SCIP, BARON, Knitro, and others across LP, MIP, QP, conic, MINLP, NLP, and global optimization.
- **Rigorous Debugging:** Diagnoses infeasible or unbounded models, resolves common AMPL syntax pitfalls, and tunes solver options for performance and numerical stability.
- **Formulation & Translation:** Converts natural-language business descriptions and mathematical formulations into clean, executable, well-structured code.

## Why Use This Skill Over Claude Alone?

A general language model already knows AMPL, but much of what it learned reflects older conventions. This skill closes that gap and operates under explicit, source-grounded constraints:

- **Corrects Outdated Patterns:** Replaces legacy habits (embedded data files, standalone `.run` scripts, hand-coded big-M reformulations, the deprecated AMPL IDE) with the workflow AMPL Optimization recommends today, including the official AMPL VS Code extension.
- **Source-Grounded Best Practices:** Encodes guidance drawn from AMPL's official documentation, the `amplpy` API, and the MP solver interface, with detailed data-loading, result-retrieval, and solver-configuration patterns.
- **Progressive Context Loading:** Stays out of the way until it is relevant, then loads the precise reference material needed (MP expression catalogs, solver capability tables) without bloating every conversation.
- **Algorithmic Precision:** Enforces professional operations research standards such as tight variable bounds, native indicator constraints, correct use of ordered sets and double-inequality constraints, and verification that a model has actually solved before reporting results.

## Typical Prompts

- *"Formulate a multi-period capacity planning model in AMPL and solve it with amplpy from this description."*
- *"My constraint throws an evaluation error. Help me debug it following AMPL's modern conventions."*
- *"Rewrite this big-M reformulation using AMPL's MP logical operators instead."*
- *"Load this pandas DataFrame into my model and return the optimal solution as a DataFrame."*
- *"Which solver should I use for a non-convex MIQCP, and how do I configure it through amplpy?"*

## Operational Notes

- **Automatic Invocation:** Once added, Claude activates the skill on its own whenever a request involves AMPL, amplpy, or optimization modeling. No special command is required, though you can mention it explicitly.
- **Where It Runs:** Custom Agent Skills are available on paid Claude plans and integrate through Claude's code execution environment. You can add the skill in Claude.ai settings, create or load it in Claude Code, or upload it through the Claude API.
- **Code Validation:** The skill excels at generating, refactoring, and explaining optimization code, but does not run live solvers on your behalf. Always execute and validate the generated models in your own environment with a licensed solver before relying on results. Free AMPL and solver licenses are available at ampl.com/ce and ampl.com/courses.
- **Trusted Sources:** As with installing any software, add Agent Skills only from sources you trust. This skill is published and maintained by AMPL Optimization.
