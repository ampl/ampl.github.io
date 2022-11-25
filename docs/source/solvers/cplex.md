# IBM CPLPEX

IBM ILOG CPLEX has been a well known and widely used large-scale solver for over three decades. Its efficiency and robustness have been demonstrated through varied applications in thousands of commercial installations worldwide.

[[Read More](https://ampl.com/products/solvers/solvers-we-sell/cplex/)]
[[Options](options/cplex)]
[[Download](https://portal.ampl.com)]

## How to use it

```ampl
ampl: option solver cplex; # change the solver
ampl: option cplex_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

## Options

Full list of solver options:
```{toctree}
options/cplex
```