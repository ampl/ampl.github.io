
# XPRESSASL Options

```ampl
ampl: option solver xpressasl; # change the solver
ampl: option xpressasl_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

Solver options obtained with `$ xpressasl -=`.

```
advance            whether to use an initial basis, if available:
                        0 = no, overriding mipstartstatus;
                        1 = yes (default), subject to mipstartstatus.
                   In an AMPL session, "option send_statuses 0;" is preferable
                   to "option xpress_options '... advance=0 ...';".

algaftercrossover  algorithm for final cleanup after running the barrier
                   algorithm:
                        1 = automatic choice (default)
                        2 = dual simplex
                        3 = primal simplex
                        4 = concurrent

algafternetwork    algorithm for final cleanup after the network simplex
                   algorithm:
                        1 = automatic choice (default)
                        2 = dual simplex
                        3 = primal simplex

archconsistent     whether to force the same execution path to be
                   independent of the platform architecture:
                        0 = no (default)
                        1 = yes

autocutting        whether to automatically decide if to generate cutting
                   planes at local nodes (overriden by cutfreq):
                        -1 = automatic (default)
                         0 = disabled
                         1 = enabled

autoperturb        whether to introduce perturbations when the simplex method
                   encounters too many degenerate pivots:
                        1 = yes (default); 0 = no

autoscaling        whether the Optimizer should automatically select between
                   different scaling algorithms:
                       -1 = automatic (default)
                        0 = disabled
                        1 = cautious strategy.  Non-standard scaling will only
                            be selected if it appears to be clearly superior
                        2 = moderate strategy
                        3 = aggressive strategy.  Standard scaling will only be
                            selected if it appears to be clearly superior

backtrack          choice of next node when solving MIP problems:
                        -1 = automatic choice (default)
                         1 = withdrawn; formerly choice 2 until a feasible
                                integer solution has been found, then
                                Forrest-Hirst-Tomlin choice
                         2 = node with best estimated solution
                         3 = node with best bound on the solution (default)
                         4 = deepest node (depth-first search)
                         5 = highest node (breadth-first search)
                         6 = earliest-created node
                         7 = most recently created node
                         8 = random choice
                         9 = node with fewest LP relaxation infeasibilities
                        10 = combination of 2 and 9
                        11 = combination of 2 and 4

backtracktie       how to break ties for the next MIP node:  same choices as
                   for "backtrack"

baralg             which barrier algorithm to use with "barrier":
                        -1 = automatic choice (default with just "barrier")
                         1 = infeasible-start barrier algorithm
                         2 = homogeneous self-dual barrier algorithm
                         3 = start with 2 and maybe switch to 1 while solving

barcores           if positive, number of CPU cores to assume present when
                   using the barrier algorithm.  Default = -1, which means
                   automatic choice.

barcrash           choice of crash procedure for crossover:
                        0 = no crash
                        1-6 = available strategies (default 4):
                        1 = most conservative, 6 = most aggressive

bardualstop        barrier method convergence tolerance on
                   dual infeasibilities; default = 0 (automatic choice)

bargapstop         barrier method convergence tolerance on the relative
                   duality gap; default = 0

bargaptarget       barrier algorithm target tolerance for the relative duality
                   gap.  If not satisfied and no further progress is possible
                   but barstopgap is satisfied, then the current solution is
                   considered optimal.

barindeflimit      maximum indefinite factorizations to allow in the barrier
                   algorithm for solving a QP: stop when the limit is hit;
                   default = 15

bariterlimit       maximum number of Newton Barrier iterations; default = 500

barkernel          how the barrier algorithm weights centrality:
                        >= +1.0 ==> more emphasis on centrality
                        <= -1.0 ==> each iteration, adaptively select a value
                                from [+1, -barkernel].
                   Default = 1.

barobjperturb      defines how the barrier perturbs the objective (default
                   1e-6); values >0 let the optimizer decide if to perturb the
                   objective, values <0 force the perturbation:
                        n > 0 = automatic decison, scale n
                            0 = turn off perturbation
                        n < 0 = force perturbation by abs(n)

barobjscale        how the barrier algorithm scales the objective:
                         -1 = automatic chocie (default)
                          0 = scale by the geometric mean of the objective
                              coefficients
                        > 0 = scale so the argest objective coefficient in
                              absolute value is <= barobjscale.
                   When the objective is quadratic, the quadratic diagonal
                   is used in determining the scale.

barorder           Cholesky factorization pivot order for barrier algorithm:
                        0 = automatic choice (default)
                        1 = minimum degree
                        2 = minimum local fill
                        3 = nested dissection

barorderthreads    number of threads to use when choosing a pivot order for
                   Cholesky factorization; default 0 ==> automatic choice.

baroutput          amount of output for the barrier method:
                        0 = no output
                        1 = each iteration (default)

barpresolve        level of barrier-specific presolve effort:
                        0 = use standard presolve (default)
                        1 = use more effort
                        2 = do full matrix eliminations for size reduction

barprimalstop      barrier method convergence tolerance on
                   primal infeasibilities; default = 0 (automatic choice)

barrefiter         maximum number of refinement iterations, helpful when the
                   the solution is near to the optimum using barrier or crossover:
                            0 = default
                        n > 0 = perform n refinement iterations

barreg             regularization to use with "barrier":
                        -1 = automatic choice (default with just "barrier")
                        Values >= 0 are the sum of:
                        1 = use "standard" regularization
                        2 = use "reduced" regularization: less perturbation
                                than "standard" regularization
                        4 = keep dependent rows in the KKT system
                        8 = keep degenerate rows in the KKT system

barrier            [no assignment] use the Newton Barrier algorithm

barstart           choice of starting point for barrier method:
                        -1 = use incoming solution for warm start
                         0 = automatic choice (default)
                         1 = heuristics based on magnitudes of matrix entries
                         2 = use pseudoinverse of constraint matrix
                         3 = unit starting point for homogeneous self-dual
                            barrier algorithm.

barstepstop        barrier method convergence tolerance: stop when
                   step size <= barstepstop; default = 1e-10

barthreads         number of threads used in the Newton Barrier algorithm;
                   default = -1 (determined by "threads")

basisin            load initial basis from specified file

basisout           save final basis to specified file

