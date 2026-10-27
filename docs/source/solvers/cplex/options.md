
# CPLEX Options

```ampl
ampl: option solver cplex; # change the solver
ampl: option cplex_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

Solver options obtained with `$ cplex -=`.

```
IBM ILOG CPLEX Optimizer Options for AMPL
-----------------------------------------

To set these options, assign a string specifying their values to the AMPL
option "cplex_options". For example:

   ampl: option cplex_options 'mipgap=1e-6';

'' Options:

acc:_all
      Solver acceptance level for all constraints and expressions. Value
      meaning: as described in the specific acc:... options.

      Can be useful to disable all reformulations (acc:_all=2), or force
      linearization (acc:_all=0.)

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

acc:pl (acc:pwl, acc:piecewise)
      Solver acceptance level for 'PLConstraint' as flat constraint, default
      2:

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

alg:barrier (barrier, baropt)
      Solve (MIP node) LP/QPs by barrier method.

alg:basis (basis)
      Whether to use and/or return a basis for LP models (variable/constraint
      suffixes .(s)status):

      0 - No
      1 - Use incoming basis (if provided)
      2 - Return final basis
      3 - Both (1 + 2 = default)

      See alg:start for interaction with the LP warmstart.

      See also mip:basis and qcp:dual (for some solvers).

alg:benders (benders, bendersopt)
      Solve MIP using Benders algorithm. Both integer and continuous variables
      must be present.

alg:benders_feascuttol (benders_feascut_tol)
      Tolerance for violations of feasibility cuts in Benders algorithm
      (default 1e-6; must be in [1e-9, 0.1]).

alg:benders_optcut_tol (benders_optcut_tol)
      Tolerance for violations of optimality cuts in Benders algorithm
      (default 1e-6; must be in [1e-9, 0.1]).

