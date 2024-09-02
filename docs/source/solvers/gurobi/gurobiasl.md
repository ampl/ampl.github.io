
# GUROBIASL Options

```ampl
ampl: option solver gurobiasl; # change the solver
ampl: option gurobiasl_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

Solver options obtained with `$ gurobiasl -=`.

```
aggfill          Amount of fill allowed during aggregation during
                        gurobi's presolve (default -1).

aggregate        Whether to use aggregation during Gurobi presolve:
                        0 = no (sometimes reduces numerical errors)
                        1 = yes (default).

ams_eps          Relative tolerance for reporting alternate MIP solutions
                        (default 0 = no limit).

ams_epsabs       Absolute tolerance for reporting alternate MIP solutions
                        (default 0 = no limit).

ams_limit        Limit on number of alternate MIP solutions written,
                        with no limit when ams_limit = 0 (default).

ams_mode         Search mode for MIP solutions when ams_stub is specified
                        to request finding several alternative solutions:
                        0 = ignore ams_stub; seek just one optimal solution
                        1 = make some effort at finding additional solutions
                        2 = seek "ams_limit" best solutions (default).

ams_stub         Stub for alternative MIP solutions, written to files with
                        names obtained by appending "1.sol", "2.sol", etc., to
                        ams_stub.  The number of such files written is affected
                        by four keywords:
                          ams_mode specifies how much effort to expend;
                          ams_limit gives the maximum number of files written,
                                with no limit when ams_limit = 0 (default);
                          ams_eps gives a relative tolerance on the objective
                                values of alternative solutions; and
                          ams_epsabs gives an absolute tolerance on how much
                                worse the objectives can be.
                        The number of alternative MIP solution files written is
                        returned in suffix npool on the objective and problem.
                        Suffix poolignore can be used to keep only one solution
                        with the best objective value among solutions that
                        differ only in variables where the suffix is 1.

barconvtol       Tolerance on the relative difference between the
                        primal and dual objectives for stopping the barrier
                        algorithm (default 1e-8).

barcorrectors    Limit on the number of central corrections done in
                        each barrier iteration (default -1 = automatic choice)

barhomogeneous   Whether to use the homogeneous barrier algorithm
                 (e.g., when method=2 is specified):
                        -1 = only when solving a MIP node relaxation (default)
                         0 = never
                         1 = always.
                 The homogeneous barrier algorithm can detect infeasibility or
                 unboundedness directly, without crossover, but is a bit slower
                 than the nonhomogeneous barrier algorithm.

bariterlim       Limit on the number of barrier iterations (default 1000).

barorder         Ordering used to reduce fill in sparse-matrix factorizations
                                during the barrier algorithm:
                        -1 = automatic choice (default)
                         0 = approximate minimum degree
                         1 = nested dissection.

barqcptol        Convergence tolerance on the relative difference between
                 primal and dual objective values for barrier algorithms when
                 solving problems with quadratic constraints (default 1e-6).

basis            Whether to use or return a basis:
                        0 = no
                        1 = use incoming basis (if provided)
                        2 = return final basis
                        3 = both (1 + 2 = default).
                 For problems with integer variables and quadratic constraints,
                 basis = 0 is assumed quietly unless qcpdual=1 is specified.

basisdebug       Whether to honor basis and solnsens when an optimal solution
                 was not found:
                        0 = only if a feasible solution was found (default)
                        1 = yes
                        2 = no.

bestbndstop      Stop once the best bound on the objective value
                 is at least as good as this value.

bestbound        Whether to return suffix .bestbound for the best known bound
                 on the objective value:
                        0 = no (default)
                        1 = yes
                 The suffix is on the objective and problem and is +Infinity
                 for minimization problems and -Infinity for maximization
                 problems if there are no integer variables or if an integer
                 feasible solution has not yet been found.

bestobjstop      Stop after a feasible solution with objective value
                 at least as good as this value has been found.

bqpcuts          Whether to enable Boolean Quadric Polytope cut generation:
                        -1 = automatic choice (default)
                         0 = disallow BQP cuts
                         1 = enable moderate BQP cut generation
                         2 = enable aggressive BQP cut generation.
                 Values 1 and 2 override the "cuts" keyword.

branchdir        Which child node to explore first when branching:
                        -1 = explore "down" branch first
                         0 = explore "most promising" branch first (default)
                         1 = explore "up" branch first.

cliquecuts       Overrides "cuts"; choices as for "cuts".

