# LOQO

LOQO is a powerful solver for smooth constrained optimization problems, based on interior-point method applied to a sequence of quadratic approximations. Subject to the requirement that the defining functions be smooth (at the points evaluated by the algorithm), LOQO can handle a range of problems: linear or nonlinear, convex or nonconvex, constrained or unconstrained. For convex problems, LOQO finds a globally optimal solution; otherwise, it iterates from the given starting point to find a locally optimal solution.

[[Read More](https://ampl.com/products/solvers/solvers-we-sell/loqo/)]
[[Options](options.md)]
[[Changes](changes.md)]
[[Download](https://portal.ampl.com)]

## How to use it

```ampl
ampl: option solver loqo; # change the solver
ampl: option loqo_options 'option1=value1 option2=value2'; # specify options
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