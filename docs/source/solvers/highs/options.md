
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

   ampl: option highs_options 'mip:gap=1e-6';

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
      Whether to use and/or return a basis for LP models (variable/constraint
      suffixes .(s)status):

      0 - No
      1 - Use incoming basis (if provided)
      2 - Return final basis
      3 - Both (1 + 2 = default)

      See alg:start for interaction with the LP warmstart.

      See also mip:basis and qcp:dual (for some solvers).

alg:dualfeastol (dualfeastol, dual_feasibility_tolerance)
      Dual feasibility tolerance (default 1e-7).

alg:dualrestol (dualrestol, dual_residual_tolerance)
      Dual residual tolerance (default 1e-7).

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

alg:feastol (feastol, primal_feasibility_tolerance)
      Primal feasibility tolerance (default 1e-7).

alg:infinitebound (infinitebound, infinite_bound)
      Limit on |constraint bound|: values greater than or equal to this will
      be treated as infinite (default: 1e20).

alg:infinitecoeff (infinitecoeff, large_matrix_value)
      Upper limit on |matrix entries|: values greater than or equal to this
      will be treated as infinite (default: 1e15).

alg:infinitecost (infinitecost, infinite_cost)
      Limit on |cost coefficient|: values greater than or equal to this will
      be treated as infinite (default: 1e20).

alg:ipmopttol (ipmopttol, ipm_optimality_tolerance)
      IPM optimality tolerance (default 1e-8).

alg:kkttol (kkttol, alg:kkt_tolerance, kkt_tolerance)
      KKT tolerance (default 1e-7). If changed from its default, this
      tolerance is used for all feasibility and optimality (KKT) measures,
      overriding the individual tolerances.

alg:lbpen (lbpen)
      See alg:feasrelax.

alg:method (method, lp:method, lpmethod, lp:algorithm, solver)
      Which algorithm to use for non-MIP problems:

      choose     - Automatic (default)
      simplex    - Simplex
      ipm        - Interior Point Method (automatic)
      hipo       - HiPO interior point method (not available in every HiGHS
                   library build; rejected with a message if unavailable)
      ipx        - IPX interior point method
      pdlp       - cuPDLP-c solver
      pdlp-gpu   - cuPDLP-c solver on NVIDIA GPU. Requires CUDA, not
                   available on MacOS
      hipdlp     - HiPDLP solver
      hipdlp-gpu - HiPDLP-c solver on NVIDIA GPU. Requires CUDA, not
                   available on MacOS
      qpasm      - QP active set method

alg:opttol (opttol, optimality_tolerance)
      Optimality tolerance (default 1e-7).

alg:parallel (parallel)
      Parallel option :

      choose - Automatic (default)
      off    - Off
      on     - On

alg:primalrestol (primalrestol, primal_residual_tolerance)
      Primal residual tolerance (default 1e-7).

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

alg:simplex (simplex, simplex_strategy)
      Strategy for simplex solver :

      0 - Choose automatically
      1 - Dual, serial (default)
      2 - Dual, 'SIP' (Single Iteration Parallelism)
      3 - Dual, 'PAMI' (Parallelization Across Multiple Iterations)
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

alg:simplexmaxconcurrency (simplexmaxconcurrency, simplex_max_concurrency)
      Maximum level of concurrency in parallel simplex (1..8, default 8).

alg:simplexminconcurrency (simplexminconcurrency, simplex_min_concurrency)
      Minimum level of concurrency in parallel simplex (1..8, default 1).

alg:simplexprimaledge (simplexprimaledge, simplex_primal_edge_weight_strategy)
      Simplex primal edge weights strategy :

      -1 - Choose automatically (default)
      0  - Dantzig
      1  - Devex
      2  - Steepest

alg:simplexscale (simplexscale, simplex_scale_strategy)
      Simplex scaling strategy :

      0 - Off
      1 - Choose automatically
      2 - Equilibration (default)
      3 - Forced equilibration
      4 - Max value

alg:simplexupdatelim (simplexupdatelim, simplex_update_limit)
      Limit on the number of simplex UPDATE operations before refactorization
      (default 5000).