bestbound          [no assignment] return suffix .bestbound for the best known
                   bound on the objective value.  The suffix is on the problem
                   and objective and is +Infinity for minimization problems and
                   -Infinity for maximization problems if there are no integer
                   variables or if an integer feasible solution has not yet
                   been found.

bigm               infeasibility penalty; default = 1024

bigmmethod         0 = phase I/II, 1 = BigM method (default)

branchchoice       whether to explore branch with min. or max. estimate first:
                        0 = explore branch with min. estimate first (default)
                        1 = explore branch with max. estimate first
                        2 = if an incumbent solution exists, first explore
                                the branch satisfied by the incumbent;
                                otherwise use choice 0 (min. est. first)
                        3 (default) = explore the first branch that moves the
                                branching variable away from its value at the
                                root node; if the branching entity is not a
                                simple variable, assume branchchoice=0

branchdisj         whether to branch on general split disjunctions while
                   solving MIPs:
                        -1 = automatic choice (default)
                         0 = disabled
                         1 = cautious strategy: create branches only for
                                general integers with a wide range
                         2 = moderate strategy
                         3 = aggressive strategy:  create disjunctive branches
                                for both binary and integer variables

branchstruct       whether to search for special structure during branch and
                   bound:
                        -1 = automatic choice (default)
                         0 = no
                         1 = yes

breadthfirst       number of MIP nodes included in best-first search
                   (default 11) before switching to local-first search

cachesize          cache size in Kbytes -- relevant to Newton Barrier:
                        -1 = determined automatically
                   default = system-dependent (-1 for Intel)

choleskyalg        type of Cholesky factorization used for barrier: sum of
                          1 ==> manual matrix blocking
                          2 ==> single pass with manual blocking
                          4 ==> nonseparable QP relaxation
                          8 ==> manual corrector weight (honor "16" bit)
                         16 ==> manual corrector weight "on"
                         32 ==> manual refinement
                         64 ==> use preconditioned conjugate gradients
                        128 ==> refine with QMR (quasi-minimal residual)
                        default = -1 (automatic choice)

choleskytol        zero tolerance for Cholesky pivots in the
                   Newton Barrier algorithm; default = 1e-15

clamping           control adjustements of the returned solution values
                    such that they are always within bounds:
                        -1 ==> determined automatically
                         0 ==> adjust primal solution to be within
                               primal bounds (default)
                         1 ==> adjust primal slack values to be within
                               primal bounds
                         2 ==> adjust dual solution to be within dual
                               bounds
                         3 ==> adjust reduced costs to be within dual
                               bounds

concurrentthreads  synonym for lpthreads

conedecomp         whether to decompose regular and rotated cone constraints
                   having more than two elements and to use the result in an
                   outer approximation:
                        -1 = automatic choice (default)
                         0 = no
                         1 = yes, unless the cone variable is fixed by XPRESS's
                                presolve
                         2 = yes, even if the cone variable is fixed
                         3 = yes, but only for outer approximations

convexitychk       whether to check convexity before solving:
                        0 = no
                        1 = yes (default)

corespercpu        number of cores to assume per cpu; default = -1 ==> number
                   detected; barrier cache = cachesize / corespercpu

covercuts          for MIPS, the number of rounds of lifted-cover inequalities
                   at the top node; default = -1 ==> automatic choice

cpuplatform        whether the Newton Barrier method should use AVX or SSE2
                   instructions on platforms that offer both:
                        -2 = highest supported [Generic, SSE2, AVX, or AVX2]
                        -1 = highest deterministic support (default; no AVX2)
                         0 = use generic code: neither AVX nor SSE2
                         1 = use SSE2
                         2 = use AVX
                         3 = use AVX2

cputime            which times to report when logfile is specified:
                        0 = elapsed time (default)
                        1 = CPU time
                        2 = process time
                   You may need to experiment to see how cputime=1 and
                   cputime=2 differ (if they do) on your system.

crash              type of simplex crash:
                        0 = none
                        1 = one-pass search for singletons
                        2 = multi-pass search for singletons (default)
                        3 = multi-pass search including slacks
                        4 = at most 10 passes, only considering slacks
                            at the end
                        n = (for n > 10) like 4, but at most n-10 passes

crossover          whether to find a simplex basis after the barrier alg.:
                        -1 = automatic choice (default)
                         0 = no crossover
                         1 = primal crossover first
                         2 = dual crossover first

crossoveritlim     limit on crossover iterations after the barrier
                   algorithm; default = 2147483645

crossoverops       bit vector affecting crossover after the barrier
                   algorithm:  sum of
                        1 = return the barrier solution (rather than the last
                            intermediate solution) when crossover stop early
                        2 = skip the second crossover stage
                        4 = skip pivots that are "less numerically reliable"
                        8 = do a slower but more numerically stable crossover

crossoverthreads   limit on threads used during crossover;
                   default not specified in the Release 8.2 documentation

crossovertol       tolerance (default 1e-6) for deciding whether to adjust the
                   relative pivot tolerance during crossover when a new basis
                   factorization is necessary.  Errors in the recalculated
                   basic solution above this tolerance cause the pivot
                   tolerance to be adjusted.

cutdepth           maximum MIP tree depth at which to generate cuts:
                        0  = no cuts
                        -1 = automatic choice (default)

cutfactor          limit on number of cuts and cut coefficients added
                   while solving MIPs:
                        -1 = automatic choice (default)
                         0 = do not add cuts
                         > 0 ==> multiple of number of original constraints

cutfreq            MIP cuts are only generated at tree depths that are integer
                   multiples of cutfreq; -1 = automatic choice (default)

cutselect          detailed control of cuts at MIP root node:  sum of
                            32 = clique cuts
                            64 = mixed-integer founding (MIR) cuts
                           128 = lifted cover cuts
                          2048 = flow path cuts
                          4096 = implication cuts
                          8192 = automatic lift-and-project strategy
                         16384 = disable cutting from cut rows
                         32768 = lifted GUB cover cuts
                         65536 = zero-half cuts
                        131072 = indicator-constraint cuts
                            -1 = all available cuts (default)

cutstrategy        how aggressively to generate MIP cuts; more ==> fewer nodes
                   but more time per node:
                        -1 = automatic choice (default)
                         0 = no cuts
                         1 = conservative strategy
                         2 = moderate strategy
                         3 = aggressive strategy

