(mp2nl)=

# MP2NL

MP2NL translates MP-compatible syntax and features to any AMPL solver:
the expressions described in the [MP Modeling Guide](https://mp.ampl.com/model-guide.html)
(logical and counting constraints, piecewise-linear terms, complementarity, ...)
are reformulated for a solver that reads only the classic NL format.
While this might mostly benefit MINLP solvers, such as
[Knitro](../knitro/index.md)
or [Couenne](../couenne/index.md),
NLP solvers (such as [Ipopt](../ipopt/index.md))
could benefit from automatic reformulation
of complementarity constraints
or (convex) piecewise-linear expressions.

## Invocation

Some of the
{ref}`nonlinear AMPL solvers <nonlinear-solvers>`
(currently [Knitro](../knitro/index.md),
[BARON](../baron/index.md),
[CONOPT](../conopt/index.md),
[LINDO Global](../lindoglobal/index.md)),
as well as the legacy solvers
[gurobiasl](../gurobi/index.md),
[cplexasl](../cplex/index.md),
[xpressasl](../xpress/index.md)
include the bridge and support option `mp2nl=1`.
For any other AMPL solver, call `mp2nl` as the solver and name the real
solver (the *subsolver*) inside it:

::::{tab-set}
:::{tab-item} Python
```python
# a driver with the bridge built in
ampl.solve(solver="knitro", knitro_options="mp2nl=1 outlev=1")

# any other NL solver: MP2NL is the solver, the subsolver is named inside
ampl.solve(solver="mp2nl",
           mp2nl_options="solver=ipopt cvt:compl=2 cvt:compl:eps=1e-8 lim:time=60",
           ipopt_options="print_level=0")
```
:::
:::{tab-item} AMPL
```ampl
ampl: option knitro_options 'mp2nl=1 outlev=1';
ampl: option solver knitro; solve;

ampl: option solver mp2nl;
ampl: option mp2nl_options 'solver=ipopt cvt:compl=2 cvt:compl:eps=1e-8 lim:time=60';
ampl: option ipopt_options 'print_level=0';
ampl: solve;
```
:::
::::

Enable the bridge whenever the model uses MP's expressions, including the
`==>` syntax of indicator constraints: a solver that does not understand such
a construct may misread the model without an error message.

## Where the options go

- `mp2nl_options`: MP's options. `solver=`, `cvt:...` (reformulations),
  `acc:...` (what the subsolver accepts), `sol:chk:...` (solution check),
  and generic ones such as `lim:time`, `mip:gap`, `outlev`.
  `lim:time` and `mip:gap` are passed on as the subsolver's own keywords
  where MP2NL knows them.
- `<subsolver>_options`: the subsolver's own keywords. MP keywords placed
  here are usually rejected by the subsolver, and the solve fails.
- With a built-in bridge (`mp2nl=1`), pass MP's `cvt:...` and `sol:chk:...`
  options through the AMPL option `mp_options`.

## Choosing the subsolver

MP reformulates logic with binary variables, so the subsolver must accept the
problem class *after* reformulation (`outlev=1` prints the model before and
after). A continuous NLP subsolver relaxes those binaries and can report an
optimal solution that violates the logic; MP's automatic solution check then
prints "Tolerance violations". Use an MINLP solver for models with logic;
complementarity constraints alone, with a smooth reformulation (`cvt:compl=1`
or `2`), can go to an NLP solver.

The status is the subsolver's: a local solver's "optimal" on a nonconvex
model is a local optimum.

More: the MP documentation section
[Meta-driver MP2NL](https://mp.ampl.com/modeling-tools.html#meta-driver-mp2nl)
(configurations, `printconfigs`, `config=`, `stub=`, complementarity
reformulations), and the notebooks tagged
[mp2nl](https://colab.ampl.com/tags/mp2nl.html).

## Features

### Instrumentation

For a generic summary of the options and features used most often, see
[Important features](https://mp.ampl.com/features-guide.html#important-features)
in the MP documentation.

```{include} features.inc
```

## Solver options

Full list of solver options:
```{toctree}
options.md
```

## Retrieving solutions

The outcome of the last optimization is stored in the AMPL parameter `solve_result_num` and the relative message in
`solve_result`.

```ampl
display solve_result_num, solve_result;
```

MP2NL solve result codes can be obtained by running `mp2nl -!` or `ampl: shell "mp2nl -!";`:
```{literalinclude} solve_results.inc
:language: none
```

For general information, see [MP result codes guide](https://mp.ampl.com/features-guide.html#solve-result-codes).

## Changelog

```{toctree}
changes.md
```