cloudhost        Host for Gurobi Instant Cloud.

cloudid          Use Gurobi Instant Cloud with this "accessID".

cloudkey         Use Gurobi Instant Cloud with this "secretKey".
                 Both cloudid and cloudkey are required.

cloudpool        Optional "machine pool" to use with Gurobi Instant Cloud.

cloudpriority    Priority of Cloud job, an integer >= -100 and <= 100.
                 Default 0.  Jobs with priority 100 run immediately -- use
                 caution when specifying this value.

concurrentmip    How many independent MIP solves to allow at once when multiple
                 threads are available.  The available threads are divided as
                 evenly as possible among the concurrent solves.  Default = 1.

concurrentwin    Whether to return the winning method after a continuous
                 problem has been solved with concurrent optimization:
                        0 = do not return (default)
                        1 = return as problem suffix "concurrentwinmethod".
                 See option "method" for a description of the returned values.

covercuts        Overrides "cuts"; choices as for "cuts".

crossover        How to transform a barrier solution to a basic one:
                        -1 = automatic choice (default)
                         0 = none: return an interior solution
                         1 = push dual vars first, finish with primal simplex
                         2 = push dual vars first, finish with dual simplex
                         3 = push primal vars first, finish with primal simplex
                         4 = push primal vars first, finish with dual simplex

crossoverbasis   strategy for initial basis construction during crossover:
                        0 = favor speed (default)
                        1 = favor numerical stability.

cutagg           Maximum number of constraint aggregation passes
                 during cut generation (-1 = default = no limit);
                 overrides "cuts".

cutoff           If the optimal objective value is worse than cutoff,
                 report "objective cutoff" and do not return a solution.
                 Default: +Infinity for minimizing, -Infinity for maximizing.

cutpasses        Maximum number of cutting-plane passes to do
                 during root-cut generation; default = -1 ==> automatic choice.

cuts             Global cut generation control, valid unless overridden
                 by individual cut-type controls:
                        -1 = automatic choice (default)
                         0 = no cuts
                         1 = conservative cut generation
                         2 = aggressive cut generation
                         3 = very aggressive cut generation.

degenmoves       Limit on the number of degenerate simplex moves -- for use
                 when too much time is taken after solving the initial root
                 relaxation of a MIP problem and before cut generation or root
                 heuristics have started.  Default -1 ==> automatic choice.

disconnected     Whether to exploit independent MIP sub-models:
                        -1 = automatic choice (default)
                         0 = no
                         1 = use moderate effort
                         2 = use aggressive effort.

dualreductions   Whether Gurobi's presolve should use dual reductions, which
                 may be useful on a well-posed problem but can prevent
                 distinguishing whether a problem is infeasible or unbounded:
                        0 = no
                        1 = yes (default).

feasrelax        Whether to modify the problem into a feasibility
                 relaxation problem:
                        0 = no (default)
                        1 = yes, minimizing the weighted sum of violations
                        2 = yes, minimizing the weighted count of violations
                        3 = yes, minimizing the sum of squared violations
                        4-6 = same objective as 1-3, but also optimize the
                                original objective, subject to the violation
                                objective being minimized
                 Weights are given by suffixes .lbpen and .ubpen on variables
                 and .rhspen on constraints (when positive), else by keywords
                 lbpen, ubpen, and rhspen, respectively (default values = 1).
                 Weights <= 0 are treated as Infinity, allowing no violation.

feasrelaxbigm    Value of "big-M" sometimes used with constraints when doing
                 a feasibility relaxation.  Default = 1e6.

feastol          Primal feasibility tolerance (default 1e-6).

fixedmethod      Value of "method" to use when seeking a basis for MIP problems
                 when "basis=2" or (the default) "basis=3" has been specified.
                 Default: if "method" is 0 or 1 then "method" else 1.

flowcover        flowcover cuts:  Overrides "cuts"; choices as for "cuts".

flowpath         flowpath cuts:  Overrides "cuts"; choices as for "cuts".

gomory           Maximum number of Gomory cut passes during cut generation
                 (-1 = default = no limit); overrides "cuts".

gubcover         gubcover cuts:  Overrides "cuts"; choices as for "cuts".

heurfrac         Fraction of time to spend in MIP heuristics (default 0.05)

