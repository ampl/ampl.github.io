# IBM CPLEX

IBM ILOG CPLEX has been a well known and widely used large-scale solver for over three decades. Its efficiency and robustness have been demonstrated through varied applications in thousands of commercial installations worldwide.

[[Read More](https://ampl.com/products/solvers/solvers-we-sell/cplex/)]
[[Options](#solver-options)]
[[Changes](changes.md)]
[[Download CPLEX](https://portal.ampl.com/user/ampl/download/cplex)]

## How to use it
CPLEX options consist of a single-word option, or an option followed by an = sign and a value; a space may be used as a separator in place of the =.

```ampl
ampl: option solver cplex; # change the solver
ampl: option cplex_options 'single-word-option option1=value1 option2 value2'; # specify options
ampl: solve; # solve the problem
```

## Resources

* [Solver options](#solver-options)
* [Using with callbacks](https://ampls.ampl.com/)

## Solver options

Full list of solver options:
```{toctree}
options.md
```
```{toctree}
:hidden:
cplexmp.md
```

## Changelog

```{toctree}
changes.md
```
```{toctree}
:hidden:
changesmp.md
```