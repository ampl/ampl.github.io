
# GUROBI Options

```ampl
ampl: option solver gurobi; # change the solver
ampl: option gurobi_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

Solver options obtained with `$ gurobi -=`.

```
Gurobi Optimizer Options for AMPL
---------------------------------

To set these options, assign a string specifying their values to the AMPL
option "gurobi_options". For example:

   ampl: option gurobi_options 'opttol=1e-6';

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

acc:abs
      Solver acceptance level for 'AbsConstraint' as flat constraint, default
      2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:and (acc:forall)
      Solver acceptance level for 'AndConstraint' as flat constraint, default
      2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:cos
      Solver acceptance level for 'CosConstraint' as either constraint or
      expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted as constraint but automatic redefinition will be used
          where possible
      2 - Accepted as constraint natively and preferred
      3 - Accepted as expression but automatic redefinition will be used
          where possible
      4 - Accepted as expression natively and preferred

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

acc:indeq (acc:indlineq)
      Solver acceptance level for 'IndicatorConstraintLinEQ' as flat
      constraint, default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:indge (acc:indlinge)
      Solver acceptance level for 'IndicatorConstraintLinGE' as flat
      constraint, default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:indle (acc:indlinle)
      Solver acceptance level for 'IndicatorConstraintLinLE' as flat
      constraint, default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

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

acc:max
      Solver acceptance level for 'MaxConstraint' as flat constraint, default
      2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:min
      Solver acceptance level for 'MinConstraint' as flat constraint, default
      2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

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

acc:or (acc:exists)
      Solver acceptance level for 'OrConstraint' as flat constraint, default
      2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:pl (acc:pwl, acc:piecewise)
      Solver acceptance level for 'PLConstraint' as flat constraint, default
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

acc:sin
      Solver acceptance level for 'SinConstraint' as either constraint or
      expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted as constraint but automatic redefinition will be used
          where possible
      2 - Accepted as constraint natively and preferred
      3 - Accepted as expression but automatic redefinition will be used
          where possible
      4 - Accepted as expression natively and preferred

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

acc:tan
      Solver acceptance level for 'TanConstraint' as either constraint or
      expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted as constraint but automatic redefinition will be used
          where possible
      2 - Accepted as constraint natively and preferred
      3 - Accepted as expression but automatic redefinition will be used
          where possible
      4 - Accepted as expression natively and preferred

alg:basis (basis)
      Whether to use and/or return a basis for LP models (variable/constraint
      suffixes .(s)status):

      0 - No
      1 - Use incoming basis (if provided)
      2 - Return final basis
      3 - Both (1 + 2 = default)

      See alg:start for interaction with the LP warmstart.

      See also mip:basis and qcp:dual (for some solvers).

      Note that if you provide a valid starting extreme point, either through
      primal/dual status, or through warmstart, then Gurobi LP presolve will
      be disabled. For models where presolve greatly reduces the problem size,
      this might hurt performance. See also lp:warmstart.

      For problems with integer variables or quadratic constraints,
      alg:basis=0 is assumed quietly unless mip:basis=1 or qcp:dual=1 is
      specified, respectively.

alg:concurrentmethod (concurrentmethod)
      Controls the methods used by the concurrent continuous solver:

      -1 - Automatic (default)
      0  - Barrier, dual, primal simplex
      1  - Barrier and dual simplex
      2  - Barrier and primal simplex
      3  - Dual and primal simplex

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
      on constraints (when nonnegative, default values = 0), else by keywords
      alg:lbpen, alg:ubpen, and alg:rhspen, respectively (default values = 1).
      Weights < 0 are treated as Infinity, allowing no violation.

alg:feasrelaxbigm (feasrelaxbigm)
      Value of "big-M" sometimes used with constraints when doing a
      feasibility relaxation. Default = 1e6.

alg:feastol (feastol)
      Primal feasibility tolerance (default 1e-6).

alg:global (global)
      Synonym for pre:funcnonlinear.

