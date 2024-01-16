# COPT

Cardinal Optimizer (COPT) incorporates a full suite of solvers for
linear, convex quadratic, and second-order conic mixed-integer programming.
It ranks at the top of benchmark tests on continuous linear programs,
and has been fully extended to handle integer variables.
The framework used by the driver supports automatic reformulation for many expression types; the modeling guide can be
found [here](https://mp.ampl.com/model-guide.html).


[[Read More](https://ampl.com/products/solvers/solvers-we-sell/copt/)]
[[Modeling guide](https://mp.ampl.com/model-guide.html)]
[[Options](options.md)]
[[Changes](changes.md)]
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
options.md
```

## Changelog

```{toctree}
changes.md
```