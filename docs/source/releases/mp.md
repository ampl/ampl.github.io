# AMPL MP Library Changelog

## 20250617
- Option *cvt:unnest*: bits 2 and 4 switch on
  inlining of linear and quadratic subexpressions
  produced during reformulations (by default on).
- Options *cvt:pre:ctx2ineq*, *cvt:pre:ctx2count*
  to control context propagation into conditional
  comparisons #267.


## 20250616
- Multi-objective emulator: added support for 
  objective-specific options via objective suffixes
  beginning with *option_*


## 20250429
- Fix a bug in parsing of quadratic expressions,
  which could wrongly parse products of unequal
  linear expressions, such as (x-3)*(x-z-5).


## 20250424
- Option *alg:sens* return synonym suffixes
  `.down/.up/.current` for objective coefficients
  and `.down/.up` for right-hand sides.
- Improved parsing speed of large sums of quadratic
  and polynomial expressions.
  - Setting option *cvt:qp2passes=0* switches to
    a simpler method, usually slightly slower.
  - Option *cvt:multoutcard* to limit the size of
    out-multiplied QP expressions. Can improve speed
    on large models, but prone to numerical issues.


## 20250308
- Fixed a bug in monotonicity presolve which could
  have led to wrong models using a^x with a<1.
- Reduced memory fragmentation for linear
  and quadratic expressions.
- Option *tech:outlev_mp=1* (implied by *tech:outlev=1*)
  prints initial and transformed model statistics.
- Improved presolve for disequality: more cases when
  no logical disjunction is needed.


## 20250205
- Fixed a bug in model reformulations which could
  cause some constraints to be lost, see issue 248.
- Option *alg:sens=1* now returns suffix `.sensobj` with
  current objective coefficients in the solver model
  (this is the model corresponding to AMPL command `solexpand`.)
- Option *acc:_all* is overridden by individual acceptance
  options, e.g., *acc:or*.
- Substitute AMPL defined variables
  into linear, quadratic, and polynomial expressions
  (option *cvt:dvelim*).
  This can simplify quadratic and polynomial models
  (linear substitutions are already performed by AMPL,
  see AMPL options *linelim* and *substout.)
- *cvt:prod=7* default for LP and convex solvers,
  logicalizing also products of just 2 binary variables.
- More presolve for logical expressions
  (Not, And, Or, Indicator), and new options to control
  some of them: *cvt:pre:ineqresult*, *cvt:pre:ineqrhs*.
- Fix lower bound calculation of the division result.
- [BREAKING] Option acc:pow now affects only expressions x^y
  with both x, y variable; previous meaning of *acc:pow*
  is now with *acc:powconstexp*.
- Option *tech:writemodel:index* to choose the iteration
  when solver model is exported
  in the multi-objective emulator.
- SCIP (and any solver with linear objective
	and non-linear constraints): improve reformulation
	of QP objectives.
- Fix reformulation of non-linear objective expressions
  for the multi-objective case (option *obj:multi*) when
  negative objective weights are used (*obj:multi:weight*).


## 20240724
- Option *acc:_all*
  - Useful to disable all reformulations (*acc:_all=2*),
    or force linearization (*acc:_all=0*).
- Faster input of quadratic expressions.


## 20240617
- *Multi-objective emulator*
  - *obj:multi=2* forces emulation, even if MO natively supported.
	- Fixed a bug in the objective degradation suffixes
    `.objabstol`, `.objreltol`.


## 20240604
- Presolve division by constant, resulting in fewer constraints
- Fix no-solution case in multi-objective emulator


## 20240529
- *Multi-objective emulator*
  - All flat MP solvers support multi-objective mode (*obj:multi=1*),
		either natively, or via emulation.
  - Suffixes `.objpriority`, `.objweight`, `.objabstol`, `.objreltol`.
  - [BREAKING] Default intuitive handling of `.objweight`,
    see option `obj:multi:weight`, even when natively supported.


## 20240429
- *Options `report_times` and `timing`*.
  - Options `timing` and `report_times` now have the same effect:
    setting their value to 1 returns basic timing information, 
    setting it to 2 returns more granular info.


## 20240320
- *SOS constraints*.
  - Fixed handling of SOS2 constraints created by AMPL
    as reformulations of PL expressions (`option
    pl_linearize 1`, default; set to 0 to use the solver's
    native PL functions if supported, or MP linearization.)
  - Disallow repeated weights for SOS constraints
    (suffixes `.sosno`/`.ref`).
