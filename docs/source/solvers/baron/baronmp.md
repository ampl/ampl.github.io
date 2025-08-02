
# BARONMP Options

```ampl
ampl: option solver baronmp; # change the solver
ampl: option baronmp_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

Solver options obtained with `$ baronmp -=`.

```
BARONMP Optimizer Options for AMPL
--------------------------------------------

To set these options, assign a string specifying their values to the AMPL
option "baronmp_options". For example:

   ampl: option baronmp_options 'mipgap=1e-6';

'' Options:

acc:_all
      Solver acceptance level for all constraints and expressions. Value
      meaning: as described in the specific acc:... options.

      Can be useful to disable all reformulations (acc:_all=2), or force
      linearization (acc:_all=0.)

acc:_expr
      Solver acceptance level for all expressions, default 1:

      0 - Not accepted, all expressions will be treated as flat constraints,
          or redefined
      1 - Accepted. See the individual acc:... options

acc:div
      Solver acceptance level for 'DivConstraint' as expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:exp
      Solver acceptance level for 'ExpConstraint' as either constraint or
      expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted as constraint but automatic redefinition will be used
          where possible
      2 - Accepted as constraint natively and preferred
      3 - Accepted as expression but automatic redefinition will be used
          where possible
      4 - Accepted as expression natively and preferred

acc:expa (acc:expA)
      Solver acceptance level for 'ExpAConstraint' as either constraint or
      expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted as constraint but automatic redefinition will be used
          where possible
      2 - Accepted as constraint natively and preferred
      3 - Accepted as expression but automatic redefinition will be used
          where possible
      4 - Accepted as expression natively and preferred

acc:lineq
      Solver acceptance level for 'LinConEQ' as flat constraint, default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:linfunccon
      Solver acceptance level for 'LinearFunctionalConstraint' as expression,
      default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

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

acc:log
      Solver acceptance level for 'LogConstraint' as either constraint or
      expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted as constraint but automatic redefinition will be used
          where possible
      2 - Accepted as constraint natively and preferred
      3 - Accepted as expression but automatic redefinition will be used
          where possible
      4 - Accepted as expression natively and preferred

acc:loga (acc:logA)
      Solver acceptance level for 'LogAConstraint' as either constraint or
      expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted as constraint but automatic redefinition will be used
          where possible
      2 - Accepted as constraint natively and preferred
      3 - Accepted as expression but automatic redefinition will be used
          where possible
      4 - Accepted as expression natively and preferred

acc:nlassigneq
      Solver acceptance level for 'NLAssignEQ' as flat constraint, default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:nlassignge
      Solver acceptance level for 'NLAssignGE' as flat constraint, default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:nlassignle
      Solver acceptance level for 'NLAssignLE' as flat constraint, default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:nlcon (acc:nlalgcon)
      Solver acceptance level for 'NLConstraint' as flat constraint, default
      2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:powconstexp
      Solver acceptance level for 'PowConstExpConstraint' as either constraint
      or expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted as constraint but automatic redefinition will be used
          where possible
      2 - Accepted as constraint natively and preferred
      3 - Accepted as expression but automatic redefinition will be used
          where possible
      4 - Accepted as expression natively and preferred

acc:quadeq
      Solver acceptance level for 'QuadConEQ' as flat constraint, default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:quadfunccon
      Solver acceptance level for 'QuadraticFunctionalConstraint' as
      expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

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

acc:quadrange (acc:quadrng)
      Solver acceptance level for 'QuadConRange' as flat constraint, default
      2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

alg:deltaa (deltaa)
      Adjustment parameter for delta values.

alg:deltar (deltar)
      Relative delta adjustment.

alg:deltat (deltat)
      Time-based delta adjustment.

alg:deltaterm (deltaterm)
      Delta termination criterion.

alg:epsa (epsa)
      EpsA convergence tolerance (default 1e-6). BARON stops if the current
      function value f satisfies abs(f - L) <= epsa, where L is the currently
      best available bound on f.

alg:epsr (epsr)
      BARON's EpsR convergence tolerance (default 1e-9). BARON stops if the
      current function value f satisfies abs(f - L) <= abs(L*epsr), where L is
      the currently best available bound on f.