iisfind          Whether to return an IIS (irreducible infeasible set of
                 constraints and variable bounds, via suffix .iis on
                 constraints and variables) when the problem is infeasible:
                        0 = no (default)
                        1 ==> yes.
                 When iisfind=1 and the problem is infeasible, suffixes
                 iisforce, iisforcelb, and iisforceub can be used to influence
                 the IIS found, either forcing an entity to be in or not in the
                 IIS or letting the algorithm decide:
                        0 = algorithm decides (default)
                        1 = force to be excluded from the IIS
                        2 = force to be included in the IIS.

iismethod        Which method to use when finding an IIS (irreducible
                 infeasible set of constraints, including variable bounds):
                        -1 = automatic choice (default)
                         0 = often faster than method 1
                         1 = can find a smaller IIS than method 0.

implied          implied cuts:  Overrides "cuts"; choices as for "cuts".

improvegap       Optimality gap below which the MIP solver switches from
                 trying to improve the best bound to trying to find better
                 feasible solutions (default 0).

improvetime      Execution seconds after which the MIP solver switches from
                 trying to improve the best bound to trying to find better
                 feasible solutions (default Infinity).

impstartnodes    Number of MIP nodes after which the solution strategy
                 will change from improving the best bound to finding better
                 feasible solutions (default Infinity).

infproofcuts     Whether to generate infeasibility proof cuts:
                        -1 = automatic choice (default)
                         0 = no
                         1 = moderate cut generation
                         2 = aggressive cut generation.

integrality      Setting this parameter to 1 requests the solver to work
                 harder at finding solutions that are still (nearly) feasible
                 when all integer variables are rounded to exact integral
                 values:
                        0 = no (default)
                        1 = yes.

intfeastol       Feasibility tolerance for integer variables (default 1e-05).

intstart         When there are integer variables, whether to use
                 an initial guess (if available):
                        0 = no
                        1 = yes (default).

iterlim          iteration limit (default: no limit)

kappa            Whether to return the estimated condition number (kappa) of
                 the optimal basis (default 0): sum of
                        1 = report kappa in Gurobi's result message;
                        2 = return kappa in the solver-defined suffix kappa on
                            the objective and problem.
                 The request is ignored when there is no optimal basis.

lazy             Whether to honor suffix .lazy on linear constraints in
                 problems with binary or integer variables:
                        0 = no (ignore .lazy)
                        1 = yes (default).
                 Lazy constraints are indicated with .lazy values of -1, 1, 2,
                 or 3 and are ignored until a solution feasible to the
                 remaining constraints is found.  What happens next depends
                 on the value of .lazy:
                       -1 ==> treat the constraint as a user cut; the
                              constraint must be redundant with respect to the
                              rest of the model, although it can cut off LP
                              solutions;
                        1 ==> the constraint may still be ignored if another
                              lazy constraint cuts off the current solution;
                        2 ==> the constraint will henceforth be enforced if it
                              is violated by the current solution;
                        3 ==> the constraint will henceforth be enforced.

lbpen            See feasrelax.

liftprojectcuts  Whether to generate lift-and-project cuts:
                        -1 = automatic choice (default)
                         0 = no
                         1 = moderate cut generation
                         2 = aggressive cut generation.

logfile          Name of file to receive log lines (default: none);
                        implies outlev = 1.

logfreq          Interval in seconds between log lines (default 5).

lpmethod         Synonym for method.

lpwarmstart      Controls how gurobi uses warm-start in LP optimization:
                        0 = ignore information
                        1 = use information to solve the original problem
                        2 = use the (crushed) information to solve the
                            presolved problem.
                 Note that if presolve is disabled, 1 prioritizes basis
                 statuses, 2 prioritizes start vectors.  Default = 1.

maxmipsub        Maximum number of nodes for RIMS heuristic to explore
                 on MIP problems (default 500).

maxvio           Whether to return the maximum of all (unscaled) violations to
                 the current problem:
                        0 = do not return (default)
                        1 = return in the problem suffix "maxvio".

memlimit         Maximum amount of memory available to Gurobi (in GB, default
                 no limit). The solution will fail if more memory is needed.

method           Which algorithm to use for non-MIP problems or for the root
                 node of MIP problems:
                        -1 automatic (default): 3 for LP, 2 for QP, 1 for MIP
                                root node
                         0 = primal simplex
                         1 = dual simplex
                         2 = barrier
                         3 = nondeterministic concurrent (several solves in
                                parallel)
                         4 = deterministic concurrent
                         5 = deterministic concurrent simplex.

