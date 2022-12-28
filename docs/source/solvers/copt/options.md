
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

alg:relax (relax)
      0*/1: Whether to relax integrality of variables.

alg:rhspen (rhspen)
      See alg:feasrelax.

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

lim:nodes (nodelim, nodelimit)
      Maximum MIP nodes to explore (default: no limit).

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
      Relative optimality gap, default 1e-4.

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
      Whether to perform presolving before solving the problem:

      -1 - Automatic choice (default)
      0  - No
      1  - Yes.

sol:count (countsolutions)
      0*/1: Whether to count the number of solutions and return it in the
      ".nsol" problem suffix.

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
      auxiliary information.

tech:exportfile (writeprob, writemodel)
      Specifies the name of a file where to export the model before solving
      it. This file name can have extension ".lp()", ".mps", etc. Default = ""
      (don't export the model).

tech:justexportfile (justwriteprob, justwritemodel)
      Specifies the name of a file where to export the model, do not solve
      it.This file name can have extension ".lp()", ".mps", etc. Default = ""
      (don't export the model).

tech:logfile (logfile)
      Log file name.

tech:miptasks (miptasks)
      Number of MIP tasks in parallel;
      default -1 ==> automatic.

tech:optionfile (optionfile, option:file)
      Name of solver option file. (surrounded by 'single' or "double" quotes
      if the name contains blanks). Lines that start with # are ignored.
      Otherwise, each nonempty line should contain "name=value".

tech:outlev (outlev)
      0-1: output logging verbosity. Default = 0 (no logging).

tech:simplexthreads (simplexthreads)
      Number of threads used by dual simplex;
      default -1 ==> use value in tech:threads.

tech:threads (threads)
      Number of threads to use;
      default -1 ==> automatic.

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

```