alg:firstfeas (firstfeas)
      If set to 1, BARON will terminate once it finds numsol feasible
      solutions, irrespective of solution quality. Default is 0, meaning that
      BARON will search for the *best* numsol feasible solutions.

alg:firstloc (firstloc)
      If set to 1, BARON will terminate once it finds a local optimum,
      irrespective of solution quality. Default is 0, meaning that BARON will
      search for the best numsol feasible solutions.

alg:relax (relax)
      0*/1: Whether to relax integrality of variables.

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

cvt:compl (cvt:complementarity)
      Complementarity conversion method (if not accepted natively, see
      acc:compl and acc:nlcompl):

      0 - Disjunction: a<=0 || b<=0, a>=0, b>=0
      1 - Product: a*b=cvt:compl:tol
      2 - Fischer-Burmeister function: sqrt(a^2+b^2+2*cvt:compl:tol)=a+b
      3 - min(a,b)=0

cvt:compl:tol (cvt:compl:eps, compl:eps)
      Tolerance parameter for the product and Fischer-Burmeister encodings of
      complementarity, see cvt:compl. Default 1e-6.

cvt:dvelim (dvelim)
      Eliminate AMPL defined variables by substitution into linear, quadratic,
      and polynomial expressions:

      0 - Do not eliminate, always instantiate the variables.
      1 - Eliminate only those used 1x. This can increase model density but
          greatly simplifies some models.
      2 - Always substitute where possible, even if the variable needs to be
          instantiated for use in other places. Can introduce redundancy, but
          seems best for some models (default.)

      See also cvt:pre:unnest, as well as AMPL options linelim and substout.

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

      Low value can speed up model input, but prone to numerical issues.

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

cvt:pre:ctx2count (ctx2count)
      Propagate exact context into atleast/atmost/exactly, count and numberof
      expressions, vs mixed. Bitwise OR of the following values:

      1 - atleast/atmost/exactly, count
      2 - numberof with constant total
      4 - numberof with variable total.

      Default 0, see #267.

cvt:pre:ctx2ineq (ctx2ineq)
      0/1*: Propagate exact context into conditional inequalities, vs mixed.
      See #267.

cvt:pre:eqbinary
      0/1*: Preprocess reified equality comparison with a binary variable.

cvt:pre:eqresult
      0/1*: Preprocess reified equality comparison's decidable cases.

cvt:pre:ineqresult
      0/1*: Preprocess reified inequality comparison's decidable cases.

cvt:pre:ineqrhs
      0/1*: Preprocess reified inequality comparison's right-hand sides.

cvt:pre:unnest (cvt:unnest, cvt:pre:inline, cvt:inline)
      Inline nested expressions. Bitwise OR of the following values:

      1 - Ands and Ors
      2 - Linear subexpressions
      4 - Quadratic subexpressions.

      See also option cvt:dvelim concerning only the input model. Default 7.

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
      0/1*: Parse sums of QP expressions in 2 passes. Usually faster.

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

lim:iter (iterlimit, maxiter)
      Maximum number of iterations.

lim:time (timelim, timelimit, maxtime)
      Maximum time in seconds (default 1000).

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

pre:feastol (pre:eps, pre:feastolabs, pre:epsabs)
      Absolute tolerance to check variable and constraint bound contraditions.
      Only triggers if also pre:feastolrel is violated. See also
      sol:chk:feastol. Default 1e-6.

pre:feastolrel (pre:epsrel)
      Relative tolerance to check variable and constraint bound
      contradictions. Only triggers if also pre:feastol is violated. See also
      sol:chk:feastol. Default 1e-6.

sol:chk:fail (chk:fail, checkfail)
      Fail on MP solution check violations, with solve result 150.

sol:chk:feastol (sol:chk:eps, chk:eps, chk:feastol)
      Absolute tolerance to check objective values', variable and constraint
      bounds' violations. Only triggers if also sol:chk:feastolrel is
      violated. See also pre:feastol. Default 1e-6.

sol:chk:feastolrel (sol:chk:epsrel, chk:epsrel, chk:feastolrel)
      Relative tolerance to check objective values', variable and constraint
      bounds' violations. Only triggers if also sol:chk:feastol is violated.
      See also pre:feastol. Default 1e-6.

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