minrelnodes      Number of nodes for the Minimum Relaxation heuristic to
                 explore at the MIP root node when a feasible solution has not
                 been found by any other heuristic; default -1 ==> automatic
                 choice.

mipfocus         MIP solution strategy:
                        0 = balance finding good feasible solutions and
                            proving optimality (default)
                        1 = favor finding feasible solutions
                        2 = favor proving optimality
                        3 = focus on improving the best objective bound.

mipgap           max. relative MIP optimality gap (default 1e-4)

mipgapabs        absolute MIP optimality gap (default 1e-10)

mipsep           MIPsep cuts:  Overrides "cuts"; choices as for "cuts".

mipstart         Whether to use initial guesses in problems with
                 integer variables:
                        0 = no
                        1 = yes (default).

miqcpmethod      Method for solving mixed-integer quadratically constrained
                 (MIQCP) problems:
                        -1 = automatic choice (default)
                         0 = solve continuous QCP relaxations at each node
                         1 = use linearized outer approximations.

mircuts          MIR cuts:  Overrides "cuts"; choices as for "cuts".

modkcuts         mod-k cuts:  Overrides "cuts"; choices as for "cuts".

multiobj         Whether to do multi-objective optimization:
                        0 = no (default)
                        1 = yes
                 When multiobj = 1 and several objectives are present, suffixes
                 .objpriority, .objweight, .objreltol, and .objabstol on the
                 objectives are relevant.  Objectives with greater .objpriority
                 values (integer values) have higher priority.  Objectives with
                 the same .objpriority are weighted by .objweight.  Objectives
                 with positive .objabstol or .objreltol are allowed to be
                 degraded by lower priority objectives by amounts not exceeding
                 the .objabstol (absolute) and .objreltol (relative) limits.
                 The objective must all be linear.  Objective-specific
                 convergence tolerances and method values may be assigned via
                 keywords of the form obj_n_name, such as obj_1_method for the
                 first objective.

multiobjmethod   Choice of optimization algorithm for lower-priority
                 objectives:
                        -1 = automatic choice (default)
                         0 = primal simplex
                         1 = dual simplex
                         2 = ignore warm-start information; use the algorithm
                                specified by the method keyword.
                 The method keyword determines the algorithm to use for the
                 highest priority objective.

multiobjpre      How to apply Gurobi's presolve when doing
                 multi-objective optimization:
                        -1 = automatic choice (default)
                         0 = do not use Gurobi's presolve
                         1 = conservative presolve
                         2 = aggressive presolve, which may degrade lower-
                                priority objectives.

multprice_norm   Choice of norm used in multiple pricing:
                        -1 = automatic choice (default)
                         0, 1, 2, 3 = specific choices:  hard to describe,
                                but sometimes a specific choice will perform
                                much better than the automatic choice.

networkalg       Controls whether to use network simplex, if an LP is a
                 network problem:
                        -1 = automatic choice (default)
                         0 = do not use network simplex
                         1 = use network sinmplex.

networkcuts      Network cuts:  Overrides "cuts"; choices as for "cuts".

nlpheur          Controls the NLP heuristic, affecting non-convex quadratic
                 problems:
                         0 = Do not apply heuristic
                         1 = Apply heuristic (default).

nodefiledir      Directory where MIP tree nodes are written after memory
                 for them exceeds nodefilestart; default "."

nodefilestart    Gigabytes of memory to use for MIP tree nodes;
                 default = Infinity (no limit, i.e., no node files written).

nodelim          maximum MIP nodes to explore (default: no limit)

nodemethod       Algorithm used to solve relaxed MIP node problems:
                        -1 = automatic choice (default)
                         0 = primal simplex
                         1 = dual simplex (default)
                         2 = barrier.

nonconvex        How to handle non-convex quadratic objectives and constraints:
                        -1 = default choice (currently the same as 1)
                         0 = complain about nonquadratic terms
                         1 = complain if Gurobi's presolve cannot discard or
                                eliminate nonquadratic terms
                         2 = translate quadratic forms to bilinear form and use
                                spatial branching.

norelheurtime    Limits the amount of time spent in the NoRel heuristic;
                 see the description of norelheurwork for details.  This
                 parameter will introduce non determinism; use norelheurwork
                 for deterministic results.  Default 0.

norelheurwork    Limits the amount of work spent in the NoRel heuristic.
                 This heuristics searches for high-quality feasible solutions
                 before solving the root relaxation.  The work metrix is hard
                 to define precisely, as it depends on the machine.  Default 0.

