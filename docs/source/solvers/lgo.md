# LGO

LGO is capable of determining high-quality solutions to global optimization problems that have (possibly many) locally optimal solutions. Because LGO makes only limited assumptions as to problem structure and differentiability, it can be applied in a broad range of design and operational applications.

[[Read More](https://ampl.com/products/solvers/solvers-we-sell/lgo/)]
[[Options](options/lgo)]
[[Download](https://portal.ampl.com)]

## How to use it

```ampl
ampl: option solver lgo; # change the solver
ampl: option lgo_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

## Options

Full list of solver options:
```{toctree}
options/lgo
```
