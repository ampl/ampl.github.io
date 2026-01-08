
# XPRESS Options

```ampl
ampl: option solver xpress; # change the solver
ampl: option xpress_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

Solver options obtained with `$ xpress -=`.

```
XPRESS Optimizer Options for AMPL
--------------------------------------------

To set these options, assign a string specifying their values to the AMPL
option "xpress_options". For example:

   ampl: option xpress_options 'mipgap=1e-6';

'' Options:

acc:_all
      Solver acceptance level for all constraints and expressions. Value
      meaning: as described in the specific acc:... options.

      Can be useful to disable all reformulations (acc:_all=2), or force
      linearization (acc:_all=0.)

acc:_expr
      Solver acceptance level for all expressions, default 1:

      0 - Not accepted, all expressions will be treated as flat constraints,
          or redefined
      1 - Accepted. See the individual acc:... options

acc:abs
      Solver acceptance level for 'AbsConstraint' as either constraint or
      expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted as constraint but automatic redefinition will be used
          where possible
      2 - Accepted as constraint natively and preferred
      3 - Accepted as expression but automatic redefinition will be used
          where possible
      4 - Accepted as expression natively and preferred

acc:acos
      Solver acceptance level for 'AcosConstraint' as either constraint or
      expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted as constraint but automatic redefinition will be used
          where possible
      2 - Accepted as constraint natively and preferred
      3 - Accepted as expression but automatic redefinition will be used
          where possible
      4 - Accepted as expression natively and preferred

acc:acosh
      Solver acceptance level for 'AcoshConstraint' as flat constraint,
      default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:and (acc:forall)
      Solver acceptance level for 'AndConstraint' as flat constraint, default
      2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:asin
      Solver acceptance level for 'AsinConstraint' as either constraint or
      expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted as constraint but automatic redefinition will be used
          where possible
      2 - Accepted as constraint natively and preferred
      3 - Accepted as expression but automatic redefinition will be used
          where possible
      4 - Accepted as expression natively and preferred

acc:asinh
      Solver acceptance level for 'AsinhConstraint' as flat constraint,
      default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:atan
      Solver acceptance level for 'AtanConstraint' as either constraint or
      expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted as constraint but automatic redefinition will be used
          where possible
      2 - Accepted as constraint natively and preferred
      3 - Accepted as expression but automatic redefinition will be used
          where possible
      4 - Accepted as expression natively and preferred

acc:atanh
      Solver acceptance level for 'AtanhConstraint' as flat constraint,
      default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:cos
      Solver acceptance level for 'CosConstraint' as either constraint or
      expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted as constraint but automatic redefinition will be used
          where possible
      2 - Accepted as constraint natively and preferred
      3 - Accepted as expression but automatic redefinition will be used
          where possible
      4 - Accepted as expression natively and preferred

acc:cosh
      Solver acceptance level for 'CoshConstraint' as flat constraint, default
      2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:div
      Solver acceptance level for 'DivConstraint' as either constraint or
      expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted as constraint but automatic redefinition will be used
          where possible
      2 - Accepted as constraint natively and preferred
      3 - Accepted as expression but automatic redefinition will be used
          where possible
      4 - Accepted as expression natively and preferred

acc:exp
      Solver acceptance level for 'ExpConstraint' as either constraint or
      expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted as constraint but automatic redefinition will be used
          where possible
      2 - Accepted as constraint natively and preferred
      3 - Accepted as expression but automatic redefinition will be used
          where possible
      4 - Accepted as expression natively and preferred

acc:expa (acc:expA)
      Solver acceptance level for 'ExpAConstraint' as flat constraint, default
      2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:indeq (acc:indlineq)
      Solver acceptance level for 'IndicatorConstraintLinEQ' as flat
      constraint, default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:indge (acc:indlinge)
      Solver acceptance level for 'IndicatorConstraintLinGE' as flat
      constraint, default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:indle (acc:indlinle)
      Solver acceptance level for 'IndicatorConstraintLinLE' as flat
      constraint, default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:lineq
      Solver acceptance level for 'LinConEQ' as flat constraint, default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:linfunccon
      Solver acceptance level for 'LinearFunctionalConstraint' as expression,
      default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:linge
      Solver acceptance level for 'LinConGE' as flat constraint, default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:linle
      Solver acceptance level for 'LinConLE' as flat constraint, default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:log
      Solver acceptance level for 'LogConstraint' as either constraint or
      expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted as constraint but automatic redefinition will be used
          where possible
      2 - Accepted as constraint natively and preferred
      3 - Accepted as expression but automatic redefinition will be used
          where possible
      4 - Accepted as expression natively and preferred

acc:loga (acc:logA)
      Solver acceptance level for 'LogAConstraint' as either constraint or
      expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted as constraint but automatic redefinition will be used
          where possible
      2 - Accepted as constraint natively and preferred
      3 - Accepted as expression but automatic redefinition will be used
          where possible
      4 - Accepted as expression natively and preferred

acc:max
      Solver acceptance level for 'MaxConstraint' as either constraint or
      expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted as constraint but automatic redefinition will be used
          where possible
      2 - Accepted as constraint natively and preferred
      3 - Accepted as expression but automatic redefinition will be used
          where possible
      4 - Accepted as expression natively and preferred

acc:min
      Solver acceptance level for 'MinConstraint' as either constraint or
      expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted as constraint but automatic redefinition will be used
          where possible
      2 - Accepted as constraint natively and preferred
      3 - Accepted as expression but automatic redefinition will be used
          where possible
      4 - Accepted as expression natively and preferred

acc:nlassigneq
      Solver acceptance level for 'NLAssignEQ' as flat constraint, default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:nlassignge
      Solver acceptance level for 'NLAssignGE' as flat constraint, default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:nlassignle
      Solver acceptance level for 'NLAssignLE' as flat constraint, default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:nlcon (acc:nlalgcon)
      Solver acceptance level for 'NLConstraint' as flat constraint, default
      2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:or (acc:exists)
      Solver acceptance level for 'OrConstraint' as flat constraint, default
      2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:pl (acc:pwl, acc:piecewise)
      Solver acceptance level for 'PLConstraint' as flat constraint, default
      2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:powconstexp
      Solver acceptance level for 'PowConstExpConstraint' as either constraint
      or expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted as constraint but automatic redefinition will be used
          where possible
      2 - Accepted as constraint natively and preferred
      3 - Accepted as expression but automatic redefinition will be used
          where possible
      4 - Accepted as expression natively and preferred

acc:quadeq
      Solver acceptance level for 'QuadConEQ' as flat constraint, default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:quadfunccon
      Solver acceptance level for 'QuadraticFunctionalConstraint' as
      expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:quadge
      Solver acceptance level for 'QuadConGE' as flat constraint, default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:quadle
      Solver acceptance level for 'QuadConLE' as flat constraint, default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:sin
      Solver acceptance level for 'SinConstraint' as either constraint or
      expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted as constraint but automatic redefinition will be used
          where possible
      2 - Accepted as constraint natively and preferred
      3 - Accepted as expression but automatic redefinition will be used
          where possible
      4 - Accepted as expression natively and preferred

acc:sinh
      Solver acceptance level for 'SinhConstraint' as flat constraint, default
      2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:sos1
      Solver acceptance level for 'SOS1Constraint' as flat constraint, default
      2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:sos2
      Solver acceptance level for 'SOS2Constraint' as flat constraint, default
      2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:tan
      Solver acceptance level for 'TanConstraint' as either constraint or
      expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted as constraint but automatic redefinition will be used
          where possible
      2 - Accepted as constraint natively and preferred
      3 - Accepted as expression but automatic redefinition will be used
          where possible
      4 - Accepted as expression natively and preferred

acc:tanh
      Solver acceptance level for 'TanhConstraint' as flat constraint, default
      2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

alg:addcutoff (addcutoff, mipaddcutoff, mip:xprs_mipaddcutoff, XPRS_MIPADDCUTOFF)
      Branch and Bound: The amount to add to the objective function of the
      best integer solution found to give the new CURRMIPCUTOFF. Once an
      integer solution has been found whose objective function is equal to or
      better than CURRMIPCUTOFF, improvements on this value may not be
      interesting unless they are better by at least a certain amount. If
      MIPADDCUTOFF is nonzero, it will be added to CURRMIPCUTOFF each time an
      integer solution is found which is better than this new value. This cuts
      off sections of the tree whose solutions would not represent substantial
      improvements in the objective function, saving processor time. The
      control MIPABSSTOP provides a similar function but works in a different
      way.

      Default: -1.0E-05

alg:barrier (barrier)
      Solve (MIP node) LPs by barrier method.

alg:basis (basis)
      Whether to use and/or return a basis for LP models (variable/constraint
      suffixes .(s)status):

      0 - No
      1 - Use incoming basis (if provided)
      2 - Return final basis
      3 - Both (1 + 2 = default)

      See alg:start for interaction with the LP warmstart.

      See also mip:basis and qcp:dual (for some solvers).

alg:clamping (clamping, sol:xprs_clamping, XPRS_CLAMPING)
      This bit-vector control (see Section Bit-vector controls) allows for the
      adjustment of returned solution values such that they are always within
      bounds.

      Values (default: 0):

      * (-1) Determined automatically.

      * (0) Adjust primal solution to always be within primal bounds. Slacks
        if provided will be adjusted accordingly.

      * (1) Adjust primal slack values to always be within constraint bounds.

      * (2) Adjust dual solution to always be within the dual bounds implied
        by the slacks. Reduced costs, if provided, will be adjusted
        accordingly.

      * (3) Adjust reduced costs to always be within dual bounds implied by
        the primal solution.

alg:cutoff (cutoff, lim:xprs_mipabscutoff, XPRS_MIPABSCUTOFF)
      Branch and Bound: If the user knows that they are interested only in
      values of the objective function which are better than some value, this
      can be assigned to MIPABSCUTOFF. This allows the Optimizer to ignore
      solving any nodes which may yield worse objective values, saving
      solution time. When a MIP solution is found a new cut off value is
      calculated and the value can be obtained from the CURRMIPCUTOFF
      attribute. The value of CURRMIPCUTOFF is calculated using the
      MIPRELCUTOFF and MIPADDCUTOFF controls.

      Default: 1.0E+40 (for minimization problems); -1.0E+40 (for maximization
      problems).

alg:dual (alg:dualopt, dual, dualopt)
      Solve (MIP node) LPs by dual simplex method.

alg:feastol (feastol, tol:xprs_feastol, XPRS_FEASTOL)
      This tolerance determines when a solution is treated as feasible. If the
      amount by which a constraint's activity violates its right-hand side or
      ranged bound is less in absolute magnitude than FEASTOL, then the
      constraint is treated as satisfied. Similarly, if the amount by which a
      column violates its bounds is less in absolute magnitude than FEASTOL,
      those bounds are also treated as satisfied.

      Default: 1.0E-06

alg:feastolperturb (feastolperturb, sim:xprs_feastolperturb, XPRS_FEASTOLPERTURB)
      This tolerance determines how much a feasible primal basic solution is
      allowed to be perturbed when performing basis changes. The tolerance
      FEASTOL is always considered as an upper limit for the perturbations,
      but in some cases smaller value can be more desirable.

      Default: 1.0E-06

alg:feastoltarget (feastoltarget, sol:xprs_feastoltarget, XPRS_FEASTOLTARGET)
      This specifies the target feasibility tolerance for the solution
      refiner.

      Default: 0 — use the value specified by FEASTOL.

alg:global (global)
      0/1*: Allow global solving. Passing 0 should linearize all expressions
      requiring Xpress Global.

alg:localsolver (localsolver, nlp:localsolver, alg:xslp_solver, XSLP_SOLVER, LOCALSOLVER)
      Selects the library to use for local solves

      Values (default: -1):

      * (-1) automatic selection, based on model characteristics and solver
        availability

      * (0) use Xpress-SLP (always available)

      * (1) use Knitro if available

      * (2) use Xpress-Optimizer if possible (convex quadratic problems only)

alg:method (method, lpmethod, defaultalg, mip:xprs_defaultalg, XPRS_DEFAULTALG)
      This selects the algorithm that will be used to solve LPs, standalone or
      during MIP optimization.

      Values (default: 1):

      * (1) Automatically determined.

      * (2) Dual simplex.

      * (3) Primal simplex.

      * (4) Newton barrier (or hybrid gradient, if BARALG=4 is set).

alg:network (network)
      Solve (substructure of) (MIP node) LPs by network simplex method.

alg:nlpsolver (nlpsolver, nlp:solver, alg:xslp_nlpsolver, XSLP_NLPSOLVER, NLPSOLVER)
      Controls whether to call FICO Xpress Global or one of the local solvers

      Values (default: -1):

      * (-1) If the license allows and there are no user functions or
        multistart jobs, FICO Xpress Global will be called, otherwise a local
        solver.

      * (1) The algorithm selected by XSLP_SOLVER will be used to find a
        locally optimal solution

      * (2) FICO Xpress Global will be used to find a globally optimal
        solution

alg:numericalemphasis (alg:numericfocus, numericfocus, numfocus, numericemphasis, numericalemphasis, num:xprs_numericalemphasis, XPRS_NUMERICALEMPHASIS)
      How much emphasis to place on numerical stability instead of solve
      speed.

      Values (default: -1):

      * (-1) Automatic. The emphasis might be influenced by the setting of
        other controls.

      * (0) Emphasize speed.

      * (1) Mild emphasis on numerical stability.

      * (2) Medium emphasis on numerical stability.

      * (3) Strong emphasis on numerical stability.

alg:primal (alg:primalopt, primal, primalopt)
      Solve (MIP node) LPs by primal simplex method.

alg:randomseed (randomseed, tech:xprs_randomseed, XPRS_RANDOMSEED)
      Sets the initial seed to use for the pseudo-random number generator in
      the Optimizer. The sequence of random numbers is always reset using the
      seed when starting a new optimization run.

      Default: 1

alg:refactor (refactor, mip:xprs_refactor, XPRS_REFACTOR)
      Indicates whether the optimization should restart using the current
      representation of the factorization in memory.

      Values (default: -1):

      * (-1) Automatic.

      * (0) Do not refactor on reoptimizing.

      * (1) Refactor on reoptimizing.

alg:refineops (refineops, sol:xprs_refineops, XPRS_REFINEOPS)
      This specifies when the solution refiner should be executed to reduce
      solution infeasibilities. The refiner will attempt to satisfy the target
      tolerances for all original linear constraints before presolve or
      scaling has been applied.

      Values (default: 19 (bits 0, 1 and 4 are set)):

      * (0) Run the solution refiner on an optimal solution of a continuous
        problem.

      * (1) Run the solution refiner when a new solution is found during a
        tree search. The refiner will be applied to the presolved solution
        before any post-solve operations are applied.

      * (3) Run the solution refiner on each node of the MIP search.

      * (4) Run the solution refiner on an optimal solution before postsolve
        on a continuous problem.

      * (5) Apply the iterative refiner to refine the solution.

      * (6) Use higher precision in the iterative refinement.

      * (7) If set, the iterative refiner will use the primal simplex
        algorithm.

      * (8) If set, the iterative refiner will use the dual simplex algorithm.

      * (9) Refine MIP solutions such that rounding them keeps the problem
        feasible when reoptimized.

      * (10) Attempt to refine MIP solutions such that rounding them keeps the
        problem feasible when reoptimized, but accept integers solutions even
        if refinement fails.

alg:relax (relax)
      0*/1: Whether to relax integrality of variables.

alg:relcutoff (relcutoff, miprelcutoff, lim:xprs_miprelcutoff, XPRS_MIPRELCUTOFF)
      Branch and Bound: Percentage of the incumbent value to be added to the
      value of the objective function when an integer solution is found, to
      give the new value of CURRMIPCUTOFF. The effect is to cut off the search
      in parts of the tree whose best possible objective function would not be
      substantially better than the current solution. The control MIPRELSTOP
      provides a similar functionality but works in a different way.

      Default: 1.0E-04

alg:resourcestrategy (resourcestrategy, tech:xprs_resourcestrategy, XPRS_RESOURCESTRATEGY)
      Controls whether the optimizer is allowed to make nondeterministic
      decisions if memory is running low in an effort to preserve memory and
      finish the solve. Available memory (or container limits) are
      automatically detected but can also be changed by MAXMEMORYSOFT and
      MAXMEMORYHARD

      Values (default: 0):

      * (1) Allow the optimizer to change the solve path if necessary to
        preserve memory when getting close to one of the memory limits.

alg:start (warmstart)
      Whether to use incoming primal (and dual, for LP) variable values in a
      warmstart:

      0 - No
      1 - Yes (for LP: if there is no incoming alg:basis)
      2 - Yes (for LP: omitting the incoming alg:basis, if any)
      3 - Yes (for LP: together with the incoming alg:basis, if any;
          default).

alg:xslp_msmaxboundrange (XSLP_MSMAXBOUNDRANGE, MSMAXBOUNDRANGE)
      Defines the maximum range inside which initial points are generated by
      multistart presets

      Default: 1000

alg:xslp_multistart (XSLP_MULTISTART, MULTISTART)
      The multistart main control. Defines if the multistart search is to be
      initiated, or if only the baseline model is to be solved.

      Values (default: -1):

      * (-1) Depends on if any multistart jobs have been added.

      * (0) Multistart is off.

      * (1) Multistart is on.

alg:xslp_multistart_log (XSLP_MULTISTART_LOG, MULTISTART_LOG)
      The level of logging during the multistart run.

      Default: 0

alg:xslp_multistart_maxsolves (XSLP_MULTISTART_MAXSOLVES, MULTISTART_MAXSOLVES)
      The maximum number of jobs to create during the multistart search.

      Default: -1 (no upper limit)

alg:xslp_multistart_maxtime (XSLP_MULTISTART_MAXTIME, MULTISTART_MAXTIME)
      The maximum total time to be spent in the mutlistart search.

      Default: 0 (no upper limit)

alg:xslp_multistart_poolsize (XSLP_MULTISTART_POOLSIZE, MULTISTART_POOLSIZE)
      The maximum number of problem objects allowed to pool up before
      synchronization in the deterministic multistart.

      Default: 2

alg:xslp_multistart_seed (XSLP_MULTISTART_SEED, MULTISTART_SEED)
      Random seed used for the automatic generation of initial point when
      loading multistart presets

      Default: 0

alg:zerotol (matrixtol, tol:xprs_matrixtol, XPRS_MATRIXTOL)
      The zero tolerance on matrix elements. If the value of a matrix element
      is less than or equal to MATRIXTOL in absolute value, it is treated as
      zero. The control applies when solving a problem, for an input tolerance
      see INPUTTOL.

      Default: 1.0E-09

bar:alg (baralg, bar:xprs_baralg, XPRS_BARALG)
      This control determines which barrier algorithm is used to solve the
      problem. Notably, this is also the control to enable the primal-dual
      hybrid gradient algorithm.

      Values (default: -1):

      * (-1) Determined automatically.

      * (0) Unused.

      * (1) Use the infeasible-start barrier algorithm.

      * (2) Use the homogeneous self-dual barrier algorithm.

      * (3) Start with 2 and optionally switch to 1 during the execution.

      * (4) Use the hybrid gradient algorithm.

bar:cachesize (cachesize, sys:xprs_cachesize, XPRS_CACHESIZE)
      This parameter is deprecated and will be removed in a future release.
      Newton Barrier: L2 or L3 (see notes) cache size in kB (kilobytes) of the
      CPU. On Intel (or compatible) platforms a value of -1 may be used to
      determine the cache size automatically. If the CPU model is new then the
      cache size may not be correctly detected by an older release of the
      software.

      Default: -1

bar:choleskyalg (choleskyalg, bar:xprs_choleskyalg, XPRS_CHOLESKYALG)
      Newton barrier: type of Cholesky factorization used; bit-vector-control
      (see Section Bit-vector controls).

      Values (default: -1 (automatic)):

      * (0) matrix blocking: 0: automatic setting; 1: manual setting.

      * (1) if manual selection of matrix blocking: 0: multi-pass; 1:
        single-pass.

      * (2) nonseparable QP relaxation: 0: off; 1: on.

      * (3) corrector weight: 0: automatic setting; 1: manual setting.

      * (4) if manual selection of corrector weight: 0: off; 1: on.

      * (5) refinement: 0: automatic setting; 1: manual setting.

      * (6) preconditioned conjugate gradient method (PCGM): 0: PCGM off; 1:
        PCGM on.

      * (7) Preconditioned quasi minimal residual (QMR) to refine solution: 0:
        QMR off; 1: QMR on.

      * (8) Perform refinement on the augmented system 0: off; 1: on.

      * (9) Force highest accuracy in refinement 0: off; 1: on.

bar:choleskytol (choleskytol, bar:xprs_choleskytol, XPRS_CHOLESKYTOL)
      Newton barrier: The tolerance for pivot elements in the Cholesky
      decomposition of the normal equations coefficient matrix, computed at
      each iteration of the barrier algorithm. If the absolute value of the
      pivot element is less than or equal to CHOLESKYTOL, it merits special
      treatment in the Cholesky decomposition process.

      Default: 1.0E-15

bar:cores (barcores, bar:xprs_barcores, XPRS_BARCORES)
      If set to a positive integer it determines the number of physical CPU
      cores assumed to be present in the system by the barrier and hybrid
      gradient algorithms. If the value is set to the default value (-1),
      Xpress will automatically detect the number of cores.

      Default: -1(automatically detected)

bar:corespercpu (corespercpu, sys:xprs_corespercpu, XPRS_CORESPERCPU)
      Used to override the detected value of the number of cores on a CPU. The
      cache size (either detected or specified via the CACHESIZE control) used
      in Barrier methods will be divided by this amount, and this scaled-down
      value will be the amount of cache allocated to each Barrier thread

      Default: -1

bar:cpuplatform (cpuplatform, sys:xprs_cpuplatform, XPRS_CPUPLATFORM)
      Newton Barrier: Selects the AMD, Intel x86 or ARM vectorization
      instruction set that Barrier should run optimized code for. On AMD /
      Intel x86 platforms the SSE2, AVX and AVX2 instruction sets are
      supported while on ARM platforms the NEON architecture extension can be
      activated.

      Values (default: -2, using AVX2 instructions if supported by the CPU):

      * (-2) Highest supported [Generic, SSE2, AVX or AVX2].

      * (-1) Highest supported solve path consistent code [Generic, SSE2 or
        AVX].

      * (0) Use generic code compatible with all CPUs.

      * (1) Use SSE2 / NEON optimized code.

      * (2) Use AVX optimized code.

      * (3) Use AVX2 optimized code.

bar:crash (barcrash, bar:xprs_barcrash, XPRS_BARCRASH)
      Newton barrier and hybrid gradient: This determines the type of crash
      used for the crossover. During the crash procedure, an initial basis is
      determined which attempts to speed up the crossover. A good choice at
      this stage will significantly reduce the number of iterations required
      to crossover to an optimal solution. The possible values increase
      proportionally to their time-consumption.

      Values (default: 4):

      * (0) Turns off all crash procedures.

      * (1-6) Available strategies with 1 being conservative and 6 being
        aggressive.

bar:crossover (crossover, bar:xprs_crossover, XPRS_CROSSOVER)
      Newton barrier and hybrid gradient: This control determines whether the
      barrier method will cross over to the simplex method when at optimal
      solution has been found, to provide an end basis (see XPRSgetbasis,
      XPRSwritebasis) and advanced sensitivity analysis information (see
      XPRSobjsa, XPRSrhssa, XPRSbndsa).

      Values (default: -1):

      * (-1) Determined automatically.

      * (0) No crossover.

      * (1) Primal crossover first.

      * (2) Dual crossover first.

bar:crossoverops (crossoverops, bar:xprs_crossoverops, XPRS_CROSSOVEROPS)
      Newton barrier and hybrid gradient: a bit-vector (see Section Bit-vector
      controls) for adjusting the behavior of the crossover procedure.

      Values (default: 0):

      * (0) Returned solution when the crossover terminates prematurely: 0:
        Return the last basis from the crossover; 1: Return the barrier
        solution.

      * (1) Select the crossover stages to be performed: 0: Perform both
        crossover stages; 1: Skip second crossover stage.

      * (2) Set crossover behaviour: 0: Force to perform all pivots; 1: Skip
        pivots that are numerically less reliable.

      * (3) Set crossover behaviour: 0: Perform standard crossover; 1: Perform
        a slower, but numerically more careful crossover.

bar:crossoverthreads (crossoverthreads, bar:xprs_crossoverthreads, XPRS_CROSSOVERTHREADS)
      Determines the maximum number of threads that parallel crossover is
      allowed to use. If CROSSOVERTHREADS is set to the default value (-1),
      the BARTHREADS control will determine the number of threads used.

      Default: -1 (determined by the BARTHREADS control)

bar:crossovertol (crossovertol, crossoveraccuracytol, bar:xprs_crossoveraccuracytol, XPRS_CROSSOVERACCURACYTOL)
      Newton barrier: This control determines how crossover adjusts the
      default relative pivot tolerance. When re-inversion is necessary,
      crossover will compare the recalculated working basic solution with the
      assumed ones just before re-inversion took place. If the error is above
      this threshold, crossover will adjust the relative pivot tolerance to
      address the build-up of numerical inaccuracies.

      Default: 1e-6

bar:densecollimit (densecollimit, bar:xprs_densecollimit, XPRS_DENSECOLLIMIT)
      Newton barrier: Columns with more than DENSECOLLIMIT elements are
      considered to be dense. Such columns will be handled specially in the
      Cholesky factorization of this matrix.

      Default: 0 — determined automatically.

bar:dualstop (bardualstop, bar:xprs_bardualstop, XPRS_BARDUALSTOP)
      Newton barrier and hybrid gradient: This is a convergence parameter,
      representing the tolerance for dual infeasibilities. If the difference
      between the constraints and their bounds in the dual problem falls below
      this tolerance in absolute value, optimization will stop and the current
      solution will be returned.

      Values (default: 0):

      * (0) The default value is determined automatically based on the problem
        size, structure and algorithm choice.

      * (>=0) The tolerance for dual infeasibilities.

bar:gap (bargaptarget, bar:xprs_bargaptarget, XPRS_BARGAPTARGET)
      Newton barrier: The target tolerance for the relative duality gap. The
      barrier algorithm will keep iterating until either BARGAPTARGET is
      satisfied or until no further improvements are possible. In the latter
      case, if BARGAPSTOP is satisfied, it will declare the problem optimal.

      Values (default: 0 ):

      * (0) The default value is determined automatically based on the problem
        size, structure and algorithm choice.

      * (>=0) The target tolerance for the relative duality gap.

bar:gapstop (bargapstop, bar:xprs_bargapstop, XPRS_BARGAPSTOP)
      Newton barrier and hybrid gradient: This is a convergence parameter,
      representing the tolerance for the relative duality gap. When the
      difference between the primal and dual objective function values falls
      below this tolerance, the Optimizer determines that the optimal solution
      has been found.

      Values (default: 0 ):

      * (0) The default value is determined automatically based on the problem
        size, structure and algorithm choice.

      * (>=0) The tolerance for the relative duality gap.

bar:hgextrapolate (barhgextrapolate, pdhg:xprs_barhgextrapolate, XPRS_BARHGEXTRAPOLATE)
      Extrapolation parameter for the hybrid gradient algorithm. Although
      theory suggests that a value of 1 is best, slightly smaller values
      perform better in general.

      Default: 0.15

bar:hgmaxrestarts (barhgmaxrestarts, pdhg:xprs_barhgmaxrestarts, XPRS_BARHGMAXRESTARTS)
      The maximum number of restarts in the hybrid gradient algorithm.
      Restarts play the role of iterations in the hybrid gradient algorithm. A
      log line is printed at every restart, unless BAROUTPUT is set to 0.

      Default: 1250

bar:hgops (barhgops, pdhg:xprs_barhgops, XPRS_BARHGOPS)
      Bit-vector control (see Section Bit-vector controls) options for the
      hybrid gradient algorithm. Bits 1, 2 and 3 control which norms of the
      coefficient matrix are used for solution normalization. The
      normalization factor is the maximum of the selected norms. By default,
      or if all three bits are set to 0, the infinity norm is used. The omega
      parameter referenced in bits 4, 5 and 6 is a measure of the relative
      magnitudes of the objective and the right-hand side.

      Values (default: 24, the infinity norm is used for initialization and
      the L2 norm for measuring the solution quality. ):

      * (0) Use an asymmetric average for the primal averaging.

      * (1) Use the 1-norm of the coefficient matrix in normalizing the
        initial solution.

      * (2) Use the 2-norm of the coefficient matrix in normalizing the
        initial solution.

      * (3) Use the infinity norm of the coefficient matrix in normalizing the
        initial solution.

      * (4) Use L2 norm to measure solution quality.

      * (5) Contract omega towards 1 if the infeasibility is small enough.

      * (6) Omega is based on the infeasibility.

bar:indeflimit (barindeflimit, bar:xprs_barindeflimit, XPRS_BARINDEFLIMIT)
      Newton Barrier. This limits the number of consecutive indefinite barrier
      iterations that will be performed. The optimizer will try to minimize
      (resp. maximize) a QP problem even if the Q matrix is not positive
      (resp. negative) semi-definite. However, the optimizer may detect that
      the Q matrix is indefinite and this can result in the optimizer not
      converging. This control specifies how many indefinite iterations may
      occur before the optimizer stops and reports that the problem is
      indefinite. It is usual to specify a value greater than one, and only
      stop after a series of indefinite matrices, as the problem may be found
      to be indefinite incorrectly on a few iterations for numerical reasons.

      Default: 15

bar:kernel (barkernel, bar:xprs_barkernel, XPRS_BARKERNEL)
      Newton barrier: Defines how centrality is weighted in the barrier
      algorithm.

      Values (default: 0.0):

      * (>=+1.0) Increases the emphasis on centrality when larger value is
        set.

      * (<=-1.0) Selects a value adaptively in every iteration from [+1,
        -BARKERNEL].

bar:l1cache (l1cache, bar:xprs_l1cache, XPRS_L1CACHE)
      This parameter is deprecated and will be removed in a future release.
      Newton barrier: L1 cache size in kB (kilo bytes) of the CPU. On Intel
      (or compatible) platforms a value of -1 may be used to determine the
      cache size automatically.

      Default: Hardware/platform dependent.

bar:objperturb (barobjperturb, bar:xprs_barobjperturb, XPRS_BAROBJPERTURB)
      Defines how the barrier perturbs the objective.

      Values (default: 1e-6):

      * (>0) Let the optimizer decide if the objective is perturbed or not and
        use the parameter value as the scale of the perturbation.

      * (0) Turn off objective perturbation.

      * (<0) Always perturb the objective by the absolute value of the
        parameter.

bar:objscale (barobjscale)
      How the barrier algorithm scales the objective; when the objective is
      quadratic, the quadratic diagonal is used in determining the scale:

      -1  - Automatic choice (default)
      0   - Scale by the geometric mean of the objective coefficients
      > 0 - Scale so the argest objective coefficient in absolute value is <=
            barobjscale.

bar:order (barorder, bar:xprs_barorder, XPRS_BARORDER)
      Newton barrier: This controls the Cholesky factorization in the
      Newton-Barrier.

      Values (default: 0):

      * (0) Choose automatically.

      * (1) Minimum degree method. This selects diagonal elements with the
        smallest number of nonzeros in their rows or columns.

      * (2) Minimum local fill method. This considers the adjacency graph of
        nonzeros in the matrix and seeks to eliminate nodes that minimize the
        creation of new edges.

      * (3) Nested dissection method. This considers the adjacency graph and
        recursively seeks to separate it into non-adjacent pieces.

