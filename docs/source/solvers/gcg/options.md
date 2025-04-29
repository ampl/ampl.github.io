
# GCG Options

```ampl
ampl: option solver gcg; # change the solver
ampl: option gcg_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

Solver options obtained with `$ gcg -=`.

```
GCG Optimizer Options for AMPL
--------------------------------------------

To set these options, assign a string specifying their values to the AMPL
option "gcg_options". For example:

   ampl: option gcg_options 'mipgap=1e-6';

'' Options:

acc:_all
      Solver acceptance level for all constraints and expressions. Value
      meaning: as described in the specific acc:... options.

      Can be useful to disable all reformulations (acc:_all=2), or force
      linearization (acc:_all=0.)

acc:lineq
      Solver acceptance level for 'LinConEQ' as flat constraint, default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

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

acc:linrange (acc:linrng)
      Solver acceptance level for 'LinConRange' as flat constraint, default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

alg:basis (basis)
      Whether to use or return a basis:

      0 - No
      1 - Use incoming basis (if provided)
      2 - Return final basis
      3 - Both (1 + 2 = default)

alg:method (method, lpmethod)
      LP algorithm for solving initial LP relaxations:

      s - automatic simplex (default)
      p - primal simplex
      d - dual simplex
      b - barrier
      c - barrier with crossover

alg:relax (relax)
      0*/1: Whether to relax integrality of variables.

alg:remethod (remethod, relpmethod)
      LP algorithm for resolving LP relaxations if a starting basis exists:

      s - automatic simplex (default)
      p - primal simplex
      d - dual simplex
      b - barrier
      c - barrier with crossover

branch:preferbinary (preferbinary)
      0/1: whether branching on binary variables should be preferred

      0 - Binary variables should not be preferred on branching (default)

      1 - Binary variables should be preferred on branching.

cut:dircutoffdistweight (dircutoffdistweight)
      Weight of directed cutoff distance in cut score calculation (default:
      0.0)

cut:efficacyweight (efficacyweight)
      Weight of efficacy in cut score calculation (default: 1.0)

cut:intsupportweight (intsupportweight)
      Weight of integral support in cut score calculation (default: 0.1)

cut:maxcuts (maxcuts)
      Maximal number of cuts separated per separation round (0: disable local
      separation; default: 100)

cut:maxcutsroot (maxcutsroot)
      Maximal number of separated cuts at the root node (0: disable root node
      separation; default: 2000)

cut:maxrounds
      Maximal number of separation rounds per node (default: -1: unlimited)

cut:maxroundsroot
      Maximal number of separation rounds in the root node (default: -1:
      unlimited)

cut:maxstallrounds
      Maximal number of consecutive separation rounds without objective or
      integrality improvement in local nodes (-1: no additional restriction;
      default: 1)

cut:maxstallroundsroot
      Maximal number of consecutive separation rounds without objective or
      integrality improvement in the root node (-1: no additional restriction;
      default: 10)

cut:minactivityquot
      Minimum cut activity quotient to convert cuts into constraints during a
      restart (0.0: all cuts are converted; default: 0.8)

cut:minefficacy
      Minimal efficacy for a cut to enter the LP (default: 0.0001)

cut:minefficacyroot
      Minimal efficacy for a cut to enter the LP in the root node (default:
      0.0001)

cut:minortho (minortho)
      Minimal orthogonality for a cut to enter the LP (default: 0.9)

cut:minorthoroot (minorthoroot)
      Minimal orthogonality for a cut to enter the LP in the root node
      (default: 0.1)

cut:objparalweight (objparalweight)
      Weight of objective parallelism in cut score calculation (default: 0.1)

cut:poolfreq
      Separation frequency for the global cut pool (-1: disable global cut
      pool; 0: only separate pool at the root; default: 10)

cut:settings
      0/1/2/3: sets cuts settings

      0 - Sets cuts default (default)

      1 - Sets cuts aggressive

      2 - Sets cuts fast

      3 - Sets cuts off.

cvt:bigM (cvt:bigm, cvt:mip:bigM, cvt:mip:bigm)
      Default value of big-M for linearization of logical constraints. Not
      used by default. Use with care (prefer tight bounds). Should be smaller
      than (1.0 / [integrality tolerance])

cvt:dvelim (dvelim)
      Eliminate AMPL defined variables by substitution into linear, quadratic,
      and polynomial expressions:

      0 - Do not eliminate, always instantiate the variables.
      1 - Eliminate only those used 1x. This can increase model density but
          greatly simplifies some models.
      2 - Always substitute where possible, even if the variable needs to be
          instantiated for use in other places. Can introduce redundancy, but
          seems best for some models (default.)

      See also AMPL options linelim and substout.

