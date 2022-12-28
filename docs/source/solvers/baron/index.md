# BARON

BARON is a general nonlinear optimizer capable of solving nonconvex optimization problems to global optimality. Decision variables may be continuous, integer, or a mixture of the two. BARON has been used for applications in the chemical process industries, pharmaceuticals, energy production, engineering design, and asset management.

[[Read More](https://ampl.com/products/solvers/solvers-we-sell/baron/)]
[[Options](options.md)]
[[Download](https://portal.ampl.com)]

## How to use it

```ampl
ampl: option solver baron; # change the solver
ampl: option baron_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

## Options

Full list of solver options:
```{toctree}
options.md
```