bar:orderthreads (barorderthreads, bar:xprs_barorderthreads, XPRS_BARORDERTHREADS)
      If set to a positive integer it determines the number of concurrent
      threads for the sparse matrix ordering algorithm in the Newton-barrier
      method.

      Values (default: 0 ):

      * (0) The default value is determined automatically based on the problem
        size, structure and algorithm choice.

      * (>=0) The number of concurrent threads for the sparse matrix ordering
        algorithm in the Newton-barrier method.

bar:output (baroutput, bar:xprs_baroutput, XPRS_BAROUTPUT)
      Newton barrier and hybrid gradient: This specifies the level of solution
      output provided. Output is provided either after each iteration of the
      algorithm, or else can be turned off completely by this parameter.

      Values (default: 1):

      * (0) No output.

      * (1) At each iteration.

bar:presolve (barpresolve, bar:xprs_barpresolveops, XPRS_BARPRESOLVEOPS)
      Newton barrier: This bit-vector (see Section Bit-vector controls)
      controls the Newton-Barrier specific presolve operations.

      Values (default: 0):

      * (0) Use standard presolve.

      * (1) Extra effort is spent in barrier specific presolve.

      * (2) Do full matrix eliminations (reduce matrix size).

bar:primalstop (barprimalstop, bar:xprs_barprimalstop, XPRS_BARPRIMALSTOP)
      Newton barrier and hybrid gradient: This is a convergence parameter,
      indicating the tolerance for primal infeasibilities. If the difference
      between the constraints and their bounds in the primal problem falls
      below this tolerance in absolute value, the Optimizer will terminate and
      return the current solution.

      Values (default: 0 ):

      * (0) The default value is determined automatically based on the problem
        size, structure and algorithm choice.

      * (>=0) The tolerance for primal infeasibilities.

bar:refiter (barrefiter, bar:xprs_barrefiter, XPRS_BARREFITER)
      Newton barrier: After terminating the barrier algorithm, further
      refinement steps can be performed. Such refinement steps are especially
      helpful if the solution is near to the optimum and can improve primal
      feasibility and decrease the complementarity gap. It is also often
      advantageous for the crossover algorithm. BARREFITER specifies the
      maximum number of such refinement iterations.

      Default: 0

bar:regularize (barreg, barrregularize, bar:xprs_barregularize, XPRS_BARREGULARIZE)
      This bit-vector control (see Section Bit-vector controls) determines how
      the barrier algorithm applies regularization on the KKT system.

      Values (default: -1):

      * (0) Standard regularization is turned on/off.

      * (1) Reduced regularization is turned on/off. This option reduces the
        perturbation effect of the standard regularization.

      * (2) Forces to keep dependent rows in the KKT system.

      * (3) Forces to preserve degenerate rows in the KKT system.

      * (4) Restrict regularization to infeasible iterates.

      * (5) Disable iterative regularizations.

      * (6) Apply iterative regularization more often.

bar:start (barstart, bar:xprs_barstart, XPRS_BARSTART)
      Controls the computation of the starting point and warm-starting for the
      Newton barrier and the hybrid gradient algorithms.

      Values (default: 0):

      * (-1) Uses the existing solution for warm-start if one is available.

      * (0) Warm-start is disabled; the starting point is determined
        automatically from the next three options.

      * (1) Uses simple heuristics to compute the starting point based on the
        magnitudes of the matrix entries.

      * (2) Uses the pseudoinverse of the constraint matrix to determine
        primal and dual initial solutions. Less sensitive to scaling and
        numerically more robust, but in several case less efficient than 1.

      * (3) Uses the unit starting point for the homogeneous self-dual barrier
        algorithm.

bar:stepstop (barstepstop, bar:xprs_barstepstop, XPRS_BARSTEPSTOP)
      Newton barrier: A convergence parameter, representing the minimal step
      size. On each iteration of the barrier algorithm, a step is taken along
      a computed search direction. If that step size is smaller than
      BARSTEPSTOP, the Optimizer will terminate and return the current
      solution.

      Default: 1.0E-16

bar:threads (barthreads, bar:xprs_barthreads, XPRS_BARTHREADS)
      If set to a positive integer it determines the number of threads
      implemented to run the Newton-barrier and hybrid gradient algorithms. If
      the value is set to the default value (-1), the THREADS control will
      determine the number of threads used.

      Default: -1(determined by the THREADS control)

bar:xprs_algaftercrossover (XPRS_ALGAFTERCROSSOVER)
      The algorithm to be used for the final clean up step after the
      crossover.

      Values (default: 1):

      * (1) Automatically determined.

      * (2) Dual simplex.

      * (3) Primal simplex.

      * (4) Concurrent.

bar:xprs_barfailiterlimit (XPRS_BARFAILITERLIMIT)
      Newton barrier: The maximum number of consecutive iterations that fail
      to improve the solution in the barrier algorithm.

      Values (default: 0):

      * (0) Determined automatically

      * (>0) Maximum number of consecutive barrier iterations allowed without
        progress.

bar:xprs_barfreescale (XPRS_BARFREESCALE)
      Defines how the barrier algorithm scales free variables.

      Default: 1e-6

bar:xprs_bariterative (XPRS_BARITERATIVE)
      The maximum number of barrier iterations in which an iterative solver is
      used instead of the Cholesky decomposition.

      Values (default: -2):

      * (-2) Automatically determined.

      * (-1) Turn iterative solver off.

      * (0) Use iterative solver for the starting point computation.

      * (n>0) Try to apply iterative solver for the first n barrier
        iterations.

bar:xprs_barlargebound (XPRS_BARLARGEBOUND)
      Threshold for the barrier to handle large bounds.

      Default: 0

bar:xprs_barobjscale (XPRS_BAROBJSCALE)
      Defines how the barrier scales the objective.

      Values (default: -1):

      * (-1) Let the optimizer decide.

      * (0) Scale by geometric mean.

      * (>=0) Scale such that the largest objective coefficient's largest
        element does not exceed this number. In quadratic problems, the
        quadratic diagonal is used as reference valuses instead of the linear
        objective.

bar:xprs_barperturb (XPRS_BARPERTURB)
      Newton barrier: In numerically challenging cases it is often
      advantageous to apply perturbations on the KKT system to improve its
      numerical properties. BARPERTURB controlls how much perturbation is
      allowed during the barrier iterations. By default no perturbation is
      allowed. Set this parameter with care as larger perturbations may lead
      to less efficient iterates and the best settings are problem-dependent.

      Default: 0

bar:xprs_barrhsscale (XPRS_BARRHSSCALE)
      Defines how the barrier scales the right hand side.

      Values (default: -1):

      * (-1) Let the optimizer decide.

      * (0) Scale by geometric mean.

      * (>=0) Scale such that the largest right hand side coefficient's
        largest element does not exceed this number.

bar:xprs_barsolution (XPRS_BARSOLUTION)
      This determines whether the barrier has to decide which is the best
      solution found or return the solution computed by the last barrier
      iteration.

      Values (default: 0):

      * (-1) (callback only: do not save current soulution as the best one).

      * (0) return the best solution found (in callback: let the barrier
        decide the current solution is the best or not).

      * (1) return the last barrier iteration (in callback: save current
        solution as the best solution so far).

bar:xprs_barstartweight (XPRS_BARSTARTWEIGHT)
      Newton barrier: This sets a weight for the warm-start point when
      warm-start is set for the barrier algorithm. Using larger weight gives
      more emphasis for the supplied starting point.

      Default: 0.85

bar:xprs_preanalyticcenter (XPRS_PREANALYTICCENTER)
      Determines if analytic centers should be computed and used for variable
      fixing and the generation of alternative reduced costs (-1: Auto 0: Off,
      1: Fixing, 2: Redcost, 3: Both)

      Values (default: -1):

      * (-1) Automatic.

      * (0) Disable analytic center presolving.

      * (1) Use analytic center for variable fixing only.

      * (2) Use analytic center for reduced cost computation only.

      * (3) Use analytic centers for both, variable fixing and reduced cost
        computation.

bit:xslp_control (XSLP_CONTROL)
      Bit map describing which Xpress NonLinear functions also activate the
      corresponding Optimizer Library function

      Values (default: 0 (no bits set)):

      * (0) Xpress NonLinear problem management functions do NOT invoke the
        corresponding Optimizer Library function for the underlying linear
        problem.

      * (1) XSLPcopycontrols does NOT invoke XPRScopycontrols.

      * (2) XSLPcopycallbacks does NOT invoke XPRScopycallbacks.

      * (3) XSLPcopyprob does NOT invoke XPRScopyprob.

      * (4) XSLPsetdefaults does NOT invoke XPRSsetdefaults.

      * (5) XSLPsave does NOT invoke XPRSsave.

      * (6) XSLPrestore does NOT invoke XPRSrestore.

cut:cover (covercuts, cut:xprs_covercuts, XPRS_COVERCUTS)
      Branch and Bound: The number of rounds of lifted cover inequalities at
      the root node. A lifted cover inequality is an additional constraint
      that can be particularly effective at reducing the size of the feasible
      region without removing potential integral solutions. The process of
      generating these can be carried out a number of times, further reducing
      the feasible region, albeit incurring a time penalty. There is usually a
      good payoff from generating these at the root node, since these
      inequalities then apply to every subsequent node in the tree search.

      Default: -1 — determined automatically.

cut:depth (cutdepth, cut:xprs_cutdepth, XPRS_CUTDEPTH)
      Branch and Bound: Sets the maximum depth in the tree search at which
      cuts will be generated. Generating cuts can take a lot of time, and is
      often less important at deeper levels of the tree since tighter bounds
      on the variables have already reduced the feasible region. A value of 0
      signifies that no cuts will be generated.

      Default: -1 — determined automatically.

cut:factor (cutfactor)
      Limit on number of cuts and cut coefficients added while solving MIPs.
      Default=-1 (automatic); a value of 0 will disable cuts generation.

cut:freq (cutfreq, cut:xprs_cutfreq, XPRS_CUTFREQ)
      Branch and Bound: This specifies the frequency at which cuts are
      generated in the tree search. If the depth of the node modulo CUTFREQ is
      zero, then cuts will be generated.

      Default: -1 — determined automatically.

cut:gomory (gomcuts, cut:xprs_gomcuts, XPRS_GOMCUTS)
      Branch and Bound: The number of rounds of Gomory or lift-and-project
      cuts at the root node.

      Default: -1 — determined automatically.

cut:lnpbest (lnpbest, cut:xprs_lnpbest, XPRS_LNPBEST)
      Number of infeasible MIP entities to create lift-and-project cuts for
      during each round of Gomory cuts at the root node (see GOMCUTS).

      Default: 50

cut:lnpiterlimit (lnpiterlimit, cut:xprs_lnpiterlimit, XPRS_LNPITERLIMIT)
      Number of iterations to perform in improving each lift-and-project cut.

      Default: -1 — determined automatically.

cut:qccuts (qccuts, cut:xprs_qccuts, XPRS_QCCUTS)
      Branch and Bound: Limit on the number of rounds of outer approximation
      cuts generated for the root node, when solving a mixed integer quadratic
      constrained or mixed integer second order conic problem with outer
      approximation.

      Default: -1 — determined automatically.

cut:rltcuts (rltcuts, cut:xprs_rltcuts, XPRS_RLTCUTS)
      Determines whether RLT cuts should be separated in the Xpress Global
      Solver.

      Values (default: -1):

      * (-1) The solver decides if RLT cuts are beneficial or not. This is the
        default setting.

      * (0) RLT cuts are disabled.

      * (1) RLT cuts are separated.

cut:select (cutselect, cut:xprs_cutselect, XPRS_CUTSELECT)
      A bit-vector (see Section Bit-vector controls) providing detailed
      control of the cuts created for the root node of a MIP solve. Use
      TREECUTSELECT to control cuts during the tree search.

      Values (default: -1):

      * (5) Clique cuts.

      * (6) Mixed Integer Rounding (MIR) cuts.

      * (7) Lifted cover cuts.

      * (8) Turn on row aggregation for MIR cuts.

      * (11) Flow path cuts.

      * (12) Implication cuts.

      * (13) Turn on automatic Lift-and-Project cutting strategy.

      * (14) Disable cutting from cut rows.

      * (15) Lifted GUB cover cuts.

      * (16) Zero-half cuts.

      * (17) Indicator constraint cuts.

      * (18) Strong Chvatal-Gomory cuts.

      * (20) Farkas cuts.

cut:strategy (cutstrategy, cut:xprs_cutstrategy, XPRS_CUTSTRATEGY)
      Branch and Bound: This specifies the cut strategy. A more aggressive cut
      strategy, generating a greater number of cuts, will result in fewer
      nodes to be explored, but with an associated time cost in generating the
      cuts. The fewer cuts generated, the less time taken, but the greater
      subsequent number of nodes to be explored.

      Values (default: -1):

      * (-1) Automatic selection of the cut strategy.

      * (0) No cuts.

      * (1) Conservative cut strategy.

      * (2) Moderate cut strategy.

      * (3) Aggressive cut strategy.

cut:treecover (treecovercuts, cut:xprs_treecovercuts, XPRS_TREECOVERCUTS)
      Branch and Bound: The number of rounds of lifted cover inequalities
      generated at nodes other than the root node in the tree. Compare with
      the description for COVERCUTS. A value of -1 indicates the number of
      rounds is determined automatically.

      Default: -1

cut:treegomory (treegomcuts, cut:xprs_treegomcuts, XPRS_TREEGOMCUTS)
      Branch and Bound: The number of rounds of Gomory cuts generated at nodes
      other than the first node in the tree. Compare with the description for
      GOMCUTS. A value of -1 indicates the number of rounds is determined
      automatically.

      Default: -1

cut:treeqccuts (treeqccuts, qp:xprs_treeqccuts, XPRS_TREEQCCUTS)
      Branch and Bound: Limit on the number of rounds of outer approximation
      cuts generated for nodes other than the root node, when solving a mixed
      integer quadratic constrained or mixed integer second order conic
      problem with outer approximation.

      Default: -1 — determined automatically.

cut:treeselect (treecutselect, cut:xprs_treecutselect, XPRS_TREECUTSELECT)
      A bit-vector (see Section Bit-vector controls) providing detailed
      control of the cuts created during the tree search of a MIP solve. Use
      CUTSELECT to control cuts on the root node.

      Values (default: -1):

      * (5) Clique cuts.

      * (6) Mixed Integer Rounding (MIR) cuts.

      * (7) Lifted cover cuts.

      * (8) Turn on row aggregation for MIR cuts.

      * (11) Flow path cuts.

      * (12) Implication cuts.

      * (13) Turn on automatic Lift and Project cutting strategy.

      * (14) Disable cutting from cut rows.

      * (15) Lifted GUB cover cuts.

      * (16) Zero-half cuts.

      * (17) Indicator constraint cuts.

      * (18) Strong Chvatal-Gomory cuts.

      * (20) Farkas cuts.

cut:xprs_autocutting (XPRS_AUTOCUTTING)
      Should the Optimizer automatically decide whether to generate cutting
      planes at local nodes in the tree or not? If the CUTFREQ control is set,
      no automatic selection will be made and local cutting will be enabled.

      Values (default: -1):

      * (-1) Automatic.

      * (0) Disabled.

      * (1) Enabled.

cut:xprs_cutfactor (XPRS_CUTFACTOR)
      Limit on the number of cuts and cut coefficients the optimizer is
      allowed to add to the matrix during tree search. The cuts and cut
      coefficients are limited by CUTFACTOR times the number of rows and
      coefficients in the initial matrix.

      Values (default: -1):

      * (-1) Let the optimizer decide on the maximum amount of cuts based on
        CUTSTRATEGY.

      * (>=0) Multiple of number of rows and coefficients to use.

cut:xprs_mcfcutstrategy (XPRS_MCFCUTSTRATEGY)
      Level of Multi-Commodity Flow (MCF) cutting planes separation: This
      specifies how aggressively MCF cuts should be separated. If the
      separation of MCF cuts is enabled, Xpress will try to detect a MCF
      network structure in the problem and, if such a structure is identified,
      it will separate specific cutting planes exploiting the identified
      network.

      Values (default: -1 ):

      * (-1) Automatic - let the Optimizer decide.

      * (0) Separation of MCF cuts disabled.

      * (1) Moderate separation of MCF cuts.

      * (2) Aggressive separation of MCF cuts.

cut:xprs_sdpcutstrategy (XPRS_SDPCUTSTRATEGY)
      Level of SDP cutting planes separation: This specifies how aggressively
      SDP cuts should be separated.

      Values (default: -1 ):

      * (-1) Automatic - let the Optimizer decide.

      * (0) Separation of SDP cuts disabled.

      * (1) Conservative separation of SDP cuts.

      * (2) Moderate separation of SDP cuts.

      * (3) Aggressive separation of SDP cuts.

cut:xslp_cutstrategy (XSLP_CUTSTRATEGY, SLPCUTSTRATEGY)
      Determines whihc cuts to apply in the MISLP search when the default
      SLP-in-MIP strategy is used.

      Default: 0

cvt:bigM (cvt:bigm, cvt:mip:bigM, cvt:mip:bigm)
      Default value of big-M for linearization of logical constraints. Not
      used by default. Use with care (prefer tight bounds). Should be smaller
      than (1.0 / [integrality tolerance])

cvt:compl (cvt:complementarity)
      Complementarity conversion method (if not accepted natively, see
      acc:compl and acc:nlcompl). Default 0:

      0 - Disjunction: a<=0 || b<=0, a>=0, b>=0
      1 - Product: a*b=cvt:compl:tol
      2 - Fischer-Burmeister function: sqrt(a^2+b^2+2*cvt:compl:tol)=a+b
      3 - min(a,b)=0

cvt:compl:tol (cvt:compl:eps, compl:eps)
      Tolerance parameter for the product and Fischer-Burmeister encodings of
      complementarity, see cvt:compl. Default 1e-9.

cvt:dvelim (dvelim)
      Eliminate AMPL defined variables by substitution into linear, quadratic,
      and polynomial expressions:

      0 - Do not eliminate, always instantiate the variables.
      1 - Eliminate only those used 1x. This can increase model density but
          greatly simplifies some models.
      2 - Always substitute where possible, even if the variable needs to be
          instantiated for use in other places. Can introduce redundancy, but
          seems best for some models (default.)

      See also cvt:pre:unnest, as well as AMPL options linelim and substout.

cvt:expcones (expcones)
      0*/1: Recognize exponential cones.

cvt:expr:nlassign (expr:nlassign)
      Above which reference count, a formula node should be assigned to a
      variable (see acc: options). 0 means all nodes outlined. Default 1.

cvt:mip:eps (cvt:cmp:eps, cmp:eps)
      Tolerance for strict comparison of continuous variables for MIP. Applies
      to <, >, and != operators. Also applies to negation of conditional
      comparisons: b==1 <==> x<=5 means that with b==0, x>=5+eps. Normally
      should be larger or equal to the solver's feasibility tolerance.
      Default: 1e-4.

cvt:multoutcard (multoutcard)
      Up to which (estimated) QP matrix cardinality should a product of 2
      linear expressions be multiplied out. Default 1e9.

      Low value can speed up model input, but prone to numerical issues.

cvt:names (names, modelnames)
      Whether to read or generate variable / constraint / objective names:

      0 - No names
      1 - (Default) Only provide names if at least one of .col / .row name
          files was written by AMPL (AMPL: `option [<solver>_]auxfiles rc;`) 
      2 - Read names from AMPL, but create generic names if not provided
      3 - Create generic names.

cvt:plapprox:domain (plapprox:domain, plapproxdomain)
      For piecewise-linear approximated functions, both arguments and result
      are bounded to +-[pladomain]. Default 1e6.

cvt:plapprox:reltol (plapprox:reltol, plapproxreltol)
      Relative tolerance for piecewise-linear approximation. Default 0.01.

cvt:pre:all
      0/1*: Set to 0 to disable most presolve in the flat converter.

cvt:pre:boundlogarg (boundlogarg)
      0*/1: Bound logarithm arguments to nonnegative.

cvt:pre:ctx2bndeq (ctx2bndeq)
      0/1*: Propagate exact context into conditional (dis)equalities-to-bound,
      vs always mixed. Can be affected by cvt:pre:ineq2bndeq. See #267.

cvt:pre:ctx2count (ctx2count)
      DEPRECATED. Use ctx2bndeq. NEW DEFAULT.

      Propagate exact context into atleast/atmost/exactly, count and numberof
      expressions, vs always mixed. Bitwise OR of the following values:

      1 - atleast/atmost/exactly, count
      2 - numberof with constant reference value
      4 - numberof with variable reference value.

      Default 7, see #267.

cvt:pre:ctx2ineq (ctx2ineq)
      0/1*: Propagate exact context into conditional inequalities, vs always
      mixed. See #267.

      Finer control provided by cvt:pre:ctx:cond...(le/ge) options.

cvt:pre:ctx:abs (ctx:abs)
      Controls propagation of context into abs() expressions, which could
      affect reformulations of abs() and its arguments (see the acc: options).
      Bitwise OR of the following values:

      1 - Propagate positive context exactly (otherwise always mixed)
      2 - Propagate negative context exactly (otherwise always mixed)

      Default 3. See mp.ampl.com/components.html#mathematical-background.

cvt:pre:ctx:acos (ctx:acos)
      Context propagation for 'Acos' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:acosh (ctx:acosh)
      Context propagation for 'Acosh' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:alldiff (ctx:alldiff)
      Context propagation for 'AllDiff' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:and (ctx:and)
      Context propagation for 'And' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:asin (ctx:asin)
      Context propagation for 'Asin' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:asinh (ctx:asinh)
      Context propagation for 'Asinh' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:atan (ctx:atan)
      Context propagation for 'Atan' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:atanh (ctx:atanh)
      Context propagation for 'Atanh' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:condlineq (ctx:condlineq)
      Context propagation for 'Conditional< AlgebraicConstraint< LinTerms,
      RhsEQ > >' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:condlinge (ctx:condlinge)
      Context propagation for 'Conditional< AlgebraicConstraint< LinTerms,
      RhsGE > >' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:condlingt (ctx:condlingt)
      Context propagation for 'Conditional< AlgebraicConstraint< LinTerms,
      RhsGT > >' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:condlinle (ctx:condlinle)
      Context propagation for 'Conditional< AlgebraicConstraint< LinTerms,
      RhsLE > >' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:condlinlt (ctx:condlinlt)
      Context propagation for 'Conditional< AlgebraicConstraint< LinTerms,
      RhsLT > >' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:condquadeq (ctx:condquadeq)
      Context propagation for 'Conditional< AlgebraicConstraint<
      QuadAndLinTerms, RhsEQ > >' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:condquadge (ctx:condquadge)
      Context propagation for 'Conditional< AlgebraicConstraint<
      QuadAndLinTerms, RhsGE > >' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:condquadgt (ctx:condquadgt)
      Context propagation for 'Conditional< AlgebraicConstraint<
      QuadAndLinTerms, RhsGT > >' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:condquadle (ctx:condquadle)
      Context propagation for 'Conditional< AlgebraicConstraint<
      QuadAndLinTerms, RhsLE > >' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:condquadlt (ctx:condquadlt)
      Context propagation for 'Conditional< AlgebraicConstraint<
      QuadAndLinTerms, RhsLT > >' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:cos (ctx:cos)
      Context propagation for 'Cos' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:cosh (ctx:cosh)
      Context propagation for 'Cosh' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:count (ctx:count)
      Context propagation for 'Count' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:div (ctx:div)
      Context propagation for 'Div' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:equiv (ctx:equiv)
      Context propagation for 'Equivalence' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:exp (ctx:exp)
      Context propagation for 'Exp' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:expa (ctx:expa)
      Context propagation for 'ExpA' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:ifthen (ctx:ifthen)
      Context propagation for 'IfThen' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:impl (ctx:impl)
      Context propagation for 'Implication' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:linfunccon (ctx:linfunccon)
      Context propagation for 'LinearFunctionalConstraint' expression, see
      cvt:pre:ctx:abs.

cvt:pre:ctx:log (ctx:log)
      Context propagation for 'Log' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:loga (ctx:loga)
      Context propagation for 'LogA' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:logistic (ctx:logistic)
      Context propagation for 'Logistic' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:max (ctx:max)
      Context propagation for 'Max' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:min (ctx:min)
      Context propagation for 'Min' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:not (ctx:not)
      Context propagation for 'Not' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:numberofconst (ctx:numberofconst)
      Context propagation for 'NumberofConst' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:numberofvar (ctx:numberofvar)
      Context propagation for 'NumberofVar' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:or (ctx:or)
      Context propagation for 'Or' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:pl (ctx:pl)
      Context propagation for 'PL' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:pow (ctx:pow)
      Context propagation for 'Pow' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:powconstexp (ctx:powconstexp)
      Context propagation for 'PowConstExp' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:quadfunccon (ctx:quadfunccon)
      Context propagation for 'QuadraticFunctionalConstraint' expression, see
      cvt:pre:ctx:abs.

cvt:pre:ctx:signpowconstexp (ctx:signpowconstexp)
      Context propagation for 'SignpowConstExp' expression, see
      cvt:pre:ctx:abs.

cvt:pre:ctx:sin (ctx:sin)
      Context propagation for 'Sin' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:sinh (ctx:sinh)
      Context propagation for 'Sinh' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:tan (ctx:tan)
      Context propagation for 'Tan' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:tanh (ctx:tanh)
      Context propagation for 'Tanh' expression, see cvt:pre:ctx:abs.

cvt:pre:eqbinary
      0/1*: Preprocess reified equality comparison with a binary variable.

cvt:pre:eqresult
      0/1*: Preprocess reified equality comparison's decidable cases.

cvt:pre:feastol (pre:feastol, pre:eps, pre:feastolabs, pre:epsabs)
      Absolute tolerance to check variable and constraint bound contraditions.
      Only warns if also pre:feastolrel is violated. See also sol:chk:feastol.
      Default 1e-6.

cvt:pre:feastolrel (pre:feastolrel, pre:epsrel)
      Relative tolerance to check variable and constraint bound
      contradictions. Only warns if also pre:feastol is violated. See also
      sol:chk:feastol. Default 1e-6.

cvt:pre:ineq2bndeq (ineq2bndeq)
      0/1*: Preprocess reified inequality expr <(=) c, where c <)=(
      lb(expr)+cvt:mip:eps, into expr == lb(expr), which works better on some
      benchmarks/solvers.

cvt:pre:ineq2related (ineq2related, ineq2rel)
      0/1*: Unify related reified inequalities: <=c, <c+cvt:mip:eps, >c,
      >=c+cvt:mip:eps.

cvt:pre:ineqresult
      0/1*: Preprocess reified inequality comparison's decidable cases.

cvt:pre:ineqrhs
      0/1*: Preprocess reified inequality comparison's right-hand sides (round
      for integer expression body).

cvt:pre:logistic (cvt:logistic)
      0*/1: recognize logistic functions in the model, see acc:logistic.

cvt:pre:prod (cvt:prod)
      Product preprocessing flags. Sum of a subset of the following bits:

      1 - Quadratize higher-order products in the following order: integer
      terms first, then real-valued ones; in each group, smaller-range terms
      first.
      2 - Logicalize products of 2 binary terms. Logicalizing means that the
      product is converted to a conjunction. If the solver does not support it
      natively (see acc:and), the conjunction is linearized.
      4 - Logicalize products of >=3 binary terms.

      Default: 5.

      Bits 2 or 4 imply bit 1.

cvt:pre:signpow (cvt:signpow)
      0*/1: recognize signpow() functions in the model, such as abs(x)*x, see
      acc:signpow.

cvt:pre:sort (cvt:sort)
      0/1*: Sort and eliminate duplicates in arguments of AND, OR, MIN, MAX.
      Sort arguments of COUNT, ATLEAST, EXACTLY, ATMOST, NUMBEROF, ALLDIFF.
      Can be necessary for some solvers.

cvt:pre:unnest (cvt:unnest, cvt:pre:inline, cvt:inline)
      Inline nested expressions. Bitwise OR of the following values:

      1 - AND/FORALL and OR/EXISTS expressions
      2 - Linear subexpressions
      4 - Quadratic subexpressions
      8 - MIN/MAX.

      See also option cvt:dvelim concerning only the input model. Default 15.

cvt:qp2passes (cvt:qp2pass, qp2passes, qp2pass)
      0/1*: Parse sums of QP expressions in 2 passes. Usually faster.

cvt:quadcon (passquadcon)
      Convenience option. Set to 0 to disable quadratic constraints. Synonym
      for acc:quad..=0. Currently this disables out-multiplication of
      quadratic terms, then they are linearized.

cvt:quadobj (passquadobj)
      0/1*: Pass quadratic objective terms to the solver. When 0, if the
      solver accepts quadratic constraints, such a constraint will be created
      with those, otherwise linearly approximated.

cvt:socp (socpmode, socp)
      Second-Order Cone recognition mode:

      0 - Do not recognize SOCP forms
      1 - Recognize from non-quadratic expressions only (sqrt, abs)
      2 - Recognize from quadratic and non-quadratic SOCP forms. Helpful if
          the solver does not recognize non-standard forms

      Recognized SOCP forms can be further converted to (SOCP-standardized)
      quadratic constraints, see cvt:socp2qc. Default: 1.

cvt:socp2qc (socp2qcmode, socp2qc)
      Mode to convert recognized SOCP forms to SOCP-standardized quadratic
      constraints:

      0 - Do not convert
      1 - Convert if no other cone types found, and not all original
          quadratics could be recognized as SOC, in particular if the
          objective is quadratic
      2 - Always convert

      Such conversion can be necessary if the solver does not accept a mix of
      conic and quadratic constraints/objectives. Default: 2.

cvt:sos (sos)
      0/1*: Whether to honor declared suffixes .sosno and .ref describing SOS
      sets. Each distinct nonzero .sosno value designates an SOS set, of type
      1 for positive .sosno values and of type 2 for negative values. The .ref
      suffix contains corresponding reference values used to order the
      variables.

cvt:sos2 (sos2)
      0*/1: Whether to honor SOS2 constraints for nonconvex piecewise-linear
      terms, using suffixes .sos and .sosref provided by AMPL. Currently under
      rework.

cvt:uenc:negctx:max (uenc:negctx:max, cvt:uenc:negctx, uenc:negctx)
      If cvt:uenc:ratio applies, max number of constants in comparisons
      x==const in negative context (equivalently, x!=const in positive
      context), where const!=lb(x) and const!=ub(x), to skip unary encoding of
      x. Default 1.

      Example:

      var x in 1..9;
      var y >=1 <=200;
      
      s.t. Con: (x==9 || x==2 || x==6) ==> y >= 4;

      With uenc:negctx<=1, this triggers unary encoding for x.

cvt:uenc:ratio (uenc:ratio)
      Min ratio (ub-lb+1)/Nvalues to skip unary encoding for a variable x,
      where Nvalues is the number of constants used in conditional comparisons
      x==const. Instead, indicator constraints (or big-Ms) are used, if
      uenc:negctx also applies. Default 0.

      Example:

      var x in 1..9;
      var y >=1 <=200;
      
      s.t. Con: y>3 ==> (x==2 || x==6 || x==5);

      With uenc:ratio>3, this triggers unary encoding for x.

dat:xslp_defaultiv (XSLP_DEFAULTIV, NLPDEFAULTIV)
      Default initial value for an SLP variable if none is explicitly given

      Default: 100

diff:xslp_delta_a (XSLP_DELTA_A, SLPDELTA_A)
      Absolute perturbation of values for calculating numerical derivatives

      Default: 0.001

diff:xslp_delta_infinity (XSLP_DELTA_INFINITY, SLPDELTA_INFINITY)
      Maximum value for partial derivatives

      Default: 1.0e+15

diff:xslp_delta_r (XSLP_DELTA_R, SLPDELTA_R)
      Relative perturbation of values for calculating numerical derivatives

      Default: 0.001

diff:xslp_delta_x (XSLP_DELTA_X, SLPDELTA_X)
      Minimum absolute value of delta coefficients to be retained

      Default: 1.0e-6