normadjust       Synonym for multprice_norm.

numericfocus     How much to try detecting and managing numerical issues:
                        0 = automatic choice (default)
                        1-3 = increasing focus on more stable computations.

obbt             Controls aggressiveness of Optimality-Based Bound Tightening:
                        -1 = automatic choice (default)
                         0 = do not use OBBT
                         1 = low aggressiveness
                         2 = moderate  aggressiveness
                         3 = high aggressiveness.

objno            Objective to optimize:
                        0 = none
                        1 = first (default, if available),
                        2 = second (if available), etc.

objrep           Whether to replace
                        minimize obj: v;
                 with
                        minimize obj: f(x)
                 when variable v appears linearly in exactly one constraint
                 of the form
                        s.t. c: v >= f(x);
                 or
                        s.t. c: v == f(x);
                 Possible objrep values:
                        0 = no
                        1 = yes for v >= f(x)
                        2 = yes for v == f(x) (default)
                        3 = yes in both cases
                 For maximization problems, ">= f(x)" is changed to "<= f(x)"
                 in the description above.

objscale         How to scale the objective:
                        0 ==> automatic choice (default)
                        negative >= -1 ==> divide by max abs. coefficient
                                           raised to this power
                        positive ==> divide by this value.

opttol           Optimality tolerance on reduced costs (default 1e-6).

outlev           Whether to write Gurobi log lines (chatter) to stdout:
                        0 = no (default)
                        1 = yes (see logfreq).