alg:start (warmstart)
      Whether to use incoming primal (and dual, for LP) variable values in a
      warmstart:

      0 - No
      1 - Yes (for LP: if there is no incoming alg:basis)
      2 - Yes (for LP: omitting the incoming alg:basis, if any)
      3 - Yes (for LP: together with the incoming alg:basis, if any;
          default).

alg:ubpen (ubpen)
      See alg:feasrelax.

alg:zerocoeff (zerocoeff, small_matrix_value)
      Lower limit on |matrix entries|: values less than or equal to this will
      be treated as zero (default: 1e-9).

bar:centring (centring, pre:centring, run_centring)
      Perform centring steps or not:

      0 - No (default)
      1 - Yes.

bar:centringratiotol (centringratiotol, pre:centringratiotolerance, centring_ratio_tolerance, centringratiotolerance)
      Centring stops when the ratio max(x_j*s_j) / min(x_j*s_j) is below this
      tolerance (default 100).

bar:crossover (crossover, run_crossover)
      Run crossover after IPM to get a basic solution:

      choose - Run if the results of IPM without crossover is imprecise
      off    - Off
      on     - On (default)

bar:hipoblocksize (hipoblocksize, hipo_block_size)
      Block size for dense linear algebra within HiPO (default 128).

bar:hipoordering (hipoordering, bar:hipo_ordering, hipo_ordering)
      Control the ordering used by HiPO before factorization:

      choose - Choose automatically (default)
      metis  - Multilevel graph partitioning
      amd    - Approximate minimum degree
      rcm    - Reverse Cuthill-McKee

bar:hipoparallel (hipoparallel, bar:hipo_parallel_type, hipo_parallel_type)
      Control the type of parallelism used by HiPO:

      tree - Tree parallelism
      node - Node parallelism
      both - Both tree and node parallelism

bar:hiposystem (hiposystem, bar:hipo_system, hipo_system)
      Control which Newton/KKT system is used by HiPO:

      choose    - Choose automatically (default)
      augmented - Augmented system
      normaleq  - Normal equations

bar:iterlim (bariterlim, lim:ipmiterationlimit, ipmiterationlimit, ipm_iteration_limit)
      Limit on IPM iterations (default: no limit).

bar:maxcentringsteps (maxcentringsteps, pre:maxcentringsteps, max_centring_steps)
      Maximum number of steps to use when computing the analytic centre
      (default 5).

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
      1 - Eliminate only those used once.
      2 - (Default). Always substitute where possible, even if the variable
          needs to be instantiated for use in other places. Can introduce
          redundancy but proves efficient in many cases.

      See also cvt:pre:unnest, as well as AMPL options linelim and substout.

cvt:expcones (expcones)
      0*/1: Recognize exponential cones.

cvt:expr:nlassign (expr:nlassign)
      Above which reference count, an algebraic formula node should be
      assigned to a variable (see acc: options). 0 means all nodes assigned.
      Default 1.

cvt:expr:nlreif (expr:nlreif, expr:nlreify)
      Above which reference count, a logical formula node should be assigned
      (reified) to a variable (see acc: options). 0 means all nodes reified.
      Default 1.

cvt:mip:eps (cvt:cmp:eps, cmp:eps)
      Tolerance for strict comparison of continuous variables for MIP. Applies
      to <, >, and != operators. Also applies to negation of conditional
      comparisons: b==1 <==> x<=5 means that with b==0, x>=5+eps. Normally
      should be larger or equal to the solver's feasibility tolerance.
      Default: 1e-4.

cvt:mip:intprodbits (intprodbits)
      Products x*y of variables, when not accepted natively, with an integer
      factor of finite bounds (and the other factor bounded): exact MIP
      reformulation by binary expansion of the integer factor with the smaller
      range if it needs at most this many binary variables. Default 30.
      Otherwise, and with 0, such products are approximated as
      ((x+y)^2-x^2-y^2)/2 with piecewise-linear squares, as for continuous
      factors. Products with a binary factor are always exact.

cvt:multoutcard (multoutcard)
      Up to which (estimated) QP matrix cardinality should a product of 2
      linear expressions be multiplied out. Default 1e+09.

      Low value can speed up model input, but prone to numerical issues.

