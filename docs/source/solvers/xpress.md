# FICO XPRESS

Xpress offers proven optimization technology for large-scale applications, with out-of-the-box high performance on a wide range of model types.  Its ultra-efficient sparse matrix handling and on-the-fly data compression address the largest problems, with reliable performance even on numerically difficult or unstable problems.

[[Read More](https://ampl.com/products/solvers/solvers-we-sell/xpress/)]
[[Options](options/xpress)]
[[Download](https://portal.ampl.com)]

## How to use it

```ampl
ampl: option solver xpress; # change the solver
ampl: option xpress_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

## Options

Full list of solver options:
```{toctree}
options/xpress
```