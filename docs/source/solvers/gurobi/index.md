(gurobi)=

# Gurobi

Gurobi is a powerful commercial suite of optimization products, which include simplex, parallel and nonlinear barrier, and primal-dual hybrid gradient (PDHG) solvers to handle linear programming (LP), quadratic programming (QP), and nonlinear programming (NLP);
also quadratically constrained (QCP, SOCP) and the mixed-integer variations thereof (MILP, MIQP, MIQCP, MISOCP, MINLP).
The (MI)NLP capability is provided via nonlinear expressions (formulas).
The [MP Library](https://mp.ampl.com/) used by the AMPL Gurobi driver supports automatic reformulation for many expression types; the modeling guide can be
found [here](https://mp.ampl.com/model-guide.html).

[Product Page](https://ampl.com/products/solvers/solvers-we-sell/gurobi/)
| [Modeling guide](https://mp.ampl.com/model-guide.html)
| [Features](#features)
| [Options](#solver-options)
| [Changes](changes.md)

[Download Gurobi](https://ampl.com/download/gurobi)
| [Start a Gurobi Trial Now!](https://ampl.com/trial/gurobi)

Our enhanced Gurobi driver is now the default. The new driver provides significantly extended modeling support for logical and nonlinear operators natively through Gurobi’s built-in nonlinear and “general constraints” and through linearizations performed by the [MP Library](https://mp.ampl.com/). There are two binaries in this package: `gurobi` [[options](options.md)] is the new version, `gurobiasl` [[options](gurobiasl)] is the legacy version. If you are upgrading an existing installation and encounter any issues with the new version please report them to [support@ampl.com](mailto:support@ampl.com).

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: Python
   
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
            ampl.solve(solver="gurobi",
                       gurobi_options="option1=value1 option2=value2")

        Learn more about what we have to offer to implement and deploy `Optimization in Python <https://ampl.com/python/>`_.

   .. tab-item:: Other APIs

        `AMPL APIs <https://ampl.com/apis/>`_ are interfaces that allow developers to access the features of the AMPL interpreter from within a programming language. We have APIs available for:

        - `Python <https://ampl.com/api/latest/python>`_
        - `R <https://ampl.com/api/latest/R>`_
        - `C++ <https://ampl.com/api/latest/cpp>`_
        - `C#/.NET <https://ampl.com/api/latest/dotnet>`_
        - `Java <https://ampl.com/api/latest/java>`_
        - `MATLAB <https://ampl.com/api/latest/matlab>`_

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver gurobi;                  # Select solver
            ampl: option gurobi_options 'option1=value1 option2=value2';
            ampl: solve;
```

## At a glance

### Resources

* [Modeling guide](https://mp.ampl.com/model-guide.html)
* [Features](#features)
* [Solver options](#solver-options)
* [Solve result codes](#retrieve-solutions)
* [Driver sources](https://github.com/ampl/mp/tree/develop/solvers/gurobi)
* [Using with callbacks](https://ampls.ampl.com/)

### Features

* Problem types: 

  * LP, QP, QCP, SOCP, NLP
  * MILP, MIQP, MIQCP, MISOCP
  * MINLP
  * <details>
    <summary>General constraints and nonlinear expressions</summary>  

    * log / exp / logistic
    * min / max
    * and / or
    * abs
    * sin / cos / tan / tanh
    * pow / signpow
    </details>

* Algorithms:

  * Simplex method, parallel barrier, PDHG ([options](#solver-options) `alg:method`, `alg:pdhggpu`)
  * Nonlinear barrier (option `alg:optimalitytarget=1`)
  * Branch-and-Bound, Branch-and-Cut (mainly `mip:` and `cut:` options)
    
* [Important features](https://mp.ampl.com/features-guide.html#important-features)

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

Many solver parameters can be changed directly from AMPL, by specifying them as a space-separated string in the [AMPL option](https://dev.ampl.com/ampl/reference/options.html) `gurobi_options`, or `mp_options`. 
A list of all supported solver options is available [here](options.md) or can be obtained by executing the solver driver with the `-=` command line parameter:

```{eval-rst}

.. tab-set::

   .. tab-item:: Python
   
        .. code-block:: python

            import os
            exit_code = os.system("gurobi -=")

   .. tab-item:: Other APIs

        `AMPL APIs <https://ampl.com/apis/>`_ are interfaces that allow developers to access the features of the AMPL interpreter from within a programming language. We have APIs available for:

        - `Python <https://ampl.com/api/latest/python>`_
        - `R <https://ampl.com/api/latest/R>`_
        - `C++ <https://ampl.com/api/latest/cpp>`_
        - `C#/.NET <https://ampl.com/api/latest/dotnet>`_
        - `Java <https://ampl.com/api/latest/java>`_
        - `MATLAB <https://ampl.com/api/latest/matlab>`_

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: shell "gurobi -=";

   .. tab-item:: Shell

        .. code-block:: bash

            $ gurobi -=
```


Solver options can have multiple aliases, to accomodate for different user types. 
The main nomenclature is given first in the `-=` output, then followed by aliases in brackets,
 see for example the listing for `lim:iter`:

```
lim:iter (iterlim, iterlimit)
      Iteration limit (default: no limit).
```

The main nomenclature contains a prefix (`lim:` in this case) to help categorize and find the 
options relevant to a context. To list only the options with a specific prefix (`lim:` for this example), 
run:

```
gurobi -=lim:
```

More details on solver options: [Features guide](https://mp.ampl.com/features-guide.html).


## Specify solver options and solve

After formulating the model in AMPL, execute the following to select `gurobi` as the solver and pass the two options:
`return_mipgap=3` and `outlev=1`.


```{eval-rst}

.. tab-set::

   .. tab-item:: Python
   
        .. code-block:: python

            ampl.option["show_stats"] = 2
            ampl.solve(solver="gurobi",
                mp_options="return_mipgap=3 outlev=1",     # or: gurobi_options
                verbose=True)

   .. tab-item:: Other APIs

        `AMPL APIs <https://ampl.com/apis/>`_ are interfaces that allow developers to access the features of the AMPL interpreter from within a programming language. We have APIs available for:

        - `Python <https://ampl.com/api/latest/python>`_
        - `R <https://ampl.com/api/latest/R>`_
        - `C++ <https://ampl.com/api/latest/cpp>`_
        - `C#/.NET <https://ampl.com/api/latest/dotnet>`_
        - `Java <https://ampl.com/api/latest/java>`_
        - `MATLAB <https://ampl.com/api/latest/matlab>`_

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver gurobi;                    # Select solver
            ampl: option mp_options 'return_mipgap=3 outlev=1';
            ampl: solve [>output.log];                     # Solve [redirect output]
            
   .. tab-item:: Shell

        .. code-block:: bash

            $ [auxfiles=rc] ampl -obmodel snapshot.run     # Produce an NL file
                                                           # [with name files]
            $ mp_options='lim:time=100' gurobi model       # Version 1
            $ gurobi_options='kappa_exact=1' gurobi model  # Version 2
            $ gurobi model lim:time=100 wantsol=7          # Version 3
```


## Retrieve solutions

The outcome of the last optimization is stored in the AMPL parameter `solve_result_num` and the related message in
`solve_result`.

```{eval-rst}

.. tab-set::

   .. tab-item:: Python
   
        .. code-block:: python
        
            print(ampl.solve_result, ampl.solve_result_num)
            ROI_Values = ampl.var['ROI_Level'].to_pandas()
            
            ampl.param["a"] = ampl2.var["x"].get_values()
            ampl.eval(r" x >(“obj” & n & “.out”) ;")       #save solution in a .out file

   .. tab-item:: Other APIs

        `AMPL APIs <https://ampl.com/apis/>`_ are interfaces that allow developers to access the features of the AMPL interpreter from within a programming language. We have APIs available for:

        - `Python <https://ampl.com/api/latest/python>`_
        - `R <https://ampl.com/api/latest/R>`_
        - `C++ <https://ampl.com/api/latest/cpp>`_
        - `C#/.NET <https://ampl.com/api/latest/dotnet>`_
        - `Java <https://ampl.com/api/latest/java>`_
        - `MATLAB <https://ampl.com/api/latest/matlab>`_

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: display solve_result_num, solve_result;
            ampl: display _varname, _var, _conname, _con.slack;
            ampl: display _logconname, _logcon.value;      # Logical constraints
            ampl: display _cconname, _ccon.slack;          # Complementarities
            

   .. tab-item:: Shell

        .. code-block:: bash

            $ gurobi model lim:time=100 wantsol=6          # Print solution
            $ gurobi model timing=2 wantsol=1              # Save .sol file
                                                           # to be explored in AMPL
```


Gurobi solve result codes can be obtained by running `gurobi -!` or `ampl: shell "gurobi -!";`:
```
Solve result table for Gurobi 13.0.1
	  0- 99	solved: optimal for an optimization problem,
		feasible for a satisfaction problem 
	100-199	solved? solution candidate returned but error likely 
	    120	locally optimal solution
	    150	solved? MP solution check failed (option sol:chk:fail) 
	200-299	infeasible 
	    220	locally infeasible solution
	300-349	unbounded, feasible solution returned 
	350-399	unbounded, no feasible solution returned 
	400-449	limit, feasible: stopped, e.g., on iterations or Ctrl-C 
	    401	interrupted, feasible solution
	    402	time limit, feasible solution
	    403	iteration limit, feasible solution
	    404	node limit, feasible solution
	    405	bestobjstop or bestbndstop reached, feasible solution
	    408	solution limit
	    409	work limit, feasible solution
	    410	soft memory limit, feasible solution
	450-469	limit, problem is either infeasible or unbounded.
		Disable dual reductions or run IIS finder for definitive answer.
	470-499	limit, no solution returned 
	    471	interrupted, without a feasible solution
	    472	time limit, without a feasible solution
	    473	iteration limit, without a feasible soluton
	    474	node limit, without a feasible soluton
	    475	objective cutoff
	    477	bestbndstop reached, without a feasible solution
	    479	work limit, without a feasible solution
	    480	soft memory limit, without a feasible solution
	500-999	failure, no solution returned 
	    550	failure: numeric issue, no feasible solution
	    601	Could not talk to Gurobi Instant Cloud or Gurobi Server.
	    602	Job rejected by Gurobi Instant Cloud or Gurobi Server.
	    603	No license for specified Gurobi Instant Cloud or Gurobi Server.
	    604	Surprise failure while starting the cloud/server environment.
	    605	Bad value for cloudid or cloudkey, or Gurobi Cloud out of reach.
```

For general information, see [MP result codes guide](https://mp.ampl.com/features-guide.html#solve-result-codes).

## Handle infeasibility

### Irreducible inconsistent set (IIS)

When a model is infeasible, one useful information kind is the IIS, which are subsets of constraints that are
incompatible. See the details [here](https://mp.ampl.com/features-guide.html#irreducible-inconsistent-set-iis).


### Feasibility relaxation

Another approach to tackle infeasibilities is the feasibility relaxation to find a solution which only penalizes infeasibilities. 
See the details  [here](https://mp.ampl.com/features-guide.html#feasibility-relaxation).


## Gurobi compute server and Gurobi cloud

Gurobi supports solving your model on other machines in two alternative ways:
* [Compute server](https://www.gurobi.com/products/gurobi-compute-server/) - where a computer (or a cluster) can be configured to the specific task of solving models via Gurobi
* [Gurobi cloud](https://www.gurobi.com/products/gurobi-instant-cloud/) - where the compute server is by Gurobi itself 

To use a compute server, the option `tech:server` must be set, together with appropriate values for the `tech:server_*` options.
For Gurobi instant cloud, the options `tech:cloudid` and `tech:cloudkey` must be set, and optionally the other options `tech:cloud*`, for example:

```ampl

# Solve with compute server
option gurobi_options "tech:server=192.168.1.55";
solve;

# Solve with Gurobi instant cloud
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