diff:xslp_delta_z (XSLP_DELTA_Z, SLPDELTA_Z)
      Tolerance used when calculating derivatives

      Default: 0.00001

diff:xslp_delta_zero (XSLP_DELTA_ZERO, SLPDELTA_ZERO)
      Absolute zero acceptance tolerance used when calculating derivatives

      Default: -1.0 (not applied)

diff:xslp_derivatives (XSLP_DERIVATIVES, NLPDERIVATIVES)
      Bitmap describing the method of calculating derivatives

      Values (default: 1):

      * (0) analytic derivatives where possible

      * (1) avoid embedding numerical derivatives of instantiated functions
        into analytic derivatives

diff:xslp_hessian (XSLP_HESSIAN, NLPHESSIAN)
      Second order differentiation mode when using analytical derivatives

      Values (default: -1):

      * (-1,0) automatic selection

      * (1) numerical derivatives (finite difference)

      * (2) symbolic differentiation

      * (3) automatic differentiation

diff:xslp_jacobian (XSLP_JACOBIAN, NLPJACOBIAN)
      First order differentiation mode when using analytical derivatives

      Values (default: -1):

      * (-1,0) automatic selection

      * (1) numerical derivatives (finite difference)

      * (2) symbolic differentiation

      * (3) automatic differentiation

func:xslp_evaluate (XSLP_EVALUATE, NLPEVALUATE)
      Evaluation strategy for user functions

      Values (default: 0):

      * (0) use derivatives where possible;

      * (1) always re-evaluate.

func:xslp_funceval (XSLP_FUNCEVAL, NLPFUNCEVAL)
      Bit map for determining the method of evaluating user functions and
      their derivatives

      Values (default: 0):

      * (3) evaluate function whenever independent variables change.

      * (4) evaluate function when independent variables change outside
        tolerances.

      * (5) application of bits 3-4: 0 = functions which do not have a defined
        re-evaluation mode;1 = all functions.

      * (6) tangential derivatives.

      * (7) forward derivatives

      * (8) application of bits 6-7: 0 = functions which do not have a defined
        derivative mode;1 = all functions.

func:xslp_threadsafeuserfunc (XSLP_THREADSAFEUSERFUNC, NLPTHREADSAFEUSERFUNC)
      Defines if user functions are allowed to be called in parallel

      Values (default: 0 (no parallel user function calls)):

      * (0) user function are not thread safe, and will not be called in
        parallel

      * (1) user functions are thread safe, and may be called in parallel

global:xprs_globalboundingbox (XPRS_GLOBALBOUNDINGBOX)
      If a nonlinear problem cannot be solved due to appearing unbounded, it
      can automatically be regularized by the application of a bounding box on
      the variables. If this control is set to a negative value, in a second
      solving attempt all original variables will be bounded by the absolute
      value of this control. If set to a positive value, there will be a third
      solving attempt afterwards, if necessary, in which also all auxiliary
      variables are bounded by this value.

      Values (default: 1.0E+06):

      * (0) Disabled. Problem will return unbounded.

      * (n<0) Enabled. Apply lower and upper bounds of this magnitude to all
        original variables if initial LP is unbounded.

      * (n>0) Enabled. Apply lower and upper bounds of this magnitude to all
        original and auxiliary variables if initial LP and first
        regularization are unbounded.

global:xprs_globallsheurstrategy (XPRS_GLOBALLSHEURSTRATEGY)
      When integer-feasible (for MINLP, any solution for NLP) but
      nonlinear-infeasible solutions are encountered within a global solve,
      the integer variables can be fixed and a local solver (as defined by the
      LOCALSOLVER control) can be called on the remaining continuous problem.
      This control defines the frequency and effort of such local solves.

      Values (default: -1 ):

      * (-1) Automatic selection of the strategy.

      * (0) Never run a local solver on a partially fixed solution.

      * (1) Conservative strategy.

      * (2) Moderate strategy.

      * (3) Aggressive strategy.

global:xprs_globalnlpcuts (XPRS_GLOBALNLPCUTS)
      Limit on the number of rounds of outer approximation and convexification
      cuts generated for the root node, when solving an (MI)NLP to global
      optimality.

      Default: -1 — determined automatically.

global:xprs_globalnuminitnlpcuts (XPRS_GLOBALNUMINITNLPCUTS)
      Specifies the maximum number of tangent cuts when setting up the initial
      relaxation during a global solve. By default, the algorithm chooses the
      number of cuts automatically. Adding more cuts tightens the problem,
      resulting in a smaller branch-and-bound tree, at the cost of slowing
      down each LP solve.

      Default: -1 — determined automatically.

global:xprs_globalpresolveobbt (XPRS_GLOBALPRESOLVEOBBT)
      Controls the amount of work performed by Optimization-Based Bound
      Tightening (OBBT).

      Values (default: -1):

      * (-1) Automatic. The solver decides how much effort goes into OBBT.

      * (0) Disabled. No OBBT will be performed.

      * (1) OBBT is run for a small subset of the variables, approximately
        equal to the square root of the number of total variables used in the
        solve, i.e., original and auxiliary.

      * (2) OBBT is run on a larger portion of the variables while keeping the
        computational effort limited w.r.t. the whole global solve.

      * (3) OBBT is run on all variables. This is most computationally taxing
        as a large number of LPs will be solved.

global:xprs_globalspatialbranchcuttingeffort (XPRS_GLOBALSPATIALBRANCHCUTTINGEFFORT)
      Limits the effort that is spent on creating cuts during spatial
      branching.

      Values (default: -1.0):

      * (-1) The algorithm chooses the effort limit automatically (default).

      * (0) Disables cuts on branching entities.

      * (0<n<1) Relative effort to spend on cutting on branching entities.
        Higher values lead to more cuts.

global:xprs_globalspatialbranchifpreferorig (XPRS_GLOBALSPATIALBRANCHIFPREFERORIG)
      Whether spatial branchings on original variables should be preferred
      over branching on auxiliary variables that were introduced by the
      reformulation of the global solver.

      Values (default: -1):

      * (-1) Automatically determined.

      * (0) Always consider both original and auxiliary variables.

      * (1) Always prefer branching on original variables over auxiliaries.

      * (2) Always prefer branching on auxiliary variables over originals.

global:xprs_globalspatialbranchpropagationeffort (XPRS_GLOBALSPATIALBRANCHPROPAGATIONEFFORT)
      Limits the effort that is spent on propagation during spatial branching.

      Values (default: -1.0):

      * (-1) The algorithm chooses the effort limit automatically (default).

      * (0) Disables propagation on branching entities.

      * (n>0) Relative effort to spend on propagating on branching entities.
        Higher values lead to more propagation.

global:xprs_globaltreenlpcuts (XPRS_GLOBALTREENLPCUTS)
      Limit on the number of rounds of outer approximation and convexification
      cuts generated for each node in the tree, when solving an (MI)NLP to
      global optimality.

      Default: -1 — determined automatically.

heur:xprs_heurdepth (XPRS_HEURDEPTH)
      Branch and Bound: Sets the maximum depth in the tree search at which
      heuristics will be used to find MIP solutions. It may be worth stopping
      the heuristic search for solutions after a certain depth in the tree
      search. A value of 0 signifies that heuristics will not be used. This
      control no longer has any effect and will be removed from future
      releases.

      Default: -1

heur:xprs_heurdiveiterlimit (XPRS_HEURDIVEITERLIMIT)
      Branch and Bound: Simplex iteration limit for reoptimizing during the
      diving heuristic.

      Values (default: -1):

      * (>=1) Fixed iteration limit.

      * (0) No iteration limit.

      * (<0) Automatic selection of the iteration limit based on the problem
        size. The absolute value is used as a multiplier on the automatic
        selection.

heur:xprs_heurmaxsol (XPRS_HEURMAXSOL)
      Branch and Bound: This specifies the maximum number of heuristic
      solutions that will be found in the tree search. This control no longer
      has any effect and will be removed from future releases.

      Default: -1

heur:xprs_heurnodes (XPRS_HEURNODES)
      Branch and Bound: This specifies the maximum number of nodes at which
      heuristics are used in the tree search. This control no longer has any
      effect and will be removed from future releases.

      Default: -1

heur:xprs_heursearchbackgroundselect (XPRS_HEURSEARCHBACKGROUNDSELECT)
      Bit-vector control (see Section Bit-vector controls) to select which
      large neighborhood searches to run in the background (for example in
      parallel to the root cut loop).

      Values (default: -1):

      * (1) Enable L heuristic.

heur:xprs_heursearchcopycontrols (XPRS_HEURSEARCHCOPYCONTROLS)
      Select how user-set controls should affect local search heuristics.

      Values (default: 1):

      * (0) Do not copy any user-set controls

      * (1) Automatic - Let the Optimizer decide which user-set controls to
        copy

      * (2) Copy all user-set controls

heur:xprs_prerootthreads (XPRS_PREROOTTHREADS)
      Specifies an explicit number of threads that should be used for the
      Pre-root parallel heuristic phase. By default, this phase will use all
      threads available to the solver (as governed by the control THREADS).

      Values (default: -1):

      * (-1) Use all available threads.

      * (0) Disable pre-root parallel heuristics.

      * (n>0) Use the specified number of threads, superseding the value of
        THREADS

heur:xprs_usersolheuristic (XPRS_USERSOLHEURISTIC)
      Determines how much effort to put into running a local search heuristic
      to find a feasible integer solution from a partial or infeasible user
      solution.

      Values (default: -1):

      * (-1) Automatically determined.

      * (0) Search heuristic disabled.

      * (1) Light effort.

      * (2) Moderate effort.

      * (3) High effort.

heur:xslp_findiv (XSLP_FINDIV, NLPFINDIV)
      Option for running a heuristic to find a feasible initial point

      Values (default: -1):

      * (-1) Automatic (default).

      * (0) Disable the heuristic.

      * (1) Enable the heuristic.

heur:xslp_gridheurselect (XSLP_GRIDHEURSELECT, SLPGRIDHEURSELECT)
      Bit map selectin which heuristics to run if the problem has variable
      with an integer delta

      Values (default: 6):

      * (0) Enumeration: try all combinations.

      * (1) Simple search heuristics.

      * (2) Simulated annealing.

heur:xslp_heurstrategy (XSLP_HEURSTRATEGY, SLPHEURSTRATEGY)
      Branch and Bound: This specifies the MINLP heuristic strategy. On some
      problems it is worth trying more comprehensive heuristic strategies by
      setting HEURSTRATEGY to 2 or 3.

      Values (default: -1):

      * (-1) Automatic selection of heuristic strategy (depending on
        XPRS_HEUREMPHASIS).

      * (0) No heuristics.

      * (1) Basic heuristic strategy.

      * (2) Enhanced heuristic strategy.

      * (3) Extensive heuristic strategy.

      * (4) Run all heuristics without effort limits.

