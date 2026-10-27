
# MOSEK Options

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

'' Options:

acc:_all
      Solver acceptance level for all constraints and expressions. Value
      meaning: as described in the specific acc:... options.

      Can be useful to disable all reformulations (acc:_all=2), or force
      linearization (acc:_all=0.)

acc:expcone
      Solver acceptance level for 'ExponentialConeConstraint' as flat
      constraint, default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

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

acc:quadcone
      Solver acceptance level for 'QuadraticConeConstraint' as flat
      constraint, default 2:

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

acc:quadrange (acc:quadrng)
      Solver acceptance level for 'QuadConRange' as flat constraint, default
      2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:rotatedquadcone
      Solver acceptance level for 'RotatedQuadraticConeConstraint' as flat
      constraint, default 2:

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

alg:dualfeastol (basistols)
      Dual feasibility tolerance of the simplex optimizers
      (MSK_DPAR_BASIS_TOL_S, min 1e-9, default 1e-6).

alg:feastol (basistolx)
      Primal feasibility tolerance of the simplex optimizers
      (MSK_DPAR_BASIS_TOL_X, min 1e-9, default 1e-6).

alg:method (method, lpmethod, simplex)
      Which algorithm to use for non-MIP problems or for the root node of MIP
      problems:

      0 - Optimizer for conic constraints
      1 - Dual simplex
      2 - Automatic (default)
      3 - Free simplex
      4 - Interior-point method
      5 - Mixed-integer optimizer
      6 - New dual simplex (MOSEK 11)
      7 - New primal simplex (MOSEK 11)
      8 - Primal simplex

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

alg:start (warmstart)
      Whether to use incoming primal (and dual, for LP) variable values in a
      warmstart:

      0 - No
      1 - Yes (for LP: if there is no incoming alg:basis)
      2 - Yes (for LP: omitting the incoming alg:basis, if any)
      3 - Yes (for LP: together with the incoming alg:basis, if any;
          default).

bar:basis (bar:crossover, crossover)
      Whether the interior-point optimizer also computes an optimal basis:

      0 - Never
      1 - Always (default)
      2 - If no error detected
      3 - If primal and dual feasible

bar:codfeastol (intpntcotoldfeas)
      Dual feasibility tolerance of the interior-point optimizer for conic
      problems (0..1, default 1e-8).

bar:copfeastol (intpntcotolpfeas)
      Primal feasibility tolerance of the interior-point optimizer for conic
      problems (0..1, default 1e-8).

bar:corelgaptol (intpntcotolrelgap)
      Relative gap termination tolerance of the interior-point optimizer for
      conic problems (0..1, default 1e-8).

bar:dfeastol (intpnttoldfeas)
      Dual feasibility tolerance of the interior-point optimizer for linear
      problems (0..1, default 1e-8).

bar:iterlim (bariterlim)
      Interior-point iteration limit (default 400).

bar:order (intpntordermethod)
      Ordering method of the interior-point optimizer:

      0 - Automatic (default)
      1 - Approximate minimum local fill-in
      2 - Experimental
      3 - Try graph partitioning
      4 - Force graph partitioning
      5 - No ordering

bar:pfeastol (intpnttolpfeas)
      Primal feasibility tolerance of the interior-point optimizer for linear
      problems (0..1, default 1e-8).

bar:relgaptol (intpnttolrelgap)
      Relative gap termination tolerance of the interior-point optimizer for
      linear problems (min 1e-14, default 1e-8).

bar:solveform (intpntsolveform)
      Whether the interior-point optimizer solves the primal or the dual
      problem:

      0 - Automatic (default)
      1 - Solve the primal problem
      2 - Solve the dual problem

cut:clique (cliquecuts)
      0/1: whether to generate clique cuts (default 1)

cut:cover (covercuts, cut:knapsackcover)
      0/1: whether to generate knapsack cover cuts (default 1)

cut:gomory (gomorycuts, cut:gmi)
      0/1: whether to generate Gomory mixed-integer cuts (default 1)

cut:implied (impliedcuts, cut:impliedbound)
      0/1: whether to generate implied bound cuts (default 1)

cut:lipro (liprocuts)
      0/1: whether to generate lift-and-project cuts (default 0)

cut:mir (mircuts, cut:cmir)
      0/1: whether to generate complemented mixed-integer rounding cuts
      (default 1)

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
      0/1*: Recognize exponential cones.

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
      conic and quadratic constraints/objectives. Default: 1.

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

lim:iter (iterlim, simmaxiterations)
      Simplex iteration limit (default 10000000).

lim:lowerobjcut (lowerobjcut)
      Lower objective cut: MOSEK stops when it proves that the optimal
      objective value is below this (default -infinity). With lim:upperobjcut
      this is MOSEK's objective range, reported as 'objective range'
      (solve_result 406).

lim:miptime (miptimelim)
      Time limit for the mixed-integer optimizer in seconds
      (MSK_DPAR_MIO_MAX_TIME; default -1: no limit; lim:time applies too).

