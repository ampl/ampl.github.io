# HiGHS

A leading free solver that has evolved from a large-scale optimization project at the University of Edinburgh. HiGHS is open-source software to solve linear programming, mixed-integer programming, and convex quadratic programming models.

[[Read More](https://ampl.com/products/solvers/open-source-solvers/)]
[[Options](options.md)]
[[Changes](changes.md)]
[[Download](https://portal.ampl.com)]

## How to use it

```ampl
ampl: option solver highs; # change the solver
ampl: option highs_options 'option1=value1 option2=value2'; # specify options
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