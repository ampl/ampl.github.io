# CBC

The COIN Branch and Cut solver (CBC) is an open-source mixed-integer program (MIP) solver written in C++.

[[Read More](https://ampl.com/products/solvers/open-source-solvers/)]
[[Options](options/cbc)]
[[Download](https://portal.ampl.com)]

## How to use it

```ampl
ampl: option solver cbc; # change the solver
ampl: option cbc_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

## Options

Full list of solver options:
```{toctree}
options/cbc
```