lim:nodes (nodelim, nodelimit)
      Limit on the number of MIP branches (MSK_IPAR_MIO_MAX_NUM_BRANCHES;
      default -1: no limit).

lim:sol (sollim, sollimit, solutionlimit)
      Limit on the number of feasible MIP solutions found, causing early
      termination if exceeded; default -1 (no limit).

lim:time (timelim, timelimit, time_limit)
      Limit on solve time (in seconds; default -1: no limit).

lim:upperobjcut (upperobjcut)
      Upper objective cut: MOSEK stops when it proves that the optimal
      objective value is above this (default +infinity).

lp:degen (simdegen)
      Degeneration handling of the simplex optimizers:

      0 - No degeneration handling
      1 - Automatic (default)
      2 - Aggressive
      3 - Moderate
      4 - Minimum

lp:dualselection (dualselection)
      Pricing strategy of the dual simplex optimizer:

      0 - Automatic (default)
      1 - Full pricing
      2 - Approximate steepest edge
      3 - Devex pricing
      4 - Steepest edge
      5 - Partial pricing

lp:hotstart (simhotstart)
      Hot start of the simplex optimizers:

      0 - No hot start
      1 - Automatic (default)
      2 - Hot start from the status keys only

lp:primalselection (primalselection)
      Pricing strategy of the primal simplex optimizer:

      0 - Automatic (default)
      1 - Full pricing
      2 - Approximate steepest edge
      3 - Devex pricing
      4 - Steepest edge
      5 - Partial pricing

lp:solveform (simsolveform)
      Whether the simplex optimizers solve the primal or the dual problem:

      0 - Automatic (default)
      1 - Solve the primal problem
      2 - Solve the dual problem

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

mip:branchdir (branchdir)
      Branching direction of the mixed-integer optimizer:

      0 - Automatic (default)
      1 - Up
      2 - Down
      3 - Nearest integer
      4 - Farthest integer
      5 - Towards the root LP value
      6 - Guided by the incumbent
      7 - By pseudo costs

mip:conic:outapprox (conicoutapprox)
      0*/1: If this option is turned on outer approximation is used when
      solving relaxations of conic problems; otherwise interior point is used.

mip:constructsol (mipconstructsol)
      Sets MSK_IPAR_MIO_CONSTRUCT_SOL. If set to MSK_ON and all integer
      variables have been given a value for which a feasible mixed integer
      solution exists, then MOSEK generates an initial solution to the mixed
      integer problem by fixing all integer values and solving the remaining
      problem.Default = OFF

mip:cuts (cuts, mip:cutselection)
      Cut selection level of the mixed-integer optimizer:

      -1 - Automatic (default)
      0  - Generated cuts are less likely to be added
      1  - Cuts are selected more aggressively

mip:djcbigm (djcmaxbigm)
      Maximal big-M value used when disjunctive constraints are reformulated
      by the mixed-integer optimizer (default 1e6).

mip:feaspump (feaspump)
      MIP feasibility pump.

      -1 - Automatic (default)
      0  - The Feasibility Pump is disabled
      1  - The Feasibility Pump is enabled with an effort to improve solution
           quality
      2  - The Feasibility Pump is enabled with an effort to reach
           feasibility early

mip:feastol (feastol)
      Feasibility tolerance for the mixed-integer optimizer (1e-9..1e-3,
      default 1e-6). Note: in this driver, 'feastol' is this MIP tolerance;
      the LP tolerances are alg:feastol (simplex) and bar:pfeastol
      (interior-point).

mip:gap (mipgap)
      Max. relative MIP optimality gap (default 1e-4).

mip:gapabs (mipgapabs)
      Max. absolute MIP optimality gap (default 0.0).

mip:heurlevel (heurlevel)
      MIP heuristic level to find an initial good feasible solution.

      -1: automatic (default);
      0: not used;
      positive, larger - more effort (3-5 recommended).

mip:inttol (inttol, intfeastol, mip:intfeastol)
      MIP integrality tolerance (min 1e-9, default 1e-5).

mip:nodemethod (nodemethod, mip:nodeoptimizer)
      Optimizer for the node relaxations of a mixed-integer problem:

      0 - Optimizer for conic constraints
      1 - Dual simplex
      2 - Automatic (default)
      3 - Free simplex
      4 - Interior-point method
      6 - New dual simplex
      7 - New primal simplex
      8 - Primal simplex

mip:nodeselect (nodeselect, mip:nodeselection)
      Node selection strategy of the mixed-integer optimizer:

      0 - Automatic (default)
      1 - Depth first (first)
      2 - Best bound
      3 - Best estimate using pseudo costs

mip:probing (probing)
      Amount of probing in the presolve of the mixed-integer optimizer:

      -1 - Automatic (default)
      0  - Disabled
      1  - Low amount of probing
      2  - Medium amount of probing
      3  - High amount of probing

mip:relgapconst (miorelgapconst)
      This value is used to compute the relative gap for the solution to an
      integer optimization problem (min 1e-15, default 1e-10).

mip:restarts (maxrestarts)
      Maximal number of restarts of the mixed-integer optimizer (default 10).