alg:iisfind (iisfind, iis)
      Whether to find and export an IIS. Default = 0 (don't export).

alg:iisforce (iisforce)
      0/1*: whether to consider the .iis(lb/ub)force suffixes on variables and
      range constraints, as well as .iisforce on other constraints. Suffix
      values mean the following (ATTENTION: different to Gurobi IIS...Force
      attribute!):

      -1 - This model item never to be in an IIS (careful, the remaining
      constraints can be feasible)
      0 - No influence on this bound or constraint (default)
      1 - This model item always to be in the computed IIS.

alg:iismethod (iismethod)
      Which method to use when finding an IIS (irreducible infeasible set of
      constraints, including variable bounds):

      -1 - Automatic choice (default)
      0  - Often faster than method 1
      1  - Can find a smaller IIS than method 0
      2  - Ignore the bound constraints.

alg:infunbdinfo (infunbdinfo, InfUnbdInfo)
      Synonym for alg:rays.

alg:kappa (kappa, basis_cond)
      Whether to return the estimated condition number (kappa) of the optimal
      basis (default 0): sum of 1 = report kappa in the result message; 2 =
      return kappa in the solver-defined suffix .kappa on the objective and
      problem. The request is ignored when there is no optimal basis.

alg:kappa_exact (kappa_exact, basis_cond_exact)
      Whether to return the exact condition number (kappa) of the optimal
      basis (default 0): sum of 1 = report kappa in the result message; 2 =
      return kappa in the solver-defined suffix .kappa_exact on the objective
      and problem. The request is ignored when there is no optimal basis.

      The exact kappa may be hard to compute.

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

alg:networkalg (networkalg)
      Whether to use network simplex if an LP is a network problem:

      -1 - Automatic choice (default)
      0  - No
      1  - Yes.

alg:nlpheur (nlpheur)
      Use NLP heuristic to find feasible solutions to non-convex quadratic
      models:

      0 - No
      1 - Yes (default)

alg:numericfocus (numericfocus, numfocus, numericemphasis, numericalemphasis)
      How much to try detecting and managing numerical issues:

      0 - Automatic choice (default)
      1-3 - Increasing focus on more stable computations.

alg:rays (rays)
      Whether to return suffix .unbdd (unbounded ray) if the objective is
      unbounded or suffix .dunbdd (Farkas dual) if the constraints are
      infeasible:

      0 - Neither
      1 - Just .unbdd
      2 - Just .dunbdd
      3 - Both (default)

      Only applies to LP models.

alg:relax (relax)
      0*/1: Whether to relax integrality of variables.

alg:rhspen (rhspen)
      See alg:feasrelax.

alg:sens (sens, solnsens, sensitivity)
      Whether to return suffixes for solution sensitivities, i.e., ranges of
      values for which the optimal basis remains optimal (note that the
      variable and objective values can change):

      0 - No (default)
      1 - Yes: suffixes returned on variables are
      .sensobjlo = smallest objective coefficients
      .down = same as .sensobjlo
      .sensobj = current objective coefficients
      .current = same as .sensobj
      .sensobjhi = greatest objective coefficients
      .up = same as .sensobjhi
      .senslblo = smallest variable lower bounds
      .senslbhi = greatest variable lower bounds
      .sensublo = smallest variable upper bounds
      .sensubhi = greatest variable upper bounds;

      suffixes for all constraints are

      .senslblo = smallest constraint lower bounds
      .senslbhi = greatest constraint lower bounds
      .sensublo = smallest constraint upper bounds
      .sensubhi = greatest constraint upper bounds;

      suffixes for one-sided constraints only:

      .sensrhslo = smallest right-hand side values
      .down = same as .sensrhslo
      .sensrhshi = greatest right-hand side values.
      .up = same as .sensrhshi.

      The suffixes correspond to the AMPL solver model, command 'solexpand'.
      For easiest interpretation, disable AMPL presolve, 'option presolve 0;'

      For problems with integer variables or quadratic constraints, alg:sens=0
      is assumed quietly.

alg:solutiontarget (solutiontarget, lptarget)
      Specifies the solution target for linear programs (LP):

      -1 - Automatic (default)
      0  - Primal and dual optimal and basic
      1  - primal and dual optimal

alg:start (warmstart)
      Whether to use incoming primal (and dual, for LP) variable values in a
      warmstart:

      0 - No
      1 - Yes (for LP: if there is no incoming alg:basis)
      2 - Yes (for LP: omitting the incoming alg:basis, if any)
      3 - Yes (for LP: together with the incoming alg:basis, if any;
          default).

      For Gurobi, choices can be refined vie "lp:warmstart"; MIP-specific
      options can be tuned via "mip:start".

alg:ubpen (ubpen)
      See alg:feasrelax.

bar:convtol (barconvtol)
      Tolerance on the relative difference between the primal and dual
      objectives for stopping the barrier algorithm (default 1e-8).

bar:corr (barcorrectors)
      Limit on the number of central corrections done in each barrier
      iteration (default -1 = automatic choice).

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

cut:mixingcuts
      Mixing cuts: overrides "cuts"

      -1 - Automatic choice (default)
      0  - No cuts
      1  - Conservative cut generation
      2  - Aggressive cut generation.

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

cvt:bigM (cvt:bigm, cvt:mip:bigM, cvt:mip:bigm)
      Default value of big-M for linearization of logical constraints. Not
      used by default. Use with care (prefer tight bounds). Should be smaller
      than (1.0 / [integrality tolerance])

cvt:compl (cvt:complementarity)
      Complementarity conversion method (if not accepted natively, see
      acc:compl and acc:nlcompl). Default 0:

      0 - Disjunction: a<=0 || b<=0, a>=0, b>=0
      1 - Product: a*b=cvt:compl:tol
      2 - Fischer-Burmeister function: sqrt(a^2+b^2+2*cvt:compl:tol)=a+b
      3 - min(a,b)=0

cvt:compl:tol (cvt:compl:eps, compl:eps)
      Tolerance parameter for the product and Fischer-Burmeister encodings of
      complementarity, see cvt:compl. Default 1e-9.

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
      comparisons: b==1 <==> x<=5 means that with b==0, x>=5+eps. Normally
      should be larger or equal to the solver's feasibility tolerance.
      Default: 1e-4.

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

cvt:pre:boundlogarg (boundlogarg)
      0*/1: Bound logarithm arguments to nonnegative.

cvt:pre:ctx2bndeq (ctx2bndeq)
      0/1*: Propagate exact context into conditional (dis)equalities-to-bound,
      vs always mixed. Can be affected by cvt:pre:ineq2bndeq. See #267.

cvt:pre:ctx2count (ctx2count)
      DEPRECATED. Use ctx2bndeq. NEW DEFAULT.

      Propagate exact context into atleast/atmost/exactly, count and numberof
      expressions, vs always mixed. Bitwise OR of the following values:

      1 - atleast/atmost/exactly, count
      2 - numberof with constant reference value
      4 - numberof with variable reference value.

      Default 7, see #267.

cvt:pre:ctx2ineq (ctx2ineq)
      0/1*: Propagate exact context into conditional inequalities, vs always
      mixed. See #267.

      Finer control provided by cvt:pre:ctx:cond...(le/ge) options.

cvt:pre:ctx:abs (ctx:abs)
      Controls propagation of context into abs() expressions, which could
      affect reformulations of abs() and its arguments (see the acc: options).
      Bitwise OR of the following values:

      1 - Propagate positive context exactly (otherwise always mixed)
      2 - Propagate negative context exactly (otherwise always mixed)

      Default 3. See mp.ampl.com/components.html#mathematical-background.

cvt:pre:ctx:acos (ctx:acos)
      Context propagation for 'Acos' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:acosh (ctx:acosh)
      Context propagation for 'Acosh' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:alldiff (ctx:alldiff)
      Context propagation for 'AllDiff' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:and (ctx:and)
      Context propagation for 'And' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:asin (ctx:asin)
      Context propagation for 'Asin' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:asinh (ctx:asinh)
      Context propagation for 'Asinh' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:atan (ctx:atan)
      Context propagation for 'Atan' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:atanh (ctx:atanh)
      Context propagation for 'Atanh' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:condlineq (ctx:condlineq)
      Context propagation for 'Conditional< AlgebraicConstraint< LinTerms,
      RhsEQ > >' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:condlinge (ctx:condlinge)
      Context propagation for 'Conditional< AlgebraicConstraint< LinTerms,
      RhsGE > >' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:condlingt (ctx:condlingt)
      Context propagation for 'Conditional< AlgebraicConstraint< LinTerms,
      RhsGT > >' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:condlinle (ctx:condlinle)
      Context propagation for 'Conditional< AlgebraicConstraint< LinTerms,
      RhsLE > >' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:condlinlt (ctx:condlinlt)
      Context propagation for 'Conditional< AlgebraicConstraint< LinTerms,
      RhsLT > >' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:condquadeq (ctx:condquadeq)
      Context propagation for 'Conditional< AlgebraicConstraint<
      QuadAndLinTerms, RhsEQ > >' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:condquadge (ctx:condquadge)
      Context propagation for 'Conditional< AlgebraicConstraint<
      QuadAndLinTerms, RhsGE > >' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:condquadgt (ctx:condquadgt)
      Context propagation for 'Conditional< AlgebraicConstraint<
      QuadAndLinTerms, RhsGT > >' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:condquadle (ctx:condquadle)
      Context propagation for 'Conditional< AlgebraicConstraint<
      QuadAndLinTerms, RhsLE > >' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:condquadlt (ctx:condquadlt)
      Context propagation for 'Conditional< AlgebraicConstraint<
      QuadAndLinTerms, RhsLT > >' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:cos (ctx:cos)
      Context propagation for 'Cos' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:cosh (ctx:cosh)
      Context propagation for 'Cosh' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:count (ctx:count)
      Context propagation for 'Count' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:div (ctx:div)
      Context propagation for 'Div' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:equiv (ctx:equiv)
      Context propagation for 'Equivalence' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:exp (ctx:exp)
      Context propagation for 'Exp' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:expa (ctx:expa)
      Context propagation for 'ExpA' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:ifthen (ctx:ifthen)
      Context propagation for 'IfThen' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:impl (ctx:impl)
      Context propagation for 'Implication' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:linfunccon (ctx:linfunccon)
      Context propagation for 'LinearFunctionalConstraint' expression, see
      cvt:pre:ctx:abs.

cvt:pre:ctx:log (ctx:log)
      Context propagation for 'Log' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:loga (ctx:loga)
      Context propagation for 'LogA' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:max (ctx:max)
      Context propagation for 'Max' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:min (ctx:min)
      Context propagation for 'Min' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:not (ctx:not)
      Context propagation for 'Not' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:numberofconst (ctx:numberofconst)
      Context propagation for 'NumberofConst' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:numberofvar (ctx:numberofvar)
      Context propagation for 'NumberofVar' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:or (ctx:or)
      Context propagation for 'Or' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:pl (ctx:pl)
      Context propagation for 'PL' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:pow (ctx:pow)
      Context propagation for 'Pow' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:powconstexp (ctx:powconstexp)
      Context propagation for 'PowConstExp' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:quadfunccon (ctx:quadfunccon)
      Context propagation for 'QuadraticFunctionalConstraint' expression, see
      cvt:pre:ctx:abs.

cvt:pre:ctx:sin (ctx:sin)
      Context propagation for 'Sin' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:sinh (ctx:sinh)
      Context propagation for 'Sinh' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:tan (ctx:tan)
      Context propagation for 'Tan' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:tanh (ctx:tanh)
      Context propagation for 'Tanh' expression, see cvt:pre:ctx:abs.

cvt:pre:eqbinary
      0/1*: Preprocess reified equality comparison with a binary variable.

cvt:pre:eqresult
      0/1*: Preprocess reified equality comparison's decidable cases.

cvt:pre:feastol (pre:feastol, pre:eps, pre:feastolabs, pre:epsabs)
      Absolute tolerance to check variable and constraint bound contraditions.
      Only warns if also pre:feastolrel is violated. See also sol:chk:feastol.
      Default 1e-6.

cvt:pre:feastolrel (pre:feastolrel, pre:epsrel)
      Relative tolerance to check variable and constraint bound
      contradictions. Only warns if also pre:feastol is violated. See also
      sol:chk:feastol. Default 1e-6.

cvt:pre:ineq2bndeq (ineq2bndeq)
      0/1*: Preprocess reified inequality expr <(=) c, where c <)=(
      lb(expr)+cvt:mip:eps, into expr == lb(expr), which works better on some
      benchmarks/solvers.

cvt:pre:ineq2related (ineq2related, ineq2rel)
      0/1*: Unify related reified inequalities: <=c, <c+cvt:mip:eps, >c,
      >=c+cvt:mip:eps.

cvt:pre:ineqresult
      0/1*: Preprocess reified inequality comparison's decidable cases.

cvt:pre:ineqrhs
      0/1*: Preprocess reified inequality comparison's right-hand sides (round
      for integer expression body).

