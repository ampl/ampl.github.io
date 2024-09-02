
# HiGHS Options

```ampl
ampl: option solver highs; # change the solver
ampl: option highs_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

Solver options obtained with `$ highs -=`.

```
HIGHS Optimizer Options for AMPL
--------------------------------------------

To set these options, assign a string specifying their values to the AMPL
option "highs_options". For example:

   ampl: option highs_options 'relgaptol=1e-6';

 Options:

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

alg:dualfeastol (dualfeastol, dual_feasibility_tolerance)
      Dual feasibility tolerance (default 1e-7).

alg:feastol (feastol, primal_feasibility_tolerance)
      Primal feasibility tolerance (default 1e-7).

alg:infinitebound (infinitebound, infinite_bound)
      Limit on |constraint bound|: values larger than this will be treated as
      infinite (default: 1e20).

alg:infinitecoeff (infinitecoeff, large_matrix_value)
      Upper limit on |matrix entries|: values larger than this will be treated
      as infinite (default: 1e15).

alg:infinitecost (infinitecost, infinite_cost)
      Limit on cost coefficient : values larger than this will be treated as
      infinite (default: 1e20).

alg:ipmopttol (ipmopttol, ipm_optimality_tolerance)
      IPM optimality tolerance (default 1e-8).

alg:method (method, lpmethod, solver)
      Which algorithm to use :

      choose  - Automatic (default)
      simplex - Simplex
      ipm     - Interior Point Method
      pdlp    - cuPDLP-c solver

alg:parallel (parallel)
      Parallel option :

      choose - Automatic (default)
      off    - Off
      on     - On

alg:pdlpdgaptol (pdlpdgaptol, pdlp_d_gap_tol)
      Duality gap tolerance for PDLP solver (default 1e-4).

alg:rays (rays)
      Whether to return suffix .unbdd if the objective is unbounded or suffix
      .dunbdd if the constraints are infeasible:

      0 - Neither
      1 - Just .unbdd
      2 - Just .dunbdd
      3 - Both (default)

alg:relax (relax)
      0*/1: Whether to relax integrality of variables.

