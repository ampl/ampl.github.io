
# GCG Options

```ampl
ampl: option solver gcg; # change the solver
ampl: option gcg_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

Solver options obtained with `$ gcg -=`.

```
GCG Optimizer Options for AMPL
--------------------------------------------

To set these options, assign a string specifying their values to the AMPL
option "gcg_options". For example:

   ampl: option gcg_options 'mipgap=1e-6';

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

alg:dualfeastol (dualfeastol, num:dualfeastol)
      Feasibility tolerance for reduced costs in LP solution (default: 1e-07)

alg:feastol (feastol, num:feastol)
      Feasibility tolerance for constraints (default: 1e-06)

alg:method (method, lpmethod)
      LP algorithm for solving initial LP relaxations:

      s - automatic simplex (default)
      p - primal simplex
      d - dual simplex
      b - barrier (SoPlex has none: runs the dual simplex)
      c - barrier with crossover (SoPlex: dual simplex)

alg:relax (relax)
      0*/1: Whether to relax integrality of variables.

alg:remethod (remethod, relpmethod)
      LP algorithm for resolving LP relaxations if a starting basis exists:

      s - automatic simplex (default)
      p - primal simplex
      d - dual simplex
      b - barrier (SoPlex has none: runs the dual simplex)
      c - barrier with crossover (SoPlex: dual simplex)

branch:preferbinary (preferbinary)
      0/1: whether branching on binary variables should be preferred

      0 - Binary variables should not be preferred on branching (default)

      1 - Binary variables should be preferred on branching.

cut:dircutoffdistweight (dircutoffdistweight)
      Weight of directed cutoff distance in cut score calculation (default:
      0.0)

cut:efficacyweight (efficacyweight)
      Weight of efficacy in cut score calculation (default: 1.0)

cut:intsupportweight (intsupportweight)
      Weight of integral support in cut score calculation (default: 0.1)

cut:maxcuts (maxcuts)
      Maximal number of cuts separated per separation round (0: disable local
      separation; default: 100)

cut:maxcutsroot (maxcutsroot)
      Maximal number of separated cuts per separation round at the root node
      (0: disable root node separation; default: 2000)

cut:maxrounds
      Maximal number of separation rounds per node (default: -1: unlimited)

cut:maxroundsroot
      Maximal number of separation rounds in the root node (default: -1:
      unlimited)

cut:maxstallrounds
      Maximal number of consecutive separation rounds without objective or
      integrality improvement in local nodes (-1: no additional restriction;
      default: 1)

cut:maxstallroundsroot
      Maximal number of consecutive separation rounds without objective or
      integrality improvement in the root node (-1: no additional restriction;
      default: 10)

cut:minactivityquot
      Minimum cut activity quotient to convert cuts into constraints during a
      restart (0.0: all cuts are converted; default: 0.8)

cut:minefficacy
      Minimal efficacy for a cut to enter the LP (default: 0.0001)

cut:minefficacyroot
      Minimal efficacy for a cut to enter the LP in the root node (default:
      0.0001)

cut:minortho (minortho)
      Minimal orthogonality for a cut to enter the LP (0..1; default: 0.9)

cut:minorthoroot (minorthoroot)
      Minimal orthogonality for a cut to enter the LP in the root node (0..1;
      default: 0.9)

cut:objparalweight (objparalweight)
      Weight of objective parallelism in cut score calculation (default: 0.1)

cut:poolfreq
      Separation frequency for the global cut pool (-1: disable global cut
      pool; 0: only separate pool at the root; default: 10)

cut:settings
      0/1/2/3: sets cuts settings

      0 - Sets cuts default (default)

      1 - Sets cuts aggressive

      2 - Sets cuts fast

      3 - Sets cuts off.

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
      0*/1: Pass quadratic objective terms to the solver. When 0, if the
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

det:benders (det:benders-enabled, benders-enabled)
      0/1: whether benders detection should be enabled?

      0 - Benders detection not enabled (default)

      1 - Benders detection enabled.

det:bendersonlybinmaster (det:benders-onlybinmaster, benders-onlybinmaster)
      0/1: whether only decomposition with only binary variables in the master
      are searched?

      0 - Not only decomposition with only binary variables in the master are
      searched (default)

      1 - Only decomposition with only binary variables in the master are
      searched.