mip:return_gap (return_mipgap)
      Whether to return mipgap suffixes or include mipgap values (|objectve -
      .bestbound|) in the solve_message: sum of

      1 - Return .relmipgap suffix (relative to |obj|)
      2 - Return .absmipgap suffix (absolute mipgap)
      4 - Suppress mipgap values in solve_message.

      Default = 0. The suffixes are on the objective and problem. Returned
      suffix values are +Infinity if no integer-feasible solution has been
      found, in which case no mipgap values are reported in the solve_message.

mip:rinsmaxnodes (rinsmaxnodes)
      Maximal number of nodes in each RINS heuristic run (-1: automatic,
      default; 0: RINS off).

mip:rootcutrounds (rootcutrounds)
      Maximal number of cut separation rounds at the root node (default 100).

mip:rootmethod (rootmethod, mip:rootoptimizer)
      Optimizer for the root relaxation of a mixed-integer problem:

      0 - Optimizer for conic constraints
      1 - Dual simplex
      2 - Automatic (default)
      3 - Free simplex
      4 - Interior-point method
      6 - New dual simplex
      7 - New primal simplex
      8 - Primal simplex

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

mip:symmetry (symmetry, pre:mipfolding, mipfolding, miosimmetrylevel)
      Amount of symmetry detection and handling by the mixed-integer optimizer
      (MSK_IPAR_MIO_SYMMETRY_LEVEL):

      -1 - Automatic (default)
      0  - Disabled
      1  - Low amount
      2  - Medium amount
      3  - High amount
      4  - Extremely high amount

mip:varselection (varselection)
      Controls the variable selection strategy employed by the mixed-integer
      optimizer:

      0 - Automatic (default)
      1 - Pseudocost variable selection
      2 - Strong branching selection

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

pre:aggregate (aggregate)
      Whether to use aggregation in presolve:

      0 - No
      1 - Yes (default)

pre:dualray_analysis (dualrayanalysis)
      Controls the amount of dual ray analysis employed by the mixed-integer
      optimizer:

      -1 - Automatic (default)
      0  - Disabled
      1  - Low amount of analyis
      2  - Higher amount of analysis

pre:folding (folding, foldinguse)
      Whether to use folding in presolve (for MIP problems use mip:symmetry):

      0 - Disabled
      1 - The solver decides on the usage and amount of folding
      2 - If only the interior-point solution is requested then the solver
          decides; if the basic solution is requested then folding is disabled
          (default)
      3 - Full folding is always performed regardless of workload

pre:lindep (lindep)
      0/1: whether presolve removes linearly dependent rows (default 1).

pre:passes (prepasses)
      Limit on the number of presolve passes; a negative value implies MOSEK
      decides:

      -1 - Automatic choice (default)
      n>=0 - At most n passes.

pre:scale (scale)
      Whether to use scaling in presolve. Applies to both simplex and interior
      point method:

      0 - Mosek chooses scaling heuristic (default)
      1 - No scaling.

pre:solve (presolve)
      MIP presolve:

      0 - Do not use presolve
      1 - Use presolve
      2 - Automatic (default)

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
      Log file name. Without tech:outlev=1 the log goes to the file only.

tech:lpseed (lpseed)
      Sets the random seed (0..32749, default 23456) used for randomization in
      the simplex optimizers.

tech:optionfile (optionfile, option:file)
      Name of an AMPL solver option file to read (surrounded by 'single' or
      "double" quotes if the name contains blanks). Lines that start with #
      are ignored. Otherwise, each nonempty line should contain "name=value",
      e.g., "lim:iter=500".

tech:optionnative (optionnative, optnative, tech:param)
      General way to specify values of both documented and undocumented Mosek
      parameters; value should be a quoted string (delimited by ' or ")
      containing a parameter name, a space, and the value to be assigned to
      the parameter. Can appear more than once. Cannot be used to query
      current parameter values.

tech:optionnativeread (optionnativeread, tech:param:read, param:read)
      Name of Mosek parameter file (surrounded by 'single' or "double" quotes
      if the name contains blanks) to be read. File format:

      BEGIN MOSEK
      MSK_DPAR_MIO_MAX_TIME 3
      END MOSEK

      Parameter descriptions:
      docs.mosek.com/latest/cmdtools/param-groups.html.

tech:optionnativewrite (optionnativewrite, tech:param:write, param:write)
      Name of Mosek parameter file (surrounded by 'single' or "double" quotes
      if the name contains blanks) to be written.

tech:outlev (outlev)
      0*/1: Whether to write MOSEK log lines to stdout (MSK_IPAR_LOG; larger
      levels can be set with tech:optionnative).

tech:outlev_mp (outlev_mp)
      0*/1: whether to print MP model information.

tech:seed (seed, tech:mipseed, mipseed)
      Random number seed (default 42), used for randomization in the
      mixed-integer optimizer, may influence the solution path.

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
      Controls the number of threads employed by the optimizer. Default 0 ==>
      number of threads used will be equal to the number of cores detected on
      the machine.

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

