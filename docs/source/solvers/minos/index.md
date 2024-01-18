# MINOS

MINOS is an established choice for both linear and nonlinear optimization problems. It incorporates proven methods for large-scale sparse nonlinear constraints, and its methods are especially effective for nonlinear objectives subject to linear and near-linear constraints.

[[Read More](https://ampl.com/products/solvers/solvers-we-sell/minos/)]
[[Options](options.md)]
[[Changes](changes.md)]
[[Download MINOS](https://portal.ampl.com/user/ampl/download/minos)]

## How to use it

```ampl
ampl: option solver minos; # change the solver
ampl: option minos_options 'option1=value1 option2=value2'; # specify options
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