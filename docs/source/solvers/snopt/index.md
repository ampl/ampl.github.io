# SNOPT

SNOPT is a widely used large-scale optimizer for difficult large-scale nonlinear problems. It incorporates proven methods that have wide applicability and are especially effective for nonlinear problems whose functions and gradients are expensive to evaluate.

[[Read More](https://ampl.com/products/solvers/solvers-we-sell/snopt/)]
[[Options](options.md)]
[[Changes](changes.md)]
[[Download](https://portal.ampl.com)]

## How to use it

```ampl
ampl: option solver snopt; # change the solver
ampl: option snopt_options 'option1=value1 option2=value2'; # specify options
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