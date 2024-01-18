# Octeract

The Octeract Engine supports global optimization of mixed-integer nonlinear optimization problems. It is designed to achieve substantial speedups on very large numbers of parallel processing nodes, while also performing efficiently on multi-core shared memory architectures.

[[Read More](https://ampl.com/products/solvers/solvers-we-sell/octeract/)]
[[Download Octeract](https://portal.ampl.com/user/ampl/download/octeract)]

## How to use it

```ampl
ampl: option solver octeract; # change the solver
ampl: option octeract_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```