iis:find (iisfind, iis, alg:iisfind)
      Whether to find and export an IIS. Default = 0 (don't export).

iis:log (iislog, inf:xprs_iislog, XPRS_IISLOG)
      Selects how much information should be printed during the IIS procedure.
      Please refer to Appendix The IIS Log for a more detailed description of
      the IIS logging format.

      Values (default: 1, a progress log is printed ):

      * (0) The IIS procedure does not produce any output.

      * (1) Prints general information and a progress log of the deletion
        filter, including bounds on the size of the IIS and timing
        information.

      * (2) Complete logging, including the full progress log of all the
        subproblem solves in the deletion filter. This setting is recommended
        only for debugging as it may produce a lot of output.

iis:max (iismax, maxiis, inf:xprs_maxiis, XPRS_MAXIIS)
      This function controls the number of Irreducible Infeasible Sets to be
      found using the XPRSiisall (IIS-a).

      Values (default: -1):

      * (-1) Search for all IIS.

      * (0) Do not search for IIS.

      * (n>0) Search for the first n IIS.

iis:ops (iisops, inf:xprs_iisops, XPRS_IISOPS)
      Selects which part of the restrictions (bounds, constraints, entities)
      should always be kept in an IIS. This is useful if certain types of
      restrictions cannot be violated, thus they are known not to be the cause
      of infeasibility. The IIS obtained this way is irreducible only for the
      non-protected restrictions. This bit-vector control (see Section
      Bit-vector controls) has an effect only on the deletion filter of the
      IIS procedure.

      Values (default: 0, all restrictions are valid candidates for removal ):

      * (0) Keep binary integralities.

      * (1) Keep the 0 lower bounds of variables.

      * (2) Keep fixed variables.

      * (3) Keep all variable bounds.

      * (4) Keep all general integer entities, except binaries.

      * (5) Keep all equality constraints.

      * (6) Keep all general constraints.

      * (7) Keep all piecewise linear constraints.

      * (8) Keep all specially ordered set (SOS) constraints.

      * (9) Keep all indicator constraints.

      * (10) Keep all delayed rows.

      * (11) Keep all constraints.

inf:xprs_repairinfeasmaxtime (XPRS_REPAIRINFEASMAXTIME)
      This parameter is deprecated and will be removed in a future release.
      Overall time limit for the repairinfeas tool

      Values (default: 0):

      * (0) No time limit.

      * (n>0) If an integer solution has been found, stop MIP search after n
        seconds, otherwise continue until an integer solution is finally
        found.

      * (n<0) Stop in LP or MIP search after n seconds.

inf:xprs_repairinfeastimelimit (XPRS_REPAIRINFEASTIMELIMIT)
      Overall time limit for the repairinfeas tool

      Values (default: 1e+20):

      * (>0) Stop repairinfeas search after the given number of seconds.

lim:bariter (bar:iterlim, bariterlim, bar:xprs_bariterlimit, XPRS_BARITERLIMIT)
      Newton barrier: The maximum number of iterations. While the simplex
      method usually performs a number of iterations which is proportional to
      the number of constraints (rows) in a problem, the barrier method
      standardly finds the optimal solution to a given accuracy after a number
      of iterations which is independent of the problem size. The penalty is
      rather that the time for each iteration increases with the size of the
      problem. BARITERLIMIT specifies the maximum number of iterations which
      will be carried out by the barrier.

      Default: 500

lim:crossoveriter (bar:crossoveriterlim, crossoveriterlim, crossoveritlim, bar:xprs_crossoveriterlimit, XPRS_CROSSOVERITERLIMIT)
      Newton barrier and hybrid gradient: The maximum number of iterations
      that will be performed in the crossover procedure before the
      optimization process terminates.

      Default: 2147483647

lim:heurdiveiterlimit (heurdepth, mip:heurdiveiterlimit)
      Simplex iteration limit for reoptimizing during the diving heuristic;
      default = -1 (automatic selection); a value of 0 implies no iteration
      limit

lim:iter (lpiterlimit, iterlim, lp:xprs_lpiterlimit, XPRS_LPITERLIMIT)
      The maximum number of iterations that will be performed by primal
      simplex or dual simplex before the optimization process terminates. For
      MIP problems, this is the maximum total number of iterations over all
      nodes explored by the Branch and Bound method.

      Default: 2147483647

lim:lprefineiter (lprefineiterlimit, lp:xprs_lprefineiterlimit, XPRS_LPREFINEITERLIMIT)
      This specifies the simplex iteration limit the solution refiner can
      spend in attempting to increase the accuracy of an LP solution.

      Default: -1 — determined automatically.

lim:maxcuttime (maxcuttime, cut:xprs_maxcuttime, XPRS_MAXCUTTIME)
      The maximum amount of time allowed for generation of cutting planes and
      reoptimization. The limit is checked during generation and no further
      cuts are added once this limit has been exceeded.

      Values (default: 0):

      * (0) No time limit.

      * (>0) Stop cut generation after the given number of seconds.

lim:mem (memlimit, maxmemoryhard, tech:xprs_maxmemoryhard, XPRS_MAXMEMORYHARD)
      This control sets the maximum amount of memory in megabytes the
      optimizer should allocate. If this limit is exceeded, the solve will
      terminate. This control is designed to make the optimizer stop in a
      controlled manner, so that the problem object is valid once termination
      occurs. The solve state will be set to incomplete. This is different to
      an out of memory condition in which case the optimizer returns an error.
      The optimizer may still allocate memory once the limit is exceeded to be
      able to finsish the operations and stop in a controlled manner. When
      RESOURCESTRATEGY is enabled, the control also has the same effect as
      MAXMEMORYSOFT and will cause the optimizer to try preserving memory when
      possible.

      Default: 0 (no limit)

lim:mipsol (maxmipsol, lim:xprs_maxmipsol, XPRS_MAXMIPSOL)
      Branch and Bound: This specifies a limit on the number of integer
      solutions to be found by the Optimizer. It is possible that during
      optimization the Optimizer will find the same objective solution from
      different nodes. However, MAXMIPSOL refers to the total number of
      integer solutions found, and not necessarily the number of distinct
      solutions.

      Default: 0

lim:nodes (nodelim, nodelimit, maxnode, mip:xprs_maxnode, XPRS_MAXNODE)
      Branch and Bound: The maximum number of nodes that will be explored.

      Default: 2147483647

lim:prerooteffort (prerooteffort, mip:prerooteffort, heur:xprs_prerooteffort, XPRS_PREROOTEFFORT)
      Dial for the work spent during the Pre-root parallel heuristic phase. A
      positive value sets a suitable work limit that is dependent on
      problem-characteristics. Changing the value up/or down dials the work
      spent in this phase up or down. This control also enables/disables
      Pre-root parallel heuristics.

      Values (default: -1):

      * (-2) Enable Pre-root parallel heuristics without a specific work limit
        for this phase. The phase will terminate if a different limit is hit,
        or if it runs out of heuristic work to do.

      * (-1) Enablement of Pre-root parallel heuristics is subject to
        HEUREMPHASIS.

      * (0) Disable Pre-root parallel heuristics.

      * (x>0) Enable Pre-root parallel heuristics with a work limit dependent
        on problem characteristics, using x as a factor to dial this work
        limit up or down.

lim:prerootwork (prerootworklim, prerootworklimit, heur:xprs_prerootworklimit, XPRS_PREROOTWORKLIMIT)
      Set an explicit work limit in work units for the Pre-root parallel
      heuristic phase. Any positive value also enables this phase and runs it
      until the PREROOTWORKLIMIT units of work are hit.

      Values (default: -1):

      * (-1) No explicit work limit for the Pre-root parallel heuristic phase.
        If enabled, the work limit for this phase is controlled via
        PREROOTEFFORT.

      * (0) Disable Pre-root parallel heuristics.

      * (x>0) Enable Pre-root parallel heuristics with an explicit work limit
        of x work units. If set, this work limit has precedence over any work
        limit set by PREROOTEFFORT.

lim:softmem (softmemlimit, maxmemorysoft, tech:xprs_maxmemorysoft, XPRS_MAXMEMORYSOFT)
      When RESOURCESTRATEGY is enabled, this control sets the maximum amount
      of memory in megabytes the optimizer targets to allocate. This may
      change the solving path, but will not cause the solve to terminate
      early. To set a hard version of the same, please set MAXMEMORYHARD.

      Default: 0 (no limit)

lim:soltime (soltimelim, soltimelimit, lim:xprs_soltimelimit, XPRS_SOLTIMELIMIT)
      The maximum time in seconds that the Optimizer will run a MIP solve
      before it terminates, given that a solution has been found. As long as
      no solution has been found, this control will have no effect.

      Values (default: 1e+20):

      * (>0) If an integer solution has been found, stop MIP search after the
        given number of seconds, otherwise continue until an integer solution
        is finally found.

lim:stalltime (maxstalltime, lim:xprs_maxstalltime, XPRS_MAXSTALLTIME)
      The maximum time in seconds that the Optimizer will continue to search
      for improving solution after finding a new incumbent.

      Values (default: 0):

      * (0) No stall time limit.

      * (>0) If an integer solution has been found, stop MIP search after the
        given number of seconds without a new incumbent. No effect as long as
        no solution was found.

lim:time (timelim, timelimit, lim:xprs_timelimit, XPRS_TIMELIMIT)
      The maximum time in seconds that the Optimizer will run before it
      terminates, including the problem setup time and solution time. For MIP
      problems, this is the total time taken to solve all nodes.

      Values (default: 1e+20):

      * (>0) Stop LP or MIP search after the given number of seconds.

lim:work (worklim, worklimit, tech:xprs_worklimit, XPRS_WORKLIMIT)
      The maximum work (measured in work units) that the Optimizer will run
      before it terminates. WORK is accumulated during the search and ever
      increasing. In contrast to TIME, WORK is independent of the hardware and
      platform on which the search is conducted. The WORKLIMIT serves as a
      deterministic stopping criterion. When it is reached, it leaves the
      optimizer in a reproducible state.

      Values (default: 1e+20):

      * (>0) Stop LP or MIP search when the given number of work units is
        reached.

lim:xprs_maxchecksonmaxcuttime (XPRS_MAXCHECKSONMAXCUTTIME)
      This control is intended for use where optimization runs that are
      terminated using the MAXCUTTIME control are required to be reproduced
      exactly. This control is necessary because of the inherent difficulty in
      terminating algorithmic software in a consistent way using temporal
      criteria. The control value relates to the number of times the optimizer
      checks the MAXCUTTIME criterion up to and including the check when the
      termination of cutting was activated. To use the control the user first
      must obtain the value of the CHECKSONMAXCUTTIME attribute after the run
      returns. This attribute value is the number of times the optimizer
      checked the MAXCUTTIME criterion during the last call to the
      optimization routine XPRSmipoptimize. Note that this attribute value
      will be negative if the optimizer terminated cutting on the MAXCUTTIME
      criterion. To ensure accurate reproduction of a run the user should
      first ensure that MAXCUTTIME is set to its default value or to a large
      value so the run does not terminate again on MAXCUTTIME and then simply
      set the control MAXCHECKSONMAXCUTTIME to the absolute value of the
      CHECKSONMAXCUTTIME value.

      Values (default: 0):

      * (0) Not active.

      * (n>0) The number of times the optimizer should check the MAXCUTTIME
        criterion before triggering a termination.

lim:xprs_maxchecksonmaxtime (XPRS_MAXCHECKSONMAXTIME)
      This control is intended for use where optimization runs that are
      terminated using the TIMELIMIT (or the deprecated MAXTIME) control are
      required to be reproduced exactly. This control is necessary because of
      the inherent difficulty in terminating algorithmic software in a
      consistent way using temporal criteria. The control value relates to the
      number of times the optimizer checks the TIMELIMIT criterion up to and
      including the check when the termination was activated. To use the
      control the user first must obtain the value of the CHECKSONMAXTIME
      attribute after the run returns. This attribute value is the number of
      times the optimizer checked the TIMELIMIT criterion during the last call
      to the optimization routine XPRSmipoptimize. Note that this attribute
      value will be negative if the optimizer terminated on the TIMELIMIT
      criterion. To ensure that a reproduction of a run terminates in the same
      way the user should first ensure that TIMELIMIT is set to its default
      value or to a large value so the run does not terminate again on
      TIMELIMIT and then simply set the control MAXCHECKSONMAXTIME to the
      absolute value of the CHECKSONMAXTIME value.

      Values (default: 0):

      * (0) Not active.

      * (n>0) The number of times the optimizer should check the TIMELIMIT (or
        MAXTIME) criterion before triggering a termination.

lim:xprs_maxtime (XPRS_MAXTIME)
      This parameter is deprecated and will be removed in a future release.
      The maximum time in seconds that the Optimizer will run before it
      terminates, including the problem setup time and solution time. For MIP
      problems, this is the total time taken to solve all nodes.

      Values (default: 0):

      * (0) No time limit.

      * (n>0) If an integer solution has been found, stop MIP search after n
        seconds, otherwise continue until an integer solution is finally
        found.

      * (n<0) Stop in LP or MIP search after n seconds.

lim:xslp_maxtime (XSLP_MAXTIME, NLPMAXTIME)
      The maximum time in seconds that the SLP optimization will run before it
      terminates

      Default: 0

log:xprs_maxpagelines (XPRS_MAXPAGELINES)
      Number of lines between page breaks in printable output.

      Default: 23

log:xprs_outputcontrols (XPRS_OUTPUTCONTROLS)
      This control toggles the printing of all control settings at the
      beginning of the search. This includes the printing of controls that
      have been explicitly assigned to their default value. All unset controls
      are omitted as they keep their default value.

      Values (default: 1):

      * (0) Turn off printing of user-specified control settings.

      * (1) Print controls.

log:xprs_outputlog (XPRS_OUTPUTLOG)
      This controls the level of output produced by the Optimizer during
      optimization. In the Console Optimizer, OUTPUTLOG controls which
      messages are sent to the screen (stdout). When using the Optimizer
      library, no output is sent to the screen. If the user wishes output to
      be displayed, they must define a callback function and print messages to
      the screen themselves. In this case, OUTPUTLOG controls which messages
      are sent to the user output callback.

      Values (default: 1):

      * (0) Turn all output off. Use XPRS_OUTPUTLOG_NO_OUTPUT from xprs.h.

      * (1) Print all messages. Use XPRS_OUTPUTLOG_FULL_OUTPUT from xprs.h.

      * (3) Print error and warning messages. Use
        XPRS_OUTPUTLOG_ERRORS_AND_WARNINGS from xprs.h.

      * (4) Print error messages only. Use XPRS_OUTPUTLOG_ERRORS from xprs.h.

log:xslp_echoxprsmessages (XSLP_ECHOXPRSMESSAGES)
      Controls if the XSLP message callback should relay messages from the
      XPRS library.

      Values (default: -1):

      * (-1) automatic: if an XSLP message callback is not set, then messages
        from the nonlinear solver are sent to the XPRS message callback; if an
        XSLP message callback is set, then messages are not echoed.

      * (0) the XPRS and XSLP message callbacks are treated as independent.

      * (1) messages from the XPRS message callback are sent to the XSLP
        message callback.

      * (2) messages from the nonlinear solver are sent to the XPRS message
        callback.

log:xslp_primalintegralalpha (XSLP_PRIMALINTEGRALALPHA, NLPPRIMALINTEGRALALPHA)
      Decay term for primal integral computation

      Default: 0

log:xslp_primalintegralref (XSLP_PRIMALINTEGRALREF, NLPPRIMALINTEGRALREF)
      Reference solution value to take into account when calculating the
      primal integral

      Default: XPRS_PLUSINFINITY

lp:bigm (bigm, bigmpenalty, lp:xprs_bigm, XPRS_BIGM)
      The infeasibility penalty used if the 'Big M' method is implemented.

      Default: Dependent on the matrix characteristics.

lp:bigmmethod (bigmmethod, lp:xprs_bigmmethod, XPRS_BIGMMETHOD)
      Simplex: This specifies whether to use the 'Big M' method, or the
      standard phase I (achieving feasibility) and phase II (achieving
      optimality). In the 'Big M' method, the objective coefficients of the
      variables are considered during the feasibility phase, possibly leading
      to an initial feasible basis which is closer to optimal. The
      side-effects involve possible round-off errors due to the presence of
      the 'Big M' factor in the problem.

      Values (default: 1):

      * (0) For phase I / phase II.

      * (1) If 'Big M' method to be used.

lp:crash (crash, lp:xprs_crash, XPRS_CRASH)
      Simplex: This determines the type of crash used when the algorithm
      begins. During the crash procedure, an initial basis is determined which
      is as close to feasibility and triangularity as possible. A good choice
      at this stage will significantly reduce the number of iterations
      required to find an optimal solution. The possible values increase
      proportionally to their time-consumption.

      Values (default: 2):

      * (0) Turns off all crash procedures.

      * (1) For singletons only (one pass).

      * (2) For singletons only (multi pass).

      * (3) Multiple passes through the matrix considering slacks.

      * (4) Multiple (≤10) passes through the matrix but only doing slacks
        at the very end.

      * (n>10) As for value 4 but performing at most n - 10 passes.

      * (0) Perform standard crash.

      * (1) Perform additional numerical checks during crash.

      * (2) Extend the set of column candidates for crash.

      * (3) Extend the set of row candidates for crash.

      * (4) Force crash, i.e., consider all suitable columns/rows as
        candidates for crash.

lp:dualforceparallel (forceparalleldual, dualforceparallel, lp:xprs_forceparalleldual, XPRS_FORCEPARALLELDUAL)
      Dual simplex: specifies whether the dual simplex solver should always
      use the parallel simplex algorithm. By default, when using a single
      thread, the dual simplex solver will execute a dedicated sequential
      simplex algorithm.

      Values (default: 0):

      * (0) Disabled.

      * (1) Enabled. Force the dual simplex solver to use the parallel
        algorithm.

lp:dualgradient (dualgradient, lp:xprs_dualgradient, XPRS_DUALGRADIENT)
      Simplex: This specifies the dual simplex pricing method.

      Values (default: -1):

      * (-1) Determined automatically.

      * (0) Devex.

      * (1) Steepest edge.

      * (2) Direct steepest edge.

      * (3) Sparse Devex.

lp:dualize (dualize, lp:xprs_dualize, XPRS_DUALIZE)
      For a linear problem or the initial linear relaxation of a MIP,
      determines whether to form and solve the dual problem.

      Values (default: -1):

      * (-1) Determine automatically which version would be faster.

      * (0) Solve the original problem.

      * (1) Solve the dualized problem.

lp:dualizeops (dualizeops, lp:xprs_dualizeops, XPRS_DUALIZEOPS)
      Bit-vector control (see Section Bit-vector controls) for adjusting the
      behavior when a problem is dualized.

      Values (default: 1 (bit 0 is set)):

      * (0) Swap the simplex algorithm to run. If dual simplex is selected for
        the original problem then primal simplex will be run on the dualized
        problem, and simiarly if primal simplex is selected.

lp:dualperturb (dualperturb, lp:xprs_dualperturb, XPRS_DUALPERTURB)
      The factor by which the problem will be perturbed prior to optimization
      by dual simplex. A value of 0.0 results in no perturbation prior to
      optimization. Note the interconnection to the AUTOPERTURB control. If
      AUTOPERTURB is set to 1, the decision whether to perturb or not is left
      to the Optimizer. When the problem is automatically perturbed in dual
      simplex, however, the value of DUALPERTURB will be used for
      perturbation.

      Default: -1 — determined automatically.

lp:dualstrategy (dualstrategy, lp:xprs_dualstrategy, XPRS_DUALSTRATEGY)
      This bit-vector control (see Section Bit-vector controls) specifies the
      dual simplex strategy.

      Values (default: 1):

      * (0) Switch to primal when re-optimization goes dual infeasible and
        numerically unstable.

      * (1) When dual intend to switch to primal, stop the solve instead of
        switching to primal.

      * (2) Use more aggressive cut-off in MIP search.

      * (3) Use dual simplex to remove cost perturbations.

      * (4) Enable more aggressive dual pivoting strategy.

      * (5) Keep using dual simplex even when it's numerically unstable.

lp:dualthreads (dualthreads, tech:xprs_dualthreads, XPRS_DUALTHREADS)
      Determines the maximum number of threads that dual simplex is allowed to
      use. If DUALTHREADS is set to the default value (-1), the THREADS
      control will determine the number of threads used.

      Default: -1 (determined by the THREADS control)

lp:etatol (etatol, sim:xprs_etatol, XPRS_ETATOL)
      Tolerance on eta elements. During each iteration, the basis inverse is
      premultiplied by an elementary matrix, which is the identity except for
      one column - the eta vector. Elements of eta vectors whose absolute
      value is smaller than ETATOL are taken to be zero in this step.

      Default: 1.0E-13

lp:folding (lpfolding, alg:lpfolding, lp:xprs_lpfolding, XPRS_LPFOLDING)
      Simplex and barrier: whether to fold an LP problem before solving it.

      Values (default: -1):

      * (-1) Automatic.

      * (0) Disable LP folding.

      * (1) Enable LP folding. Attempt to fold all LP problems and MIP initial
        relaxations.

lp:invertfreq (invertfreq, sim:xprs_invertfreq, XPRS_INVERTFREQ)
      Simplex: The frequency with which the basis will be inverted. The basis
      is maintained in a factorized form and on most simplex iterations it is
      incrementally updated to reflect the step just taken. This is
      considerably faster than computing the full inverted matrix at each
      iteration, although after a number of iterations the basis becomes less
      well-conditioned and it becomes necessary to compute the full inverted
      matrix. The value of INVERTFREQ specifies the maximum number of
      iterations between full inversions.

      Default: -1 — the frequency is determined automatically.

lp:invertmin (invertmin, sim:xprs_invertmin, XPRS_INVERTMIN)
      Simplex: The minimum number of iterations between full inversions of the
      basis matrix. See the description of INVERTFREQ for details.

      Default: 3

lp:keepbasis (keepbasis, lp:xprs_keepbasis, XPRS_KEEPBASIS)
      Simplex: This determines whether the basis should be kept when
      reoptimizing a problem. The choice is between using a crash basis
      created at the beginning of simplex or using a basis from a previous
      solve (if such exists). By default, this control gets (re)set
      automatically in various situations. By default, it will be
      automatically set to 1 after a solve that produced a valid basis. This
      will automatically warmstart a subsequent solve. Explicitly loading a
      starting basis will also set this control to 1. If the control is
      explicitly set to 0, any existing basis will be ignored for a new solve,
      and the Optimizer will start from an ad-hoc crash basis.

      Values (default: 0):

      * (0) Problem optimization starts from scratch, i.e., any previous basis
        is ignored.

      * (1) The previous basis should be used as a starting basis.

      * (2) Use the previous basis only if it is valid for the current problem
        (the number of basic variables must match the number of rows).

      * (3) Use the previous basis only if it is valid and numerically stable
        in the current problem.

lp:keepnrows (keepnrows, prob:xprs_keepnrows, XPRS_KEEPNROWS)
      How nonbinding rows should be handled by the MPS reader.

      Values (default: -1):

      * (-1) Delete N type rows from the matrix.

      * (0) Delete elements from N type rows leaving empty N type rows in the
        matrix.

      * (1) Keep N type rows.

lp:log (lplog, lp:xprs_lplog, XPRS_LPLOG)
      Simplex: The frequency at which the simplex log is printed.

      Values (default: 100):

      * (n<0) Detailed output every -n iterations.

      * (0) Log displayed at the end of the optimization only.

      * (n>0) Summary output every n iterations.

lp:netstalllimit (netstalllimit, sim:xprs_netstalllimit, XPRS_NETSTALLLIMIT)
      Limit the number of degenerate pivots of the network simplex algorithm,
      before switching to either primal or dual simplex, depending on
      ALGAFTERNETWORK.

      Values (default: -1):

      * (-1) Automatically determined limit

      * (0) No limit.

      * (n>0) Limit to n network simplex iterations.

lp:optimalitytoltarget (optimalitytoltarget, sol:xprs_optimalitytoltarget, XPRS_OPTIMALITYTOLTARGET)
      This specifies the target optimality tolerance for the solution refiner.

      Default: 0 — use the value specified by OPTIMALITYTOL.

lp:opttol (lp:optimalitytol, opttol, optimalitytol, tol:xprs_optimalitytol, XPRS_OPTIMALITYTOL)
      Simplex: This is the zero tolerance for reduced costs. On each
      iteration, the simplex method searches for a variable to enter the basis
      which has a negative reduced cost. The candidates are only those
      variables which have reduced costs less than the negative value of
      OPTIMALITYTOL.

      Default: 1.0E-06

lp:penalty (penalty, pre:xprs_penalty, XPRS_PENALTY)
      Minimum absolute penalty variable coefficient. BIGM and PENALTY are set
      by the input routine (XPRSreadprob (READPROB)) but may be reset by the
      user prior to XPRSlpoptimize (LPOPTIMIZE).

      Default: Dependent on the matrix characteristics.

lp:pivtol (pivtol, markowitztol, lp:xprs_markowitztol, XPRS_MARKOWITZTOL)
      The Markowitz tolerance used for the factorization of the basis matrix.

      Default: 0.01

lp:pricingalg (pricingalg, lp:xprs_pricingalg, XPRS_PRICINGALG)
      Simplex: This determines the primal simplex pricing method. It is used
      to select which variable enters the basis on each iteration. In general
      Devex pricing requires more time on each iteration, but may reduce the
      total number of iterations, whereas partial pricing saves time on each
      iteration, but may result in more iterations.

      Values (default: 0):

      * (-1) Partial pricing.

      * (0) Determined automatically.

      * (1) Devex pricing.

      * (2) Steepest edge.

      * (3) Steepest edge with unit initial weights.

lp:primalunshift (primalunshift, lp:xprs_primalunshift, XPRS_PRIMALUNSHIFT)
      Determines whether primal is allowed to call dual to unshift.

      Values (default: 0):

      * (0) Allow the dual algorithm to be used to unshift.

      * (1) Don't allow the dual algorithm to be used to unshift.

lp:relpivottol (relpivottol, sim:xprs_relpivottol, XPRS_RELPIVOTTOL)
      Simplex: At each iteration a pivot element is chosen within a given
      column of the matrix. The relative pivot tolerance, RELPIVOTTOL, is the
      size of the element chosen relative to the largest possible pivot
      element in the same column.

      Default: 1.0E-06

lp:sifting (sifting, lp:xprs_sifting, XPRS_SIFTING)
      Determines whether to enable sifting algorithm with the dual simplex
      method.

      Values (default: -1):

      * (-1) Automatically determined.

      * (0) Disable sifting.

      * (1) Enable sifting.

lp:siftpasses (siftpasses, lp:xprs_siftpasses, XPRS_SIFTPASSES)
      Determines how quickly we allow to grow the worker problems during the
      sifting algorithm. Using larger values can increase the number of
      columns added to the worker problem which often results in increased
      solve times for the worker problems but the number of necessary sifting
      iterations may be reduced.

      Default: 4

lp:siftpresolveops (siftpresolveops, lp:xprs_siftpresolveops, XPRS_SIFTPRESOLVEOPS)
      Determines the presolve operations for solving the subproblems during
      the sifting algorithm.

      Values (default: -1):

      * (-1) Use the PRESOLVEOPS setting specified for the original problem.

      * (>=0) Use the value for the PRESOLVEOPS parameter for solving the
        subproblems during the sifting algorithm.

lp:siftswitch (siftswitch, lp:xprs_siftswitch, XPRS_SIFTSWITCH)
      Determines which algorithm to use for solving the subproblems during
      sifting.

      Values (default: -1):

      * (-1) Dual simplex.

      * (0) Barrier.

      * (>0) Use the barrier algorithm while the number of dual
        infeasibilities is larger than this value, otherwise use dual simplex.

lp:xprs_algafternetwork (XPRS_ALGAFTERNETWORK)
      The algorithm to be used for the clean up step after the network simplex
      solver.

      Values (default: -1):

      * (-1) Automatically determined.

      * (2) Dual simplex.

      * (3) Primal simplex.

lp:xprs_autoperturb (XPRS_AUTOPERTURB)
      Simplex: This indicates whether automatic perturbation is performed. If
      this is set to 1, the problem will be perturbed whenever the simplex
      method encounters an excessive number of degenerate pivot steps, thus
      preventing the Optimizer being hindered by degeneracies.

      Values (default: 1):

      * (0) No perturbation performed.

      * (1) Automatic perturbation is performed.

lp:xprs_lpflags (XPRS_LPFLAGS)
      A bit-vector control (see Section Bit-vector controls) which defines the
      algorithm for solving an LP problem or the initial LP relaxation of a
      MIP problem.

      Values (default: 0):

      * (0) Use the dual simplex method.

      * (1) Use the primal simplex method.

      * (2) Use the barrier method (or hybrid gradient method if BARALG=4 is
        set).

      * (3) Use the network simplex method.

lp:xprs_lplogdelay (XPRS_LPLOGDELAY)
      Time interval between two LP log lines.

      Default: 1.0

lp:xprs_lplogstyle (XPRS_LPLOGSTYLE)
      Simplex: The style of the simplex log.

      Values (default: 1):

      * (0) Simplex log is printed based on simplex iteration count, at a
        fixed frequency as specified by the LPLOG control.

      * (1) Simplex log is printed based on an estimation of elapsed time,
        determined by an internal deterministic timer.

lp:xprs_primalops (XPRS_PRIMALOPS)
      Primal simplex: allows fine tuning the variable selection in the primal
      simplex solver.

      Values (default: -1):

      * (0) Use aggressive dj scaling.

      * (1) Conventional dj scaling.

      * (2) Use reluctant switching back to partial pricing.

      * (3) Use dynamic switching between cheap and expensive pricing
        strategies.

      * (4) Keep solving even after potential cycling is detected.

lp:xprs_primalperturb (XPRS_PRIMALPERTURB)
      The factor by which the problem will be perturbed prior to optimization
      by primal simplex. A value of 0.0 results in no perturbation prior to
      optimization. Note the interconnection to the AUTOPERTURB control. If
      AUTOPERTURB is set to 1, the decision whether to perturb or not is left
      to the Optimizer. When the problem is automatically perturbed in primal
      simplex, however, the value of PRIMALPERTURB will be used for
      perturbation.

      Default: -1 — determined automatically.

mip:basis (fixmodel, mip:fix)
      Whether to compute duals / basis / sensitivity for MIP models:

      0 - No (default)
      1 - Yes.

mip:bestbound (bestbound, return_bound)
      Whether to return suffix .bestbound for the best known MIP dual bound on
      the objective value:

      0 - No (default)
      1 - Yes.

      The suffix is on the objective and problem and is -Infinity for
      minimization problems and +Infinity for maximization problems if there
      are no integer variables or if a dual bound is not available.

mip:branchchoice (branchchoice, mip:xprs_branchchoice, XPRS_BRANCHCHOICE)
      Once a MIP entity has been selected for branching, this control
      determines which of the branches is solved first.

      Values (default: 0):

      * (0) Minimum estimate branch first.

      * (1) Maximum estimate branch first.

      * (2) If an incumbent solution exists, solve the branch satisfied by
        that solution first. Otherwise solve the minimum estimate branch first
        (option 0).

      * (3) Solve first the branch that forces the value of the branching
        variable to move farther away from the value it had at the root node.
        If the branching entity is not a simple variable, solve the minimum
        estimate branch first (option 0).

mip:branchdisj (branchdisj, mip:xprs_branchdisj, XPRS_BRANCHDISJ)
      Branch and Bound: Determines whether the optimizer should attempt to
      branch on general split disjunctions during the branch and bound search.

      Values (default: -1):

      * (-1) Automatic selection of the strategy.

      * (0) Disabled.

      * (1) Cautious strategy. Disjunctive branches will be created only for
        general integers with a wide range.

      * (2) Moderate strategy.

      * (3) Aggressive strategy. Disjunctive branches will be created for both
        binaries and integers.

mip:branchstructural (branchstructural, branchstruct, mip:xprs_branchstructural, XPRS_BRANCHSTRUCTURAL)
      Branch and Bound: Determines whether the optimizer should search for
      special structure in the problem to branch on during the branch and
      bound search.

      Values (default: -1):

      * (-1) Automatically determined.

      * (0) Disabled.

      * (1) Enabled.

mip:breadthfirst (breadthfirst, mip:xprs_breadthfirst, XPRS_BREADTHFIRST)
      The number of nodes to include in the best-first search before switching
      to the local first search (NODESELECTION=4).

      Default: 11

mip:components (mipcomponents, mip:xprs_mipcomponents, XPRS_MIPCOMPONENTS)
      Determines whether disconnected components in a MIP should be solved as
      separate MIPs. There can be significant performence benefits from
      solving disconnected components individual instead of being part of the
      main branch-and-bound search.

      Values (default: -1 ):

      * (-1) Automatic - let the solver decide.

      * (0) Disable solving disconnected components separately.

      * (1) Solve disconnected components separately.

mip:concurrentnodes (mipconcurrentnodes, mip:xprs_mipconcurrentnodes, XPRS_MIPCONCURRENTNODES)
      Sets the node limit for when a winning solve is selected when concurrent
      MIP solves are enabled. When multiple MIP solves are started, they each
      run up to the MIPCONCURRENTNODES node limit and only one winning solve
      is selected for contuinuing the search with.

      Values (default: -1 ):

      * (-1) Automatic - let the solver decide on a node limit.

      * (>0) Number of nodes each concurrent solve should complete before a
        winner is selected.

mip:concurrentsolves (mipconcurrentsolves, mip:xprs_mipconcurrentsolves, XPRS_MIPCONCURRENTSOLVES)
      Selects the number of concurrent solves to start for a MIP. Each solve
      will use a unique random seed for its random number generator, but will
      otherwise apply the same user controls. The first concurrent solve to
      complete will have solved the MIP and all the concurrent solves will be
      terminated at this point. Using concurrent solves can be advantageous
      when a MIP displays a high level of performance variability.

      Values (default: 0 ):

      * (-1) Enabled. The number of concurrent solves depends on MIPTHREADS.

      * (0, 1) Disabled

      * (n>1) Enabled. The number of concurrent solves to start is given by n.

mip:deterministic (deterministic, tech:xprs_deterministic, XPRS_DETERMINISTIC)
      Selects whether to use a deterministic or opportunistic mode when
      solving a problem using multiple threads.

      Values (default: 1):

      * (0) Use opportunistic mode.

      * (1) Use deterministic mode.

      * (2) Use deterministic mode, except allow the initial concurrent
        continuous solve of a MIP to be opportunistic.

mip:dualreductions (mipdualreductions, pre:xprs_mipdualreductions, XPRS_MIPDUALREDUCTIONS)
      Branch and Bound: Limits operations that can reduce the MIP solution
      space.

      Values (default: 1):

      * (2) Allow dual reductions on continuous variables only.

      * (1) Allow all dual reductions.

      * (0) Prevent all dual reductions.

mip:feasibilityjump (feasibilityjump, heur:xprs_feasibilityjump, XPRS_FEASIBILITYJUMP)
      MIP: Decides if the Feasibility Jump heuristic should be run. The value
      for this control is either -1 (let Xpress decide), 0 (off) or a value
      that indicates for which type of models the heuristic should be run.

      Values (default: -1):

      * (-1) Use automatic settings.

      * (0) Turned off.

      * (1) Run the heuristic on models with all integer variables.

      * (2) Run the heuristic on models in which all non-integer variables
        have bounds [0,1].

      * (3) Run the heuristic on models in which all non-integer variables
        have integer bounds.

mip:feasibilitypump (feasibilitypump, heur:xprs_feasibilitypump, XPRS_FEASIBILITYPUMP)
      Branch and Bound: Decides if the Feasibility Pump heuristic should be
      run at the root node.

      Values (default: -1):

      * (-1) Automatic.

      * (0) Turned off.

      * (1) Always try the Feasibility Pump.

      * (2) Try the Feasibility Pump only if other heuristics have failed to
        find an integer solution.

mip:gap (mipgap, lim:xprs_miprelstop, XPRS_MIPRELSTOP)
      Branch and Bound: This determines when the branch and bound tree search
      will terminate. Branch and bound tree search will stop if: |MIPOBJVAL -
      BESTBOUND| ≤ MIPRELSTOP x max(|BESTBOUND|,|MIPOBJVAL|) where MIPOBJVAL
      is the value of the best solution's objective function and BESTBOUND is
      the current best solution bound. For example, to stop the tree search
      when a MIP solution has been found and the Optimizer can guarantee it is
      within 5% of the optimal solution, set MIPRELSTOP to 0.05.

      Default: 0.0001

mip:gapabs (mipgapabs, lim:xprs_mipabsstop, XPRS_MIPABSSTOP)
      Branch and Bound: The absolute tolerance determining whether the tree
      search will continue or not. It will terminate if |MIPOBJVAL -
      BESTBOUND| ≤ MIPABSSTOP where MIPOBJVAL is the value of the best
      solution's objective function, and BESTBOUND is the current best
      solution bound. For example, to stop the tree search when a MIP solution
      has been found and the Optimizer can guarantee it is within 100 of the
      optimal solution, set MIPABSSTOP to 100.

      Default: 0.0

mip:heurbeforelp (heurbeforelp, heur:xprs_heurbeforelp, XPRS_HEURBEFORELP)
      Branch and Bound: Determines whether primal heuristics should be run
      before the initial LP relaxation has been solved.

      Values (default: -1):

      * (-1) Automatic - let the optimizer decide if heuristics should be run.

      * (0) Disabled.

      * (1) Enabled.

mip:heurdiverandomize (hdive_rand, heurdiverandomize, heur:xprs_heurdiverandomize, XPRS_HEURDIVERANDOMIZE)
      The level of randomization to apply in the diving heuristic. The diving
      heuristic uses priority weights on rows and columns to determine the
      order in which to e.g. round fractional columns, or the direction in
      which to round them. This control determines by how large a random
      factor these weights should be changed.

      Values (default: 0.0):

      * (0.0-1.0) Amount of randomization (0.0=none, 1.0=full)

mip:heurdivesoftrounding (hdive_rounding, heurdivesoftrounding, heur:xprs_heurdivesoftrounding, XPRS_HEURDIVESOFTROUNDING)
      Branch and Bound: Enables a more cautious strategy for the diving
      heuristic, where it tries to push binaries and integer variables to
      their bounds using the objective, instead of directly fixing them. This
      can be useful when the default diving heuristics fail to find any
      feasible solutions.

      Values (default: -1):

      * (-1) Automatic selection.

      * (0) Do not use soft rounding.

      * (1) Cautious use of the soft rounding strategy.

      * (2) More aggressive use of the soft rounding strategy.

mip:heurdivespeedup (hdive_speed, heurdivespeedup, heur:xprs_heurdivespeedup, XPRS_HEURDIVESPEEDUP)
      Branch and Bound: Changes the emphasis of the diving heuristic from
      solution quality to diving speed.

      Values (default: -1):

      * (-2) Automatic selection biased towards quality

      * (-1) Automatic selection biased towards speed.

      * (0-4) manual emphasis bias from emphasis on quality (0) to emphasis on
        speed (4).

mip:heurdivestrategy (hdive_strategy, heurdivestrategy, heur:xprs_heurdivestrategy, XPRS_HEURDIVESTRATEGY)
      Branch and Bound: Chooses the strategy for the diving heuristic.

      Values (default: -1):

      * (-1) Automatic selection of strategy.

      * (0) Disables the diving heuristic.

      * (1-18) Available pre-set strategies for rounding infeasible MIP
        entities and reoptimizing during the heuristic dive.

mip:heuremphasis (heuremphasis, heur:xprs_heuremphasis, XPRS_HEUREMPHASIS)
      Branch and Bound: This control specifies an emphasis for the search
      w.r.t. primal heuristics and other procedures that affect the speed of
      convergence of the primal-dual gap. For problems where the goal is to
      achieve a small gap but not neccessarily solving them to optimality, it
      is recommended to set HEUREMPHASIS to 1. This setting triggers many
      additional heuristic calls, aiming for reducing the gap at the beginning
      of the search, typically at the expense of an increased time for proving
      optimality.

      Values (default: -1):

      * (-1) Optimizer default strategy.

      * (0) Disables all heuristics.

      * (1) Focus on reducing the primal-dual gap in the early part of the
        search.

      * (2) Extremely aggressive search heuristics.

mip:heurforcespecialobj (heurforcespecobj, heurforcespecialobj, heur:xprs_heurforcespecialobj, XPRS_HEURFORCESPECIALOBJ)
      Branch and Bound: This specifies whether local search heuristics without
      objective or with an auxiliary objective should always be used, despite
      the automatic selection of the Optimiezr. Deactivated by default.

      Values (default: 0):

      * (0) Disabled.

      * (1) Enabled. Run special objective heuristics on large problems and
        even if incumbent exists.

mip:heurfreq (heurfreq, heur:xprs_heurfreq, XPRS_HEURFREQ)
      Branch and Bound: This specifies the frequency at which heuristics are
      used in the tree search. Heuristics will only be used at a node if the
      depth of the node is a multiple of HEURFREQ.

      Default: -1

mip:heursearcheffort (heursearcheffort, heur:xprs_heursearcheffort, XPRS_HEURSEARCHEFFORT)
      Adjusts the overall level of the local search heuristics.

      Default: 1.0

mip:heursearchfreq (heurfreq, heursearchfreq, heur:xprs_heursearchfreq, XPRS_HEURSEARCHFREQ)
      Branch and Bound: This specifies how often the local search heuristic
      should be run in the tree.

      Values (default: -1):

      * (-1) Automatic.

      * (0) Disabled in the tree.

      * (n>0) Number of nodes between each run.

mip:heursearchrootcutfreq (heurrootcutfreq, heursearchrootcutfreq, heur:xprs_heursearchrootcutfreq, XPRS_HEURSEARCHROOTCUTFREQ)
      How frequently to run the local search heuristic during root cutting.
      This is given as how many cut rounds to perform between runs of the
      heuristic. Set to zero to avoid applying the heuristic during root
      cutting. Branch and Bound: This specifies how often the local search
      heuristic should be run in the tree.

      Values (default: -1):

      * (-1) Automatic.

      * (0) Disabled heuristic during cutting.

      * (n>0) Number of cutting rounds between each run.

mip:heursearchrootselect (heursearchrootselect, heur:xprs_heursearchrootselect, XPRS_HEURSEARCHROOTSELECT)
      A bit-vector control (see Section Bit-vector controls) for selecting
      which local search heuristics to apply on the root node of a MIP solve.
      Use HEURSEARCHTREESELECT to control local search heuristics during the
      tree search.

      Values (default: 117):

      * (0) Local search with a large neighborhood. Potentially slow but is
        good for finding solutions that differs significantly from the
        incumbent.

      * (1) Local search with a small neighborhood centered around a node LP
        solution.

      * (2) Local search with a small neighborhood centered around an integer
        solution. This heuristic will often provide smaller, incremental
        improvements to an incumbent solution.

      * (3) Local search with a neighborhood set up through the combination of
        multiple integer solutions.

      * (4) Unused

      * (5) Local search without an objective function. Called seldom and only
        when no feasible solution is available.

      * (6) Local search with an auxiliary objective function. Called seldom
        and only when no feasible solution is available.

mip:heursearchtreeselect (heursearchtreeselect, heur:xprs_heursearchtreeselect, XPRS_HEURSEARCHTREESELECT)
      A bit-vector control (see Section Bit-vector controls) for selecting
      which local search heuristics to apply during the tree search of a MIP
      solve. Use HEURSEARCHROOTSELECT to control local search heuristics on
      the root node.

      Values (default: 17):

      * (0) Local search with a large neighborhood. Potentially slow but is
        good for finding solutions that differs significantly from the
        incumbent.

      * (1) Local search with a small neighborhood centered around a node LP
        solution.

      * (2) Local search with a small neighborhood centered around an integer
        solution. This heuristic will often provide smaller, incremental
        improvements to an incumbent solution.

      * (3) Local search with a neighborhood set up through the combination of
        multiple integer solutions.

      * (4) Unused

      * (5) Local search without an objective function. Called seldom and only
        when no feasible solution is available.

      * (6) Local search with an auxiliary objective function. Called seldom
        and only when no feasible solution is available.

mip:heurshiftprop (heurshiftprop, heur:xprs_heurshiftprop, XPRS_HEURSHIFTPROP)
      Determines whether the Shift-and-propagate primal heuristic should be
      executed. If enabled, Shift-and-propagate is an LP-free primal heuristic
      that is executed immediately after presolve.

      Values (default: -1):

      * (-1) The solver decides if Shift-and-propagate should be run. This is
        the default setting.

      * (0) Shift-and-propagate is disabled.

      * (1) Shift-and-propagate is enabled.

mip:heurthreads (heurthreads, heur:xprs_heurthreads, XPRS_HEURTHREADS)
      Branch and Bound: The number of threads to dedicate to running
      heuristics during the root solve.

      Values (default: 0):

      * (-1) Automatically determined from the THREADS control.

      * (0) Disabled.

      * (>=1) Number of additional threads to dedicate to parallel heuristics.

mip:historycosts (historycosts, mip:xprs_historycosts, XPRS_HISTORYCOSTS)
      Branch and Bound: How to update the pseudo cost for a MIP entity when a
      strong branch or a regular branch is applied.

      Values (default: -1):

      * (-1) Automatically determined.

      * (0) No update.

      * (1) Update using only regular branches from the root to the current
        node.

      * (2) Same as 1, but update with strong branching results as well.

      * (3) Update using any regular branching or strong branching information
        from all nodes solves before the current node.

mip:intfeastol (inttol, intfeastol, tol:xprs_miptol, XPRS_MIPTOL)
      Branch and Bound: This is the tolerance within which a decision
      variable's value is considered to be integral.

      Default: 5.0E-06

mip:kappafreq (mipkappafreq, mip:xprs_mipkappafreq, XPRS_MIPKAPPAFREQ)
      Branch and Bound: Specifies how frequently the basis condition number
      (also known as kappa) should be calculated during the branch-and-bound
      search.

      Values (default: 0):

      * (0) Do not calculate condition numbers.

      * (1) Calculate conditions numbers on every node, including after each
        round of root cutting.

      * (n>1) Calculate a condition number once per node of every n'th level
        of the branch-and-bound tree.

mip:localchoice (localchoice, mip:xprs_localchoice, XPRS_LOCALCHOICE)
      Controls when to perform a local backtrack between the two child nodes
      during a dive in the branch and bound tree.

      Values (default: 3):

      * (1) Never backtrack from the first child, unless it is dropped
        (infeasible or cut off).

      * (2) Always solve both child nodes before deciding which child to
        continue with.

      * (3) Automatically determined.

mip:log (miplog, log:xprs_miplog, XPRS_MIPLOG)
      MIP log print control.

      Values (default: -100):

      * (-n) Print out summary log at each nth node.

      * (0) No printout during MIP tree search.

      * (1) Only print out summary statement at the end.

      * (2) Print out detailed log at all solutions found.

      * (3) Print out detailed log at each node.

mip:maxlocalbacktrack (maxlocalbacktrack, maxlocalbt, mip:xprs_maxlocalbacktrack, XPRS_MAXLOCALBACKTRACK)
      Branch-and-Bound: How far back up the current dive path the optimizer is
      allowed to look for a local backtrack candidate node.

      Values (default: -1):

      * (-1) Automatic.

      * (n>0) Local backtrack limit.

mip:maxtasks (maxmiptasks, tech:xprs_maxmiptasks, XPRS_MAXMIPTASKS)
      Branch-and-Bound: The maximum number of tasks to run in parallel during
      a MIP solve.

      Values (default: -1):

      * (-1) Task limit determined automatically from MIPTHREADS.

      * (>0) Fixed task limit.

mip:miprefineiterlimit (miprefiterlim, miprefineiterlimit, sol:xprs_miprefineiterlimit, XPRS_MIPREFINEITERLIMIT)
      This defines an effort limit expressed as simplex iterations for the MIP
      solution refiner. The limit is per reoptimizations in the MIP refiner.

      Default: -1 — determined automatically.

mip:nodeprobingeffort (nodeprobingeffort, pre:xprs_nodeprobingeffort, XPRS_NODEPROBINGEFFORT)
      Adjusts the overall level of node probing.

      Default: 1.0

mip:nodeselection (nodeselection, mip:xprs_nodeselection, XPRS_NODESELECTION)
      Branch and Bound: This determines which nodes will be considered for
      solution once the current node has been solved.

      Values (default: Dependent on the matrix characteristics.):

      * (1) Local first: Choose between descendant and sibling nodes if
        available; choose from all outstanding nodes otherwise.

      * (2) Best first: Choose from all outstanding nodes.

      * (3) Local depth first: Choose between descendant and sibling nodes if
        available; choose from the deepest nodes otherwise.

      * (4) Best first, then local first: Best first is used for the first
        BREADTHFIRST nodes, after which local first is used.

      * (5) Pure depth first: Choose from the deepest outstanding nodes.

mip:presolve (mippresolve, pre:xprs_mippresolve, XPRS_MIPPRESOLVE)
      Branch and Bound: Type of integer processing to be performed. If set to
      0, no processing will be performed. This is a bit-vector control (see
      Section Bit-vector controls).

      Values (default: -1):

      * (0) Reduced cost fixing will be performed at each node. This can
        simplify the node before it is solved, by deducing that certain
        variables' values can be fixed based on additional bounds imposed on
        other variables at this node.

      * (1) Primal reductions will be performed at each node. Uses constraints
        of the node to tighten the range of variables, often resulting in
        fixing their values. This greatly simplifies the problem and may even
        determine optimality or infeasibility of the node before the simplex
        method commences.

      * (2) [Unused] This bit is no longer used to control probing. Refer to
        the integer control PREPROBING for setting probing level during
        presolve.

      * (3) If node preprocessing is allowed to change bounds on continuous
        columns.

      * (4) Dual reductions will be performed at each node.

      * (5) Allow global (non-bound) tightening of the problem during the tree
        search.

      * (6) The objective function will be used to find reductions at each
        node.

      * (7) [Unused] This bit is no longer used to control restarts. Refer to
        the integer control MIPRESTART for disabling tree restarts.

      * (8) Allow that symmetry is used to presolve the node problem.

mip:pseudocost (pseudocost, mip:xprs_pseudocost, XPRS_PSEUDOCOST)
      Branch and Bound: The default pseudo cost used in estimation of the
      degradation associated with an unexplored node in the tree search. A
      pseudo cost is associated with each integer decision variable and is an
      estimate of the amount by which the objective function will be worse if
      that variable is forced to an integral value.

      Default: 0.01

mip:qcrootalg (qcrootalg, qp:xprs_qcrootalg, XPRS_QCROOTALG)
      This control determines which algorithm is to be used to solve the root
      of a mixed integer quadratic constrained or mixed integer second order
      cone problem, when outer approximation is used.

      Values (default: -1):

      * (-1) Determined automatically.

      * (0) Use the barrier algorithm.

      * (1) Use the dual simplex on a relaxation of the problem constructed
        using outer approximation.

mip:rampup (miprampup, mip:xprs_miprampup, XPRS_MIPRAMPUP)
      Controls the strategy used by the parallel MIP solver during the ramp-up
      phase of a branch-and-bound tree search.

      Values (default: -1):

      * (-1) Automatically determined.

      * (0) No special treatment during the ramp-up phase. Always run with the
        maximal number of tasks.

      * (1) Limit the number of tasks until the initial dives have completed.

mip:relaxtreememorylimit (relaxtreemem, relaxtreememorylimit, tech:xprs_relaxtreememorylimit, XPRS_RELAXTREEMEMORYLIMIT)
      When the memory used by the branch and bound search tree exceeds the
      target specified by the TREEMEMORYLIMIT control, the optimizer will try
      to reduce this by writing nodes to the tree file. In rare cases, usually
      where the solve has many millions of very small nodes, the tree
      structural data (which cannot be written to the tree file) will grow
      large enough to approach or exceed the tree's memory target. When this
      happens, optimizer performance can degrade greatly as the solver makes
      heavy use of the tree file in preference to memory. To prevent this, the
      solver will automatically relax the tree memory limit when it detects
      this case; the RELAXTREEMEMORYLIMIT control specifies the proportion of
      the previous memory limit by which to relax it. Set RELAXTREEMEMORYLIMIT
      to 0.0 to force the Xpress Optimizer to never relax the tree memory
      limit in this way.

      Default: 0.1

mip:restart (miprestart, mip:xprs_miprestart, XPRS_MIPRESTART)
      Branch and Bound: controls strategy for in-tree restarts.

      Values (default: -1):

      * (-1) Determined automatically (XPRS_MIPRESTART_DEFAULT).

      * (0) Disable in-tree restarts (XPRS_MIPRESTART_OFF).

      * (1) Allow in-tree restarts at normal aggressiveness
        (XPRS_MIPRESTART_MODERATE).

      * (2) Allow in-tree restarts at higher aggressiveness (more likely to
        trigger a restart) (XPRS_MIPRESTART_AGGRESSIVE).

mip:restartfactor (miprestartfactor, mip:xprs_miprestartfactor, XPRS_MIPRESTARTFACTOR)
      Branch and Bound: Fine tune initial conditions to trigger an in-tree
      restart. Use a value > 1 to increase the aggressiveness with which the
      Optimizer restarts. Use a value < 1 to relax the aggressiveness with
      which the Optimizer restarts. Note that this control does not affect the
      initial condition on the gap, which must be set separately.

      Default: 1.0

mip:restartgapthreshold (miprestartgapthreshold, mip:xprs_miprestartgapthreshold, XPRS_MIPRESTARTGAPTHRESHOLD)
      Branch and Bound: Initial gap threshold to delay in-tree restart. The
      restart is delayed initially if the gap, given as a fraction between 0
      and 1, is below this threshold. The optimizer adjusts the threshold
      every time a restart is delayed. Note that there are other criteria that
      can delay or prevent a restart.

      Default: 0.02

mip:return_gap (return_mipgap)
      Whether to return mipgap suffixes or include mipgap values (|objectve -
      .bestbound|) in the solve_message: sum of

      1 - Return .relmipgap suffix (relative to |obj|)
      2 - Return .absmipgap suffix (absolute mipgap)
      4 - Suppress mipgap values in solve_message.

      Default = 0. The suffixes are on the objective and problem. Returned
      suffix values are +Infinity if no integer-feasible solution has been
      found, in which case no mipgap values are reported in the solve_message.

mip:round (round)
      Whether to round integer variables to integral values before returning
      the solution, and whether to report that the solver returned noninteger
      values for integer values: sum of

      1 ==> Round nonintegral integer variables
      2 ==> Modify solve_result
      4 ==> Modify solve_message

      Default = 0. Modifications that were or would be made are reported in
      solve_result and solve_message only if the maximum deviation from
      integrality exceeded mip:round_reptol.

mip:round_reptol (round_reptol)
      Tolerance for reporting rounding of integer variables to integer values;
      see "mip:round". Default = 1e-9.

mip:sbbest (sbbest, mip:xprs_sbbest, XPRS_SBBEST)
      Number of infeasible MIP entities to initialize pseudo costs for on each
      node.

      Values (default: -1):

      * (-1) determined automatically.

      * (0) disable strong branching.

      * (n>0) perform strong branching on up to n entities at each node.

mip:sbeffort (sbeffort, mip:xprs_sbeffort, XPRS_SBEFFORT)
      Adjusts the overall amount of effort when using strong branching to
      select an infeasible MIP entity to branch on.

      Default: 1.0

mip:sbestimate (sbestimate, mip:xprs_sbestimate, XPRS_SBESTIMATE)
      Branch and Bound: How to calculate pseudo costs from the local node when
      selecting an infeasible MIP entity to branch on. These pseudo costs are
      used in combination with local strong branching and history costs to
      select the branch candidate.

      Values (default: -1):

      * (-1) Automatically determined.

      * (1-6) Different variants of local pseudo costs.

mip:sbiterlimit (sbiterlimit, mip:xprs_sbiterlimit, XPRS_SBITERLIMIT)
      Number of dual iterations to perform the strong branching for each
      entity.

      Default: -1 — determined automatically.

mip:sbselect (sbselect, mip:xprs_sbselect, XPRS_SBSELECT)
      The size of the candidate list of MIP entities for strong branching.

      Values (default: -2):

      * (-2) Automatic (low effort).

      * (-1) Automatic (high effort).

      * (n>=0) Include n entities in the candidate list (but always at least
        SBBEST candidates).

mip:symmetry (symmetry, pre:xprs_symmetry, XPRS_SYMMETRY)
      Adjusts the overall amount of effort for symmetry detection.

      Values (default: 1):

      * (0) No symmetry detection.

      * (1) Conservative effort.

      * (2) Intensive symmetry search.

mip:symselect (symselect, pre:xprs_symselect, XPRS_SYMSELECT)
      Adjusts the overall amount of effort for symmetry detection.

      Values (default: -1):

      * (0) Search the whole matrix (otherwise the 0, 1 and -1 coefficients
        only).

      * (1) Search all entities (otherwise binaries only).

mip:threads (mipthreads, mip:xprs_mipthreads, XPRS_MIPTHREADS)
      If set to a positive integer it determines the number of threads
      implemented to run the parallel MIP code. If MIPTHREADS is set to the
      default value (-1), the THREADS control will determine the number of
      threads used.

      Default: -1 (determined by the THREADS control)

mip:toltarget (miptoltarget, sol:xprs_miptoltarget, XPRS_MIPTOLTARGET)
      Target MIPTOL value used by the automatic MIP solution refiner as
      defined by REFINEOPS. Negative and zero values are ignored.

      Default: 0.0

mip:varselection (varselection, mip:xprs_varselection, XPRS_VARSELECTION)
      Branch and Bound: This determines the formula used to calculate the
      estimate of each integer variable, and thus which integer variable is
      selected to be branched on at a given node. The variable selected to be
      branched on is the one with the maximum estimate.

      Values (default: -1):

      * (-1) Determined automatically.

      * (1) The minimum of the 'up' and 'down' pseudo costs.

      * (2) The 'up' pseudo cost plus the 'down' pseudo cost.

      * (3) The maximum of the 'up' and 'down' pseudo costs, plus twice the
        minimum of the 'up' and 'down' pseudo costs.

      * (4) The maximum of the 'up' and 'down' pseudo costs.

      * (5) The 'down' pseudo cost.

      * (6) The 'up' pseudo cost.

      * (7) A weighted combination of the 'up' and 'down' pseudo costs, where
        the weights depend on how fractional the variable is.

      * (8) The product of the 'up' and 'down' pseudo costs.

mip:xprs_backtrack (XPRS_BACKTRACK)
      Branch and Bound: Specifies how to select the next node to work on when
      a full backtrack is performed.

      Values (default: 3):

      * (-1) Automatically determined.

      * (1) Unused.

      * (2) Select the node with the best estimated solution.

      * (3) Select the node with the best bound on the solution.

      * (4) Select the deepest node in the search tree (equivalent to
        depth-first search).

      * (5) Select the highest node in the search tree (equivalent to
        breadth-first search).

      * (6) Select the earliest node created.

      * (7) Select the latest node created.

      * (8) Select a node randomly.

      * (9) Select the node whose LP relaxation contains the fewest number of
        infeasible MIP entities.

      * (10) Combination of 2 and 9.

      * (11) Combination of 2 and 4.

      * (12) Combination of 3 and 4.

mip:xprs_backtracktie (XPRS_BACKTRACKTIE)
      Branch and Bound: Specifies how to break ties when selecting the next
      node to work on when a full backtrack is performed. The options are the
      same as for the BACKTRACK control.

      Values (default: -1):

      * (-1) Default selection.

      * (1) Unused.

      * (2) Select the node with the best estimated solution.

      * (3) Select the node with the best bound on the solution.

      * (4) Select the deepest node in the search tree (equivalent to
        depth-first search).

      * (5) Select the highest node in the search tree (equivalent to
        breadth-first search).

      * (6) Select the earliest node created.

      * (7) Select the latest node created.

      * (8) Select a node randomly.

      * (9) Select the node whose LP relaxation contains the fewest number of
        infeasible MIP entities.

      * (10) Combination of 2 and 9.

      * (11) Combination of 2 and 4.

      * (12) Combination of 3 and 4.

mip:xprs_conflictcuts (XPRS_CONFLICTCUTS)
      Branch and Bound: Specifies how cautious or aggressive the optimizer
      should be when searching for and applying conflict cuts. Conflict cuts
      are in-tree cuts derived from nodes found to be infeasible or cut off,
      which can be used to cut off other branches of the search tree.

      Values (default: -1):

      * (-1) Automatic.

      * (0) Disable conflict cuts.

      * (1) Cautious application of conflict cuts.

      * (2) Medium application of conflict cuts.

      * (3) Aggressive application of conflict cuts.

mip:xprs_mipfracreduce (XPRS_MIPFRACREDUCE)
      Branch and Bound: Specifies how often the optimizer should run a
      heuristic to reduce the number of fractional integer variables in the
      node LP solutions.

      Values (default: -1):

      * (-1) Automatic.

      * (0) Disabled.

      * (1) Run before and after cutting on the root node.

      * (2) Run also during root cutting.

      * (3) Run also during the tree search.

mip:xprs_mipterminationmethod (XPRS_MIPTERMINATIONMETHOD)
      Branch and Bound: How a MIP solve should be stopped on early termination
      when there are still active tasks in the system. This can happen when,
      for example, a time or node limit is reached.

      Values (default: 0):

      * (0) Terminate tasks at the earliest opportunity. This can result in
        some unfinished node solves being discarded, although never integer
        solutions.

      * (1) Allow tasks to complete their current work but prevent new tasks
        from being started.

mip:xprs_mutexcallbacks (XPRS_MUTEXCALLBACKS)
      Branch and Bound: This determines whether the callback routines are
      mutexed from within the optimizer.

      Values (default: 1):

      * (0) Callbacks are not mutexed.

      * (1) Callbacks are mutexed.

mip:xprs_treecompression (XPRS_TREECOMPRESSION)
      When writing nodes to the gloal file, the optimizer can try to use
      data-compression techniques to reduce the size of the tree file on disk.
      The TREECOMPRESSION control determines the strength of the
      data-compression algorithm used; higher values give superior
      data-compression at the affect of decreasing performance, while lower
      values compress quicker but not as effectively. Where TREECOMPRESSION is
      set to 0, no data compression will be used on the tree file.

      Default: 2

mip:xprs_treediagnostics (XPRS_TREEDIAGNOSTICS)
      A bit-vector (see Section Bit-vector controls) providing control over
      how various tree-management-related messages get printed in the tree log
      file during the branch-and-bound search.

      Values (default: 7):

      * (0) Output regular summaries of current tree memory usage.

      * (1) Output messages whenever tree data is being written to tree file.

      * (2) Output progress messages while tree data is being written to the
        tree file, at an interval controlled by the TREEFILELOGINTERVAL
        control.

mip:xprs_treememorysavingtarget (XPRS_TREEMEMORYSAVINGTARGET)
      When the memory used by the branch-and-bound search tree exceeds the
      limit specified by the TREEMEMORYLIMIT control, the optimizer will try
      to save memory by writing lower-rated sections of the tree to the tree
      file. The target amount of memory to save will be enough to bring memory
      usage back below the limit, plus enough extra to give the tree room to
      grow. The TREEMEMORYSAVINGTARGET control specifies the extra proportion
      of the tree's size to try to save; for example, if the tree memory limit
      is 1000Mb and TREEMEMORYSAVINGTARGET is 0.1, when the tree size exceeds
      1000Mb the optimizer will try to reduce the tree size to 900Mb. Reducing
      the value of TREEMEMORYSAVINGTARGET will cause less extra nodes of the
      tree to be written to the tree file, but will result in the memory
      saving routine being triggered more often (as the tree will have less
      room in which to grow), which can reduce performance. Increasing the
      value of TREEMEMORYSAVINGTARGET will cause additional, more highly-rated
      nodes, of the tree to be written to the tree file, which can cause
      performance issues if these nodes are required later in the solve.

      Default: 0.4

mislp:xslp_mipalgorithm (XSLP_MIPALGORITHM, SLPMIPALGORITHM)
      Bitmap describing the MISLP algorithms to be used

      Values (default: 17 (bits 0 and4 are set)):

      * (0) Solve initial SLP to convergence.

      * (2) Relax step bounds according to XSLP_MIPRELAXSTEPBOUNDS after
        initial node.

      * (3) Fix step bounds according to XSLP_MIPFIXSTEPBOUNDS after initial
        node.

      * (4) Relax step bounds according to XSLP_MIPRELAXSTEPBOUNDS at each
        node.

      * (5) Fix step bounds according to XSLP_MIPFIXSTEPBOUNDS at each node.

      * (6) Limit iterations at each node to XSLP_MIPITERLIMIT.

      * (7) Relax step bounds according to XSLP_MIPRELAXSTEPBOUNDS after MIP
        solution is found.

      * (8) Fix step bounds according to XSLP_MIPFIXSTEPBOUNDS after MIP
        solution is found.

      * (9) Use MIP at each SLP iteration instead of SLP at each node.

      * (10) Use MIP on converged SLP solution and then SLP on the resulting
        MIP solution.

mislp:xslp_mipcutoff_a (XSLP_MIPCUTOFF_A, SLPMIPCUTOFF_A)
      Absolute objective function cutoff for MIP termination

      Default: 0.00001

mislp:xslp_mipcutoff_r (XSLP_MIPCUTOFF_R, SLPMIPCUTOFF_R)
      Absolute objective function cutoff for MIP termination

      Default: 0.00001

mislp:xslp_mipcutoffcount (XSLP_MIPCUTOFFCOUNT, SLPMIPCUTOFFCOUNT)
      Number of SLP iterations to check when considering a node for cutting
      off

      Default: 5

mislp:xslp_mipcutofflimit (XSLP_MIPCUTOFFLIMIT, SLPMIPCUTOFFLIMIT)
      Number of SLP iterations to check when considering a node for cutting
      off

      Default: 10

mislp:xslp_mipdefaultalgorithm (XSLP_MIPDEFAULTALGORITHM, SLPMIPDEFAULTALGORITHM)
      Default algorithm to be used during the tree search in MISLP

      Default: 3

mislp:xslp_miperrortol_a (XSLP_MIPERRORTOL_A, SLPMIPERRORTOL_A)
      Absolute penalty error cost tolerance for MIP cut-off

      Default: 0 (inactive)

mislp:xslp_miperrortol_r (XSLP_MIPERRORTOL_R, SLPMIPERRORTOL_R)
      Relative penalty error cost tolerance for MIP cut-off

      Default: 0 (inactive)

mislp:xslp_mipfixstepbounds (XSLP_MIPFIXSTEPBOUNDS, SLPMIPFIXSTEPBOUNDS)
      Bitmap describing the step-bound fixing strategy during MISLP

      Values (default: 0):

      * (0) Fix step bounds on structural SLP variables which are not in
        coefficients.

      * (1) Fix step bounds on all structural SLP variables.

      * (2) Fix step bounds on SLP variables appearing only in coefficients.

      * (3) Fix step bounds on SLP variables appearing in coefficients.

mislp:xslp_mipiterlimit (XSLP_MIPITERLIMIT, SLPMIPITERLIMIT)
      Maximum number of SLP iterations at each node

      Default: 0

mislp:xslp_miplog (XSLP_MIPLOG, SLPMIPLOG)
      Frequency with which MIP status is printed

      Default: 0 (deterministic logging)

mislp:xslp_mipocount (XSLP_MIPOCOUNT, SLPMIPOCOUNT)
      Number of SLP iterations at each node over which to measure objective
      function variation

      Default: 5

mislp:xslp_mipotol_a (XSLP_MIPOTOL_A, SLPMIPOTOL_A)
      Absolute objective function tolerance for MIP termination

      Default: 0.00001

mislp:xslp_mipotol_r (XSLP_MIPOTOL_R, SLPMIPOTOL_R)
      Relative objective function tolerance for MIP termination

      Default: 0.00001

mislp:xslp_miprelaxstepbounds (XSLP_MIPRELAXSTEPBOUNDS, SLPMIPRELAXSTEPBOUNDS)
      Bitmap describing the step-bound relaxation strategy during MISLP

      Values (default: 15 (relax all types)):

      * (0) Relax step bounds on structural SLP variables which are not in
        coefficients.

      * (1) Relax step bounds on all structural SLP variables.

      * (2) Relax step bounds on SLP variables appearing only in coefficients.

      * (3) Relax step bounds on SLP variables appearing in coefficients.

num:xprs_autoscaling (XPRS_AUTOSCALING)
      Whether the Optimizer should automatically select between different
      scaling algorithms. If the SCALING control is set, no automatic scaling
      will be applied.

      Values (default: -1):

      * (-1) Automatic.

      * (0) Disabled.

      * (1) Cautious strategy. Non-standard scaling will only be selected if
        it appears to be clearly superior.

      * (2) Moderate strategy.

      * (3) Aggressive strategy. Standard scaling will only be selected if it
        appears to be clearly superior.

num:xprs_objscalefactor (XPRS_OBJSCALEFACTOR)
      Custom objective scaling factor, expressed as a power of 2. When set, it
      overwrites the automatic objective scaling factor. A value of 0 means no
      objective scaling. This control is applied for the full solve, and is
      independent of any extra scaling that may occur specifically for the
      barrier or simplex solvers. As it is a power of 2, to scale by 16, set
      the value of the control to 4.

      Default: 0

num:xslp_infinity (XSLP_INFINITY, NLPINFINITY)
      Value returned by a divide-by-zero in a formula

      Default: 1.0e+10

obj:multi (multiobj)
      Whether to use multi-objective optimization:

      0 - Single objective, see option obj:no (default)
      1 - Multi-objective, solver's native handling if available
      2 - Multi-objective, force emulation

      When obj:multi>0 and several objectives are present, suffixes
      .objpriority, .objweight, .objreltol, and .objabstol on the objectives
      are relevant. Objectives with greater .objpriority values (integer
      values) have higher priority. Objectives with the same .objpriority are
      weighted by .objweight, according to the option obj:multi:weight.

      Objectives with positive .objabstol or .objreltol are allowed to be
      degraded by lower priority objectives by amounts not exceeding the
      .objabstol (absolute) and .objreltol (relative) limits.

      Note that with solver's native handling (when obj:multi=1 and
      supported), some solvers might have special rules for the tolerances,
      especially for LP, and not allow quadratic objectives. See the solver
      documentation.