cvt:expcones (expcones)
      0*/1: Recognize exponential cones.

cvt:mip:eps (cvt:cmp:eps, cmp:eps)
      Tolerance for strict comparison of continuous variables for MIP. Applies
      to <, >, and != operators. Also applies to negation of conditional
      comparisons: b==1 <==> x<=5 means that with b==0, x>=5+eps. Default:
      1e-4.

cvt:multoutcard (multoutcard)
      Up to which (estimated) QP matrix cardinality should a product of 2
      linear expressions be multiplied out. Default 1e9.

      Can speed up model input, but prone to numerical issues.

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

cvt:pre:eqbinary
      0/1*: Preprocess reified equality comparison with a binary variable.

cvt:pre:eqresult
      0/1*: Preprocess reified equality comparison's decidable cases.

cvt:pre:ineqresult
      0/1*: Preprocess reified inequality comparison's decidable cases.

cvt:pre:ineqrhs
      0/1*: Preprocess reified inequality comparison's right-hand sides.

cvt:pre:unnest
      0/1*: Inline nested expressions, currently Ands/Ors.

cvt:prod (cvt:pre:prod)
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

cvt:qp2passes (cvt:qp2pass, qp2passes, qp2pass)
      Parse sums of QP expressions in 2 passes. Usually faster. Default 1.

cvt:quadcon (passquadcon)
      Convenience option. Set to 0 to disable quadratic constraints. Synonym
      for acc:quad..=0. Currently this disables out-multiplication of
      quadratic terms, then they are linearized.

cvt:quadobj (passquadobj)
      0*/1: Pass quadratic objective terms to the solver. When 0, if the
      solver accepts quadratic constraints, such a constraint will be created
      with those, otherwise linearly approximated.

cvt:socp (socpmode, socp)
      Second-Order Cone recognition mode:

      0 - Do not recognize SOCP forms
      1 - Recognize from non-quadratic expressions only (sqrt, abs)
      2 - Recognize from quadratic and non-quadratic SOCP forms. Helpful if
          the solver does not recognize non-standard forms

      Recognized SOCP forms can be further converted to (SOCP-standardized)
      quadratic constraints, see cvt:socp2qc. Default: 0.

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

cvt:uenc:negctx:max (uenc:negctx:max, uenc:negctx)
      If cvt:uenc:ratio applies, max number of constants in comparisons
      x==const in negative context (equivalently, x!=const in positive
      context) to skip UEnc(x). Default 1.

cvt:uenc:ratio (uenc:ratio)
      Min ratio (ub-lb)/Nvalues to skip unary encoding for a variable x, where
      Nvalues is the number of constants used in conditional comparisons
      x==const. Instead, indicator constraints (or big-Ms) are used, if
      uenc:negctx also applies. Default 0.

det:benders-enabled (benders-enabled)
      0/1: whether benders detection should be enabled?

      0 - Benders detection not enabled (default)

      1 - Benders detection enabled.

det:benders-onlybinmaster (benders-onlybinmaster)
      0/1: whether only decomposition with only binary variables in the master
      are searched?

      0 - Not only decomposition with only binary variables in the master are
      searched (default)

      1 - Only decomposition with only binary variables in the master are
      searched.

det:benders-onlycontsubpr (benders-onlycontsubpr)
      0/1: whether only decomposition with only continiuous variables in the
      subproblems are searched?

      0 - Not only decomposition with only continiuous variables in the
      subproblems are searched (default)

      1 - Only decomposition with only continiuous variables in the
      subproblems are searched.

det:classification-enabled (classification-enabled)
      0/1: whether classification should be enabled?

      0 - Classification not enabled

      1 - Classification enabled (default).

det:enabled
      0/1: whether detection should be enabled?

      0 - Detection not enabled

      1 - Detection enabled (default).

det:maxnclassesperpartition (maxnclassesperpartition)
      Maximum number of classes per partition (default: 9)

det:maxnclassesperpartitionforlargeprobs (maxnclassesperpartitionforlargeprobs)
      Maximum number of classes per partition for large problems (nconss +
      nvars >= 50000) (default: 5)

det:maxrounds
      Maximum number of detection loop rounds (default: 1)

det:maxtime
      Maximum detection time in seconds (default: 600)

