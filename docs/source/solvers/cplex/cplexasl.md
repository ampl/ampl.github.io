
# CPLEXASL Options

```ampl
ampl: option solver cplexasl; # change the solver
ampl: option cplexasl_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

Solver options obtained with `$ cplexasl -=`.

```
absmipgap              Absolute mixed-integer optimality gap tolerance
                       (for difference between current best integer solution
                       and optimal value of LP relaxation).  Default 0.

advance                Whether to use advance basis information (initial
                       primal and dual variable values and basis indicators).
                       Default 1 (yes).

aggcutlim              Bound on the number of constraints aggregated to
                       generate flow-cover and mixed-integer-rounding cuts;
                       default = 3.

aggfill                Synonym for "agglim".

agglim                 Variables that appear in more than agglim rows
                       (default 10) will not be substituted away by the
                       "aggregate" algorithm.

aggregate              Whether to make substitutions to reduce the number of
                       rows:  0 ==> no; n > 0 ==> apply aggregator n times.
                       Default -1 ==> automatic choice.

aggtol                 Pivot tolerance for aggregating.  It seldom needs
                       fiddling.  Default = .05; must be in [1e-10, .99].

autoopt                Single-word phrase:  use CPLEX's automatic choice of
                       optimizer (currently dualopt for LPs).

autopt                 Synonym for "autoopt".

auxrootthreads         Controls the number of threads used for auxiliary
                       chores when solving the root node of a MIP problem.
                       When N threads are available (possibly limited by
                       "threads"), auxrootthreads must be less than N.
                       Possible values:
                           0 = automatic choice (default)
                           n < N:  use N-n threads for the root node and
                                n threads for auxiliary chores.

backtrack              Tolerance (> 0, default 0.9999) for when to backtrack
                       during branch & bound.  Low values tend to pure
                       best-bound search.  High values (> 1) tend to pure
                       depth-first search.  Values less than the default
                       are often good when subproblems are expensive.

baralg                 How to start the barrier algorithm:
                           0 (default) = 1 for MIP subproblems, else 3
                           1 = infeasibility-estimate start
                           2 = infeasibility-constant start
                           3 = standard start.

barcorr                Limit on centering corrections in each iteration
                       of the barrier algorithm:
                           -1 = decide automatically (default)
                           nonnegative = at most that many.

bardisplay             Specifies how much the barrier algorithm chatters:
                           0 = no output (default)
                           1 = one line per iteration
                           2 = more output.

bargrowth              Tolerance for detecting unbounded faces in the
                       barrier algorithm: higher values make the test
                       for unbounded faces harder to satisfy.
                       Default = 1e12.

bariterlim             Maximum barrier iterations allowed (default 2^31 - 1).

barobjrange            Limit on the absolute objective value before the
                       barrier algorithm considers the problem unbounded.
                       Default = 1e20.

baropt                 Single-word phrase:  use the barrier algorithm
                       (unless there are discrete variables).

barstart               Barrier starting-point algorithm:
                           1 = assume dual is 0 (default)
                           2 = estimate dual
                           3 = average of primal estimate, 0 dual
                           4 = average of primal and dual estimates.

barstartalg            Synonym for "barstart".

basis_cond             Whether to show the condition number of the simplex
                       basis in the solve_message and to return its value
                       in the problem.basis_cond and objective.basis_cond
                       suffixes.  (Default = 0 = no; 1 = yes).

bbinterval             For nodeselect = 2, select the best-bound node,
                       rather than the best-estimate node, every
                       bbinterval iterations (default 7); 0 means
                       always use the best-estimate node.

benders_feascut_tol    Tolerance for violations of feasibility cuts in Benders
                       algorithm.  Default = 1e-6.

benders_optcut_tol     Tolerance for violations of optimality cuts in Benders
                       algorithm.  Default = 1e-6.