obj:multi:options (multiobjoptions)
      0/1*: Regard multiobjective option suffixes which are objective suffixes
      beginning with option_. Example: suffix option_timelim; let
      _obj[2].option_timelim:=15;

obj:multi:weight (multiobjweight, obj:multi:weights, multiobjweights)
      How to interpret each objective's weight sign:

      1 - relative to the sense of the 1st objective
      2 - relative to its own sense (default)

      With the 1st option (legacy behaviour), negative .objweight for
      objective i would make objective i's sense the opposite of the model's
      1st objective. Otherwise, it would make objective i's sense the opposite
      to its sense defined in the model.

obj:multi:xprs_multiobjlog (XPRS_MULTIOBJLOG)
      Log level for multi-objective optimization.

      Values (default: 2):

      * (0) No logging.

      * (1) Print a summary of each problem that is solved as part of the
        multi-objective optimization.

      * (2) In addition to summaries, print messages produced by each solve at
        the level determined by OUTPUTLOG.

obj:multi:xprs_multiobjops (XPRS_MULTIOBJOPS)
      Modifies the behaviour of the optimizer when solving multi-objective
      problems.

      Values (default: 7 (all bits are set, see Section Bit-vector controls
      for bit-vector controls)):

      * (0) XPRS_MULTIOBJOPS_ENABLEDMulti-objective enabled. If this bit is
        not set, multi-objective problems will treated as single-objective
        problems, and only objective 0 will be optimized.

      * (1) XPRS_MULTIOBJOPS_PRESOLVEApply multi-objective modifications
        during presolve. If this bit is not set, the original problem will be
        modified when solving each subsequent objective, and these
        modifications will remain in the problem after the solve has
        completed.

      * (2) XPRS_MULTIOBJOPS_RCFIXINGReduced cost fixing. If this bit is set,
        optimality of earlier objectives will be preserved by fixing all
        non-basic variables with non-zero reduced costs to their bounds. If
        not set, optimality of earlier objectives will be preserved by adding
        constraints to the problem.

obj:no (objno)
      Objective to optimize:

      0 - None
      1 - First (default, if available)
      2 - Second (if available), etc.

pdhg:xprs_barhggpu (XPRS_BARHGGPU)
      Whether to use a GPU for the hybrid gradient algorithm. Even though the
      GPU implementation of the hybrid gradient algorithm is identical in
      operation and functionality to the CPU implementation, the returned
      solutions can differ between the two versions due to the different
      architecture of the GPU. GPU support is not available in the
      deterministic concurrent LP algorithm.

      Values (default: 0, do not use a GPU. ):

      * (0) Do not use a GPU.

      * (1) Use the GPU.

pdhg:xprs_barhggpublocksize (XPRS_BARHGGPUBLOCKSIZE)
      The size of CUDA blocks to use for the GPU calculations.

      Default: 256

pdhg:xprs_barhgprecision (XPRS_BARHGPRECISION)
      Whether to use single or double precision floating-point arithmetic in
      the hybrid gardient algorithm. The single precision implementation uses
      less memory and is, in general, faster than the double precision
      implementation. This control applies to both the CPU and the GPU
      implementation of the algorithm. The performance difference is greater
      for the GPU version.

      Values (default: -1, use double precision for CPU platforms and single
      precision on GPU platforms. ):

      * (-1) Automatically selected based on the value of BARHGGPU: single
        precision arithmetic is used if BARHGGPU is 1 (GPU execution), and
        double precision arithmetic is used if BARHGGPU is 0 (CPU execution).

      * (0) Use single precision arithmetic on both CPU and GPU platforms.

      * (1) Use double precision arithmetic on both CPU and GPU platforms.

pdhg:xprs_barhgreltol (XPRS_BARHGRELTOL)
      Relative feasibility tolerance for the hybrid gradient algorithm.

      Default: 0, determined automatically.

pre:basisred (prebasisred, pre:xprs_prebasisred, XPRS_PREBASISRED)
      Determines if a lattice basis reduction algorithm should be attempted as
      part of presolve

      Values (default: 0):

      * (-1) Automatic.

      * (0) Disable basis reduction.

      * (1) Enable basis reduction.

pre:bndredcone (prebndredcone, pre:xprs_prebndredcone, XPRS_PREBNDREDCONE)
      Determines if second order cone constraints should be used for inferring
      bound reductions on variables when solving a MIP.

      Values (default: -1):

      * (-1) Automatic.

      * (0) Disable bound reductions from second order cone constraints.

      * (1) Enable bound reductions from second order cone constraints.

pre:bndredquad (prebndredquad, pre:xprs_prebndredquad, XPRS_PREBNDREDQUAD)
      Determines if convex quadratic constraints should be used for inferring
      bound reductions on variables when solving a MIP.

      Values (default: -1):

      * (-1) Automatic.

      * (0) Disable bound reductions from quadratic constraints.

      * (1) Enable bound reductions from quadratic constraints.

pre:cliquestrategy (precliquestrategy, pre:xprs_precliquestrategy, XPRS_PRECLIQUESTRATEGY)
      Determines how much effort to spend on clique covers in presolve.

      Default: -1

pre:coefelim (precoefelim, pre:xprs_precoefelim, XPRS_PRECOEFELIM)
      Presolve: Specifies whether the optimizer should attempt to recombine
      constraints in order to reduce the number of non zero coefficients when
      presolving a mixed integer problem.

      Values (default: 2):

      * (0) Disabled.

      * (1) Remove as many coefficients as possible.

      * (2) Cautious eliminations. Will not perform a reduction if it might
        destroy problem structure useful to e.g. heuristics or cutting.

pre:components (precomponents, pre:xprs_precomponents, XPRS_PRECOMPONENTS)
      Presolve: determines whether small independent components should be
      detected and solved as individual subproblems during root node
      processing.

      Values (default: -1):

      * (-1) Automatically determined.

      * (0) Disable detection of independent components.

      * (1) Enable detection of independent components.

pre:componentseffort (precomponentseffort, pre:xprs_precomponentseffort, XPRS_PRECOMPONENTSEFFORT)
      Presolve: adjusts the overall effort for the independent component
      presolver. This control affects working limits for the subproblem
      solving as well as thresholds when it is called. Increase to put more
      emphasis on component presolving.

      Default: 1.0

pre:configuration (preconfiguration, pre:xprs_preconfiguration, XPRS_PRECONFIGURATION)
      MIP Presolve: determines whether binary rows with only few repeating
      coefficients should be reformulated. The reformulation enumerates the
      extremal feasible configurations of a row and introduces new columns and
      rows to model the choice between these extremal configurations. This
      presolve operation can be disabled as part of the (advanced) IP
      reductions PRESOLVEOPS.

      Values (default: -1):

      * (-1) Automatically determined.

      * (0) Disable configuration presolving.

pre:convertseparable (preconvertseparable, pre:xprs_preconvertseparable, XPRS_PRECONVERTSEPARABLE)
      Presolve: reformulate problems with a non-diagonal quadratic objective
      and/or constraints as diagonal quadratic or second-order conic
      constraints.

      Values (default: -1):

      * (-1) Automatically determined.

      * (0) Disable reformulation.

      * (1) Enable reformulation to diagonal quadratic constraints.

      * (2) Enable reformulation to diagonal quadratic constraints and
        reduction to second-order cones.

pre:domcol (predomcol, pre:xprs_predomcol, XPRS_PREDOMCOL)
      Presolve: Determines the level of dominated column removal reductions to
      perform when presolving a mixed integer problem. Only binary columns
      will be checked.

      Values (default: -1):

      * (-1) Automatically determined.

      * (0) Disabled.

      * (1) Cautious strategy, limited effort looking for special structure.

      * (2) Same as 2 but checking all candidates.

      * (3) Includes 1 and 2 but also looks for more generic column
        domination.

pre:domrow (predomrow, pre:xprs_predomrow, XPRS_PREDOMROW)
      Presolve: Determines the level of dominated row removal reductions to
      perform when presolving a problem.

      Values (default: -1):

      * (-1) Automatically determined.

      * (0) Disabled.

      * (1) Cautious strategy.

      * (2) Medium strategy.

      * (3) Aggressive strategy. All candidate row combinations will be
        considered.

pre:duprow (preduprow, pre:xprs_preduprow, XPRS_PREDUPROW)
      Presolve: Determines the type of duplicate rows to look for and
      eliminate when presolving a problem.

      Values (default: -1):

      * (-1) Automatically determined.

      * (0) Do not eliminate duplicate rows.

      * (1) Eliminate only rows that are identical in all variables.

      * (2) Same as option 1 plus eliminate duplicate rows with simple penalty
        variable expressions. (MIP only).

      * (3) Same as option 2 plus eliminate duplicate rows with more complex
        penalty variable expressions. (MIP only).

pre:elimfillin (elimfillin, pre:xprs_elimfillin, XPRS_ELIMFILLIN)
      Amount of fill-in allowed when performing an elimination in presolve .

      Default: 7

pre:elimquad (preelimquad, pre:xprs_preelimquad, XPRS_PREELIMQUAD)
      Presolve: Allows for elimination of quadratic variables via doubleton
      rows.

      Values (default: -1):

      * (-1) Automatically determined.

      * (0) Do not eliminate duplicate rows.

      * (1) Eliminate at least one quadratic variable for each doubleton row.

pre:elimtol (elimtol, pre:xprs_elimtol, XPRS_ELIMTOL)
      The Markowitz tolerance for the elimination phase of the presolve.

      Default: 0.001

pre:folding (prefolding, pre:xprs_prefolding, XPRS_PREFOLDING)
      Presolve: Determines if a folding procedure should be used to aggregate
      continuous columns in an equitable partition.

      Values (default: -1):

      * (-1) Automatically determined.

      * (0) Disabled.

      * (1) Enabled.

pre:genconsdualreductions (genconsdualreductions, pre:xprs_genconsdualreductions, XPRS_GENCONSDUALREDUCTIONS)
      This parameter specifies whether dual reductions should be applied to
      reduce the number of columns and rows added when transforming general
      constraints to MIP structs.

      Values (default: 1):

      * (0) Disabled. No dual reductions, add columns and rows.

      * (1) Enabled. Only add neccessary columns and rows, drop those implied
        by the objective sense.

pre:implications (preimplications, pre:xprs_preimplications, XPRS_PREIMPLICATIONS)
      Presolve: Determines whether to use implication structures to remove
      redundant rows. If implication sequences are detected, they might also
      be used in probing.

      Values (default: -1):

      * (-1) Automatically determined.

      * (0) Do not use implications for sparsification.

      * (1) Use implications to remove reduandant rows.

pre:indlinbigbigm (indprelinbigm, pre:indlinbigm, pre:xprs_indprelinbigm, XPRS_INDPRELINBIGM)
      During presolve, indicator constraints will be linearized using a BigM
      coefficient whenever that BigM coefficient is small enough. This control
      defines the largest BigM for which the original constraint will be
      replaced by the linearized version. If the BigM is larger than
      INDPRELINBIGM but smaller than INDLINBIGM, the linearized row will be
      added but the original indicator constraint is kept as a numerically
      stable way to check feasibility.

      Default: 100.0

pre:indlinsmallbigm (indlinbigm, alg:indlinbigm, pre:xprs_indlinbigm, XPRS_INDLINBIGM)
      During presolve, indicator constraints will be linearized using a BigM
      coefficient whenever that BigM coefficient is small enough. This control
      defines the largest BigM for which such a linearized version will be
      added to the problem in addition to the original constraint. If the BigM
      is even smaller than INDPRELINBIGM, then the original indicator
      constraint will additionally be dropped from the problem.

      Default: 1.0E+05

pre:lindep (prelindep, pre:xprs_prelindep, XPRS_PRELINDEP)
      Presolve: Determines whether to check for and remove linearly dependent
      equality constraints when presolving a problem.

      Values (default: -1):

      * (-1) Automatically determined.

      * (0) Do not check for linearly dependent equality constraints.

      * (1) Check for and remove linearly dependent equality constraints.

pre:maxgrow (presolvemaxgrow, pre:xprs_presolvemaxgrow, XPRS_PRESOLVEMAXGROW)
      Limit on how much the number of non-zero coefficients is allowed to grow
      during presolve, specified as a ratio of the number of non-zero
      coefficients in the original problem.

      Default: 0.1

pre:maximpliedbound (maximpliedbound, pre:xprs_maximpliedbound, XPRS_MAXIMPLIEDBOUND)
      Presolve: When tighter bounds are calculated during MIP preprocessing,
      only bounds whose absolute value are smaller than MAXIMPLIEDBOUND will
      be applied to the problem.

      Default: 1.0E+08

pre:maxscalefactor (maxscalefactor, pre:xprs_maxscalefactor, XPRS_MAXSCALEFACTOR)
      This determines the maximum scaling factor that can be applied during
      scaling. The maximum is provided as an exponent of a power of 2.

      Values (default: 64):

      * (0-64) The maximum is provided an exponent of a power of 2.

pre:objcutdetect (preobjcutdetect, pre:xprs_preobjcutdetect, XPRS_PREOBJCUTDETECT)
      Presolve: Determines whether to check for constraints that are parallel
      or near parallel to a linear objective function, and which can safely be
      removed. This reduction applies to MIPs only.

      Values (default: 1):

      * (0) Disable check and reductions.

      * (1) Enable check and reductions.

pre:objscalefactor (objscalefactor)
      Power of 2 (default 0) by which the objective is scaled. Nonzero
      objscalfactor values override automatic global objective scaling

pre:ops (presolveops, pre:xprs_presolveops, XPRS_PRESOLVEOPS)
      This bit-vector control (see Section Bit-vector controls) specifies the
      operations which are performed during the presolve.

      Values (default: 511 (bits 0 — 8 incl. are set)):

      * (0) Singleton column removal.

      * (1) Singleton row removal.

      * (2) Forcing row removal.

      * (3) Dual reductions.

      * (4) Redundant row removal.

      * (5) Duplicate column removal.

      * (6) Duplicate row removal.

      * (7) Strong dual reductions.

      * (8) Variable eliminations.

      * (9) No IP reductions.

      * (10) No domain changes for MIP entities (e.g., semi-continuous
        detection or shifting integers).

      * (11) No advanced IP reductions.

      * (12) No eliminations on integers.

      * (13) No reductions based on solution enumeration.

      * (14) Linearly dependant row removal.

      * (15) No integer variable and SOS detection.

      * (16) No implied bounds.

      * (17) No clique presolve.

      * (18) No mod2 presolve.

