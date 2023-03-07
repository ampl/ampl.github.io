# Mosek

Mosek is a versatile linear, quadratic, quadratically constrained and semidefinite optimizer that supports continuous and discrete variables. 

[[Read More](https://ampl.com/products/solvers/solvers-we-sell/mosek/)]
[[Options](options.md)]
[[Changes](changes.md)]
[[Download](https://portal.ampl.com)]

## How to use it

```ampl
ampl: option solver mosek; # change the solver
ampl: option mosek_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

## At a glance

### Resources

* [Driver sources](https://github.com/ampl/mp/tree/develop/solvers/mosek)
* [Full list of solver options](options.md)

### Features

* Problem types: 

  * LP, QP, QCP
  * MIP, MIQP, MIQCP

* Features for all models:
    * Problem input
        * [Basis IO](https://amplmp.readthedocs.io/en/latest/rst/features-guide.html#input-and-output-basis)
        * [Warm start](https://amplmp.readthedocs.io/en/latest/rst/features-guide.html#warm-start)

    * Model investigation

        * [Sensitivity analysis](https://amplmp.readthedocs.io/en/latest/rst/features-guide.html#sensitivity-analysis)

    * Dealing with infeasibility/unboundedness
    
        * [Unbounded rays](https://amplmp.readthedocs.io/en/latest/rst/features-guide.html#unbounded-rays)



* Features for MIP models:
    * Model investigation
      * [Return MIP gap](https://amplmp.readthedocs.io/en/latest/rst/features-guide.html#return-mip-gap)
      * [Return best dual bound](https://amplmp.readthedocs.io/en/latest/rst/features-guide.html#return-best-dual-bound)
      

## Solver options

Full list of solver options:
```{toctree}
options.md
```

Many solver parameters can be changed directly from AMPL, by specifying them as a space separated string in the option `mosek_options`. 
A list of all supported options is available [here](options.md) or can be obtained by executing the solver driver with the `-=` command line parameter:

```
mosek -=
```

or from AMPL:

```ampl
shell "mosek -=";
```

Solver options can have multiple aliases, to accomodate for different user types. 
The main numenclature is given first in the -= output, then followed by aliases in brackets,
 see for example the listing for `lim:iter`:

```
lim:iter (iterlim, iterlimit)
      Iteration limit (default: no limit).
```

The main numenclature contains a prefix (`lim:` in this case) to help categorize and find the 
options relevant to a context. To list only the options with a specific prefix (`lim:` for this example), 
run:

```
mosek -=lim:
```

## Specifying solver options and solving a model

After formulating the model in AMPL, execute the following to select Mosek as solver and pass the two options:
`return_mipgap=3` and `outlev=1`.

```ampl
option solver mosek;
option mosek_options "retmipgap=3 outlev=1";
solve;
```

## Retrieving solutions

The outcome of the last optimization is stored in the AMPL parameter `solve_result_num` and the relative message in
`solve_result`.

```ampl
display solve_result_num, solve_result;
```