cvt:pre:prod (cvt:prod)
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

cvt:pre:sort (cvt:sort)
      0/1*: Sort and eliminate duplicates in arguments of AND, OR, MIN, MAX.
      Sort arguments of COUNT, ATLEAST, EXACTLY, ATMOST, NUMBEROF, ALLDIFF.
      Can be necessary for some solvers.

cvt:pre:unnest (cvt:unnest, cvt:pre:inline, cvt:inline)
      Inline nested expressions. Bitwise OR of the following values:

      1 - AND/FORALL and OR/EXISTS expressions
      2 - Linear subexpressions
      4 - Quadratic subexpressions
      8 - MIN/MAX.

      See also option cvt:dvelim concerning only the input model. Default 15.

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
      quadratic constraints, see cvt:socp2qc. Default: 1.

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

cvt:uenc:negctx:max (uenc:negctx:max, cvt:uenc:negctx, uenc:negctx)
      If cvt:uenc:ratio applies, max number of constants in comparisons
      x==const in negative context (equivalently, x!=const in positive
      context), where const!=lb(x) and const!=ub(x), to skip unary encoding of
      x. Default 1.

      Example:

      var x in 1..9;
      var y >=1 <=200;
      
      s.t. Con: (x==9 || x==2 || x==6) ==> y >= 4;

      With uenc:negctx<=1, this triggers unary encoding for x.