pre:passes (presolvepasses, pre:xprs_presolvepasses, XPRS_PRESOLVEPASSES)
      Number of reduction rounds to be performed in presolve

      Default: 1

pre:permute (prepermute, pre:xprs_prepermute, XPRS_PREPERMUTE)
      This bit-vector control (see Section Bit-vector controls) specifies
      whether to randomly permute rows, columns and MIP entities when starting
      the presolve. With the default value 0, no permutation will take place.

      Values (default: 0):

      * (0) Permute rows.

      * (1) Permute columns.

      * (2) Permute MIP entities. This bit only affects MIP problems.

pre:permuteseed (prepermuteseed, pre:xprs_prepermuteseed, XPRS_PREPERMUTESEED)
      This control sets the seed for the pseudo-random number generator for
      permuting the problem when starting the presolve. This control only has
      effects when PREPERMUTE is enabled.

      Default: 1

pre:probing (preprobing, pre:xprs_preprobing, XPRS_PREPROBING)
      Presolve: Amount of probing to perform on binary variables during
      presolve. This is done by fixing a binary to each of its values in turn
      and analyzing the implications.

      Values (default: -1):

      * (-1) Let the optimizer decide on the amount of probing.

      * (0) Disabled.

      * (+1) Light probing — only few implications will be examined.

      * (+2) Full probing — all implications for all binaries will be
        examined.

      * (+3) Full probing and repeat as long as the problem is significantly
        reduced.

pre:protectdual (preprotectdual, pre:xprs_preprotectdual, XPRS_PREPROTECTDUAL)
      Presolve: specifies whether the presolver should protect a given dual
      solution by maintaining the same level of dual feasibility. Enabling
      this control often results in a worse presolved model. This control only
      expected to be optionally enabled before calling XPRScrossoverlpsol.

      Values (default: 0):

      * (0) Disabled.

      * (1) Enabled. Protect the dual solution during presolve.

pre:pwldualreductions (pwldualreductions, pre:xprs_pwldualreductions, XPRS_PWLDUALREDUCTIONS)
      This parameter specifies whether dual reductions should be applied to
      reduce the number of columns, rows and SOS-constraints added when
      transforming piecewise linear objectives and constraints to MIP structs.

      Values (default: 1):

      * (0) Disabled. No dual reductions, add all columns, rows and
        SOS-constraints.

      * (1) Enabled. Only add neccessary columns, rows and sets, drop those
        implied by the objective sense.

pre:pwlnonconvextransformation (pwlnonconvextransformation, pre:xprs_pwlnonconvextransformation, XPRS_PWLNONCONVEXTRANSFORMATION)
      This control specifies the reformulation method for piecewise linear
      constraints at the beginning of the search. Note that the chosen
      formulation will only be used if MIP entities are necessary but not if
      presolve detected that a convex reformulation is possible. Furthermore,
      the binary formulation will only be applied to piecewise linear
      constraints with bounded input variable, otherwise the SOS2-formulation
      will be used.

      Values (default: -1):

      * (-1) Automatic.

      * (0) Use a formulation based on SOS2-constraints.

      * (1) Use a formulation based on binary variables.

pre:rootpresolve (rootpresolve, mip:xprs_rootpresolve, XPRS_ROOTPRESOLVE)
      Determines if presolving should be performed on the problem after the
      tree search has finished with root cutting and heuristics.

      Values (default: -1):

      * (-1) Let the optimizer decide if the problem should be presolved
        again.

      * (0) Disabled.

      * (+1) Always presolve the root problem.

pre:scaling (scaling, num:xprs_scaling, XPRS_SCALING)
      This bit-vector control (see Section Bit-vector controls) determines how
      the Optimizer will rescale a model internally before optimization. If
      set to 0, no scaling will take place.

      Values (default: 163, meaning bits 0, 1, 5 and 7 are set):

      * (0) Row scaling.

      * (1) Column scaling.

      * (2) Row scaling again.

      * (3) Maximum.

      * (4) Curtis-Reid.

      * (5) 0: scale by geometric mean.1: scale by maximum element.

      * (6) Treat big-M rows as normal rows.

      * (7) Scale objective function for the simplex method.

      * (8) Exclude the quadratic part of constraint when calculating scaling
        factors.

      * (9) Scale before presolve.

      * (10) Do not scale rows up.

      * (11) Do not scale columns down.

      * (12) Do not apply automatic objective scaling.

      * (13) RHS scaling.

      * (14) Disable aggressive quadratic scaling.

      * (15) Enable explicit linear slack scaling.

pre:solve (presolve, pre:xprs_presolve, XPRS_PRESOLVE)
      This control determines whether presolving should be performed prior to
      starting the main algorithm. Presolve attempts to simplify the problem
      by detecting and removing redundant constraints, tightening variable
      bounds, etc. In some cases, infeasibility may even be determined at this
      stage, or the optimal solution found.

      Values (default: 1):

      * (-1) Presolve applied, but a problem will not be declared infeasible
        if primal infeasibilities are detected. The problem will be solved by
        the LP optimization algorithm, returning an infeasible solution, which
        can sometimes be helpful.

      * (0) Presolve not applied.

      * (1) Presolve applied.

      * (2) Presolve applied, but redundant bounds are not removed. This can
        sometimes increase the efficiency of the barrier algorithm.

      * (3) Presolve is applied, and bounds detected to be redundant are
        always removed.

pre:solve_nlp (presolve_nlp, presolve_slp, pre:xslp_presolve, XSLP_PRESOLVE, NLPPRESOLVE)
      This control determines whether presolving should be performed on the
      nonlinear problem prior to starting the main algorithm

      Values (default: -1):

      * (-1) Disable nonlinear presolve if and only if Optimizer presolve is
        disabled.

      * (0) Disable nonlinear presolve.

      * (1) Activate nonlinear presolve.

      * (2) Low memory presolve. Original problem is not restored by postsolve
        and dual solution may not be completely postsolved.

pre:sosreftol (sosreftol, tol:xprs_sosreftol, XPRS_SOSREFTOL)
      The minimum relative gap between the ordering values of elements in a
      special ordered set. The gap divided by the absolute value of the larger
      of the two adjacent values must be at least SOSREFTOL.

      Default: 1.0E-06

pre:trace (trace, pre:xprs_trace, XPRS_TRACE)
      Display the infeasibility diagnosis during presolve. If non-zero, an
      explanation of the logical deductions made by presolve to deduce
      infeasibility or unboundedness will be displayed on screen or sent to
      the message callback function.

      Default: 0

pre:xprs_alternativeredcosts (XPRS_ALTERNATIVEREDCOSTS)
      Controls aggressiveness of searching for alternative reduced cost

      Values (default: -1):

      * (-1) The solver decides if searching for alternative reduced cost is
        beneficial or not. This is the default setting.

      * (0) Searching for alternative reduced cost is disabled.

      * (1) Searching for alternative reduced cost is enabled.

pre:xprs_genconsabstransformation (XPRS_GENCONSABSTRANSFORMATION)
      This control specifies the reformulation method for absolute value
      general constraints at the beginning of the search.

      Values (default: -1):

      * (-1) Automatic.

      * (0) Use a formulation based on indicator constraints.

      * (1) Use a formulation based on SOS1-constraints.

pre:xprs_preconedecomp (XPRS_PRECONEDECOMP)
      Presolve: decompose regular and rotated cones with more than two
      elements and apply Outer Approximation on the resulting components.

      Values (default: -1):

      * (-1) Automatically determined.

      * (0) Disable cone decomposition.

      * (1) Enable cone decomposition by replacing large cones with small ones
        in the presolved problem.

      * (2) Similar to 1, plus decomposition is enabled even if the cone
        variable is fixed.

      * (3) Cones are decomposed within the Outer Approximation domain only,
        i.e., the problem maintains the original cones.

pre:xprs_preconvertobjtocons (XPRS_PRECONVERTOBJTOCONS)
      Presolve: convert a linear or quadratic objective function into an
      objective transfer constraint

      Values (default: -1):

      * (-1) Automatically determined.

      * (0) Disable reformulation.

      * (1) Move only the quadratic part of the objective into a constraint.

      * (2) Move both the linear and quadratic parts of the objective into a
        constraint.

pre:xprs_presort (XPRS_PRESORT)
      This bit-vector control (see Section Bit-vector controls) specifies
      whether to sort rows, columns and MIP entities by their names when
      starting the presolve. With the default value 0, no sorting will take
      place.

      Values (default: 0):

      * (0) Sort rows.

      * (1) Sort columns.

      * (2) Sort MIP entities. This bit only affects MIP problems.

pre:xslp_boundthreshold (XSLP_BOUNDTHRESHOLD, SLPBOUNDTHRESHOLD)
      The maximum size of a bound that can be introduced by nonlinear
      presolve.

      Default: 1.0e+10

pre:xslp_linquadbr (XSLP_LINQUADBR, NLPLINQUADBR)
      Use linear and quadratic constraints and objective function to further
      reduce bounds on all variables

      Values (default: -1):

      * (-1) automatic selection

      * (0) disable

      * (1) enable

pre:xslp_postsolve (XSLP_POSTSOLVE, NLPPOSTSOLVE)
      This control determines whether postsolving should be performed
      automatically

      Values (default: -1):

      * (-1) Postsolve if the problem could be solved to
        optimality/infeasibility.

      * (0) Do not automatically postsolve.

      * (1) Postsolve automatically.

pre:xslp_presolve_elimtol (XSLP_PRESOLVE_ELIMTOL, NLPPRESOLVE_ELIMTOL)
      Tolerance for nonlinear eliminations during SLP presolve

      Default: 0.001

pre:xslp_presolvelevel (XSLP_PRESOLVELEVEL, NLPPRESOLVELEVEL)
      This control determines the level of changes presolve may carry out on
      the problem and whether column/row indices may change

      Values (default: XSLP_PRESOLVELEVEL_FULL):

      * (1) Individual rows only presolve, no dropped columns/rows or index
        changes, no nonlinear transformations (XSLP_PRESOLVELEVEL_LOCALIZED).

      * (2) All linear presolve that does not drop columns/rows, no index
        changes, no nonlinear transformations (XSLP_PRESOLVELEVEL_BASIC).

      * (3) Full linear presolve including dropping columns/rows and index
        changes, no nonlinear transformations (XSLP_PRESOLVELEVEL_LINEAR).

      * (4) Full presolve (XSLP_PRESOLVELEVEL_FULL).

pre:xslp_presolveops (XSLP_PRESOLVEOPS, NLPPRESOLVEOPS)
      Bitmap indicating the SLP presolve actions to be taken

      Values (default: 2104):

      * (0) Generic SLP presolve.

      * (1) Explicitly fix columns identified as fixed to zero.

      * (2) Explicitly fix all columns identified as fixed.

      * (3) SLP bound tightening.

      * (4) MISLP bound tightening.

      * (5) Bound tightening based on function domains.

      * (8) Do not presolve coefficients.

      * (9) Do not remove delta variables.

      * (10) Avoid reductions that can not be dual postsolved.

      * (11) Allow eliminations on determined variables.

      * (12) Avoid performing linear reductions at the nlp level.

      * (13) Avoid simplifying nonlinear expressions.

pre:xslp_presolvezero (XSLP_PRESOLVEZERO, NLPPRESOLVEZERO)
      Minimum absolute value for a variable which is identified as nonzero
      during SLP presolve

      Default: 1.0E-09

pre:xslp_probing (XSLP_PROBING, NLPPROBING)
      This control determines whether probing on a subset of variables should
      be performed prior to starting the main algorithm. Probing runs multiple
      times bound reduction in order to further tighten the bounding box.

      Values (default: -1):

      * (-1) Automatic.

      * (0) Disable SLP probing.

      * (1) Activate SLP probing only on binary variables.

      * (2) Activate SLP probing only on binary or unbounded integer
        variables.

      * (3) Activate SLP probing only on binary or integer variables.

      * (4) Activate SLP probing only on binary, integer variables, and
        unbounded continuous variables.

      * (5) Activate SLP probing on any variable.

pre:xslp_reformulate (XSLP_REFORMULATE, NLPREFORMULATE)
      Controls the problem reformulations carried out before augmentation.
      This allows SLP to take advantage of dedicated algorithms for special
      problem classes.

      Values (default: 511 (bits 0 — 8 incl. are set)):

      * (0) Solve convex quadratic objectives using the XPRS library .

      * (1) Convert non-convex quadratic objectives to SLP constructs .

      * (2) Solve convex quadratic constraints using the XPRS library.

      * (3) Convert non-convex QCQP constraints to SLP constructs.

      * (4) Keep second order cones in the XPRS problem to keep them in the
        linearizations.

      * (5) Convexity of a quadratic only problem may be checked by calling
        the optimizer to solve the instance.

      * (6) Convert pievewise linear functions to MIP constructs.

      * (7) Convert ABS functions to MIP constraints if the full problem can
        be made not nonlinear.

      * (8) Convert MIN and MAX functions to MIP expressions if the full
        problem can be made not nonlinear.

      * (9) Always convert ABS expressions.

      * (10) Always convert MIN and MAX expressions.

prob:xprs_checkinputdata (XPRS_CHECKINPUTDATA)
      Check input arrays for bad data.

      Values (default: 1 (on)):

      * (0) Do not check.

      * (1) Check input arrays.

prob:xprs_extracols (XPRS_EXTRACOLS)
      The initial number of extra columns to allow for in the matrix. If
      columns are to be added to the matrix, then, for maximum efficiency,
      space should be reserved for the columns before the matrix is input by
      setting the EXTRACOLS control. If this is not done, resizing will occur
      automatically, but more space may be allocated than the user actually
      requires.

      Default: 0

prob:xprs_extraelems (XPRS_EXTRAELEMS)
      The initial number of extra matrix elements to allow for in the matrix,
      including coefficients for cuts. If rows or columns are to be added to
      the matrix, then, for maximum efficiency, space should be reserved for
      the extra matrix elements before the matrix is input by setting the
      EXTRAELEMS control. If this is not done, resizing will occur
      automatically, but more space may be allocated than the user actually
      requires.

      Default: Hardware/platform dependent.

prob:xprs_extramipents (XPRS_EXTRAMIPENTS)
      The initial number of extra MIP entities to allow for.

      Default: 0

prob:xprs_extrarows (XPRS_EXTRAROWS)
      The initial number of extra rows to allow for in the matrix, including
      cuts. If rows are to be added to the matrix, then, for maximum
      efficiency, space should be reserved for the rows before the matrix is
      input by setting the EXTRAROWS control. If this is not done, resizing
      will occur automatically, but more space may be allocated than the user
      actually requires.

      Default: 0

prob:xprs_extrasetelems (XPRS_EXTRASETELEMS)
      The initial number of extra elements in sets to allow for in the matrix.
      If sets are to be added to the matrix, then, for maximum efficiency,
      space should be reserved for the set elements before the matrix is input
      by setting the EXTRASETELEMS control. If this is not done, resizing will
      occur automatically, but more space may be allocated than the user
      actually requires.

      Default: 0

prob:xprs_extrasets (XPRS_EXTRASETS)
      The initial number of extra sets to allow for in the matrix. If sets are
      to be added to the matrix, then, for maximum efficiency, space should be
      reserved for the sets before the matrix is input by setting the
      EXTRASETS control. If this is not done, resizing will occur
      automatically, but more space may be allocated than the user actually
      requires.

      Default: 0

prob:xprs_inputtol (XPRS_INPUTTOL)
      The tolerance on input values elements. If any value is less than or
      equal to INPUTTOL in absolute value, it is treated as zero. For the
      internal zero tolerance see MATRIXTOL.

      Default: 0.0

prob:xprs_maxmcoeffbufferelems (XPRS_MAXMCOEFFBUFFERELEMS)
      The maximum number of matrix coefficients to buffer before flushing into
      the internal representation of the problem. Buffering coefficients can
      offer a significant performance gain when you are building a matrix
      using XPRSchgcoef or XPRSchgmcoef, but can lead to a significant memory
      overhead for large matrices, which this control allows you to influence.

      Default: 2147483647

qp:eigenvaluetol (eigenvaluetol, qp:xprs_eigenvaluetol, XPRS_EIGENVALUETOL)
      A quadratic matrix is considered not to be positive semi-definite, if
      its smallest eigenvalue is smaller than the negative of this value.

      Default: 1E-6

qp:miqcpalg (miqcpalg, qp:xprs_miqcpalg, XPRS_MIQCPALG)
      This control determines which algorithm is to be used to solve mixed
      integer quadratic constrained and mixed integer second order cone
      problems.

      Values (default: -1):

      * (-1) Determined automatically.

      * (0) Use the barrier algorithm in the branch and bound algorithm.

      * (1) Use outer approximations in the branch and bound algorithm.

qp:nonconvex (nonconvex, pre:xprs_ifcheckconvexity, XPRS_IFCHECKCONVEXITY)
      Determines if the convexity of the problem is checked before
      optimization. Applies to quadratic, mixed integer quadratic and
      quadratically constrained problems. Checking convexity takes some time,
      thus for problems that are known to be convex it might be reasonable to
      switch the checking off.

      Values (default: 1):

      * (0) Turn off convexity checking.

      * (1) Turn on convexity checking.

qp:repairindefiniteq (repairindefq, repairindefiniteq, qp:xprs_repairindefiniteq, XPRS_REPAIRINDEFINITEQ)
      Controls if the optimizer should make indefinite quadratic matrices
      positive definite when it is possible.

      Values (default: 1):

      * (0) Repair if possible.

      * (1) Do not repair.

qp:simplexops (qsimplexops, qp:xprs_qsimplexops, XPRS_QSIMPLEXOPS)
      Controls the behavior of the quadratic simplex solvers via a bit-vector
      (see Section Bit-vector controls).

      Values (default: 0 ):

      * (0) Force traditional primal first phase.

      * (1) Force BigM primal first phase.

      * (2) Force traditional dual first phase.

      * (3) Force BigM dual first phase.

      * (4) Always use artificial bounds in dual.

      * (5) Use original problem basis only when warmstarting the KKT.

      * (6) Skip the primal bound flips for ranged primals (might cause more
        trouble than good if the bounds are very large).

      * (7) Also do the single pivot crash.

      * (8) Do not apply aggressive perturbation in dual.

      * (9) Applies standard scaling to the KKT system.

      * (10) Do not fall back to using Barrier in case of numerical
        difficulties with quadratic simplex during a MIP solve.

      * (11) Use primal simplex to solve the phase 1 feasibility problem
        before applying quadratic primal simplex.

      * (12) Use dual simplex to solve the phase 1 feasibility problem before
        applying quadratic primal simplex.

      * (13) Use barrier algorithm to solve the phase 1 feasibility problem
        before applying quadratic primal simplex.

      * (14) Use partial pricing.

      * (15) Use full pricing.

      * (16) Perform cleanup if a superbasic solution is provided for
        warm-start.

qp:unshift (quadunshift, quadraticunshift, qp:xprs_quadraticunshift, XPRS_QUADRATICUNSHIFT)
      Determines whether an extra solution purification step is called after a
      solution found by the quadratic simplex (either primal or dual).

      Values (default: -1):

      * (-1) Determined automatically.

      * (0) No purification step.

      * (1) Always do the purification step.

sim:xprs_pivottol (XPRS_PIVOTTOL)
      Simplex: The zero tolerance for matrix elements. On each iteration, the
      simplex method seeks a nonzero matrix element to pivot on. Any element
      with absolute value less than PIVOTTOL is treated as zero for this
      purpose.

      Default: 1.0E-09

sim:xprs_ppfactor (XPRS_PPFACTOR)
      The partial pricing candidate list sizing parameter.

      Default: 1.0

slp:xslp_algorithm (XSLP_ALGORITHM, SLPALGORITHM)
      Bit map describing the SLP algorithm(s) to be used

      Values (default: 166 (sets bits 1, 2, 5, 7)):

      * (0) Do not apply step bounds.

      * (1) Apply step bounds to SLP delta vectors only when required.

      * (2) Estimate step bounds from early SLP iterations.

      * (3) Use dynamic damping.

      * (4) Do not update values which are converged within strict tolerance.

      * (5) Retain previous value when cascading if determining row is zero.

      * (6) Reset XSLP_DELTA_Z to zero when converged and continue SLP.

      * (7) Quick convergence check.

      * (8) Escalate penalties.

      * (9) Use the primal simplex algorithm when all error vectors become
        inactive.

      * (11) Continue optimizing after penalty cost reaches maximum.

      * (12) Accept a solution which has converged even if there are still
        significant active penalty error vectors.

      * (13) Skip the solution polishing step if the LP postsolve returns a
        slightly infeasible, but claimed optimal solution.

      * (14) Step bounds are updated to accomodate cascaded values (otherwise
        cascaded values are pushed to respect step bounds).

      * (15) Apply clamping when converged on extended criteria only with some
        variables having active step bounds.

      * (16) Apply clamping when converged on extended criteria only.

slp:xslp_analyze (XSLP_ANALYZE, SLPANALYZE)
      Bit map activating additional options supporting model / solution path
      analysis

      Values (default: 0):

      * (3) Include an extended iteration summary.

      * (4) Run infeasibility analysis on infeasible iterations.

      * (6) Write the linearizations to disk at every XSLP_AUTOSAVE
        iterations.

      * (7) Write the initial basis of the linearizations to disk at every
        XSLP_AUTOSAVE iterations.

      * (8) Create an XSLP save file at every XSLP_AUTOSAVE iterations.

slp:xslp_atol_a (XSLP_ATOL_A, SLPATOL_A)
      Absolute delta convergence tolerance

      Default: -1.0

slp:xslp_atol_r (XSLP_ATOL_R, SLPATOL_R)
      Relative delta convergence tolerance

      Default: -1.0

slp:xslp_augmentation (XSLP_AUGMENTATION, SLPAUGMENTATION)
      Bit map describing the SLP augmentation method(s) to be used

      Values (default: 12 (sets bits 2 and 3)):

      * (0) Minimum augmentation.

      * (1) Even handed augmentation.

      * (2) Penalty error vectors on all non-linear equality constraints.

      * (3) Penalty error vectors on all non-linear inequality constraints.

      * (4) Penalty vectors to exceed step bounds.

      * (5) Use arithmetic means to estimate penalty weights.

      * (6) Estimate step bounds from values of row coefficients.

      * (7) Estimate step bounds from absolute values of row coefficients.

      * (8) Row-based step bounds.

      * (9) Penalty error vectors on all constraints.

      * (10) Intial values do not imply an SLP variable.

      * (12) Avoid running an LP around fixed initial values trying to get
        feasible.

slp:xslp_autosave (XSLP_AUTOSAVE, SLPAUTOSAVE)
      Frequency with which to save the model

      Default: 0

slp:xslp_barcrossoverstart (XSLP_BARCROSSOVERSTART, SLPBARCROSSOVERSTART)
      Default crossover activation behaviour for barrier start

      Default: 0

slp:xslp_barlimit (XSLP_BARLIMIT, SLPBARLIMIT)
      Number of initial SLP iterations using the barrier method

      Default: 0

slp:xslp_barstallinglimit (XSLP_BARSTALLINGLIMIT, SLPBARSTALLINGLIMIT)
      Number of iterations to allow numerical failures in barrier before
      switching to dual

      Default: 3

slp:xslp_barstallingobjlimit (XSLP_BARSTALLINGOBJLIMIT, SLPBARSTALLINGOBJLIMIT)
      Number of iterations over which to measure the objective change for
      barrier iterations with no crossover

      Default: 3

slp:xslp_barstallingtol (XSLP_BARSTALLINGTOL, SLPBARSTALLINGTOL)
      Required change in the objective when progress is measured in barrier
      iterations without crossover

      Default: 0.05

slp:xslp_barstartops (XSLP_BARSTARTOPS, SLPBARSTARTOPS)
      Controls behaviour when the barrier is used to solve the linearizations

      Values (default: -1):

      * (0) Check objective progress when no crossover is applied.

      * (1) Fall back to dual simplex if too many numerical problems are
        reported by the barrier.

      * (2) If a non-vertex converged solution found by barrier without
        crossover can be returned as a final solution.

slp:xslp_cascade (XSLP_CASCADE, SLPCASCADE)
      Bit map describing the cascading to be used

      Values (default: 257):

      * (0) Apply cascading to all variables with determining rows.

      * (1) Apply cascading to SLP variables which appear in coefficients and
        which would change by more than XPRS_FEASTOL.

      * (2) Apply cascading to all SLP variables which appear in coefficients.

      * (3) Apply cascading to SLP variables which are structural and which
        would change by more than XPRS_FEASTOL.

      * (4) Apply cascading to all SLP variables which are structural.

      * (5) Create secondary order groupping DR rows with instantiated user
        functions together in the order.

      * (6) In cases where the determining column is below XSLP_DRCOLTOL, fix
        at the previous rather than current value.

      * (7) In cases where the determining column is below XSLP_DRCOLTOL, fix
        within a range XSLP_DRFIXRANGE of previous value.

      * (8) Automatically determine whether to apply cascading.

slp:xslp_cascadenlimit (XSLP_CASCADENLIMIT, SLPCASCADENLIMIT)
      Maximum number of iterations for cascading with non-linear determining
      rows

      Default: 10

slp:xslp_cascadetol_pa (XSLP_CASCADETOL_PA, SLPCASCADETOL_PA)
      Absolute cascading print tolerance

      Default: 0.01

slp:xslp_cascadetol_pr (XSLP_CASCADETOL_PR, SLPCASCADETOL_PR)
      Relative cascading print tolerance

      Default: 0.01

slp:xslp_clampshrink (XSLP_CLAMPSHRINK, SLPCLAMPSHRINK)
      Shrink ratio used to impose strict convergence on variables converged in
      extended criteria only

      Default: 0.3

slp:xslp_clampvalidationtol_a (XSLP_CLAMPVALIDATIONTOL_A, SLPCLAMPVALIDATIONTOL_A)
      Absolute validation tolerance for applying XSLP_CLAMPSHRINK

      Default: 1.0e-06

slp:xslp_clampvalidationtol_r (XSLP_CLAMPVALIDATIONTOL_R, SLPCLAMPVALIDATIONTOL_R)
      Relative validation tolerance for applying XSLP_CLAMPSHRINK

      Default: 1.0e-06

slp:xslp_convergenceops (XSLP_CONVERGENCEOPS, SLPCONVERGENCEOPS)
      Bit map describing which convergence tests should be carried out

      Values (default: 39935 (bits 0-9, 11-12, and 15 are set)):

      * (0) Execute the closure tolerance checks.

      * (1) Execute the delta tolerance checks.

      * (2) Execute the matrix tolerance checks.

      * (3) Execute the impact tolerance checks.

      * (4) Execute the slack impact tolerance checks.

      * (5) Check for user provided convergence.

      * (6) Execute the objective range checks.

      * (7) Execute the objective range + constraint activity check.

      * (8) Execute the objective range + active step bound check.

      * (9) Execute the convergence continuation check.

      * (10) Take scaling of individual variables / rows into account.

      * (11) Execute the validation target convergence checks.

      * (12) Execute the first order optimality target convergence checks.

      * (13) Allow convex quadratic problems to converge on extended criteria.

      * (15) Do not declare converged if still sufficient improvement in
        objective.

slp:xslp_ctol (XSLP_CTOL, SLPCTOL)
      Closure convergence tolerance

      Default: -1.0

slp:xslp_damp (XSLP_DAMP, SLPDAMP)
      Damping factor for updating values of variables

      Default: 1

slp:xslp_dampexpand (XSLP_DAMPEXPAND, SLPDAMPEXPAND)
      Multiplier to increase damping factor during dynamic damping

      Default: 1

slp:xslp_dampmax (XSLP_DAMPMAX, SLPDAMPMAX)
      Maximum value for the damping factor of a variable during dynamic
      damping

      Default: 1

slp:xslp_dampmin (XSLP_DAMPMIN, SLPDAMPMIN)
      Minimum value for the damping factor of a variable during dynamic
      damping

      Default: 1

slp:xslp_dampshrink (XSLP_DAMPSHRINK, SLPDAMPSHRINK)
      Multiplier to decrease damping factor during dynamic damping

      Default: 1

slp:xslp_dampstart (XSLP_DAMPSTART, SLPDAMPSTART)
      SLP iteration at which damping is activated

      Default: 0

slp:xslp_defaultstepbound (XSLP_DEFAULTSTEPBOUND, SLPDEFAULTSTEPBOUND)
      Minimum initial value for the step bound of an SLP variable if none is
      explicitly given

      Default: 16

slp:xslp_delayupdaterows (XSLP_DELAYUPDATEROWS, SLPDELAYUPDATEROWS)
      Number of SLP iterations before update rows are fully activated

      Default: 2

slp:xslp_deltacost (XSLP_DELTACOST, SLPDELTACOST)
      Initial penalty cost multiplier for penalty delta vectors

      Default: 200

slp:xslp_deltacostfactor (XSLP_DELTACOSTFACTOR, SLPDELTACOSTFACTOR)
      Factor for increasing cost multiplier on total penalty delta vectors

      Default: 1.3

slp:xslp_deltaformat (XSLP_DELTAFORMAT, SLPDELTAFORMAT)
      Formatting string for creation of names for SLP delta vectors

      Default: pD_%s where p is a unique prefix for names in the current
      problem

slp:xslp_deltamaxcost (XSLP_DELTAMAXCOST, SLPDELTAMAXCOST)
      Maximum penalty cost multiplier for penalty delta vectors

      Default: XPRS_PLUSINFINITY

slp:xslp_deltaoffset (XSLP_DELTAOFFSET, SLPDELTAOFFSET)
      Position of first character of SLP variable name used to create name of
      delta vector

      Default: 0

slp:xslp_deltazlimit (XSLP_DELTAZLIMIT, SLPDELTAZLIMIT)
      Number of SLP iterations during which to apply XSLP_DELTA_Z

      Default: 0

slp:xslp_djtol (XSLP_DJTOL, SLPDJTOL)
      Tolerance on DJ value for determining if a variable is at its step bound

      Default: 1.0e-6

slp:xslp_drcoldjtol (XSLP_DRCOLDJTOL, SLPDRCOLDJTOL)
      Reduced cost tolerance on the delta variable when fixing due to the
      determining column being below XSLP_DRCOLTOL.

      Default: 0.0

slp:xslp_drcoltol (XSLP_DRCOLTOL, SLPDRCOLTOL)
      The minimum absolute magnitude of a determining column, for which the
      determined variable is still regarded as well defined

      Default: 1.0e-6

slp:xslp_drfixrange (XSLP_DRFIXRANGE, SLPDRFIXRANGE)
      The range around the previous value where variables are fixed in
      cascading if the determining column is below XSLP_DRCOLTOL.

      Default: 0.1

slp:xslp_ecfcheck (XSLP_ECFCHECK, SLPECFCHECK)
      Check feasibility at the point of linearization for extended convergence
      criteria

      Values (default: 1):

      * (0) no check (extended criteria are always used);

      * (1) check until one infeasible constraint is found;

      * (2) check all constraints.

slp:xslp_ecftol_a (XSLP_ECFTOL_A, SLPECFTOL_A)
      Absolute tolerance on testing feasibility at the point of linearization

      Default: -1.0

slp:xslp_ecftol_r (XSLP_ECFTOL_R, SLPECFTOL_R)
      Relative tolerance on testing feasibility at the point of linearization

      Default: -1.0

slp:xslp_enforcecostshrink (XSLP_ENFORCECOSTSHRINK, SLPENFORCECOSTSHRINK)
      Factor by which to decrease the current penalty multiplier when
      enforcing rows.

      Default: 0.00001

