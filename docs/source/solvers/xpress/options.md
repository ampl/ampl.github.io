
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

 Options:

acc:abs
      Solver acceptance level for 'AbsConstraint', default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:and (acc:forall)
      Solver acceptance level for 'AndConstraint', default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:indeq (acc:indlineq)
      Solver acceptance level for 'IndicatorConstraintLinEQ', default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:indge (acc:indlinge)
      Solver acceptance level for 'IndicatorConstraintLinGE', default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:indle (acc:indlinle)
      Solver acceptance level for 'IndicatorConstraintLinLE', default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:max
      Solver acceptance level for 'MaxConstraint', default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:min
      Solver acceptance level for 'MinConstraint', default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:or (acc:exists)
      Solver acceptance level for 'OrConstraint', default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:quadeq
      Solver acceptance level for 'QuadConEQ', default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:quadge
      Solver acceptance level for 'QuadConGE', default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:quadle
      Solver acceptance level for 'QuadConLE', default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:sos2
      Solver acceptance level for 'SOS2Constraint', default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

alg:addcutoff (addcutoff, mipaddcutoff)
      Amount to add to the objective function of the best integer

      solution found to give the new MIP cutoff; default -1e-5.

alg:basis (basis)
      Whether to use or return a basis:

      0 - No
      1 - Use incoming basis (if provided)
      2 - Return final basis
      3 - Both (1 + 2 = default)

alg:clamping (clamping)
      Control adjustements of the returned solution values such that they are
      always within bounds:

      -1 - Determined automatically
      0  - Adjust primal solution to always be within primal bounds (default)
      1  - Adjust primal slack values to always be within constraint bounds
      2  - Adjust dual solution to always be within the dual bounds implied
           by the slacks
      3  - Adjust reduced costs to always be within dual bounds implied by
           the primal solution

alg:cutoff (cutoff)
      If the optimal objective value is worse than cutoff, report "objective
      cutoff" and do not return a solution. Default: 1.0E+40 for minimizing,
      -1.0E+40 for maximizing.

alg:feastol (feastol)
      Primal feasibility tolerance (default 1e-6).

alg:feastolperturb (feastolperturb)
      How much a feasible primal basic solution is allowed to be perturbed
      when performing basis changes. The tolerance specified by "alg:feastol"
      is always considered as an upper limit for the perturbations; default =
      1.0E-06

alg:feastoltarget (feastoltarget)
      Specifies the target feasibility tolerance for the solution refiner.
      Default = 0 (use the value of "alg:feastol")