alg:benders_strategy (benders_strategy)
      How to decompose the problem for Benders algorithm:

      0 - Automatic (default): if suffix benders is present on variables,
          variables that have .benders = 0 go into the master and CPLEX
          assigns other variables to workers; otherwise integer variables go
          into the master and variables into workers
      1 - Use suffix benders to determine which variables are for the master
          (.benders = 0) and which for workers (.benders = n > 0 ==> worker n
      2 - Similar to 0, but suffix benders is required
      3 - Similar to 0, but ignore suffix benders

alg:benders_worker (benders_worker)
      Designate the algorithm that CPLEX applies to solve the subproblems when
      using Benders decomposition:

      0 - Automatic (default)
      1 - Primal simplex
      2 - Dual simplex
      3 - Network simplex
      4 - Barrier
      5 - Sifting

alg:concurrent (concurrentopt, concurrent)
      Solve LPs and MIP root relaxations with the concurrent optimizer
      (several algorithms in parallel). Synonym for alg:method=6.

alg:conflictalg (conflictalg)
      Choice of algorithm used by the CPLEX's conflict refiner:

      0 - Automatic choice (default)
      1 - Fast
      2 - Propagate
      3 - Presolve
      4 - IIS
      5 - Limited solve
      6 - Full solve

      Settings 1, 2, and 3 are fast but may not discard many constraints; 5
      and 6 work harder at this. Setting 4 searches for an Irreducible
      Infeasible Set of linear constraints(e.g., ignoring quadratic
      constraints).

alg:droptol (droptol)
      If droptol > 0 is specified, linear constraint and objective
      coefficients less than droptol in magnitude are treated as zero.

alg:dualopt (alg:dual, dualopt, tranopt)
      Solve (MIP node) LPs by dual simplex method.

alg:dualproblem (dual)
      Compatibility option with the legacy cplexasl driver. Interacts with
      pre:dual as follows:

      alg:dualproblem - alone, equivalent to pre:dual=0
      alg:dualproblem pre:dual=-1 - together, equivalent to pre:dual=1
      alg:dualproblem pre:dual=0 - together, equivalent to pre:dual=0
      alg:dualproblem pre:dual=1 - together, equivalent to pre:dual=-1.

alg:feasopt (feasopt)
      Compatibility option of the cplexasl driver, together with
      alg:feasoptobj mapped onto alg:feasrelax: for infeasible problems,
      whether to find a feasible point for a relaxed problem:

      0 - No (default)
      1 - Find a relaxed feasible point
      2 - Find a "best" solution among the relaxed feasible points

alg:feasoptobj (feasoptobj)
      Objective for alg:feasopt:

      1 - Minimize the sum of constraint and variable bound relaxations
          (default)
      2 - Minimize the number of constraints and variable bounds relaxed (a
          MIP problem, generally harder than 1)
      3 - Minimize the sum of squares of constraint and variable bound
          relaxations

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

alg:feasrelax:tol (feasopttol)
      Tolerance for constraint violations in the relaxed problem of
      alg:feasrelax; default 1e-6.

alg:feastol (feastol, feasibility)
      Primal feasibility tolerance (default 1e-6, possible values are between
      1e-9 and 0.1).

alg:kappa (kappa, basis_cond)
      Whether to return the estimated condition number (kappa) of the optimal
      basis (default 0): sum of 1 = report kappa in the result message; 2 =
      return kappa in the solver-defined suffix .kappa on the objective and
      problem. The request is ignored when there is no optimal basis.

alg:lbpen (lbpen)
      See alg:feasrelax.

alg:method (method, lpmethod, qpmethod, simplex, mip:method, mipstartalg, startalg, startalgorithm)
      Which algorithm to use for non-MIP problems or for the root node of MIP
      problems:

      0 - Automatic (default)
      1 - Primal simplex
      2 - Dual simplex
      3 - Network simplex
      4 - Barrier
      5 - Sifting
      6 - Concurrent (dual, barrier and primal in opportunistic mode; dual
          and barrier in deterministic mode; 4 is used for MIPQs).

      For MIQP problems (quadratic objective, linear constraints), setting 5
      is treated as 0 and 6 as 4. For MIQCP problems (quadratic objective &
      constraints), all settings are treated as 4. See also mip:nodemethod.
      Overrides netopt option and
      primalopt/dualopt/barrier/network/sifting/concurrent flags.

alg:netfeasibility (netfeasibility, netfeastol)
      Feasibility tolerance for network primal optimization. Can be any number
      from 1e-11 to 1e-1; default: 1e-6.

alg:netfind (netfind, netfinder)
      Level of network extraction for network simplex optimization:

      1 - Extract pure network only
      2 - Try reflection scaling (default)
      3 - Try general scaling

alg:netopt (netopt)
      Whether to use network simplex method for non-MIP problems or for the
      continuous relaxations of MIP nodes, unless alg:(node)method or
      primalopt/dualopt/barrier/network/sifting flags are specified. Options
      alg:(node)method override (for MIP, in the root or subnodes):

      0 - (Default) never invoke the network optimizer
      1 - Compatibility value; same as 3
      2 - Compatibility value; same as 3
      3 - Invoke the network optimizer by setting CPLEX' LP/QP/MIPNodeMethod
          to CPX_ALG_NET telling CPLEX to search for network (sub)structures
          in the model. CPLEX presolve might influence automatic recognition
          of network structures

alg:netoptimality (netoptimality)
      Specifies the optimality tolerance for network optimization; that is,
      the amount a reduced cost may violate the criterion for an optimal
      solution. Can be any number from 1e-11 to 1e-1; default: 1e-6.

alg:netpricing (netpricing)
      Pricing algorithm for network simplex optimization:

      0 - (Default) automatic
      1 - Partial pricing
      2 - Multiple partial pricing
      3 - Multiple partial pricing with sorting

alg:network (network)
      Solve (substructure of) (MIP node's) LP/QP by network simplex method.
      Synonym for alg:netopt=3.

alg:numericalemphasis (numfocus, numericemphasis, numericalemphasis, alg:numericfocus, numericfocus)
      0*/1: Whether to try to improve numerical accuracy (at a possible cost
      of time or memory).

alg:primalopt (alg:primal, primalopt, optimize)
      Solve (MIP node) LPs by primal simplex method.

alg:primalproblem (primal)
      Compatibility option with the legacy cplexasl driver. No effect.

alg:rays (rays)
      Whether to return suffix .unbdd (unbounded ray) if the objective is
      unbounded or suffix .dunbdd (Farkas dual) if the constraints are
      infeasible:

      0 - Neither
      1 - Just .unbdd
      2 - Just .dunbdd
      3 - Both (default)

alg:readbasis (readbasis, startbasis)
      BAS file containing the starting basis. It is read after any incoming
      .sstatus basis (see alg:basis) and overrides it.

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

alg:siftalg (siftalg)
      Algorithm for sifting subproblems:

      0 - Automatic (default)
      1 - Primal simplex
      2 - Dual simplex
      3 - Network simplex
      4 - Barrier

alg:sifting (sifting, siftopt, siftingopt)
      Solve (MIP node) LPs by sifting method.

alg:siftsimplex (simplexsifting)
      0/1*: Whether the simplex algorithm may use sifting when appropriate.

alg:start (warmstart)
      Whether to use incoming primal (and dual, for LP) variable values in a
      warmstart:

      0 - No
      1 - Yes (for LP: if there is no incoming alg:basis)
      2 - Yes (for LP: omitting the incoming alg:basis, if any)
      3 - Yes (for LP: together with the incoming alg:basis, if any;
          default).

      For IBM ILOG CPLEX, choices can be refined via alg:start:advance and,
      for MIP starts, mip:start:effort.

alg:start:advance (alg:start:advanced, advance, advind)
      If set to 1 or 2, this parameter specifies that CPLEX should use
      advanced starting information when it initiates optimization. Exact
      meaning differs by problem type. Here for LP:

      0 - Do not use advanced start information
      1 - Use an advanced basis supplied by the user (default)
      2 - Crush an advanced basis or starting vector supplied by the user.

alg:ubpen (ubpen)
      See alg:feasrelax.

bar:baralg (baralg)
      How to start the barrier algorithm:

      0 - Default (= 1 for MIP subproblems, else 3)
      1 - Infeasibility-estimate start
      2 - Infeasibility-constant start
      3 - Standard start

bar:comptol (comptol)
      Convergence tolerance for barrier algorithm: the algorithm stops when
      the relative complementarity is < bartol (default 1e-8).

bar:corrections (barcorr, barmaxcor)
      Limit on centering corrections in each iteration of the barrier
      algorithm:

      -1  - Automatic (default)
      0   - None
      n>0 - Maximum number of centering corrections per iteration

bar:crossover (crossover, mipcrossover)
      How to transform a barrier solution to a basic one:

      -1 - Automatic choice (default)
      0  - None: return an interior solution
      1  - Primal crossover
      2  - Dual crossover

bar:dense (bar:densecol, dense, densecol)
      If positive, minimum nonzeros in a column for the barrier algorithm to
      consider the column dense. If 0 (default), this tolerance is selected
      automatically.

bar:growth (bargrowth, growth)
      Tolerance for detecting unbounded faces in the barrier algorithm: higher
      values make the test for unbounded faces harder to satisfy (default
      1e12; must be >= 1).

bar:iterlim (bariterlim)
      Maximum barrier iterations allowed (default: no limit).

bar:objrange (barobjrange)
      Limit on the absolute objective value before the barrier algorithm
      considers the problem unbounded (default 1e20).

bar:ordering (ordering)
      Ordering algorithm used by the barrier algorithm:

      0 - Automatic (default)
      1 - Approximate minimum degree (AMD)
      2 - Approximate minimum fill (AMF)
      3 - Nested dissection (ND)

bar:qcpcomptol (qcpconvergetol, qcpcomptol)
      Convergence tolerance on relative complementarity for problems with
      quadratic constraints; default 1e-7.

bar:start (barstart, barstartalg)
      Barrier starting-point algorithm:

      1 - Assume dual is 0 (default)
      2 - Estimate dual
      3 - Average of primal estimate, 0 dual
      4 - Average of primal and dual estimates

cut:aggforcut (aggforcut, aggcutlim)
      Bound on the number of constraints aggregated to generate flow-cover and
      mixed-integer-rounding cuts (default 3).

cut:aggtol (aggtol)
      Pivot tolerance for aggregating (undocumented CPLEX parameter 1055). It
      seldom needs fiddling. Default = .05; must be in [1e-10, .99].

cut:bqp (bqpcuts)
      Whether to enable Boolean Quadric Polytope cut generation for nonconvex
      QP and MIQP problems, choices as for "cut:cuts".

cut:clique (cliquecuts, cliques)
      Whether to use clique cuts in solving MIPs, choices as for "cut:cuts".

cut:cover (covercuts, covers)
      Whether to use cover cuts in solving MIPs, choices as for "cut:cuts".

cut:cuts (cuts, mipcuts)
      Global cut generation control, applied to all cut families (cut:bqp,
      cut:clique, cut:cover, cut:disj, cut:flowcover, cut:frac, cut:gubcover,
      cut:implied, cut:liftandproject, cut:localimplied, cut:mcf, cut:mir,
      cut:node, cut:flowpath, cut:rlt, cut:zerohalf) unless overridden by the
      individual cut-type controls; value 3 is reduced to 2 for families
      accepting at most 2:

      -1 - Disallow
      0  - Automatic (default)
      1  - Enable moderate cuts generation
      2  - Enable aggressive cuts generation.
      3  - Enable very aggressive cuts generation.

cut:disj (disjcuts)
      Whether to use disjunctive cuts in solving MIPs, choices as for
      "cut:cuts".

cut:eachcutlim (eachcutlim)
      Limit on the number of cuts of each type; default=2100000000.

cut:factor (cutsfactor, cutfactor)
      Limit on MIP cuts added (a real number):

      <0          - No limit
      -1          - No limit (default)
      0 <= n <= 1 - No MIP cuts
      n > 1       - (n-1)*m, where m is the original number of rows(after
                    presolve)

cut:flowcover (flowcovercuts, flowcuts)
      Whether to use flowcover cuts in solving MIPs:

      -1 - Disallow
      0  - Automatic (default)
      1  - Enable moderate cuts generation
      2  - Enable aggressive cuts generation

cut:flowpath (flowpathcuts)
      Whether to use flow path cuts in solving MIPs, choices as for
      "cut:flowcover".

cut:frac (gomory, fraccuts)
      Whether to use fractional Gomory cuts in solving MIPs, choices as for
      "cut:flowcover".

cut:fraccand (fraccand, gomorycand)
      Limit on number of candidate variables when generating Gomory cuts for
      MIP problems; default=200.

cut:fracpass (fracpass, gomorypass, fractionalcuts)
      Limit on number of passes to generate MIP fractional Gomory cuts,
      default=0 => automatic choice, positive = at most that many passes.

cut:gubcover (gubcover, gubcuts)
      Whether to use fractional GUB cuts in solving MIPs, choices as for
      "cut:flowcover".

cut:implied (implied, impliedcuts)
      Whether to use implied cuts in solving MIPs, choices as for
      "cut:flowcover".

cut:liftandproject (liftandproject, liftandprojectcuts, splitcuts)
      Whether to use lift and project cuts in solving MIPs, choices as for
      "cut:cuts".

cut:localimplied (localimplied, localimpliedcuts)
      Whether to use locally valid implied cuts in solving MIPs, choices as
      for "cut:cuts".

cut:mcf (mcfcuts, cut:mfc, mfccuts)
      Whether to use multi-commodity flow (MCF) cuts in solving MIPs, choices
      as for "cut:flowcover". (cut:mfc/mfccuts are legacy spellings.)

cut:mir (mircuts)
      Whether to use mixed-integer rounding (MIR) cuts in solving MIPs,
      choices as for "cut:flowcover".

cut:node (nodecuts)
      Decides whether or not cutting planes are separated at the nodes of the
      branch-and-bound tree, choices as for "cut:cuts".

cut:passes (cutpasses, cutpass)
      Maximum number of cutting-plane passes during root-cut generation:

      -1    - None
      0     - Automatic
      n > 0 - Number of passes to perform

cut:rlt (rltcuts)
      Whether to use the Relaxation Linearization Technique (RLT) to generate
      cuts in solving MIPs, choices as for "cut:cuts".

cut:stats (cutstats)
      Whether the solve_message report the numbers and kinds of cuts used.

      0 - No (default)
      1 - Yes.

cut:zerohalf (zerohalfcuts)
      Whether to use zero-half cuts in solving MIPs, choices as for
      "cut:flowcover".

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

lim:dettime (dettimelim)
      Time limit in platform-dependent "ticks".

lim:iter (iterlim, iterlimit, iterations, lpiterlim)
      LP iteration limit (default: large).

lim:lowercutoff (lowercutoff, mip:lowercutoff)
      See lim:uppercutoff.

lim:lowerobj (lowerobjlim, lowerobj)
      See lim:upperobjlim.

lim:lowerobjstop (lowerobjstop, mip:lowerobj)
      See lim:upperobjstop.

lim:netiterations (netiterations, netiter)
      Limit on network simplex iterations (default: large).

lim:nodes (nodes, node, nodelim, nodelimit)
      Maximum MIP nodes to explore (default: no limit).

lim:probetime (probetime)
      Limit in seconds on time spent probing; default 1e75.

lim:probetimedet (probetimedet)
      Limit in "ticks" on time spent probing; default 1e75.

lim:siftiter (siftiterations, siftiter)
      Limit on sifting iterations (default: no limit).

lim:sol (sollimit, solutionlimit, mipsolutions, solutionlim)
      Limit the number of feasible MIP solutions found, causing early
      termination if exceeded; must be >= 1; default = no limit.

lim:time (timelim, timelimit, time, lptimelim)
      Limit on solve time (in seconds; default: no limit).

lim:treememory (treememory, treelimit, treememlim)
      Maximum megabytes of memory for the branch-and-bound tree (default 1e75
      ==> no limit).

lim:uppercutoff (uppercutoff, mip:uppercutoff)
      Sets the upper cutoff tolerance. When the problem is a minimization
      problem, CPLEX cuts off or discards any solutions that are greater than
      the specified upper cutoff value. If the model has no solution with an
      objective value less than or equal to the cutoff value, CPLEX declares
      the model infeasible. In other words, setting an upper cutoff value c
      for a minimization problem is similar to adding this constraint to the
      objective function of the model: obj <= c. Default: 1e+75.

      Only effective in the branch and bound algorithm, for example, in a
      mixed integer program (MIP).

lim:upperobj (upperobjlim, upperobj)
      Sets an upper limit on the value of the objective function in the
      simplex algorithms. Setting an upper objective function limit causes
      CPLEX to halt the optimization process when the maximum objective
      function value limit has been reached. This limit applies only during
      Phase II of the simplex algorithm in maximization problems. Default:
      1e+75.

lim:upperobjstop (upperobjstop, mip:upperobj)
      In a maximization MILP or MIQP, the solver will abort the optimization
      process as soon it finds a solution of value greater than or equal to
      the specified value. It is ignored if the problem is multiobjective.
      Default: 1e+75.

lp:crash (crash)
      Crash strategy (used to obtain starting basis in simplex); possible
      values = -1, 0, 1; default = 1. The best setting is problem-dependent
      and can only be found by experimentation. 0 completely ignores the
      objective.

lp:dgradient (dgradient)
      Pricing algorithm for dual simplex (default 0):

      0 - Automatic (default)
      1 - Standard dual pricing
      2 - Steepest-edge pricing
      3 - Steepest-edge pricing in slack space
      4 - Steepest-edge with unit initial norms
      5 - Devex pricing

lp:doperturb (doperturb, perturb)
      Whether to perturb the problem initially when using simplex (by the
      amount given by lp:perturb); setting it to 1 is occasionally helpful for
      highly degenerate problems:

      0 - No (default)
      1 - Yes.

lp:dynamicrows (dynamicrows)
      Whether CPLEX manages the rows of the basis matrix dynamically during
      dual simplex:

      -1 - Automatic choice (default)
      0  - No
      1  - Yes.

lp:markowitz (markowitz)
      Markowitz pivot tolerance; default = 0.01; must be between 1e-4 and
      0.99999. Bigger values may improve numerical properties of the solution
      (and may take more time).

lp:opttol (optimality, opttol, optimalitytolerance)
      Dual optimality tolerance: simplex will stop when all reduced costs are
      smaller than this value in the improving direction; default=1e-6.

lp:perturb (perturbation, perturbconst)
      Amount by which to perturb variable bounds when perturbing problems (see
      "lp:doperturb"); default=1e-6, must be in [1e-8, 1e75].

lp:perturblim (perturblim, perturblimit, limitperturb)
      Number of stalled simplex iterations before the problem is perturbed;
      default=0 => automatic.

lp:pgradient (pgradient)
      Pricing algorithm for primal simplex (default 0):

      -1 - Reduced-cost pricing
      0  - Hybrid reduced-cost and devex pricing (default)
      1  - Devex pricing
      2  - Steepest-edge pricing
      3  - Steepest-edge pricing with slack initial norms
      4  - Full pricing

lp:pricing (pricing)
      Size of the pricing candidate list for partial pricing; default 0 ==>
      automatic choice.

lp:refactor (refactor)
      LP iterations between refactorizing the basis; default 0 ==> automatic
      choice; maximum 10000.

lp:singular (singular, singularlim)
      Maximum number of times CPLEX tries to repair the basis when it
      encounters singularities; default 10.

lp:solutiontype (solutiontype)
      Whether to seek a basic solution when solving an LP:

      0 - Automatic - seeks a solution with basis (default)
      1 - Yes (equivalent to 0)
      2 - No

mip:backtrack (backtrack)
      Tolerance (>0, default 0.9999) for when to backtrack during branch &
      bound. Low values tend to pure best-bound search. High values(~1) tend
      to pure depth-first search. Values less than the default are often good
      when subproblems are expensive.

mip:basis (fixmodel, mip:fix)
      Whether to compute duals / basis / sensitivity for MIP models.

      0 - No (default)
      1 - Yes.

mip:basis:iterlimit
      Iteration limit for the fixed-model solve only. -1 (default) uses the
      solver default. For emulation, 0 skips the supplementary solve.

mip:basis:method (finalmipalg, mip:fixmethod)
      Algorithm for the fixed (continuous) model solved to obtain duals and a
      basis for MIP models (see mip:basis):

      0 - Automatic (default)
      1 - Primal simplex
      2 - Dual simplex
      3 - Network simplex
      4 - Barrier
      5 - Sifting
      6 - Concurrent (dual, barrier and primal in opportunistic mode; dual
          and barrier in deterministic mode; 4 is used for MIPQs).

mip:basis:timelimit
      Time limit in seconds for the fixed-model solve only. -1 (default) uses
      the solver default, independently of the MIP time limit. For emulation,
      0 skips the supplementary solve.

mip:bbinterval (bbinterval)
      For nodeselect = 2, select the best-bound node, rather than the best -
      estimate node, every bbinterval iterations (default 7); 0 means always
      use the best-estimate node.

mip:bestbound (bestbound, return_bound)
      Whether to return suffix .bestbound for the best known MIP dual bound on
      the objective value:

      0 - No (default)
      1 - Yes.

      The suffix is on the objective and problem and is -Infinity for
      minimization problems and +Infinity for maximization problems if there
      are no integer variables or if a dual bound is not available.

mip:bestnode (bestnode)
      Request return of suffix .bestnode on the objective and problem for the
      objective value at the best feasible MIP node. If a feasible node has
      not yet been found, this value is +Infinity for minimization problems
      and -Infinity for maximization problems.

mip:boundstr (boundstr, bndstrenind)
      Whether to apply bound strengthening in mixed integer programs (MIPs):

      -1 - Automatic choice (default)
      0  - No
      1  - Yes.

mip:branchdir (branchdir, branch)
      Which child node to explore first when branching:

      -1 - Explore "down" branch first
      0  - Explore "most promising" branch first (default)
      1  - Explore "up" branch first.

mip:cardls (cardls)
      Cardinality local search heuristic:

      -1   - Off
      0    - Automatic (default)
      1, 2 - Apply with increasing effort

mip:dive (dive)
      MIP dive strategy (how to choose between child nodes):

      0 - Automatic (default)
      1 - Traditional dive (never probing dives)
      2 - Probing dive (look ahead at both children)
      3 - Guided dive (explore solutions similar to the incumbent)

mip:emphasis (mipemphasis, mip:focus, mipfocus)
      MIP solution strategy:

      0 - Balance finding good feasible solutions and proving optimality
          (default)
      1 - Favor finding feasible solutions
      2 - Favor providing optimality
      3 - Focus on improving the best objective bound
      4 - Focus on finding hidden feasible solutions
      5 - Focus on finding high quality solutions earlier (heuristic).

mip:eplin (eplin)
      Epsilon used in CPLEX's linearization of logical constraints, e.g., x <
      a becomes x <= a - eplin; default 1e-3.

mip:fpheur (fpheur)
      Whether to use the feasibility pump heuristic on MIP problems:

      -1 - No
      0  - Automatic (default)
      1  - Yes, focus on finding a feasible solution
      2  - Yes, focus on finding a good objective value at a feasible
           solution

mip:gap (mipgap)
      Max. relative MIP optimality gap (default 1e-4; must be in [0, 1]).

mip:gapabs (mipgapabs, absmipgap)
      Max. absolute MIP optimality gap (default 1e-6; must be in [0, 1e20]).

mip:heureffort (heureffort)
      Effort spent on MIP heuristics: 0 disables them, values < 1 reduce and
      values > 1 increase the effort; default 1. Do not combine with a
      non-default mip:heurfreq.

mip:heurfreq (heurfreq, heuristicfreq)
      How often to apply the periodic (node) heuristic for MIPs:

      -1    - Never
      0     - Automatic (default)
      n > 0 - Every n nodes

mip:inttol (inttol, intfeastol, integrality)
      Feasibility tolerance for integer variables (default 1e-05, must be in
      [0.0, 0.5])

mip:kappastats (mipkappa)
      Whether to compute MIP kappa statistics, which summarize the condition
      numbers of the optimal bases seen while solving:

      -1 - No MIP kappa statistics
      0  - Automatic (default): compute for a sample of subproblems when
           alg:numericalemphasis is on
      1  - Compute for a sample of subproblems
      2  - Compute for all subproblems (possibly expensive)

mip:lbheur (lbheur)
      0*/1: Whether to use a local branching heuristic to try to improve new
      incumbents found during a MIP search.

mip:miqcpstrat (miqcpstrat)
      Strategy for solving quadratically-constrained MIPs (MIQCP):

      0 - Automatic (default)
      1 - Solve a QCP relaxation at each node
      2 - Solve an LP relaxation at each node

mip:nodefile (nodefile)
      Whether to save node information in a temporary file:

      0 - No
      1 - Compressed node file in memory (default)
      2 - Node file on disk
      3 - Compressed node file on disk

mip:nodemethod (nodemethod, mipalg, mipalgorithm, mipsubalg, subalg, subalgorithm)
      Algorithm used to solve relaxed MIP node problems (after the initial
      relaxation); for MIQP problems (quadratic objective, linear
      constraints), settings other than 3 and 5 are treated as 0. For MIQCP
      problems (quadratic objective and constraints), only 0 is permitted.

      0 - Automatic (default)
      1 - Primal simplex
      2 - Dual simplex
      3 - Network simplex
      4 - Barrier
      5 - Sifting

      See also alg:method. Overrides netopt option and
      primalopt/dualopt/barrier/network/sifting flags.

mip:nodesel (nodesel, nodeselect)
      Strategy for choosing next node while optimizing

      integer variables:

      0 - Depth-first search
      1 - Breadth-first search (default)
      2 - Best-estimate search
      3 - Alternative best-estimate search

mip:objdiff (objdiff, objdif, objdifference)
      Used to update the cutoff each time a solution is found. This absolute
      value is subtracted from (added to) the newly found integer objective
      value when minimizing (maximizing). This forces the mixed integer
      optimization to ignore integer solutions that are not at least this
      amount better than the best one found so far. Positive values may speed
      the search -- and may cause the optimal solution to be missed.

mip:ordertype (ordertype, mipordertype)
      How to generate default priorities for integer variables when no
      priority order is given:

      0 - Do not generate priorities (default)
      1 - Use decreasing costs
      2 - Use increasing bound range
      3 - Use coefficient count

mip:polishafter:absgap (polishafter_absmipgap)
      Start polishing integer solutions after the absolute MIP gap is at most
      this value; default 0.

mip:polishafter:dettime (polishafter_timedet)
      Start polishing integer solutions after finding at least one
      integer-feasible solution and spending this many "ticks"; default 1e75.

mip:polishafter:gap (polishafter_mipgap)
      Start polishing integer solutions after the relative MIP gap is at most
      this value; default 0.

mip:polishafter:nodes (polishafter_nodes)
      Start polishing integer solutions after processing this many nodes;
      default: no limit.

mip:polishafter:sols (polishafter_intsol)
      Start polishing integer solutions after finding this many
      integer-feasible solutions; default: no limit.

mip:polishafter:time (polishafter_time)
      Start polishing integer solutions after finding at least one
      integer-feasible solution and spending this many seconds; default 1e75.

mip:probe (probe)
      How much variable probing to do before MIP branching (sometimes
      dramatically affects performance, for better or worse):

      -1 - No probing
      0  - Automatic (default)
      1  - Moderate probing
      2  - Aggressive probing
      3  - Very aggressive probing

mip:relobjdiff (relobjdiff, relobjdif)
      If objdiff parameter is 0, relobjdiff times the absolute value is used
      as a cutoff (see objdiff)

mip:repairtries (repairtries)
      How many times to try to repair an infeasible MIP start:

      -1    - None
      0     - Automatic (default)
      n > 0 - That many times

mip:return_gap (return_mipgap)
      Whether to return mipgap suffixes or include mipgap values (|objectve -
      .bestbound|) in the solve_message: sum of

      1 - Return .relmipgap suffix (relative to |obj|)
      2 - Return .absmipgap suffix (absolute mipgap)
      4 - Suppress mipgap values in solve_message.

      Default = 0. The suffixes are on the objective and problem. Returned
      suffix values are +Infinity if no integer-feasible solution has been
      found, in which case no mipgap values are reported in the solve_message.

mip:rinsheur (rinsheur)
      Frequency of the relaxation induced neighborhood search (RINS)
      heuristic:

      -1    - Never
      0     - Automatic (default)
      n > 0 - Every n nodes

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

mip:search (mipsearch)
      Search strategy for mixed-integer problems:

      0 - Automatic (default)
      1 - Traditional branch and cut
      2 - Dynamic search

mip:start:effort (mipstartvalue, mipstart:effort)
      Effort level CPLEX applies to the MIP start passed from the incoming
      variable values (see alg:start):

      0 - Do not pass the MIP start to CPLEX
      1 - Automatic choice of effort level (default)
      2 - Withdrawn; treated as 1
      3 - CPX_MIPSTART_CHECKFEAS: fail if the start is infeasible
      4 - CPX_MIPSTART_SOLVEFIXED: solve the problem fixed at the start
      5 - CPX_MIPSTART_SOLVEMIP: solve a subMIP (see mip:submipnodelim)
      6 - CPX_MIPSTART_REPAIR: try to repair an infeasible start (see
          mip:repairtries)
      7 - CPX_MIPSTART_NOCHECK: assume the start is feasible

mip:strongcand (strongcand)
      Length of the candidate list for strong branching; default 10.

mip:strongit (strongit)
      Number of simplex iterations on each variable in the candidate list
      during strong branching; default 0 ==> automatic choice.

mip:submipalg (submipalg)
      Choice of algorithm used to solve the subproblems of a subMIP: not a
      subproblem, but an auxiliary MIP that CPLEX sometimes forms and solves,
      e.g., when dealing with a partial MIP start, repairing an infeasible MIP
      start, using the RINS heuristic, branching locally or polishing a
      solution. Possible values (only 0 is allowed for MIQCPs):

      0 - Automatic (default)
      1 - Primal simplex
      2 - Dual simplex
      3 - Network simplex
      4 - Barrier
      5 - Sifting

mip:submipnodelim (submipnodelim)
      Limit on nodes explored when CPLEX solves a subMIP (RINS, solution
      polishing, MIP start processing); default 500.

mip:submipscale (submipscale)
      Rarely used choice of scaling for auxiliary subMIPs (described with
      "submipalg"):

      -1 - No scaling
      0  - Equilibration (default)
      1  - More aggressive

mip:submipstartalg (submipstartalg)
      Rarely used choice of algorithm for the initial relaxation of a subMIP
      (described with "submipalg"); for MIQPs, 5 is treated as 0; only 0 is
      allowed for MIQCPs:

      0 - Automatic (default)
      1 - Primal simplex
      2 - Dual simplex
      3 - Network simplex
      4 - Barrier
      5 - Sifting

mip:symmetry (symmetry)
      Whether to break symmetry during preprocessing of MIP problems:

      -1 - Automatic (default)
      0  - Off
      1  - Moderate symmetry breaking
      2  - Aggressive
      3  - Very aggressive
      4  - Highly aggressive
      5  - Extremely aggressive

mip:varbranch (varbranch, varsel, varselect)
      MIP branch variable selection strategy:

      -1 - Branch on variable with smallest integer infeasibility
      0  - Algorithm decides (default)
      1  - Branch on variable with largest integer infeasibility
      2  - Branch based on pseudo costs
      3  - Strong branching
      4  - Branch based on pseudo reduced costs

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

pre:aggfill (aggfill, agglim)
      Variables that appear in more than agglim rows (default 10) will not be
      substituted away by the aggregator.

pre:aggregate (aggregate)
      Whether to make substitutions to reduce the number of rows:

      -1    - Automatic (default) (1 for LP, infinite for MIP)
      0     - Do not use any aggregator
      n > 0 - Apply aggregator n times

pre:coeffreduce (coeffreduce)
      Whether to use coefficient reduction when preprocessing MIPS

      -1 - Automatic (default)
      0  - No
      1  - Reduce only integral coefficients
      2  - Reduce all potential coefficients
      3  - Reduce aggresively with tiling

pre:dependency (dependency)
      Whether to use CPLEX's presolve dependency checker:

      -1 - Automatic (default)
      0  - No
      1  - Turn on only at start of preprocessing
      2  - Turn on only at end of preprocessing
      3  - Turn on at both start and end of preprocessing

pre:dual (predual, presolvedual)
      Whether CPLEX' presolve phase should present the CPLEX solution
      algorithm with the primal(-1) or dual(1) problem or (default = 0) should
      decide automatically.

      For compatibility, pre:dual interacts with alg:dualproblem.

pre:folding (folding)
      Whether to try LP folding during preprocessing:

      -1 - Automatic (default)
      0  - Off
      1  - Moderate folding
      2  - Aggressive
      3  - Very aggressive
      4  - Highly aggressive
      5  - Extremely aggressive

pre:node (presolvenode)
      Whether to run presolve at each node of the MIP branch-and-bound:

      -1 - No node presolve
      0  - Automatic (default)
      1  - Always apply presolve at nodes
      2  - Probing on integer-infeasible variables
      3  - Aggressive node probing

pre:passes (prepasses, prepass)
      Limit on the number of CPLEX presolve passes:

      -1 - Automatic choice (default)
      n>=0 - At most n passes.

pre:qcpduals (qcpduals)
      Whether to compute dual values for quadratically constrained problems:

      0 - Do not calculate dual values for QCPs
      1 - Calculate them unless this interferes with presolve reductions
          (default)
      2 - Calculate them, disabling interfering presolve reductions

pre:qpmakepsd (qpmakepsd)
      0/1*: Whether to reformulate a binary-only MIQP or MIQCP so that its
      quadratic matrix becomes positive semi-definite.

pre:qtolin (qtolin)
      Whether to linearize products of bounded variables in quadratic
      objectives during preprocessing:

      -1 - Automatic choice (default)
      0  - No
      1  - Yes.

pre:reduce (prereduce)
      Kinds of reductions permitted during CPLEX presolve:

      0 - No primal or dual reductions
      1 - Only primal reductions
      2 - Only dual reductions
      3 - Both primal and dual reductions (default)

pre:reformulations (prereformulations)
      Reformulations applied during CPLEX presolve:

      0 - None
      1 - Allow reformulations that interfere with crushing forms
      2 - Allow reformulations that interfere with uncrushing forms
      3 - All reformulations (default)

pre:relax (prerelax, relaxpresolve, relpresolve)
      Whether to use CPLEX's presolve on the initial LP relaxation of a MIP:

      -1 - Automatic choice (default)
      0  - No
      1  - Yes.

pre:repeat (repeatpresolve)
      Whether to repeat CPLEX's presolve after root processing:

      -1 - Automatic (default)
      0  - Off
      1  - Repeat presolve without cuts
      2  - Repeat presolve with cuts
      3  - Repeat presolve with cuts and allow new root cuts

pre:scale (scale)
      How to scale the problem:

      -1 - No scaling
      0  - Equilibration (default)
      1  - More aggressive

pre:solve (presolve)
      Whether to use CPLEX's presolve:

      0 - No
      1 - Yes (default)

pre:sos1enc (presos1enc, presos1reform)
      Encoding used for SOS1 reformulation:

      -1 - No reformulation
      0  - Automatic (default)
      1  - Reformulate as linear constraints, with a reformulation which is
           logarithmic in the size of the SOSs.

pre:sos2enc (presos2enc, presos2reform)
      Encoding used for SOS2 reformulation, see pre:sos1enc.

qp:target (optimalitytarget)
      Type of solution to compute for a (MI)QP (not QCP) problem:

      0 - automatic (default)
      1 - assume convex and search for global optimum
      2 - search for first order optimality (not valid for QMIP)
      3 - solve non-convex to global optimality

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
      1e75).

sol:poolgapabs (ams_epsabs, poolagap, poolgapabs)
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
      2 - run "populate" instead of seeking a single best solution

sol:poolpopulatelim (populatelim)
      Limit on number of solutions added to the solution pool by the populate
      algorithm. Default: 20.

sol:poolreplace (poolreplace)
      Policy for replacing solutions in the solution pool if more than
      poolcapacity solutions are generated:

      0 - FIFO (first-in, first-out); default
      1 - Keep best solutions
      2 - Keep most diverse solutions

sol:report_uncertain (report_uncertain_sol)
      0/1*: whether to report objective value(s) in solve_message when
      solve_result is '?' (unknown).

sol:stub (poolstub, ams_stub, solstub, solutionstub)
      Stub for alternative MIP solutions, written to files with names obtained
      by appending "1.sol", "2.sol", etc., to <solutionstub>. The number of
      such files written is affected by the keywords poolgap, poolgapabs,
      poollimit, poolpopulatelim, poolpopulate, poolintensity and poolmode.
      The number of alternative MIP solution files written is returned in
      suffix .nsol on the problem.

tech:auxrootthreads (auxrootthreads)
      Controls the number of threads used for auxiliary chores when solving
      the root node of a MIP problem. When N threads are available (possibly
      limited by "threads"), auxrootthreads must be less than N.

      -1    - Do not use additional threads for auxiliary tasks
      0     - Automatic (default)
      n < N - Use n threads for auxiliary root tasks

tech:bardisplay (bardisplay)
      Specifies how much the barrier algorithm chatters:

      0 - no information (default)
      1 - balanced setup and iteration information
      2 - diagnostic information

tech:clocktype (clocktype)
      Kind of times CPLEX reports and uses for time limits:

      0 - Automatic
      1 - CPU time
      2 - Wall clock time (default)

tech:clonelog (clonelog)
      Whether clone log files are created during parallel optimization:

      -1 - No clone logs
      0  - Automatic (default)
      1  - Write clone logs for parallel optimization

tech:conflictdisplay (conflictdisplay)
      What to report when the conflict finder is working:

      0 - Nothing
      1 - Summary (default)
      2 - Detailed

tech:cpumask (cpumask)
      Whether and how to bind threads to cores on systems where this is
      possible: off=no CPU binding, auto=automatic binding(default). Values
      other than "off" and "auto" must be a hexadecimal string.The lowest
      order bit is for the first logical CPU. For example, "a5" and "A5"
      indicate that CPUs 0, 2, 5, and 7 are available for binding to threads,
      since hex value a5 =2^7+2^5+2^2+2^0.

tech:datacheck (datacheck)
      Data consistency checking and modeling assistance:

      0 - Off (default)
      1 - Check data consistency and issue warnings
      2 - Also offer modeling assistance (warnings about bad scaling etc.)

tech:debug (debug)
      0*/1: whether to assist testing & debugging, e.g., by outputting
      auxiliary information (mostly via suffixes).

tech:endbasis (writebas, endbasis)
      Write the final basis to the specified file (in BAS format).

tech:intsolfileprefix (intsolfileprefix)
      If set, CPLEX writes every MIP integer solution it finds to a file whose
      name starts with this prefix.

tech:logfile (logfile)
      Log file name.

tech:lpdisplay (display, lpdisplay)
      Frequency of displaying LP progress information:

      0 - never (default)
      1 - each factorization
      2 - each iteration

tech:memoryemphasis (memoryemphasis)
      0*/1: Whether to compress data to reduce the memory used, which may make
      some information (e.g., basis condition) unavailable.

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

tech:modisplay (modisplay, multiobjdisplay)
      Level of display during multiobjective optimization:

      0 - No output
      1 - (Default) summary display after each subproblem
      2 - Summary display after each subproblem, as well as subproblem logs

tech:mpslong (mpslong)
      0/1*: Whether to write numbers with full precision to MPS and REW files.

tech:netdisplay (netdisplay)
      Decides what CPLEX reports to the screen during network optimization:

      0 - No display
      1 - Display true objective values (can be non-monotonic)
      2 - (Default) display penalized objective values

tech:nosolve (nosolve)
      Stop after loading the problem and honoring any "writeprob" or
      "writemipstart" directives.

tech:numcores (numcores)
      Write number of logical cores to stdout:

      0 - No (default)
      1 - Yes.

tech:optionfile (optionfile, option:file)
      Name of an AMPL solver option file to read (surrounded by 'single' or
      "double" quotes if the name contains blanks). Lines that start with #
      are ignored. Otherwise, each nonempty line should contain "name=value",
      e.g., "lim:iter=500".

tech:optionnativeread (optionnativeread, tech:param:read, param:read)
      Name of CPLEX parameter file (surrounded by 'single' or "double" quotes
      if the name contains blanks). The easiest approach to use PRM files is
      to export an initial file with tech:optionnativewrite.

tech:optionnativewrite (optionnativewrite, tech:param:write, param:write)
      Name of CPLEX parameter file (surrounded by 'single' or "double" quotes
      if the name contains blanks) to be written. Only parameters with
      non-default values are written.

tech:outlev (outlev)
      Whether to write CPLEX log lines (chatter) to stdout, for granular
      control see "tech:lpdisplay", "tech:mipdisplay", "tech:bardisplay".
      Values:

      0 - no output (default)
      1 - equivalent to "bardisplay"=1, "display"=1, "mipdisplay"=2
      2 - equivalent to "bardisplay"=2, "display"=2, "mipdisplay"=5

tech:outlev_mp (outlev_mp)
      0*/1: whether to print MP model information.

tech:parallelmode (parallelmode)
      Parallel optimization mode:

      -1 - Opportunistic
      0  - Automatic (default)
      1  - Deterministic

tech:prestats (prestats)
      0*/1: Whether to include CPLEX's presolve statistics (aggregator and
      presolve log lines) in the solve_message.