alg:simplex (simplex, simplex_strategy)
      Strategy for simplex solver :

      0 - Choose automatically (default)
      1 - Dual (serial)
      2 - Dual ('PAMI' - Parallelization Across Multiple Iterations)
      3 - Dual ('SIP' - Single Iteration Parallelism
      4 - Primal

alg:simplexcrash (simplexcrash, simplex_crash_strategy)
      Simplex crash strategy :

      0 - Off (default)
      1 - LTSSF
      2 - Bixby

alg:simplexdualedge (simplexdualedge, simplex_dual_edge_weight_strategy)
      Simplex dual edge weights strategy :

      -1 - Choose automatically (default)
      0  - Dantzig
      1  - Devex
      2  - Steepest

alg:simplexprimaledge (simplexprimaledge, simplex_primal_edge_weight_strategy)
      Simplex primal edge weights strategy :

      -1 - Choose automatically (default)
      0  - Dantzig
      1  - Devex
      2  - Steepest

alg:simplexscale (simplexscale, simplex_scale_strategy)
      Simplex scaling strategy :

      0 - Off
      1 - Choose automatically (default)
      2 - Equilibration
      3 - Forced equilibration
      4 - Max value 0
      5 - Max value 1

alg:start (warmstart)
      Whether to use incoming primal (and dual, for LP) variable values in a
      warmstart:

      0 - No
      1 - Yes (for LP: if there is no incoming alg:basis) (default)
      2 - Yes (for LP: ignoring the incoming alg:basis, if any.)

alg:zerocoeff (zerocoeff, small_matrix_value)
      Lower limit on |matrix entries|: values smaller than this will be
      treated as zero (default: 1e-9).

bar:crossover (run_crossover)
      Run crossover after IPM to get a basic solution

cvt:bigM (cvt:bigm, cvt:mip:bigM, cvt:mip:bigm)
      Default value of big-M for linearization of logical constraints. Not
      used by default. Use with care (prefer tight bounds). Should be smaller
      than (1.0 / [integrality tolerance])

cvt:expcones (expcones)
      0*/1: Recognize exponential cones.

cvt:mip:eps (cvt:cmp:eps, cmp:eps)
      Tolerance for strict comparison of continuous variables for MIP. Applies
      to <, >, and != operators. Also applies to negation of conditional
      comparisons: b==1 <==> x<=5 means that with b==0, x>=5+eps. Default:
      1e-4.

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
      0/1*: Preprocess reified equality comparison's boolean result bounds.

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

      Default: 1+4. That is, 2-term binary products which are not part of a
      higher-order binary product, are not logicalized by default.

      Bits 2 or 4 imply bit 1.

cvt:quadcon (passquadcon)
      Convenience option. Set to 0 to disable quadratic constraints. Synonym
      for acc:quad..=0. Currently this disables out-multiplication of
      quadratic terms, then they are linearized.

cvt:quadobj (passquadobj)
      0/1*: Multiply out and pass quadratic objective terms to the solver, vs.
      linear approximation.

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
      0/1*: Whether to honor SOS2 constraints for nonconvex piecewise-linear
      terms, using suffixes .sos and .sosref provided by AMPL.

cvt:uenc:negctx:max (uenc:negctx:max, uenc:negctx)
      If cvt:uenc:ratio applies, max number of constants in comparisons
      x==const in negative context (equivalently, x!=const in positive
      context) to skip UEnc(x). Default 1.

cvt:uenc:ratio (uenc:ratio)
      Min ratio (ub-lb)/Nvalues to skip unary encoding for a variable x, where
      Nvalues is the number of constants used in conditional comparisons
      x==const. Instead, indicator constraints (or big-Ms) are used, if
      uenc:negctx also applies. Default 0.

lim:improvingsols (improvingsolslimit, mip_max_improving_sols)
      Maximum number of improving solutions found (default: no limit).

lim:ipmiterationlimit (ipmiterationlimit, ipm_iteration_limit)
      Limit on IPM iterations (default: no limit).

lim:leavenodes (leaveslim, mip_max_leaves)
      Maximum MIP number of leaf nodes (default: no limit).

lim:nodes (nodelim, nodelimit, mip_max_nodes)
      Maximum MIP nodes to explore (default: no limit).

lim:objectivebound (objective_bound, objectivebound)
      Objective bound for termination of the dual simplex solver (default: no
      limit).

lim:objectivetarget (objective_target, objectivetarget)
      Objective target for termination of the MIP solver (default: no limit).

lim:pdlpiterationlimit (pdlpiterationlimit, pdlp_iteration_limit)
      Iteration limit for PDLP solver (default: no limit).

lim:pdlpnativetermination (pdlp_native_termination, pdlpnativetermination)
      Use native termination for PDLP solver:

      0 - No (default)
      1 - Yes.

lim:simplexiterationlimit (simplexiterationlimit, simplex_iteration_limit)
      Limit on simplex iterations (default: no limit).

lim:stallnodes (stallnodelim, stallnodelimit, mip_max_stall_nodes)
      Maximum MIP number of nodes where estimate is above cutoff bound
      (default: no limit).

lim:time (timelim, timelimit, time_limit)
      Limit on solve time (in seconds; default: no limit).

mip:absgaptol (absgaptol, mip_abs_gap)
      Tolerance on absolute gap of MIP, |ub-lb|, to determine whether
      optimality has been reached for a MIP instance (default 1e-06).

mip:bestbound (bestbound, return_bound)
      Whether to return suffix .bestbound for the best known MIP dual bound on
      the objective value:

      0 - No (default)
      1 - Yes.

      The suffix is on the objective and problem and is -Infinity for
      minimization problems and +Infinity for maximization problems if there
      are no integer variables or if a dual bound is not available.

mip:detsimmetry (detsimmetry, mip_detect_symmetry)
      Whether symmetry should be detected (default 1)

mip:heureff (heureff, mip_heuristic_effort)
      Fraction of time to spend in MIP heuristics (default 0.05).

mip:intfeastol (intfeastol, inttol, mip_feasibility_tolerance)
      Feasibility tolerance for integer variables (default 1e-06).

mip:lpagelimit (lpagelimit, mip_lp_age_limit)
      Maximal age of dynamic LP rows before they are removed from the LP
      relaxation (default 10)

mip:mincliquetable (mincliquetable, mip_min_cliquetable_entries_for_parallelism)
      Minimal number of entries in the cliquetable before neighborhood queries
      of the conflict graph use parallel processing(default 100000)

mip:poolsoftlimit (poolsoftlimit, mip_pool_soft_limit)
      Soft limit on the number of rows in the cutpool for dynamic age
      adjustment(default 10000)

mip:pscostreliability (pscostreliability, mip_pscost_minreliable)
      Minimal number of observations before pseudo costs are considered
      reliable(default 8)

mip:relgaptol (relgaptol, mip_rel_gap)
      Tolerance on relative gap, | ub - lb|/|ub | , to determine whether
      optimality has been reached for a MIP instance (default 1e-04).

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

pre:centring (run_centring, centring)
      Perform centring steps or not:

      0 - No (default)
      1 - Yes.

pre:centringratiotolerance (centring_ratio_tolerance, centringratiotolerance)
      Centring stops when the ratio max(x_j*s_j) / min(x_j*s_j) is below this
      tolerance (default 100).

pre:maxcentringsteps (max_centring_steps, maxcentringsteps)
      Maximum number of steps to use when computing the analytic centre
      (default 5).

pre:pdlpscaling (pdlp_scaling, pdlpscaling)
      Scaling option for PDLP solver:

      0 - No
      1 - Yes (default)

pre:solve (presolve)
      Whether to use presolve:

      choose - Automatic (default)
      off    - Off
      on     - On

pre:userboundscale (user_bound_scale, userboundscale)
      Exponent of power-of-two bound scaling for model (default 0).

pre:usercostscale (user_cost_scale, usercostscale)
      Exponent of power-of-two cost scaling for model (default 0).

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

tech:debug (debug)
      0*/1: whether to assist testing & debugging, e.g., by outputting
      auxiliary information.

tech:logfile (logfile)
      Log file name.

tech:miploglev (miploglev, mip_report_level)
      0/1*/2: MIP solver report level

tech:optionfile (optionfile, option:file)
      Name of an AMPL solver option file to read (surrounded by 'single' or
      "double" quotes if the name contains blanks). Lines that start with #
      are ignored. Otherwise, each nonempty line should contain "name=value",
      e.g., "lim:iter=500".

tech:outlev (outlev)
      0*/1: Whether to write HighS log lines (chatter) to stdout and to file.

tech:threads (threads)
      How many threads to use when using the barrier algorithm or solving MIP
      problems; default 0 ==> automatic choice.

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

tech:writemodel (writeprob, writemodel, tech:exportfile)
      Specifies files where to export the model before solving (repeat the
      option for several files.) File name extensions can be ".lp[.7z]",
      ".mps", etc.

tech:writemodelonly (justwriteprob, justwritemodel)
      Specifies files where to export the model, no solving (option can be
      repeated.) File extensions can be ".dlp", ".mps", etc.

tech:writesolution (writesol, writesolution)
      Specifies the names of files where to export the solution and/or other
      result files in solver's native formats. Option can be repeated. File
      name extensions can be ".sol[.tar.gz]", ".json", ".bas", ".ilp", etc.
```