cvt:uenc:ratio (uenc:ratio)
      Min ratio (ub-lb+1)/Nvalues to skip unary encoding for a variable x,
      where Nvalues is the number of constants used in conditional comparisons
      x==const. Instead, indicator constraints (or big-Ms) are used, if
      uenc:negctx also applies. Default 0.

      Example:

      var x in 1..9;
      var y >=1 <=200;
      
      s.t. Con: y>3 ==> (x==2 || x==6 || x==5);

      With uenc:ratio>3, this triggers unary encoding for x.

lim:iter (iterlim, iterlimit)
      Iteration limit (default: no limit).

lim:mem (memlimit, maxmemoryhard)
      Hard limit (number of MB) on memory allocated, causing early termination
      if exceeded; default = 0 (no limit)

lim:minrelnodes (minrelnodes)
      Number of nodes for the Minimum Relaxation heuristic to explore at the
      MIP root node when a feasible solution has not been found by any other
      heuristic; default -1 ==> automatic choice.

lim:nodes (nodelim, nodelimit)
      Maximum MIP nodes to explore (default: no limit).

lim:softmem (softmemlimit, maxmemorysoft)
      Soft limit (number of MB) on memory allocated; default = 0 (no limit)

lim:sol (sollimit, solutionlimit)
      Limit the number of feasible MIP solutions found, causing early
      termination if exceeded; default = 2e9

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