tech:pretunefileprm (pretunefileprm, pretunefile)
      File to which nondefault keyword settings are written in CPLEX PRM
      format before tuning.

tech:record (record)
      0*/1: Whether to record CPLEX library calls for debugging use by IBM in
      a file with an automatically chosen name of the form cplexXXXXXXX.db.

tech:seed (seed)
      Seed for random number generator used internally by CPLEX. Use "seed=?"
      to see the default, which depends on the CPLEX release.

tech:siftdisplay (siftdisplay)
      How much the sifting algorithm reports:

      0 - No display
      1 - Display major iterations (default)
      2 - Display LP subproblem information

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
      Default maximum number of threads for any of the parallel CPLEX
      optimizers (simplex, barrier, MIP, concurrent); default 0 ==> automatic
      choice (maximum available, subject to the license).

tech:timing (timing, tech:report_times, report_times)
      0*/1/2: Whether to print and return timings for the run, all times are
      wall times. If set to 1, return the solution times in the problem
      suffixes 'time_solver', 'time_setup' and 'time', 'time'=
      time_solver+time_setup+time_output is a measure of the total time spent
      in the solver driver. If set to 2, return more granular times, including
      'time_read', 'time_conversion' and 'time_output'.

tech:tunedisplay (tunedisplay)
      How much to print during tuning:

      0 - Nothing
      1 - Minimal printing (default)
      2 - Show parameters being tried
      3 - Exhaustive printing

