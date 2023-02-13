
# Mosek Options

```ampl
ampl: option solver mosek; # change the solver
ampl: option mosek_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

Solver options obtained with `$ mosek -=`.

```
MOSEK Optimizer Options for AMPL
--------------------------------

To set these options, assign a string specifying their values to the AMPL
option "mosek_options". For example:

   ampl: option mosek_options 'threads=3';

 Options:

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

acc:quadrange (acc:quadrng)
      Solver acceptance level for 'QuadConRange', default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

alg:basis (basis)
      Whether to use or return a basis:

      0 - No
      1 - Use incoming basis (if provided)
      2 - Return final basis
      3 - Both (1 + 2 = default)

alg:method (method, lpmethod, simplex)
      Which algorithm to use for non-MIP problems or for the root node of MIP
      problems:

      0 - Optimizer for conic constraints
      1 - Dual simplex
      2 - Automatic (default)
      3 - Free simplex
      4 - Interior-point method
      5 - Mixed-integer optimizer
      6 - Primal simplex

alg:rays (rays)
      Whether to return suffix .unbdd if the objective is unbounded or suffix
      .dunbdd if the constraints are infeasible:

      0 - Neither
      1 - Just .unbdd
      2 - Just .dunbdd
      3 - Both (default)

alg:relax (relax)
      0*/1: Whether to relax integrality of variables.

alg:sens (sens, solnsens, sensitivity)
      Whether to return suffixes for solution sensitivities, i.e., ranges of
      values for which the optimal basis remains optimal (note that the
      variable and objective values can change):

      0 - No (default)
      1 - Yes: suffixes returned on variables are
      .sensobjlo = smallest objective coefficient
      .sensobjhi = greatest objective coefficient
      .senslblo = smallest variable lower bound
      .senslbhi = greatest variable lower bound
      .sensublo = smallest variable upper bound
      .sensubhi = greatest variable upper bound;

      suffixes for all constraints are

      .senslblo = smallest constraint lower bound
      .senslbhi = greatest constraint lower bound
      .sensublo = smallest constraint upper bound
      .sensubhi = greatest constraint upper bound;

      suffixes for one-sided constraints only:

      .sensrhslo = smallest right-hand side value
      .sensrhshi = greatest right-hand side value.

alg:start (warmstart)
      Whether to use incoming primal (and dual, for LP) variable values in a
      warmstart:

      0 - No
      1 - Yes (for LP: if there is no incoming alg:basis) (default)
      2 - Yes (for LP: ignoring the incoming alg:basis, if any.)

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

lim:time (timelim, timelimit)
      Limit on solve time (in seconds; default: no limit).

mip:bestbound (bestbound, return_bound)
      Whether to return suffix .bestbound for the best known MIP dual bound on
      the objective value:

      0 - No (default)
      1 - Yes.

      The suffix is on the objective and problem and is -Infinity for
      minimization problems and +Infinity for maximization problems if there
      are no integer variables or if a dual bound is not available.

mip:constructsol (mipconstructsol)
      Sets MSK_IPAR_MIO_CONSTRUCT_SOL. If set to MSK_ON and all integer
      variables have been given a value for which a feasible mixed integer
      solution exists, then MOSEK generates an initial solution to the mixed
      integer problem by fixing all integer values and solving the remaining
      problem.Default = OFF

mip:inttol (inttol)
      MIP integrality tolerance.

mip:presolve (presolve)
      MIP presolve:

      0 - Do not use presolve
      1 - Use presolve
      2 - Automatic (default)

mip:relgapconst (miorelgapconst)
      This value is used to compute the relative gap for the solution to an
      integer optimization problem.Default = 1.0e-10

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

obj:no (objno)
      Objective to optimize:

      0 - None
      1 - First (default, if available)
      2 - Second (if available), etc.

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

tech:optionfile (optionfile, option:file)
      Name of solver option file. (surrounded by 'single' or "double" quotes
      if the name contains blanks). Lines that start with # are ignored.
      Otherwise, each nonempty line should contain "name=value".

tech:outlev (outlev)
      0*/1: Whether to write mosek log lines to stdout.

tech:threads (threads)
      Controls the number of threads employed by the optimizer. Default 0 ==>
      number of threads used will be equal to the number of cores detected on
      the machine.

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