slp:xslp_enforcemaxcost (XSLP_ENFORCEMAXCOST, SLPENFORCEMAXCOST)
      Maximum penalty cost in the objective before enforcing most violating
      rows

      Default: 1.0e+11

slp:xslp_errorcost (XSLP_ERRORCOST, SLPERRORCOST)
      Initial penalty cost multiplier for penalty error vectors

      Default: 200

slp:xslp_errorcostfactor (XSLP_ERRORCOSTFACTOR, SLPERRORCOSTFACTOR)
      Factor for increasing cost multiplier on total penalty error vectors

      Default: 1.3

slp:xslp_errormaxcost (XSLP_ERRORMAXCOST, SLPERRORMAXCOST)
      Maximum penalty cost multiplier for penalty error vectors

      Default: XPRS_PLUSINFINITY

slp:xslp_erroroffset (XSLP_ERROROFFSET, SLPERROROFFSET)
      Position of first character of constraint name used to create name of
      penalty error vectors

      Default: 0

slp:xslp_errortol_a (XSLP_ERRORTOL_A, SLPERRORTOL_A)
      Absolute tolerance for error vectors

      Default: 0.00001

slp:xslp_errortol_p (XSLP_ERRORTOL_P, SLPERRORTOL_P)
      Absolute tolerance for printing error vectors

      Default: 0.0001

slp:xslp_escalation (XSLP_ESCALATION, SLPESCALATION)
      Factor for increasing cost multiplier on individual penalty error
      vectors

      Default: 1.25

slp:xslp_etol_a (XSLP_ETOL_A, SLPETOL_A)
      Absolute tolerance on penalty vectors

      Default: 0.0001

slp:xslp_etol_r (XSLP_ETOL_R, SLPETOL_R)
      Relative tolerance on penalty vectors

      Default: 0.0001

slp:xslp_evtol_a (XSLP_EVTOL_A, SLPEVTOL_A)
      Absolute tolerance on total penalty costs

      Default: -1.0

slp:xslp_evtol_r (XSLP_EVTOL_R, SLPEVTOL_R)
      Relative tolerance on total penalty costs

      Default: -1.0

slp:xslp_expand (XSLP_EXPAND, SLPEXPAND)
      Multiplier to increase a step bound

      Default: 2

slp:xslp_feastoltarget (XSLP_FEASTOLTARGET, SLPFEASTOLTARGET)
      When set, this defines a target feasibility tolerance to which the
      linearizations are solved to

      Default: 0 (ignored, not set)

slp:xslp_filter (XSLP_FILTER, SLPFILTER)
      Bit map for controlling solution updates

      Values (default: 3 (bit 0,1)):

      * (0) retain best solution according to the merit function.

      * (1) check cascaded solutions against improvements in the merit
        function.

      * (2) force minimum step sizes in line search.

      * (3) accept the trust region step is the line search returns a zero
        step size.

slp:xslp_granularity (XSLP_GRANULARITY, SLPGRANULARITY)
      Base for calculating penalty costs

      Default: 4

slp:xslp_infeaslimit (XSLP_INFEASLIMIT, SLPINFEASLIMIT)
      The maximum number of consecutive infeasible SLP iterations which can
      occur before Xpress-SLP terminates

      Default: 3

slp:xslp_iterfallbackops (XSLP_ITERFALLBACKOPS, SLPITERFALLBACKOPS)
      Alternative LP level control values for numerically challengeing
      problems

      Default: none

slp:xslp_iterlimit (XSLP_ITERLIMIT, SLPITERLIMIT)
      The maximum number of SLP iterations

      Default: 1000

slp:xslp_itol_a (XSLP_ITOL_A, SLPITOL_A)
      Absolute impact convergence tolerance

      Default: -1.0

slp:xslp_itol_r (XSLP_ITOL_R, SLPITOL_R)
      Relative impact convergence tolerance

      Default: -1.0

slp:xslp_log (XSLP_LOG, NLPLOG)
      Level of printing during SLP iterations

      Values (default: 0):

      * (-1) none

      * (0) minimal

      * (1) normal: iteration, penalty vectors

      * (2) omit from convergence log any variables which have converged

      * (3) omit from convergence log any variables which have already
        converged (except variables on step bounds)

      * (4) include all variables in convergence log

      * (5) include user function call communications in the log

slp:xslp_lsiterlimit (XSLP_LSITERLIMIT, SLPLSITERLIMIT)
      Number of iterations in the line search

      Default: 0

slp:xslp_lspatternlimit (XSLP_LSPATTERNLIMIT, SLPLSPATTERNLIMIT)
      Number of iterations in the pattern search preceding the line search

      Default: 0

slp:xslp_lsstart (XSLP_LSSTART, SLPLSSTART)
      Iteration in which to active the line search

      Default: 8

slp:xslp_lszerolimit (XSLP_LSZEROLIMIT, SLPLSZEROLIMIT)
      Maximum number of zero length line search steps before line search is
      deactivated

      Default: 5

slp:xslp_matrixtol (XSLP_MATRIXTOL, SLPMATRIXTOL)
      Nonzero tolerance for dropping coefficients from the linearization.

      Default: 0.0

slp:xslp_maxweight (XSLP_MAXWEIGHT, SLPMAXWEIGHT)
      Maximum penalty weight for delta or error vectors

      Default: 100

slp:xslp_meritlambda (XSLP_MERITLAMBDA, NLPMERITLAMBDA)
      Factor by which the net objective is taken into account in the merit
      function

      Default: 0.0

slp:xslp_minsbfactor (XSLP_MINSBFACTOR, SLPMINSBFACTOR)
      Factor by which step bounds can be decreased beneath XSLP_ATOL_A

      Default: 1.0

slp:xslp_minusdeltaformat (XSLP_MINUSDELTAFORMAT, SLPMINUSDELTAFORMAT)
      Formatting string for creation of names for SLP negative penalty delta
      vectors

      Default: pD-%s where p is a unique prefix for names in the current
      problem

slp:xslp_minuserrorformat (XSLP_MINUSERRORFORMAT, SLPMINUSERRORFORMAT)
      Formatting string for creation of names for SLP negative penalty error
      vectors

      Default: pE-%s where p is a unique prefix for names in the current
      problem

slp:xslp_minweight (XSLP_MINWEIGHT, SLPMINWEIGHT)
      Minimum penalty weight for delta or error vectors

      Default: 0.01

slp:xslp_mtol_a (XSLP_MTOL_A, SLPMTOL_A)
      Absolute effective matrix element convergence tolerance

      Default: -1.0

slp:xslp_mtol_r (XSLP_MTOL_R, SLPMTOL_R)
      Relative effective matrix element convergence tolerance

      Default: -1.0

slp:xslp_mvtol (XSLP_MVTOL, SLPMVTOL)
      Marginal value tolerance for determining if a constraint is slack

      Default: -1.0

slp:xslp_objthreshold (XSLP_OBJTHRESHOLD, SLPOBJTHRESHOLD)
      Assumed maximum value of the objective function in absolute value.

      Default: 1.0e+15

slp:xslp_objtopenaltycost (XSLP_OBJTOPENALTYCOST, SLPOBJTOPENALTYCOST)
      Factor to estimate initial penalty costs from objective function

      Default: 0

slp:xslp_ocount (XSLP_OCOUNT, SLPOCOUNT)
      Number of SLP iterations over which to measure objective function
      variation for static objective (2) convergence criterion

      Default: 5

slp:xslp_optimalitytoltarget (XSLP_OPTIMALITYTOLTARGET, SLPOPTIMALITYTOLTARGET)
      When set, this defines a target optimality tolerance to which the
      linearizations are solved to

      Default: 0 (ignored, not set)

slp:xslp_otol_a (XSLP_OTOL_A, SLPOTOL_A)
      Absolute static objective (2) convergence tolerance

      Default: -1.0

slp:xslp_otol_r (XSLP_OTOL_R, SLPOTOL_R)
      Relative static objective (2) convergence tolerance

      Default: -1.0

slp:xslp_penaltycolformat (XSLP_PENALTYCOLFORMAT, SLPPENALTYCOLFORMAT)
      Formatting string for creation of the names of the SLP penalty transfer
      vectors

      Default: pPC_%s where p is a unique prefix for names in the current
      problem

slp:xslp_penaltyinfostart (XSLP_PENALTYINFOSTART, SLPPENALTYINFOSTART)
      Iteration from which to record row penalty information

      Default: 3

slp:xslp_penaltyrowformat (XSLP_PENALTYROWFORMAT, SLPPENALTYROWFORMAT)
      Formatting string for creation of the names of the SLP penalty rows

      Default: pPR_%s where p is a unique prefix for names in the current
      problem

slp:xslp_plusdeltaformat (XSLP_PLUSDELTAFORMAT, SLPPLUSDELTAFORMAT)
      Formatting string for creation of names for SLP positive penalty delta
      vectors

      Default: pD+%s where p is a unique prefix for names in the current
      problem

slp:xslp_pluserrorformat (XSLP_PLUSERRORFORMAT, SLPPLUSERRORFORMAT)
      Formatting string for creation of names for SLP positive penalty error
      vectors

      Default: pE+%s where p is a unique prefix for names in the current
      problem

slp:xslp_samecount (XSLP_SAMECOUNT, SLPSAMECOUNT)
      Number of steps reaching the step bound in the same direction before
      step bounds are increased

      Default: 3

slp:xslp_samedamp (XSLP_SAMEDAMP, SLPSAMEDAMP)
      Number of steps in same direction before damping factor is increased

      Default: 3

slp:xslp_sblorowformat (XSLP_SBLOROWFORMAT, SLPSBLOROWFORMAT)
      Formatting string for creation of names for SLP lower step bound rows

      Default: pSB-%s where p is a unique prefix for names in the current
      problem

slp:xslp_sbname (XSLP_SBNAME, SLPSBNAME)
      Name of the set of initial step bounds to be used

      Default: none

slp:xslp_sbrowoffset (XSLP_SBROWOFFSET, SLPSBROWOFFSET)
      Position of first character of SLP variable name used to create name of
      SLP lower and upper step bound rows

      Default: 0

slp:xslp_sbstart (XSLP_SBSTART, SLPSBSTART)
      SLP iteration after which step bounds are first applied

      Default: 8

slp:xslp_sbuprowformat (XSLP_SBUPROWFORMAT, SLPSBUPROWFORMAT)
      Formatting string for creation of names for SLP upper step bound rows

      Default: pSB+%s where p is a unique prefix for names in the current
      problem

slp:xslp_scale (XSLP_SCALE, SLPSCALE)
      When to re-scale the SLP problem

      Values (default: 1):

      * (0) No re-scaling.

      * (1) Re-scale every SLP iteration up to XSLP_SCALECOUNT iterations
        after the end of barrier optimization.

      * (2) Re-scale every SLP iteration up to XSLP_SCALECOUNT iterations in
        total.

      * (3) Re-scale every SLP iteration until primal simplex is automatically
        invoked.

      * (4) Re-scale every SLP iteration.

      * (5) Re-scale every XSLP_SCALECOUNT SLP iterations.

      * (6) Re-scale every XSLP_SCALECOUNT SLP iterations after the end of
        barrier optimization.

slp:xslp_scalecount (XSLP_SCALECOUNT, SLPSCALECOUNT)
      Iteration limit used in determining when to re-scale the SLP matrix

      Default: 0

slp:xslp_shrink (XSLP_SHRINK, SLPSHRINK)
      Multiplier to reduce a step bound

      Default: 0.5

slp:xslp_shrinkbias (XSLP_SHRINKBIAS, SLPSHRINKBIAS)
      Defines an overwrite / adjustment of step bounds for improving
      iterations

      Default: 0 (ignored, not set)

slp:xslp_slplog (XSLP_SLPLOG, SLPLOG)
      Frequency with which SLP status is printed

      Default: 1

slp:xslp_stol_a (XSLP_STOL_A, SLPSTOL_A)
      Absolute slack convergence tolerance

      Default: -1.0

slp:xslp_stol_r (XSLP_STOL_R, SLPSTOL_R)
      Relative slack convergence tolerance

      Default: -1.0

slp:xslp_stopoutofrange (XSLP_STOPOUTOFRANGE, NLPSTOPOUTOFRANGE)
      Stop optimization and return error code if internal function argument is
      out of range

      Default: 0

slp:xslp_tracemask (XSLP_TRACEMASK, SLPTRACEMASK)
      Mask of variable or row names that are to be traced through the SLP
      iterates

      Default: none (no tracing)

slp:xslp_tracemaskops (XSLP_TRACEMASKOPS, SLPTRACEMASKOPS)
      Controls the information printed for XSLP_TRACEMASK. The order in which
      the information is printed is determined by the order of bits in
      XSLP_TRACEMASKOPS.

      Values (default: -1):

      * (0) The variable name is used as a mask, not as an exact fit.

      * (1) Use mask to trace rows.

      * (2) Use mask to trace columns.

      * (3) Use mask to trace cascaded SLP variables.

      * (4) Show row / column category.

      * (5) Trace slack values.

      * (6) Trace dual values.

      * (7) Trace row penalty multiplier.

      * (8) Trace variable values (as returned by the lineariation).

      * (9) Trace reduced costs.

      * (10) Trace slp value (value used in linearization and cascaded).

      * (11) Trace step bounds.

      * (12) Trace convergence status.

      * (13) Trace line search.

slp:xslp_unfinishedlimit (XSLP_UNFINISHEDLIMIT, SLPUNFINISHEDLIMIT)
      The number of consecutive SLP iterations that may have an unfinished
      status before the solve is terminated.

      Default: 3

slp:xslp_updateformat (XSLP_UPDATEFORMAT, SLPUPDATEFORMAT)
      Formatting string for creation of names for SLP update rows

      Default: pU_%s where p is a unique prefix for names in the current
      problem

slp:xslp_updateoffset (XSLP_UPDATEOFFSET, SLPUPDATEOFFSET)
      Position of first character of SLP variable name used to create name of
      SLP update row

      Default: 0

slp:xslp_validationfactor (XSLP_VALIDATIONFACTOR, NLPVALIDATIONFACTOR)
      Minimum improvement in validation targets to continue iterating

      Default: 0.001

slp:xslp_validationtarget_k (XSLP_VALIDATIONTARGET_K, NLPVALIDATIONTARGET_K)
      Optimality target tolerance

      Default: 1e-6

slp:xslp_validationtarget_r (XSLP_VALIDATIONTARGET_R, NLPVALIDATIONTARGET_R)
      Feasiblity target tolerance

      Default: 1e-6

slp:xslp_validationtol_a (XSLP_VALIDATIONTOL_A, NLPVALIDATIONTOL_A)
      Absolute tolerance for the XSLPvalidate procedure

      Default: 0.00001

slp:xslp_validationtol_k (XSLP_VALIDATIONTOL_K, NLPVALIDATIONTOL_K)
      Relative tolerance for the XSLPvalidatekkt procedure

      Default: 0.00001

slp:xslp_vcount (XSLP_VCOUNT, SLPVCOUNT)
      Number of SLP iterations over which to measure static objective (3)
      convergence

      Default: 0

slp:xslp_vlimit (XSLP_VLIMIT, SLPVLIMIT)
      Number of SLP iterations after which static objective (3) convergence
      testing starts

      Default: 0

slp:xslp_vtol_a (XSLP_VTOL_A, SLPVTOL_A)
      Absolute static objective (3) convergence tolerance

      Default: -1.0

slp:xslp_vtol_r (XSLP_VTOL_R, SLPVTOL_R)
      Relative static objective (3) convergence tolerance

      Default: -1.0

slp:xslp_wcount (XSLP_WCOUNT, SLPWCOUNT)
      Number of SLP iterations over which to measure the objective for the
      extended convergence continuation criterion

      Default: 0

slp:xslp_wtol_a (XSLP_WTOL_A, SLPWTOL_A)
      Absolute extended convergence continuation tolerance

      Default: -1.0

slp:xslp_wtol_r (XSLP_WTOL_R, SLPWTOL_R)
      Relative extended convergence continuation tolerance

      Default: -1.0

slp:xslp_xcount (XSLP_XCOUNT, SLPXCOUNT)
      Number of SLP iterations over which to measure static objective (1)
      convergence

      Default: 5

slp:xslp_xlimit (XSLP_XLIMIT, SLPXLIMIT)
      Number of SLP iterations up to which static objective (1) convergence
      testing is performed

      Default: 100

slp:xslp_xtol_a (XSLP_XTOL_A, SLPXTOL_A)
      Absolute static objective function (1) tolerance

      Default: -1.0

slp:xslp_xtol_r (XSLP_XTOL_R, SLPXTOL_R)
      Relative static objective function (1) tolerance

      Default: -1.0

slp:xslp_zerocriterion (XSLP_ZEROCRITERION, SLPZEROCRITERION)
      Bitmap determining the behavior of the placeholder deletion procedure

      Values (default: 0):

      * (0) (=1) Remove placeholders in nonbasic SLP variables

      * (1) (=2) Remove placeholders in nonbasic delta variables

      * (2) (=4) Remove placeholders in a basic SLP variable if its update row
        is nonbasic

      * (3) (=8) Remove placeholders in a basic delta variable if its update
        row is nonbasic and the corresponding SLP variable is nonbasic

      * (4) (=16) Remove placeholders in a basic delta variable if the
        determining row for the corresponding SLP variable is nonbasic

      * (5) (=32) Print information about zero placeholders

slp:xslp_zerocriterioncount (XSLP_ZEROCRITERIONCOUNT, SLPZEROCRITERIONCOUNT)
      Number of consecutive times a placeholder entry is zero before being
      considered for deletion

      Default: 0

slp:xslp_zerocriterionstart (XSLP_ZEROCRITERIONSTART, SLPZEROCRITERIONSTART)
      SLP iteration at which criteria for deletion of placeholder entries are
      first activated.

      Default: 0

sol:chk:fail (chk:fail, checkfail)
      Fail on MP solution check violations, with solve result 150.

sol:chk:feastol (sol:chk:eps, chk:eps, chk:feastol)
      Absolute tolerance to check objective values', variable and constraint
      bounds' violations. Only triggers if also sol:chk:feastolrel is
      violated. See also pre:feastol. Default 1e-6.

sol:chk:feastolrel (sol:chk:epsrel, chk:epsrel, chk:feastolrel)
      Relative tolerance to check objective values', variable and constraint
      bounds' violations. Only triggers if also sol:chk:feastol is violated.
      See also pre:feastol. Default 1e-6.

sol:chk:infeas (chk:infeas, checkinfeas)
      Check even infeasible solution condidates, whenever solver reports them.

sol:chk:inttol (sol:chk:inteps, sol:inteps, chk:inttol)
      Solution checking tolerance for variables' integrality. Default 1e-5.

sol:chk:mode (solcheck, checkmode, chk:mode)
      Solution checking mode. Sum of a subset of the following bits:

      1 - Check variable bounds and integrality.
      2 - Check original model constraints, as well as any non-linear
      expression values reported by the solver.
      4 - Check intermediate auxiliary constraints (i.e., those which were
      reformulated further).
      8 - Check final auxiliary constraints sent to solver.
      16 - Check objective values.
      32, 64, 128, 256, 512 - similar, but non-linear expressions are
      recomputed (vs using their values reported by the solver.)
      *Experimental.* This is an idealistic check, because it does not
      consider possible tolerances applied by the solver when computing
      expression values.

      Default: 1+2+512.

sol:chk:prec (chk:prec, chk:precision)
      AMPL solution_precision option when checking: number of significant
      digits.

sol:chk:round (chk:round, chk:rnd)
      AMPL solution_round option when checking: round to this number of
      decimals after comma (before comma if negative.)

sol:count (countsolutions)
      0*/1: Whether to count the number of solutions and return it in the
      ".nsol" problem suffix.