tech:tunefile (tunefile, tunefileprm, tech:tunebase, tunebase)
      Name of file for tuning results in CPLEX PRM format. If specified, CPLEX
      will experiment with parameter settings that would make solving faster.
      This can significantly increase execution time of the current
      invocation, but the settings it finds might save time in future runs.

tech:tunefix (tunefix)
      List of option names not to tune (their current values are kept),
      separated by commas or white space; enclose in quotes if the list
      contains white space.

tech:tunefixfile (tunefixfile)
      Name of a file containing option names not to tune, merged with
      tech:tunefix.

tech:tunemeasure (tunemeasure)
      How tuning compares parameter sets across models:

      1 - Mean time over the models (default)
      2 - Minmax approach

tech:tunerepeat (tunerepeat)
      How many times to perturb the problem during tuning (default = 1).

tech:tunetimedet (tunetimedet)
      Limit (in "ticks") on tuning time; meaningful if < time (default = 1e75)

tech:tunetimelim (tunetimelim, tunetime)
      Limit (in seconds) on tuning time; meaningful if < time (default = 1e75)

tech:version (version)
      Single-word phrase: report version details before solving the problem.

tech:wantsol (wantsol)
      In a stand-alone invocation (no "-AMPL" on the command line), what
      solution information to write. Sum of

      1 - Write ".sol" file
      2 - Primal variables to stdout
      4 - Dual variables to stdout
      8 - Suppress solution message.