lim:work (worklim, worklimit)
      Limit on work units. Roughly corresponds to seconds per thread but
      deterministic. Default: no limit).

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

lp:opttol (opttol, optimalitytolerance)
      Dual optimality tolerance: for the simplex algorithm and crossover,
      reduced costs must all be smaller than this value in the improving
      direction in order for a model to be declared optimal. Default 1e-6.

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

lp:warmstart (lpwarmstart)
      Controls whether and how to warm-start LP optimization, see options
      alg:basis and alg:start:

      0 - Ignore any warm start information (generally)
      1 - Use warm start information to solve the original, unpresolved
          problem (default)
      2 - If presolve is enabled, use warm start to solve the presolved
          problem. Otherwise, setting 2 prioritizes start vectors
          (primal/dual), while setting 1 prioritizes basis statuses.

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

mip:intfocus (integralityfocus, intfocus)
      Setting this parameter to 1 requests the solver to work harder at
      finding solutions that are still (nearly) feasible when all integer
      variables are rounded to exact integral values to avoid numerical issues
      such as trickle flow:

      0 - No (default)
      1 - Yes.

mip:inttol (inttol, intfeastol)
      Feasibility tolerance for integer variables (default 1e-05).

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

mip:obbt (obbt)
      Controls aggressiveness of Optimality - Based Bound Tightening:

      -1 - Automatic choice (default)
      0  - No
      1  - Yes
      2  - Yes, more aggressively
      3  - Yes, even more aggressively.

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

      For Gurobi's native handling (obj:multi=1), objective-specific
      tolerances and method values may be assigned via keywords of the form
      obj_n_<name>, such as obj_1_method for the first objective.

