
# COPT Options

```ampl
ampl: option solver copt; # change the solver
ampl: option copt_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

Solver options obtained with `$ copt -=`.

```
COPT Optimizer Options for AMPL
--------------------------------------------

To set these options, assign a string specifying their values to the AMPL
option "copt_options". For example:

   ampl: option copt_options 'mipgap=1e-6';

'' Options:

acc:_all
      Solver acceptance level for all constraints and expressions. Value
      meaning: as described in the specific acc:... options.

      Can be useful to disable all reformulations (acc:_all=2), or force
      linearization (acc:_all=0.)

acc:indeq (acc:indlineq)
      Solver acceptance level for 'IndicatorConstraintLinEQ' as flat
      constraint, default 1:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:indge (acc:indlinge)
      Solver acceptance level for 'IndicatorConstraintLinGE' as flat
      constraint, default 1:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:indle (acc:indlinle)
      Solver acceptance level for 'IndicatorConstraintLinLE' as flat
      constraint, default 1:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

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

acc:quadeq
      Solver acceptance level for 'QuadConEQ' as flat constraint, default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

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

alg:basis (basis)
      Whether to use or return a basis:

      0 - No
      1 - Use incoming basis (if provided)
      2 - Return final basis
      3 - Both (1 + 2 = default)

alg:dualfeastol (dualfeastol)
      Tolerance for dual solutions and reduced cost (default 1e-6).

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

alg:feastol (feastol)
      Primal feasibility tolerance (default 1e-6).