tech:warninglimit (warninglimit)
      Limit on the number of warnings per issue given when tech:datacheck=2;
      default 10.

tech:workdir (nodefiledir, workfiledir, workdir)
      Directory where CPLEX creates a temporary subdirectory for temporary
      files, e.g., for node information and Cholesky factors.

tech:workfilelim (workfilelim)
      Maximum size in megabytes for in-core work "files" (central memory used
      before node files are written); default 2048.

tech:writegraph (cvt:writegraph, writegraph, exportgraph)
      File to export conversion graph. Format: JSON Lines.

tech:writelevel (writelevel)
      Level of detail written to SOL and MST files (tech:writesolution,
      tech:writemipstart):

      0 - Automatic (default): all variables in SOL files, discrete variables
          in MST files
      1 - All variables
      2 - Discrete variables only
      3 - Variables with nonzero values only
      4 - Discrete variables with nonzero values only

tech:writemipstart (writemipstart)
      The name of a file to which the MIP starting guess(if any) is written in
      ".mst" format.

tech:writemodel (tech:writeprob, writeprob, writemodel, tech:exportfile)
      Specifies files where to export the model before solving (repeat the
      option for several files.) File name extensions can be ".lp[.7z]",
      ".mps", etc.
      To write a model during iterative solve (e.g., with obj:multi=2), use
      tech:writemodel:index.

      Cplex-specific file name extensions are ".sav", ".mps", ".lp", ".rmp",
      ".rew", ".rlp"

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

      File name extensions can be ".sol[.gz|.zip]", ".clp", ".bas".
```

