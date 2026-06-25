
# MP2NL Options

```ampl
ampl: option solver mp2nl; # change the solver
ampl: option mp2nl_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

Solver options obtained with `$ mp2nl -=`.

```
MP2NL Optimizer Options for AMPL
--------------------------------------------

To configure MP2NL, assign a string specifying option values to the AMPL
option "mp2nl_options", as well as the subsolver option values to its own AMPL
option. For example:

   ampl: option mp2nl_options 'solver=baron';
   ampl: option baron_options 'outlev=1 iisfind=1';

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
      Solver acceptance level for 'AbsConstraint' as expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:acos
      Solver acceptance level for 'AcosConstraint' as expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:acosh
      Solver acceptance level for 'AcoshConstraint' as expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:alldiff
      Solver acceptance level for 'AllDiffConstraint' as expression, default
      4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:and (acc:forall)
      Solver acceptance level for 'AndConstraint' as expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:asin
      Solver acceptance level for 'AsinConstraint' as expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:asinh
      Solver acceptance level for 'AsinhConstraint' as expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:atan
      Solver acceptance level for 'AtanConstraint' as expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:atanh
      Solver acceptance level for 'AtanhConstraint' as expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:call
      Solver acceptance level for 'CallConstraint' as expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:condlineq
      Solver acceptance level for 'CondLinConEQ' as expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:condlinge
      Solver acceptance level for 'CondLinConGE' as expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:condlingt
      Solver acceptance level for 'CondLinConGT' as expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:condlinle
      Solver acceptance level for 'CondLinConLE' as expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:condlinlt
      Solver acceptance level for 'CondLinConLT' as expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:cos
      Solver acceptance level for 'CosConstraint' as expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:cosh
      Solver acceptance level for 'CoshConstraint' as expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:count
      Solver acceptance level for 'CountConstraint' as expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:div
      Solver acceptance level for 'DivConstraint' as expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:equiv (acc:equivalence)
      Solver acceptance level for 'EquivalenceConstraint' as expression,
      default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:exp
      Solver acceptance level for 'ExpConstraint' as expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:expa (acc:expA)
      Solver acceptance level for 'ExpAConstraint' as expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:ifthen
      Solver acceptance level for 'IfThenConstraint' as expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:impl
      Solver acceptance level for 'ImplicationConstraint' as expression,
      default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:lineq
      Solver acceptance level for 'LinConEQ' as flat constraint, default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:linfn (acc:linfunccon)
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
      Solver acceptance level for 'LogConstraint' as expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:loga (acc:logA)
      Solver acceptance level for 'LogAConstraint' as expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:max
      Solver acceptance level for 'MaxConstraint' as expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:min
      Solver acceptance level for 'MinConstraint' as expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

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

acc:nlcompl
      Solver acceptance level for 'NLComplementarity' as flat constraint,
      default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:nlcon (acc:nlalgcon)
      Solver acceptance level for 'NLConstraint' as flat constraint, default
      2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:nllogcon (acc:nllogical)
      Solver acceptance level for 'NLLogical' as flat constraint, default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:nlreifequiv
      Solver acceptance level for 'NLReifEquiv' as flat constraint, default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:nlreifimpl
      Solver acceptance level for 'NLReifImpl' as flat constraint, default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:nlreifrimpl
      Solver acceptance level for 'NLReifRimpl' as flat constraint, default 2:

      0 - Not accepted natively, automatic redefinition will be attempted
      1 - Accepted but automatic redefinition will be used where possible
      2 - Accepted natively and preferred

acc:not
      Solver acceptance level for 'NotConstraint' as expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:numberofconst
      Solver acceptance level for 'NumberofConstConstraint' as expression,
      default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:numberofvar
      Solver acceptance level for 'NumberofVarConstraint' as expression,
      default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:or (acc:exists)
      Solver acceptance level for 'OrConstraint' as expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:pow
      Solver acceptance level for 'PowConstraint' as expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:powc (acc:powconstexp)
      Solver acceptance level for 'PowConstExpConstraint' as expression,
      default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:quadfn (acc:quadfunccon)
      Solver acceptance level for 'QuadraticFunctionalConstraint' as
      expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:sin
      Solver acceptance level for 'SinConstraint' as expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:sinh
      Solver acceptance level for 'SinhConstraint' as expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

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
      Solver acceptance level for 'TanConstraint' as expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