- *Reformulation explorer*.
  - Upgraded option *writegraph* exports the reformulation
    graph which can be explored with the script in
    support/modelexplore (WIP).
- *Native handling of POW(x, INT)*.
  - Power expressions with positive integer exponent
    are passed natively to the solvers accepting them,
    vs previously quadratic or linear reformulation.
  - For best performance, global solving capability
    might be needed (e.g., Gurobi: `global=1`.)
- *Option `report_times`*.
- *Unused `acc:` options*.
  - The constraint acceptance options `acc:...`
    for non-handled constraints are ignored
    (previously triggered error.)
- *NLWPY*.
  - Python NL Writer API for MIQP models.
  - Available on PyPI.


## 20240115
- *Solve result codes*.
  - List codes by running (solver) -!
  - [BREAKING] Standardized codes. Major changes:
    - 100-199 (solved?) means solution candidate
      provided, but can be suboptimal/infeasible
    - 300-349 means unbounded problem but
      feasible solution returned
    - 400-449 means limit/interrupt but feasible
  - [BREAKING] *sol:chk:fail* returns code 150 (solved?)
- Improved translation of *SOCP constraints*.
  - Options *cvt:socp*, *cvt:socp2qc*.
- Compact solution check warnings
- Fixed presolve of the power function #226.
- Fixed graceful exit on Ctrl-C from AMPL in Linux.


## 20231103
- Improved translation of logical constraints:
  inlining of nested disjunctions and conjunctions;
  fewer auxiliary binary variables.


## 20231017
- Fixed a bug in NL reader on Windows.


## 20230919
- *mp_options*.
	Receive mp_options from AMPL (for all MP solvers).
  They are parsed before `(solvername)_options`.
- Solution checking: relative tolerance
  *sol:chk:feastolrel*; options *sol:chk:round*, *sol:chk:prec*.


## 20230831
- Solution checking, options *sol:chk:...* (experimental).
- Preprocess And/Or constraints.


## 20230817
- Alternative solutions: solve status equal to that
  of the final solution.
- Fixed a bug causing repeated names for
  auxiliary variables and constraints.
- Option values can be assigned without '='.
- Fixed a bug where equivalent conditional
  comparisons were not unified.


## 20230728
- Option 'tech:writesolution' #218.
- Option 'writeprob' ('tech:writemodel') ASL-compatible.
- Hint when 'writeprob' fails: use 'writesol'.


## 20230726
- Fixed inequalities of integer expressions with
  non-integer constants, see test_int_non_int.mod.
- Backend std feature WRITE_SOLUTION.
- Fixed parsing quoted string options.


## 20230724
- Option [solver_]auxfiles rc; transfers names
	of variables and constraints into the model;
	(solver)_options 'cvt:names=0-3' controls names.


## 20230714
- Print warnings in non-verbose mode too.
- 'barrier' equivalent to 'barrier=1' for integer options.


## 20230621
- Fix quadratic objective with repeated subexpressions.


## 20230616
- Smaller reformulations for conditional comparisons.
- Option *cvt:names* sets whether to read AMPL
  variable names or to provide generic names.


## 20230531
- Cones: recognize (affine_expr) >= y * exp(z/y)
  as exponential cone.
- Cones: recognize xy >= 1 as rotated SOC.
- Wrong solver options are gracefully reported via
  solve_message.


## 20230515
- *Recognize exponential conic constraints*.
  Exponential cones are recognized and passed to the
  solver, if supported.
  

## 20230424
- *Pass variable names* if read from a `col` file with the 
  same name of the `nl` file being read.
- *Fixed #203*: starting solution is now not passed to the 
  solver if empty.
  

## 20230321
- *Recognize second-order cones*
  Recognize SOCP constraints from algebra and pass them
  natively, or transform to quadratics.


## 20230207
- *Handle boolean constants* in ProblemFlattener.


## 20221228
- *More to #163*: ignore SOS with zero weights.


## 20221222
- *Fixed #195*: case-insensitive option synonyms.

- *Fixed #194*
   Report correct objno for feasibility problems in .sol file,
   so that AMPL can print "Objective = find feasible solution".


## 20221211
- *==> else*
   Implemented implication with 'else': *constr1* ==> *constr2* [else *constr3*]   