det:bendersonlycontsubpr (det:benders-onlycontsubpr, benders-onlycontsubpr)
      0/1: whether only decomposition with only continiuous variables in the
      subproblems are searched?

      0 - Not only decomposition with only continiuous variables in the
      subproblems are searched (default)

      1 - Only decomposition with only continiuous variables in the
      subproblems are searched.

det:classification (det:classification-enabled, classification-enabled)
      0/1: whether classification should be enabled?

      0 - Classification not enabled

      1 - Classification enabled (default).

det:enabled
      0/1: whether detection should be enabled?

      0 - Detection not enabled

      1 - Detection enabled (default).

det:maxnclasses (maxnclasses)
      Maximum number of classes a partition can use for voting on the number
      of blocks (default 18)

det:maxnclassesperpartition (maxnclassesperpartition)
      Maximum number of classes per partition (default: 9)

det:maxnclassesperpartitionforlargeprobs (maxnclassesperpartitionforlargeprobs)
      Maximum number of classes per partition for large problems (nconss +
      nvars >= 50000) (default: 5)

det:maxrounds
      Maximum number of detection loop rounds (default: 1)

det:maxtime
      Maximum detection time in seconds (default: 600)

det:origprob (det:origprob-enabled, origprob-enabled)
      0/1: whether detection for the original problem should be enabled?

      0 - Detection for the original problem not enabled

      1 - Detection for the original problem enabled (default).

det:origprobclassification (det:origprob-classificationenabled, origprob-classificationenabled)
      0/1: whether classification for the original problem should be enabled?

      0 - Classification for the original problem not enabled

      1 - Classification for the original problem enabled (default).

det:postprocess (postprocess)
      0/1: whether postprocessing of complete decompositions should be
      enabled?

      0 - Postprocessing of complete decompositions not enabled

      1 - Postprocessing of complete decompositions enabled (default).

det:scoretype (scoretype)
      Score calculation for comparing (partial) decompositions:

      maxwhi - max white
      border - border area
      classi - classic
      forswh - max foreseeing white
      spfwh  - ppc-max-white (default)
      fawh   - max foreseeing white with aggregation info
      spfawh - ppc-max-white with aggregation info
      bender - experimental benders score
      strong - strong decomposition score

gcg:discretization (discretization)
      0/1: whether discretization (TRUE) or convexification (FALSE) approach
      should be used?

      0 - convexification approach should be used

      1 - discretization approach should be used (default).

gcg:dispinfos (dispinfos)
      0/1: whether additional information about the blocks is displayed
      (default 0).

gcg:enforceproper (enforceproper)
      0/1: whether propagated bound changes in the original problem are
      enforced in the master (only proper variables; default 1).

gcg:mipdiscretization (mipdiscretization)
      0/1: whether discretization (TRUE) or convexification (FALSE) approach
      should be used in mixed-integer programs?

      0 - convexification approach should be used in mixed-integer programs

      1 - discretization approach should be used in mixed-integer programs
      (default).

gcg:mode (mode)
      The decomposition mode that GCG will use:

      0 - Dantzig-Wolfe (default)
      1 - Benders' decomposition
      2 - No decomposition

heu:settings
      0/1/2/3: sets heuristics settings

      0 - Sets heuristics default (default)

      1 - Sets heuristics aggressive

      2 - Sets heuristics fast

      3 - Sets heuristics off.

lim:autorestartnodes
      If solve exceeds this number of nodes for the first time, an automatic
      restart is triggered (default: -1: no automatic restart)

lim:bestbndstop (bestbndstop, lim:dual)
      Solving stops, if the dual bound is at least as good as this value
      (default: no limit)

lim:bestobjstop (bestobjstop, lim:primal)
      Solving stops, if the primal bound is at least as good as this value
      (default: no limit)

lim:bestsol
      Solving stops, if the given number of solution improvements were found
      (default: -1: no limit)

lim:iter (iterlim, lp:iterlim)
      Iteration limit for each single LP solve of the original problem
      (default: -1: no limit). Not a total limit.

lim:maxorigsol
      Maximal number of solutions candidates to store in the solution storage
      of the original problem (default: 10)