cvt:names (names, modelnames)
      Whether to read or generate variable / constraint / objective names:

      0 - No names
      1 - (Default) Only provide names if at least one of .col / .row name
          files was written by AMPL (AMPL: `option [<solver>_]auxfiles rc;`) 
      2 - Read names from AMPL, but create generic names if not provided
      3 - Create generic names.

cvt:nlobj (passnlobj)
      0*/1: Pass nonlinear objective terms to the solver. When 0, if the
      solver accepts nonlinear constraints, such a constraint will be created
      with those, otherwise linearly approximated. With cvt:quadobj=0, ensures
      the objective is linear.

cvt:pl:domain (pl:domain, pldomain)
      Max absolute value of the argument of a piecewise-linear expression
      converted to SOS2 (and further to MIP if SOS2 is not accepted natively).
      In the MIP reformulation, the solver's feasibility tolerance is
      amplified by up to this value. Not used by default: then an unbounded
      argument is an error in the MIP reformulation, and native SOS2 gets
      exact rays for unbounded sides. Use with care (prefer tight bounds).

cvt:plapprox:domain (plapprox:domain, plapproxdomain)
      For piecewise-linear approximated functions, both arguments and result
      are bounded to +-[pladomain]. Default 1e6.

cvt:plapprox:reltol (plapprox:reltol, plapproxreltol)
      Relative tolerance for piecewise-linear approximation. Default 0.01.

cvt:pow2_as_qp (pow2_as_qp, pow2asqp)
      0/1*: whenever both quadratics and ^2 are accepted, submit (expr)^2 as
      out-multiplied quadratics, if (expr) is linear.

      See also cvt:multoutcard, cvt:quadobj, cvt:quadcon.

cvt:pre:all
      0/1*: Set to 0 to disable most presolve in the flat converter.

cvt:pre:auxint (auxint)
      0*/1: Submit as integer the auxiliary result variables whose integrality
      is implied by their defining constraint (if-then-else, min, max, abs,
      count, numberof, integer linear and quadratic functions of integer
      arguments). Default 0: submit them as continuous (MP keeps the
      integrality for its reformulations). Variables required to have their
      type by a submitted constraint, e.g., indicator binaries, are not
      affected.

cvt:pre:boundlogarg (boundlogarg)
      0*/1: Bound logarithm arguments to nonnegative.

cvt:pre:boundsbest (boundsbest, bestbounds)
      0*/1/2/3/4: Submit best-known variable bounds to the solver (can inhibit
      its presolve):

      0 - no, hard bounds only
      1 - all variables
      2 - all but the result variables of smooth nonlinear expressions (exp,
      log, pow, trigonometric functions, divisions, products), which keep
      their hard bounds
      3 - only those variables
      4 - all variables if the submitted model has no nonlinear or quadratic
      constraints or objectives, none otherwise (for solvers whose nonlinear
      relaxations are solved by a barrier method; MP2NL sets it for such
      subsolvers).

      Note: when a variable can be fixed, the stronger bounds are always
      submitted.

cvt:pre:continuous_fixed_vars (continuous_fixed_vars, ctg_fixed)
      0/1*: Make fixed variables continuous, to avoid fake MIPs.

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

cvt:pre:ctx:call (ctx:call)
      Context propagation for 'Call' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:ceil (ctx:ceil)
      Context propagation for 'Ceil' expression, see cvt:pre:ctx:abs.

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

cvt:pre:ctx:floor (ctx:floor)
      Context propagation for 'Floor' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:ifthen (ctx:ifthen)
      Context propagation for 'IfThen' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:impl (ctx:impl)
      Context propagation for 'Implication' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:intdiv (ctx:intdiv)
      Context propagation for 'IntDiv' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:linfn (ctx:linfn)
      Context propagation for 'LinearFunctionalConstraint' expression, see
      cvt:pre:ctx:abs.

cvt:pre:ctx:log (ctx:log)
      Context propagation for 'Log' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:loga (ctx:loga)
      Context propagation for 'LogA' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:logi (ctx:logi)
      Context propagation for 'Logistic' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:max (ctx:max)
      Context propagation for 'Max' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:min (ctx:min)
      Context propagation for 'Min' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:mod (ctx:mod)
      Context propagation for 'Mod' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:mul (ctx:mul)
      Context propagation for 'Mul' expression, see cvt:pre:ctx:abs.

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

