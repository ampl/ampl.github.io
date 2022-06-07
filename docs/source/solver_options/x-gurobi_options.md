
# x-GUROBI Options

Obtained with `$ x-gurobi -=`.

```
x-Gurobi Optimizer Options for AMPL
-----------------------------------

To set these options, assign a string specifying their values to the AMPL
option "gurobi_options". For example:

   ampl: option gurobi_options 'opttol=1e-6';

Options:

acc:abs
      Acceptance level for 'abs' expression, default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

      It is advisable to experiment with the acceptance levels to find
      best-performing settings.

acc:and
      Acceptance level for 'and'/'forall' expressions, default 2.

acc:ind:eq (acc:ind_eq)
      Acceptance level for 'implied-equal' expression, default 2.

acc:ind:le (acc:ind_le, acc:ind:ge, acc:ind_ge)
      Acceptance level for 'implied-less-equal' and 'implied-greater-equal'
      expressions, default 2.

acc:max
      Acceptance level for 'max' expression, default 2.

acc:min
      Acceptance level for 'min' expression, default 2.

acc:or
      Acceptance level for 'or'/'exists' expressions, default 2.

alg:basis (basis)
      Whether to use or return a basis:

      0 - No
      1 - Use incoming basis (if provided)
      2 - Return final basis
      3 - Both (1 + 2 = default.)

      Note that if you provide a valid starting extreme point, either through
      primal/dual status, or through warmstart, then Gurobi LP presolve will
      be disabled. For models where presolve greatly reduces the problem size,
      this might hurt performance.

      For problems with integer variables or quadratic constraints,
      alg:basis=0 is assumed quietly unless mip:basis=1 or qcp:dual=1 is
      specified, respectively.

alg:cutoff (cutoff)
      If the optimal objective value is worse than cutoff, report "objective
      cutoff" and do not return a solution. Default: Infinity for minimizing,
      -Infinity for maximizing.

alg:feasrelax (feasrelax)
      Whether to modify the problem into a feasibility relaxation problem:

      0 = No (default)
      1 = Yes, minimizing the weighted sum of violations
      2 = Yes, minimizing the weighted sum of squared violations
      3 = Yes, minimizing the weighted count of violations
      4-6 = Same objective as 1-3, but also optimize the original objective,
      subject to the violation objective being minimized.

      Weights are given by suffixes .lbpen and .ubpen on variables and .rhspen
      on constraints (when nonnegative), else by keywords alg:lbpen,
      alg:ubpen, and alg:rhspen, respectively (default values = 1). Weights <
      0 are treated as Infinity, allowing no violation.

alg:feasrelaxbigm (feasrelaxbigm)
      Value of "big-M" sometimes used with constraints when doing a
      feasibility relaxation. Default = 1e6.

alg:feastol (feastol)
      Primal feasibility tolerance (default 1e-6).

alg:iisfind (iisfind, iis)
      Whether to find and export the IIS. Default = 0 (don't export).

alg:iismethod (iismethod)
      Which method to use when finding an IIS (irreducible infeasible set of
      constraints, including variable bounds):

      -1 - Automatic choice (default)
      0  - Often faster than method 1
      1  - Can find a smaller IIS than method 0
      2  - Ignore the bound constraints.

alg:kappa (kappa, basis_cond)
      Whether to return the estimated condition number (kappa) of the optimal
      basis (default 0): sum of 1 = report kappa in the result message; 2 =
      return kappa in the solver-defined suffix kappa on the objective and
      problem. The request is ignored when there is no optimal basis.

alg:lbpen (lbpen)
      See alg:feasrelax.

alg:method (method, lpmethod, simplex)
      Which algorithm to use for non-MIP problems or for the root node of MIP
      problems:

      -1 - Automatic (default): 3 for LP, 2 for QP, 1 for MIP
      0  - Primal simplex
      1  - Dual simplex
      2  - Barrier
      3  - Nondeterministic concurrent (several solves in parallel)
      4  - Deterministic concurrent
      5  - Deterministic concurrent simplex.

alg:numericfocus (numericfocus)
      How much to try detecting and managing numerical issues:

      0 - Automatic choice (default)
      1-3 - Increasing focus on more stable computations.

alg:rays (rays)
      Whether to return suffix .unbdd if the objective is unbounded or suffix
      .dunbdd if the constraints are infeasible:

      0 - Neither
      1 - Just .unbdd
      2 - Just .dunbdd
      3 - Both (default).

alg:relax (relax)
      0*/1: Whether to relax integrality of variables.

alg:rhspen (rhspen)
      See alg:feasrelax.

alg:sens (sens, solnsens, sensitivity)
      Whether to return suffixes for solution sensitivities, i.e., ranges of
      values for which the optimal basis remains optimal:

      0 - No (default)
      1 - Yes: suffixes return on variables are
      .sensobjlo = smallest objective coefficient
      .sensobjhi = greatest objective coefficient
      .senslblo = smallest variable lower bound
      .senslbhi = greatest variable lower bound
      .sensublo = smallest variable upper bound
      .sensubhi = greatest variable upper bound; suffixes for constraints are
      .sensrhslo = smallest right-hand side value
      .sensrhshi = greatest right-hand side value.

      For problems with integer variables or quadratic constraints, alg:sens=0
      is assumed quietly.

alg:start (warmstart)
      Whether to use incoming primal (and dual, for LP) variable values in a
      warmstart:

      0 - No
      1 - Yes (for LP: if there is no incoming alg:basis) (default)
      2 - Yes (for LP: ignoring the incoming alg:basis, if any.)

      Note that for LP, "alg:basis" is usually more efficient.
      For Gurobi, MIP-specific options can be tuned via "mip:start".

alg:ubpen (ubpen)
      See alg:feasrelax.

bar:convtol (barconvtol)
      Tolerance on the relative difference between the primal and dual
      objectives for stopping the barrier algorithm (default 1e-8).

bar:corr (barcorrectors)
      Limit on the number of central corrections done in each barrier
      iteration(default -1 = automatic choice).

bar:crossover (crossover)
      How to transform a barrier solution to a basic one:

      -1 - Automatic choice (default)
      0  - None: return an interior solution
      1  - Push dual vars first, finish with primal simplex
      2  - Push dual vars first, finish with dual simplex
      3  - Push primal vars first, finish with primal simplex
      4  - Push primal vars first, finish with dual simplex.

bar:crossoverbasis (crossoverbasis)
      Strategy for initial basis construction during crossover:

      0 - Favor speed (default)
      1 - Favor numerical stability.

bar:homog (barhomogeneous)
      Whether to use the homogeneous barrier algorithm (e.g., when method=2 is
      specified):

      -1 - Only when solving a MIP node relaxation (default)
      0  - Never
      1  - Always.

      The homogeneous barrier algorithm can detect infeasibility or
      unboundedness directly, without crossover, but is a bit slower than the
      nonhomogeneous barrier algorithm.

bar:iterlim (bariterlim)
      Limit on the number of barrier iterations (default 1000).

bar:order (barorder)
      Ordering used to reduce fill in sparse-matrix factorizations during the
      barrier algorithm. Possible values:

      -1 - Automatic choice (default)
      0  - Approximate minimum degree
      1  - Nested dissection.

bar:qcptol (barqcptol)
      Convergence tolerance on the relative difference between primal and dual
      objective values for barrier algorithms when solving problems with
      quadratic constraints (default 1e-6).

cut:agg (cutagg, cut:aggpasses)
      Maximum number of constraint aggregation passes during cut generation
      (-1 = default = no limit); overrides "cuts".

cut:bqp (bqpcuts)
      Whether to enable Boolean Quadric Polytope cut generation:

      -1 - Automatic choice (default)
      0  - Disallow BQP cuts
      1  - Enable moderate BQP cut generation
      2  - Enable aggressive BQP cut generation.

      Overrides the "cuts" keyword.

cut:clique (cliquecuts)
      Overrides "cuts"; choices as for "cuts".

cut:cover (covercuts)
      Overrides "cuts"; choices as for "cuts".

cut:cuts (cuts)
      Global cut generation control, valid unless overridden by individual
      cut-type controls:

      -1 - Automatic choice (default)
      0  - No cuts
      1  - Conservative cut generation
      2  - Aggressive cut generation
      3  - Very aggressive cut generation.

cut:flowcover (flowcover)
      Flowcover cuts: overrides "cuts"; choices as for "cuts".

cut:flowpath (flowpath)
      Overrides "cuts"; choices as for "cuts".

cut:gomory (gomory)
      Maximum number of Gomory cut passes during cut generation (-1 = default
      = no limit); overrides "cuts".

cut:gubcover (gubcover)
      Overrides "cuts"; choices as for "cuts".

cut:implied (implied)
      Implied cuts: overrides "cuts"; choices as for "cuts".

cut:infproof (infproofcuts)
      Whether to generate infeasibility proof cuts:

      -1 - Automatic choice (default)
      0  - No
      1  - Moderate cut generation
      2  - Aggressive cut generation.

cut:mipsep (mipsep)
      MIPsep cuts: overrides "cuts"; choices as for "cuts".

cut:mir (mircuts)
      MIR cuts: overrides "cuts"; choices as for "cuts".

cut:modk (modkcuts)
      Mod-k cuts: overrides "cuts"; choices as for "cuts".

cut:network (networkcuts)
      Network cuts: overrides "cuts"; choices as for "cuts".

cut:passes (cutpasses)
      Maximum number of cutting-plane passes during root-cut generation;
      default = -1 ==> automatic choice.

cut:relaxliftcuts (relaxliftcuts)
      Whether to enable relax-and-lift cut generation:

      -1 - Automatic choice (default)
      0  - No cuts
      1  - Conservative cut generation
      2  - Aggressive cut generation.

cut:rltcuts (rltcuts)
      Whether to enable generation of cuts by the Relaxation Linearization
      Technique (RLT):

      -1 - Automatic choice (default)
      0  - No cuts
      1  - Conservative cut generation
      2  - Aggressive cut generation.

cut:submip (submipcuts)
      Sub-MIP cuts: overrides "cuts"; choices as for "cuts".

cut:zerohalf (zerohalfcuts)
      Zero-half cuts: overrides "cuts"; choices as for "cuts".

cvt:mip:eps (cvt:cmp:eps)
      Tolerance for strict comparison of continuous variables for MIP. Ensure
      larger than the solver's feasibility tolerance.

cvt:pre:all
      0/1*: Set to 0 to disable most presolve in the flat converter.

cvt:pre:eqbinary
      0/1*: Preprocess reified equality comparison with a binary variable.

cvt:pre:eqresult
      0/1*: Preprocess reified equality comparison's boolean result bounds.

cvt:sos (sos)
      0/1*: Whether to honor declared suffixes .sosno and .ref describing SOS
      sets. Each distinct nonzero .sosno value designates an SOS set, of type
      1 for positive .sosno values and of type 2 for negative values. The .ref
      suffix contains corresponding reference values used to order the
      variables.

cvt:sos2 (sos2)
      0/1*: Whether to honor SOS2 constraints for nonconvex piecewise-linear
      terms, using suffixes .sos and .sosref provided by AMPL.

lim:iter (iterlim, iterlimit)
      Iteration limit (default: no limit).

lim:minrelnodes (minrelnodes)
      Number of nodes for the Minimum Relaxation heuristic to explore at the
      MIP root node when a feasible solution has not been found by any other
      heuristic; default -1 ==> automatic choice.

lim:nodes (nodelim, nodelimit)
      Maximum MIP nodes to explore (default: no limit).

lim:startnodes (startnodelimit, startnodes)
      Limit on how many branch-and-bound nodes to explore when doing a partial
      MIP start:

      -3 - Suppress MIP start processing
      -2 - Only check full MIP starts for feasibility and ignore partial MIP
      starts
      -1 - Use "submipnodes" (default)
      >=0 - Specific node limit.

lim:submipnodes (submipnodes, maxmipsub)
      Limit on nodes explored by MIP-based heuristics, e.g., RINS. Default =
      500.

lim:time (timelim, timelimit)
      Limit on solve time (in seconds; default: no limit).

lim:zeroobjnodes (zeroobjnodes)
      Number of nodes to explore in the zero objective heuristic. Note that
      this heuristic is only applied at the end of the MIP root, and only when
      no other root heuristic finds a feasible solution.

      This heuristic is quite expensive, and generally produces poor quality
      solutions. You should generally only use it if other means, including
      exploration of the tree with default settings, fail to produce a
      feasible solution.

lp:degenmoves (degenmoves)
      Limit on the number of degenerate simplex moves -- for use when too much
      time is taken after solving the initial root relaxation of a MIP problem
      and before cut generation or root heuristics have started. Default -1
      ==> automatic choice.

lp:multprice_norm (multprice_norm, normadjust)
      Choice of norm used in multiple pricing:

      -1 - Automatic choice (default)
      0, 1, 2, 3 - Specific choices: hard to describe, but sometimes a
      specific choice will perform much better than the automatic choice.

lp:perturb (perturb)
      Magnitude of simplex perturbation (when needed; default 2e-4).

lp:pivtol (pivtol, markowitztol)
      Markowitz pivot tolerance (default 7.8125e-3).

lp:pricing (pricing)
      Pricing strategy:

      -1 - Automatic choice (default)
      0  - Partial pricing
      1  - Steepest edge
      2  - Devex
      3  - Quick-start steepest edge.

lp:quad (quad)
      Whether simplex should use quad-precision:

      -1 - Automatic choice (default)
      0  - No
      1  - Yes.

lp:sifting (sifting)
      Whether to use sifting within the dual simplex algorithm, which can be
      useful when there are many more variables than constraints:

      -1 - Automatic choice (default)
      0  - No
      1  - Yes, moderate
      2  - Yes, aggressive.

lp:siftmethod (siftmethod)
      Algorithm to use for sifting with the dual simplex method:

      -1 - Automatic choice (default)
      0  - Primal simplex
      1  - Dual simplex
      2  - Barrier.

mip:basis (fixmodel, mip:fix)
      Whether to compute duals / basis / sensitivity for MIP models:

      0 - No (default)
      1 - Yes.

mip:bestbndstop (bestbndstop)
      Stop once the best bound on the objective value is at least as good as
      this value.

mip:bestbound (bestbound, return_bound)
      Whether to return suffix .bestbound for the best known MIP dual bound on
      the objective value:

      0 - No (default)
      1 - Yes.

      The suffix is on the objective and problem and is -Infinity for
      minimization problems and +Infinity for maximization problems if there
      are no integer variables or if a dual bound is not available.

mip:bestobjstop (bestobjstop)
      Stop after a feasible solution with objective value at least as good as
      this value has been found.

mip:branchdir (branchdir)
      Which child node to explore first when branching:

      -1 - Explore "down" branch first
      0  - Explore "most promising" branch first (default)
      1  - Explore "up" branch first.

mip:disconnected (disconnected)
      Whether to exploit independent MIP sub-models:

      -1 - Automatic choice (default)
      0  - No
      1  - Moderate effort
      2  - Aggressive effort.

mip:fixedmethod (fixedmethod)
      Value of "method" to use when seeking a basis for MIP problems when
      "mip:basis=1". Default: if "method" is 0 or 1 then "method" else 1.

mip:focus (mipfocus)
      MIP solution strategy:

      0 - Balance finding good feasible solutions and proving optimality
          (default)
      1 - Favor finding feasible solutions
      2 - Favor providing optimality
      3 - Focus on improving the best objective bound.

mip:gap (mipgap)
      Max. relative MIP optimality gap (default 1e-4).

mip:gapabs (mipgapabs)
      Max. absolute MIP optimality gap (default 1e-10).

mip:heurfrac (heurfrac)
      Fraction of time to spend in MIP heuristics (default 0.05).

mip:improvegap (improvegap)
      Optimality gap below which the MIP solver switches from trying to
      improve the best bound to trying to find better feasible solutions
      (default 0).

mip:improvetime (improvetime)
      Execution seconds after which the MIP solver switches from trying to
      improve the best bound to trying to find better feasible solutions
      (default Infinity).

mip:impstartnodes (impstartnodes)
      Number of MIP nodes after which the solution strategy will change from
      improving the best bound to finding better feasible solutions (default
      Infinity).

mip:intfeastol (intfeastol)
      Feasibility tolerance for integer variables (default 1e-05).

mip:intfocus (integralityfocus, intfocus)
      Setting this parameter to 1 requests the solver to work harder at
      finding solutions that are still (nearly) feasible when all integer
      variables are rounded to exact integral values to avoid numerical issues
      such as trickle flow:

      0 - No (default)
      1 - Yes.

mip:lazy (lazy)
      Whether to recognize suffix .lazy on constraints: sum of

      1 - Accept .lazy>0 values (true lazy constraints, if supported)
      2 - Accept .lazy<0 values (user cuts, if supported)

      Default lazy = 3 ==> accept both.

      For Gurobi, lazy/user constraints are indicated with .lazy values of -1,
      1, 2, or 3 and are ignored until a solution feasible to the remaining
      constraints is found. What happens next depends on the value of .lazy:

      -1 - Treat the constraint as a user cut; the constraint must be
      redundant with respect to the rest of the model, although it can cut off
      LP solutions;
      1 - The constraint may still be ignored if another lazy constraint cuts
      off the current solution;
      2 - The constraint will henceforth be enforced if it is violated by the
      current solution;
      3 - The constraint will henceforth be enforced.

mip:nodemethod (nodemethod)
      Algorithm used to solve relaxed MIP node problems:

      -1 - Automatic choice (default)
      0  - Primal simplex
      1  - Dual simplex
      2  - Barrier.

mip:norelheurtime (norelheurtime)
      Limits the amount of time (in seconds) spent in the NoRel heuristic; see
      the description of "norelheurwork" for details. This parameter will
      introduce nondeterminism; use "norelheurwork" for deterministic results.
      Default 0.

mip:norelheurwork (norelheurwork)
      Limits the amount of work spent in the NoRel heuristic. This heuristic
      searches for high-quality feasible solutions before solving the root
      relaxation. The work metrix is hard to define precisely, as it depends
      on the machine. Default 0.

mip:opttol (opttol, optimalitytolerance)
      Dual feasibility tolerance.

mip:partition (partitionplace)
      Whether and how to use the .partition suffix on variables in the
      partition heuristic for MIP problems: sum of

      1 ==> When the branch-and-cut search ends
      2 ==> At nodes in the branch-and-cut search
      4 ==> After the root-cut loop
      8 ==> At the start of the root-cut loop
      16 ==> Before solving the root relaxation.

      Default = 15. Values of .parition determine how variables participate in
      the partition heuristic. Variables with

      .partition = -1 are always held fixed;
      .partition = 0 can vary in all sub-MIP models;
      .partition > 0 can vary only in in that sub-MIP model.

      The partition heuristic is only run when partition_place is between 1
      and 31 and some variables have suitable .partition suffix values.

mip:priorities (priorities)
      0/1*: Whether to read the branch and bound priorities from the .priority
      suffix.

mip:pumppasses (pumppasses)
      Number of feasibility-pump passes to do after the MIP root when no other
      root heuristoc found a feasible solution. Default -1 = automatic choice.

mip:return_gap (return_mipgap)
      Whether to return mipgap suffixes or include mipgap values (|objectve -
      .bestbound|) in the solve_message: sum of

      1 - Return .relmipgap suffix (relative to |obj|)
      2 - Return .absmipgap suffix (absolute mipgap)
      4 - Suppress mipgap values in solve_message.

      Default = 0. The suffixes are on the objective and problem. Returned
      suffix values are +Infinity if no integer-feasible solution has been
      found, in which case no mipgap values are reported in the solve_message.

mip:rins (rins)
      How often to apply the RINS heuristic for MIP problems:

      -1 - Automatic choice (default)
      0 - never
      n > 0 - every n-th node.

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

      With Gurobi, for problems with numerical issues such as trickle flow,
      option "mip:intfocus" can be more reliable.

mip:round_reptol (round_reptol)
      Tolerance for reporting rounding of integer variables to integer values;
      see "mip:round". Default = 1e-9.

mip:start (mipstart, intstart)
      Whether to use initial guesses in problems with integer variables:

      0 - No (overrides alg:start)
      1 - Yes (default)
      2 - No, but use the incoming primal values as hints (VARHINTVAL),
          ignoring the .hintpri suffix
      3 - Similar to 2, but use the .hintpri suffix on variables: larger
          (integer) values give greater priority to the initial value of the
          associated variable.

mip:symmetry (symmetry)
      MIP symmetry detection:

      -1 - Automatic choice (default)
      0  - No
      1  - Conservative
      2  - Aggressive.

mip:varbranch (varbranch)
      MIP branch variable selection strategy:

      -1 - Automatic choice (default)
      0  - Pseudo reduced - cost branching
      1  - Pseudo shadow - price branching
      2  - Maximum infeasibility branching
      3  - Strong branching.

miqcp:method (miqcpmethod)
      Method for solving mixed-integer quadratically constrained (MIQCP)
      problems:

      -1 - Automatic choice (default)
      0  - Solve continuous QCP relaxations at each node
      1  - Use linearized outer approximations.

obj:*:abstol (obj_*_abstol)
      Absolute tolerance for objective with index *. Can only be applied on a
      multi-objective problem with obj:multi=1

obj:*:method (obj_*_method)
      Method for objective with index *

obj:*:priority (obj_*_priority)
      Priority for objective with index *

obj:*:reltol (obj_*_reltol)
      Relative tolerance for objective with index *

obj:*:weight (obj_*_weight)
      Weight for objective with index *

obj:multi (multiobj)
      0*/1: Whether to do multi-objective optimization.
      When obj:multi = 1 and several objectives are present, suffixes
      .objpriority, .objweight, .objreltol, and .objabstol on the objectives
      are relevant. Objectives with greater .objpriority values (integer
      values) have higher priority. Objectives with the same .objpriority are
      weighted by .objweight. Objectives with positive .objabstol or
      .objreltol are allowed to be degraded by lower priority objectives by
      amounts not exceeding the .objabstol (absolute) and .objreltol
      (relative) limits. The objectives must all be linear. Objective-specific
      convergence tolerances and method values may be assigned via keywords of
      the form obj_n_<name>, such as obj_1_method for the first objective.

obj:multiobjmethod (multiobjmethod)
      Choice of optimization algorithm for lower-priority objectives:

      -1 - Automatic choice (default)
      0  - Primal simplex
      1  - Dual simplex
      2  - Ignore warm-start information; use the algorithm specified by the
           method keyword.

      The method keyword determines the algorithm to use for the highest
      priority objective.

obj:multiobjpre (multiobjpre)
      How to apply Gurobi's presolve when doing multi-objective optimization:

      -1 - Automatic choice (default)
      0  - Do not use Gurobi's presolve
      1  - Conservative presolve
      2  - Aggressive presolve, which may degrade lower priority objectives.

obj:no (objno)
      Objective to optimize:

      0 - None
      1 - First (default, if available)
      2 - Second (if available), etc.

obj:scale (objscale)
      How to scale the objective:

      0 - Automatic choice (default)
      -1..0 - Divide by max abs. coefficient raised to this power
      >0 - Divide by this value.

pre:aggfill (aggfill)
      Amount of fill allowed during aggregation in presolve(default -1).

pre:aggregate (aggregate)
      0/1*: whether to use aggregation in presolve.Setting it to 0 can
      sometimes reduce numerical errors.

pre:deprow (predeprow)
      Whether Gurobi's presolve should remove linearly dependent
      constraint-matrix rows:

      -1 - Only for continuous models (default)
      0  - Never
      1  - For all models.

pre:dual (predual)
      Whether Gurobi's presolve should form the dual of a continuous model:

      -1 - Automatic choice (default)
      0  - No
      1  - Yes
      2  - Form both primal and dual and use two threads to choose
           heuristically between them.

pre:dualreductions (dualreductions)
      Whether Gurobi's presolve should use dual reductions, which may be
      useful on a well-posed problem but can prevent distinguishing whether a
      problem is infeasible or unbounded:

      0 - No
      1 - Yes (default.)

pre:miqcpform (premiqcpform)
      For mixed-integer quadratically constrained (MIQCP) problems, how Gurobi
      should transform quadratic constraints:

      -1 - Automatic choice (default)
      0  - Retain MIQCP form
      1  - Transform to second-order cone contraints
      2  - Transform to rotated cone constraints.

      Choices 0 and 1 work with general quadratic constraints. Choices 1 and 2
      only work with constraints of suitable forms.

pre:passes (prepasses)
      Limit on the number of Gurobi presolve passes:

      -1 - Automatic choice (default)
      n>=0 - At most n passes.

pre:qlinearize (preqlinearize, preqlin)
      How Gurobi's presolve should treat quadratic problems:

      -1 - Automatic choice (default)
      0  - Do not modify the quadratic part(s)
           			 1 or 2 = try to linearize quadratic parts:
      1  - Focus on a strong LP relaxation
      2  - Focus on a compact LP relaxation.

pre:scale (scale)
      Whether to scale the problem:

      -1 - Automatic choice (default)
      0  - No
      1  - Yes
      2  - Yes, more aggressively
      3  - Yes, even more aggressively.

      Scaling typically reduces solution times, but it may lead to larger
      constraint violations in the original, unscaled model. Choosing a
      different scaling option can sometimes improve performance for
      particularly numerically difficult models.

pre:solve (presolve)
      Whether to use Gurobi's presolve:

      -1 - Automatic choice (default)
      0  - No
      1  - Conservative
      2  - Aggressive.

pre:sos1bigm (presos1bigm)
      Big-M for converting SOS1 constraints to binary form:

      -1 - Automatic choice (default)
      0 - No conversion

      Large values (e.g., 1e8) may cause numeric trouble.

pre:sos2bigm (presos2bigm)
      Big-M for converting SOS2 constraints to binary form:

      -1 - Automatic choice (default)
      0 - No conversion

      Large values (e.g., 1e8) may cause numeric trouble.

pre:sparsify (presparsify)
      Whether Gurobi's presolve should use its "sparsify reduction", which
      sometimes gives significant problem-size reductions:

      -1 - Automatic choice (default)
      0  - No
      1  - Yes.

qcp:dual (qcpdual)
      Whether to compute dual variables when the problem has quadratic
      constraints (which can be expensive):

      0 - No (default)
      1 - Yes.

qp:nonconvex (nonconvex)
      How to handle non-convex quadratic objectives and constraints:

      -1 - Default choice (currently the same as 1)
      0  - Complain about nonquadratic terms
      1  - Complain if Gurobi's presolve cannot discard or eliminate
           nonquadratic terms
      2  - Translate quadratic forms to bilinear form and use spatial
           branching.

qp:psdtol (psdtol)
      Maximum diagonal perturbation to correct indefiniteness in quadratic
      objectives (default 1e-6).

sol:count (countsolutions)
      0*/1: Whether to count the number of solutions and return it in the
      ".nsol" problem suffix. The number and kind of solutions are controlled
      by the sol:pool... parameters. Value 1 implied by sol:stub.

sol:poolgap (ams_eps, poolgap)
      Relative tolerance for reporting alternate MIP solutions (default:
      Infinity, no limit).

sol:poolgapabs (ams_epsabs, poolgapabs)
      Absolute tolerance for reporting alternate MIP solutions (default:
      Infinity, no limit).

sol:poollimit (ams_limit, poollimit, solnlimit)
      Limit on the number of alternate MIP solutions written. Default: 10.

sol:poolmode (ams_mode, poolmode)
      Search mode for MIP solutions when sol:stub/sol:count are specified to
      request finding several alternative solutions:

sol:stub (ams_stub, solstub, solutionstub)
      Stub for alternative MIP solutions, written to files with names obtained
      by appending "1.sol", "2.sol", etc., to <solutionstub>. The number of
      such files written is affected by the keywords poolgap, poolgapabs,
      poollimit, and poolmode. The number of alternative MIP solution files
      written is returned in suffix .nsol on the problem.

tech:cloudid (cloudid)
      Use Gurobi Instant Cloud with this "accessID".

tech:cloudkey (cloudkey)
      Use Gurobi Instant Cloud with this "secretKey". Both cloudid and
      cloudkey are required.

tech:cloudpool (cloudpool)
      Optional "machine pool" to use with Gurobi Instant Cloud.

tech:cloudpriority (cloudpriority)
      Priority of Cloud job, an integer >= -100 and <= 100. Default 0. Jobs
      with priority 100 run immediately -- use caution when specifying this
      value.

tech:concurrentmip (concurrentmip)
      How many independent MIP solves to allow at once when multiple threads
      are available. Optimization terminates when the first solve completes.
      The available threads are divided as evenly as possible among the
      concurrent solves. Default = 1.

      See also "tech:distmip", "tech:pooljobs".

tech:debug (debug)
      0*/1: whether to assist testing & debugging, e.g., by outputting
      auxiliary information.

tech:distmip (pool_distmip, distmip)
      Enables distributed MIP. A value of n causes the MIP solver to divide
      the work of solving a MIP model among n machines. Use the "tech:server"
      parameter to indicate the name of the cluster where you would like your
      distributed MIP job to run (or use "tech:workerpool" if your client
      machine will act as manager and you just need a pool of workers).
      Default = 0.

      See also "tech:concurrentmip", "tech:pooljobs".

tech:exportfile (writeprob, writemodel, exportfile)
      Specifies the name of a file where to export the model before solving
      it. This file name can have extension ".lp", ".mps", etc. Default = ""
      (don't export the model).

tech:logfile (logfile)
      Log file name.

tech:logfreq (logfreq, outfreq)
      Interval in seconds between log lines (default 5).

tech:nodefiledir (nodefiledir)
      Directory where MIP tree nodes are written after memory for them exceeds
      "nodefilestart"; default "."

tech:nodefilestart (nodefilestart)
      Gigabytes of memory to use for MIP tree nodes; default = Infinity (no
      limit, i.e., no node files written).

tech:optionfile (optionfile, option:file)
      Name of solver option file. Lines that start with # are ignored.
      Otherwise, each nonempty line should contain "name=value".

tech:outlev (outlev)
      0*/1: Whether to write gurobi log lines (chatter) to stdout and to file.

tech:param (param)
      General way to specify values of both documented and undocumented Gurobi
      parameters; value should be a quoted string (delimited by ' or ")
      containing a parameter name, a space, and the value to be assigned to
      the parameter. Can appear more than once. Cannot be used to query
      current parameter values.

tech:param:read (param:read, paramfile)
      Name of Gurobi parameter file (surrounded by 'single' or "double" quotes
      if the name contains blanks). The suffix on a parameter file should be
      .prm, optionally followed by .zip, .gz, .bz2, or .7z.

      Lines that start with # are ignored. Otherwise, each nonempty line
      should contain a name and a value, separated by a space.

tech:param:write (param:write)
      Name of Gurobi parameter file (surrounded by 'single' or "double" quotes
      if the name contains blanks) to be written.

tech:pooljobs (pool_jobs, pooljobs)
      Enables distributed concurrent optimization, which can be used to solve
      LP or MIP models on multiple machines. A value of n causes the solver to
      create n independent models, using different parameter settings for
      each. Each of these models is sent to a distributed worker for
      processing. Optimization terminates when the first solve completes. Use
      the "tech:server" parameter to indicate the name of the cluster where
      you would like your distributed concurrent job to run (or use
      "tech:workerpool" if your client machine will act as manager and you
      just need a pool of workers). Default = 0.

      See also "tech:concurrentmip", "tech:distmip".

tech:resultfile (resultfile)
      Name of a file of extra information written after completion of
      optimization. The name's suffix determines what is written:

      .sol - Solution vector
      .bas - Simplex basis
      .mst - Integer variable solution vector
      .ilp - IIS for an infeasible model
      .mps, .rew, .lp, or .rlp - To capture the original model.

      The file suffix may optionally be followed by .gz, .bz2, or .7z, which
      produces a compressed result.

tech:seed (seed)
      Random number seed (default 0), affecting perturbations that may
      influence the solution path.

tech:server (server, servers)
      Comma-separated list of Gurobi Compute Servers, specified either by name
      or by IP address. Default: run Gurobi locally (i.e., do not use a remote
      Gurobi server).

tech:server_group (server_group)
      Name of Compute Server Group, if any.

tech:server_insecure (server_insecure)
      Whether to user "insecure mode" with the Gurobi Compute Server. Should
      be left at default value (0) unless an administrator specifies another
      value.

tech:server_lic (serverlic, server_lic)
      Synonym for tech:optionfile.

tech:server_password (server_password)
      Password (if needed) for specified Gurobi Compute Server(s).

tech:server_priority (server_priority)
      Priority for Gurobi Compute Server(s). Default = 0. Highest priority =
      100.

tech:server_router (server_router)
      Name or IP address of router for Compute Server, if any.

tech:server_timeout (server_timeout)
      Report job as rejected by Gurobi Compute Server if the job is not
      started within server_timeout seconds. Default = 10.

tech:threads (threads)
      How many threads to use when using the barrier algorithm or solving MIP
      problems; default 0 ==> automatic choice.

tech:timing (timing)
      0*/1: Whether to display timings for the run.

tech:tunebase (tunebase)
      Base name for results of running Gurobi's search for best parameter
      settings. The search is run only when tunebase is specified. Results are
      written to files with names derived from tunebase by appending ".prm" if
      ".prm" does not occur in tunebase and inserting _1_, _2_, ... (for the
      first, second, ... set of parameter settings) before the right-most
      ".prm". The file with _1_ inserted is the best set and the solve results
      returned are for this set. In a subsequent "solve;", you can use
      "tech:param:read=..." to apply the settings in results file ... .

tech:tunejobs (pool_tunejobs, tunejobs)
      Enables distributed parallel tuning, which can significantly increase
      the performance of the tuning tool. A value of n causes the tuning tool
      to distribute tuning work among n parallel jobs. These jobs are
      distributed among a set of machines. Use the "tech:workerpool" parameter
      to provide a distributed worker cluster. Default = 0.

      Note that distributed tuning is most effective when the worker machines
      have similar performance.

tech:tuneoutput (tuneoutput)
      Amount of tuning output when tunebase is specified:

      0 - None
      1 - Summarize each new best parameter set
      2 - Summarize each set tried (default)
      3 - Summary plus detailed solver output for each trial.

tech:tuneresults (tuneresults)
      Limit on the number of tuning result files to write when tunerbase is
      specified. The default (-1) is to write results for all parameter sets
      on the efficient frontier.

tech:tunetimelim (tunetimelim, lim:tunetime)
      Time limit (in seconds) on tuning when tunebase is specified. Default -1
      ==> automatic choice of time limit.

tech:tunetrials (tunetrials)
      Number of trials for each parameter set when tunebase is specified, each
      with a different random seed value. Default = 3.

tech:version (version)
      Single-word phrase: report version details before solving the problem.

tech:wantsol (wantsol)
      In a stand-alone invocation (no "-AMPL" on the command line), what
      solution information to write. Sum of

      1 - Write ".sol" file
      2 - Primal variables to stdout
      4 - Dual variables to stdout
      8 - Suppress solution message.

tech:workerpassword (pool_password)
      Password for the worker pool (if needed).

tech:workerpool (pool_servers)
      When using a distributed algorithm (distributed MIP, distributed
      concurrent, or distributed tuning), this parameter allows you to specify
      a Remote Services cluster that will provide distributed workers. You
      should also specify the access password for that cluster, if there is
      one, in the "workerpassword" parameter. Note that you don't need to set
      either of these parameters if your job is running on a Compute Server
      node and you want to use the same cluster for the distributed workers.

      You can provide a comma-separated list of machines for added robustness.

```

