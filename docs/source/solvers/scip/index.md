# SCIP

SCIP is currently one of the fastest non-commercial solvers for mixed integer programming (MIP)
and mixed integer nonlinear programming (MINLP). It is also a framework for constraint integer
programming and branch-cut-and-price. It allows for total control of the solution process and
the access of detailed information down to the guts of the solver.
The framework used by the driver supports automatic reformulation for many expression types; the modeling guide can be
found [here](https://mp.ampl.com/model-guide.html).

[[Read More](https://ampl.com/products/solvers/open-source-solvers/)]
[[Modeling guide](https://mp.ampl.com/model-guide.html)]
[[Options](options.md)]
[[Changes](changes.md)]
[[Download SCIP](https://portal.ampl.com/user/ampl/download/scip)]

## How to use it

```ampl
ampl: option solver scip; # change the solver
ampl: option highs_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

## Resources

* [Modeling guide](https://mp.ampl.com/model-guide.html)
* [Driver sources](https://github.com/ampl/mp/tree/develop/solvers/scipmp)

## Options

Full list of solver options:
```{toctree}
options.md
```

More details on solver options: [Features guide](https://mp.ampl.com/features-guide.html).


## Changelog

```{toctree}
changes.md
```