det:origprob-classificationenabled (origprob-classificationenabled)
      0/1: whether classification for the original problem should be enabled?

      0 - Classification for the original problem not enabled

      1 - Classification for the original problem enabled (default).

det:origprob-enabled (origprob-enabled)
      0/1: whether detection for the original problem should be enabled?

      0 - Detection for the original problem not enabled

      1 - Detection for the original problem enabled (default).

det:postprocess (postprocess)
      0/1: whether postprocessing of complete decompositions should be
      enabled?

      0 - Postprocessing of complete decompositions not enabled

      1 - Postprocessing of complete decompositions enabled (default).

det:scoretype (scoretype)
      Score calculation for comparing (partial) decompositions:

      maxwhi - max white
      border - border area
      classi - classic
      forswh - max foreseeing white
      spfwh  - ppc-max-white (default)
      fawh   - max foreseeing white with aggregation info
      spfawh - ppc-max-white with aggregation info
      bender - experimental benders score
      strong - strong decomposition score

gcg:aggregation
      0/1: whether identical blocks should be aggregated (only for
      discretization approach)?

      0 - Identical blocks should not be aggregated (only for discretization
      approach)

      1 - Identical blocks should be aggregated (only for discretization
      approach) (default).

gcg:bliss-enabled (bliss-enabled)
      0/1: whether bliss should be used to check for identical blocks?

      0 - Bliss should not be used to check for identical blocks

      1 - Bliss should be used to check for identical blocks (default).

gcg:discretization (discretization)
      0/1: whether discretization (TRUE) or convexification (FALSE) approach
      should be used?

      0 - convexification approach should be used

      1 - discretization approach should be used (default).

gcg:mipdiscretization (mipdiscretization)
      0/1: whether discretization (TRUE) or convexification (FALSE) approach
      should be used in mixed-integer programs?

      0 - convexification approach should be used in mixed-integer programs

      1 - discretization approach should be used in mixed-integer programs
      (default).

gcg:mode (mode)
      The decomposition mode that GCG will use:

      0 - Dantzig-Wolfe (default)
      1 - Benders' decomposition
      2 - No decomposition

heu:settings
      0/1/2/3: sets heuristics settings

      0 - Sets heuristics default (default)

      1 - Sets heuristics aggressive

      2 - Sets heuristics fast

      3 - Sets heuristics off.

lim:absgap (absgap)
      Solving stops, if the absolute gap = |primalbound - dualbound| is below
      the given value (default: 0.0)

lim:autorestartnodes
      If solve exceeds this number of nodes for the first time, an automatic
      restart is triggered (default: -1: no automatic restart)

lim:bestsol
      Solving stops, if the given number of solution improvements were found
      (default: -1: no limit)

lim:gap (gap)
      Solving stops, if the relative gap = |primal -
      dual|/MIN(|dual|,|primal|) is below the given value, the gap is
      'Infinity', if primal and dual bound have opposite signs (default: 0.0)

lim:maxorigsol
      Maximal number of solutions candidates to store in the solution storage
      of the original problem (default: 10)

lim:maxsol
      Maximal number of solutions to store in the solution storage (default:
      100)

lim:memory (memory)
      #maximal memory usage in MB; reported memory usage is lower than real
      memory usage! (default: 8796093022207.0)

lim:nodes
      Maximal number of nodes to process (default: -1: no limit)

lim:restarts
      Solving stops, if the given number of restarts was triggered (default:
      -1: no limit)

lim:solutions
      Solving stops, if the given number of solutions were found (default: -1:
      no limit)

lim:stallnodes
      Solving stops, if the given number of nodes was processed since the last
      improvement of the primal solution value (default: -1: no limit)

lim:time (timelim, timelimit, time_limit)
      Limit on solve time (in seconds; default: 1e+20).

lim:totalnodes
      Maximal number of total nodes (incl. restarts) to process (default: -1:
      no limit)

lp:alwaysgetduals (alwaysgetfarkasduals, alwaysgetduals)
      0/1: whether the Farkas duals should always be collected when an LP is
      found to be infeasible

      0 - The Farkas duals should not always be collected when an LP is found
      to be infeasible (default)

      1 - The Farkas duals should always be collected when an LP is found to
      be infeasible.

lp:presolving
      0/1: whether presolving of LP solver should be used

      0 - Presolving of LP solver should not be used

      1 - Presolving of LP solver should be used (default).

lp:pricing (pricing)
      Pricing strategy:

      l - lpi default (default)
      a - auto
      f - full pricing
      p - partial
      s - steepest edge pricing
      q - quickstart steepest edge pricing
      d - devex pricing

