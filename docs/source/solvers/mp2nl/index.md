# MP2NL

MP2NL translates MP-compatible syntax and features to any AMPL solver.
While this might mostly benefit MINLP solvers, such as
[Knitro](../knitro/index.md)
or [Couenne](../couenne/index.md),
NLP solvers (such as [Ipopt](../ipopt/index.md))
could benefit from automatic reformulation
of complementarity constraints
or (convex) piecewise-linear expressions.

## Invocation

Some of the
[nonlinear AMPL solvers](../index.rst#nonlinear-solvers)
(currently [Knitro](../knitro/index.md),
[Baron](../baron/index.md),
[Conopt](../conopt/index.md)),
as well as the legacy solvers
[gurobiasl](../gurobi/index.md),
[cplexasl](../cplex/index.md),
[xpressasl](../xpress/index.md)
support option `mp2nl=1`:

```ampl
ampl: option knitro_options 'soltype=1 mp2nl=1';
ampl: solve;
```

For any other AMPL solver, invoke `mp2nl` manually:

```python
ampl.solve(solver='mp2nl',
           ipopt_options='max_cpu_time 15',
           mp2nl_options='solver=ipopt cvt:compl=2 cvt:compl:eps=1e-8')
```

## Solver options

Full list of solver options:
```{toctree}
options.md
```

## Changelog

```{toctree}
changes.md
```