defaultalg         algorithm to use when none of "barrier", "dual", or "primal"
                   is specified:
                        1 = automatic choice (default)
                        2 = dual simplex
                        3 = primal simplex
                        4 = Newton Barrier

densecollimit      number of nonzeros above which a column is treated as dense
                   in the barrier algorithm's Cholesky factorization:
                        0 = automatic choice (default)

deterministic      whether a MIP search should be deterministic:
                        0 = no
                        1 = yes (default)
                        2 = yes, with opportunistic root LP solve

dual               [no assignment] use the dual simplex algorithm

dualgradient       dual simplex pricing strategy:
                        -1 = automatic choice
                         0 = Devex
                         1 = steepest edge

dualize            whether to convert the primal problem to its dual and solve
                   the converted problem:
                        -1 = automatic choice (default)
                         0 = no: solve primal problem
                         1 = yes: solve dual problem

dualizeops         when solving the dual problem after deriving it from the
                   primal, whether to use primal simplex if dual simplex was
                   specified and vice versa:
                        0 = no
                        1 = yes (default)

dualperturb        Factor by which to possibly perturb the problem in the
                   dual simplex algorithm.  If >= 0, overrides "perturb".
                   Default -1 ==> automatic choice; 0 ==> no perturbatation.

dualstrategy       how to remove infeasibilities when re-optimizing
                   with the dual algorithm during MIP solves:
                        0 = use primal algorithm
                        1 = use dual algorithm (default)

dualthreads        limit on number of threads used by parallel dual simplex,
                   overriding "threads"; default -1 ==> use "threads"

eigenvaltol        regard the matrix in a quadratic form as indefinite if its
                   smallest eigvenalue is < -eigevnaltol; default = 1e-6

elimfillin         maximum fillins allowed for a presolve elimination;
                   default = 10.

elimtol            Markowitz tolerance for the elimination phase of
                   XPRESS's presolve; default = 0.001

etatol             zero tolerance on eta elements; default varies with XPRESS
                   version; default = 1e-12 or 1e-13 with some versions.
                   Use etatol=? to see the current value.

feaspump           whether to run the Feasibility Pump heuristic at the top
                   node during branch-and-bound:  one of
                        0 = no (default)
                        1 = yes
                        2 = only if other heurstics found no integer solution

feastol            zero tolerance on RHS; default = 1e-6

feastol_perturb    how much a feasible primal basic solution is allowed to
                   be perturbed when performing basis changes.  The tolerance
                   specified by "feastol" is always considered as an upper
                   limit for the perturbations; default = 1.0E-06

feastol_target     feasibility tolerance on constraints for solution refiner
                   (see refineops):  if feastol_target > 0 is specified, it is
                   used instead of feastol

globalfilemax      maximum megabytes for temporary files storing the global
                   search tree:  a new file is started if globalfilemax
                   megabytes would be exceeded

globalloginterval  seconds between additions to the logfile about, additions
                   to the "global file", a temporary file written during a
                   global search.  Default = 60.

gomcuts            gomory cuts at root: -1 = automatic choice (default)

hdive_rand         value between 0 and 1 inclusive affecting randomization
                   in the diving heuristic:  0 (default) ==> none;
                        1 ==> full;
                        intermediate values ==> intermediate behavior

hdive_rounding     whether to use soft rounding in the MIP diving heuristic
                   (to push variables to their bounds via the objective rather
                   than fixing them):
                        -1 = automatic choice (default)
                         0 = no soft rounding
                         1 = cautious soft rounding
                         2 = aggressive soft rounding

hdive_speed        controls tradeoff between speed and solution quality
                   in the diving heuristic:  an integer between -2 and 3:
                        -2 = automatic bias toward quality
                        -1 = automatic bias toward speed (default)
                         0 = emphasize quality
                         4 = emphasize speed
                         1-3 = intermediate emphasis

hdive_strategy     strategy for diving heuristic:  integer between -1 and 10:
                        -1 = automatic choice (default)
                         0 = do not use the diving heursistic
                        1-10 = preset strategies for diving

heurdepth          deprecated:  no longer has any effect:
                   maximum depth of branch-and-bound tree search at which to
                   apply heuristics; 0 = no heuristics; default = -1

heureffort         factor affecting how much work local search heuristics
                   should expend.  Default = 1; higher values cause more
                   local searches over larger neighborhoods.

heuremphasis       epmphasis for the heuristic search for branch and
                   bound.  Setting it to 1 gets a gap quicker at the
                   expense of time to optimality:
                        -1 = default strategy
                         0 = disable heuristics
                         1 = focus on reducing the gap early
                         2 = extremely aggressive heuristics

heurforcespecobj   whether to use special objective heuristics on large
                   problems and even if an incumbant exists:
                        0 = no (default)
                        1 = yes.

heurfreq           during branch and bound, heuristics are applied at nodes
                   whose depth from the root is zero modulo heurfreq;
                   default = -1 (automatic choice)

heurmaxsol         deprecated:  no longer has any effect:
                   maximum number of heuristic solutions to find during branch-
                   and-bound tree search; default = -1 (automatic choice)

heurnodes          deprecated:  no longer has any effect:
                   maximum nodes at which to use heuristics during
                   branch-and-bound tree search; default = 1000

heurroot           bit vector controlling local search heuristics to apply at
                   the root node:  sum of
                          1 = large-neighborhood search: may be slow, but may
                                find solutions far from the incumbent
                          2 = small-neighborhood search about node LP solution
                          4 = small-neighborhood search about integer solutions
                          8 = local search near multiple integer solutions
                         16 = no effect
                         32 = local search without an objective; may only be
                                done when no feasible solution is available
                         64 = local search with an auxiliary objective; may
                                be done when no feasible solution is available
                   default = 117

heurrootcutfreq    how often to run the local search heuristic while
                   cutting at the root node:
                        -1 ==> automatic choice (default)
                         0 ==> never
                         n > 0 ==> do n cutting rounds between runs of the
                                local search heuristic

heursearch         how often the local search heurstic should be run during
                   branch-and-bound:
                        -1 = automatic choice (default)
                         0 = never
                         n > 0 ==> every n nodes

heurthreads        number of threads for the root node of
                   branch-and-bound:
                        -1 = determined from "threads" keyword
                         0 = no separate threads (default)
                         n > 0 ==> use n threads