cvt:pre:ctx:powc (ctx:powc)
      Context propagation for 'PowConstExp' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:quadfn (ctx:quadfn)
      Context propagation for 'QuadraticFunctionalConstraint' expression, see
      cvt:pre:ctx:abs.

cvt:pre:ctx:round (ctx:round)
      Context propagation for 'Round' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:sdpdotprod (ctx:sdpdotprod)
      Context propagation for 'SDPDotProd' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:signpowc (ctx:signpowc)
      Context propagation for 'SignpowConstExp' expression, see
      cvt:pre:ctx:abs.

cvt:pre:ctx:sin (ctx:sin)
      Context propagation for 'Sin' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:sinh (ctx:sinh)
      Context propagation for 'Sinh' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:tan (ctx:tan)
      Context propagation for 'Tan' expression, see cvt:pre:ctx:abs.

cvt:pre:ctx:tanh (ctx:tanh)
      Context propagation for 'Tanh' expression, see cvt:pre:ctx:abs.

cvt:pre:disj2ind (disj2ind)
      Absorb static disjunctions l || C, where C is a conditional comparison
      used only there (or an AND of such), into indicator constraints !l ==>
      C. This is how implications b==1 ==> C are received from AMPL. Bitwise
      OR of the following values:

      1 - Linear comparisons
      2 - Quadratic comparisons
      4 - Both disjuncts absorbable: absorb one into an indicator on the
      other's result (if-else shape, complementarity)
      8 - Comparisons x==k awaiting the unary encoding decision for x
      (absorbed only if no encoding is chosen)
      16 - Any AND of such comparisons (used only there) in positive context,
      e.g., a disjunct (C1 && C2) of a multi-term disjunction: indicators on
      the AND's result variable
      32 - Static disjunctions l1 || .. || lm || (y1 && .. && yk) with the AND
      used only there: clauses l1 || .. || lm || yj, without the AND's result
      variable.

      Requires cvt:pre:all=1. Default 11.

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

cvt:pre:logistic (cvt:logistic)
      0*/1: recognize logistic functions in the model, see acc:logistic.

cvt:pre:prod (cvt:prod)
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

cvt:pre:signpow (cvt:signpow)
      0*/1: recognize signpow() functions in the model, such as abs(x)*x, see
      acc:signpow.

cvt:pre:sort (cvt:sort)
      0/1*: Sort and eliminate duplicates in arguments of AND, OR, MIN, MAX.
      Sort arguments of COUNT, ATLEAST, EXACTLY, ATMOST, NUMBEROF, ALLDIFF.
      Can be necessary for some solvers.

cvt:pre:unnest (cvt:unnest, cvt:pre:inline, cvt:inline)
      Inline nested expressions. Bitwise OR of the following values:

      1 - AND/FORALL and OR/EXISTS expressions
      2 - Linear subexpressions in algebraic constraints
      4 - Linear and quadratic subexpressions in algebraic constraints
      8 - MIN/MAX
      16 - Algebraic subexpressions in indicator constraints.

      See also option cvt:dvelim concerning only the input model. Default 31.

