# COPT

Cardinal Optimizer (COPT) incorporates a full suite of solvers for linear and convex quadratic mixed-integer programming. It ranks at the top of benchmark tests on continuous linear programs, and has been fully extended to handle integer variables.

[[Read More](https://ampl.com/products/solvers/solvers-we-sell/copt/)]
[[Options](options/copt)]
[[Download](https://portal.ampl.com)]

## How to use it

```ampl
ampl: option solver copt; # change the solver
ampl: option copt_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

## Options

Full list of solver options:
```{toctree}
options/copt
```