heurtree           heuristics to apply during tree search:  sum of
                   the same values as for heurroot; default 17

iis                [no assignment] if the problem is infeasible, find an
                   Irreducible Independent Set of infeasible constraints
                   and return it in suffix .iis.  If changing the bounds
                   on just one constraint or variable could remove the
                   infeasibility, return suffix .iso with value 1 for
                   each such constraint or variable.

indlinbigm         largest "big M" value to use in converting indicator
                   constraints to regular constraints; default = 1e5.

indprelinbigm      largest "big M" value to use in converting indicator
                   constraints to regular constraints during XPRESS
                   presolve; default = 100.0

inputtol           tolerance on input elements (default 0.0); any value v where
                   abs(v) <= inputtol is treated as 0

invertfreq         maximum simplex iterations before refactoring the basis:
                   -1 = automatic choice (default)

invertmin          minimum simplex iterations before refactoring the basis:
                   default = 3

keepbasis          basis choice for the next LP iteration:
                        0 = ignore previous basis
                        1 = use previous basis (default)
                        2 = use previous basis only if the number of basic
                                variables == number of constraints

keepnrows          1 (default) if unconstrained rows are to be kept, else 0

lazy               whether to regard constraints with nonzero .lazy suffix
                   values as lazy (i.e., delayed) constraints if the problem
                   is a MIP:
                        0 = no
                        1 = yes (default)

lnpbest            number of global infeasible entities for which to create
                   lift-and-project cuts during each round of Gomory cuts
                   at the top node; default = 50

lnpiterlimit       maximum iterations for each lift-and-project cut;
                   default = -1 (automatic choice)

localchoice        when to backtrack between two child nodes
                   during a "dive":
                        1 = never backtrack from the first child unless it
                                is dropped (i.e., is infeasible or cut off)
                        2 = always solve both nodes first
                        3 = automatic choice (default)

logfile            name of log file; default = no log file

lpfolding          whether to attempt exploiting symmetries by "LP Folding":
                        -1 = automatic choice (default)
                         0 = no
                         1 = yes.

lpiterlimit        simplex iteration limit; default = 2147483647 = 2^31 - 1

lplog              frequency of printing simplex iteration log; default = 100

lpref_itlim        limit on simplex iterations used by the solution refiner
                   (see refineops); default = -1 ==> automatic choice

lpthreads          number of threads in concurrent LP solves:
                        -1 = determine from "threads" keyword (default)
                        n > 0 ==> use n threads

markowitztol       Markowitz tolerance used when factoring the basis matrix
                   default = 0.01

matrixtol          zero tolerance on matrix elements; default = 1e-9

maxcuttime         maximum time (CPU seconds) to spend generating cuts
                   and reoptimizing; default = 0 ==> no limit

maxiis             maximum number of Irreducible Infeasible Sets to find:
                        -1 = no limit (default)
                         0 = none

maxim              [no assignment] force maximization of the objective

maximise           [no assignment] force maximization of the objective

maximize           [no assignment] force maximization of the objective

maximpliedbound    when preprocessing MIP problems, only use computed bounds
                   at most maximpliedbound (default 1e8) in absolute value

maxlocalbt         max height above current node to look for a local backtrack
                   candidate node; default = 1

maxlogscale        max log2 of factors used in scaling; must be >= 0 and
                   <= 64; default 64

maxmemory          limit (integer number of megabytes) on memory used:
                        -1 = automatic choice (default)
                        >0 = target megabytes of memory to use

maxmemoryhard      hard limit (integer number of megabytes) on memory
                   allocated, causing early termination if exceeded
                        0 (default) = no limit

maxmipsol          maximum number of integer solutions to find:
                        0 = no limit (default)

maxmiptasks        maximum tasks to run in parallel during a MIP solve:
                           -1 ==> use mipthreads
                        n > 0 ==> at most n tasks running at once
                   For maxmiptasks > 0, branch-and-bound nodes are solved in a
                   deterministic way, but the barrier algorithm (if used) may
                   cause a nondeterministic MIP solve unless barthreads = 1.

maxnode            maximum number of MIP nodes to explore; default = 2147483647

maxpagelines       maximum output lines between page breaks in logfile;
                   default = 23