alg:iisfind (iisfind, iis)
      Whether to find and export an IIS. Default = 0 (don't export).

alg:indlinbigm (indlinbigm)
      Largest "big M" value to use in converting indicator constraints to
      regular constraints, default = 1e5

alg:lpfolding (lpfolding)
      Simplex and barrier: whether to fold an LP problem before solving it:
      .. value-table:

alg:maxiis (maxiis)
      Maximum number of IIS to find; default=-1 (no limit)

alg:method (method, lpmethod, defaultalg)
      Which algorithm to use for non-MIP problems or for the root node of MIP
      problems:

      1 - Automatic choice (default)
      2 - Dual simplex
      3 - Primal simplex
      4 - Netwon Barrier

alg:randomseed (randomseed)
      Sets the initial seed to use for the pseudo-random number generator in
      the Optimizer; default=1

alg:refactor (refactor)
      Whether the optimization should restart using the current representation
      of the factorization in memory:

      -1 - Automatic choice (default)
      0  - No
      1  - Yes.

alg:refineops (refineops)
      Bit vector: specifies wmhen the solution refiner should be executed to
      reduce solution infeasibilities. The refiner will attempt to satisfy the
      target tolerances for all original linear constraints before presolve or
      scaling has been applied:

      1    - refine optimal LP solutions
      2    - refine MIP solutions
      8    - refine each node of the search tree
      16   - refine non-global solutions
      32   - apply the iterative refiner to refine the solution
      64   - use higher precision in the iterative refinement
      128  - iterative refiner will use the primal simplex algorithm
      256  - iterative refiner will use the dual simplex algorithm
      512  - refine MIP solutions such that rounding them keeps the problem
             feasible when reoptimized
      1024 - ttempt to refine MIP solutions such that rounding them keeps the
             problem feasible when reoptimized, but accept integers solutions
             even if refinement fails

alg:relax (relax)
      0*/1: Whether to relax integrality of variables.

alg:relcutoff (relcutoff, miprelcutoff)
      If the optimal objective value is (relatively) worse than relcutoff,
      report "objective cutoff" and do not return a solution. Default: 1.0E-4.

alg:resourcestrategy (resourcestrategy)
      Wether to allow nondeterministic decisions to cope with low memory
      (affected by maxmemory and maxmemoryhard):

      0 - No (default)
      1 - Yes.

alg:start (warmstart)
      Whether to use incoming primal (and dual, for LP) variable values in a
      warmstart:

      0 - No
      1 - Yes (for LP: if there is no incoming alg:basis) (default)
      2 - Yes (for LP: ignoring the incoming alg:basis, if any.)

alg:zerotol (matrixtol)
      The zero tolerance on matrix elements. If the value of a matrix element
      is less than or equal to this in absolute value, it is treated as zero,
      default=1e-9.

bar:alg (baralg)
      Which barrier algorithm to use

bar:cachesize (cachesize)
      Newton Barrier: L2 or L3 (see notes) cache size in kB (kilobytes) of the
      CPU (default -1). On Intel (or compatible) platforms a value of -1 may
      be used to determine the cache size automatically.

bar:choleskyalg (choleskyalg)
      Type of Cholesky factorization used for barrier, sum of:
      :

bar:choleskytol (choleskytol)
      Zero tolerance for Cholesky pivots in the

      Newton Barrier algorithm; default = 1e-15

bar:cores (barcores)
      If positive, number of CPU cores to assume present when using the
      barrier algorithm. Default = -1, which means automatic choice

bar:corespercpu (corespercpu)
      Newton Barrier: number of cores to assume per cpu. Barrier cache =
      cachesize/corespercpu. Default -1 = automatic.

bar:cpuplatform (cpuplatform)
      Which instruction are allowed to the Newton barrier method:
      :

bar:crash (barcrash)
      Choice of crash procedure for crossover, higher number means more
      aggressive procedure:

bar:crossover (crossover)
      How to transform a barrier solution to a basic one:

      -1 - automatic choice (default)
      0  - none: return an interior solution
      1  - primal crossover first
      2  - dual crossover first

bar:crossoverops (crossoverops)
      Bit vector affecting crossover after the barrier algorithm; sum of:

      1 - return the barrier solution (rather than the last intermediate
          solution) when crossover stop early
      2 - skip the second crossover stage
      4 - skip pivots that are "less numerically reliable"
      8 - do a slower but more numerically stable crossover

bar:crossoverthreads (crossoverthreads)
      Limit on threads used during crossover; default -1 (determined by
      bar:threads).

bar:crossovertol (crossovertol, crossoveraccuracytol)
      Tolerance (default 1e-6) for deciding whether to adjust the relative
      pivot tolerance during crossover when a new basis factorization is
      necessary. Errors in the recalculated basic solution above this
      tolerance cause the pivot tolerance to be adjusted.

bar:densecollimit (densecollimit)
      Number of nonzeros above which a column is treated as dense in the
      barrier algorithm's Cholesky factorization. Default=0 (automatic).

bar:dualstop (bardualstop)
      Barrier method convergence tolerance on dual infeasibilities; default =
      0 (automatic choice)

bar:gap (bargaptarget)
      Barrier algorithm target tolerance for the relative duality gap.If not
      satisfied and no further progress is possible but barstopgap is
      satisfied, then the current solution is considered optimal.

bar:gapstop (bargapstop)
      Barrier method convergence tolerance on the relative duality gap;
      default = 0

bar:indeflimit (barindeflimit)
      Maximum indefinite factorizations to allow in the barrier algorithm for
      solving a QP: stop when the limit is hit default = 15

bar:kernel (barkernel)
      How the barrier algorithm weights centrality:

      >= +1.0 - More emphasis on centrality (default 1.0)
      <= -1.0 - Each iteration, adaptively select a value from [+1,
                -barkernel]

bar:l1cache (l1cache)
      Newton barrier: L1 cache size in kB (kilo bytes) of the CPU. On Intel
      (or compatible) platforms a value of -1 may be used to determine the
      cache size automatically.

bar:objperturb (barobjperturb)
      Defines how the barrier perturbs the objective (default 1e-6); values >
      0 let the optimizer decide if to perturb the objective, values < 0 force
      the perturbation:

      n > 0 - automatic decison, scale n
      n = 0 - turn off perturbation
      n < 0 - force perturbation by abs(n)

bar:objscale (barobjscale)
      How the barrier algorithm scales the objective; when the objective is
      quadratic, the quadratic diagonal is used in determining the scale:

      -1  - Automatic choice (default)
      0   - Scale by the geometric mean of the objective coefficients
      > 0 - Scale so the argest objective coefficient in absolute value is <=
            barobjscale.

bar:order (barorder)
      Cholesky factorization pivot order for barrier algorithm:

      0 - automatic choice(default)
      1 - minimum degree
      2 - minimum local fill
      3 - nested dissection

bar:orderthreads (barorderthreads)
      Number of threads to use when choosing a pivot order for Cholesky
      factorization; default 0 (automatic choice).

bar:output (baroutput)
      Amount of output for the barrier method:

      0 - no output
      1 - each iteration (default)

bar:presolve (barpresolve)
      Level of barrier-specific presolve effort:

      0 - no output
      1 - each iteration (default)

bar:primalstop (barprimalstop)
      Barrier method convergence tolerance on primal infeasibilities; default
      = 0 (automatic choice)

bar:refiter (barrefiter)
      Maximum number of refinement iterations, helpful when the the solution
      is near to the optimum using barrier or crossover:

      0     - default
      n > 0 - perform n refinement iterations

bar:regularize (barreg, barrregularize)
      Regularization to use with "barrier. Default=-1 (automatic choice), else
      sum of:

      1 - use "standard" regularization
      2 - use "reduced" regularization: less perturbation than "standard"
          regularization
      4 - keep dependent rows in the KKT system
      8 - keep degenerate rows in the KKT system

bar:start (barstart)
      Choice of starting point for barrier method:

      -1 - Use incoming solution for warm start
      0  - Automatic choice (default)
      1  - Heuristics based on magnitudes of matrix entries
      2  - Use pseudoinverse of constraint matrix
      3  - Unit starting point for homogeneous self - dual barrier algorithm.

bar:stepstop (barstepstop)
      Barrier method convergence tolerance: stop when step size <=
      barstepstop; default = 1e-10

bar:threads (threads)
      number of threads used in the Newton Barrier algorithm;

      default = -1 (determined by "threads")

cut:cover (covercuts)
      The number of rounds of lifted cover inequalities at the top
      node.Default=-1, automatic.

cut:depth (cutdepth)
      Maximum MIP tree depth at which to generate cuts. Default -1
      (automatic); a value of 0 will disable cuts generation.

cut:factor (cutfactor)
      Limit on number of cuts and cut coefficients added while solving MIPs.
      Default=-1 (automatic); a value of 0 will disable cuts generation.

cut:freq (cutfreq)
      Cuts are only generated at tree depths that are integer

      multiples of cutfreq. Default=-1 (automatic choice).

cut:gomory (gomcuts)
      The number of rounds of Gomory or lift-and-project cuts at the top
      node.Default=-1, automatic.

cut:lnpbest (lnpbest)
      Number of infeasible global entities to create lift-and-project cuts for
      during each round of Gomory cuts at the top node

cut:lnpiterlimit (lnpiterlimit)
      Number of iterations to perform in improving each lift-and-project cut;
      default=-1 (automatic)

cut:qccuts (qccuts)
      when using miqcpalg=1 to solve a mixed-integer problem that has
      quadratic constraints or second-order cone constraints, the number of
      rounds of outer approximation cuts at the top node; default = -1
      (automatic choice).

cut:select (cutselect)
      Detailed control of cuts at MIP root node; sum of:

      32     - clique cuts
      64     - mixed - integer founding(MIR) cuts
      128    - lifted cover cuts
      2048   - flow path cuts
      4096   - implication cuts
      8192   - automatic lift - and -project strategy
      16384  - disable cutting from cut rows
      32768  - lifted GUB cover cuts
      65536  - zero - half cuts
      131072 - indicator - constraint cuts
      -1     - all available cuts(default)

cut:strategy (cutstrategy)
      How aggressively to generate MIP cuts; more ==> fewer nodes but more
      time per node:

      -1 - automatic (default)
      0  - no cuts
      1  - conservative strategy
      2  - moderate strategy
      3  - aggressive strategy

cut:treecover (treecovercuts)
      The number of rounds of lifted cover inequalities at MIP nodes other
      than the top node. Default=-1 (automatic).

cut:treegomory (treegomcuts)
      The number of rounds of Gomory or lift-and-project cuts at MIP nodes
      other than the top node. Default=-1 (automatic).

cut:treeqccuts (treeqccuts)
      when using miqcpalg=1 to solve a MIP that has quadratic constraints or
      second-order cone constraints, the number of rounds of outer
      approximation cuts during the tree search; default = -1 (automatic
      choice).

cut:treeselect (treecutselect)
      Detailed control of cuts created during the tree search; sum of:

      32     - clique cuts
      64     - mixed - integer founding(MIR) cuts
      128    - lifted cover cuts
      2048   - flow path cuts
      4096   - implication cuts
      8192   - automatic lift - and -project strategy
      16384  - disable cutting from cut rows
      32768  - lifted GUB cover cuts
      65536  - zero - half cuts
      131072 - indicator - constraint cuts
      -1     - all available cuts(default)

cvt:bigM (cvt:bigm, cvt:mip:bigM, cvt:mip:bigm)
      Default value of big-M for linearization of logical constraints. Not
      used by default. Use with care (prefer tight bounds). Should be smaller
      than (1.0 / [integrality tolerance])

cvt:mip:eps (cvt:cmp:eps)
      Tolerance for strict comparison of continuous variables for MIP. Ensure
      larger than the solver's feasibility tolerance.

cvt:plapprox:domain (plapprox:domain, plapproxdomain)
      For piecewise-linear approximated functions, both arguments and result
      are bounded to +-[pladomain]. Default 1e6.

cvt:plapprox:reltol (plapprox:reltol, plapproxreltol)
      Relative tolerance for piecewise-linear approximation. Default 0.01.

cvt:pre:all
      0/1*: Set to 0 to disable most presolve in the flat converter.

cvt:pre:eqbinary
      0/1*: Preprocess reified equality comparison with a binary variable.

cvt:pre:eqresult
      0/1*: Preprocess reified equality comparison's boolean result bounds.

cvt:quadcon (passquadcon)
      0/1*: Multiply out and pass quadratic constraint terms to the solver,
      vs. linear approximation.

cvt:quadobj (passquadobj)
      0/1*: Multiply out and pass quadratic objective terms to the solver, vs.
      linear approximation.

cvt:sos (sos)
      0/1*: Whether to honor declared suffixes .sosno and .ref describing SOS
      sets. Each distinct nonzero .sosno value designates an SOS set, of type
      1 for positive .sosno values and of type 2 for negative values. The .ref
      suffix contains corresponding reference values used to order the
      variables.

cvt:sos2 (sos2)
      0/1*: Whether to honor SOS2 constraints for nonconvex piecewise-linear
      terms, using suffixes .sos and .sosref provided by AMPL.

lim:bariterlim (bar:iterlim, bariterlim)
      Limit on the number of barrier iterations (default 500).

lim:crossoveriterlim (bar:crossoveriterlim, crossoveriterlim, crossoveritlim)
      Limit on crossover iterations after the barrier algorithm; default =
      2147483645

lim:heurdiveiterlimit (heurdepth, mip:heurdiveiterlimit)
      Simplex iteration limit for reoptimizing during the diving heuristic;
      default = -1 (automatic selection); a value of 0 implies no iteration
      limit

lim:lpiterlimit (lpiterlimit)
      The maximum number of iterations that will be performed by primal
      simplex or dual simplex before the optimization process terminates. For
      MIP problems, this is the maximum total number of iterations over all
      nodes.

lim:lprefineiterlimit (lprefineiterlimit)
      This specifies the simplex iteration limit the solution refiner can
      spend in attempting to increase the accuracy of an LP solution;
      default=-1 (automatic).

lim:maxcuttime (maxcuttime)
      The maximum amount of time allowed for generation of cutting planes and
      reoptimization;default=0 (no time limit)

lim:maxmipsol (maxmipsol)
      Limit on the number of MIP solutions to be found (default no limit).

lim:maxstalltime (maxstalltime)
      Maximum time in seconds that the MIP Optimizer will continue to search
      for improving solution after finding a new incumbent, default=0 (no
      limit)

lim:mem (memlimit, maxmemoryhard)
      Hard limit (integer number of MB) on memory allocated, causing early
      termination if exceeded; default = 0 (no limit)

lim:nodes (nodelim, nodelimit, maxnode)
      Maximum MIP nodes to explore (default: 2147483647).

lim:softmem (softmemlimit, maxmemorysoft)
      Soft limit (integer number of MB) on memory allocated; default = 0 (no
      limit)

lim:soltime (soltimelim, soltimelimit)
      Limit on solve time (in seconds; default: no limit) to be applied only
      after a solution has been found.

lim:time (timelim, timelimit)
      Limit on solve time (in seconds; default: no limit).

lp:bigm (bigm, bigmpenalty)
      Infeasibility penalty to be used if "BigM" method is used; default =
      1024

lp:bigmmethod (bigmmethod)
      Simplex: This specifies whether to use the "Big M" method, or the
      standard phase I (achieving feasibility) and phase II (achieving
      optimality). the "Big M" method, the objective coefficients of the
      variables are considered during the feasibility phase, possibly leading
      to an initial feasible basis which is closer to optimal. The
      side-effects involve possible round-off errors.

      0 - phase I / II
      1 - bigM method (default)

lp:crash (crash)
      Simplex: This determines the type of crash used when the algorithm
      begins.For primal simplex, the choices are listed below; for dual
      simplex the choices follow and are interpreted a bit-vector:

      0        - none
      1        - one-pass search for singletons
      2        - multi-pass search for singletons
      3        - multi-pass search including slacks
      4        - at most 10 passes, only considering slacks at the end
      n>10     - like 4, but at most n-10 passes
      0 (dual) - perform standard crash.
      1 (dual) - perform additional numerical checks during crash
      2 (dual) - extend the set of column candidates for crash
      3 (dual) - extend the set of row candidates for crash
      4 (dual) - force crash

lp:dualforceparallel (forceparalleldual, dualforceparallel)
      Specifies whether the dual simplex solver should always use the parallel
      simplex algorithm

lp:dualgradient (dualgradient)
      dual simplex pricing strategy:

      -1 - automatic (default)
      0  - devex
      1  - steepest edge
      2  - direct steepest edge
      3  - sparse devex

lp:dualize (dualize)
      Whether to convert the primal problem to its dual and solve the
      converted problem:

      -1 - automatic (default)
      0  - solve the primal problem
      1  - solve the dual problem

lp:dualizeops (dualizeops)
      When solving the dual problem after deriving it from the primal, whether
      to use primal simplex if dual simplex was specified and vice versa:

      0 - No
      1 - Yes (default)

lp:dualperturb (dualperturb)
      Factor by which the problem will be perturbed prior to optimization by
      dual simplex. Default -1 (automatic); note that a value of 0 implies no
      perturbation

lp:dualstrategy (dualstrategy)
      Bit vector controlling the dual simplex strategy (default 1):

      1  - switch to primal when dual infeasible
      2  - stop the solve instead of switching to primal
      4  - use aggressive cut-off in MIP search
      8  - use dual simplex to remove cost perturbations
      16 - aggressive dual pivoting
      32 - keep using dual simplex even when numerically unstable

lp:dualthreads (dualthreads)
      Limit on threads used by parallel dual simplex; default -1 (determined
      by tech:threads).

lp:etatol (etatol)
      Zero tolerance on eta elements, elements of eta vectors whose absolute
      value is smaller than etatol are taken to be zero.

lp:invertfreq (invertfreq)
      Maximum simplex iterations before refactoring the basis; default -1
      (automatic)

lp:invertmin (invertmin)
      Minimum simplex iterations before refactoring the basis; default = 3

lp:keepbasis (keepbasis)
      Basis choice for the next LP iteration:

      0 - ignore previous basis
      1 - use previous basis (default)
      2 - use previous basis only if the number of basic variables == number
          of constraints

lp:keepnrows (keepnrows)
      Status for nonbinding rows:

      -1 - delete N type rows from the matrix (default)
      0  - delete elements from N type rows leaving empty N type rows in the
           matrix
      1  - keep N type rows

lp:log (lplog)
      Frequency of printing simplex iteration log; default = 100.Values n < 0
      display detailed outputs every -n iterations.

lp:netstalllimit (netstalllimit)
      Limit the number of degenerate pivots of the network simplex algorithmm
      before switching to primal or dual:

      -1    - automatic (default)
      0     - no limit
      n > 0 - limit to n network simplex iterations

lp:optimalitytol (optimalitytol)
      This is the zero tolerance for reduced costs. On each iteration, the
      simplex method searches for a variable to enter the basis which has a
      negative reduced cost. The candidates are only those variables which
      have reduced costs less than the negative value of optimalitytol;
      default=1e-6

lp:optimalitytoltarget (optimalitytoltarget)
      Target optimality tolerance for the solution refiner; default=0 (use the
      value specified by lp:optimalitytol)

lp:penalty (penalty)
      Minimum absolute penalty variable coefficient; default = automatic
      choice

lp:pivtol (pivtol, markowitztol)
      Markowitz pivot tolerance (default = 0.01)

lp:pricingalg (pricingalg)
      Primal simplex pricing method:

      -1 - partial pricing
      0  - automatic choice (default)
      1  - devex pricing
      2  - steepest edge
      3  - steepest edge with initial weights

lp:primalunshift (primalunshift)
      Whether the primal alg. calls the dual to unshift:

      0 - No
      1 - Yes (default)

lp:relpivottol (relpivottol)
      Relative pivot tolerance; default = 1e-6

lp:sifting (sifting)
      When using dual simplex, whether to enable sifting, which can speed up
      the solve when there are many more variables than constraints:

      -1 - Automatic choice (default)
      0  - No
      1  - Yes.

lp:siftpasses (siftpasses)
      Determines how quickly we allow to grow the worker problems during the
      sifting algorithm; default 4.

lp:siftpresolveops (siftpresolveops)
      Presolve operations for solving the subproblems during sifting:

      -1  - use the "presolveops" setting specified for the original problem
      >=0 - use the value (see "presolveops" for its semantic)

lp:siftswitch (siftswitch)
      Determines which algorithm to use for solving the subproblems during
      sifting:

      -1 - dual simplex
      0  - barrier
      >0 - use the barrier algorithm while the number of dual infeasibilities
           is larger than this value, otherwise use dual simplex

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

mip:branchchoice (branchchoice)
      Control the choice of branching when solving a MIP problem:

      0 - explore branch with min.estimate first(default)
      1 - explore branch with max.estimate first
      2 - if an incumbent solution exists, first explore the branch satisfied
          by the incumbent; otherwise use choice 0 (min.est.first).
      3 - (default) explore the first branch that moves the branching
          variable away from its value at the root node; if the branching
          entity is not a simple variable, assume branchchoice=0.

mip:branchdisj (branchdisj)
      Whether to branch on general split disjunctions while solving MIPs:

      -1 - automatic choice (default)
      0  - disabled
      1  - cautious strategy : create branches only for general integers with
           a wide range
      2  - moderate strategy
      3  - aggressive strategy : create disjunctive branches for both
           binaryand integer variables

mip:branchstructural (branchstructural, branchstruct)
      Whether to search for special structure during branch and bound:

      -1 - Automatic choice (default)
      0  - No
      1  - Yes.

mip:breadthfirst (breadthfirst)
      Number of MIP nodes included in best-first search before switching to
      local-first search; default=11.

mip:components (mipcomponents)
      Determines whether disconnected components in a MIP should

      be solved as separate MIPs:

      -1 - Automatic choice (default)
      0  - No
      1  - Yes.

mip:concurrentnodes (mipconcurrentnodes)
      Node limit to choose the winning solve when concurrent

      solves are enabled:

      -1    - automatic (default)
      n > 0 - number of nodes to complete

mip:concurrentsolves (mipconcurrentsolves)
      Select the number of concurrent solves to start for a MIP:

      -1    - enabled, the number of concurrent solves depends on mipthreads
      0     - disabled (default)
      1     - disabled (default)
      n > 1 - number of concurrent solves = n

mip:deterministic (deterministic)
      Whether a MIP search should be deterministic:

mip:dualreductions (mipdualreductions)
      Kinds of dual reductions allowed during branch and bound:

      0 - none
      1 - all (default)
      2 - restrict dual reductions to continuous variables

      If poolnbest > 1 is specified, specifying mipdualreductions = 2 might be
      prudent.

mip:feasibilityjump (feasibilityjump)
      Decides whether to run the Feasibility Jump heuristic at the top node
      during branch-and-bound:

      0 - No
      1 - Yes (default)

mip:feasibilitypump (feasibilitypump)
      Decides whether to run the Feasibility Pump heuristic at the top node
      during branch-and-bound:

      -1 - automatic (default)
      0  - turned off
      1  - always run
      2  - run if other heuristics have failed to find an integer solution

mip:gap (mipgap)
      Max. relative MIP optimality gap (default 1e-4).

mip:gapabs (mipgapabs)
      Max. absolute MIP optimality gap (default 0).

mip:heurbeforelp (heurbeforelp)
      Whether primal heuristics should be run before the initial LP relaxation
      has been solved:

      -1 - Automatic choice (default)
      0  - No
      1  - Yes.

mip:heurdiverandomize (hdive_rand, heurdiverandomize)
      The level of randomization to apply in the diving heuristic; values
      range from 0.0=none to 1.0=full.

mip:heurdivesoftrounding (hdive_rounding, heurdivesoftrounding)
      Whether to use soft rounding in the MIP diving heuristic (to push
      variables to their bounds via the objective rather than fixing them):

      -1 - automatic (default)
      0  - do not use soft rounding
      1  - cautious use
      2  - aggressing use

mip:heurdivespeedup (hdive_speed, heurdivespeedup)
      Controls tradeoff between speed and solution quality in the diving
      heuristic:
      .. value-table:

mip:heurdivestrategy (hdive_strategy, heurdivestrategy)
      Chooses the strategy for the diving heuristic:

      -1   - automatic selection (default)
      0    - disable heuristics
      1-18 - available pre-set strategies for rounding infeasible global
             entities

mip:heuremphasis (heuremphasis)
      Chooses the strategy for the diving heuristic:

      -1 - default strategy (default)
      0  - disable heuristics
      1  - focus on reducing the gap early
      2  - extremely aggressive heuristics

mip:heurforcespecialobj (heurforcespecobj, heurforcespecialobj)
      Whether to use special objective heuristics on large problems and even
      if an incumbant exists:

      0 - No (default)
      1 - Yes.

mip:heurfreq (heurfreq)
      During branch and bound, heuristics are applied at nodes whose depth
      from the root is zero modulo "heurfreq"; default -1 (automatic).

mip:heursearcheffort (heursearcheffort)
      Adjusts the overall level of the local search heuristics; default 1.0
      (normal level).

mip:heursearchfreq (heurfreq, heursearchfreq)
      Specifies how often the local search heuristic should be run in the
      tree:

      -1  - automatic (default)
      0   - disabled in the tree
      n>0 - number of nodes between each run

mip:heursearchrootcutfreq (heurrootcutfreq, heursearchrootcutfreq)
      How often to run the local search heuristic while cutting at the root
      node:

      -1  - automatic (default)
      0   - disabled during cutting
      n>0 - number cutting rounds between each run

mip:heursearchrootselect (heursearchrootselect)
      A bit vector control for selecting which local search heuristics to
      apply on the root node of a global solve; default 117:

      1  - local search with a large neighborhood. Potentially slow but is
           good for finding solutions that differs significantly from the
           incumbent
      2  - local search with a small neighborhood centered around a node LP
           solution
      4  - local search with a small neighborhood centered around an integer
           solution. This heuristic will often provide smaller, incremental
           improvements to an incumbent solution
      8  - local search with a neighborhood set up through the combination of
           multiple integer solutions.
      32 - local search without an objective function
      64 - local search with an auxiliary objective function

mip:heursearchtreeselect (heursearchtreeselect)
      A bit vector control for selecting which local search heuristics to
      apply during the tree search of a global solve, default 17:

      1  - local search with a large neighborhood. Potentially slow but is
           good for finding solutions that differs significantly from the
           incumbent
      2  - local search with a small neighborhood centered around a node LP
           solution
      4  - local search with a small neighborhood centered around an integer
           solution. This heuristic will often provide smaller, incremental
           improvements to an incumbent solution
      8  - local search with a neighborhood set up through the combination of
           multiple integer solutions.
      32 - local search without an objective function
      64 - local search with an auxiliary objective function

mip:heurthreads (heurtreads)
      Number of threads to dedicate to running heuristics on the root node:

mip:historycosts (historycosts)
      How to update the pseudo cost for a global entity when a strong branch
      or a regular branch is applied:

mip:intfeastol (intfeastol)
      Feasibility tolerance for integer variables (default 5e-06).

mip:kappafreq (mipkappafreq)
      During branch-and-bound, how often to compute basis condition numbers:

      0     - never (default)
      1     - every node
      n > 1 - once per node at level n of the branch-and-bound tree

      When mipkappafreq > 0, a final summary shows the number of sampled nodes
      that are:

      "stable": kappa < 10^7

      "suspicious": 10^7 <= kappa < 10^10

      "unstable": 10^10 <= kappa < 10^13

      "ill-posed": 10^13 <= kappa.
      A "Kappa attention level" between 0 and 1 is also reported. Condition
      numbers use the Frobenius norms of the basis and its inverse.

mip:localchoice (localchoice)
      when to backtrack between two child nodes during a "dive":

      1 - never backtrack from the first child unless it is dropped (i.e., is
          infeasible or cut off) (default)
      2 - always solve both child nodes before deciding which child to
          continue with
      3 - automatically determined

mip:log (miplog)
      Frequency of printing MIP iteration log; default = -100.Values n < 0
      display detailed outputs every -n iterations.

mip:maxlocalbacktrack (maxlocalbacktrack, maxlocalbt)
      Max height above current node to look for a local backtrack candidate
      node; default=-1(automatic)

mip:maxtasks (maxmiptasks)
      Maximum tasks to run in parallel during a MIP solve; default = -1 (use
      mip:threads).For mip:maxtasks > 0, branch-and-bound nodes are solved in
      a deterministic way, but the barrier algorithm (if used) may cause a
      nondeterministic MIP solve unless bar:threads = 1.

mip:miprefineiterlimit (miprefiterlim, miprefineiterlimit)
      Max. simplex iterations per reoptimization in MIP refiner when refineops
      is 2 or 3; default -1 (automatic).

mip:nodeprobingeffort (nodeprobingeffort)
      Multiplier on the default amount of work node probing should do. Setting
      the control to zero disables node probing.

mip:nodeselection (nodeselection)
      Determines which nodes will be considered for solution once the current
      node has been solved:

      1 - local first: choose between descendant and sibling nodes if
          available; choose from all outstanding nodes otherwise
      2 - best first: choose from all outstanding nodes
      3 - local depth first: choose between descendant and sibling nodes if
          available; choose from the deepest nodes otherwise
      4 - best first, then local first: best first is used for the first
          BREADTHFIRST nodes, after which local first is used
      5 - pure depth first: choose from the deepest outstanding nodes

mip:presolve (mippresolve)
      Type of integer processing to be performed. If set to 0, no processing
      will be performed (default automatic):

      1   - reduced-cost fixing at each node
      2   - primal reductions will be performed at each node
      8   - allow changing continuous-variable bounds
      16  - allow dual reductions
      32  - allow global tightening of the problem
      64  - use objective function
      128 - allow restarting
      256 - allow use of symmetry

mip:pseudocost (pseudocost)
      Default pseudo-cost assumed for forcing an integer variable

      to an integer value; default = 0.01

mip:qcrootalg (qcrootalg)
      when using miqcpalg = 1 to solve a mixed - integer problem that has
      quadratic constraints or second - order cone constraints, the algorithm
      for solving the root node:

      -1 - automatic (default)
      0  - use barrier
      1  - use dual simplex on outer approximation

mip:rampup (miprampup)
      Whether to limit the number of parallel tasks

      during the ramp-up phase of the parallel MIP algorithm:

      -1 - automatic choice (default)
      0  - no: use as many tasks as possible
      1  - yes, until finished with initial dives

mip:relaxtreememorylimit (relaxtreemem, relaxtreememorylimit)
      Fraction of memory limit by which to relax "treememlimit" when too much
      structural data appears; default 0.1. Set to 0 to never relax the memory
      limit in this way.

mip:restart (miprestart)
      Control strategy for in-tree restarts:

      -1 - automatic choice (default)
      0  - disable in-tree restarts
      1  - normal aggressiveness
      2  - higher aggressiveness

mip:restartfactor (miprestartfactor)
      Fine tune initial conditions to trigger an in-tree restart; values > 1
      increase the aggressiveness, < 1 decrease it (default 1.0)

mip:restartgapthreshold (miprestartgapthreshold)
      Initial gap threshold to delay in-tree restart; the restart is delayed
      if the relative gap is below the threshold (default 0.02)

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

mip:sbbest (sbbest)
      Number of infeasible global entities to initialize pseudo costs for on
      each node:

      -1    - automatic (default)
      0     - disable strong branching
      n > 1 - perform strong branching on up to n entities at each node

mip:sbeffort (sbeffort)
      Adjusts the overall amount of effort when using strong branching to
      select an infeasible global entity to branch on; default = 1.

mip:sbestimate (sbestimate)
      How to compute pseudo costs from the local node when selecting an
      infeasible entity to branch on:

      -1  - automatic (default)
      1-6 - different variants of local pseudo costs.

mip:sbiterlimit (sbiterlimit)
      Number of dual iterations to perform the strong branching; 0=none,
      default = -1 (automatic choice)

mip:sbselect (sbselect)
      size of candidate list for strong branching:

      -2    - automatic - low effort (default)
      -1    - automatic - high effort
      n > 0 - include max(n, sbbest) candidates

mip:symmetry (symmetry)
      Amount of effort to detect symmetry in MIP problems:

      0 - no simmetry detection
      1 - conservative effort
      2 - intensive effort

mip:symselect (symselect)
      Adjusts the overall amount of effort for symmetry detection:

      0 - search the whole matrix (otherwise the 0, 1 and -1 coefficients
          only)
      1 - search all entities(otherwise binaries only)

mip:threads (mipthreads)
      Determines the number of threads implemented to run the parallel MIP
      code; default -1: alg:threads will determine the number of threads.

mip:toltarget (miptoltarget)
      Value of miptol used for refining equalities on MIP problems when
      refineops is 2 or 3; default = 0.

mip:varselection (varselection)
      How to score the integer variables at a MIP node, for branching on a
      variable with minimum score:

      - 1 - automatic choice(default)
      1   - minimum of the 'up' and 'down' pseudo - costs
      2   - 'up' pseudo - cost + 'down' pseudo - cost
      3   - maximum of the 'up' and 'down' pseudo - costs plus twice their
            minimum
      4   - maximum of the 'up' and 'down' pseudo - costs
      5   - the 'down' pseudo - cost
      6   - the 'up' pseudo - cost
      7   - weighted combination of the 'up' and 'down' pseudo costs
      8   - product of 'up' and 'down' pseudo costs

obj:multi (multiobj)
      0*/1: Whether to use multi-objective optimization. If set to 1
      multi-objective optimization is performed using lexicographic method
      with the first objective treated as the most important, then the second
      objective and so on.

obj:no (objno)
      Objective to optimize:

      0 - None
      1 - First (default, if available)
      2 - Second (if available), etc.

pre:basisred (prebasisred)
      Determines if a lattice basis reduction algorithm should be attempted as
      part of presolve:

      -1 - Automatic choice (default)
      0  - No
      1  - Yes.

pre:bndredcone (prebndredcone)
      Determines if second order cone constraints should be used for inferring
      bound reductions on variables when solving a MIP:

      -1 - Automatic choice (default)
      0  - No
      1  - Yes.

pre:bndredquad (prebndredquad)
      Determines if convex quadratic contraints should be used for inferring
      bound reductions on variables when solving a MIP

pre:cliquestrategy (precliquestrategy)
      Determines how much effort to spend on clique covers in presolve;
      default=-1.

pre:coefelim (precoefelim)
      Specifies whether the optimizer should attempt to recombine constraints:

      0 - disabled
      1 - remove as many coefficients as possible
      2 - cautious eliminations

pre:components (precomponents)
      Determines whether small independent components should be detected and
      solved as individual subproblems during root node processing:

      -1 - Automatic choice (default)
      0  - No
      1  - Yes.

pre:componentseffort (precomponentseffort)
      adjusts the overall effort for the independent component presolver;
      default = 1.0.

pre:configuration (preconfiguration)
      Whether to reformulate binary rows with very few coefficients:

      0 - No
      1 - Yes (default)

pre:convertseparable (preconvertseparable)
      Reformulate problem with non-diagonal quadratic objective and/or
      constraints as diagonal quadratic or second-order conic constraints:

      -1 - automatic (default)
      0  - disable
      1  - enable reformulation to diagonal quadratic constraints.
      2  - 1, plus reduction to second-order cones
      3  - 2, plus the objective function is converted to a constraint and
           treated as a quadratic constraint

pre:domcol (predomcol)
      Whether presolve should remove variables when solving MIP problems:

      -1 - automatic (default)
      0  - disable
      1  - cautious
      2  - aggressive: all candidate will be checked

pre:domrow (predomrow)
      Whether presolve should remove constraints when solving MIP problems:

      -1 - automatic choice (default)
      0  - disabled
      1  - cautious
      2  - medium
      3  - aggressive

pre:duprow (preduprow)
      How presolve should deal with duplicate rows in MIP problems:

      -1 - automatic (default)
      0  - disable
      1  - eliminate only rows that are identical in all variables
      2  - 1 plus eliminate duplicate rows with simple penalty variable
           expressions
      3  - 2 plus eliminate duplicate rows with more complex penalty variable
           expressions

pre:elimfillin (elimfillin)
      Maximum fillins allowed for a presolve elimination; default = 10

pre:elimquad (preelimquad)
      Allows for elimination of quadratic variables via doubleton rows:

      -1 - Automatic choice (default)
      0  - No
      1  - Yes.

pre:elimtol (elimtol)
      The Markowitz tolerance for the elimination phase of the presolve;
      default=0.001

pre:folding (prefolding)
      Determines if a folding procedure should be used to aggregate continuous
      columns in an equitable partition:

      -1 - Automatic choice (default)
      0  - No
      1  - Yes.

pre:genconsdualreductions (genconsdualreductions)
      Whether dual reductions should be applied to reduce the number of
      columns and rows added when transforming general constraints to MIP
      structs:

      0 - No
      1 - Yes (default)

pre:implications (preimplications)
      Determines whether to use implication structures to remove redundant
      rows:

      -1 - Automatic choice (default)
      0  - No
      1  - Yes.

pre:indlinbigm (indprelinbigm)
      Largest "big M" value to use in converting indicator constraints to
      regular constraints during XPRESS presolve; default = 100.0

pre:lindep (prelindep)
      Determines whether to check for and remove linearly dependent equality
      constraints when presolving a problem:

      -1 - Automatic choice (default)
      0  - No
      1  - Yes.

pre:maxgrow (presolvemaxgrow)
      Limit on how much the number of non-zero coefficients is allowed to grow
      during presolve, specified as a ratio of the number of non-zero
      coefficients in the original problem; default=0.1

pre:maximpliedbound (maximpliedbound)
      When preprocessing MIP problems, only use computed bounds at most
      maximpliedbound (default 1e8) in absolute value

pre:maxscalefactor (maxscalefactor)
      Maximum log2 factor that can be applied during scaling, must be >=0 and
      <=64; default=64.

pre:objcutdetect (preobjcutdetect)
      MIP: Determines whether to check for constraints that are parallel or
      near parallel to a linear objective function, and which can safely be
      removed:

      0 - No
      1 - Yes (default)

pre:objscalefactor (objscalefactor)
      Power of 2 (default 0) by which the objective is scaled. Nonzero
      objscalfactor values override automatic global objective scaling

pre:ops (presolveops)
      Reductions to use in XPRESS's presolve, sum of:

      1 = 2^0          - Remove singleton columns
      2 = 2^1          - Remove singleton constraints (rows)
      4 = 2^2          - Forcing row removal
      8 = 2^3          - Dual reductions
      16 = 2^4         - Redundant row removal
      32 = 2^5         - Duplicate column removal
      64 = 2^6         - Duplicate row removal
      128 = 2^7        - Strong dual reductions
      256 = 2^8        - Variable eliminations
      512 = 2^9        - No IP reductions
      1024 = 2^10      - No semi-continuous variable detection
      2048 = 2^11      - No advanced IP reductions
      4096 = 2^12      - No eliminations on integers
      16384 = 2^14     - Linearly dependant row removal
      32768 = 2^15     - No integer variable and SOS detection
      536870912 = 2^29 - No dual reduction on globals

      (default 511 = bits 0-8 set)

pre:passes (presolvepasses)
      Number of reduction rounds to be performed in presolve; default=1.

pre:permute (prepermute)
      Bit vector: specifies whether to randomly permute rows, columns and
      global information when starting the presolve (default 0):

      1 - permute rows
      2 - permute columns
      4 - permute global information (for MIP)

pre:permuteseed (prepermuteseed)
      Sets the seed for the pseudo-random number generator for permuting;
      default=0

pre:probing (preprobing)
      Amount of probing to perform on binary variables during presolve. This
      is done by fixing a binary to each of its values in turn and analyzing
      the implications:

      -1 - automatic choice (default)
      0  - disabled
      1  - cautious
      2  - medium
      3  - aggressive

pre:protectdual (preprotectdual)
      Specifies whether the presolver should protect a given dual solution by
      maintaining the same level of dual feasibility:
      .. value-table:

pre:pwldualreductions (pwldualreductions)
      Whether dual reductions should be applied to reduce the number of
      columns, rows and SOS-constraints added when transforming piecewise
      linear objectives and constraints to MIP structs:

      0 - No
      1 - Yes (default)

pre:pwlnonconvextransformation (pwlnonconvextransformation)
      Reformulation method for piecewise linear constraints at the beginning
      of the search:

      -1 - automatic (default)
      0  - use a formulation based on SOS2-constraints
      1  - use a formulation based on binary variables

pre:rootpresolve (rootpresolve)
      Whether to presolve after root cutting and heuristics:

      -1 - Automatic choice (default)
      0  - No
      1  - Yes.

pre:scaling (scaling)
      Bit vector determining how to scale the constraint matrix before
      optimizing:

      1     - row scaling
      2     - column scaling
      4     - row scaling again
      8     - maximum
      16    - Curtis-Red
      32    - 0->geometric mean, 1->maximum element
      64    - no special handling for BigM rows
      128   - scale objective function for the simplex method
      256   - exclude the quadratic part of constraints when calculating
              scaling factors
      512   - scale before presolve
      1024  - do not scale constraints up
      2048  - do not scale variables down
      4096  - do not apply automatic global objective scaling
      8192  - RHS scaling
      16384 - disable aggressive quadratic scaling
      32768 - explicit linear slack scaling

pre:solve (presolve)
      Whether to use Xpress' presolve:

      0 - No
      1 - Yes, removing redundant bounds (default)
      2 - Yes, retaining redundant bounds

pre:sosreftol (sosreftol)
      Minimum relative gap between the ordering values of elements in a
      special ordered set; default=1e-6.

pre:trace (trace)
      Display the infeasibility diagnosis during presolve:

      0 - No (default)
      1 - Yes.

qp:eigenvaluetol (eigenvaluetol)
      Regard the matrix in a quadratic form as indefinite if its smallest
      eigvenalue is < -eigevnaltol; default = 1e-6

qp:miqcpalg (miqcpalg)
      Which algorithm is to be used to solve mixed integer quadratic
      constrained and mixed integer second order cone problems:

      -1 - automatic (default)
      0  - barrier
      1  - outer approximations

qp:nonconvex (nonconvex)
      Determines if the convexity of the problem is checked before
      optimization:

      0 - No
      1 - Yes (default)

qp:repairindefiniteq (repairindefq, repairindefiniteq)
      whether to repair indefinite quadratic forms:

      0 - yes
      1 - no (default)

qp:simplexops (qsimplexops)
      Bit vector, controls the behavior of the quadratic simplex solvers:

      1   - traditional primal first phase (default)
      2   - force Big M primal first phase
      4   - force traditional dual first phase
      8   - force BigM dual first phase
      16  - always use artificial bounds in dual
      32  - use original problem basis only when warmstarting the KKT
      64  - skip the primal bound flips for ranged primals (might cause more
            trouble than good if the bounds are very large)
      128 - also do the single pivot crash
      256 - do not apply aggressive perturbation in dual

qp:unshift (quadunshift, quadraticunshift)
      whether quadratic simplex should do an extra purification after finding
      a solution:

      -1 - Automatic choice (default)
      0  - No
      1  - Yes.

sol:count (countsolutions)
      0*/1: Whether to count the number of solutions and return it in the
      ".nsol" problem suffix.

sol:pooldualred (pooldualred)
      Whether to suppress removal of dominated solutions(via "dual
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

sol:poolmiptol (poolmiptol)
      Error (nonintegrality) allowed in discrete variables in the solution
      pool (default 5e-6)

sol:poolnbest (poolnbest, poollimit)
      Whether the solution pool (see poolstub) should contain inferior
      solutions. When poolnbest = n > 1, the solution pool is allowed to keep
      the n best solutions.

sol:stub (ams_stub, solstub, solutionstub)
      Stub for solution files. If "solutionstub" is specified, found solutions
      are written to files ("solutionstub & '1' & '.sol'") ... ("solutionstub
      & Current.nsol & '.sol'"), where "Current.nsol" holds the number of
      returned solutions. That is, file names are obtained by appending 1, 2,
      ... "Current.nsol" to "solutionstub".

tech:cputime (cputime)
      How time should be measured when timings are reported in the log and
      when checking against time limits :

      -1 - disable the timer
      0  - use elapsed time (default)
      1  - use process time

tech:debug (debug)
      0*/1: whether to assist testing & debugging, e.g., by outputting
      auxiliary information.

tech:exportfile (writeprob, writemodel)
      Specifies the name of a file where to export the model before solving
      it. This file name can have extension ".lp()", ".mps", etc. Default = ""
      (don't export the model).

tech:globalfileloginterval (globalfileloginterval)
      Seconds between additions to the logfile about, additions to the "global
      file", a temporary file written during a global search. Default = 60.

tech:globalfilemax (globalfilemax)
      Maximum megabytes for temporary files storing the global search tree: a
      new file is started if globalfilemax megabytes would be exceeded.

tech:justexportfile (justwriteprob, justwritemodel)
      Specifies the name of a file where to export the model, do not solve
      it.This file name can have extension ".lp()", ".mps", etc. Default = ""
      (don't export the model).

tech:optionfile (optionfile, option:file)
      Name of solver option file. (surrounded by 'single' or "double" quotes
      if the name contains blanks). Lines that start with # are ignored.
      Otherwise, each nonempty line should contain "name=value".

tech:outlev (outlev)
      Whether to write xpress log lines (chatter) to stdout and to file:

      0 - none
      1 - all
      2 - information
      3 - warnings & errors only (default)
      4 - errors
      5 - none

tech:sleeponthreadwait (sleeponthreadwait)
      Whether threads should sleep while awaiting work:

      -1 - automatically determined
      0  - no (busy-wait)
      >0 - yes (sleep, might add overhead)

tech:threads (threads)
      The default number of threads used during optimization.;default - 1 ==>
      automatic choice.

tech:timing (timing)
      0*/1: Whether to display timings for the run.

tech:tunebase (tunerdir, tunebase)
      Base name for results of running XPRESS's search for best parameter
      settings. The search is run only when tunebase is specified. This
      control only defines the root path for the tuner output. For each
      problem, the tuner result will be output to a subfolder underneath this
      path. For example, by default, the tuner result for a problem called
      prob will be located at tuneroutput/prob/

tech:tunename (tunesessionname)
      Set problem name within the tuner "tunebase" is specified.

tech:tuneoutput (tuneroutput, tuneoutput)
      Output tuner results and logs to the file system when "tunebase" is
      specified:

      0 - No
      1 - Yes (default)

tech:tunerhistory (tunerhistory)
      Reuse and append to previous tuner results of the same problem:

      0 - Discard any previous result
      1 - Append new results but do not reuse them
      2 - Reuse and append new results

tech:tunermethod (tunermethod)
      Method for tuning when "tunebase" is specified:

      - 1 - automatic choice(default)
      0   - default LP tuner
      1   - default MIP tuner
      2   - more elaborate MIP tuner
      3   - root - focused MIP tuner
      4   - tree - focused MIP tuner
      5   - simple MIP tuner
      6   - default SLP tuner
      7   - default MISLP tuner
      8   - MIP tuner using primal heuristics

tech:tunertarget (tunertarget)
      What to measure to compare two problem solutions when running the XPRESS
      tuner:

      - 1 - automatic choice(default)
      0   - solution time, then integrality gap
      1   - solution time, then best bound
      2   - solution time, then best integer solution
      3   - the "primal dual integral", whatever that is
      4   - just solution time (default for LPs)
      5   - just objective value
      6   - validation number (probably not relevant)
      7   - gap only
      8   - best bound only
      9   - best integer solution only
      10  - best primal integral - only for individual instances

tech:tunerthreads (tunerthreads)
      Number of tuner threads to run in parallel; default=-1 (automatic)

tech:tunerverbose (tunerverbose)
      whether the tuner should prints detailed information for each run:

      0 - No
      1 - Yes (default)

tech:tunetimelim (tunermaxtime, tunetimelim, lim:tunetime)
      Time limit (in seconds) on tuning when "tunebase" is specified; default
      0 (no time limit).

tech:version (version)
      Single-word phrase: report version details before solving the problem.

tech:wantsol (wantsol)
      In a stand-alone invocation (no "-AMPL" on the command line), what
      solution information to write. Sum of

      1 - Write ".sol" file
      2 - Primal variables to stdout
      4 - Dual variables to stdout
      8 - Suppress solution message.

tech:writegraph (writegraph, exportgraph)
      File to export conversion graph. Format: JSON Lines.

```

