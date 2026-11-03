# AMPL Agentic Skill

The AMPL Optimization Skill is a custom Agent Skill that turns your AI assistant into an expert collaborator for Mathematical Optimization and the AMPL modeling ecosystem. It packages AMPL Optimization's own best practices into a self-contained skill loaded automatically whenever you work on an optimization problem, so the models and code you receive reflect how AMPL is meant to be written today. Built to guide on formulation, implemention, debugging optimization models, or translating from business language to optimization code with the precision and technical rigor expected in production work.

Agent Skills are an open, filesystem-based format: a folder with a `SKILL.md` file plus reference material. The AMPL Agentic Skill is plain Markdown with no dependency on a particular vendor, so it works with Claude, Codex, Cursor and any other Agentic runtime that supports the Agent Skills format.

Get it here: [skill.ampl.com](https://skill.ampl.com).

## What the skill covers

The skill's `SKILL.md` routes each question to the matching reference file, so the assistant loads only what the task needs:

- **Modeling patterns:** AMPL instant onboarding, advanced modeling patterns for optimization problems: LP, MILP, nonlinear, complementarity, MINLP, multi-objective formulation analysis and efficiency checks.
- **Formulation & translation:** converts natural-language business descriptions and mathematical formulations into clean, executable, well-structured code.
- **Installation:** guides you through AMPL installation (preferable through `amplpy`) and license activation.
- **`amplpy`:** installation, the core workflow, best practices, and the python API reference.
- **Solver callbacks:** `ampls-api`, lazy constraints, and solver-native access.
- **Interpretability and explainability:** AMPL models are clean and easy to read so they are perfect for Agentic development debugging. It also helps you debug infeasible models.
- **Rigorous debugging, benchmarking, and validation:** diagnoses infeasible or unbounded models and failing nonlinear solvers, resolves syntax errors and common AMPL pitfalls, compares formulations, and helps you decide whether a result can be trusted.
- **MP library:** expressions, multi-objective optimization, reformulation tools, efficiency, and numerical accuracy.
- **Solver performance boost:** tuning guides for Gurobi, CPLEX, Xpress, COPT, HiGHS, CBC, cuOpt, Ipopt, Knitro, SCIP, and MP2NL. The skill will use options to improve the performance of the solver.
- **Tutorials and examples:** a worked end-to-end tutorial, MP reference models, the Netlib model library, and equivalents across the AMPL APIs.

### Default recommendations

Unless you ask for something else, the skill steers the assistant toward how AMPL is meant to be used in practice:

- **Default to Python with `amplpy`,** unless you specify another language or are already working in one. This allows having a clean `.mod` file allowing explainability of your model with the addition of data manipulation in Python, allowing straight data integration from external sources.
- **Modeling without big-M:** leverages AMPL's MP expression layer (logical, conditional, counting, piecewise-linear, and nonlinear operators) so constraints are expressed directly instead of being manually linearized.
- **Pick solvers by problem class:** LP/MIP, QP, conic, non-convex, MINLP, general NLP, global optimization, and GPU-accelerated solvers.

## Install the skill

::::{tab-set}

:::{tab-item} Any AI tool
If your AI tool can browse the web or run commands (for example Claude Code, Codex, or Cursor), you can use the skill for the current session without installing it. Tell your AI tool:

> load skill.ampl.com

To install it permanently, ask your AI tool:

> Install the AMPL agent skill from https://skill.ampl.com — download the `.skill` file from the latest release, unzip it, and add the `ampl-skill` folder to your skills directory.
:::

:::{tab-item} Claude
The repository is a Claude plugin marketplace (Claude Code, claude.ai, Cowork). In Claude Code, run:

```
/plugin install ampl --marketplace ampl/ampl-agent-skills
```

On older versions of Claude Code, run `/plugin marketplace add ampl/ampl-agent-skills` followed by `/plugin install ampl@ampl`.
:::

:::{tab-item} OpenAI Codex
Each [release](https://github.com/ampl/ampl-agent-skills/releases/latest) includes an `ampl-codex-plugin-vX.Y.Z.zip` package in the Codex plugin layout.
:::

:::{tab-item} Manual
The `skill/` folder of the repository is the installable unit. Depending on how your tool supports Agent Skills:

- **Filesystem-based:** copy the contents of `skill/` into the folder where your tool looks for installed skills.
- **Upload-based:** download the `.skill` file from the [latest release](https://github.com/ampl/ampl-agent-skills/releases/latest) and upload it wherever your tool accepts skill packages. It is a standard zip archive, so you can rename it to `.zip` if your tool requires that.

Check your tool's documentation for the exact mechanism it expects.
:::

::::

## Typical prompts

- *"Formulate a multi-period capacity planning model in AMPL and solve it with amplpy from this description."*
- *"Create an application to schedule flights on time in the US."*
- *"Load this pandas DataFrame into my model and return the optimal solution as a DataFrame."*
- *"Set up a callback with ampls-api that adds lazy constraints in Gurobi."*
- *"Which solver should I use for a non-convex MIQCP, and which options should I tune?"*
- *"Explain what this existing `.run` script does and port it to amplpy."*


## What the skill does and doesn't do

- **Knowledge only:** the skill is made only of Markdown reference files. You can give internet access to your Agents so it can search on the internet as well. It has no hooks, MCP servers, scripts, or executables, and it does not read, store, or send any data.
- **No execution:** the skill does not run AMPL or any solver directly. Always run and validate the generated models in your own environment before relying on results. Free AMPL and solver licenses are available at [ampl.com/academia](https://ampl.com/academia) and [ampl.com/ce](https://ampl.com/ce).
- **Snapshot of the docs:** each release reflects AMPL documentation, tutorials, and reference material current as of its release date, not a live feed. For live, source-cited answers, see the [AMPL MCP Knowledge Server](mcp-server.md).
- **Updates:** releases are tagged on GitHub, and the [changelog](https://github.com/ampl/ampl-agent-skills/blob/master/skill/CHANGELOG.md) lists what changed in each version. There is no auto-update: to update, download the new release and replace the installed copy.
- **Trusted sources:** as with installing any software, add Agent Skills only from sources you trust. This skill is published and maintained by AMPL Optimization.
