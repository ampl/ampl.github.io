# CONOPT

A proven choice for highly nonlinear problems, CONOPT’s efficient and reliable multi-method architecture handles a broad range of models. Specialized techniques achieve feasibility quickly, while powerful preprocessing tools reduce problem size and suggest formulation improvements.

[[Read More](https://ampl.com/products/solvers/solvers-we-sell/conopt/)]
[[Options](options.md)]
[[Download](https://portal.ampl.com)]

## How to use it

```ampl
ampl: option solver conopt; # change the solver
ampl: option conopt_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

## Options

Full list of solver options:
```{toctree}
options.md
```