# AMPL MCP Knowledge Server

The AMPL MCP Knowledge Server connects MCP-capable AI assistants to a curated AMPL knowledge base. The Model Context Protocol (MCP) lets an assistant call external tools. With this server, the assistant searches AMPL-specific material before every answer, so its guidance is grounded in AMPL sources instead of generic model memory.

It works with Claude, ChatGPT-style agents, Gemini workflows, Cursor, Copilot-style environments, Codex, and other MCP-aware clients.

## What you can do

- Get source-cited explanations of AMPL constructs.
- Build a new optimization model from a natural-language description.
- Adapt an existing industry model to a new dataset or business case.
- Convert AMPL examples into `amplpy` notebooks or Python scripts.
- Debug syntax errors, infeasibility, unboundedness, and numerical issues.
- Improve weak formulations with modern AMPL and MP constructs.
- Choose candidate solvers by problem class.

## How it works

1. You ask an AMPL, `amplpy`, solver, or optimization-modeling question.
2. The assistant selects a retrieval mode: explain, implement, debug, or enumerate.
3. It searches the knowledge base, and loads the style guide before writing or reviewing code.
4. It answers from the retrieved evidence and cites the source URLs it used.
5. You can rate the answer from 1 to 5. Ratings are stored with the retrieval keys, so weak answers can be traced to missing coverage, poor retrieval, or synthesis problems.

### Retrieval modes

Separate modes keep correct implementation examples apart from incorrect code that is kept only for diagnosis.

::::{tab-set}

:::{tab-item} Explain
**Use for:** Concepts, syntax meaning, solver concepts, and modeling explanations.

**Tool:** `search_kb` with mode `explain`

**Example:** *"What does a defined variable do in AMPL, and when should I use one?"*
:::

:::{tab-item} Implement
**Use for:** New code, examples, templates, and model construction.

**Tool:** `search_kb` with mode `implement`, plus `get_style_guide`

**Example:** *"Adapt the transportation example to my 12 warehouses and load the data from pandas."*
:::

:::{tab-item} Debug
**Use for:** Errors, infeasibility, wrong syntax, and formulation repair.

**Tool:** `search_kb` with mode `debug`, then `get_chunk` for the correction

**Example:** *"My model is infeasible after I added the capacity constraint. What is wrong?"*
:::

:::{tab-item} Enumerate
**Use for:** Completeness questions such as "list all X" or "every function of Y".

**Tool:** `enumerate_kb_section`

**Example:** *"List every option of the HiGHS solver interface."*
:::

::::

### Source priority

| Source | How it is used |
| --- | --- |
| Official AMPL documentation | Primary source for syntax, APIs, and solver-interface behavior |
| Forum discussions | Practical diagnosis; never overrides official documentation |
| Material marked for review | Secondary evidence only |
| Known wrong patterns | Never presented as valid code; linked to the corrected pattern |

## Available tools

| Tool | Purpose | When it is called |
| --- | --- | --- |
| `search_kb` | Searches AMPL, `amplpy`, solver, and modeling content | Before every AMPL answer |
| `enumerate_kb_section` | Returns every entry of a documentation section, in order | For completeness questions, where top results could miss entries |
| `get_chunk` | Fetches a full passage by its key | When a search hit is truncated or points to a correction |
| `get_style_guide` | Loads AMPL and `amplpy` style rules | Before writing or reviewing model files or `amplpy` code |
| `get_response_guide` | Loads the answering rules shared by all clients | Once, on the first AMPL question of a conversation |
| `list_doc_areas` | Lists the areas the corpus covers | For routing, filtering, and coverage checks |
| `rate_response` | Records a 1–5 rating and a comment | When you rate an answer |

## Example models

The knowledge base includes complete AMPL models and end-to-end examples. The assistant can retrieve a nearby example and adapt its sets, parameters, constraints, and objective to your case. Covered problem families include production planning, blending, diet, transportation, assignment, scheduling, network flows, logistics, energy, finance, and optimization under uncertainty.

Answers can target pure AMPL (`.mod`, `.dat`, `.run`), `amplpy` in Jupyter, an `amplpy` script with a separate `.mod` file, or Java and other APIs.

## Connect your assistant

Add the server to your client's MCP configuration. The tools appear under the name `ampl_kb`.

```json
{
  "mcpServers": {
    "ampl_kb": {
      "type": "http",
      "url": "https://mcp-kb.ampl.com/mcp"
    }
  }
}
```

:::{note}
The server uses OAuth sign-in. The first time your client connects, it asks you to sign in.
:::

## On-premises deployment

AMPL is prepared to provide the MCP Knowledge Server for deployment on your local servers, for complete security. Searches, ratings, and logs stay inside your network, under your own security and access policies. Combined with a locally hosted language model, no question, model, or data leaves your infrastructure.

To discuss an on-premises deployment, [contact AMPL sales](https://ampl.com/contact/sales/).

## Execution boundary

:::{important}
The server supplies evidence and guidance. It does not execute optimization models. Output shown without a real run is labeled unverified. When you explicitly ask for execution and your environment supports it, the assistant shows the solver output, solve status, objective value, and key decision values.
:::