benders_strategy       How to decompose the problem for Benders algorithm:
                          -1 = do not apply Benders algorithm
                           0 = automatic choice (default): if suffix benders
                                is present on variables, variables that have
                                .benders = 0 go into the master and CPLEX
                                assigns other variables to workers; otherwise
                                integer variables go into the master and
                                continuous variables into workers
                           1 = use suffix benders to determine which variables
                                are for the master (.benders = 0) and which
                                for workers (.benders = n > 0 ==> worker n
                           2 = similar to 0, but suffix benders is required
                           3 = similar to 0, but ignore suffix benders (if
                                present).

benders_worker         Designate the algorithm that CPLEX applies to solve the
                       subproblems when using Benders decomposition:
                           0 = automatic (default)
                           1 = primal simplex
                           2 = dual simplex
                           3 = network simplex
                           4 = barrier algorithm
                           5 = sifting algorithm.

bendersopt             Single-word phrase:  use Benders algorithm.
                       Both integer and continuous variables must be present.

bestbound              Single-word phrase requesting return of suffix
                       .bestbound on the objective and problem for the
                       best known bound on the objective value.  For MIP
                       problems with .bestnode value from a feasible node
                       (see below), .bestbound = .bestnode.

bestnode               Single-word phrase requesting return of suffix
                       .bestnode on the objective and problem for the
                       objective value at the best feasible MIP node.
                       For non-MIP problems and for MIP problems for which
                       a feasible node has not yet been found, this value
                       is +Infinity for minimization problems and -Infinity
                       for maximization problems.

boundstr               Whether to use bound strengthening in solving MIPs:
                          -1 (default) = automatic choice
                           0 = never
                           1 = always.

bqpcuts                Whether to generate boolean quadratic polytope (BQP)
                       cuts for nonconvex QP amd MIQP problems when solved
                       to optimality:
                          -1 = do not generate BQP cuts
                           0 = automatic choice (default)
                           1 = generate BQP cuts moderateely
                           2 = generate BQP cuts agressively
                           3 = generate BQP cuts very agressively.

branch                 Branching direction for integer variables:
                       -1 = down, 0 = algorithm decides, 1 = up; default = 0.

branchdir              Synonym for "branch".

cliquecuts             Synonym for "cliques".

cliques                Whether to use clique cuts in solving MIPs:
                          -1 = never
                          0 = automatic choice (default)
                          1, 2, 3 = ever more aggressive generation.

clocktype              Kind of times CPLEX reports during the solution
                       process:
                          0 = automatic choice
                          1 = CPU time
                          2 = wall clock time (total elapsed time = default)

coeffreduce            Whether to use coefficient reduction when
                       preprocessing MIPS:
                         -1 = automatic choice (default)
                          0 = no
                          1 = reduce only integral coefficients
                          2 = reduce all potential coefficients
                          3 = reduce aggressively with tiling.

comptol                Convergence tolerance for barrier algorithm:
                       the algorithm stops when the relative
                       complementarity is < bartol (default 1e-8).

concurrent             Single-word phrase:  with CPLEX versions >= 8
                       and when hardware and licensing permit, try
                       several methods in parallel.

concurrentopt          Synonym for "concurrent".

conflictalg            Choice of algorithm used by the CPLEX's conflict
                       refiner:
                          0 = automatic choice (default)
                          1 = fast
                          2 = propagate
                          3 = presolve
                          4 = IIS
                          5 = limited solve
                          6 = full solve.
                       Settings 1, 2, and 3 are fast but may not discard
                       many constraints; 5 and 6 work harder at this.
                       Setting 4 searches for an Irreducible Infeasible
                       Set of linear constraints (e.g., ignoring quadratic
                       constraints).

conflictdisplay        What to report when the conflict finder is working:
                          0 = nothing
                          1 = summary (default)
                          2 = detailed display.

covercuts              Synonym for "covers".

covers                 Whether to use cover cuts in solving MIPs:
                          -1 = never
                          0 = automatic choice (default)
                          1, 2, 3 = ever more aggressive generation.

cpumask                Whether and how to bind threads to cores
                       on systems where this is possible:
                           off = no CPU binding
                           auto = automatic binding (default).
                       Values other than "off" and "auto" must be a
                       hexadecimal string (digits 0-9 and a-f, ignoring
                       case, so values A-F and a-f are treated alike).
                       The lowest order bit is for the first logical CPU.
                       For example, "a5" and "A5" indicate that CPUs 0, 2,
                       5, and 7 are available for binding to threads, since
                       hex value a5 = 2^7 + 2^5 + 2^2 + 2^0.

crash                  Crash strategy (used to obtain starting basis);
                       possible values = -1, 0, 1; default = 1.
                       The best setting is problem-dependent and
                       can only be found by experimentation.
                       0 completely ignores the objective.

crossover              Causes the barrier algorithm to be run (in the
                       absence of discrete variables) and specifies
                       whether to "crossover" to an optimal simplex
                       basis afterwards:
                          0 = no crossover
                          1 = crossover with primal simplex
                              (default for baropt)
                          2 = crossover with dual simplex.

cutpass                Number of passes permitted when generating MIP
                       cutting plane:
                          -1 = none
                          0 = automatic choice (default)
                          positive = at most that many passes.

cutsfactor             Limit on MIP cuts added:
                          > 1 ==> (cutsfactor-1)*m, where m
                       is the original number of rows (after presolve);
                          < 0 ==> no limit;
                          0 <= cutsfactor <= 1 ==> no MIP cuts
                       Default = -1 (no limit).

cutstats               0 or 1 (default 0):  Whether the solve_message report
                       the numbers and kinds of cuts used.

datacheck              debug option; possible values:
                          0 = no data checking (default)
                          1 = issue warnings
                          2 = try to "assist" by warning about bad scaling.

dense                  Synonym for "densecol".

densecol               If positive, minimum nonzeros in a column for
                       the barrier algorithm to consider the column dense.
                       If 0 (default), this tolerance is selected
                       automatically.

dependency             Whether to use CPLEX's presolve dependency checker:
                         -1 = automatic choice (default)
                          0 = no
                          1 = turn on only at start of preprocessing
                          2 = turn on only at end of preprocessing
                          3 = turn on at both start and end of
                              preprocessing.

dettimelim             Time limit in platform-dependent "ticks".
                       Default = 1e75.  See timing.

dgradient              Pricing algorithm for dual simplex (default 0):
                          0 = choose automatically
                          1 = standard dual pricing
                          2 = steepest-edge pricing
                          3 = steepest-edge pricing in slack space
                          4 = steepest-edge with unit initial norms
                          5 = devex pricing.

disjcuts               Whether to generate MIP disjunctive cuts:
                          -1 = no
                          0 = automatic choice (default)
                          1, 2, 3 = ever more aggressive generation.

display                Frequency of displaying LP progress information:
                          0 (default) = never
                          1 = each factorization
                          2 = each iteration.

doperturb              1 means initially perturb the problem (by an
                       amount governed by "perturbation", which is
                       described below).  0 (default) means let the
                       algorithm decide.  Setting doperturb to 1
                       is occasionally helpful for highly degenerate
                       problems.

dparam                 Used with syntax "dparam=n=d" (no spaces), where n
                       is a decimal integer, the number of a CPLEX "double"
                       (i.e., floating-point valued) parameter.  If d is a
                       decimal floating-point value, assign d to "double"
                       parameter n.  If d is ?, report the current value of
                       "double" parameter n.  This facility provides a way
                       to modify "double" parameters that have not (yet)
                       been assigned a keyword.

droptol                If droptol > 0 is specified, linear constraint
                       and objective coefficients less than droptol in
                       magnitude are treated as zero.

dual                   Single-word phrase:  solve the dual problem.

dualopt                Single-word phrase:  use a dual simplex algorithm.

dualratio              If neither "primal" nor "dual" was specified and
                       "dual" is possible (e.g., no integer variables and
                       no node and arc declarations), choose between
                       "primal" and "dual" as follows.
                       Let m = number of rows, n = number of columns;
                       if m - n > dualthresh > 0 or m > dualratio*n,
                       solve the dual; otherwise solve the primal.
                       Defaults:  dualthresh = 0, dualratio = 3.

dualthresh             See dualratio.

eachcutlim             Limit on the number of cuts of each time.
                       Default = 2100000000.

endbasis               "endbasis foo" writes the final basis to
                       file "foo" (in BAS format).

endsol                 File for writing the final solution as an XML file.

feasibility            Amount by which basic variables can violate
                       their bounds.  Default = 1e-6; possible
                       values are between 1e-9 and 0.1.

feasopt                For infeasible problems, whether to find a feasible
                       point for a relaxed problem (see feasoptobj):
                          0 = no (default)
                          1 = find a relaxed feasible point
                          2 = find a "best" solution among the relaxed
                              feasible points.

feasoptobj             Objective for "feasopt":
                          1 = minimize the sum of constraint and variable
                              bound relaxations (default)
                          2 = minimize the number of constraint and variable
                              bounds relaxed (a MIP problem, generally
                              harder than feasoptobj = 1)
                          3 = minimize the sum of squares of constraint and
                              variable bound relaxations.

file                   Synonym for "writeprob".

finalmipalg            Specify the algorithm to solve the final LP
                       obtained by fixing all integer variables at
                       their integer values:
                          0 = automatic (default)
                          1 = primal simplex
                          2 = dual simplex
                          3 = network simplex
                          4 = barrier
                          5 = sifting (not applicable to QP)
                          6 = concurrent optimizer.

flowcuts               Whether to use flow cuts in solving MIPs:
                          -1 = never
                          0 = automatic choice (default)
                          1, 2 = ever more aggressive use.

flowpathcuts           Whether to generate MIP flow-path cuts:
                          -1 = no
                          0 = automatic choice (default)
                          1, 2 = ever more aggressive generation.

fpheur                 Whether to use the feasibility pump heuristic on MIP
                       problems:
                          -1 = no
                           0 = automatic choice (default)
                           1 = yes, focus on finding a feasible solution
                           2 = yes, focus on finding a good objective
                       value at a feasible solution.

fraccand               Limit on number of candidate variables when
                       generating Gomory cuts for MIP problems:
                       default = 200.

fraccuts               Whether to generate MIP fractional Gomory
                       cuts:
                          -1 = no
                           0 = decide automatically (default)
                           1 = generate moderately
                           2 = generate aggressively.

fracpass               Limit on number of passes to generate MIP
                       fractional Gomory cuts:
                          0 = automatic choice (default)
                          positive = at most that many passes.

fractionalcuts         Synonym for "fracpass".

growth                 Synonym for "bargrowth".

gubcuts                Whether to use GUB cuts in solving MIPs:
                          -1 = never
                          0 = automatic choice (default)
                          1, 2 = ever more aggressive generation.

heureffort             Whether to increase ( > 1) or decrease ( < 1) efforts
                       spent on heuristics during MIP solvers;
                       heureffort = 0 ==> suppress all MIP heuristics.

heurfreq               How often to apply "node heuristics" for MIPS:
                          -1 = never
                          0 = automatic choice (default)
                          n > 0 = every n nodes.

heuristicfreq          Synonym for "heurfreq".

iisfind                Whether to find and return an IIS (irreducible
                       infeasible set of variables and constraints) if
                       the problem is infeasible:
                       0 = no (default)
                       1 = find an IIS.
                       IIS details are returned in suffix .iis, which
                       assumes one of the values "non" for variables
                       and constraints not in the IIS; "low" for
                       variables or inequality constraint bodies whose lower
                       bounds are in the IIS; "upp" for variables and
                       inequality constraint bodies whose upper bounds are
                       in the IIS; and "fix" for equality constraints that
                       are in the IIS.

impliedcuts            Whether to use implied cuts in solving MIPs:
                          -1 = never
                           0 = automatic choice (default)
                           1, 2 = ever more aggressive use.

incompat               How to treat parameter settings that CPLEX finds
                       incompatible:
                          0 = quietly ignore incompatibilities
                          1 = report and ignore them (default)
                          2 = reject them, refusing to solve.
                       For example, CPLEX regards the polishafter_* parameters
                       introduced in CPLEX 11.2 as incompatible with the older
                       polishtime parameter.

integrality            Amount by which an integer variable can differ
                       from the nearest integer and still be considered
                       feasible.  Default = 1e-5; must be in [1e-9, 0.5].
                       (The upper bound was not enforced prior to CPLEX 11.)

intwarntol             Do not warn about perturbations to "integer"
                       variables to make them integers when the maximum
                       perturbation is at most intwarntol (default 1e-9);
                       see "round".

iparam                 Used with syntax "iparam=n=i" (no spaces), where n
                       is a decimal integer, the number of a CPLEX integer
                       parameter.  If i is a decimal integer, assign i to
                       integer parameter n.  If i is ?, report the current
                       value of integer parameter n.  This facility provides
                       a way to modify integer parameters that have not (yet)
                       been assigned a keyword.

iterations             Limit on total LP iterations; default 2^31 - 1.

iterlim                Synonym for "iterations".

lazy                   Whether to recognize suffix .lazy on constraints
                       (new for CPLEX 10): sum of
                          1 ==> treat .lazy = 1 as lazy constraint
                          2 ==> treat .lazy = 2 as user cut
                       Default lazy = 3 ==> treat both.  (Suffix .lazy on
                       constraints is ignored if not 0, 1, or 2 modulo 3.)

lbheur                 Whether to use a local branching heuristic in an
                       attempt to improve new incumbents found during a
                       MIP search.  (Default = 0 = no; 1 = yes.)

limitperturb           Synonym for "perturblimit".

localimpliedcuts       Whether to generate locally valid implied bound
                       cuts for MIP problems:
                          -1 ==> no
                           0 ==> automatic choice (default)
                           1 ==> yes, moderately
                           2 ==> yes, aggressively
                           3 ==> yes, very aggressively.

logfile                Name of file to receive all CPLEX messages.

lowercutoff            For maximization problems involving integer
                       variables, skip any branch whose LP relaxation's
                       optimal value is less than lowercutoff.  Warning:
                       if lowercutoff is too large, the problem will
                       appear infeasible.  Default = -1e75.

lowerobj               Stop minimizing when the objective value
                       goes below lowerobj.  Default = -1e75.

lowerobjlim            Synonym for "lowerobj".

lpdisplay              Synonym for "display".

lpiterlim              Synonym for "iterations".

lptimelim              Synonym for "time".

markowitz              Pivot tolerance; default = 0.01; must be between
                       0.0001 and 0.99999.  Bigger values may improve
                       numerical properties of the solution (and may
                       take more time).

maximize               Single-word phrase:  maximize the objective,
                       regardless of model specifications.

mcfcuts                Whether to use multi-commodity flow (MCF) cuts:
                          -1 = no
                           0 = let CPLEX decide (default)
                           1 = generate a modest number of MCS cuts
                           2 = generate MCS cuts aggressively.

memoryemphasis         Whether to compress data to reduce the memory used,
                       which may make some information (e.g., basis condition)
                       unavailable:
                          0 = no (default)
                          1 = yes.

minimize               Single-word phrase:  minimize the objective,
                       regardless of model specifications.

mipalg                 Algorithm used on mixed-integer subproblems:
                          0 = automatic choice (default)
                          1 = primal simplex
                          2 = dual simplex
                          3 = network simplex
                          4 = barrier
                          5 = sifting.
                       For MIQP problems (quadratic objective, linear
                       constraints), settings other than 3 and 5 are treated
                       as 0.  For MIQCP problems (quadratic objective and
                       constraints), all settings are treated as 4.

mipalgorithm           Synonym for "mipalg".

mipbasis               Whether to compute a basis and dual variables for MIP
                       problems when endbasis is not specified:
                         -1 = default (described below)
                          0 = no
                          1 = yes
                       This keyword is new with driver version 20040716.
                       When endbasis is specified, mipbasis=1 is assumed.
                       Otherwise, when mipbasis=0 is specified for a MIP
                       problem, no solver-status values for variables are
                       returned to AMPL.  The default is to assume 1 unless
                       a quadratic objective or constraint is present, in
                       which case qcdual is assumed if quadratic constraints
                       are present and 0 is assumed otherwise (as finding a
                       basis can be time consuming).

mipcrossover           Crossover method used when using the barrier
                       method for MIP subproblems:
                          -1 = no crossover
                           0 (default) = automatic choice
                           1 = primal
                           2 = dual.

mipcuts                Sets all ten of cliques, covers, disjcuts,
                       flowcuts, flowpathcuts, fraccuts, gubcuts,
                       impliedcuts, mircuts and zerohalfcuts to the
                       specified value.

mipdisplay             Frequency of displaying branch-and-bound
                       information (for optimizing integer variables):
                          0 (default) = never
                          1 = each integer feasible solution
                          2 = every "mipinterval" nodes
                          3 = every "mipinterval" nodes plus
                              information on LP relaxations
                              (as controlled by "display")
                          4 = same as 2, plus LP relaxation info
                          5 = same as 2, plus LP subproblem info.

mipemphasis            How to balance seeking seeking
                       feasibility versus optimality when solving a MIP:
                         0 = balance optimality and feasibility (default)
                         1 = emphasize feasibility over optimality
                         2 = emphasize optimality over feasibility
                         3 = emphasize moving the best bound
                         4 = emphasize finding hidden feasible solutions
                         5 = emphasize finding good feasible solutions sooner.

mipgap                 Relative tolerance for optimizing integer
                       variables: stop if
                          abs((best bound) - (best integer))
                              < mipgap * (1 + abs(best bound)).
                       Default = 1e-4; must be between 1e-9 and 1.

mipinterval            Frequency of node logging for mipdisplay >= 2.
                       Default = 0 ==> automatic choice.  Values n > 0 ==>
                       every n nodes and every new incumbent; n < 0 ==> less
                       frequently the more negative n is.

mipkappa               For MIP problems, whether to compute the "MIP kappa",
                       which summarizes the condition numbers of the optimal
                       bases seen while solving the problem:
                        -1 = no
                         0 = automatic choice (default)
                         1 = compute for a sample of subproblems
                         2 = compute for all subproblems (possibly expensive).

mipordertype           Synonym for "ordertype".

mipsearch              Search strategy for mixed-integer problems, new
                       in CPLEX 11:
                          0 = automatic choice (default)
                          1 = traditional branch and cut
                          2 = dynamic search.

mipsolutions           Stop branch-and-bound for integer variables
                       after finding "mipsolutions" feasible solutions.
                       Default = 2^31 - 1.

mipstart               Synonym for "mipstartvalue".

mipstartalg            For problems with integer variables, which algorithm
                       to use in solving the initial MIP subproblem:
                          0 = automatic choice (default)
                          1 = primal simplex
                          2 = dual simplex
                          3 = network simplex
                          4 = barrier
                          5 = sifting
                          6 = concurrent (several at once, if possible).
                       For MIQP problems (quadratic objective, linear
                       constraints), setting 5 is treated as 0 and 6 as 4.
                       For MIQCP problems (quadratic objective & constraints),
                       all settings are treated as 4.

mipstartstatus         Whether to use incoming variable and constraint
                       statuses if the problem has integer variables:
                          0 = no
                          1 = yes (default).

mipstartvalue          Whether to use initial guesses in problems with
                       integer variables:
                          0 = no.
                          1 = yes (default), automatic choice of algorithm.
                          2 = withdrawn and now treated as 0.
                          3 = effort level = CPX_MIPSTART_CHECKFEAS, which
                        fails if the starting point is infeasiable.
                          4 = effort level = CPX_MIPSTART_SOLVEFIXED, which
                        solves the fixed problem specified by the starting
                        guess.
                          5 = effort level = CPX_MIPSTART_SOLVEMIP, which
                        causes a subMIP problem to be solved; "submipnodelim"
                        limits the number of nodes explored.
                          6 = effort level = CPX_MIPSTART_REPAIR, which causes
                        an attempt to repair an infeasible starting guess;
                        "repairtries" tells how often to attempt a repair, and
                        "submipnodelim" limits the number of nodes explored.
                          7 = effort level = CPX_MIPSTART_NOCHECK, under which
                        the starting guess is simply assumed to be feasiable.

mipsubalg              Synonym for "mipalg".

miqcpstrat             Strategy for solving quadratically-constrained MIPs
                       (MIQCP problems):
                          0 = automatic choice (default)
                          1 = solve a quadratically-constrained node
                              relaxation (QCP) at each node
                          2 = solve an LP node relaxation at each node.

mircuts                Whether to generate MIP rounding cuts:
                          -1 = no
                           0 = automatic choice (default)
                           1 = moderate generation
                           2 = aggressive generation.

modisplay              how much to report during multiobjective optimization:
                        0 = nothing
                        1 = summary after each subproblem (default)
                        2 = subproblem logs as well as summaries.

multiobj               whether to do multi-objective optimization:
                        0 = no (default)
                        1 = yes
                       When multiobj = 1 and several linear objectives are
                       present, suffixes .objpriority, .objweight, .objreltol,
                       and .objabstol on the objectives are relevant.
                       Objectives with greater (integer) .objpriority values
                       have higher priority.  Objectives with the same
                       .objpriority are weighted by .objweight.  Objectives
                       with positive .objabstol or .objreltol are allowed to
                       be degraded by lower priority objectives by amounts not
                       exceeding the .objabstol (absolute) and .objreltol
                       (relative) limits.  The objective must all be linear.
                       Objective-specific values may be assigned via keywords
                       of the form obj_n_name, such as obj_1_pricing to
                       specify "pricing" for the first objective.  If no
                       .objweight values are provided, 1. is assumed for all.
                       Similarly, if no .objpriority values are given, 1 is
                       assumed for all.  For .objreltol and .objabstol, if
                       no values are given, all are assumed to be 0.

nameround              Whether to mangle variable and constraint names
                       by turning [ and ] into ( and ), respectively:
                          0 = no (default)
                          1 = yes.
                       This only matters if you specify endbasis=...
                       or startbasis=... or perhaps writeprob=something.lp
                       and have instructed AMPL to write .row and .col files.
                       (It is usually better to let AMPL's status facilities
                       convey basis information.)  An alternative under Unix
                       is to use the "tr" command to make the above changes
                       if they are needed.

netdisplay             Which objective value to show when using the
                       network simplex algorithm with display > 0
                       or netopt=3:
                          0 = none
                          1 = true objective
                          2 = penalized objective (default).

netfeasibility         Feasibility tolerance for the network simplex
                       algorithm.  Default = 1e-6; possible values are
                       between 1e-11 and 1e-1.

netfind                Algorithm for finding embedded networks:
                          1 = extract only the natural network
                          2 = use reflection scaling (default)
                          3 = use general scaling.

netfinder              Synonym for "netfind".

netiterations          Limit on network simplex iterations.
                       Default = large (e.g., 2^31 - 1).

netopt                 0 means never invoke the network optimizer.
                       1 (default) means invoke the network optimizer
                         only if the model had node and arc declarations.
                       2 means always invoke the network optimizer
                         (unless there are integer variables); the network
                         optimizer may be able to find and exploit an
                         embedded network.
                       3 is similar to 2, but sets CPLEX's LPMethod
                         to CPX_ALG_NET rather than explicitly invoking
                         the network optimizer.  This might make a
                         difference if CPLEX's presolve makes relevant
                         reductions.

netoptimality          Tolerance for optimality of reduced costs in the
                       network simplex algorithm.  Default 1e-6; must be
                       between 1e-11 and 1e-1.

netpricing             How to price in the network simplex algorithm:
                          0 = automatic choice (default)
                          1 = partial pricing
                          2 = multiple partial pricing
                          3 = multiple partial pricing with sorting.

node                   Synonym for "nodes".

nodecuts               Decides whether or not cutting planes are separated
                       at the nodes of the branch-and-bound tree:
                           -1 = do not generate node cuts
                            0 = automatic (default)
                            1 = generate moderately
                            2 = generate aggressively
                            3 = genertate very aggresively.

nodefile               Whether to save node information in a temporary file:
                          0 = no
                          1 (default) = compressed node file in memory
                          2 = node file on disk
                          3 = compressed node file on disk.

nodefiledir            Synonym for workfiledir.  Prior to CPLEX 7.1,
                       this directory is just for node information files.

nodelim                Synonym for "nodes".

nodes                  Stop branch-and-bound for integer variables
                       after "nodes" LP relaxations.  Default = 2^31 - 1;
                       nodes = 0 ==> complete processing at the root (create
                       cuts, apply heuristics at root);
                       1 ==> allow branching from root:  create but do not
                       solve nodes.

nodesel                Strategy for choosing next node while optimizing
                       integer variables:
                          0 = depth-first search;
                          1 = breadth-first search (default);
                          2 = best-estimate search;
                          3 = alternate best-estimate search.

nodeselect             Synonym for "nodesel".

nosolve                Stop after loading the problem and honoring any
                       "writeprob" or "writemipstart" directives.

numericalemphasis      Whether to try to improve numerical accuracy (at a
                       possible cost of time or memory):
                          0 = no (default)
                          1 = yes.

objdifference          Amount added to (for maximizing) or subtracted
                       from (for minimizing) the best (so far) feasible
                       objective value while optimizing integer variables.
                       Subsequent nodes will be ignored if their LP
                       relaxations have optimal values worse than this
                       sum.  Default = 0.  Positive values may speed
                       the search -- and may cause the optimal solution
                       to be missed.

objno                  1 (default) = first objective, 2 = second, etc.;
                       0 ==> no objective:  just find a feasible point.

objrep                 Whether to replace
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
                       For maximization problems, ">= f(x)" is changed to
                       "<= f(x)" in the description above.  This is new
                       with driver version 20130622.

optimality             Tolerance for optimality of reduced costs.
                       Default 1e-6; must be between 1e-9 and 1e-1.

optimize               Synonym for "primal".

ordering               Ordering algorithm used by the barrier algorithm
                          0 = automatic choice (default)
                          1 = approximate minimum degree
                          2 = approximate minimum fill
                          3 = nested dissection.

ordertype              How to generate default priorities for integer
                       variables when no .priority suffix is specified:
                          0 = do not generate priorities (default)
                          1 = use decreasing costs
                          2 = use increasing bound range
                          3 = use coefficient count.

outlev                 Synonym for "display".

parallelmode           Parallel optimization mode:
                          -1 = opportunistic mode
                           0 = automatic: let CPLEX decide (default)
                           1 = deterministic mode.

paramfile              File containing param settings to import.  The file
                       is read and settings in it echoed when the keyword
                       is processed.

paramfileprm           File containing param settings in CPLEX PRM format
                       to import.  The file is read without echoing settings
                       in it when the keyword is processed.

perturb                Synonym for "doperturb".

perturbation           Amount by which to perturb variable bounds
                       when perturbing problems (see "doperturb").
                       Default 1e-6; must be positive.

perturbconst           Synonym for "perturbation".

perturblim             Number of stalled simplex iterations before the
                       problem is perturbed.  Default = 0 = automatic.

perturblimit           Synonym for "perturblim".

pgradient              Pricing algorithm for primal simplex (default 0):
                          -1 = reduced-cost pricing
                           0 = hybrid reduced-cost and Devex pricing
                           1 = Devex pricing
                           2 = steepest-edge pricing
                           3 = steepest-edge with slack initial norms
                           4 = full pricing.

plconpri               Priority (default 1) for SOS2 constraints for nonconvex
                       piecewise-linear terms in constraints.

plobjpri               Priority (default 2) for SOS2 constraints for nonconvex
                       piecewise-linear terms in objectives.

polishafter_absmipgap  Start polishing integer solutions after the
                       absolute mixed-integer optimality gap is at most
                       polishafter_absmipgap.  Default 1e-6.

polishafter_intsol     Start polishing integer solutions after the
                       finding polishafter_intsol integer-feasible
                       solutions.  Default 2^31 - 1.

polishafter_mipgap     Start polishing integer solutions after the
                       relative mixed-integer optimality gap is at most
                       polishafter_mipgap.  Default 0.

polishafter_nodes      Start polishing integer solutions after the
                       processing polishafter_nodes nodes.
                       Default 2^31 - 1.

polishafter_time       Start polishing integer solutions after finding
                       at least one integer feasible solution and spending
                       polishafter_time CPU seconds seeking integer
                       solutions.  Default 1e75.

polishafter_timedet    Start polishing integer solutions after finding
                       at least one integer feasible solution and spending
                       polishafter_time "ticks" seeking integer solutions.
                       Default 1e75.

poolagap               Solutions with objective worse in absolute value by
                       poolgap than the best solution are not kept in the
                       solution pool; see poolstub.  Default 1e75.

poolcapacity           Number of solutions to keep in solution pool;
                       see poolstub.  Default 2100000000.

pooldual               Whether to return dual values (corresponding to fixed
                       integer variables) for MIP and MIQP problems in the
                       solution pool:
                          0 = no (default)
                          1 = yes (which takes extra computation)

poolgap                Solutions  with objective worse in a relative sense by
                       poolgap than the best solution are not kept in the
                       solution pool; see poolstub.  Default 1e75.

poolintensity          How hard to try adding MIP solutions to the solution
                       pool.  Useful only if poolstub is specified.  Default 0
                       is treated as 1 if poolstub is specified without
                       populate, or 2 if populate is specified.  Larger values
                       (3 or 4) cause more additions to the solution pool,
                       possibly consuming considerable time; poolintensity 4
                       tries to generate all MIP solutions, which could be a
                       very large number.

poolreplace            Policy for replacing solutions in the solution pool if
                       more than poolcapacity solutions are generated:
                          0 = FIFO (first-in, first-out); default
                          1 = Keep best solutions
                          2 = Keep most diverse solutions.

poolstub               Stub for solution files in the MIP solution pool.
                       New in CPLEX 11 and meaningful only if some variables
                       are integer or binary.  A pool of alternate MIP
                       solutions is computed if poolstub is specified, and the
                       solutions that remain in the solution pool (after some
                       are replaced if more than poolcapacity solutions are
                       found) are written to files
                         (poolstub & '1') ... (poolstub & |solution pool|),
                       where |solution pool| is the number of solutions in the
                       solution pool.  That is, file names are obtained by
                       appending 1, 2, ... |solution pool| to poolstub.  The
                       value of |solution pool| is returned in suffix npool
                       on the objective and problem.

populate               Whether to run CPLEX's "populate" algorithm in an
                       attempt to add more solutions to the MIP solution pool.
                          0 = no; just keep solutions found during the
                              initial solve
                          1 = run "populate" after finding a MIP solution
                          2 = run "populate" instead of seeking a single
                              best solution.
                       See poolstub.

populatelim            Limit on number of solutions added to the solution pool
                       by the populate algorithm.  See poolstub and populate.
                       Default 20.

predual                Whether CPLEX's presolve phase should present the
                       CPLEX solution algorithm with the primal (-1) or
                       dual (1) problem or (default = 0) should decide
                       which automatically.  Specifying "predual=1" often
                       gives better performance than specifying just "dual",
                       but sometimes "dual predual=1" is still better.

prelinear              Whether CPLEX's presolve should do full reductions
                       or only linear ones.  Default = 1 = full.

prepass                Limit on number of CPLEX presolve passes.
                       Default = -1 = decide limit automatically.

prereduce              Kinds of reductions permitted during CPLEX presolve:
                          0 = none
                          1 = only primal
                          2 = only dual
                          3 = both primal and dual (default).

prereformulations      Reformulations applied during CPLEX presolve:
                          0 = none
                          1 = allow reformulations that interphere with
                              crushing forms
                          2 = allow reformulations that interphere with
                              uncrushing forms
                          3 = all reformulations (default).

prerelax               Whether to use CPLEX's presolve on the initial LP
                       relaxation of a MIP:
                          -1 = automatic choice (default)
                           0 = no
                           1 = yes.

presolve               0 or 1 (default 1): Whether to run CPLEX's presolve
                       algorithm.

presolvedual           Synonym for "predual".

presolvenode           -1, 0, or 1 (default 0): Whether to run CPLEX's
                       presolve at each node of the MIP branch-and-bound
                       tree: -1 = no; 1 = yes; 0 = automatic choice.

presos1reform          Control the reformulation of SOS of type 1:
                         -1 = no reformulation
                          0 = automatic (default)
                          1 = reformulate as linear constraints, with a
                              reformulation which is logarithmic in the
                              size of the SOSs.

presos2reform          Control the reformulation of SOS of type 2:
                         -1 = no reformulation
                          0 = automatic (default)
                          1 = reformulate as linear constraints, with a
                              reformulation which is logarithmic in the
                              size of the SOSs.

prestats               0 or 1 (default 0):  Whether to include summary
                       statistics (if nonzero) for CPLEX's "aggregate" and
                       "presolve" algorithms in the solve_message.

pretunefile            File to which nondefault keyword settings are written
                       before tuning; written whether or not tunefile or
                       tunefilecpx is specified.

pretunefileprm         File to which nondefault keyword settings are written
                       in CPLEX PRM format before tuning; written whether or
                       not tunefile or tunefileprm is specified.  Includes
                       some display settings suppressed by pretunefile.

pricing                Size of pricing candidate list (for partial pricing).
                       0 (default) means the algorithm decides.

primal                 Single-word phrase:  solve the primal problem.

primalopt              Use the primal simplex algorithm.

priorities             Whether to consider priorities for MIP branching:
                       0 = no
                       1 = yes (default).

probe                  Whether to do variable probing when solving MIPs
                       (which sometimes dramatically affects performance,
                       for better or worse):
                          -1 = no
                           0 = automatic choice (default)
                           1, 2, or 3 = ever more probing.

probetime              Limit in seconds on time spent probing.
                       Default = 1e75.

probetimedet           Limit in "ticks" on time spent probing.
                       Default = 1e75.

qcdmax                 Limit on k*n*n for computing duals for quadratically
                       constrained problems, where k = number of quadratic
                       constraints and n = number of variables. Default = 1e9.

qcdual                 Whether to compute dual variable values for problems
                       with quadratic constraints.  Default = 1 (for "yes").
                       This may be expensive if there are many quadratic
                       constraints.  Specifying qcdual=0 suppresses the
                       computation.

qcpconvergetol         Convergence tolerance on relative complementarity for
                       problems with quadratic constraints.  Default = 1e-7.

qctol1                 Tolerance on a quadratic inequality constraint's slack.
                       After CPLEX has returned a solution, dual values are
                       deduced for "active" quadratic constraints.
                       Default 1e-5; a negative value is quietly treated as 0.

qctol2                 Tolerance on the maxnorm of the gradient of an
                       "active" quadratic constraint (see qctol1):  if the
                       maxnorm is no more than qctol2, the gradient is
                       considered to vanish and dual value 0 is deduced.
                       Default 1e-5; a negative value is quietly treated as 0.

qctol3                 Tolerance on the reduction during QR factorization of
                       the maxnorm of an "active" constraint's gradient
                       (see qctol1) for the constraint to be considered
                       independent of the other active quadratic constraints.
                       Dual value 0 is deduced for dependent constraints.
                       Default 1e-5; a negative value is quietly treated as 0.

qpmethod               Choice of algorithm for a continuous quadratic
                       programming problem:
                          0 = automatic choice (default)
                          1 = primal simplex
                          2 = dual simplex
                          3 = network simplex
                          4 = barrier algorithm
                          6 = concurrent optimizer.

qtolin                 Whether to to linearize products of bounded variables
                        in quadratic objectives:
                          -1 = automatic choice (default)
                           0 = no
                           1 = yes.

rays                   Whether to return suffix .unbdd when the objective is
                       unbounded or suffix .dunbdd when the constraints are
                       infeasible:
                          0 = neither
                          1 = just .unbdd
                          2 = just .dunbdd
                          3 = both (default)
                       To get .dunbdd, you may need to specify presolve=0
                       in $cplex_options.

readbasis              BAS file containing starting basis.

readsol                File (previously written by an endsol directive) for
                       reading the starting point.  This is for debugging
                       and is normally not used.

readvector             VEC file containing starting point for barrier alg.
                       Deprecated; use "readsol" instead.

record                 Whether to record CPLEX library calls for debugging use
                       by IBM in a file with an automatically chosen name of
                       the form cplexXXXXXXX.db:
                        0 = no (default)
                        1 = yes.

refactor               LP iterations between refactorizing the basis.
                       0 (default) means the algorithm decides.

relax                  Single-word phrase:  ignore integrality.

relaxpresolve          Synonym for "prerelax".

relobjdif              Synonym for "relobjdiff".

relobjdiff             If the objdifference parameter is 0,
                       relobjdiff times the absolute value of the objective
                       value is added to (for maximizing) or subtracted
                       from (for minimizing) the best (so far) feasible
                       objective value while optimizing integer variables.
                       Subsequent nodes will be ignored if their LP
                       relaxations have optimal values worse than this
                       sum.  Default = 0.  Positive values may speed
                       the search -- and may cause the optimal solution
                       to be missed.

relpresolve            Synonym for "prerelax".

repairtries            How many times to try to repair in infeasible
                       MIP starting guess:
                          -1 = none
                           0 = automatic choice (default)
                           > 0 = that many times.

repeatpresolve         Whether to repeat CPLEX's presolve at MIP nodes:
                          -1 = automatic choice (default)
                           0 = no
                           1 = presolve again ignoring cuts
                           2 = presolve again considering cuts
                           3 = presolve again considering cuts and
                               allowing new root cuts.

reqconvex              Whether to require a quadratic model to be convex:
                          0 = automatic choice (default)
                          1 = require convexity
                          2 = do not require convexity; just look
                              for a local solution
                          3 = globally solve if noncovex.

resolve                Whether to re-solve the problem with CPLEX's
                       presolve turned off when it reports the problem
                       to be infeasible or unbounded.  Re-solving may
                       take extra time but should determine whether the
                       problem is infeasible or unbounded.
                          0 = no
                          1 = yes (default).

return_mipgap          Whether to return mipgap suffixes or include
                       mipgap values in the solve_message:  sum of

                          1 = return relmipgap suffix
                          2 = return absmipgap suffix
                          4 = suppress mipgap values in solve_message

                       The suffixes are on the objective and problem;
                       returned suffix values are +Infinity if no integer-
                       feasible solution has been found, in which case no
                       mipgap values are reported in the solve_message.
                       Default = 0.  See also bestbound and bestnode above.

rinsheur               Relaxation INduced neighborhood Search HEURistic
                       for MIP problems:
                          -1 = none
                           0 = automatic choice of interval (default)
                           n (for n > 0) = every n nodes.

rltcuts                Whether to use RLT (Reformulation Linearization
                       Technique) cuts:
                          -1 = no
                           0 = automatic choice (default)
                           1 = generate RLT cuts moderately
                           2 = generate RLT cuts aggressively
                           3 = generate RLT cuts very aggressively

round                  Whether to round integer variables to integral
                       values before returning the solution, and whether
                       to report that CPLEX returned noninteger values
                       for integer values (default 1):  sum of
                          1 ==> round nonintegral integer variables
                          2 ==> do not modify solve_result
                          4 ==> do not modify solve_message
                          8 ==> modify solve_result and solve_message
                       even if maxerr < intwarntol (default 1e-9).
                       Modifications take place only if CPLEX assigned
                       nonintegral values to one or more integer variables.

scale                  How to scale the problem:
                          -1 = no scaling
                           0 (default) = equilibration
                           1 = a more aggressive scheme that sometimes helps.

seed                   Seed for random number generator used internally
                       by CPLEX.  Use "seed=?" to see the default, which
                       depends on the CPLEX release.

sensitivity            Single-word phrase:  return sensitivity information for
                       the objective (in suffixes .up for the largest value
                       of a variable's cost coefficient or constraint's
                       right-hand side before the optimal basis changes,
                       .down for the smallest such value, and .current for
                       the current cost coefficient or right-hand side).

siftingopt             Synonym for "siftopt".

siftopt                Single-word phrase:  on LPs with CPLEX versions >= 8,
                       solve ever larger sequences of subproblems until the
                       whole LP is solved.

simplexsifting         Whether to allow the simplex algorithm to use sifting
                       when appropriate:
                          0 = no
                          1 = yes (default).

singular               Maximum number of times CPLEX should try to
                       repair the basis when it encounters singularities.
                       Default = 10.

singularlim            Synonym for "singular".

solutionlim            Synonym for "mipsolutions".

solutiontype           Whether to seek a basic solution when solving an LP:
                          0 = automatic choice (default)
                          1 = yes
                          2 = no (just seek a primal-dual pair).

sos                    0 or 1 (default 1):  Whether to honor declared
                       suffixes .sosno and .ref describing SOS sets.
                       Each distinct nonzero .sosno value designates an SOS
                       set, of type 1 for positive .sosno values and of type
                       2 for negative values.  The .ref suffix contains
                       corresponding reference values.

sos2                   0 or 1 (default 1): Whether to tell CPLEX about SOS2
                       constraints for nonconvex piecewise-linear terms.

sparam                 Used with syntax "sparam=n=str" (no spaces), where n
                       is a decimal integer, the number of a CPLEX string
                       parameter.  If str is ?, report the current value of
                       string parameter n.  Otherwise, if str is a quoted
                       string or a sequence of nonblank characters, assign
                       str to string parameter n.  This facility provides a
                       way to modify string parameters that have not (yet)
                       been assigned a keyword.

splitcuts              Whether to use lift-and-project cuts on MIP problems
                       (new for CPLEX 12.5.1):
                          -1 = no
                           0 = automatic choice (default)
                           1 = moderate use
                           2 = aggressive use
                           3 = very aggressive use.

startalg               Synonym for "mipstartalg".

startalgorithm         Synonym for "mipstartalg".

startbasis             "startbasis foo" reads the initial basis
                       (in BAS format) from file "foo".

startsol               Synonym for "readsol".

startvector            Synonym for "readvector".

strongcand             Length of the candidate list for "strong branching"
                       when solving MIPs: default 10.

strongit               Number of simplex iterations on each variable in
                       the candidate list during strong branching.
                       Default = 0 = automatic choice.

subalg                 Synonym for "mipalg".

subalgorithm           Synonym for "mipalg".

submipalg              Choice of algorithm used to solve the subproblems
                       of a subMIP: not a subproblem, but an auxiliary MIP
                       that CPLEX sometimes forms and solves, e.g., when
                        * dealing with a partial MIP start
                        * repairing an infeasible MIP start
                        * using the RINS heuristic
                        * branching locally
                        * polishing a solution.
                       Possible values (when appropriate):
                        0 = automatic choice (default)
                        1 = primal simplex
                        2 = dual simplex
                        3 = network simplex (not for MIQPs)
                        4 = barrier
                        5 = sifting (0 is used for MIQPs).
                       Only 0 is allowed for MIQCPs.

submipnodelim          Limit on nodes searched by relaxation induced
                       neighborhood search (RINS) heuristic for MIP
                       problems and for processing of MIP starting values.
                       Default = 500.

submipscale            Rarely used choice of scaling for auxiliary subMIPs
                       (described with "submipalg"):
                        -1 = no scaling
                         0 = equilibration scaling (default)
                         1 = more aggressive scaling.

submipstartalg         Rarely used choice of algorithm for the initial
                       relaxation of a subMIP (described with "submipalg"):
                        0 = automatic choice (default)
                        1 = primal simplex
                        2 = dual simplex
                        3 = network simplex
                        4 = barrier
                        5 = sifting (0 is used for MIQPs)
                        6 = concurrent (dual, barrier and primal in
                                opportunistic mode; dual and barrier in
                                deterministic mode; 4 is used for MIPQs).
                       Only 0 is allowed for MIQCPs.

symmetry               Whether to break symmetry during
                           preprocessing of MIP problems:
                          -1 = automatic choice (default)
                           0 = no
                           1 = moderate effort
                           2 = more effort
                           3 = still more effort
                           4 = even more effort (new in CPLEX 11)
                           5 = more effort than 4 (new in CPLEX 11).

threads                Default maximum number of threads for any of
                       the parallel CPLEX optimizers (limited also
                       by licensing).  Default = 1 prior to CPLEX 11,
                       or 0 (use maximum threads available) starting
                       with CPLEX 11.  May be overridden, prior to
                       CPLEX 11, by more specific limits, such as
                       barthreads or mipthreads.

time                   Time limit in seconds; default = 1e75.

timelimit              Synonym for "time".

timing                 Whether to write times in seconds or "ticks" to
                       stdout or stderr: sum of
                           1 = write time in seconds to stdout
                           2 = write time in seconds to stderr
                           4 = write time in "ticks" to stdout
                           8 = write time in "ticks" to stderr
                          16 = write number of logical cores to stdout
                          32 = write number of logical cores to stderr.
                       Default = 0.

tranopt                Synonym for "dualopt".

treelimit              Synonym for "treememory".

treememlim             Synonym for "treememory".

treememory             Max. megabytes of memory (default 1e75) to use for
                       branch-and-bound tree.

tunedisplay            How much to print during tuning:
                          0 = nothing
                          1 = minimal printing (default)
                          2 = show parameters being tried
                          3 = exhaustive printing.

tunefile               Name of file for tuning results.  If specified, CPLEX
                       will experiment with parameter settings that would
                       make the solution faster.  This can significantly
                       increase execution time of the current invocation, but
                       the settings it finds might save time in future runs.

tunefileprm            Name of file for tuning results in CPLEX PRM format.
                       If specified, CPLEX will experiment with parameter
                       settings as described for "tunefile".

tunefix                List of keywords not to tune, enclosed in quotes
                       (" or ') or separated by commas without white space
                       if more than one.

tunefixfile            Name of file containing keywords not to tune.
                       (There is no PRM format alternative.)  Merged with
                       tunefix specification (if any).

tunerepeat             How many times to perturb the problem during tuning.
                       Default = 1.

tunetime               Limit (in seconds) on tuning time; meaningful
                       if < time.  Default = 1e75.

tunetimedet            Limit (in "ticks") on tuning time; meaningful
                       if < time.  Default = 1e75.

uppercutoff            For minimization problems involving integer
                       variables, skip any branch whose LP relaxation's
                       optimal value is more than uppercutoff.  Warning:
                       if uppercutoff is too small, the problem will
                       appear infeasible.  Default = 1e75.

upperobj               Stop maximizing when the objective value
                       goes above upperobj.  Default = 1e75.

upperobjlim            Synonym for "upperobj".

varsel                 Strategy for selecting the next branching
                       variable during integer branch-and-bound:
                          -1 = branch on variable with smallest
                               integer infeasibility
                           0 = algorithm decides (default)
                           1 = branch on variable with largest
                               integer infeasibility
                           2 = branch based on pseudo costs
                           3 = strong branching
                           4 = branch based on pseudo reduced costs.

varselect              Synonym for "varsel".

version                Single-word phrase:  show the current version.

wantsol                solution report without -AMPL: sum of
                           1 = write .sol file
                           2 = print primal variable values
                           4 = print dual variable values
                           8 = do not print solution message

warninglimit           Limit on the number of warnings per issue
                       given when "datacheck=2" is specified.  Default = 10.

workfiledir            Directory where CPLEX creates a temporary
                       subdirectory for temporary files, e.g., for
                       node information and Cholesky factors.

workfilelim            Maximum size in megabytes for in-core work "files".
                       Default 2048.

writebasis             Synonym for "endbasis".

writemipstart          [Debug option] The name of a file to which the MIP
                       starting guess (if any) is written in ".mst" format.
                       If there is no MIP start, an empty file is written.

writeprob              Name of file to which the problem is written
                       in a format determined by the name's suffix:
                            .sav = binary SAV file;
                            .mps = MPS file, original names;
                            .lp = LP file, original names;
                            .rmp = MPS file, generic names;
                            .rew = MPS file, generic names;
                            .rlp = LP file, generic names.
                       SAV and LP formats are peculiar to CPLEX.

writesol               Synonym for "endsol".

zerohalfcuts           Whether to generate zero-half cuts for MIP problems:
                          -1 = no
                           0 = automatic choice (default):  continue
                               generating until new cuts are not helpful
                           1 = generate zero-half cuts moderately
                           2 = generate zero-half cuts aggressively.
```