param            General way to specify values of both documented and
                 undocumented Gurobi parameters; value should be a quoted
                 string (delimited by ' or ") containing a parameter name, a
                 space, and the value to be assigned to the parameter.  Can
                 appear more than once.  Cannot be used to query current
                 parameter values.

paramfile        Name of file (surrounded by 'single' or "double" quotes if the
                 name contains blanks) of parameter names and values for them.
                 Lines that start with # are ignored.  Otherwise, each nonempty
                 line should contain a name and a value, separated by a space.

partitionplace   Whether and how to use the .partition suffix on variables
                 in the partition heuristic for MIP problems: sum of
                         1 ==> when the branch-and-cut search ends
                         2 ==> at nodes in the branch-and-cut search
                         4 ==> after the root-cut loop
                         8 ==> at the start of the root-cut loop
                        16 ==> before solving the root relaxation.
                 Default = 15.  Values of .parition determine how variables
                 participate in the partition heuristic.  Variables with
                        .partition = -1 are always held fixed;
                        .partition = 0 can vary in all sub-MIP models;
                        .partition > 0 can vary only in in that sub-MIP model.
                 The partition heuristic is only run when partition_place is
                 between 1 and 31 and some variables have suitable .partition
                 suffix values.

perturb          Magnitude of simplex perturbation (when needed; default 2e-4).

pivtol           Markowitz pivot tolerance (default 7.8125e-3)

poolgap          Synonym for ams_eps.

poolgapabs       Synonym for ams_epsabs.

poolsearchmode   Synonym for ams_mode.

poolsolutions    Synonym for ams_limit.

poolstub         Synonym for ams_stub.

predeprow        Whether Gurobi's presolve should remove linearly
                 dependent constraint-matrix rows:
                        -1 = only for continuous models (default)
                         0 = never
                         1 = for all models.

predual          Whether gurobi's presolve should form the dual of a
                                continuous model:
                        -1 = automatic choice (default)
                         0 = no
                         1 = yes
                         2 = form both primal and dual and use two threads to
                             choose heuristically between them.

premiqcpform     For mixed-integer quadratically constrained (MIQCP) problems,
                 how Gurobi should transform quadratic constraints:
                        -1 = automatic choice (default)
                         0 = retain MIQCP form
                         1 = transform to second-order cone contraints
                         2 = transform to rotated cone constraints
                 Choices 0 and 1 work with general quadratic constraints.
                 Choices 1 and 2 only work with constraints of suitable forms.

prepases         deprecated synonym for "prepasses"

prepasses        Limit on the number of Gurobi presolve passes:
                        -1 = automatic choice (automatic)
                         n >= 0: at most n passes.

preqlinearize    How Gurobi's presolve should treat quadratic problems:
                        -1 = automatic choice (default)
                         0 = do not modify the quadratic part(s)
                         1 or 2 = try to linearize quadratic parts:
                                1 = focus on a strong LP relaxation
                                2 = focus on a compact relaxation.

presolve         Whether to use Gurobi's presolve:
                        -1 = automatic choice (default)
                         0 = no
                         1 = conservative presolve
                         2 = aggressive presolve.

presos1bigm      Big-M for converting SOS1 constraints to binary form:
                        -1 = automatic choice (default)
                         0 = no conversion
                 Large values (e.g., 1e8) may cause numeric trouble.

presos2bigm      Big-M for converting SOS2 constraints to binary form:
                        -1 = automatic choice
                         0 = no conversion (default)
                 Large values (e.g., 1e8) may cause numeric trouble.

presos1enc       Encoding used for SOS1 reformulation:
                        -1 = automatic choice (default)
                         0 = multiple choice model, produces an LP relaxation
                             that is easy to solve
                         1 = incremental model, reduces the amount of branching
                         2 = formulation whose LP relaxation is easier to solve
                         3 = formulation with better branching behavior,
                             requires sum of the variables == 1.
                 Options 0 and 1 produce reformulations that are linear in
                 size; options 2 and 3 use reformulation logarithmic in size.
                 Option 2 and 3 apply only when all the variables are >=0.

presos2enc       Encoding used for SOS2 reformulation, see presos1enc.

presparsify      Whether Gurobi's presolve should use its "sparsify reduction",
                 which sometimes gives significant problem-size reductions:
                        -1 = automatic choice
                         0 = no
                         1 = yes.

pricing          Pricing strategy:
                        -1 = automatic choice (default)
                         0 = partial pricing
                         1 = steepest edge
                         2 = Devex
                         3 = quick-start steepest edge.

priorities       Whether to use the variable.priority suffix with MIP problems.
                 When several branching candidates are available, a variable
                 with the highest .priority is chosen for the next branch.
                 Priorities are nonnegative integers (default 0).
                 Possible values for "priorities":
                        0 = ignore .priority; assume priority 0 for all vars
                        1 = use .priority if present (default).

psdtol           Maximum diagonal perturbation to correct indefiniteness
                 in quadratic objectives (default 1e-6).

pumppasses       Number of feasibility-pump passes to do after the MIP root
                 when no other root heuristoc found a feasible solution.
                 Default -1 = automatic choice.

qcpdual          Whether to compute dual variables when the problem
                 has quadratic constraints (which can be expensive):
                        0 = no (default)
                        1 = yes.

quad             Whether simplex should use quad-precision:
                        -1 = automatic choice (default)
                         0 = no
                         1 = yes.

rays             Whether to return suffix .unbdd if the objective is unbounded
                 or suffix .dunbdd if the constraints are infeasible:
                        0 = neither
                        1 = just .unbdd
                        2 = just .dunbdd
                        3 = both (default).

relax            Whether to relax integrality:
                        0 = no (default)
                        1 = yes: treat integer and binary variables
                                as continuous.

relaxliftcuts    Whether to enable relax-and-lift cut generation:
                        -1 = automatic choice (default)
                         0 = disallow relax-and-lift cuts
                         1 = enable moderate relax-and-lift cut generation
                         2 = enable aggressive relax-and-lift cut generation.
                 Values 1 and 2 override the "cuts" keyword.

resultfile       Name of a file of extra information written after
                 completion of optimization.  The name's suffix determines what
                 is written:
                        .sol  solution vector
                        .bas  simplex basis
                        .mst  integer variable solution vector.

return_mipgap    Whether to return mipgap suffixes or include mipgap values
                 (|objectve - best_bound|) in the solve_message:  sum of
                        1 = return relmipgap suffix (relative to |obj|);
                        2 = return absmipgap suffix (absolute mipgap);
                        4 = suppress mipgap values in solve_message.
                 Default = 0.  The suffixes are on the objective and problem.
                 Returned suffix values are +Infinity if no integer-feasible
                 solution has been found, in which case no mipgap values are
                 reported in the solve_message.

rhspen           See feasrelax.

rins             How often to apply the RINS heuristic for MIP problems:
                        -1 = automatic choice (default)
                         0 = never
                         n > 0: every n-th node.

rltcuts          Whether to enable generation of cuts by the Relaxation
                 Linearization Technique (RLT):
                        -1 = automatic choice (default)
                         0 = disallow RLT cuts
                         1 = enable moderate RLT cut generation
                         2 = enable aggressive RLT cut generation.
                 Values 1 and 2 override the "cuts" keyword.

round            Whether to round integer variables to integral values before
                 returning the solution, and whether to report that GUROBI
                 returned noninteger values for integer values:  sum of
                         1 ==> round nonintegral integer variables
                         2 ==> modify solve_result
                         4 ==> modify solve_message
                 Default = 7.  Modifications that were or would be made are
                 reported in solve_result and solve_message only if the maximum
                 deviation from integrality exceeded round_reptol.

round_reptol     Tolerance for reporting rounding of integer variables to
                 integer values; see "round".  Default = 1e-9.

scale            Whether to scale the problem:
                        -1 = automatic choice (default)
                         0 = no
                         1 = yes
                         2 = yes, more aggressively
                         3 = yes, even more aggressively.

seed             Random number seed (default 0), affecting perturbations that
                 may influence the solution path.

server           Comma-separated list of Gurobi compute servers, specified
                 either by name or by IP address.  Default: run Gurobi locally
                 (i.e., do not use a remote Gurobi server).

server_insecure  Whether to use "insecure mode" with the Gurobi Compute
                 Server.  Should be left at default value (0) unless an
                 administrator specifies another value.

server_password  Password (if needed) for specified Guruobi compute server(s).

server_priority  Priority for Gurobi compute server(s).  Default = 0.
                 Highest priority = 100.

server_timeout   Report job as rejected by Gurobi compute server if the
                 job is not started within server_timeout seconds.
                 Default = -1 (no limit).

serverlic        Name of file containing "server = ..." and possibly
                 values for server_password, server_port, and server_timeout.
                 Synonyms for server: computeserver, servers.
                 Synonym for server_password: password.

servers          Synonym for server.

sifting          Whether to use sifting within the dual simplex algorithm,
                 which can be useful when there are many more variables than
                 constraints:
                        -1 = automatic choice (default)
                         0 = no
                         1 = yes, moderate sifting
                         2 = yes, aggressive sifting.

siftmethod       Algorithm to use for sifting with the dual simplex method:
                        -1 = automatic choice (default)
                         0 = primal simplex
                         1 = dual simplex
                         2 = barrier.

simplex          Synonym for method.

softmemlimit     Maximum amount of memory available to Gurobi (in GB; default
                 = no limit). The solution is returned even if more memory
                 could be used.

solnlimit        maximum MIP solutions to find (default 2e9)

solnsens         Whether to return suffixes for solution sensitivities, i.e.,
                 ranges of values for which the optimal basis remains optimal:
                        0 = no (default)
                        1 = yes:  suffixes return on variables are
                                .sensobjlo = smallest objective coefficient
                                .sensobjhi = greatest objective coefficient
                                .senslblo = smallest variable lower bound
                                .senslbhi = greatest variable lower bound
                                .sensublo = smallest variable upper bound
                                .sensubhi = greatest variable upper bound
                        suffixes for constraints are
                                .sensrhslo = smallest right-hand side value
                                .sensrhshi = greatest right-hand side value.
                 For range constraints Lconst <= expr <= Uconst or equivalently
                 Uconst >= expr >= Lconst (where both Lconst and Uconst are
                 constants and expr is an expression involving variables,
                 .sensrhslo and .sensrhshi apply to Lconst and
                                .sensrhslo2 = smallest Uconst
                                .sensrhslo2 = greatest Uconst.
                 Note that AMPL converts constraints with a single relational
                 operator into the form expr relop Const.  If you write
                 Const relop expr, AMPL converts it to -(expr) relop -(Const).
                 You need to take this into account when examining the
                 .sensrhslo and .sensrhshi values.
                 For problems with integer variables and quadratic constraints,
                 solnsens = 0 is quietly assumed.

solutiontarget   Specifies the solution targetfor linear programs (LP):
                        -1 = automatic (default)
                        0 = primal and dual optimal and basic
                        1 = primal and dual optimal.

sos              whether to honor declared suffixes .sosno and .ref describing
                 SOS sets:
                        0 = no
                        1 = yes (default):  each distinct nonzero .sosno
                                value designates an SOS set, of type 1 for
                                positive .sosno values and of type 2 for
                                negative values.  The .ref suffix contains
                                corresponding reference values.

sos2             Whether to tell Gurobi about SOS2 constraints for nonconvex
                 piecewise-linear terms:
                        0 = no
                        1 = yes (default), using suffixes .sos and .sosref
                                provided by AMPL.

startnodelimit   Limit on how many branch-and-bound nodes to explore when
                 doing a partial MIP start:
                        -2 = suppress MIP start processing
                        -1 = use submipnodes (default)
                        >= 0 ==> specific node limit.

submipcuts       sub-MIP cuts:  Overrides "cuts"; choices as for "cuts".

submipnodes      Limit on nodes explored by MIP-based heuristics, e.g., RINS.
                 Default = 500.

symmetry         MIP symmetry detection:
                        -1 = automatic choice (default)
                         0 = none
                         1 = conservative
                         2 = agressive.

threads          How many threads to use when using the barrier algorithm
                 or solving MIP problems; default 0 ==> automatic choice.

timelim          limit on solve time (in seconds; default: no limit)

timing           Whether to report timing:
                        0 = no (default)
                        1 = report times on stdout
                        2 = report times on stderr.

tunebase         Base name for results of running Gurobi's search for better
                 parameter settings.  The search is run only when tunebase
                 is specified.  Results are written to files with names derived
                 from tunebase by appending ".prm" if ".prm" does not occur in
                 tunebase and inserting 1, 2, ... (for the first, second,
                 ... set of parameter settings) before the right-most ".prm".
                 The file with "1" inserted is the best set and the solve
                 results returned are for this set.  In a subsequent "solve;",
                 you can use paramfile=... to apply the settings in results
                 file ... .

tuneoutput       Amount of tuning output when tunebase is specified:
                        0 = none
                        1 = summarize each new best parameter set
                        2 = summarize each set tried (default)
                        3 = summary plus detailed solver output for each trial.

tuneresults      Limit on the number of tuning result files to write
                 when tunerbase is specified.  The default (-1) is to write
                 results for all parameter sets on the efficient frontier.

tunetimelimit    Time limit (in seconds) on tuning when tunebase
                 is specified.  Default -1 ==> automatic choice of time limit.

tunetrials       Number of trials for each parameter set when tunebase
                 is specified, each with a different random seed value.
                 Default = 3.

ubpen            See feasrelax.

varbranch        MIP branch variable selection strategy:
                        -1 = automatic choice (default)
                         0 = pseudo reduced-cost branching
                         1 = pseudo shadow-price branching
                         2 = maximum infeasibility branching
                         3 = strong branching.

version          Report version details before solving the problem.  This is a
                 single-word "phrase" that does not accept a value assignment.

wantsol          solution report without -AMPL: sum of
                        1 ==> write .sol file
                        2 ==> print primal variable values
                        4 ==> print dual variable values
                        8 ==> do not print solution message.

warmstart        Whether to use incoming primal and dual variable values
                 (if both are available) in a simplex warm start:
                        0 = no;
                        1 = yes if there is no incoming basis (default);
                        2 = yes, ignoring the incoming basis (if any);
                        3 = no, but on MIP problems, use the incoming primal
                            values as hints, ignoring the .hintpri suffix;
                        4 = similar to 3, but use the .hintpri suffix on
                            variables:  larger (integer) values give greater
                            priority to the initial value of the associated
                            variable.
                 Note that specifying basis=0 or basis=2 causes there to be
                 no incoming basis.  This is relevant to warmstart values
                 1, 3, and 4.  For continuous problems, warmstart values >= 2
                 are treated as 1.
                 Normally an incoming solution vector disables Gurobi's
                 LP presolve; to enable it set lpwarmstart to 2.

work             Whether to report the amount of (deterministic) work spent on
                 the latest optimization:
                        0 = do not report (default)
                        1 = report in the problem suffix "work".

worklimit        Maximum amount of work expended (in work units); in contrast
                 to timelim, work limits are deterministic (default no limit).

writeprob        Name of a GUROBI-format file to be written (for debugging);
                 must end in one of ".bas", ".lp", ".mps", ".prm", ".rew",
                 ".rlp", ".sol", or for the "fixed" model used to recover a
                 basis or dual values for problems with integer variables or
                 quadratic constraints, ".fix_lp" or ".fix_mps"; the '_' will
                 be replaced by '.' in the name of the file written for
                 ".fix_lp" or ".fix_mps".  Can appear more than once with
                 different filenames.

zerohalfcuts     zero-half cuts:  Overrides "cuts"; choices as for "cuts".

zeroobjnodes     Number of nodes to explore at the root MIP node if no other
                 heuristic has found a feasible solution.  Default = -1
                 (automatic choice).
```