obj:multi:weight (multiobjweight, obj:multi:weights, multiobjweights)
      How to interpret each objective's weight sign:

      1 - relative to the sense of the 1st objective
      2 - relative to its own sense (default)

      With the 1st option (legacy behaviour), negative .objweight for
      objective i would make objective i's sense the opposite of the model's
      1st objective. Otherwise, it would make objective i's sense the opposite
      to its sense defined in the model.

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
      1 - Yes (default)

pre:funcnonlinear (funcnonlinear, global)
      Controls how general functions with their constraint's or objective's
      suffix .funcnonlinear or, if not available, .global unset (or set to 0)
      are treated (ATTENTION: different meaning than Gurobi FuncNonLinear
      parameter and attribute; ATTENTION: also set acc:_expr=0 with
      pre:funcnonlinear=-1 to use 'general constraints'):

      -1 - Piecewise-linear approximation
      0  - Automatic (default)
      1  - Treated as nonlinear functions

      Suffix values mean the same.

pre:funcpieceerror (funcpieceerror)
      For 'funcpieces=-1' or -2, this option provides the maximum allowed
      error (absolute for -1, relative for -2) in the piecewise-linear
      approximation.

      The value can be overridden by suffix .funcpieceerror of the individual
      constraints.

pre:funcpiecelength (funcpiecelength)
      If 'funcpieces=1', this option or suffix provide the length of each
      piece of the piecewise-linear approximation.

pre:funcpieceratio (funcpieceratio)
      This option (and suffix) control whether the piecewise-linear
      approximation of a function constraint is an underestimate of the
      function, an overestimate, or somewhere in between. A value of 0.0 will
      always underestimate, while a value of 1.0 will always overestimate. A
      value in between will interpolate between the underestimate and the
      overestimate. A special value of -1 chooses points that are on the
      original function.

