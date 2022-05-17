
# HiGHS for AMPL Options

Obtained with `$ highs -=`.

```

HiGHS Optimizer Options for AMPL
--------------------------------------------

To set these options, assign a string specifying their values to the AMPL
option "highs_options". For example:

   ampl: option highs_options 'relgaptol=1e-6';

Options:

alg:basis (basis)
      Whether to use or return a basis:

      0 - No
      1 - Use incoming basis (if provided)
      2 - Return final basis
      3 - Both (1 + 2 = default.)

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
      IMP optimality tolerance (default 1e-8).

alg:method (method, lpmethod)
      Which algorithm to use :

      choose  - Automatic (default)
      simplex - Simplex
      ipm     - Interior point method

alg:parallel (parallel)
      Parallel option :

      choose - Automatic (default)
      off    - Off
      on     - On

alg:relax (relax)
      0*/1: Whether to relax integrality of variables.

alg:simplex (simplex, simplex_strategy)
      Strategy for simplex solver :

      0 - Choose automatically (default)
      1 - Dual (serial)
      2 - Dual (PAMI)
      3 - Dual (SIP)
      4 - Primal

alg:simplexcrash (simplexcrash, simplex_crash_strategy)
      Simplex crah strategy :

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
      2 - Equlibration
      3 - Forced equilibration
      4 - Max value 0
      5 - Max value 1

alg:zerocoeff (zerocoeff, small_matrix_value)
      Lower limit on |matrix entries|: values smaller than this will be
      treated as zero (default: 1e-9).

cvt:mip:eps (cvt:cmp:eps)
      Tolerance for strict comparison of continuous variables for MIP. Ensure
      larger than the solver's feasibility tolerance.

cvt:pre:all
      0/1*: Set to 0 to disable all presolve in the flat converter.

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

lim:improvingsols (improvingsolslimit, mip_max_improving_sols)
      Maximum number of improving solutions found (default: no limit).

lim:ipmiterationlimit (ipmiterationlimit, ipm_iteration_limit)
      Limit on IPM iterations (default: no limit).

lim:leavenodes (leaveslim, mip_max_leaves)
      Maximum MIP number of leaf nodes (default: no limit).

lim:nodes (nodelim, nodelimit, mip_max_nodes)
      Maximum MIP nodes to explore (default: no limit).

lim:simplexiterationlimit (simplexiterationlimit, simplex_iteration_limit)
      Limit on simplex iterations (default: no limit).

lim:stallnodes (stallnodelim, stallnodelimit, mip_max_stall_nodes)
      Maximum MIP number of nodes where estimate is above cutoff bound
      (default: no limit).

lim:time (timelim, timelimit, time_limit)
      Limit on solve time (in seconds; default: no limit).

mip:absgaptol (absgaptol, mip_abs_gap)
      tolerance on absolute gap of MIP, |ub-lb|, to determine whether
      optimality has been reached for a MIP instance (default 1e-06).

mip:detsimmetry (detsimmetry, mip_detect_symmetry)
      Whether symmetry should be detected (default 1)

mip:heureff (heureff, mip_heuristic_effort)
      Fraction of time to spend in MIP heuristics (default 0.05).

mip:intfeastol (intfeastol, mip_feasibility_tolerance)
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
      tolerance on relative gap, | ub - lb|/|ub | , to determine whether
      optimality has been reached for a MIP instance (default 1e-04).

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

obj:no (objno)
      Objective to optimize:

      0 - None
      1 - First (default, if available)
      2 - Second (if available), etc.

pre:solve (presolve)
      Whether to use presolve:

      choose - Automatic (default)
      off    - Off
      on     - On

tech:debug (debug)
      0*/1: whether to assist testing & debugging, e.g., by outputting
      auxiliary information.

tech:exportfile (writeprob)
      Specifies the name of a file where to export the model before solving
      it. This file name can have extension ".lp()", ".mps", etc. Default = ""
      (don't export the model).

tech:miploglev (miploglev, mip_report_level)
      0/1*/2: MIP solver report level

tech:optionfile (optionfile, option:file)
      Name of solver option file. Lines that start with # are ignored.
      Otherwise, each nonempty line should contain "name=value".

tech:outlev (outlev)
      0*/1: Whether to write HighS log lines (chatter) to stdout and to file.

tech:threads (threads)
      How many threads to use when using the barrier algorithm or solving MIP
      problems; default 0 ==> automatic choice.

tech:timing (timing)
      0*/1: Whether to display timings for the run.

tech:version (version)
      Single-word phrase: report version details before solving the problem.

tech:wantsol (wantsol)
      In a stand-alone invocation (no "-AMPL" on the command line), what
      solution information to write. Sum of

      1 - Write ".sol" file
      2 - Primal variables to stdout
      4 - Dual variables to stdout
      8 - Suppress solution message.