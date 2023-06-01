# GCG

GCG is a generic decomposition solver for mixed-integer programs (MIPs). It automatically performs a Dantzig-Wolfe reformulation and runs a full-fledged branch-price-and-cut algorithm to solve it to optimality. Alternatively, GCG is able to automatically apply a Benders decomposition. No user interaction is necessary, thus GCG provides decomposition-based MIP solving technology to everyone.

[[Read More](https://ampl.com/products/solvers/open-source-solvers/)]
[[Options](options.md)]
[[Changes](changes.md)]
[[Download](https://portal.ampl.com)]

## How to use it

```ampl
ampl: option solver gcg; # change the solver
ampl: option highs_options 'option1=value1 option2=value2'; # specify options
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