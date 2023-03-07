# LINDO Global Solver

LINDO Global is a versatile nonlinear optimizer that supports global optimization in continuous and discrete variables. It accepts a variety of objective and constraint functions, including many that are nonconvex and nonsmooth.

[[Read More](https://ampl.com/products/solvers/solvers-we-sell/lindoglobal/)]
[[Options](options.md)]
[[Changes](changes.md)]
[[Download](https://portal.ampl.com)]

## How to use it

```ampl
ampl: option solver lindoglobal; # change the solver
ampl: option lindoglobal_options 'option1=value1 option2=value2'; # specify options
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