- *PLApproxRelTol, PLApproxDomain*
   Parameters to control piecewise-linear approximation.
   cvt:plapprox:reltol default value changed from 1e-5 to 0.01.

## 20221012
- *Piecewise-linear approximation of quadratics*
    Automatic for linear solvers.
    For convex QP solvers, set the following options:
    cvt:quadobj=0 cvt:quadcon=0 to linearize nonconvex objective(s)
    and/or constraints.
    Recognizing x^2 for stronger univariate approximation.

## 20220928
- *Piecewise-linear approximation of univariate nonlinear functions*
    Approximation of exp, a^x, x^a, log, log10, trigonometric and hyperbolic
    functions.

- *Default value of big-M*
    For linearization of logical constraints on variables without finite bounds,
    option cvt:mip:bigM can provide a default big-M bound.
    

## 20220725
- *Solution file export* 
    On Windows now creates files with LF only to avoid issues when exporting
    suffixes to AMPL.

    Multiple solutions export file format amended.


## 20220720
- *Propagating suffixes via expression trees into flat constraints*
    Partially implemented #184. x-gurobi accepts options
    'funcpieces...' and corresponding suffixes which are passed into
    GRBaddgenconstrExp etc.

    Subexpressions: note that if a subexpression is contained in several
    constraints, for contradicting suffix values the maximum is taken.

- *Option 'cvt:writegraph'*
   Exporting the flattening / conversion graph in JSON Lines format (WIP).


## 20220617
- *PowConstraint is reduced to quadratics in some cases*
    For constant non-negative integer exponent and base variables
    with negative lower bound, PowConstraint
    is reduced to quadratics (possibly with auxiliary variables).
    Reason: Gurobi's GRBaddgenconstrPow
    not accepting negative bases.

- *Context for algebraic constraints*
    Context is now propagated for algebraic constraints.
    For example, 3x + max(y, z) <= 6 will result in 3 linear
    constraints. (Earlier this was done for logical constraints
    and objectives).


## 20220526
- *Special ordered sets*
    Fixed: SOS are now recognized even if the suffix '.ref' 
    value is integer


## 20220511
- *Complementarity constraints: also quadratics*
    Complementarity constraints now handle quadratics.

- *Branch develop is used for new code*
    The active development branch is now *develop*.

- *Convert quadratic range constraints to QuadCon(LE/EQ/GE)*
    Gurobi and COPT do not support quadratic range constraints.
    (Gurobi's linear ranges are not feature-complete).
    Conversion of linear range constraints into one-side rhs
    constraints has been generalized for any algebraic ones.


## 20220408
- *Complementarity constraints: 1st go*
    Conversion to MIP of complementarity constraints
    (no quadratics but functional subexpressions ok).

- *DivConstraint and DivConverter_MIP*
    ModelFlattener now receives the Div expression
    and MIPFlatConverter handles it via quadratics.

- *Fix NL input variable order*

- *Reduce default strict comparison tolerance*
    Change *cvt:mip:eps* default value to 1e-4.

- *Build on MacOS 12.3, in particular on Apple M1*
    Fixed linking on MacOS 12.3 and FindCPLEX.cmake.
    For Apple M1, manually set -DCMAKE_OSX_ARCHITECTURES="x86_64"
    in CMake when building with CPLEX 22.1 because
    it contains only Intel libraries.

- *Expression maps*
    FlatConverter eliminates subexpressions of all types.
    A subexpression means here a duplicate expression, such as
    abs(x+2) occurring several times in the model (here x+2
    is a nested subexpression).

- *AMPLS C API*
    C API allowing access to underlying solver API.
    Replaces the previous Solver C API (solver-c.cc).
    Toy driver `gurobi_ampls` exemplifies API usage.


## 20220216
- *Improved warnings (#161, #163)*:
    In verbose mode, FlatConverter / Backend print warning summary
    before and after solving
    
- *Fixed solver option parsing in Windows (#160)*

- *Reworked Backend / ModelAPI class hierarchy (#162)*:
    In particular, also generalized old MP hierarchy
    (Solver / ProblemBuilder / AppSolutionHandler / SolverNLHandler)

- *Allowing SOS constraints with repeated weights (#163)*:
    Although Gurobi states SOS weights should be unique, it accepts them repeated.
    This happens when AMPL linearizes a PL function with redundant (repeated) slopes.
    It seems better to use PL functions natively (*option pl_linearize 0;*).
