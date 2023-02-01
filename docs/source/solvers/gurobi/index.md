# Gurobi

Gurobi is a powerful commercial suite of optimization products, which includes simplex and parallel barrier solvers to handle linear programming (LP) and quadratic progermming (QP), also quadratically constrained (QCP) and the mixed-integer variations thereof (MIP, MIQP, MIQCP). It also supports some types of general constraints.
The framework used by the drivers supports automatic reformulation for many expression types; the relative guide can be
found [here](https://amplmp.readthedocs.io/en/latest/rst/model-guide.html#modeling-guide).

[[Read More](https://ampl.com/products/solvers/solvers-we-sell/gurobi/)]
[[Options](options.md)]
[[Download](https://portal.ampl.com)]

```{note}
Our enhanced Gurobi driver (previously know as x-gurobi) is now the default Gurobi driver. The new driver provides significantly extended modeling support for logical and nonlinear operators natively through Gurobi’s built-in “general constraints” and through linearizations performed by the [MP library](https://amplmp.readthedocs.io/). There are two binaries in this package: `gurobi` [[options](options.md)] is the new version, `gurobiasl` [[options](gurobiasl)] is the legacy version. If you are upgrading an existing installation and encounter any issues with the new version please report them to [support@ampl.com](mailto:support@ampl.com).
```

## How to use it

```ampl
ampl: option solver gurobi; # change the solver
ampl: option gurobi_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

## At a glance

### Resources

* [Driver sources](https://github.com/ampl/mp/tree/develop/solvers/gurobi)
* [Full list of solver options](options.md)

### Features

* Problem types: 

  * LP, QP, QCP
  * MIP, MIQP, MIQCP
  * <details>
    <summary>General constraints</summary>  

    * log / exp
    * min / max
    * and / or
    * abs
    * sin/cos/tan
    * norm
    </details>



* Features for all models:
    * Problem input
        * [Basis IO](https://amplmp.readthedocs.io/en/latest/rst/features-guide.html#input-and-output-basis)
        * [Warm start](https://amplmp.readthedocs.io/en/latest/rst/features-guide.html#warm-start)
        * [Multiple objectives](https://amplmp.readthedocs.io/en/latest/rst/features-guide.html#multiple-objectives)

    * Model investigation

        * [Condition number](https://amplmp.readthedocs.io/en/latest/rst/features-guide.html#kappa)
        * [Multiple solutions](https://amplmp.readthedocs.io/en/latest/rst/features-guide.html#multiple-solutions)
        * [Sensitivity analysis](https://amplmp.readthedocs.io/en/latest/rst/features-guide.html#sensitivity-analysis)

    * Dealing with infeasibility/unboundedness
    
        * [Feasibility relaxation](https://amplmp.readthedocs.io/en/latest/rst/features-guide.html#feasibility-relaxation)
        * [IIS](https://amplmp.readthedocs.io/en/latest/rst/features-guide.html#irreducible-inconsistent-subset-iis)
        * [Unbounded rays](https://amplmp.readthedocs.io/en/latest/rst/features-guide.html#unbounded-rays)



* Features for MIP models:
    * Model investigation
      * [Return MIP gap](https://amplmp.readthedocs.io/en/latest/rst/features-guide.html#return-mip-gap)
      * [Return best dual bound](https://amplmp.readthedocs.io/en/latest/rst/features-guide.html#return-best-dual-bound)
      * [Fixed model](https://amplmp.readthedocs.io/en/latest/rst/features-guide.html#fixed-model-return-basis-for-mip)
    * Solution process:
      * [Lazy constraints and user cuts](https://amplmp.readthedocs.io/en/latest/rst/features-guide.html#lazy-constraints-and-user-cuts)
      * [Branching variable priorites](https://amplmp.readthedocs.io/en/latest/rst/features-guide.html#variable-priorities)
      

## Solver options

Full list of solver options:
```{toctree}
options.md
```
```{toctree}
:hidden:
gurobiasl.md
```

Many solver parameters can be changed directly from AMPL, by specifying them as a space separated string in the option `gurobi_options`. 
A list of all supported options is available [here](options.md) or can be obtained by executing the solver driver with the `-=` command line parameter:

```
gurobi -=
```

or from AMPL:

```ampl
shell "gurobi -=";
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
gurobi -=lim:
```

## Specifying solver options and solving a model

After formulating the model in AMPL, execute the following to select gurobi as solver and pass the two options:
`return_mipgap=3` and `outlev=1`.

```ampl
option solver gurobi;
option gurobi_options "retmipgap=3 outlev=1";
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


### Feasibility Relaxation

Another approach to tackle infeasibilities is to use feasibility relaxation to find a solution which only penalizes infeasibilities. 
This is supported via the framework, see the description  [here](https://amplmp.readthedocs.io/en/latest/rst/features-guide.html#feasibiliyrelaxation).


## Gurobi compute server and Gurobi cloud

Gurobi supports solving your model on other machines in two alternative ways:
* [Compute server](https://www.gurobi.com/products/gurobi-compute-server/) - where a computer (or a cluster) can be configured to the specific task of solving models via gurobi
* [Gurobi cloud](https://www.gurobi.com/products/gurobi-instant-cloud/) - where the compute server is by Gurobi itself 

To use a compute server, the option `tech:server` must be set, together with appropriate values for the `tech:server_*` options.
For gurobi instant cloud, the options `tech:cloudid` and `tech:cloudkey` must be set, and optionally the other options `tech:cloud*`, for example:

```ampl

# Solve with compute server
option gurobi_options "tech:server=192.168.1.55";
solve;

# Solve with gurobi instant cloud
option gurobi_options "tech:cloudid=mygurobiid tech:cloudkey=myprivatekey";
solve;
```