lim:maxsol
      Maximal number of solutions to store in the solution storage (default:
      100)

lim:memory (memory, memlim)
      #maximal memory usage in MB; reported memory usage is lower than real
      memory usage! (default: 8796093022207.0)

lim:nodes (nodelim, nodelimit)
      Maximal number of nodes to process (default: -1: no limit)

lim:restarts
      Solving stops, if the given number of restarts was triggered (default:
      -1: no limit)

lim:sol (sollim, solutionlimit, lim:solutions)
      Solving stops, if the given number of solutions were found (default: -1:
      no limit)

lim:stallnodes
      Solving stops, if the given number of nodes was processed since the last
      improvement of the primal solution value (default: -1: no limit)

lim:time (timelim, timelimit, time_limit)
      Limit on solve time (in seconds; default: 1e+20).

lim:totalnodes
      Maximal number of total nodes (incl. restarts) to process (default: -1:
      no limit)

lp:alwaysgetduals (alwaysgetfarkasduals, alwaysgetduals)
      0/1: whether the Farkas duals should always be collected when an LP is
      found to be infeasible

      0 - The Farkas duals should not always be collected when an LP is found
      to be infeasible (default)

      1 - The Farkas duals should always be collected when an LP is found to
      be infeasible.

lp:presolving
      0/1: whether presolving of LP solver should be used

      0 - Presolving of LP solver should not be used

      1 - Presolving of LP solver should be used (default).

lp:pricing (pricing)
      Pricing strategy:

      l - lpi default (default)
      a - auto
      f - full pricing
      p - partial
      s - steepest edge pricing
      q - quickstart steepest edge pricing
      d - devex pricing

lp:scaling (pre:scale, scale)
      LP scaling: 0 none, 1 normal (default), 2 aggressive.

lp:solvedepth
      Maximal depth for solving LP at the nodes (default: -1: no depth limit)

lp:solvefreq
      Frequency for solving LP at the nodes (-1: never; 0: only root LP;
      default: 1)

lp:threads
      Number of threads used for solving the LP (default: 0: automatic)

mip:bestbound (bestbound, return_bound)
      Whether to return suffix .bestbound for the best known MIP dual bound on
      the objective value:

      0 - No (default)
      1 - Yes.

      The suffix is on the objective and problem and is -Infinity for
      minimization problems and +Infinity for maximization problems if there
      are no integer variables or if a dual bound is not available.

mip:gap (mipgap, lim:gap, gap)
      Solving stops, if the relative gap = |primal -
      dual|/MIN(|dual|,|primal|) is below the given value, the gap is
      'Infinity', if primal and dual bound have opposite signs (default: 0.0)

mip:gapabs (mipgapabs, lim:absgap, absgap)
      Solving stops, if the absolute gap = |primalbound - dualbound| is below
      the given value (default: 0.0)

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

misc:allowstrongdualreds (allowstrongdualreds)
      0/1: whether strong dual reductions should be allowed in propagation and
      presolving

      0 - Strong dual reductions should not be allowed in propagation and
      presolving

      1 - Strong dual reductions should be allowed in propagation and
      presolving (default).

misc:allowweakdualreds (allowweakdualreds)
      0/1: whether weak dual reductions should be allowed in propagation and
      presolving

      0 - Weak dual reductions should not be allowed in propagation and
      presolving

      1 - Weak dual reductions should be allowed in propagation and presolving
      (default).

misc:scaleobj (scaleobj)
      0/1: whether the objective function should be scaled so that it is
      always integer

      0 - The objective function should not be scaled so that it is always
      integer

      1 - The objective function should be scaled so that it is always integer
      (default).

nod:childsel
      Child selection rule:

      d - down
      u - up
      p - pseudo costs
      i - inference
      l - lp value
      r - root LP value difference
      h - hybrid inference/root LP value difference (default)

num:checkfeastolfac (checkfeastolfac)
      Feasibility tolerance factor; for checking the feasibility of the best
      solution (default: 1.0)

num:epsilon (epsilon)
      Absolute values smaller than this are considered zero (default: 1e-09)

num:infinity (infinity)
      Values larger than this are considered infinity (default: 1e+20)

num:lpfeastolfactor (lpfeastolfactor)
      Factor w.r.t. primal feasibility tolerance that determines default (and
      maximal) primal feasibility tolerance of LP solver (default: 1.0)

