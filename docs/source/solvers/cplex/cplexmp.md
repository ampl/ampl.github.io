
# CPLEXMP Options

```ampl
ampl: option solver cplexmp; # change the solver
ampl: option cplexmp_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

Solver options obtained with `$ cplexmp -=`.

```
IBM ILOG CPLEX Optimizer Options for AMPL
--------------------------------------------

To set these options, assign a string specifying their values to the AMPL
option "cplex_options". For example:

   ampl: option cplex_options 'mipgap=1e-6';

 Options:

acc:indeq (acc:indlineq)
      Solver acceptance level for 'IndicatorConstraintLinEQ', default 1:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:indge (acc:indlinge)
      Solver acceptance level for 'IndicatorConstraintLinGE', default 1:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:indle (acc:indlinle)
      Solver acceptance level for 'IndicatorConstraintLinLE', default 1:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:linrange (acc:linrng)
      Solver acceptance level for 'LinConRange', default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:pl (acc:pwl, acc:piecewise)
      Solver acceptance level for 'PLConstraint', default 2:

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

alg:basis (basis)
      Whether to use or return a basis:

      0 - No
      1 - Use incoming basis (if provided)
      2 - Return final basis
      3 - Both (1 + 2 = default)

alg:feasrelax (feasrelax)
      Whether to modify the problem into a feasibility relaxation problem:

      0 = No (default)
      1 = Yes, minimizing the weighted sum of violations
      2 = Yes, minimizing the weighted sum of squared violations
      3 = Yes, minimizing the weighted count of violations
      4-6 = Same objective as 1-3, but also optimize the original objective,
      subject to the violation objective being minimized.

      Weights are given by suffixes .lbpen and .ubpen on variables and .rhspen
      on constraints (when nonnegative, default values = 0), else by keywords
      alg:lbpen, alg:ubpen, and alg:rhspen, respectively (default values = 1).
      Weights < 0 are treated as Infinity, allowing no violation.