lp:solvedepth
      Maximal depth for solving LP at the nodes (default: -1: no depth limit)

lp:solvefreq
      Frequency for solving LP at the nodes (-1: never; 0: only root LP;
      default: 0)

lp:threads
      Number of threads used for solving the LP (default: 0: automatic)

mip:bestbound (bestbound, return_bound)
      Whether to return suffix .bestbound for the best known MIP dual bound on
      the objective value:

      0 - No (default)
      1 - Yes.

      The suffix is on the objective and problem and is -Infinity for
      minimization problems and +Infinity for maximization problems if there
      are no integer variables or if a dual bound is not available.

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

misc:allowstrongdualreds (allowstrongdualreds)
      0/1: whether strong dual reductions should be allowed in propagation and
      presolving

      0 - Strong dual reductions should not be allowed in propagation and
      presolving

      1 - Strong dual reductions should be allowed in propagation and
      presolving (default).

misc:allowweakdualreds (allowweakdualreds)
      0/1: whether weak dual reductions should be allowed in propagation and
      presolving

      0 - Weak dual reductions should not be allowed in propagation and
      presolving

      1 - Weak dual reductions should be allowed in propagation and presolving
      (default).

misc:scaleobj (scaleobj)
      0/1: whether the objective function should be scaled so that it is
      always integer

      0 - The objective function should not be scaled so that it is always
      integer

      1 - The objective function should be scaled so that it is always integer
      (default).

nod:childsel
      Child selection rule:

      d - down
      u - up
      p - pseudo costs
      i - inference
      l - lp value
      r - root LP value difference
      h - hybrid inference/root LP value difference (default)

num:checkfeastolfac (checkfeastolfac)
      Feasibility tolerance factor; for checking the feasibility of the best
      solution (default: 1.0)

num:dualfeastol (dualfeastol)
      Feasibility tolerance for reduced costs in LP solution (default: 1e-07)

num:epsilon (epsilon)
      Absolute values smaller than this are considered zero (default: 1e-09)

num:feastol (feastol)
      Feasibility tolerance for constraints (default: 1e-06)

num:infinity (infinity)
      Values larger than this are considered infinity (default: 1e+20)

num:lpfeastolfactor (lpfeastolfactor)
      Factor w.r.t. primal feasibility tolerance that determines default (and
      maximal) primal feasibility tolerance of LP solver (default: 1.0)

num:sumepsilon (sumepsilon)
      Absolute values of sums smaller than this are considered (default:
      1e-06)

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

obj:multi:weight (multiobjweight, obj:multi:weights, multiobjweights)
      How to interpret each objective's weight sign:

      1 - relative to the sense of the 1st objective
      2 - relative to its own sense (default)

      With the 1st option (legacy behaviour), negative .objweight for
      objective i would make objective i's sense the opposite of the model's
      1st objective. Otherwise, it would make objective i's sense the opposite
      to its sense defined in the model.

obj:no (objno)
      Objective to optimize:

      0 - None
      1 - First (default, if available)
      2 - Second (if available), etc.

par:maxnthreads (maxnthreads)
      Maximum number of threads used during parallel solve (default: 8)

par:minnthreads (minnthreads)
      Minimum number of threads used during parallel solve (default: 1)

par:mode (mode)
      0/1: Parallel optimisation mode

      0 - Opportunistic

      1 - Deterministic (default)

pre:abortfac (abortfac)
      Abort presolve, if at most this fraction of the problem was changed in
      last presolve round (default: 0.0008)

pre:clqtablefac (clqtablefac)
      Limit on number of entries in clique table relative to number of problem
      nonzeros (default: 2.0)

pre:donotaggr (donotaggr)
      0/1: whether aggregation of variables should be forbidden

      0 - Aggregation of variables should not be forbidden (default)

      1 - Aggregation of variables should be forbidden.

pre:donotmultaggr (donotmultaggr)
      0/1: whether multi-aggregation of variables should be forbidden

      0 - Multi-aggregation of variables should not be forbidden (default)

      1 - Multi-aggregation of variables should be forbidden.

pre:immrestartfac (immrestartfac)
      Fraction of integer variables that were fixed in the root node
      triggering an immediate restart with preprocessing (default: 0.1)

pre:maxrestarts
      Maximal number of restarts (default: -1: unlimited)

pre:maxrounds
      Maximal number of presolving rounds (default: -1: unlimited; 0: off)