sol:pooldualred (pooldualred)
      Whether to suppress removal of dominated solutions (via "dual
      reductions") when poolstub is specified:

      0 - Yes (default, can be expensive)
      1 - No
      2 - Honor presolveops bit 3 (2^3 = 8)

sol:pooldupcol (pooldupcol)
      Whether to suppress duplicate variable removal when poolstub is
      specified:

      0 - Yes (default, can be expensive)
      1 - No
      2 - Honor presolveops bit 3 (2^3 = 8)

sol:pooldups (poold/ups)
      How poolstub should handle duplicate solutions:

      0 - Retain all duplicates
      1 - Discard exact matches
      2 - Discard exact matches of continuous variables and matches of
          rounded values of discrete variables
      3 - Discard matches of rounded values of discrete variables (default)

      Rounding of discrete variables is affected bypoolmiptol and poolfeastol

sol:poolfeastol (poolfeastol)
      Zero tolerance for discrete variables in the solution pool (default
      1e-6)

sol:poollimit (poollimit, poolnbest)
      When poollimit = n > 1, the solution pool (see sol:stub) is allowed to
      keep n best solutions. Default 10.

sol:poolmiptol (poolmiptol)
      Error (nonintegrality) allowed in discrete variables in the solution
      pool (default 5e-6)

sol:report_uncertain (report_uncertain_sol)
      0/1*: whether to report objective value(s) in solve_message when
      solve_result is '?' (unknown).

sol:stub (ams_stub, solstub, solutionstub)
      Stub for solution files. If "solutionstub" is specified, found solutions
      are written to files ("solutionstub & '1' & '.sol'") ... ("solutionstub
      & Current.nsol & '.sol'"), where "Current.nsol" holds the number of
      returned solutions. That is, file names are obtained by appending 1, 2,
      ... "Current.nsol" to "solutionstub".

sys:xprs_gpuplatform (XPRS_GPUPLATFORM)
      Controls what kind of GPU support is enabled overall in Xpress.
      Individual solver components may disable GPU support.

      Values (default: 1, use GPU support if available, unless disabled by
      another control ):

      * (0) Do not use any GPU support.

      * (1) Use GPU support based on CUDA (if available).

tech:backgroundselect (backgroundselect, heur:xprs_backgroundselect, XPRS_BACKGROUNDSELECT)
      Bit-vector control (see Section Bit-vector controls) to select which
      tasks to run in background jobs (for example in parallel to the root cut
      loop).

      Values (default: -1):

      * (0) Feasibility jump heuristic.

      * (1) Fast branch-and-bound heuristic.

      * (2) Same as bit 1 but with some additional heuristics enabled.

      * (3) Fix-propagate-repair heuristic.

tech:backgroundthreads (backgroundmaxthreads, backgroundthreads, tech:xprs_backgroundmaxthreads, XPRS_BACKGROUNDMAXTHREADS)
      Limit the number of threads to use in background jobs (for example in
      parallel to the root cut loop).

      Default: -1, let Xpress decide.

tech:cputime (cputime, sys:xprs_cputime, XPRS_CPUTIME)
      How time should be measured when timings are reported in the log and
      when checking against time limits

      Values (default: 0):

      * (-1) Disable the timer.

      * (0) Use elapsed time.

      * (1) Use process time.

tech:debug (debug)
      0*/1: whether to assist testing & debugging, e.g., by outputting
      auxiliary information (mostly via suffixes).

tech:globalfileloginterval (globalfileloginterval, mip:xprs_treefileloginterval, XPRS_TREEFILELOGINTERVAL)
      This control sets the interval between progress messages output while
      writing tree data to the tree file, in seconds. The solve is slowed
      greatly while data is being written to the tree file and this output
      allows the user to see how much progress is being made.

      Default: 60

tech:globalfilemax (globalfilemax, tech:xprs_maxtreefilesize, XPRS_MAXTREEFILESIZE)
      The maximum size, in megabytes, to which the tree file may grow, or 0
      for no limit. When the tree file reaches this limit, a second tree file
      will be created. Useful if you are using a filesystem that puts a
      maximum limit on the size of a file.

      Default: 0

tech:logfile (logfile)
      Log file name; default=no file

tech:optionfile (optionfile, option:file)
      Name of an AMPL solver option file to read (surrounded by 'single' or
      "double" quotes if the name contains blanks). Lines that start with #
      are ignored. Otherwise, each nonempty line should contain "name=value",
      e.g., "lim:iter=500".

tech:outlev (outlev)
      Whether to write xpress log lines (chatter) to stdout and to file:

      0 - none
      1 - all
      2 - information
      3 - warnings & errors only (default)
      4 - errors
      5 - none

tech:outlev_mp (outlev_mp)
      0*/1: whether to print MP model information.

tech:sleeponthreadwait (sleeponthreadwait, sys:xprs_sleeponthreadwait, XPRS_SLEEPONTHREADWAIT)
      This parameter is deprecated and will be removed in a future release. In
      previous versions this was used to determine if the threads should be
      put into a wait state when waiting for work.

      Values (default: -1):

      * (-1) Automatically determined depending on the CPU the Optimizer is
        running on.

      * (0) Keep the threads busy when waiting for work.

      * (1) Put the threads into a wait state when waiting for work.

tech:threads (threads, tech:xprs_threads, XPRS_THREADS)
      The default number of threads used during optimization.

      Values (default: -1):

      * (-1) Determined automatically based on hardware configuration.

      * (>0) Number of threads to use.

tech:timing (timing, tech:report_times, report_times)
      0*/1/2: Whether to print and return timings for the run, all times are
      wall times. If set to 1, return the solution times in the problem
      suffixes 'time_solver', 'time_setup' and 'time', 'time'=
      time_solver+time_setup+time_output is a measure of the total time spent
      in the solver driver. If set to 2, return more granular times, including
      'time_read', 'time_conversion' and 'time_output'.

tech:tunebase (tunerdir, tunebase)
      Base name for results of running XPRESS's search for best parameter
      settings. The search is run only when tunebase is specified. This
      control only defines the root path for the tuner output. For each
      problem, the tuner result will be output to a subfolder underneath this
      path. For example, by default, the tuner result for a problem called
      prob will be located at tuneroutput/prob/

tech:tunename (tunesessionname)
      Set problem name within the tuner "tunebase" is specified.

tech:tuneoutput (tuneroutput, tuneoutput, tech:xprs_tuneroutput, XPRS_TUNEROUTPUT)
      Tuner: Whether to output tuner results and logs to the file system.

      Values (default: 1):

      * (0) Don't output to the file system.

      * (1) Output results and logs to the file system.

tech:tunerhistory (tunerhistory, tech:xprs_tunerhistory, XPRS_TUNERHISTORY)
      Tuner: Whether to reuse and append to previous tuner results of the same
      problem.

      Values (default: 2):

      * (0) Discard any previous tuner results.

      * (1) Append new results to the previous tuner results, but do not reuse
        them.

      * (2) Reuse the previous results and append new results to it.

tech:tunermethod (tunermethod, tech:xprs_tunermethod, XPRS_TUNERMETHOD)
      Tuner: Selects a factory tuner method. A tuner method consists of a list
      of controls with different settings that the tuner will evaluate and try
      to combine.

      Values (default: -1):

      * (-1) Automatically determined. The tuner will select the default
        method based on the problem type.

      * (0) Select the default LP tuner method.

      * (1) Select the default MIP tuner method.

      * (2) Select a more comprehensive MIP tuner method.

      * (3) Select a root-focus MIP tuner method.

      * (4) Select a tree-focus MIP tuner method.

      * (5) Select a simple MIP tuner method.

      * (6) Select the default SLP tuner method.

      * (7) Select the default MISLP tuner method.

      * (8) Select a MIP tuner method focussed on primal heuristics.

      * (9) Select the default Xpress Global tuner method.

tech:tunermethodread (tunermethodread)
      Read existing tuner method from the specified .xtm file, see
      "tunermethodwrite" to obtaing a template file

tech:tunermethodwrite (tunermethodwrite)
      Write existing tuner method from the specified .xtm file

tech:tunertarget (tunertarget, tech:xprs_tunertarget, XPRS_TUNERTARGET)
      Tuner: Defines the tuner target -- what should be evaluated when
      comparing two runs with different control settings.

      Values (default: -1):

      * (-1) Automatically determined. The tuner will choose the default
        target based on problem type.

      * (0) Solution time then gap. (MIP/MISLP default)

      * (1) Solution time then best bound.

      * (2) Solution time then best integer solution.

      * (3) The primal dual integral.

      * (4) Time only. (LP/SLP default)

      * (5) SLP objective only. (SLP/MISLP choice)

      * (6) SLP validation number only. (SLP/MISLP choice)

      * (7) Gap only.

      * (8) Best bound only.

      * (9) Best integer solution only.

      * (10) Best primal integral. (Only for individual instances, not for
        problem sets)

tech:tunerthreads (tunerthreads, tech:xprs_tunerthreads, XPRS_TUNERTHREADS)
      Tuner: the number of threads used by the tuner.

      Values (default: 1):

      * (-1) Choose automaticlly.

      * (1) The tuner will run in sequential.

      * (n>1) The tuner will run in parallel with n threads.

tech:tunerverbose (tunerverbose, tech:xprs_tunerverbose, XPRS_TUNERVERBOSE)
      Tuner: whether the tuner should prints detailed information for each
      run.

      Values (default: 1):

      * (1) Print extra information.

      * (0) Print less information.

tech:tunetimelim (tunermaxtime, tunetimelim, lim:tunetime, tech:xprs_tunermaxtime, XPRS_TUNERMAXTIME)
      Tuner: The maximum time in seconds that the tuner will run before it
      terminates.

      Values (default: 0):

      * (0) No time limit.

      * (>0) Stop the tuner after the given number of seconds.

tech:version (version)
      Single-word phrase: report version details before solving the problem.

tech:wantsol (wantsol)
      In a stand-alone invocation (no "-AMPL" on the command line), what
      solution information to write. Sum of

      1 - Write ".sol" file
      2 - Primal variables to stdout
      4 - Dual variables to stdout
      8 - Suppress solution message.

tech:writegraph (cvt:writegraph, writegraph, exportgraph)
      File to export conversion graph. Format: JSON Lines.

tech:writemodel (tech:writeprob, writeprob, writemodel, tech:exportfile)
      Specifies files where to export the model before solving (repeat the
      option for several files.) File name extensions can be ".lp[.7z]",
      ".mps", etc.
      To write a model during iterative solve (e.g., with obj:multi=2), use
      tech:writemodel:index.

tech:writemodel:index (tech:writeprob:index, writeprobindex, writemodelindex)
      During iterative solve (e.g., with obj:multi=2), the iteration before
      which to write solver model. 0 means before iteration is initialized;
      positive value - before solving that iteration. Default 0.

tech:writemodelonly (justwriteprob, justwritemodel)
      Specifies files where to export the model, no solving (option can be
      repeated.) File extensions can be ".dlp", ".mps", etc.

tech:writesolution (writesol, writesolution)
      Specifies the names of files where to export the solution and/or other
      result files in solver's native formats. Option can be repeated. File
      name extensions can be ".sol[.tar.gz]", ".json", ".bas", ".ilp", etc.

tech:xprs_callbackchecktimedelay (XPRS_CALLBACKCHECKTIMEDELAY)
      Minimum delay in milliseconds between two consecutive executions of the
      CHECKTIME callback in the same solution process

      Values (default: 0):

      * (0) Callback delay is disabled - the callback is executed every time;

      * (n>0) Callback invocation is suppressed if less than n milliseconds
        have passed since the last invocation.

tech:xprs_callbackchecktimeworkdelay (XPRS_CALLBACKCHECKTIMEWORKDELAY)
      Minimum delay in work units between two consecutive executions of the
      CHECKTIME callback in the same solution process

      Values (default: 0):

      * (0) Callback delay is disabled - the callback is executed every time;

      * (n>0) Callback invocation if less than n work units, which may be a
        fraction of a work unit, have passed since the last invocation.

tech:xprs_callbackfrommainthread (XPRS_CALLBACKFROMMAINTHREAD)
      Branch and Bound: specifies whether the MIP callbacks should only be
      called on the main thread.

      Values (default: 0):

      * (0) Invoke callbacks on worker threads during parallel MIP;

      * (1) Only ever invoke a callback on the thread that called
        XPRSmipoptimize.

tech:xprs_compute (XPRS_COMPUTE)
      Controls whether the next solve is performed directly or on an Insight
      Compute Interface.

      Values (default: Depends on environment):

      * (0) Solve locally.

      * (1) Solve using an Insight Compute Interface.

tech:xprs_computeexecservice (XPRS_COMPUTEEXECSERVICE)
      Selects the Insight execution service that will be used for solving
      remote optimizations.

      Default: Empty string

tech:xprs_computejobpriority (XPRS_COMPUTEJOBPRIORITY)
      Selects the priority that will be used for remote optimization jobs.

      Default: 0

tech:xprs_computelog (XPRS_COMPUTELOG)
      Controls how the run log is fetched when a solve is performed on an
      Insight Compute Interface.

      Values (default: 1):

      * (0) Run log will not be fetched

      * (1) Run log will be fetched in real-time

      * (2) Run log will be fetched at the end of the solve

      * (3) Run log will be fetched at the end of the solve if the solve fails
        with an error

tech:xprs_concurrentthreads (XPRS_CONCURRENTTHREADS)
      Determines the number of threads used by the concurrent solver.

      Values (default: -1):

      * (-1) Determined automatically

      * (>0) Number of threads to use.

tech:xprs_cpialpha (XPRS_CPIALPHA)
      decay term for confined primal integral computation.

      Default: 0

tech:xprs_deterministiclog (XPRS_DETERMINISTICLOG)
      Suppress non-deterministic log information in the standard MIP log. In
      particular, wall clock time stamps are replaced by (deterministic) work
      units.

      Values (default: 0):

      * (0) Report wall clock time stamps and other non-deterministic log
        information (the default)

      * (1) Suppress non-deterministic log information. In particular, report
        deterministic work units instead of time.

tech:xprs_escapenames (XPRS_ESCAPENAMES)
      If characters illegal to an mps or lp file should be escaped to
      guarantee readability, and whether escaped characters should be
      transformed back when reading such a file.

      Values (default: 1):

      * (0) Illegal characters are not escaped.

      * (1) Illegal characters are escaped.

tech:xprs_forceoutput (XPRS_FORCEOUTPUT)
      Certain names in the problem object may be incompatible with different
      file formats (such as names containing spaces for LP files). If the
      optimizer might be unable to read back a problem because of non-standard
      names, it will first attempt to write it out using an extended naming
      convention. If the names would not be possible to extend so that they
      would be reproducible and recognizable, it will give an error message
      and won't create the file. If the optimizer might be unable to read back
      a problem because of non-standard names, it will give an error message
      and won't create the file. This option may be used to force output
      anyway.

      Values (default: 0):

      * (0) Check format compatibility, and in case of failure try to extend
        names so that they are reproducible and recognizable.

      * (1) Force output using problem names as is.

      * (2) Always use 'x(' original name ')' in LP files to create a
        representation that can be read by Xpress. Default for problem having
        spaces in names

      * (3) Substitute spaces by the '_' character in LP files

tech:xprs_iotimeout (XPRS_IOTIMEOUT)
      The maximum number of seconds to wait for an I/O operation before it is
      cancelled.

      Default: 30

tech:xprs_mipabsgapnotify (XPRS_MIPABSGAPNOTIFY)
      Branch and bound: if the gapnotify callback has been set using
      XPRSaddcbgapnotify, then this callback will be triggered during the tree
      search when the absolute gap reaches or passes the value you set of the
      MIPRELGAPNOTIFY control.

      Default: -1.0

tech:xprs_mipabsgapnotifybound (XPRS_MIPABSGAPNOTIFYBOUND)
      Branch and bound: if the gapnotify callback has been set using
      XPRSaddcbgapnotify, then this callback will be triggered during the tree
      search when the best bound reaches or passes the value you set of the
      MIPRELGAPNOTIFYBOUND control.

      Default: 1.0E+20 (for minimization problems); -1.0E+20 (for maximization
      problems)

tech:xprs_mipabsgapnotifyobj (XPRS_MIPABSGAPNOTIFYOBJ)
      Branch and bound: if the gapnotify callback has been set using
      XPRSaddcbgapnotify, then this callback will be triggered during the tree
      search when the best solution value reaches or passes the value you set
      of the MIPRELGAPNOTIFYOBJ control.

      Default: -1.0E+20 (for minimization problems); 1.0E+20 (for maximization
      problems)

tech:xprs_miprelgapnotify (XPRS_MIPRELGAPNOTIFY)
      Branch and bound: if the gapnotify callback has been set using
      XPRSaddcbgapnotify, then this callback will be triggered during the
      branch and bound tree search when the relative gap reaches or passes the
      value you set of the MIPRELGAPNOTIFY control.

      Default: -1.0

tech:xprs_mps18compatible (XPRS_MPS18COMPATIBLE)
      Provides compatibility of MPS file output for older MPS readers.

      Values (default: 0):

      * (Bit 0) Do not write objective sense (OBJSENSE section).

      * (Bit 1) Fixed binaries are written as fixed only (unless used as a
        base variable for an indicator constraint).

tech:xprs_mpsboundname (XPRS_MPSBOUNDNAME)
      When reading an MPS file, this control determines which entries from the
      BOUNDS section will be read. As with all string controls, this is of
      length 64 characters plus a null terminator,

tech:xprs_mpsecho (XPRS_MPSECHO)
      Determines whether comments in MPS matrix files are to be printed out
      during matrix input.

      Values (default: 0):

      * (0) MPS comments are not to be echoed.

      * (1) MPS comments are to be echoed.

tech:xprs_mpsformat (XPRS_MPSFORMAT)
      Specifies the format of MPS files.

      Values (default: 1):

      * (-1) To determine the file type automatically.

      * (0) For fixed format.

      * (1) If MPS files are assumed to be in free format by input.

tech:xprs_mpsobjname (XPRS_MPSOBJNAME)
      When reading an MPS file, this control determines which neutral row will
      be read as the objective function. If this control is set when reading a
      multi-objective MPS file, only the named objective will be read; all
      other objectives will be ignored. As with all string controls, this is
      of length 64 characters plus a null terminator,

tech:xprs_mpsrangename (XPRS_MPSRANGENAME)
      When reading an MPS file, this control determines which entries from the
      RANGES section will be read. As with all string controls, this is of
      length 64 characters plus a null terminator,

tech:xprs_mpsrhsname (XPRS_MPSRHSNAME)
      When reading an MPS file, this control determines which entries from the
      RHS section will be read. As with all string controls, this is of length
      64 characters plus a null terminator,

tech:xprs_outputmask (XPRS_OUTPUTMASK)
      Mask to restrict the row and column names written to file. As with all
      string controls, this is of length 64 characters plus a null terminator,

tech:xprs_outputtol (XPRS_OUTPUTTOL)
      Zero tolerance on print values.

      Default: 1.0E-05

tech:xprs_serializepreintsol (XPRS_SERIALIZEPREINTSOL)
      Setting SERIALIZEPREINTSOL to 1 will ensure that the preintsol callback
      is always fired in a deterministic order during a parallel MIP solve.
      This applies only when the control DETERMINISTIC is set to 1.

      Values (default: 0):

      * (0) The preintsol callbacks will be fired asynchronously from
        different threads.

      * (1) The preintsol callbacks will be fired in a deterministic order.

tech:xprs_treememorylimit (XPRS_TREEMEMORYLIMIT)
      A soft limit, in megabytes, for the amount of memory to use in storing
      the branch and bound search tree. This doesn't include memory used for
      presolve, heuristics, solving the LP relaxation, etc. When set to 0 (the
      default), the optimizer will calculate a limit automatically based on
      the amount of free physical memory detected in the machine. When the
      memory used by the branch and bound tree exceeds this limit, the
      optimizer will try to reduce the memory usage by writing lower-rated
      sections of the tree to a file called the 'tree file'. Though the solve
      can continue if it cannot bring the tree memory usage below the
      specified limit, performance will be inhibited and a message will be
      printed to the log.

      Default: 0 (calculate limit automatically)

tech:xprs_tunermethodfile (XPRS_TUNERMETHODFILE)
      Tuner: Defines a file from which the tuner can read user-defined tuner
      method.

      Default: (empty)

tech:xprs_tunermode (XPRS_TUNERMODE)
      Tuner: Whether to always enable the tuner or disable it.

      Values (default: -1):

      * (-1) No effect.

      * (0) Always disable the tuner. XPRStune (TUNE) will have no effect.

      * (1) Always enable the tuner. XPRSmipoptimize (MIPOPTIMIZE),
        XPRSlpoptimize (LPOPTIMIZE), etc. will call the tuner before solving
        the problem.

tech:xprs_tuneroutputpath (XPRS_TUNEROUTPUTPATH)
      Tuner: Defines a root path to which the tuner writes the result file and
      logs.

      Default: tuneroutput

tech:xprs_tunerpermute (XPRS_TUNERPERMUTE)
      Tuner: Defines the number of permutations to solve for each control
      setting.

      Values (default: 0):

      * (0) Solve the original problem only for each setting.

      * (n>0) Solve the original problem and n permuted problems for each
        setting.

tech:xprs_tunersessionname (XPRS_TUNERSESSIONNAME)
      Tuner: Defines a session name for the tuner.

      Default: (empty)

tech:xprs_version (XPRS_VERSION)
      The Optimizer version number, e.g. 1301 meaning release 13.01.

      Default: Software version dependent

tech:xslp_calcthreads (XSLP_CALCTHREADS, NLPCALCTHREADS)
      Number of threads used for formula and derivatives evaluations

      Default: -1 (determined by XSLP_THREADS)

tech:xslp_deterministic (XSLP_DETERMINISTIC, NLPDETERMINISTIC)
      Determines if the parallel features of SLP should be guaranteed to be
      deterministic

      Default: 1

tech:xslp_ivname (XSLP_IVNAME, NLPIVNAME)
      Name of the set of initial values to be used

      Default: none

tech:xslp_keepequalscolumn (XSLP_KEEPEQUALSCOLUMN, NLPKEEPEQUALSCOLUMN)
      When set to a nonzero value, the MPS reader will keep the equals column
      in the problem

      Default: 0

tech:xslp_memoryfactor (XSLP_MEMORYFACTOR)
      Factor for expanding size of dynamic arrays in memory

      Default: 1.6

tech:xslp_multistart_threads (XSLP_MULTISTART_THREADS, MULTISTART_THREADS)
      The maximum number of threads to be used in multistart

      Default: -1 (determined by XSLP_THREADS)

tech:xslp_threads (XSLP_THREADS, NLPTHREADS)
      Default number of threads to be used

      Default: -1 (use XPRS_THREADS value)

tech:xslp_tolname (XSLP_TOLNAME, SLPTOLNAME)
      Name of the set of tolerance sets to be used

      Default: none

tol:xslp_cdtol_a (XSLP_CDTOL_A, SLPCDTOL_A)
      Absolute tolerance for deducing constant derivatives

      Default: 1.0e-08

tol:xslp_cdtol_r (XSLP_CDTOL_R, SLPCDTOL_R)
      Relative tolerance for deducing constant derivatives

      Default: 1.0e-08

tol:xslp_validationtol_r (XSLP_VALIDATIONTOL_R, NLPVALIDATIONTOL_R)
      Relative tolerance for the XSLPvalidate procedure

      Default: 0.00001

tol:xslp_zero (XSLP_ZERO, NLPZERO)
      Absolute tolerance

      Default: 1.0E-15

xktr:param_algorithm (XKTR_PARAM_ALGORITHM, KNITRO_PARAM_ALGORITHM)
      Indicates which algorithm to use to solve nonlinear problems

      Values (default: 0):

      * (0) (auto) let Knitro automatically choose an algorithm, based on the
        problem characteristics.

      * (1) (direct) use the Interior/Direct algorithm.

      * (2) (cg) use the Interior/CG algorithm.

      * (3) (active) use the Active Set algorithm.

      * (4) (sqp) use the SQP algorithm.

      * (5) (multi) run all algorithms, perhaps in parallel.

      * (6) (al) use the Augmented Lagrangian algorithm.

xktr:param_bar_directinterval (XKTR_PARAM_BAR_DIRECTINTERVAL, KNITRO_PARAM_BAR_DIRECTINTERVAL)
      Controls the maximum number of consecutive conjugate gradient (CG) steps
      before Knitro will try to enforce that a step is taken using direct
      linear algebra.

      Default: 10

xktr:param_bar_feasible (XKTR_PARAM_BAR_FEASIBLE, KNITRO_PARAM_BAR_FEASIBLE)
      Specifies whether special emphasis is placed on getting and staying
      feasible in the interior-point algorithms.

      Values (default: 0):

      * (0) (no) No special emphasis on feasibility.

      * (1) (stay) Iterates must satisfy inequality constraints once they
        become sufficiently feasible.

      * (2) (get) Special emphasis is placed on getting feasible before trying
        to optimize.

      * (3) (get_stay) Implement both options 1 and 2 above.

xktr:param_bar_feasmodetol (XKTR_PARAM_BAR_FEASMODETOL, KNITRO_PARAM_BAR_FEASMODETOL)
      Specifies the tolerance in equation that determines whether Knitro will
      force subsequent iterates to remain feasible.

      Default: 1.0e-4

xktr:param_bar_initmu (XKTR_PARAM_BAR_INITMU, KNITRO_PARAM_BAR_INITMU)
      Specifies the initial value for the barrier parameter : μ used with the
      barrier algorithms. This option has no effect on the Active Set
      algorithm.

      Default: 1.0e-1

xktr:param_bar_initpt (XKTR_PARAM_BAR_INITPT, KNITRO_PARAM_BAR_INITPT)
      Indicates whether an initial point strategy is used with barrier
      algorithms.

      Values (default: 0):

      * (0) (auto) Let Knitro automatically choose the strategy.

      * (1) (yes) Shift the initial slacks and multipliers to improve barrier
        algorithm performance.

      * (2) (no) Do no alter the initial slacks and multipliers.

xktr:param_bar_maxbacktrack (XKTR_PARAM_BAR_MAXBACKTRACK, KNITRO_PARAM_BAR_MAXBACKTRACK)
      Indicates the maximum allowable number of backtracks during the
      linesearch of the Interior/Direct algorithm before reverting to a CG
      step.

      Default: 3

xktr:param_bar_maxcrossit (XKTR_PARAM_BAR_MAXCROSSIT, KNITRO_PARAM_BAR_MAXCROSSIT)
      Specifies the maximum number of crossover iterations before termination.

      Default: 0

xktr:param_bar_maxrefactor (XKTR_PARAM_BAR_MAXREFACTOR, KNITRO_PARAM_BAR_MAXREFACTOR)
      Indicates the maximum number of refactorizations of the KKT system per
      iteration of the Interior/Direct algorithm before reverting to a CG
      step.

      Default: -1

xktr:param_bar_murule (XKTR_PARAM_BAR_MURULE, KNITRO_PARAM_BAR_MURULE)
      Indicates which strategy to use for modifying the barrier parameter mu
      in the barrier algorithms.

      Values (default: 0):

      * (0) (auto) Let Knitro automatically choose the strategy.

      * (1) (monotone) Monotonically decrease the barrier parameter. Available
        for both barrier algorithms.

      * (2) (adaptive) Use an adaptive rule based on the complementarity gap
        to determine the value of the barrier parameter. Available for both
        barrier algorithms.

      * (3) (probing) Use a probing (affine-scaling) step to dynamically
        determine the barrier parameter. Available only for the
        Interior/Direct algorithm.

      * (4) (dampmpc) Use a Mehrotra predictor-corrector type rule to
        determine the barrier parameter, with safeguards on the corrector
        step. Available only for the Interior/Direct algorithm.

      * (5) (fullmpc) Use a Mehrotra predictor-corrector type rule to
        determine the barrier parameter, without safeguards on the corrector
        step. Available only for the Interior/Direct algorithm.

      * (6) (quality) Minimize a quality function at each iteration to
        determine the barrier parameter. Available only for the
        Interior/Direct algorithm.

xktr:param_bar_pencons (XKTR_PARAM_BAR_PENCONS, KNITRO_PARAM_BAR_PENCONS)
      Indicates whether a penalty approach is applied to the constraints.

      Values (default: 0):

      * (0) (auto) Let Knitro automatically choose the strategy.

      * (1) (none) No constraints are penalized.

      * (2) (all) A penalty approach is applied to all general constraints.

xktr:param_bar_penrule (XKTR_PARAM_BAR_PENRULE, KNITRO_PARAM_BAR_PENRULE)
      Indicates which penalty parameter strategy to use for determining
      whether or not to accept a trial iterate.

      Values (default: 0):

      * (0) (auto) Let Knitro automatically choose the strategy.

      * (1) (single) Use a single penalty parameter in the merit function to
        weight feasibility versus optimality.

      * (2) (flex) Use a more tolerant and flexible step acceptance procedure
        based on a range of penalty parameter values.

xktr:param_bar_switchrule (XKTR_PARAM_BAR_SWITCHRULE, KNITRO_PARAM_BAR_SWITCHRULE)
      Indicates whether or not the barrier algorithms will allow switching
      from an optimality phase to a pure feasibility phase.

      Values (default: 0):

      * (0) (auto) Let Knitro determine the switching procedure.

      * (1) (never) Never switch to feasibility phase.

      * (2) (level1) Allow switches to feasibility phase.

      * (3) (level2) Use a more aggressive switching rule.

xktr:param_delta (XKTR_PARAM_DELTA, KNITRO_PARAM_DELTA)
      Specifies the initial trust region radius scaling factor used to
      determine the initial trust region size.

      Default: 1.0e0

xktr:param_feastol (XKTR_PARAM_FEASTOL, KNITRO_PARAM_FEASTOL)
      Specifies the final relative stopping tolerance for the feasibility
      error.

      Default: 1.0e-6

xktr:param_feastolabs (XKTR_PARAM_FEASTOLABS, KNITRO_PARAM_FEASTOLABS)
      Specifies the final absolute stopping tolerance for the feasibility
      error.

      Default: 0.0e0

xktr:param_gradopt (XKTR_PARAM_GRADOPT, KNITRO_PARAM_GRADOPT)
      Specifies how to compute the gradients of the objective and constraint
      functions.

      Values (default: 1):

      * (1) (exact) User provides a routine for computing the exact gradients.

      * (2) (forward) Knitro computes gradients by forward finite-differences.

      * (3) (central) Knitro computes gradients by central finite differences.

xktr:param_hessopt (XKTR_PARAM_HESSOPT, KNITRO_PARAM_HESSOPT)
      Specifies how to compute the (approximate) Hessian of the Lagrangian.

      Values (default: 0):

      * (0) (auto) Let Knitro make an automatic choice.

      * (1) (exact) User provides a routine for computing the exact Hessian.

      * (2) (bfgs) Knitro computes a (dense) quasi-Newton BFGS Hessian.

      * (3) (sr1) Knitro computes a (dense) quasi-Newton SR1 Hessian.

      * (4) (finite_diff) Knitro computes Hessian-vector products using
        finite-differences.

      * (5) (product) User provides a routine to compute the Hessian-vector
        products.

      * (6) (lbfgs) Knitro computes a limited-memory quasi-Newton BFGS Hessian
        (its size is determined by the option lmsize).

      * (7) (gauss_newton) Knitro computes a Gauss-Newton approximation of the
        hessian (available for least-squares only, and default value for
        least-squares)

xktr:param_honorbnds (XKTR_PARAM_HONORBNDS, KNITRO_PARAM_HONORBNDS)
      Indicates whether or not to enforce satisfaction of simple variable
      bounds throughout the optimization.

      Values (default: 2):

      * (0) (no) Knitro does not require that the bounds on the variables be
        satisfied at intermediate iterates.

      * (1) (always) Knitro enforces that the initial point and all subsequent
        solution estimates satisfy the bounds on the variables.

      * (2) (initpt) Knitro enforces that the initial point satisfies the
        bounds on the variables.

xktr:param_infeastol (XKTR_PARAM_INFEASTOL, KNITRO_PARAM_INFEASTOL)
      Specifies the (relative) tolerance used for declaring infeasibility of a
      model.

      Default: 1.0e-8

xktr:param_lmsize (XKTR_PARAM_LMSIZE, KNITRO_PARAM_LMSIZE)
      Specifies the number of limited memory pairs stored when approximating
      the Hessian using the limited-memory quasi-Newton BFGS option.

      Default: 10

xktr:param_maxcgit (XKTR_PARAM_MAXCGIT, KNITRO_PARAM_MAXCGIT)
      Specifies the number of limited memory pairs stored when approximating
      the Hessian using the limited-memory quasi-Newton BFGS option.

      Values (default: 0):

      * (0) Let Knitro automatically choose a value based on the problem size.

      * (n) At most n>0 CG iterations may be performed during one minor
        iteration of Knitro.

xktr:param_maxit (XKTR_PARAM_MAXIT, KNITRO_PARAM_MAXIT)
      Specifies the maximum number of iterations before termination.

      Values (default: 0):

      * (0) Let Knitro automatically choose a value based on the problem type.
        Currently Knitro sets this value to 10000 for LPs/NLPs and 3000 for
        MIP problems.

      * (n) At most n>0 iterations may be performed before terminating.

xktr:param_mip_branchrule (XKTR_PARAM_MIP_BRANCHRULE, KNITRO_PARAM_MIP_BRANCHRULE)
      Specifies which branching rule to use for MIP branch and bound
      procedure.

      Values (default: 0):

      * (0) (auto) Let Knitro automatically choose the branching rule.

      * (1) (most_frac) Use most fractional (most infeasible) branching.

      * (2) (pseudcost) Use pseudo-cost branching.

      * (3) (strong) Use strong branching (see options
        XKTR_PARAM_MIP_STRONG_CANDLIM, XKTR_PARAM_MIP_STRONG_LEVEL,
        XKTR_PARAM_MIP_STRONG_MAXIT for further control of strong branching
        procedure).

xktr:param_mip_gub_branch (XKTR_PARAM_MIP_GUB_BRANCH, KNITRO_PARAM_MIP_GUB_BRANCH)
      Specifies whether or not to branch on generalized upper bounds (GUBs).

      Values (default: 0):

      * (0) (no) Do not branch on GUBs.

      * (1) (yes) Allow branching on GUBs.

xktr:param_mip_heuristic (XKTR_PARAM_MIP_HEURISTIC, KNITRO_PARAM_MIP_HEURISTIC)
      Specifies which MIP heuristic search approach to apply to try to find an
      initial integer feasible point.

      Values (default: 0):

      * (0) (auto) Let Knitro choose the heuristic to apply (if any).

      * (1) (none) No heuristic search applied.

      * (2) (feaspump) Apply feasibility pump heuristic.

      * (3) (mpec) Apply heuristic based on MPEC formulation.

xktr:param_mip_implicatns (XKTR_PARAM_MIP_IMPLICATNS, KNITRO_PARAM_MIP_IMPLICATNS)
      Specifies whether or not to add constraints to the MIP derived from
      logical implications.

      Values (default: 1):

      * (0) (no) Do not add constraints from logical implications.

      * (1) (yes) Knitro adds constraints from logical implications.

xktr:param_mip_intgapabs (XKTR_PARAM_MIP_INTGAPABS, KNITRO_PARAM_INTGAPABS)
      The absolute integrality gap stop tolerance for MIP.

      Default: 1.0e-6

xktr:param_mip_intgaprel (XKTR_PARAM_MIP_INTGAPREL, KNITRO_PARAM_INTGAPREL)
      The relative integrality gap stop tolerance for MIP.

      Default: 1.0e-6

xktr:param_mip_knapsack (XKTR_PARAM_MIP_KNAPSACK, KNITRO_PARAM_MIP_KNAPSACK)
      Specifies rules for adding MIP knapsack cuts.

      Values (default: 1):

      * (0) (none) Do not add knapsack cuts.

      * (1) (ineqs) Add cuts derived from inequalities only.

      * (2) (ineqs_eqs) Add cuts derived from both inequalities and
        equalities.

xktr:param_mip_lpalg (XKTR_PARAM_MIP_LPALG, KNITRO_PARAM_MIP_LPALG)
      Specifies which algorithm to use for any linear programming (LP)
      subproblem solves that may occur in the MIP branch and bound procedure.

      Values (default: 0):

      * (0) (auto) Let Knitro automatically choose an algorithm, based on the
        problem characteristics.

      * (1) (direct) Use the Interior/Direct (barrier) algorithm.

      * (2) (cg) Use the Interior/CG (barrier) algorithm.

      * (3) (active) Use the Active Set (simplex) algorithm.

xktr:param_mip_maxnodes (XKTR_PARAM_MIP_MAXNODES, KNITRO_PARAM_MIP_MAXNODES)
      Specifies the maximum number of nodes explored.

      Default: 100000

xktr:param_mip_method (XKTR_PARAM_MIP_METHOD, KNITRO_PARAM_MIP_METHOD)
      Specifies which MIP method to use.

      Values (default: 0):

      * (0) (auto) Let Knitro automatically choose the method.

      * (1) (BB) Use the standard branch and bound method.

      * (2) (HQG) Use the hybrid Quesada-Grossman method (for convex,
        nonlinear problems only).

xktr:param_mip_outinterval (XKTR_PARAM_MIP_OUTINTERVAL, KNITRO_PARAM_MIP_OUTINTERVAL)
      Specifies node printing interval for XKTR_PARAM_MIP_OUTLEVEL when
      XKTR_PARAM_MIP_OUTLEVEL > 0.

      Values (default: 10):

      * (0) Print output every node.

      * (2) Print output every 2nd node.

      * (N) Print output every Nth node.

xktr:param_mip_outlevel (XKTR_PARAM_MIP_OUTLEVEL, KNITRO_PARAM_MIP_OUTLEVEL)
      Specifies how much MIP information to print.

      Values (default: 1):

      * (0) (none) Do not print any MIP node information.

      * (1) (iters) Print one line of output for every node.

xktr:param_mip_pseudoinit (XKTR_PARAM_MIP_PSEUDOINIT, KNITRO_PARAM_MIP_PSEUDOINIT)
      Specifies the method used to initialize pseudo-costs corresponding to
      variables that have not yet been branched on in the MIP method.

      Values (default: 0):

      * (0) Let Knitro automatically choose the method.

      * (1) Initialize using the average value of computed pseudo-costs.

      * (2) Initialize using strong branching.

xktr:param_mip_rootalg (XKTR_PARAM_MIP_ROOTALG, KNITRO_PARAM_MIP_ROOTALG)
      Specifies which algorithm to use for the root node solve in MIP (same
      options as XKTR_PARAM_ALGORITHM user option).

      Default: 0

xktr:param_mip_rounding (XKTR_PARAM_MIP_ROUNDING, KNITRO_PARAM_MIP_ROUNDING)
      Specifies the MIP rounding rule to apply.

      Values (default: 0):

      * (0) (auto) Let Knitro choose the rounding rule.

      * (1) (none) Do not round if a node is infeasible.

      * (2) (heur_only) Round using a fast heuristic only.

      * (3) (nlp_sometimes) Round and solve a subproblem if likely to succeed.

      * (4) (nlp_always) Always round and solve a subproblem.

xktr:param_mip_selectrule (XKTR_PARAM_MIP_SELECTRULE, KNITRO_PARAM_MIP_SELECTRULE)
      Specifies the MIP select rule for choosing the next node in the branch
      and bound tree.

      Values (default: 0):

      * (0) (auto) Let Knitro choose the node selection rule.

      * (1) (depth_first) Search the tree using a depth first procedure.

      * (2) (best_bound) Select the node with the best relaxation bound.

      * (3) (combo_1) Use depth first unless pruned, then best bound.

xktr:param_mip_strong_candlim (XKTR_PARAM_MIP_STRONG_CANDLIM, KNITRO_PARAM_MIP_STRONG_CANDLIM)
      Specifies the maximum number of candidates to explore for MIP strong
      branching.

      Default: 10

xktr:param_mip_strong_level (XKTR_PARAM_MIP_STRONG_LEVEL, KNITRO_PARAM_MIP_STRONG_LEVEL)
      Specifies the maximum number of tree levels on which to perform MIP
      strong branching.

      Default: 10

xktr:param_mip_strong_maxit (XKTR_PARAM_MIP_STRONG_MAXIT, KNITRO_PARAM_MIP_STRONG_MAXIT)
      Specifies the maximum number of iterations to allow for MIP strong
      branching solves.

      Default: 1000

xktr:param_objrange (XKTR_PARAM_OBJRANGE, KNITRO_PARAM_OBJRANGE)
      Specifies the extreme limits of the objective function for purposes of
      determining unboundedness.

      Default: 1.0e20

xktr:param_opttol (XKTR_PARAM_OPTTOL, KNITRO_PARAM_OPTTOL)
      Specifies the final relative stopping tolerance for the KKT (optimality)
      error.

      Default: 1.0e-6

xktr:param_opttolabs (XKTR_PARAM_OPTTOLABS, KNITRO_PARAM_OPTTOLABS)
      Specifies the final absolute stopping tolerance for the KKT (optimality)
      error.

      Default: 0.0e0

xktr:param_outlev (XKTR_PARAM_OUTLEV, KNITRO_PARAM_OUTLEV)
      Controls the level of output produced by Knitro.

      Values (default: 2):

      * (0) (none) Printing of all output is suppressed.

      * (1) (summary) Print only summary information.

      * (2) (iter_10) Print basic information every 10 iterations.

      * (3) (iter) Print basic information at each iteration.

      * (4) (iter_verbose) Print basic information and the function count at
        each iteration.

      * (5) (iter_x) Print all the above, and the values of the solution
        vector x.

      * (6) (all) Print all the above, and the values of the constraints c at
        x and the Lagrange multipliers lambda.

xktr:param_presolve (XKTR_PARAM_PRESOLVE, KNITRO_PARAM_PRESOLVE)
      Determine whether or not to use the Knitro presolver to try to simplify
      the model by removing variables or constraints. Specifies conditions for
      terminating the MIP algorithm.

      Values (default: 1):

      * (0) (none) Do not use Knitro presolver.

      * (1) (basic) Use the Knitro basic presolver.

xktr:param_presolve_tol (XKTR_PARAM_PRESOLVE_TOL, KNITRO_PARAM_PRESOLVE_TOL)
      Determines the tolerance used by the Knitro presolver to remove
      variables and constraints from the model.

      Default: 1.0e-6

xktr:param_scale (XKTR_PARAM_SCALE, KNITRO_PARAM_SCALE)
      Performs a scaling of the objective and constraint functions based on
      their values at the initial point.

      Values (default: 1):

      * (0) (no) No scaling is performed.

      * (1) (yes) Knitro is allowed to scale the objective function and
        constraints.

xktr:param_soc (XKTR_PARAM_SOC, KNITRO_PARAM_SOC)
      Specifies whether or not to try second order corrections (SOC).

      Values (default: 1):

      * (0) (no) No second order correction steps are attempted.

      * (1) (maybe) Second order correction steps may be attempted on some
        iterations.

      * (2) (yes) Second order correction steps are always attempted if the
        original step is rejected and there are nonlinear constraints.

xktr:param_soltype (XKTR_PARAM_SOLTYPE, KNITRO_PARAM_SOLTYPE)
      This option specifies the solution returned by Knitro. Generally, the
      solution converged to by Knitro is a locally optimal solution that
      corresponds to the best feasible solution found. However, on rare
      occasions, Knitro may enounter a feasible solution during the
      optimization process that has a better objective value than the final
      solution converged to by Knitro. Setting soltype = 1 in this case will
      return this iterate.

      Values (default: 0):

      * (0) (final) Always return the final solution to which Knitro
        converges.

      * (1) (bestfeas) Always return the best feasible solution encountered
        during the optimization.

xktr:param_xtol (XKTR_PARAM_XTOL, KNITRO_PARAM_XTOL)
      The optimization process will terminate if the relative change in all
      components of the solution point estimate is less than xtol.

      Default: 1.0e-15
```

