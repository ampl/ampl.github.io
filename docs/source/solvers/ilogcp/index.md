# ILOG CP

IBM ILOG CP Optimizer is a generic CP-based system to model and solve scheduling problems.

[[Read More](https://ampl.com/products/solvers/solvers-we-sell/cplex/)]
[[Options](options.md)]
[[Changes](changes.md)]
[[Download](https://portal.ampl.com)]

## How to use it

```ampl
ampl: option solver ilogcp; # change the solver
ampl: option ilogcp_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

## Options

Full list of solver options:
```{toctree}
options.md
```

## Changelog

```{toctree}
changes.md
```