pre:funcpieces (funcpieces)
      This option (and suffix) set the strategy used for performing a
      piecewise-linear approximation of a function constraint. They have the
      following meaning:

      0 - Automatic choice (default)
      >=2 - Sets the number of pieces; pieces are equal width
      1 - Uses a fixed width for each piece; the actual width is provided in
      the 'funcpiecelength' option/suffix
      -1 - Bounds the absolute error of the approximation; the error bound is
      provided in the 'funcpieceerror' option/suffix
      -2 - Bounds the relative error of the approximation; the error bound is
      provided in the 'funcpieceerror' option/suffix.

pre:funcpiecesuf (funcpiecesuf, funcpiecesuffixes)
      0/1*: whether to consider the individual .funcpiece... suffixes in
      objectives and constraints, which impact Gurobi's approximation quality
      of nonlinear constraints, beyond the corresponding global options

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

pre:sos1enc (presos1enc)
      Encoding used for SOS1 reformulation:

      -1 - Automatic choice (default)
      0 - Multiple choice model, produces an LP relaxation that is easy to
      solve
      1 - Incremental model, reduces the amount of branching
      2 - Formulation whose LP relaxation is easier to solve
      3 - Formulation with better branching behavior, requires sum of the
      variables == 1.

      Options 0 and 1 produce reformulations that are linear in size; options
      2 and 3 use reformulation logarithmic in size. Option 2 and 3 apply only
      when all the variables are >=0.

pre:sos2bigm (presos2bigm)
      Big-M for converting SOS2 constraints to binary form:

      -1 - Automatic choice (default)
      0 - No conversion

      Large values (e.g., 1e8) may cause numeric trouble.

pre:sos2enc (presos2enc)
      Encoding used for SOS2 reformulation, see presos1enc.

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

      -1 - Default choice (currently almost the same as 2)
      0  - Complain about nonquadratic terms
      1  - Complain if Gurobi's presolve cannot discard or eliminate
           nonquadratic terms
      2  - Translate quadratic forms to bilinear form and use spatial
           branching.

qp:psdtol (psdtol)
      Maximum diagonal perturbation to correct indefiniteness in quadratic
      objectives (default 1e-6).

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

      0 - Just collect solutions during normal solve, and sort them
          best-first
      1 - Make some effort at finding additional solutions
      2 - Seek "poollimit" best solutions (default).'Best solutions' are
          defined by the poolgap(abs) parameters.

sol:report_uncertain (report_uncertain_sol)
      0/1*: whether to report objective value(s) in solve_message when
      solve_result is '?' (unknown).

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
      auxiliary information (mostly via suffixes).

tech:distmip (pool_distmip, distmip)
      Enables distributed MIP. A value of n causes the MIP solver to divide
      the work of solving a MIP model among n machines. Use the "tech:server"
      parameter to indicate the name of the cluster where you would like your
      distributed MIP job to run (or use "tech:workerpool" if your client
      machine will act as manager and you just need a pool of workers).
      Default = 0.

      See also "tech:concurrentmip", "tech:pooljobs".

tech:logfile (logfile)
      Log file name; note that the solver log will be written to the log
      regardless of the value of tech:outlev.

tech:logfreq (logfreq, outfreq)
      Interval in seconds between log lines (default 5).

tech:nodefiledir (nodefiledir)
      Directory where MIP tree nodes are written after memory for them exceeds
      "nodefilestart"; default "."

tech:nodefilestart (nodefilestart)
      Gigabytes of memory to use for MIP tree nodes; default = Infinity (no
      limit, i.e., no node files written).

tech:optionfile (optionfile, option:file)
      Name of an AMPL solver option file to read (surrounded by 'single' or
      "double" quotes if the name contains blanks). Lines that start with #
      are ignored. Otherwise, each nonempty line should contain "name=value",
      e.g., "lim:iter=500".