num:sumepsilon (sumepsilon)
      Absolute values of sums smaller than this are considered zero (default:
      1e-06)

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

par:maxnthreads (maxnthreads)
      Maximum number of threads used during parallel solve (default: 8)

par:minnthreads (minnthreads)
      Minimum number of threads used during parallel solve (default: 1)

par:mode (parallelmode)
      0/1: Parallel optimisation mode (SCIP's concurrent solve, not used by
      GCG)

      0 - Opportunistic

      1 - Deterministic (default)

pre:abortfac (abortfac)
      Abort presolve, if at most this fraction of the problem was changed in
      last presolve round (default: 0.0008)

pre:clqtablefac (clqtablefac)
      Limit on number of entries in clique table relative to number of problem
      nonzeros (default: 2.0)

pre:donotaggr (donotaggr)
      0/1: whether aggregation of variables should be forbidden

      0 - Aggregation of variables should not be forbidden (default)

      1 - Aggregation of variables should be forbidden.

pre:donotmultaggr (donotmultaggr)
      0/1: whether multi-aggregation of variables should be forbidden

      0 - Multi-aggregation of variables should not be forbidden (default)

      1 - Multi-aggregation of variables should be forbidden.

pre:immrestartfac (immrestartfac)
      Fraction of integer variables that were fixed in the root node
      triggering an immediate restart with preprocessing (default: 0.05)

pre:maxrestarts
      Maximal number of restarts (default: -1: unlimited)

pre:maxrounds
      Maximal number of presolving rounds (default: -1: unlimited; 0: off)

pre:restartfac (restartfac)
      Fraction of integer variables that were fixed in the root node
      triggering a restart with preprocessing after root node evaluation
      (default: 0.025)

pre:restartminred (restartminred)
      Minimal fraction of integer variables removed after restart to allow for
      an additional restart (default: 0.05)

pre:settings
      0/1/2/3: sets presolvings settings

      0 - Sets presolvings default (default)

      1 - Sets presolvings aggressive

      2 - Sets presolvings fast

      3 - Sets presolvings off.

pre:solve (presolve)
      0/1: whether to use SCIP presolving on the original problem (default 1);
      0 is the same as pre:settings=3.

pre:subrestartfac (subrestartfac)
      Fraction of integer variables that were globally fixed during the
      solving process triggering a restart with preprocessing (default: 1.0)

pricing:artificialvars (useartificialvars)
      0/1: whether artificial variables are used to make the restricted master
      feasible instead of Farkas pricing (default 0).

pricing:dispinfos (pricingdispinfos)
      0/1: whether additional information on the pricing process is displayed
      (default 0).

pricing:eagerfreq (eagerfreq)
      Frequency at which all pricing problems are solved (default 10; 0:
      disabled)

pricing:heuriters (heurpricingiters)
      Maximum number of heuristic pricing iterations per pricing call and
      problem (default 1)

pricing:maxcolsprob (maxcolsprobredcost)
      Maximal number of columns per pricing problem per reduced cost pricing
      round (default 10)

pricing:maxcolsround (maxcolsroundredcost)
      Maximal number of columns per reduced cost pricing round (default 100)

pricing:maxcolsroundroot (maxcolsroundredcostroot)
      Maximal number of columns per reduced cost pricing round at the root
      node (default 100)

pricing:maxheurdepth (maxheurdepth)
      Maximum depth at which heuristic pricing is performed (default -1: no
      limit)

pricing:maxrounds (maxroundsredcost)
      Maximal number of pricing rounds per node after the root node (default:
      no limit)

pricing:sorting (sorting)
      Order in which the pricing problems are solved:

      i - indices
      d - dual solutions of the convexity constraints
      r - reliability (default)
      l - last pricing results

pricing:stabilization (stabilization)
      0/1: whether dual value stabilization should be performed in pricing
      (default 1).

pricing:stabilizationtree (stabilizationtree)
      0/1: whether stabilization should also be performed in the tree, in
      nodes other than the root (default 0).

pro:abortoncutoff
      0/1: whether propagation should be aborted immediately (setting this to
      0 could help conflict analysis to produce more conflict constraints)

      0 - Propagation should not be aborted immediately

      1 - Propagation should be aborted immediately (default).