acc:tanh
      Solver acceptance level for 'TanhConstraint' as expression, default 4:

      0 - Not accepted natively, automatic redefinition will be attempted
      3 - Accepted but automatic redefinition will be used where possible
      4 - Accepted natively and preferred

alg:relax (relax)
      0*/1: Whether to relax integrality of variables.

alg:start (warmstart)
      Whether to use incoming primal (and dual, for LP) variable values in a
      warmstart:

      0 - No
      1 - Yes (for LP: if there is no incoming alg:basis)
      2 - Yes (for LP: omitting the incoming alg:basis, if any)
      3 - Yes (for LP: together with the incoming alg:basis, if any;
          default).

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
      Default 2147483647.

      See also *nl:assign:defvar*.

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

cvt:pow2_as_qp (pow2_as_qp, pow2asqp)
      0/1*: whenever both quadratics and ^2 are accepted, submit (expr)^2 as
      out-multiplied quadratics, if (expr) is linear.

      See also cvt:multoutcard, cvt:quadobj, cvt:quadcon.

cvt:pre:all
      0/1*: Set to 0 to disable most presolve in the flat converter.

cvt:pre:boundlogarg (boundlogarg)
      0*/1: Bound logarithm arguments to nonnegative.

cvt:pre:boundsbest (boundsbest)
      0*/1: Submit best-known variable bounds to the solver. Can inhibit its
      presolve.

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

      Default: 5.

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
      2 - Linear subexpressions
      4 - Quadratic subexpressions
      8 - MIN/MAX.

      See also option cvt:dvelim concerning only the input model. Default 15.

cvt:qp2passes (cvt:qp2pass, qp2passes, qp2pass)
      0/1*: Parse sums of QP expressions in 2 passes. Usually faster.

cvt:quadcon (passquadcon)
      0/1*: set to 0 to disable quadratic constraints. Synonym for
      acc:quad..=0. Setting to 0 disables out-multiplication of quadratic
      terms, then they are linearized.

cvt:quadobj (passquadobj)
      0*/1: Pass quadratic objective terms to the solver. When 0, if the
      solver accepts quadratic constraints, such a constraint will be created
      with those, otherwise linearly approximated.

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

lim:time (timelim, timelimit, time_limit)
      Enforce limit on solve time (in seconds; default: 1e+20). DOES NOTHING
      CURRENTLY.

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

nl:assign:defvar (nldefvar)
      Above which reference count, an algebraic expression is converted into a
      defined variable. Default 1.

      This option is applied after *cvt:expr:nlassign*.

nl:comments (nlcomments)
      0*/1: add comments to the text-format NL file.

nl:config (config)
      Choose subsolver configuration (see nl:printconfigs).

nl:printconfigs (printconfigs)
      Print the configurations for various values of the solver/config
      options.

nl:solver (solver, nlsolver)
      Subsolver (underlying AMPL solver.)

      Automatically sets solver configuration, if known.

nl:solver_options (solver_options, slv_opts)
      Subsolver options.

      This way is for convenience; the preferred and dominating way is to use
      the <subsolver>_options environment variable (which can be set in AMPL
      in the usual way as 'option <subsolver>_options "...";')

nl:stub (stub, nlstub)
      Filename stub for the NL and SOL files.

nl:text (nltextformat, nltext)
      0*/1: write NL file in text format.

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

obj:multi:options (multiobjoptions)
      0/1*: Regard multiobjective option suffixes which are objective suffixes
      beginning with option_. Example: suffix option_timelim; let
      _obj[2].option_timelim:=15;

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

tech:optionfile (optionfile, option:file)
      Name of an AMPL solver option file to read (surrounded by 'single' or
      "double" quotes if the name contains blanks). Lines that start with #
      are ignored. Otherwise, each nonempty line should contain "name=value",
      e.g., "lim:iter=500".

tech:outlev (outlev)
      0*/1: Verbosity for the MP2NL driver. For the underlying solver, use the
      <subsolver>_options environment variable.

tech:outlev_mp (outlev_mp)
      0*/1: whether to print MP model information.

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
      3 - Report statistics both in suffixes and the suffix 'stats'

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
```