tech:barstats (barstats)
      Report detailed BARON statistics.

tech:cplexlibname (cplexlibname)
      If used, specifies the path to cplex libraries

tech:debug (debug)
      0*/1: whether to assist testing & debugging, e.g., by outputting
      auxiliary information (mostly via suffixes).

tech:keepsol (keepsol)
      Keep BARON's solution files.

tech:lpsolver (lpsolver)
      Choice of LP solver, which matters mainly when there are integer
      variables: one of cbc (default), cplex, or xpress. The last two must be
      suitably licensed to be used.

tech:lsolmsg (lsolmsg)
      Show solution messages for lsolver.

tech:lsolver (lsolver)
      Local nonlinear solver that BARON should call.

tech:nlpsolver (nlpsol, nlpsolver)
      Local nonlinear solvers BARON is allowed to use: sum (mod 16) of
      | 1 - IPOPT (builtin)
      | 2 - FilterSD (builtin)
      | 4 - FilterSQP (builtin)
      | 8 - lsolver (if lsolver=... is specified)
      Default 0 - allow all.

tech:numsol (numsol)
      Number of near optimal solutions to find. Default = 1; values > 1 imply
      keepsol and cause suffix .numsol on the objective and problem to be
      returned.

tech:objbound (objbound)
      Return suffixes .obj_lb and .obj_ub on the problem and objective with
      Baron's final lower and upper bounds on the objective value

tech:objno (objno)
      Objective number (default: 1).

tech:optfile (optfile)
      Name of BARON option file (not required). If given, the file should
      contain name-value pairs, one per line, with the name and value
      separated by a blank, a colon, or an equal sign, possibly surrounded by
      white space. The names and possible values are summarized in section 7
      of the BARON user manual (baron_manual.pdf). Empty lines and lines that
      start with # are ignored.

tech:optionfile (optionfile, option:file)
      Name of an AMPL solver option file to read (surrounded by 'single' or
      "double" quotes if the name contains blanks). Lines that start with #
      are ignored. Otherwise, each nonempty line should contain "name=value",
      e.g., "lim:iter=500".

tech:optionnative (optionnative, optnative, tech:param)
      General way to specify values of both documented and undocumented Baron
      parameters; value should be a quoted string (delimited by ' or ")
      containing a parameter name, a space, and the value to be assigned to
      the parameter.

tech:outlev (outlev)
      Output verbosity level.

tech:outlev_mp (outlev_mp)
      0*/1: whether to print MP model information.

tech:overwrite (overwrite)
      If set, overwrite the files in the scratch directory.

tech:prfreq (prfreq)
      Report progress every prfreq nodes (default 1e6).

tech:prloc (prloc)
      Whether to report local searches:

      0 - No (default)
      1 - Yes.

tech:problem (problem)
      Problem name printed in logfile.

tech:prtime (prtime)
      Report progress every prtime seconds (default 30).

tech:scratch (scratch)
      Directory for temporary files; if set to 'local' it uses a subdirectory
      of the NL file location with the NL file name

tech:seed (seed)
      Initial seed for random number generation, must be a positive integer
      (default 19631963).

tech:sumfile (sumfile)
      Name of summary file.

tech:threads (threads)
      Maximum number of threads to use (default 1 when integer variables are
      present)

tech:timing (timing, tech:report_times, report_times)
      0*/1/2: Whether to print and return timings for the run, all times are
      wall times. If set to 1, return the solution times in the problem
      suffixes 'time_solver', 'time_setup' and 'time', 'time'=
      time_solver+time_setup+time_output is a measure of the total time spent
      in the solver driver. If set to 2, return more granular times, including
      'time_read', 'time_conversion' and 'time_output'.

tech:trace (trace)
      Name of BARON trace file.

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

tech:writesolution (writesol, writesolution)
      Specifies the names of files where to export the solution and/or other
      result files in solver's native formats. Option can be repeated. File
      name extensions can be ".sol[.tar.gz]", ".json", ".bas", ".ilp", etc.

tech:xpresslibname (xpresslibname)
      If used, specifies the path to xpress libraries
```