pre:restartfac (restartfac)
      Fraction of integer variables that were fixed in the root node
      triggering a restart with preprocessing after root node evaluation
      (default: 0.025)

pre:restartminred (restartminred)
      Minimal fraction of integer variables removed after restart to allow for
      an additional restart (default: 0.1)

pre:settings
      0/1/2/3: sets presolvings settings

      0 - Sets presolvings default (default)

      1 - Sets presolvings aggressive

      2 - Sets presolvings fast

      3 - Sets presolvings off.

pre:subrestartfac (subrestartfac)
      Fraction of integer variables that were globally fixed during the
      solving process triggering a restart with preprocessing (default: 1.0)

pro:abortoncutoff
      0/1: whether propagation should be aborted immediately (setting this to
      0 could help conflict analysis to produce more conflict constraints)

      0 - Propagation should not be aborted immediately

      1 - Propagation should be aborted immediately (default).

pro:maxrounds
      Maximal number of propagation rounds per node (-1: unlimited; 0: off;
      default: 100)

pro:maxroundsroot
      Maximal number of propagation rounds in the root node (-1: unlimited; 0:
      off; default: 1000)

ran:lpseed (lpseed)
      Random seed for LP solver, e.g. for perturbations in the simplex
      (default: 0: LP default)

ran:permutationseed (permutationseed)
      Seed value for permuting the problem after reading/transformation
      (default: 0: no permutation)

ran:permuteconss (permuteconss)
      0/1: whether the order of constraints should be permuted (depends on
      permutationseed)?

      0 - Order of constraints should not be permuted

      1 - Order of constraints should be permuted (default).

ran:permutevars (permutevars)
      0/1: whether the order of variables should be permuted (depends on
      permutationseed)?

      0 - Order of variables should not be permuted (default)

      1 - Order of variables should be permuted.

ran:randomseedshift (randomseedshift)
      Global shift of all random seeds in the plugins and the LP random seed
      (default: 0)

sol:chk:fail (chk:fail, checkfail)
      Fail on MP solution check violations, with solve result 150.

sol:chk:feastol (sol:chk:eps, chk:eps, chk:feastol)
      Absolute tolerance to check objective values, variable and constraint
      bounds. Default 1e-6.

sol:chk:feastolrel (sol:chk:epsrel, chk:epsrel, chk:feastolrel)
      Relative tolerance to check objective values, variable and constraint
      bounds. Default 1e-6.

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

sol:report_uncertain (report_uncertain_sol)
      0/1*: whether to report objective value(s) in solve_message when
      solve_result is '?' (unknown).

sol:stub (solstub, solutionstub)
      Stub for solution files. If "solutionstub" is specified, found solutions
      are written to files ("solutionstub & '1' & '.sol'") ... ("solutionstub
      & Current.nsol & '.sol'"), where "Current.nsol" holds the number of
      returned solutions. That is, file names are obtained by appending 1, 2,
      ... "Current.nsol" to "solutionstub".

tech:debug (debug)
      0*/1: whether to assist testing & debugging, e.g., by outputting
      auxiliary information (mostly via suffixes).

tech:exportfile (writeprob, writemodel)
      Specifies the name of a file where to export the model before solving
      it. This file name can have extension ".lp", ".mps", etc. Default = ""
      (don't export the model).

tech:logfile (logfile)
      Log file name.

tech:optionfile (optionfile, option:file)
      Name of an AMPL solver option file to read (surrounded by 'single' or
      "double" quotes if the name contains blanks). Lines that start with #
      are ignored. Otherwise, each nonempty line should contain "name=value",
      e.g., "lim:iter=500".

tech:optionnativeread (optionnativeread, tech:param:read, param:read)
      Filename of GCG parameter file (as path).The suffix on a parameter file
      should be .set.

tech:outlev (outlev)
      0*/1: Whether to write GCG log lines (chatter) to stdout and to file.

tech:outlev-native (outlev-native)
      0*/1/2/3/4/5: Whether to write GCG log lines (chatter) to stdout and to
      file (native output level of SCIP).

tech:outlev_mp (outlev_mp)
      0*/1: whether to print MP model information.

tech:timing (timing, tech:report_times, report_times)
      0*/1/2: Whether to print and return timings for the run, all times are
      wall times. If set to 1, return the solution times in the problem
      suffixes 'time_solver', 'time_setup' and 'time', 'time'=
      time_solver+time_setup+time_output is a measure of the total time spent
      in the solver driver. If set to 2, return more granular times, including
      'time_read', 'time_conversion' and 'time_output'.

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
```

