(what_is_new)=
# What's new?

## New book: Hands-On Mathematical Optimization with AMPL in Python

```{eval-rst}
.. image:: https://portal.ampl.com/dl/ads/mo_book_big.png
  :alt: Hands-On Mathematical Optimization with AMPL in Python
  :target: https://ampl.com/mo-book/
```

## AMPL Community Edition

**Free, full-powered AMPL for personal, academic, or commercial prototyping purposes using [AMPL APIs](ampl/apis.rst)**.

-   License never expires
-   Unlimited variables & constraints

Get your free license at: **<https://ampl.com/ce>**

**Solvers permanently available:**

-   Open-source solvers: **HiGHS, CBC, Couenne, Ipopt, Bonmin.**
-   [NEOS solvers](https://ampl.com/products/ampl/run-ampl-on-neos/) (including commercial solvers), directly in AMPL through the [kestrel interface](https://dev.ampl.com/solvers/kestrel.html).

**Commercial solver trials readily available (30 days each):**

-   Linear: [Gurobi](https://ampl.com/products/solvers/solvers-we-sell/gurobi/), [CPLEX](https://ampl.com/products/solvers/solvers-we-sell/cplex/), [Xpress](https://ampl.com/products/solvers/solvers-we-sell/xpress/), [COPT](https://ampl.com/products/solvers/solvers-we-sell/copt/)
-   Nonlinear: [Artleys Knitro](https://ampl.com/products/solvers/solvers-we-sell/knitro/), [CONOPT](https://ampl.com/products/solvers/solvers-we-sell/conopt/), [LOQO](https://ampl.com/products/solvers/solvers-we-sell/loqo/), [MINOS](https://ampl.com/products/solvers/solvers-we-sell/minos/), [SNOPT](https://ampl.com/products/solvers/solvers-we-sell/snopt/)
-   Global: [BARON](https://ampl.com/products/solvers/solvers-we-sell/baron/), [LGO](https://ampl.com/products/solvers/solvers-we-sell/lgo/), [LINDO Global](https://ampl.com/products/solvers/solvers-we-sell/lindoglobal/), [OCTERACT](https://ampl.com/products/solvers/solvers-we-sell/octeract/)

**APIs included:**

[![](https://portal.ampl.com/static/img/apis/PythonLogo.svg)](https://amplpy.ampl.com/) [![](https://portal.ampl.com/static/img/apis/RLogo.svg)](https://rampl.ampl.com/) [![](https://portal.ampl.com/static/img/apis/CppLogo.svg)](https://ampl.com/api/latest/cpp/) [![](https://portal.ampl.com/static/img/apis/CSharpLogo.svg)](https://ampl.com/api/latest/dotnet/) [![](https://portal.ampl.com/static/img/apis/MatlabLogo.svg)](https://ampl.com/api/latest/matlab/) [![](https://portal.ampl.com/static/img/apis/JavaLogo.svg)](https://ampl.com/api/latest/java/)

**What else is included?**

-   [AMPL Model Colaboratory](https://ampl.com/colab/) powered by our [Python API](https://amplpy.ampl.com/)!
-   [Enhanced solver interfaces (e.g., Gurobi, COPT, XPRESS, HiGHS)](https://mp.ampl.com/model-guide.html)
-   [Data Connectors (e.g., .xlsx, .csv, ODBC)](https://ampl.com/products/ampl/data-connectors/) and [Function Libraries (e.g., GSL)](https://gsl.ampl.com/)
-   [It works with Docker Containers and Cloud Functions (e.g., AWS Lambda, Azure Functions, etc.)](ampl_docker)
-   Since it is a [cloud license](cloud_licenses) it can be used on continuous integration and continuous delivery (CI/CD) platforms.

## Using AMPL in Google Colab, Kaggle, and similar platforms

We have a set of Jupyter Notebooks available on our [Model Colaboratory](https://ampl.com/colab/).

You can use our template (<https://ampl.com/colab/tags/template.html>)
as a starting point. Our cloud licenses, including AMPL CE licenses, work on all cloud platforms.

## Snapshot feature (save and restore AMPL sessions)

In your AMPL bundle you should find `x-ampl`, the development version of AMPL where experimental features are enabled. One of such features is the snapshot command which allows saving the AMPL session in such a way that you can restore the state of AMPL using it.

### Example using it with amplpy

You need to be using at least amplpy 0.12.0 (you can install it with `python -m pip install amplpy>=0.12.0`).

You can then use [`AMPL.snapshot`](https://amplpy.ampl.com/en/latest/classes/ampl.html#amplpy.AMPL.snapshot) to retrieve a session snapshot as a string. The string returned is a compact representation of the AMPL state (model declaration, data, solution loaded, options, etc.)
```python
ampl = AMPL()
...
snapshot = ampl.snapshot()
print(snapshot)
```
This string can then be passed to another AMPL object using `AMPL.eval`. The following example produces the output below:
```python
from amplpy import AMPL, Environment

print('First object:')
ampl = AMPL()
ampl.read('diet.mod')
ampl.read_data('diet.dat')
ampl.option['solver'] = 'gurobi'
ampl.solve()
ampl.snapshot("snapshot.run")  # save the session snapshot to a file

print('Second object:')
ampl2 = AMPL()
ampl2.read("snapshot.run")  # load the snapshot from the snapshot.run file 
ampl2.display('Buy')

print('Third object:')
ampl3 = AMPL()
snapshot = ampl2.snapshot()  # return a string with the session snapshot
ampl3.eval(snapshot)  # load the snapshot from the string
ampl3.display('_VARS;')
ampl3.eval('option solver;')
```


```
First object:
Gurobi 11.0.0: optimal solution; objective 88.2
1 simplex iterations
Second object:
Buy [*] :=
BEEF   0
 CHK   0
FISH   0
 HAM   0
 MCH  46.6667
 MTL   0
 SPG   0
 TUR   0
;

Third object:
set _VARS := Buy;

option solver gurobi;
```

One thing that may also be useful: In the example, there is the line `ampl.snapshot("snapshot.run")` that writes the snapshot to a file called `snapshot.run`. This file can be loaded into AMPL (e.g., for debugging) as follows:
```
$ ampl
ampl: include "snapshot.run";
ampl: display Buy;
Buy [*] :=
BEEF   0
 CHK   0
FISH   0
 HAM   0
 MCH  46.6667
 MTL   0
 SPG   0
 TUR   0
;
```
The snapshot feature is not finished and it is still being perfected. If you encounter any issues, please let us know.

## Enhanced solver drivers: gurobi, copt, highs

We have released `gurobi`, the enhanced
[AMPL-Gurobi](https://ampl.com/products/solvers/solvers-we-sell/gurobi/)
interface, `copt`, an interface to [Cardinal Optimizer](https://www.shanshu.ai/copt),
and `highs`, an interface to [HiGHS](https://highs.dev/).
They are included in the [AMPL distribution bundle](https://portal.ampl.com).

The drivers have the following features:

- Full support of logical expressions and constraints, as described in the AMPL page on Logic and Constraint Programming Extensions.
- Algebraic expressions beyond linear and quadratic.
- Choice between conversions in the driver vs. native solver support.

[[Modeling Guide](https://mp.ampl.com/model-guide.html)] [[gurobi options](solvers/gurobi/options.md)] [[copt options](solvers/copt/options.md)]  [[highs options](solvers/highs/options.md)]

## New AMPL-solver interface library

We're rolling out a new AMPL-solver interface library that significantly
expands the range of model expressions that can be used with popular
solvers. Initially, the new library is being used to implement AMPL
interfaces to two notable new solvers, [COPT](https://ampl.com/products/solvers/solvers-we-sell/copt/) and [HiGHS](https://ampl.com/products/solvers/open-source/), and to provide
greatly enhanced support for [Gurobi's](https://ampl.com/products/solvers/solvers-we-sell/gurobi/) generalized constraints. Extensions to
other solvers will be released soon.

### NEW SOLVER INTERFACE

Modeling languages aim to let you describe
optimization models to a computer in much the same way that you describe
models to other people. The newly extended ["MP" interface](https://github.com/ampl/mp)
brings AMPL closer to this goal, by allowing expanded use of a variety of convenient
expressions in objectives and constraints. Notable examples include:

- Conditional operators: `if-then-else`; `==>`, `<==`, `<==>`
- Logical operators: `or`, `and`, `not`; `exists`, `forall`
- Piecewise linear functions: `abs`; `min`, `max`; `<<breakpoints;slopes>>`
- Counting operators: `count`; `atmost`, `atleast`, `exactly`; `numberof`
- Comparison operators: `>`, `<`, `!=`; `alldiff`

These operators can be applied to general forms of AMPL expressions, and
thus can be used together in objective and constraint specifications. The
new interface also helps solvers to accept nonlinear operators (`*`, `/`, `^`) in
a broader variety of circumstances.

A public [MP Library repository](https://github.com/ampl/mp) on GitHub links to a [modeling guide](https://mp.ampl.com/model-guide.html) and
documentation of the source code. See also the slides from our presentation
of the new interface at this summer's [EURO and ICCOPT conferences](https://ampl.com/MEETINGS/TALKS/2022_07_Bethlehem_Fourer.pdf), or attend
updated presentations at the [INFORMS Annual Meeting, October 15-19](https://ampl.com/resources/informs-annual-2022/).

### NEW SOLVERS

The first implementations using the MP interface library are
now available in our regular distributions through the [AMPL Portal](https://portal.ampl.com/).

An entirely new MP-based interface greatly expands the variety of AMPL
expressions that can be used with the [Gurobi](https://ampl.com/products/solvers/solvers-we-sell/gurobi/) solver. The new implementation uses the solver's native "generalized
constraints" where possible, but can be switched to use alternative
transformations built into MP. Common univariate nonlinear functions (`exp`,
`log`; `sin`, `cos`, `tan`) are also supported, using Gurobi's native
piecewise-linear approximation facilities.

Two relatively new linear/quadratic MIP solvers -- [COPT](https://ampl.com/products/solvers/solvers-we-sell/copt/) and [HiGHS](https://ampl.com/products/solvers/open-source/) -- are now
also supported by AMPL, exclusively through the MP interface. Both are in
active development and appear in recent benchmark listings. COPT, a product
of Cardinal Operations, has joined the lineup of commercial solvers that we
distribute. HiGHS, a free open-source solver, has evolved from a project at
the University of Edinburgh. They appear as "copt" and "highs" in AMPL
distributions.

Currently supported MIP solvers such as [Xpress](https://ampl.com/products/solvers/solvers-we-sell/xpress/) and [CPLEX](https://ampl.com/products/solvers/solvers-we-sell/cplex/) are also planned to
have versions with the new interface. Also we will soon be distributing the
*MOSEK* solver with an MP interface.

## Using remote solvers from NEOS with gokestrel

To simplify the work of comparing and testing solvers, we have made AMPL and solver resources available online in collaboration with the [NEOS Server](https://www.neos-server.org/) project, under the auspices of the [Wisconsin Institutes for Discovery](https://www.discovery.wisc.edu/) at the University of Wisconsin, Madison. 

Thanks to [gokestrel](https://github.com/ampl/gokestrel), our new Kestrel driver, instead of specifying a solver installed on your computer or local network, you invoke Kestrel, a "client" program that sends your problem to a solver running on one of the NEOS Server's remote computers. The results from the NEOS Server are eventually returned through Kestrel to AMPL, where you can view and manipulate them locally in the usual way.

Important options:
- `email`: your e-mail address (it is required by NEOS).
- `kestrel_options`: allows you to specify among other things, the solver to use

As an example, here is how you might invoke Kestrel from a local AMPL session, using CPLEX as your remote solver:

```
ampl: model diet.mod;
ampl: data diet.dat;
ampl: option solver kestrel;
ampl: option email "***@***.***";
ampl: option kestrel_options "solver=cplex";
ampl: option cplex_options "display=2";
ampl: solve;
Connecting to: neos-server.org:3333
Job XXXX submitted to NEOS, password='xxxx'
Check the following URL for progress report:
https://neos-server.org/neos/cgi-bin/nph-neos-solver.cgi?admin=results&jobnumber=XXXX&pass=xxxx
Job XXXX dispatched
password: xxxx
---------- Begin Solver Output -----------
Condor submit: 'neos.submit'
Condor submit: 'watchdog.submit'
Job submitted to NEOS HTCondor pool.
CPLEX 20.1.0.0: optimal solution; objective 88.2
1 dual simplex iterations (0 in phase I)
```
