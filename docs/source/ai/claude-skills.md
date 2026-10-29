# AMPL Skill

The AMPL Skill is a portable Agent Skill that gives your AI assistant specialized knowledge of AMPL: the modeling language, the `amplpy` and `ampls-api` Python interfaces, modeling best practices, solver options, and tutorial content. It helps optimization practitioners, from beginners to advanced users, write correct, idiomatic AMPL models.

Agent Skills are an open, filesystem-based format: a folder with a `SKILL.md` file plus reference material. The AMPL Skill is plain Markdown with no dependency on a particular vendor, so it works with Claude, Codex, Cursor and any other LLM tool or agent runtime that supports the Agent Skills format.

Get it here: [skill.ampl.com](https://skill.ampl.com) (redirects to the [ampl/ampl-agent-skills](https://github.com/ampl/ampl-agent-skills) repository).

## What the skill covers

The skill's `SKILL.md` routes each question to the matching reference file, so the assistant loads only what the task needs:

- **Core language:** syntax, sets and indexing, parameters, variables, objectives and constraints, data files, database access, commands, display, scripting, solver interaction, suffixes, and AMPL options.
- **Modeling patterns:** classic LP, network, columnwise, piecewise-linear, nonlinear, complementarity, and integer programming, plus guidance on choosing between formulations and on building heuristics around a model.
- **`amplpy`:** installation, the core workflow, best practices, and the API reference.
- **`ampls-api`:** solver callbacks, lazy constraints, and solver-native access.
- **MP library:** expressions, multi-objective optimization, reformulation tools, efficiency, and numerical accuracy.
- **Solver options:** tuning guides for Gurobi, CPLEX, Xpress, COPT, HiGHS, CBC, cuOpt, Ipopt, Knitro, SCIP, and MP2NL.
- **Tutorials and examples:** a worked end-to-end tutorial, MP reference models, the Netlib model library, and equivalents across the AMPL APIs.
- **Troubleshooting, benchmarking, and validation:** syntax errors, infeasible or unbounded solves, failing nonlinear solvers, comparing formulations, and deciding whether a result can be trusted.

## Default recommendations

Unless you ask for something else, the skill steers the assistant toward how AMPL is meant to be used in practice:

- **Use an API, not script mode.** Keep the model in a `.mod` file and do everything else (loading data, setting options, solving, retrieving results, control flow) through one of AMPL's APIs.
- **Default to Python with `amplpy`,** unless you specify another language or are already working in one.
- **Prefer MP-based solver drivers** over the legacy ASL drivers where both exist (Gurobi, CPLEX, Xpress).
- **Pick solvers by problem class:** LP/MIP, QP, conic, non-convex, MINLP, general NLP, global optimization, and GPU-accelerated solvers.

`.dat` and `.run` files are not the default for new work, but they are still documented in full, so the assistant can read, debug, and extend existing pure-AMPL projects.

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
- *"Should this constraint be an indicator or a big-M? My MIP is slow."*
- *"Load this pandas DataFrame into my model and return the optimal solution as a DataFrame."*
- *"Set up a callback with ampls-api that adds lazy constraints in Gurobi."*
- *"Which solver should I use for a non-convex MIQCP, and which options should I tune?"*
- *"Explain what this existing `.run` script does and port it to amplpy."*

## What the skill does and doesn't do

- **Knowledge only:** the skill is made only of Markdown reference files. It has no hooks, MCP servers, scripts, or executables, and it does not read, store, or send any data.
- **No execution:** the skill does not run AMPL or any solver. Always run and validate the generated models in your own environment before relying on results. Free AMPL and solver licenses are available at [ampl.com/ce](https://ampl.com/ce) and [ampl.com/courses](https://ampl.com/courses).
- **Snapshot of the docs:** each release reflects AMPL documentation, tutorials, and reference material current as of its release date, not a live feed. For live, source-cited answers, see the [AMPL MCP Knowledge Server](mcp-server.md).
- **Updates:** releases are tagged on GitHub, and the [changelog](https://github.com/ampl/ampl-agent-skills/blob/master/skill/CHANGELOG.md) lists what changed in each version. There is no auto-update: to update, download the new release and replace the installed copy.
- **Trusted sources:** as with installing any software, add Agent Skills only from sources you trust. This skill is published and maintained by AMPL Optimization.