tech:optionnative (optionnative, optnative, tech:param)
      General way to specify values of both documented and undocumented Gurobi
      parameters; value should be a quoted string (delimited by ' or ")
      containing a parameter name, a space, and the value to be assigned to
      the parameter. Can appear more than once. Cannot be used to query
      current parameter values.

tech:optionnativeread (optionnativeread, tech:param:read, param:read)
      Name of Gurobi parameter file (surrounded by 'single' or "double" quotes
      if the name contains blanks). The suffix on a parameter file should be
      .prm, optionally followed by .zip, .gz, .bz2, or .7z.

      Lines that start with # are ignored. Otherwise, each nonempty line
      should contain a name and a value, separated by a space.

tech:optionnativewrite (optionnativewrite, tech:param:write, param:write)
      Name of Gurobi parameter file (surrounded by 'single' or "double" quotes
      if the name contains blanks) to be written.

tech:outlev (outlev)
      0*/1: Whether to write gurobi log lines (chatter) to stdout.

tech:outlev_mp (outlev_mp)
      0*/1: whether to print MP model information.

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

tech:reportwork (reportwork, work)
      0*/1: Whether to report the work spent in the optimization in the
      problem suffix `work`. Gurobi's work units are deterministic, and
      roughly equivalent to one second on a single thread.

tech:resultfile (resultfile)
      Name of a file of extra information written after completion of
      optimization. The name's suffix determines what is written:

      .sol - Solution vector
      .bas - Simplex basis
      .mst - Integer variable solution vector
      .ilp - IIS for an infeasible model
      .mps, .rew, .lp, or .rlp - To capture the original model.

      The file suffix may optionally be followed by .gz, .bz2, or .7z, which
      produces a compressed result. Use tech:writesolution to write several
      files.

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

tech:timing (timing, tech:report_times, report_times)
      0*/1/2: Whether to print and return timings for the run, all times are
      wall times. If set to 1, return the solution times in the problem
      suffixes 'time_solver', 'time_setup' and 'time', 'time'=
      time_solver+time_setup+time_output is a measure of the total time spent
      in the solver driver. If set to 2, return more granular times, including
      'time_read', 'time_conversion' and 'time_output'.

tech:tunebase (tunebase)
      Base name for results of running Gurobi's search for best parameter
      settings. The search is run only when tunebase is specified. Results are
      written to files with names derived from tunebase by appending ".prm" if
      ".prm" does not occur in tunebase and inserting _1_, _2_, ... (for the
      first, second, ... set of parameter settings) before the right-most
      ".prm". The file with _1_ inserted is the best set and the solve results
      returned are for this set. In a subsequent "solve;", you can use
      "tech:param:read=..." to apply the settings in results file ... .

tech:tunedynamicjobs (pool_tunedynamicjobs, tunedynamicjobs)
      Enables distributed parallel tuning, which can significantly increase
      the performance of the tuning tool. A value of n causes the tuning tool
      to use a dynamic set of up to n workers in parallel. A value of -1
      allows the solver to use an unlimited number of workers. Default = 0.

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

tech:wls_accessid (wls_accessid)
      Web License Manager access ID

tech:wls_licenseid (wls_licenseid, licenseid)
      Web License Manager license ID.

tech:wls_secret (wls_secret)
      Web License Manager secret key

tech:wls_token (wls_token)
      Web License Manager token retrieved with the REST API. If specified, all
      other WSL-related parameters are ignored.

tech:wls_tokenduration (wls_tokenduration)
      Token duration (in minutes). Default = 0 (automatic)

tech:wls_tokenrefresh (wls_tokenrefresh)
      Fraction of the token duration after which a token refresh is triggered.
      The minimum refresh interval is 4 minutes. Default = 0.9

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

tech:writepresolved (writepresolved, writepresolvedmodel, exportpresolvedfile)
      Specifies the name of a file where to export the presolved model before
      solving it. This file name can have extension ".lp", ".mps", etc.
      Default = "" (don't export the model).

tech:writesolution (writesol, writesolution)
      Specifies the names of files where to export the solution and/or other
      result files in solver's native formats. Option can be repeated. File
      name extensions can be ".sol[.tar.gz]", ".json", ".bas", ".ilp", etc.
```