cvt:pre:vbnd (vbnd)
      Comparisons x (cmp) c decided by the domain of x reuse an existing
      binary instead of a new reified comparison. Bitwise OR of the following
      values:

      1 - Variable-bound constraints x >= L*b, x <= U*b with binary b (AMPL's
      encoding of x in {0} union interval[L, U], or the user's), 0 <= c <= L:
      reuse b or its negation
      2 - Root disjunctions x <= a || x >= b (e.g., x == 0 || x >= L for x >=
      0), a < c < b: reuse the comparison x >= b or its negation.

      Default 3.

cvt:qp2passes (cvt:qp2pass, qp2passes, qp2pass)
      0/1*: Parse sums of QP expressions in 2 passes. Usually faster.

cvt:quadcon (passquadcon)
      0/1*: set to 0 to disable quadratic constraints. Synonym for
      acc:quad..=0. Setting to 0 disables out-multiplication of quadratic
      terms, then they are linearized.

cvt:quadobj (passquadobj)
      0/1*: Pass quadratic objective terms to the solver. When 0, if the
      solver accepts quadratic constraints, such a constraint will be created
      with those, otherwise linearly approximated. With cvt:nlobj=0, ensures
      the objective is linear.

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
      rework; we recommend to switch off PL expression linearization in AMPL
      (option pl_linearize 0).

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

iis:find (iisfind, iis, alg:iisfind)
      Whether to find and export an IIS. Default = 0 (don't export).

iis:strategy (iis_strategy, iisstrategy)
      Strategy for IIS calculation (with iis:find=1), -1 or a sum of:

      -1 - Automatic: 6 (default)
      0  - Light test only (infeasible bounds)
      1  - Try dual ray
      2  - Try elastic LP
      4  - Find an irreducible (true) IIS by a deletion filter
      8  - Prioritise columns over rows in the deletion filter
      16 - Find the IIS of the LP relaxation for a MIP

      HiGHS presets: 6 = true IIS with row priority, 14 = true IIS with column
      priority. HiGHS's IIS finder is LP-based: for a MIP, the reported rows
      and bounds form an infeasible subsystem found by solving elastic MIPs,
      which cannot be proven irreducible; with 16, integrality is dropped and
      the IIS of the LP relaxation is sought.

lim:iistime (iistimelim, lim:iis_time_limit, iis_time_limit, iistimelimit)
      Time limit for computing IIS (default: no limit).

lim:iter (iterlim, lim:simplexiterationlimit, simplexiterationlimit, simplex_iteration_limit)
      Limit on simplex iterations when solving LPs, not counting MIP
      subproblems (default: no limit).

lim:leavenodes (leaveslim, mip_max_leaves)
      Maximum MIP number of leaf nodes (default: no limit).

lim:nodes (nodelim, nodelimit, mip_max_nodes)
      Maximum MIP nodes to explore (default: no limit).

lim:objectivebound (objective_bound, objectivebound)
      Objective bound for termination of the dual simplex solver (default: no
      limit).

lim:objectivetarget (objective_target, objectivetarget)
      Objective target for termination of the MIP solver (default: no limit).

lim:pdlpiter (pdlpiterlim, lim:pdlp_iteration_limit, pdlpiterationlimit, pdlp_iteration_limit)
      Iteration limit for PDLP solver (default: no limit).

lim:qpiter (qpiterlim, lim:qp_iteration_limit, qp_iteration_limit, qpiterationlimit)
      Iteration limit for QP active set method (default: no limit).

lim:sol (sollim, lim:improvingsols, improvingsolslimit, mip_max_improving_sols)
      Stop the MIP solver after this many improving solutions have been found
      (default: no limit).

lim:stallnodes (stallnodelim, stallnodelimit, mip_max_stall_nodes)
      Maximum MIP number of nodes where estimate is above cutoff bound
      (default: no limit).

lim:time (timelim, timelimit, time_limit)
      Limit on solve time (in seconds; default: no limit).

mip:basis (fixmodel, mip:fix)
      Whether to compute duals / basis / sensitivity for MIP models. Emulated
      by fixing integer variables to an incumbent and solving a continuous
      model. Currently supports linear algebraic models only (no SOS,
      piecewise-linear, logical, or general constraints).

      0 - No (default)
      1 - Yes.

mip:basis:iterlimit
      Iteration limit for the fixed-model solve only. -1 (default) uses the
      solver default. For emulation, 0 skips the supplementary solve.

mip:basis:timelimit
      Time limit in seconds for the fixed-model solve only. -1 (default) uses
      the solver default, independently of the MIP time limit. For emulation,
      0 skips the supplementary solve.

mip:bestbound (bestbound, return_bound)
      Whether to return suffix .bestbound for the best known MIP dual bound on
      the objective value:

      0 - No (default)
      1 - Yes.

      The suffix is on the objective and problem and is -Infinity for
      minimization problems and +Infinity for maximization problems if there
      are no integer variables or if a dual bound is not available.

mip:gap (mipgap, mip:relgaptol, relgaptol, mip_rel_gap)
      Tolerance on relative gap, | ub - lb|/|ub | , to determine whether
      optimality has been reached for a MIP instance (default 1e-04).

mip:gapabs (mipgapabs, mip:absgaptol, absgaptol, mip_abs_gap)
      Tolerance on absolute gap of MIP, |ub-lb|, to determine whether
      optimality has been reached for a MIP instance (default 1e-06).

mip:heur:feasjump (heurfeasjump, mip_heuristic_run_feasibility_jump)
      0/1*: Use the feasibility jump heuristic.

mip:heur:rens (heurrens, mip_heuristic_run_rens)
      0/1*: Use the RENS heuristic.

mip:heur:rins (heurrins, mip_heuristic_run_rins)
      0/1*: Use the RINS heuristic.

mip:heur:rootredcost (heurrootredcost, mip_heuristic_run_root_reduced_cost)
      0/1*: Use the root reduced cost heuristic.

mip:heur:shifting (heurshifting, mip_heuristic_run_shifting)
      0*/1: Use the Shifting heuristic.

mip:heur:ziround (heurziround, mip_heuristic_run_zi_round)
      0*/1: Use the ZI Round heuristic.

mip:heureff (heureff, mip_heuristic_effort)
      Fraction of time to spend in MIP heuristics (default 0.05).

mip:intfeastol (intfeastol, inttol, mip_feasibility_tolerance)
      Feasibility tolerance for integer variables (default 1e-06).

mip:ipmsolver (mipipmsolver, mip_ipm_solver)
      Choose the ipm solver to be used during mip solves:

      choose - Automatic (default)
      ipx    - IPX interior point method
      hipo   - HiPO interior point method

mip:lifting (lifting, mip_lifting_for_probing)
      Level of lifting for probing that is used (default -1).

mip:lpagelimit (lpagelimit, mip_lp_age_limit)
      Maximal age of dynamic LP rows before they are removed from the LP
      relaxation (default 10, max 32767).

mip:lpsolver (miplpsolver, mip_lp_solver)
      Choose the lp solver to be used during mip solves:

      choose  - Automatic (default)
      simplex - Simplex
      ipm     - Interior Point Method (automatic)
      hipo    - HiPO interior point method
      ipx     - IPX interior point method

mip:maxstartnodes (maxstartnodes, mip_max_start_nodes)
      Maximum number of MIP nodes when completing a partial MIP start (default
      500). See mip:start.

mip:mincliquetable (mincliquetable, mip_min_cliquetable_entries_for_parallelism)
      Minimal number of entries in the cliquetable before neighborhood queries
      of the conflict graph use parallel processing (default 100000).

mip:nodecuts (nodecuts, mip_allow_cut_separation_at_nodes)
      0/1*: Whether cut separation at nodes other than the root is permitted.

mip:plateau:absgaptol (mip:plateauabsgaptol, plateauabsgaptol)
      If set (>0), also track the reported absolute MIP gap as progress for
      mip:plateautime: the plateau timer resets whenever the absolute gap
      shrinks by at least this amount. Default 0 (disabled).

mip:plateau:abstol (mip:plateauabstol, plateauabstol)
      Minimum absolute objective improvement to reset the mip:plateautime
      timer. Default 0 (any improvement resets the timer).

mip:plateau:log (mip:plateaulog, plateaulog)
      Whether to print the current plateau status. Default 0 (silent).

mip:plateau:relgaptol (mip:plateaurelgaptol, plateaurelgaptol)
      If set (>0), also track the reported relative MIP gap as progress for
      mip:plateautime: the plateau timer resets whenever the relative gap
      shrinks by at least this amount. Default 0 (disabled).

mip:plateau:reltol (mip:plateaureltol, plateaureltol)
      Minimum relative objective improvement, as a fraction of the current
      value, to reset the mip:plateautime timer. Default 0.

mip:plateau:time (mip:plateautime, plateautime)
      Stop the MIP search if the incumbent objective (and, if
      mip:plateauabsgaptol/mip:plateaurelgaptol are set, the MIP gap) has not
      improved by at least mip:plateauabstol or mip:plateaureltol for this
      many seconds. Default 0 (disabled).

mip:plateau:warmup (mip:plateauwarmup, plateauwarmup)
      Grace period (in seconds) after the solve starts before mip:plateautime
      is checked. Default 0.

mip:plateau:warmup:absgap (mip:plateauwarmupabsgap, plateauwarmupabsgap)
      Absolute MIP gap to be reached before mip:plateautime is checked.
      Default 0.

mip:plateau:warmup:relgap (mip:plateauwarmuprelgap, plateauwarmuprelgap)
      Relative MIP gap to be reached before mip:plateautime is checked.
      Default 0.

mip:poolagelimit (poolagelimit, mip_pool_age_limit)
      Maximal age of rows in the MIP cutpool before they are deleted (default
      30, max 1000).

mip:poolsoftlimit (poolsoftlimit, mip_pool_soft_limit)
      Soft limit on the number of rows in the cutpool for dynamic age
      adjustment (default 10000).

mip:pscostreliability (pscostreliability, mip_pscost_minreliable)
      Minimal number of observations before pseudo costs are considered
      reliable (default 8).

mip:restart (miprestart, mip_allow_restart)
      0/1*: Whether MIP restart is permitted.

mip:return_gap (return_mipgap)
      Whether to return mipgap suffixes or include mipgap values (|objectve -
      .bestbound|) in the solve_message: sum of

      1 - Return .relmipgap suffix (relative to |obj|)
      2 - Return .absmipgap suffix (absolute mipgap)
      4 - Suppress mipgap values in solve_message.

      Default = 0. The suffixes are on the objective and problem. Returned
      suffix values are +Infinity if no integer-feasible solution has been
      found, in which case no mipgap values are reported in the solve_message.

mip:rootpresolveonly (rootpresolveonly, mip_root_presolve_only)
      0*/1: Whether MIP presolve is only applied at the root node.

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

mip:start (mipstart)
      How a partial MIP start (initial values for some integer variables, with
      alg:start>0) is completed:

      1 - Pass the provided values to HiGHS, which completes a partial start
          itself by a limited MIP search (see mip:maxstartnodes; default)
      2 - Complete a partial start in the driver: fix the provided values of
          integer variables, solve, unfix, and pass the complete solution
          (legacy behavior)

mip:symmetry (symmetry, mip:detsimmetry, detsimmetry, mip_detect_symmetry)
      0/1*: Whether MIP symmetry should be detected.

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
      especially for LP, and only allow linear objectives. See the solver
      documentation and options cvt:quadobj, cvt:nlobj.

obj:multi:options (multiobjoptions)
      0/1*: Regard multiobjective option suffixes which are objective suffixes
      beginning with option_. Example: suffix option_timelim; let
      _obj[2].option_timelim:=15;

obj:multi:stats (multiobjstats)
      0*/1: Report multiobjective pass statistics in the following objective
      suffixes:

      * .objpass: index of the pass where this objective was solved, 0 if not
        solved due to a stop in a previous pass

      * .objpass_result: the solve_result of the pass where this objective was
        solved; -1 if not

      * .objpass_runtime, _mipgap, _objval, _objbound, _work, _itercount,
        _nodecount, _opennodecount if available.

      With MP's emulation (obj:multi=2), _objval and _objbound refer to the
      blended pass objective in the sense of the first objective, and _runtime
      is the wall-clock time of the pass including model updates; numeric
      statistics are NaN if not available for a pass. If the solver's native
      multiobjective mode does not report pass statistics, use obj:multi=2.

      See also tech:stats.

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

pdlp:opttol (pdlpopttol, pdlp:optimality_tolerance, pdlp_optimality_tolerance, pdlp_opt_tol)
      PDLP optimality tolerance (default 1e-7).

pdlp:restart (pdlprestart, pdlp:restart_strategy, pdlprestartstrategy, pdlp_restart_strategy)
      Restart strategy for PDLP solver:

      0 - Off
      1 - Fixed
      2 - Adaptive (default)
      3 - Halpern

pdlp:restartmethod (pdlprestartmethod, pdlp:cupdlpc_restart_method, pdlpcupdlpcrestartmethod, pdlp_cupdlpc_restart_method)
      Restart mode for PDLP solver:

      0 - None
      1 - GPU (default)
      2 - CPU

pdlp:ruiziter (pdlpruiziter, pdlp:ruiz_iterations, pdlp_ruiz_iterations)
      Number of Ruiz scaling iterations for PDLP solver (default 10).

pdlp:scaling (pdlpscaling, pre:pdlpscaling_mode, pdlp_scaling_mode)
      Scaling mode for PDLP solver (default 5 = 1 + 4), sum of:

      1 - Ruiz scaling
      2 - L2
      4 - PC (preconditioner-oriented)

pdlp:stepsize (pdlpstepsize, pdlp:step_size_strategy, pdlpstepsizestrategy, pdlp_step_size_strategy)
      Stepsize strategy for PDLP solver:

      0 - Fixed
      1 - Adaptive (default)
      2 - Malitsky-Pock
      3 - PID

pre:solve (presolve)
      Whether to use presolve:

      choose - Automatic (default)
      off    - Off
      on     - On

pre:userboundscale (user_bound_scale, userboundscale)
      Exponent of power-of-two bound scaling for model (default 0; negative
      exponents allowed).

pre:userobjectivescale (user_objective_scale, userobjectivescale)
      Exponent of power-of-two objective scaling for model (default 0;
      negative exponents allowed).

qp:hotstart (qphotstart, qp_allow_hot_start)
      0*/1: Allow the active set QP solver to hot start.

qp:nullspacelim (qpnullspacelim, qp:nullspace_limit, qp_nullspace_limit, qpnullspacelimit)
      Nullspace limit for the active set QP solver (default: 4000).

qp:regularization (qpregularization, qp:regularization_value, qp_regularization_value, qpregularizationvalue)
      Regularization value added to the Hessian in the active set QP solver
      (default: 1e-7).

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

sol:report_uncertain (report_uncertain_sol)
      0/1*: whether to report objective value(s) in solve_message when
      solve_result is '?' (unknown).

tech:debug (debug)
      0*/1: whether to assist testing & debugging, e.g., by outputting
      auxiliary information (mostly via suffixes).

tech:logfile (logfile)
      Log file name.

tech:logtoconsole (logtoconsole, log_to_console)
      0/1*: Whether HiGHS log lines go to the console (with tech:outlev=1; set
      0 to log only to tech:logfile).

tech:miplogfreq (miplogfreq, mip_min_logging_interval)
      Minimum interval between MIP log lines, in seconds (default 5).

tech:miploglev (miploglev, mip_report_level)
      0/1*/2: MIP solver report level

tech:optionfile (optionfile, option:file)
      Name of an AMPL solver option file to read (surrounded by 'single' or
      "double" quotes if the name contains blanks). Lines that start with #
      are ignored. Otherwise, each nonempty line should contain "name=value",
      e.g., "lim:iter=500".

tech:outlev (outlev)
      0*/1: Whether to write HiGHS log lines (chatter) to stdout and to file.

tech:outlev_mp (outlev_mp)
      0*/1: whether to print MP model information.

tech:seed (seed, random_seed)
      Random number seed (default 0), affecting perturbations that may
      influence the solution path.

tech:stats (stats, tech:report_stats, solve_stats)
      Whether to return solve statistics and timings; the information will be
      stored in the problem suffixes: 'simplex_iterations',
      'barrier_iterations', 'nodes' and possibly other solver-dependent
      suffixes. A JSON representation of the information above is returned in
      the problem suffix `stats`.
      Note that timing information will also be included in the JSON
      representation if tech:timing>0. Values:

      0 - Do not report statistics (default)
      1 - Report statistics in JSON format in the problem suffix 'stats'
      2 - Report statistics in suffixes
      3 - Report statistics both in suffixes and the suffix 'stats'.

      See also obj:multi:stats.

tech:threads (threads)
      Maximum number of threads used by HiGHS (parallel simplex, IPM and MIP);
      default 0 ==> automatic choice.

tech:timelesslog (timelesslog, timeless_log)
      0*/1: Suppress time-based data in the HiGHS log.

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

tech:writesolution (writesol, writesolution)
      Specifies the names of files where to export the solution and/or other
      result files in solver's native formats. Option can be repeated.
```

