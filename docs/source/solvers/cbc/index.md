# CBC

The COIN Branch and Cut solver (CBC) is an open-source mixed-integer program (MIP) solver written in C++.
The framework used by the driver supports automatic reformulation for many expression types; the modeling guide can be
found [here](https://mp.ampl.com/model-guide.html).

[[Read More](https://ampl.com/products/solvers/open-source-solvers/)]
[[Modeling guide](https://mp.ampl.com/model-guide.html)]
[[Options](options.md)]
[[Changes](changes.md)]
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
options.md
```

## Changelog

```{toctree}
changes.md
```