maxstalltime       maximum time in seconds that the Optimizer will continue to
                   search for improving solution after finding a new incumbent:
                            0 ==> no limit (default)
                        n > 0 ==> stop after n seconds without a
                                  new incumbent (no effet before
                                  the first has been found

maxtime            limit on solution time:  for maxtime=n (an integer),
                        n < 0 ==> stop LP or MIP search after -n seconds
                        n = 0 ==> no time limit (default)
                        n > 0 ==> for MIP problems, stop after n seconds
                                  if a feasible solution has been found;
                                  otherwise continue until a feasible
                                  solution has been found.

minim              [no assignment] force minimization of the objective

minimise           [no assignment] force minimization of the objective

minimize           [no assignment] force minimization of the objective

mipabscutoff       initial MIP cutoff:  ignore MIP nodes with objective values
                   worse than mipabscutoff; default = 1e40 for minimization,
                   -1e40 for maximization

mipabsstop         stop MIP search if abs(MIPOBJVAL - BESTBOUND) <= mipabsstop
                   default = 0

mipaddcutoff       amount to add to the objective function of the best integer
                   solution found to give the new MIP cutoff; default -1e-5

mipcomponents      determines whether disconnected components in a MIP should
                   be solved as separate MIPs:
                        -1 ==> automatic (default)
                         0 ==> disable
                         1 ==> enable

mipconcurnodes     node limit to choose the winning solve when concurrent
                   solves are enabled:
                           -1 ==> automatic (default)
                        n > 0 ==> number of nodes to complete

mipconcursolves    select the number of concurrent solves to start for a MIP:
                           -1 ==> enabled, the number of concurrent solves
                                  depends on mipthreads
                         0, 1 ==> disabled (default)
                        n > 1 ==> number of concurrent solves = n

mipdualreductions  kinds of dual reductions allowed during branch and bound:
                        0 ==> none
                        1 ==> all (default)
                        2 ==> restrict dual reductions to continuous variables.
                   If poolnbest > 1 is specified, specifying
                   mipdualreductions = 2 might be prudent.

mipkappafreq       during branch-and-bound, how often to compute
                   basis condition numbers:
                        0 ==> never (default)
                        1 ==> every node
                        n > 1 ==> once per node at level n of the
                                branch-and-bound tree.
                   When mipkappafreq > 0, a final summary shows the number of
                   sampled nodes that are
                        "stable": kappa < 10^7
                        "suspicious": 10^7 <= kappa < 10^10
                        "unstable": 10^10 <= kappa < 10^13
                        "ill-posed": 10^13 <= kappa.
                   A "Kappa attention level" between 0 and 1 is also reported.
                   Condition numbers use the Frobenius norms of the basis
                   and its inverse.

miplog             MIP printing level to logfile (default -100):
                        -n = print summary line every n MIP nodes
                         0 = no MIP summary lines
                         1 = only print a summary at the end
                         2 = log each solution found
                         3 = log each node

mipops             MIP solver options:  one of
                        0 = traditional primal first phase (default)
                        1 = Big M primal first phase
                        2 = traditional dual first
                        3 = Big M dual first
                        4 = always use artificial bounds in dual
                        5 = use original basis only when warmstarting
                        6 = skip primal bound flips for ranged primals
                        7 = also do single-pivot crash
                        8 = suppress aggressive dual perturbations

mippresolve        MIP presolve done at each node: sum of
                            1 = reduced-cost fixing
                            2 = logical preprocessing of binary variables
                            4 = ignored; replaced by "preprobing"
                            8 = allow changing continuous-variable bounds
                           16 = allow dual reductions
                           32 = allow global tightening of the problem
                           64 = use objective function
                          128 = allow restarting
                          256 = allow use of symmetry
                   default = -1 (automatic choice)

miprampup          whether to limit the number of parallel tasks
                   during the ramp-up phase of the parallel MIP algorithm:
                        -1 = automatic choice (default)
                         0 = no: use as many tasks as possible
                         1 = yes, until finished with initial dives

miprefiterlim      max. simplex iterations per reoptimization in MIP refiner
                   when refineops is 2 or 3; default -1 ==> automatic choice

miprelcutoff       fraction of best integer solution found to add to MIP
                   cutoff; default 1e-4

miprelstop         stop MIP search if
                   abs(MIPOBJVAL - BESTBOUND) < miprelstop * abs(BESTBOUND);
                   default = 0.0001

miprestart         MIP: control strategy for in-tree restarts:
                   -1 = determined automatically (default)
                    0 = disable in-tree restarts
                    1 = normal aggressiveness
                    2 = higher aggressiveness

miprestartfactor   MIP: fine tune initial conditions to trigger an in-tree
                   restart; values > 1 increase the aggressiveness, < 1
                   decrease it (default 1.0)

miprestartgaptol   MIP: initial gap threshold to delay in-tree restart;
                   the restart is delayed if the relative gap is below the
                   threshold (default 0.02)

mipstart           synonym for mipstartvalue

mipstartstatus     whether to use incoming statuses on MIP problems;
                   default 1 ==> yes

mipstartvalue      whether to use the specified initial guess (if supplied)
                   when solving a MIP problem:
                        0 = no
                        1 = yes (default)

mipstop            how to stop a MIP solve when a time or node limit is
                   reached:
                        0 = stop tasks as soon as possible (default)
                        1 = let currently running tasks finish, but do not
                                start new ones

mipthreads         number of threads to use solving mixed-integer
                   programming problems:
                        -1 = use "threads" keyword (default)
                        n > 0 ==> use n threads

miptol             integer feasibility tolerance; default = 5e-6

miptoltarget       value of miptol used for refining equalities on MIP
                   problems when refineops is 2 or 3; default = 0

miqcpalg           algorithm for solving mixed-integer problems with quadratic
                   or second-order cone constraints:
                        -1 = automatic choice (default)
                         0 = barrier algorithm during branch and bound
                         1 = outer approximations during branch and bound

netstalllimit      limit the number of degenerate pivots of the network
                   simplex algorithmm before switching to primal or dual:
                           -1 ==> automatic
                            0 ==> no limit
                        n > 0 ==> limit to n iterations

network            [no assignment] try to find and exploit an embedded network

nodeprobingeffort  effort put into probing during branch and bound; the
                   number is used as a multiplier on the default amount of
                   work.  Set to 0 to disable node probing; default 1.

nodeselection      next MIP node control:
                        1 = local first:  choose among descendant and sibling
                            nodes if available, else from all outstanding nodes
                        2 = best first of all outstanding nodes
                        3 = local depth first:  choose among descendant and
                            sibling nodes if available, else from deepest nodes
                        4 = best first for breadthfirst nodes, then local first
                        5 = pure depth first:  choose among deepest nodes.
                   The default is determined from matrix characteristics.

objno              objective number (0=none, 1=first...)

objrep             Whether to replace
                        minimize obj: v;
                   with
                        minimize obj: f(x)
                   when variable v appears linearly in exactly one
                   constraint of the form
                        s.t. c: v >= f(x);
                   or
                        s.t. c: v == f(x);
                   Possible objrep values:
                        0 = no
                        1 = yes for v >= f(x)
                        2 = yes for v == f(x) (default)
                        3 = yes in both cases
                   For a maximization problem, "<=" replaces ">=".

objscalefactor     Power of 2 (default 0) by which the objective is scaled.
                   Nonzero objscalfactor values override automatic global
                   objective scaling.

optimalitytol      tolerance on reduced cost; default = 1e-6

opttol_target      feasibility tolerance on reduced costs for solution refiner
                   (see refineops):  default = 0; if opttol_target > 0 is
                   specified, it is used instead of optimalitytol.

outlev             message level:
                        1 = all
                        2 = information
                        3 = warnings & errors only (default)
                        4 = errors
                        5 = none

outputtol          zero tolerance on print values; default 1e-5

param              Used with syntax "param=name=value" (no spaces), where
                   "name" is the name of an XPRESS control parameter and
                   "value" is to be assigned to that parameter.  If value is
                   ?, report the current value of the parameter.  If name is
                   a string control, value can be a quoted string or a
                   sequence of nonblank characters other than comma.  This
                   facility provides a way to modify control parameters,
                   identified by name or number, that have not (yet) been
                   assigned a keyword.  As a special case, "param=?" requests
                   a list of all control parameters and their current values.

penalty            minimum absolute penalty variable coefficient;
                   default = automatic choice

permuteseed        seed for the random-number generator used by prepermute;
                   default = 1

pivottol           zero tolerance for pivots; default = 1e-9

pooldualred        Whether to suppress removal of dominated solutions (via
                   "dual reductions") when poolstub is specified:
                        0 = yes (default, which can be expensive)
                        1 = no
                        2 = honor presolveops bit 3 (2^3 = 8)

pooldupcol         Whether to suppress duplicate variable removal when
                   poolstub is specified:
                        0 = yes (default, which can be expensive)
                        1 = no
                        2 = honor presolveops bit 5 (2^5 = 32)

pooldups           How poolstub should handle duplicate solutions:
                        0 = retain all duplicates
                        1 = discard exact matches
                        2 = discard exact matches of continuous variables
                                and matches of rounded values of discrete
                                variables
                        3 = default: discard matches of rounded values of
                                discrete variables
                   Rounding of discrete variables is affected by poolmiptol
                   and poolfeastol.

poolfeastol        Zero tolerance for discrete variables in the solution
                   pool (see poolstub); default = 1e-6.

poolmiptol         Error (nonintegrality) allowed in discrete variables
                   in the solution pool (see poolstub); default = 5e-6.

poolnbest          Whether the solution pool (see poolstub) should contain
                   inferior solutions.  When poolnbest = n > 1, the
                   solution pool is allowed to keep the n best solutions.

poolstub           Stub for solution files in the MIP solution pool.
                   Ignored unless some variables are integer or binary.
                   A pool of alternate MIP solutions is computed if
                   poolstub is specified, and the solutions in this pool
                   are written to files

                      (poolstub & '1') ... (poolstub & |solution pool|),

                   where |solution pool| is the number of solutions in the
                   solution pool.  That is, file names are obtained by
                   appending 1, 2, ... |solution pool| to poolstub.  The
                   value of |solution pool| is returned in suffix npool
                   on the objective and problem.

ppfactor           partial-pricing candidate-list size factor; default = 1.0

preanalyticcenter  whether to compute and use analytic centers while solving
                   MIP problems:
                        -1 = automatic choice (default)
                         0 = no
                         1 = yes, but only for variable fixing
                         2 = yes, but only for computing reduced costs
                         3 = yes, for both variable fixing and reduced costs.

prebasisred        whether XPRESS's presolve should try to use a lattice basis
                   reduction algorithm:
                        -1 = automatic choice (default)
                         0 = no
                         1 = yes.

prebndredcone      for MIP problems, whether to use cone constraints to
                   reduce bounds on variables:
                         0 = no
                         1 = yes
                        -1 = default (undocumented)

prebndredquad      for MIP problems, whether to use convex quadratic
                   constraints to reduce bounds on variables:
                         0 = no
                         1 = yes
                        -1 = default (undocumented)

precoefelim        whether XPRESS's presolve should recombine constraints:
                        0 = no,
                        1 = yes, as many as possible
                        2 = yes, cautiously (default)

precomponents      whether XPRESS's presolve should detect and separately
                   solve independent MIP subproblems:
                        -1 = automatic choice (default)
                         0 = no
                         1 = yes

preconvertsep      How to reformulate problems with nondiagonal quadratic
                   objectives or constraints:
                        -1 = automatic choice (default)
                         0 = no reformulation
                         1 = reformulate to diagonal constraints
                         2 = also allow reduction to second-order cones
                         3 = also convert the objective to a constraint.

predomcol          whether XPRESS's presolve should remove variables
                   when solving MIP problems:
                        -1 = automatic choice (default)
                         0 = no
                         1 = yes, cautiously
                         2 = yes, check all candidates

predomrow          whether XPRESS's presolve should remove constraints
                   when solving MIP problems:
                        -1 = automatic choice (default)
                         0 = no
                         1 = yes, cautiously
                         2 = yes, medium strategy
                         3 = yes, check all candidates

preduprow          how XPRESS's presolve should deal with duplicate rows
                   in MIP problems:
                        -1 = automatic choice (default)
                         0 = do not remove duplicate rows (constraints)
                         1 = remove duplicate rows identical in all variables
                         2 = like 1 but allowing simple penalty variables
                         3 = like 1 but allowing more complex penalty variables

prefolding         choose if folding aggregate continuous column in an
                   equitable partition:
                        -1 = automatic choiche (default)
                         0 = disabled
                         1 = enabled

preimplications    whether XPRESS's presolve should use implication
                   structures to remove redundant rows:
                        -1 = automatic choice (default)
                         0 = no
                         1 = yes

prelindep          whether to check for and remove linearly dependent
                   equality constraints:
                        -1 = automatic choice (default)
                         0 = no
                         1 = yes

preobjcutdetect    on MIP problems, whether to check for constraints
                   that are (nearly) parallel to a linear objective function
                   and can be removed safely:
                        0 = no
                        1 = yes (default)

prepermute         whether to randomly permute variables or constraints before
                   applying XPRESS's presolve:  sum of
                        1 ==> permute constraints
                        2 ==> permute variables
                        4 ==> permute global MIP information
                   default = 0; see permuteseed

preprobing         how much probing on binary variables to do during XPRESS's
                   presolve:
                        -1 = automatic choice (default)
                         0 = none
                         1 = light probing
                         2 = full probing
                         3 = repeated full probing

presolve           whether to use XPRESS's presolver:
                        0 = no
                        1 = yes, removing redundant bounds (default)
                        2 = yes, retaining redundant bounds

presolvemaxgrow    factor by which the number of nonzero coefficients
                   may grow during XPRESS's presolve; default = 0.1

presolveops        reductions to use in XPRESS's presolve:  sum of
                            1 = 2^0  = remove singleton columns
                            2 = 2^1  = remove singleton constraints (rows)
                            4 = 2^2  = forcing row removal (whatever that is)
                            8 = 2^3  = dual reductions
                           16 = 2^4  = redundant constraint (row) removal
                           32 = 2^5  = duplicate variable removal
                           64 = 2^6  = duplicate constraint removal
                          128 = 2^7  = strong dual reductions
                          256 = 2^8  = variable eliminations
                          512 = 2^9  = no IP reductions
                         1024 = 2^10 = no semicontinuous variable detection
                         2048 = 2^11 = no advanced IP reductions
                        16384 = 2^14 = remove linearly dependent constraints
                        32768 = 2^15 = no integer variable and SOS detection
                   default = 511 (bits 0-8 set).

presolvepasses     Number of rounds to use in the XPRESS presolve algorithm;
                   default = 1.

pricingalg         primal simplex pricing method:
                        -1 = partial pricing
                         0 = automatic choice (default)
                         1 = Devex pricing

primal             [no assignment] use the primal simplex algorithm

primalops          primal simplex options:  sum of
                        1 = 2^0 = aggressive dj scaling
                        2 = 2^1 = conventional dj scaling
                        4 = 2^2 = reluctant switching back to partial pricing
                        8 = 2^3 = dynamic switching between cheap and expensive pricing
                        default = all of the above; if bits 0 and 1 are the same (both on or
                        both off), choose dj scaling automatically

primalperturb      Factor by which to possibly perturb the problem in the
                   dual primal algorithm.  If >= 0, overrides "perturb".
                   Default -1 ==> automatic choice; 0 ==> no perturbatation.

primalunshift      whether the primal alg. calls the dual to unshift:
                        0 = yes (default)
                        1 = no

pseudocost         default pseudo-cost assumed for forcing an integer variable
                   to an integer value; default = 0.01

pseudocost_ud      how to update pseudocosts during branch-and-bound:
                        -1 = automatic choice (default)
                         0 = no updates
                         1 = use only regular branches
                         2 = use regular and strong branch results
                         3 = use results from all nodes

qccuts             when using miqcpalg=1 to solve a mixed-integer problem that
                   has quadratic constraints or second-order cone constraints,
                   the number of rounds of outer approximation cuts at the top
                   node:  default = -1 means automatic choice.

qcrootalg          when using miqcpalg=1 to solve a mixed-integer problem that
                   has quadratic constraints or second-order cone constraints,
                   the algorithm for solving the root node:
                        -1 = automatic choice (default)
                         0 = barrier algorithm
                         1 = dual simplex on outer approximations

quadunshift        whether quadratic simplex should do an extra
                        purification after finding a solution:
                        -1 = automatic choice (default)
                         0 = no
                         1 = yes

ray                whether to return a ray of unboundedness in suffix .unbdd:
                        0 ==> no (default)
                        1 ==> yes, after suppressing XPRESS's presolve
                        2 ==> yes, without suppressing XPRESS's presolve
                   The last setting (ray=2) may give wrong results when
                   XPRESS's presolve detects infeasibility.  Both ray=1 and
                   ray=2 cause reoptimization with primal simplex if some other
                   algorithm was used.  No ray is returned for MIP problems.

refineops          whether refine equalities -- to reduce infeasibilities
                   in constraints that should hold as equalities: sum of
                         1 ==> refine LP solutions
                         2 ==> refine MIP solutions;
                         4 ==> refine the final MIP solution found
                         8 ==> refine each node of the search tree
                        16 ==> refine non-global solutions
                        32 ==> refine all solutions
                        64 ==> use higher precision during iterative refinement
                       128 ==> use the primal simplex algorithm for refining
                       256 ==> use the dual simplex algorithm for refining
                       512 ==> refine MIP solutions such that rounding them
                                keeps the problem feasible when reoptimized
                      1024 ==> attempt to refine MIP solutions such that
                                rounding them keeps the problem feasible when
                                reoptimized, but accept integers solutions
                                even if refinement fails.
                   default = 1 + 2 + 16 = 19.

relax              [no assignment] ignore integrality

relaxtreemem       fraction of memory limit by which to relax "treememlimit"
                   when too much structural data appears; default 0.1

relpivottol        relative pivot tolerance default = 1e-6

repairindefq       whether to repair indefinite quadratic forms:
                        0 = yes
                        1 = no (default)

resourcestrategy   whether to allow nondeterministic decisions to cope with
                   low memory (affected by maxmemory and maxmemoryhard):
                        0 = no (default)
                        1 = yes

rootpresolve       whether to presolve after root cutting and heuristics:
                        -1 = automatic choice (default)
                         0 = no
                         1 = yes

round              whether to round integer variables to integral values before
                   returning the solution, and whether to report that XPRESS
                   returned noninteger values for integer values:  sum of
                         1 ==> round nonintegral integer variables
                         2 ==> do not modify solve_result
                         4 ==> do not modify solve_message
                         8 ==> report modifications even if maxerr < 1e-9
                   Modifications take place only if XPRESS assigned nonintegral
                   values to one or more integer variables, and (for round < 8)
                   are reported if the maximum deviation from integrality
                   exceeded 1e-9.  Default = 1.

sbbest             For MIP problems, the number of infeasible
                   global entities on which to perform strong branching;
                   default -1 ==> automatic choice.

sbeffort           multiplier on strong-branching controls that
                   are set to "automatic"; default = 1.0

sbestimate         how to compute pseudo costs from the local node
                   when selecting an infeasible entity to branch on:
                        -1 = automatic choice (default)
                        1-6 = particular strategies (not described)

sbiterlimit        Number of dual iterations to perform the strong branching;
                   0 ==> none; default = -1 (automatic choice)

sbselect           size of candidate list for strong branching:
                        -2 = low-effort automatic choice (default)
                        -1 = high-effort automatic choice
                        n >= 0 ==> include max(n, sbbest) candidates

scaling            how to scale the constraint matrix before optimizing: sum of
                            1 = 2^0 = row scaling
                            2 = 2^1 = column scaling
                            4 = 2^2 = row scaling again
                            8 = 2^3 = maximum scaling
                           16 = 2^4 = Curtis-Reid
                           32 = 2^5 = scale by maximum element (rather
                                        than by geometric mean)
                           64 = 2^6 = no special handing for big-M constraints
                          128 = 2^7 = objective-function scaling
                          256 = 2^8 = excluding quadratic part of constraint
                                        when calculating scaling factors
                          512 = 2^9 = scale before presolve
                         1024 = 2^10 = do not scale constraints (rows) up
                         2048 = 2^11 = do not scale variables down
                         4096 = 2^12 = do global objective function scaling
                         8192 = 2^13 = do right-hand side scaling
                        16384 = 2^14 = disable aggressive quadratic scaling
                        32768 = 2^15 = disable explicit slack scaling.
                   Default = 163.

sifting            when using dual simplex, whether to enable sifting,
                   which can speed up the solve when there are many more
                   variables than constraints:
                        -1 = automatic choice (default)
                         0 = no
                         1 = yes

siftpasses         how quickly we allow the worker problems to grow during the
                   sifting algorithm; large values might reduce the number of
                   iterations but increase the solve time for each.  Default 4.

siftpresolveops    presolve operations for solving the subproblems during
                   sifting:
                         -1 = use presolveops value (default)
                        > 0 = use this value

siftswitch         determines which algoorithm to use during sifting
                           -1 ==> dual simplex
                            0 ==> barrier
                        n > 0 ==> barrier if the number of dual
                                  infeasibilities > n else dual simplex

sleeponthreadwait  whether threads should sleep while awaiting work:
                        0 = no (busy-wait)
                        1 = yes (sleep; may add overhead)
                   default = -1 (automatic choice)

sos                whether to use explicit SOS information; default 1 ==> yes

sos2               whether to tell XPRESS about SOS2 constraints for
                   nonconvex piecewise-linear terms; default 1 ==> yes

sosreftol          minimum relative gap between reference row entries;
                   default = 1e-6

symmetry           amount of effort to detect symmetry in MIP problems:
                        0 = none: do not attempt symmetry detection
                        1 = modest effort (default)
                        2 = aggressive effort

threads            default number of threads to use:
                        -1 = automatic choice (based on hardware)
                         n > 0 ==> use n threads

timing             [no assignment] give timing statistics

trace              whether to explain infeasibility:
                        0 = no (default)
                        1 = yes

treecompress       level of effort at data compression when branch-and-bound
                   memory exceeds "treememlimit":  higher ==> greater effort
                   (taking more time); default = 2

treecovercuts      number of rounds of lifted-cover inequalities at MIP nodes
                   other than the top node (cf covercuts);
                   default = -1 (automatic choice)

treecuts           cuts to generate at nodes during tree search:  sum of
                            32 = 2^5  = clique cuts
                            64 = 2^6  = mixed-integer rounding (MIR) cuts
                            64 = 2^7  = lifted-cover cuts
                          2048 = 2^11 = flow-path cuts
                          4096 = 2^12 = implication cuts
                          8192 = 2^13 = lift-and-project cuts
                         16384 = 2^14 = disable cutting from row cuts
                         32768 = 2^15 = lifted GUB cover cuts
                         65536 = 2^16 = zero-half cuts
                        131072 = 2^17 = indicator cuts.
                   Default = 259839 (same effect as -2305).

treegomcuts        number of rounds of Gomory cuts to generate at MIP nodes
                   other than the top node (cf covercuts);
                   default = -1 (automatic choice)

treememlimit       an integer: soft limit in megabytes on memory to use for
                   branch-and-bound trees.  Default = 0 ==> automatic choice.

treememtarget      fraction of "treememlimit" to try to recover by compression
                   or writing to nodefile when  "treememlimit" is exceeded.
                   Default = 0.2

treeoutlev         how much to report about branch-and-bound trees
                   (if allowed by outlev):  sum of
                        1 = regular summaries
                        2 = report tree compression and output to nodefile
                   default = 3

tunerdir           directory for tuner results; specifying tunerdir causes
                   the XPRESS tuner to solve the problem several times
                   to find good settings for solving similar problems.
                   Results are stored in tunerdir and its subdirectories.

tunerhistory       when tunerdir is specified, whether to reuse previous
                   tuner results and/or to augment them:
                        0 = discard previous tuner results
                        1 = ignore previous tuner results,
                                but add new results to them
                        2 = reuse previous tuner results and add
                                new results to them (default).

tunermaxtime       maximum seconds to run the tuner when tunerdir is
                   specified.  Default 0 ==> no limit.  Use "maxtime" to limit
                   the time the tuner uses for each problem solved.

tunermethod        method for tuning when tunerdir is specified:
                        -1 = automatic choice (default)
                         0 = default LP tuner
                         1 = default MIP tuner
                         2 = more elaborate MIP tuner
                         3 = root-focused MIP tuner
                         4 = tree-focused MIP tuner
                         5 = simple MIP tuner
                         6 = default SLP tuner
                         7 = default MISLP tuner
                         8 = MIP tuner using primal heuristics.

tunermethodfile    name of a file that can be read to specify the
                   method for tuning (overriding tunermethod) when tunerdir
                   is specified.

tunerpermute       when running the XPRESS tuner and tunerpermute = n > 0,
                   solve the original problem and n permutations thereof.

tunertarget        what to measure to compare two problem solutions
                   when running the XPRESS tuner (what to measure):
                        -1 = automatic choice (default)
                         0 = solution time, then integrality gap
                         1 = solution time, then best bound
                         2 = solution time, then best integer solution
                         3 = the "primal dual integral", whatever that is
                         4 = just solution time (default for LPs)
                         5 = just objective value
                         6 = validation number (probably not relevant)
                         7 = integrality gap only
                         8 = best bound only
                         9 = best integer solution only.

tunerthreads       number of tuner threads to run in parallel:
                   default -1 ==> automatic choice.
                   "threads" controls the number of threads for each solve.
                   The product of threads and tunerthreads should not exceed
                   the number of threads the system can run in parallel.

varselection       how to score the integer variables at a MIP node, for
                        branching on a variable with minimum score:
                        -1 = automatic choice (default)
                         1 = minimum of the 'up' and 'down' pseudo-costs
                         2 = 'up' pseudo-cost + 'down' pseudo-cost
                         3 = maximum of the 'up' and 'down' pseudo-costs plus
                             twice their minimum
                         4 = maximum of the 'up' and 'down' pseudo-costs
                         5 = the 'down' pseudo-cost
                         6 = the 'up' pseudo-cost

version            Report version details before solving the problem.  This is
                   a single-word "phrase" that does not accept a value
                   assignment.

wantsol            solution report without -AMPL: sum of
                        1 = write .sol file
                        2 = print primal variable values
                        4 = print dual variable values
                        8 = do not print solution message

writeprob          Name of file to which the problem is written
                   in a format determined by the name's suffix:
                        .mps = MPS file;
                        .lp = LP file.
```