alg:iisfind (iisfind, iis)
      Whether to find and export an IIS. Default = 0 (don't export).

alg:lbpen (lbpen)
      See alg:feasrelax.

alg:rays (rays)
      Whether to return suffix .unbdd if the objective is unbounded or suffix
      .dunbdd if the constraints are infeasible:

      0 - Neither
      1 - Just .unbdd
      2 - Just .dunbdd
      3 - Both (default)

alg:relax (relax)
      0*/1: Whether to relax integrality of variables.

alg:rhspen (rhspen)
      See alg:feasrelax.

alg:start (warmstart)
      Whether to use incoming primal (and dual, for LP) variable values in a
      warmstart:

      0 - No
      1 - Yes (for LP: if there is no incoming alg:basis) (default)
      2 - Yes (for LP: ignoring the incoming alg:basis, if any.)

alg:ubpen (ubpen)
      See alg:feasrelax.

cvt:bigM (cvt:bigm, cvt:mip:bigM, cvt:mip:bigm)
      Default value of big-M for linearization of logical constraints. Not
      used by default. Use with care (prefer tight bounds). Should be smaller
      than (1.0 / [integrality tolerance])

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

lim:time (timelim, timelimit)
      limit on solve time (in seconds; default: no limit).

mip:bestbound (bestbound, return_bound)
      Whether to return suffix .bestbound for the best known MIP dual bound on
      the objective value:

      0 - No (default)
      1 - Yes.

      The suffix is on the objective and problem and is -Infinity for
      minimization problems and +Infinity for maximization problems if there
      are no integer variables or if a dual bound is not available.

mip:gap (mipgap)
      Relative optimality gap |bestbound-bestinteger|/(1e-10+|bestinteger|).

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

obj:*:abstol (obj_*_abstol)
      Absolute tolerance for objective with index *. Can only be applied on a
      multi-objective problem with obj:multi=1

obj:*:priority (obj_*_priority)
      Priority for objective with index *

obj:*:reltol (obj_*_reltol)
      Relative tolerance for objective with index *

obj:*:weight (obj_*_weight)
      Weight for objective with index *

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

qp:target (optimalitytarget)
      Type of solution to compute for a QP problem

sol:chk:fail (chk:fail, checkfail)
      Fail on solution checking violations.

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

      Default: 1+2+16+512.

sol:chk:prec (chk:prec, chk:precision)
      AMPL solution_precision option when checking: number of significant
      digits.

sol:chk:round (chk:round, chk:rnd)
      AMPL solution_round option when checking: round to this number of
      decimals after comma (before comma if negative.)

sol:count (countsolutions)
      0*/1: Whether to count the number of solutions and return it in the
      ".nsol" problem suffix. The number and kind of solutions are controlled
      by the sol:pool... parameters. Value 1 implied by sol:stub.

sol:poolgap (ams_eps, poolgap)
      Relative tolerance for reporting alternate MIP solutions (default:
      1e75).

sol:poolgapabs (ams_epsabs, poolagap)
      Absolute tolerance for reporting alternate MIP solutions (default:
      1e75).

sol:poolintensity (poolintensity)
      How hard to try adding MIP solutions to the solution

      pool. Useful only if poolstub is specified.

      0 - Treated as 1 if poolstub is specified without populate, or 2 if
          populate is specified (default)
      3 - More additions to the solution pool
      4 - Tries to generate all MIP solutions and keep the best
          "sol:poollimit" ones.

sol:poollimit (ams_limit, poolcapacity, poollimit, solnlimit)
      Limit on the number of alternate MIP solutions written. Default:
      2100000000.

sol:poolmode (ams_mode, poolmode)
      Search mode for MIP solutions when sol:stub/sol:count are specified to
      request finding several alternative solutions. Overriden by sol:populate
      andsol:poolintensity. Values:

      0 - Just collect solutions during normal solve
      1 - Make some effort at finding additional solutions =>
          poolintensity=2, populate=1
      2 - Seek "sol:poollimit" best solutions (default) => poolintensity=2,
          populate=1

sol:poolpopulate (populate)
      Whether to run CPLEX's "populate" algorithm in an attempt to add more
      solutions to the MIP solution pool:

      0 - no; just keep solutions found during the initial solve
      1 - run "populate" after finding a MIP solution

sol:poolpopulatelim (populatelim)
      Limit on number of solutions added to the solution pool by the populate
      algorithm. Default: 20.

sol:poolreplace (poolreplace)
      Policy for replacing solutions in the solution pool if more than
      poolcapacity solutions are generated:

      0 - FIFO (first-in, first-out); default
      1 - Keep best solutions
      2 - Keep most diverse solutions

sol:stub (ams_stub, solstub, solutionstub)
      Stub for alternative MIP solutions, written to files with names obtained
      by appending "1.sol", "2.sol", etc., to <solutionstub>. The number of
      such files written is affected by the keywords poolgap, poolgapabs,
      poollimit, poolpopulatelim, poolpopulate, poolintensity and poolmode.
      The number of alternative MIP solution files written is returned in
      suffix .nsol on the problem.

tech:bardisplay (bardisplay)
      Specifies how much the barrier algorithm chatters:

      0 - no information (default)
      1 - balanced setup and iteration information
      2 - diagnostic information

tech:debug (debug)
      0*/1: whether to assist testing & debugging, e.g., by outputting
      auxiliary information.

tech:logfile (logfile)
      Log file name.

tech:lpdisplay (display, lpdisplay)
      Frequency of displaying LP progress information:

      0 - never (default)
      1 - each factorization
      2 - each iteration

tech:mipdisplay (mipdisplay)
      Frequency of displaying branch-and-bound information:

      0 - no node log displayed (default)
      1 - each integer feasible solution
      2 - every "mipinterval" nodes
      3 - same as 2 plus cutting planes info and info about new incumbents
          found through MIP starts
      4 - same as 3, plus LP root relaxation info (according to "display")
      5 - same as 4, plus LP subproblems (according to "display")

tech:mipinterval (mipinterval)
      Frequency of node logging for "tech::mipdisplay" >=2:

      0     - automatic (default)
      n > 0 - every n nodes and every incumbent
      n < 0 - new incumbents and less info the more negative n is

tech:optionfile (optionfile, option:file)
      Name of solver option file to read (surrounded by 'single' or "double"
      quotes if the name contains blanks). Lines that start with # are
      ignored. Otherwise, each nonempty line should contain "name=value".

tech:outlev (outlev)
      Whether to write CPLEX log lines (chatter) to stdout,for granular
      control see "tech:lpdisplay", "tech:mipdisplay",
      "tech:bardisplay".Values:

      0 - no output (default)
      1 - equivalent to "bardisplay"=1, "display"=1, "mipdisplay"=3
      2 - equivalent to "bardisplay"=2, "display"=2, "mipdisplay"=5

tech:threads (threads)
      How many threads to use when using the barrier algorithm
      or solving MIP problems; default 0 ==> automatic choice.

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

tech:writegraph (writegraph, exportgraph)
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

