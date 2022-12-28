# FICO XPRESS

Xpress offers proven optimization technology for large-scale applications, with out-of-the-box high performance on a wide range of model types.  Its ultra-efficient sparse matrix handling and on-the-fly data compression address the largest problems, with reliable performance even on numerically difficult or unstable problems.
The framework used by the drivers supports automatic reformulation for many expression types; the relative guide can be
found [here](https://amplmp.readthedocs.io/en/latest/rst/model-guide.html#modeling-guide).

[[Read More](https://ampl.com/products/solvers/solvers-we-sell/xpress/)]
[[Options](options.md)]
[[Download](https://portal.ampl.com)]

```{note}
This package contains an all-new Xpress driver, that provides significantly extended modeling support for logical and nonlinear operators through linearizations performed by the [MP library](https://amplmp.readthedocs.io/). For compatibility, there are two binaries in this package: `xpress` [[options](options.md)] is the new version, `xpressasl` [[options](xpressasl.md)] is the legacy version. If you are upgrading an existing installation and encounter any issues with the new version please report them to [support@ampl.com](mailto:support@ampl.com).
```

## How to use it

```ampl
ampl: option solver xpress; # change the solver
ampl: option xpress_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

## At a glance

### Resources

* [Driver sources](https://github.com/ampl/mp/tree/develop/solvers/xpress)
* [Full list of solver options](options.md)

### Features

* Problem types: 

  * LP, QP, QCP
  * MIP, MIQP, MIQCP
  * <details>
    <summary>General constraints</summary>  

    * min / max
    * and / or
    * abs
    </details>

* Features for all models:
    * Problem input
        * [Basis IO](https://amplmp.readthedocs.io/en/latest/rst/features-guide.html#input-and-output-basis)
        * [Warm start](https://amplmp.readthedocs.io/en/latest/rst/features-guide.html#warm-start)
        * [Multiple objectives](https://amplmp.readthedocs.io/en/latest/rst/features-guide.html#multiple-objectives)

    * Model investigation

        * [Multiple solutions](https://amplmp.readthedocs.io/en/latest/rst/features-guide.html#multiple-solutions)

    * Dealing with infeasibility/unboundedness
    
        * [IIS](https://amplmp.readthedocs.io/en/latest/rst/features-guide.html#irreducible-inconsistent-subset-iis)



* Features for MIP models:
    * Model investigation
      * [Return MIP gap](https://amplmp.readthedocs.io/en/latest/rst/features-guide.html#return-mip-gap)
      * [Return best dual bound](https://amplmp.readthedocs.io/en/latest/rst/features-guide.html#return-best-dual-bound)
      * [Fixed model](https://amplmp.readthedocs.io/en/latest/rst/features-guide.html#fixed-model-return-basis-for-mip)


## Solver options

Full list of solver options:
```{toctree}
options.md
```
```{toctree}
:hidden:
xpressasl.md
```

Many solver parameters can be changed directly from AMPL, by specifying them as a space separated string in the option `xpress_options`. 
A list of all supported options is available [here](options.md) or can be obtained by executing the solver driver with the `-=` command line parameter:

```
xpress -=
```

or from AMPL:

```ampl
shell "xpress -=";
```

Solver options can have multiple aliases, to accomodate for different user types. 
The main numenclature is given first in the -= output, then followed by aliases in brackets,
 see for example the listing for `lim:time`:

```
lim:time (timelim, timelimit)
      Limit on solve time (in seconds; default: no limit).
```

The main numenclature contains a prefix (`lim:` in this case) to help categorize and find the 
options relevant to a context. To list only the options with a specific prefix (`lim:` for this example), 
run:

```
xpress -=lim:
```

## Specifying solver options and solving a model

After formulating the model in AMPL, execute the following to select gurobi as solver and pass the two options:
`return_mipgap=3` and `outlev=1`.

```ampl
option solver xpress;
option xpress_options "retmipgap=3 outlev=1";
solve;
```

## Retrieving solutions

The outcome of the last optimization is stored in the AMPL parameter `solve_result_num` and the relative message in
`solve_result`.

```ampl
display solve_result_num, solve_result;
```

## Handling infeasibility

### IIS

When a model is unfeasible, one usedful information is finding the irreducible inconsistent sets, which are subsets of constraints that are
incompatible. This is supported by the framework, see the description [here](https://amplmp.readthedocs.io/en/latest/rst/features-guide.html#irreducible-inconsistent-set-iis).