alg:iisfind (iisfind, iis)
      Whether to find and export an IIS. Default = 0 (don't export).

alg:iismethod (iismethod)
      Which method to use when finding an IIS (irreducible infeasible set of
      constraints, including variable bounds):

      -1 - Automatic choice (default)
      0  - Find smaller IIS
      1  - Find IIS quickly

alg:lbpen (lbpen)
      See alg:feasrelax.

alg:matrixtol (matrixtol)
      nput matrix coefficient tolerance (default 1e-10).

alg:rays (rays)
      Whether to return suffix .unbdd (unbounded ray) if the objective is
      unbounded or suffix .dunbdd (Farkas dual) if the constraints are
      infeasible:

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

bar:crossover (crossover)
      Execute crossover to transform a barrier solution to a basic one
      (default 1).

bar:iterlim (BarIterLimit)
      Limit on the number of barrier iterations (default 500).

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

      Default: 7.

      Bits 2 or 4 imply bit 1.

cvt:qp2passes (cvt:qp2pass, qp2passes, qp2pass)
      Parse sums of QP expressions in 2 passes. Usually faster. Default 1.

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
      quadratic constraints, see cvt:socp2qc. Default: 2.

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

lim:nodes (nodelim, nodelimit)
      Maximum MIP nodes to explore (default: no limit).

lim:soltime (soltimelim, soltimelimit)
      Time limit if a primal feasible solution has been found (in seconds;
      default: no limit).

lim:time (timelim, timelimit)
      limit on solve time (in seconds; default: no limit).

lp:barhomogeneous (barhomogeneous)
      Whether to use homogeneous self-dual form in barrier:

      -1 - Automatic choice (default)
      0  - No
      1  - Yes.

lp:barorder (barorder)
      Barrier ordering algorithm:

      -1 - Choose automatically (default)
      0  - Approximate Minimum Degree (AMD)
      1  - Nested Dissection (ND)

lp:dualperturb (dualperturb)
      Whether to allow the objective function perturbation when using the dual
      simplex method:

      -1 - Automatic choice (default)
      0  - No
      1  - Yes.

lp:dualprice (dualprice)
      Specifies the dual simplex pricing algorithm:

      -1 - Choose automatically (default)
      0  - Use Devex pricing algorithm
      1  - Using dual steepest-edge pricing algorithm

lp:method (method, lpmethod)
      Which algorithm to use for non-MIP problems:

      -1 - Automatic (default)
      1  - Dual simplex
      2  - Barrier
      3  - Crossover
      4  - Concurrent (simplex and barrier simultaneously)
      5  - Choose between simplex and barrier automatically
      6  - First-order method (PDLP)

lp:pdlpgpudevice (pdlpgpudevice, gpudevide)
      Specify devide ID of GPU to use in case of multiple GPUs (default -1,
      choose automatically)

lp:pdlpgpumode (pdlpgpumode, gpumode)
      Wether to use GPU or CPU for PDLP method. Note that CUDA GPU mode is
      only supported on Windows and Linux:

      -1 - Automatic (default)
      0  - Force the use of CPU mode
      1  - Utilize NVIDA GPU

lp:pdlptol (pdlptol)
      Convergence tolerance for PDLP (default 1e-6)

mip:bestbound (bestbound, return_bound)
      Whether to return suffix .bestbound for the best known MIP dual bound on
      the objective value:

      0 - No (default)
      1 - Yes.

      The suffix is on the objective and problem and is -Infinity for
      minimization problems and +Infinity for maximization problems if there
      are no integer variables or if a dual bound is not available.

mip:conflictanalysis (conflictanalysis)
      Whether to perform conflict analysis:

      -1 - Automatic choice (default)
      0  - No
      1  - Yes.

mip:cutlevel (cutlevel)
      Level of cutting-planes generation:

      -1 - Automatic (default)
      0  - Off
      1  - Fast
      2  - Normal
      3  - Aggressive

mip:divingheurlevel (divingheurlevel)
      Level of diving heuristics:

      -1 - Automatic (default)
      0  - Off
      1  - Fast
      2  - Normal
      3  - Aggressive

mip:gap (mipgap)
      Relative MIP optimality gap, default 1e-4.

mip:gapabs (mipgapabs)
      Absolute MIP optimality gap, default 1e-6.

mip:heurlevel (heurlevel)
      Level of heuristics:

      -1 - Automatic (default)
      0  - Off
      1  - Fast
      2  - Normal
      3  - Aggressive

mip:intfeastol (intfeastol, inttol)
      Feasibility tolerance for integer variables (default 1e-06).

mip:nodecutrounds (nodecutrounds)
      Rounds of cutting-planes generation of search tree node;
      default -1 ==> automatic.

mip:return_gap (return_mipgap)
      Whether to return mipgap suffixes or include mipgap values (|objectve -
      .bestbound|) in the solve_message: sum of

      1 - Return .relmipgap suffix (relative to |obj|)
      2 - Return .absmipgap suffix (absolute mipgap)
      4 - Suppress mipgap values in solve_message.

      Default = 0. The suffixes are on the objective and problem. Returned
      suffix values are +Infinity if no integer-feasible solution has been
      found, in which case no mipgap values are reported in the solve_message.

mip:rootcutlevel (rootcutlevel)
      Level of cutting-planes generation of root node:

      -1 - Automatic (default)
      0  - Off
      1  - Fast
      2  - Normal
      3  - Aggressive

mip:rootcutrounds (rootcutrounds)
      Rounds of cutting-planes generation of root node;
      default -1 ==> automatic.

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

mip:roundingheurlevel (roundingheurlevel)
      Level of rounding heuristics:

      -1 - Automatic (default)
      0  - Off
      1  - Fast
      2  - Normal
      3  - Aggressive

mip:strongbranching (strongbranching)
      Level of strong branching:

      -1 - Automatic (default)
      0  - Off
      1  - Fast
      2  - Normal
      3  - Aggressive

mip:submipheurlevel (submipheurlevel)
      Level of Sub-MIP heuristics:

      -1 - Automatic (default)
      0  - Off
      1  - Fast
      2  - Normal
      3  - Aggressive

mip:treecutlevel (treecutlevel)
      Level of cutting-planes generation of search tree:

      -1 - Automatic (default)
      0  - Off
      1  - Fast
      2  - Normal
      3  - Aggressive

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

pre:dualize (dualize)
      Whether to dualize the problem before solving it:

      -1 - Automatic choice (default)
      0  - No
      1  - Yes.

pre:scale (scale)
      Whether to scale the problem:

      -1 - Automatic choice (default)
      0  - No
      1  - Yes.

      Scaling typically reduces solution times, but it may lead to larger
      constraint violations in the original, unscaled model. Choosing a
      different scaling option can sometimes improve performance for
      particularly numerically difficult models.

pre:solve (presolve)
      Level of presolving to perform before solving the problem:

      -1 - Automatic (default)
      0  - Off
      1  - Fast
      2  - Normal
      3  - Aggressive

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

tech:barrierthreads (barthreads)
      Number of threads used by the barrier algorithm;
      default -1 ==> use value in tech:threads.

tech:crossoverthreads (crossoverthreads)
      Number of threads used by crossover;
      default -1 ==> use value in tech:threads.

tech:debug (debug)
      0*/1: whether to assist testing & debugging, e.g., by outputting
      auxiliary information (mostly via suffixes).

tech:logfile (logfile)
      Log file name.

tech:miptasks (miptasks)
      Number of MIP tasks in parallel;
      default -1 ==> automatic.

tech:optionfile (optionfile, option:file)
      Name of an AMPL solver option file to read (surrounded by 'single' or
      "double" quotes if the name contains blanks). Lines that start with #
      are ignored. Otherwise, each nonempty line should contain "name=value",
      e.g., "lim:iter=500".

tech:outlev (outlev)
      0-1: output logging verbosity. Default = 0 (no logging).

tech:outlev_mp (outlev_mp)
      0*/1: whether to print MP model information.

tech:simplexthreads (simplexthreads)
      Number of threads used by dual simplex;
      default -1 ==> use value in tech:threads.

tech:threads (threads)
      Number of threads to use;
      default -1 ==> automatic.

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
```