pro:maxrounds
      Maximal number of propagation rounds per node (-1: unlimited; 0: off;
      default: 100)

pro:maxroundsroot
      Maximal number of propagation rounds in the root node (-1: unlimited; 0:
      off; default: 1000)

ran:permuteconss (permuteconss)
      0/1: whether the order of constraints should be permuted (depends on
      permutationseed)?

      0 - Order of constraints should not be permuted

      1 - Order of constraints should be permuted (default).

ran:permutevars (permutevars)
      0/1: whether the order of variables should be permuted (depends on
      permutationseed)?

      0 - Order of variables should not be permuted (default)

      1 - Order of variables should be permuted.

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

sol:poolgap (poolgap, ams_eps)
      Relative tolerance for reporting alternative solutions (default: no
      limit).

sol:poolgapabs (poolgapabs, ams_epsabs)
      Absolute tolerance for reporting alternative solutions (default: no
      limit).

sol:poollimit (poollimit, ams_limit, solnlimit)
      Limit on the number of alternative solutions reported (options sol:stub,
      sol:count); default 10, -1: all solutions stored by GCG (at most
      lim:maxsol).

sol:report_uncertain (report_uncertain_sol)
      0/1*: whether to report objective value(s) in solve_message when
      solve_result is '?' (unknown).

sol:stub (ams_stub, solstub, solutionstub)
      Stub for solution files. If "solutionstub" is specified, found solutions
      are written to files ("solutionstub & '1' & '.sol'") ... ("solutionstub
      & Current.nsol & '.sol'"), where "Current.nsol" holds the number of
      returned solutions. That is, file names are obtained by appending 1, 2,
      ... "Current.nsol" to "solutionstub".

tech:clocktype (clocktype)
      Clock type for time limits and reporting: 1 CPU user seconds, 2 wall
      clock time (default).

tech:debug (debug)
      0*/1: whether to assist testing & debugging, e.g., by outputting
      auxiliary information (mostly via suffixes).

tech:logfile (logfile)
      Log file name. Without tech:outlev=1 the log goes to the file only.

tech:lpseed (lpseed, ran:lpseed)
      Random seed for LP solver, e.g. for perturbations in the simplex
      (default: 0: LP default)

tech:optionfile (optionfile, option:file)
      Name of an AMPL solver option file to read (surrounded by 'single' or
      "double" quotes if the name contains blanks). Lines that start with #
      are ignored. Otherwise, each nonempty line should contain "name=value",
      e.g., "lim:iter=500".

tech:optionnative (optionnative, optnative, tech:param, param)
      General way to set any GCG/SCIP parameter of the original problem; the
      value should be a quoted string (delimited by ' or ") containing one or
      more 'name=value' or 'name value' pairs separated by spaces, for example
      'pricing/masterpricer/eagerfreq=5 detection/maxrounds 2'. Can appear
      more than once. Cannot be used to query current parameter values.

tech:optionnativeread (optionnativeread, tech:param:read, param:read)
      Filename of GCG parameter file (as path).The suffix on a parameter file
      should be .set.

tech:optionnativewrite (optionnativewrite, tech:param:write, param:write)
      Name of a GCG parameter file (.set) to write before solving, with all
      parameters of the original problem.

tech:outlev (outlev)
      0*/1: Whether to write GCG log lines (chatter) to stdout and to file.

tech:outlev_mp (outlev_mp)
      0*/1: whether to print MP model information.

tech:outlevnative (outlevnative, tech:outlev-native, outlev-native)
      0*/1/2/3/4/5: Native SCIP verbosity level (display/verblevel; the SCIP
      default is 4, the driver's is 0). tech:outlev=1 selects 4.

tech:permseed (permseed, ran:permutationseed, permutationseed)
      Seed value for permuting the problem after reading/transformation
      (default: 0: no permutation)

tech:seed (seed, ran:randomseedshift, randomseedshift)
      Global shift of all random seeds in the plugins and the LP random seed
      (default: 0)

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

tech:threads (threads, pricing:threads)
      Maximum number of threads used to parallelize pricing (default 1; 0:
      automatic, at most 8). The branch-and-price itself is sequential.

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

