# Gurobi

Gurobi is a powerful commercial suite of optimization products, which includes simplex
and parallel barrier solvers to handle linear programming (LP) and quadratic programming (QP),
also quadratically constrained (QCP, SOCP) and the mixed-integer variations thereof (MIP, MIQP, MIQCP, MISOCP).
It also supports some types of general constraints, this addressing MINLP.
The framework used by the driver supports automatic reformulation for many expression types; the modeling guide can be
found [here](https://mp.ampl.com/model-guide.html).

[[Read More](https://ampl.com/products/solvers/solvers-we-sell/gurobi/)]
[[Modeling guide](https://mp.ampl.com/model-guide.html)]
[[Options](#solver-options)]
[[Changes](changes.md)]
[[Download Gurobi](https://portal.ampl.com/user/ampl/download/gurobi)]

Our enhanced Gurobi driver (previously know as x-gurobi) is now the default Gurobi driver. The new driver provides significantly extended modeling support for logical and nonlinear operators natively through Gurobi’s built-in “general constraints” and through linearizations performed by the [MP library](https://mp.ampl.com/). There are two binaries in this package: `gurobi` [[options](options.md)] is the new version, `gurobiasl` [[options](gurobiasl)] is the legacy version. If you are upgrading an existing installation and encounter any issues with the new version please report them to [support@ampl.com](mailto:support@ampl.com).

## How to use it

```{eval-rst}

.. tabs::

   .. tab:: AMPL

        .. code-block:: ampl

            ampl: option solver gurobi; # change the solver
            ampl: option gurobi_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem

   .. tab:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install gurobi # install Gurobi

            # Activate your license (e.g., free ampl.com/ce or ampl.com/courses licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="gurobi", gurobi_options="option1=value1 option2=value2")

        Learn more about what we have to offer to implement and deploy `Optimization in Python <https://ampl.com/python/>`_.

   .. tab:: Other APIs

        `AMPL APIs <https://ampl.com/apis/>`_ are interfaces that allow developers to access the features of the AMPL interpreter from within a programming language. We have APIs available for:

        - `Python <https://ampl.com/api/latest/python>`_
        - `R <https://ampl.com/api/latest/R>`_
        - `C++ <https://ampl.com/api/latest/cpp>`_
        - `C#/.NET <https://ampl.com/api/latest/dotnet>`_
        - `Java <https://ampl.com/api/latest/java>`_
        - `MATLAB <https://ampl.com/api/latest/matlab>`_
```

## At a glance

### Resources

* [Modeling guide](https://mp.ampl.com/model-guide.html)
* [Solver options](#solver-options)
* [Solve result codes](#retrieving-solutions)
* [Driver sources](https://github.com/ampl/mp/tree/develop/solvers/gurobi)
* [Using with callbacks](https://ampls.ampl.com/)

### Features

* Problem types: 

  * LP, QP, QCP, SOCP
  * MIP, MIQP, MIQCP, MISOCP, MINLP
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
        * [Basis IO](https://mp.ampl.com/features-guide.html#input-and-output-basis)
        * [Warm start](https://mp.ampl.com/features-guide.html#warm-start)
        * [Multiple objectives](https://mp.ampl.com/features-guide.html#multiple-objectives)

    * Model investigation

        * [Condition number](https://mp.ampl.com/features-guide.html#kappa)
        * [Multiple solutions](https://mp.ampl.com/features-guide.html#multiple-solutions)
        * [Sensitivity analysis](https://mp.ampl.com/features-guide.html#sensitivity-analysis)

    * Dealing with infeasibility/unboundedness
    
        * [Feasibility relaxation](https://mp.ampl.com/eatures-guide.html#feasibility-relaxation)
        * [IIS](https://mp.ampl.com/features-guide.html#irreducible-inconsistent-subset-iis)
        * [Unbounded rays](https://mp.ampl.com/features-guide.html#unbounded-rays)



* Features for MIP models:
    * Model investigation
      * [Return MIP gap](https://mp.ampl.com/features-guide.html#return-mip-gap)
      * [Return best dual bound](https://mp.ampl.com/features-guide.html#return-best-dual-bound)
      * [Fixed model](https://mp.ampl.com/features-guide.html#fixed-model-return-basis-for-mip)
    * Solution process:
      * [Lazy constraints and user cuts](https://mp.ampl.com/features-guide.html#lazy-constraints-and-user-cuts)
      * [Branching variable priorites](https://mp.ampl.com/features-guide.html#variable-priorities)
      

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

More details on solver options: [Features guide](https://mp.ampl.com/features-guide.html).


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

Gurobi solve result codes can be obtained by running `gurobi -!` or `ampl: shell "gurobi -!";`:

| Value | Message                                                     |
|-------|-------------------------------------------------------------|
| 0     | optimal solution                                            |
| 1     | optimal solution with integer variables rounded to integers |
| 2     | optimal solution with nonintegral "integer" variables       |
| 100   | suboptimal: could not satisfy optimality tolerances        |
| 101   | bestbndstop reached                                         |
| 102   | bestobjstop reached                                         |
| 103   | bestobjstop or bestbndstop reached                          |
| 104   | bestobjstop or bestbndstop reached with no solution available |
| 200   | infeasible [IIS computation not attempted]                  |
| 201   | infeasible [IIS returned]                                   |
| 202   | infeasible [IIS finder failed]                              |
| 203   | infeasible; .dunbdd returned [IIS computation not attempted] |
| 204   | infeasible; .dunbdd returned [IIS also returned]            |
| 205   | infeasible; .dunbdd returned [IIS finder failed]            |
| 300   | unbounded                                                   |
| 301   | unbounded [unbounded or infeasible; IIS finder failed]      |
| 302   | unbounded; .unbdd returned                                  |
| 303   | unbounded; .unbdd returned [IIS finder failed]              |
| 400   | objective cutoff                                            |
| 401   | iteration limit with a feasible solution                    |
| 402   | node limit with a feasible solution                         |
| 403   | time limit with a feasible solution                         |
| 404   | solution limit                                              |
| 405   | interrupted with a feasible solution                        |
| 411   | iteration limit without a feasible solution                 |
| 412   | node limit without a feasible solution                      |
| 413   | time limit without a feasible solution                      |
| 415   | interrupted without a feasible solution                     |
| 500   | Could not create the gurobi environment                     |
| 501   | Gurobi call failed [message gives routine name]             |
| 502   | misc. failure [message gives details]                       |
| 503   | Bad `$gurobi_options`                                       |
| 504   | Surprise VBasis[...] = ...                                  |
| 505   | Surprise CBasis[...] = ...                                  |
| 506   | Gurobi set/get parameter failed [message gives more  details] |
| 510   | cannot open logfile (specified in $gurobi_options or command line) |
| 511   | cannot open paramfile (specified in $gurobi_options or command line) |
| 512   | missing value in paramfile                                  |
| 513   | extra text in paramfile                                     |
| 514   | invalid parameter name in paramfile                         |
| 520   | numeric error                                               |
| 521   | nonlinear objective                                         |
| 522   | nonlinear constraint                                        |
| 523   | quadratic objective involving division by 0                 |
| 524   | indefinite quadratic objective or constraint                |
| 525   | quadratic constraint involving division by 0                |
| 530   | could not open serverlic file                               |
| 531   | error in serverlic file                                     |
| 532   | error while tuning                                          |
| 540   | Gurobi Compute Server not reached or bad `pool_...` settings |
| 541   | Rejected by Gurobi Compute Server                           |
| 542   | Feature not supported by Gurobi Compute Server              |
| 543   | Feature not supported                                       |
| 563   | logical constraint is not an indicator constraint           |
| 564   | bad suffixes for multiple objectives                        |
| 565   | Error return from named routine                             |
| 567   | complementarity constraint                                  |
| 570   | solution found but not available                            |
| 601   | could not talk to Gurobi compute server                     |
| 602   | job rejected by Gurobi compute server                       |
| 603   | no license for specified gurobi compute server              |
| 604   | surprise return while trying to use Gurobi compute server   |
| 605   | bad value for `cloudid` or `cloudkey`, or Gurobi Cloud out of reach |

For general information, see [MP result codes guide](https://mp.ampl.com/features-guide.html#solve-result-codes).

## Handling infeasibility

### IIS

When a model is unfeasible, one usedful information is finding the irreducible inconsistent sets, which are subsets of constraints that are
incompatible. This is supported by the framework, see the description [here](https://mp.ampl.com/features-guide.html#irreducible-inconsistent-set-iis).


### Feasibility Relaxation

Another approach to tackle infeasibilities is to use feasibility relaxation to find a solution which only penalizes infeasibilities. 
This is supported via the framework, see the description  [here](https://mp.ampl.com/features-guide.html#feasibiliyrelaxation).


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

## Changelog

```{toctree}
changes.md
```
```{toctree}
:hidden:
changesasl.md
```