# Artleys Knitro

Artelys Knitro is an especially powerful nonlinear solver, offering a range of state-of-the-art algorithms and options for working with smooth objective and constraint functions in continuous and integer variables. It is designed for local optimization of large-scale problems with up to hundreds of thousands of variables.

[[Read More](https://ampl.com/products/solvers/solvers-we-sell/knitro/)]
[[Options](options/knitro)]
[[Download](https://portal.ampl.com)]

## How to use it

```ampl
ampl: option solver knitro; # change the solver
ampl: option knitro_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

## Options

Full list of solver options:
```{toctree}
options/knitro
```