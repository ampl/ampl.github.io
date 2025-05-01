
# CPLEX Options

```ampl
ampl: option solver cplex; # change the solver
ampl: option cplex_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

Solver options obtained with `$ cplex -=`.

```
IBM ILOG CPLEX Optimizer Options for AMPL
--------------------------------------------

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
      Whether to use or return a basis:

      0 - No
      1 - Use incoming basis (if provided)
      2 - Return final basis
      3 - Both (1 + 2 = default)

alg:benders (benders, bendersopt)
      Solve MIP using Benders algorithm. Both integer and continuous variables
      must be present.

alg:benders_feascuttol (benders_feascut_tol)
      Tolerance for violations of feasibility cuts in Benders
      algorithm(default 1e-6).

alg:benders_optcut_tol (benders_optcut_tol)
      Tolerance for violations of optimality cuts in Benders algorithm(default
      1e-6).

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

alg:dualopt (alg:dual, dualopt)
      Solve (MIP node) LPs by dual simplex method.

alg:dualproblem (dual)
      Compatibility option with the legacy cplexasl driver. Interacts with
      pre:dual as follows:

      alg:dualproblem - alone, equivalent to pre:dual=0
      alg:dualproblem pre:dual=-1 - together, equivalent to pre:dual=1
      alg:dualproblem pre:dual=0 - together, equivalent to pre:dual=0
      alg:dualproblem pre:dual=1 - together, equivalent to pre:dual=-1.

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

alg:feastol (feastol)
      Primal feasibility tolerance (default 1e-6, possible values are between
      1e-9 and 0.1).

alg:iisfind (iisfind, iis)
      Whether to find and export an IIS. Default = 0 (don't export).

alg:kappa (kappa, basis_cond)
      Whether to return the estimated condition number (kappa) of the optimal
      basis (default 0): sum of 1 = report kappa in the result message; 2 =
      return kappa in the solver-defined suffix .kappa on the objective and
      problem. The request is ignored when there is no optimal basis.

alg:lbpen (lbpen)
      See alg:feasrelax.

alg:method (method, lpmethod, qpmethod, simplex, mip:method, mipstartalg)
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
      Overrides netopt option and primalopt/dualopt/barrier/network/sifting
      flags.

alg:netfeasibility (netfeasibility, netfeastol)
      Feasibility tolerance for network primal optimization. Can be any number
      from 1e-11 to 1e-1; default: 1e-6.

alg:netfind (netfind, netfinder)
      Level of network extraction for network simplex optimization:

      0 - Extract pure network only
      1 - (Default) try reflection scaling
      2 - Try general scaling

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

alg:primalopt (alg:primal, primalopt)
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

alg:sifting (sifting, siftopt, siftingopt)
      Solve (MIP node) LPs by sifting method.

alg:start (warmstart)
      Whether to use incoming primal (and dual, for LP) variable values in a
      warmstart:

      0 - No
      1 - Yes (for LP: if there is no incoming alg:basis) (default)
      2 - Yes (for LP: ignoring the incoming alg:basis, if any.)

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
      1e12).

bar:iterlim (bariterlim)
      Maximum barrier iterations allowed (default 9223372036800000000).

bar:objrange (barobjrange)
      Limit on the absolute objective value before the barrier algorithm
      considers the problem unbounded (default 1e20).

bar:start (barstart, barstartalg)
      Barrier starting-point algorithm:

      1 - Assume dual is 0 (default)
      2 - Estimate dual
      3 - Average of primal estimate, 0 dual
      4 - Average of primal and dual estimates

cut:aggforcut (aggforcut)
      Bound on the number of constraints aggregated to generate flow-cover and
      mixed-integer-rounding cuts (default 3).

cut:aggtol (aggtol)
      Pivot tolerance for aggregating. It seldom needs fiddling. Default =
      .05; must be in [1e-10, .99].

cut:bqp (bqpcuts)
      Whether to enable Boolean Quadric Polytope cut generation for nonconvex
      QP and MIQP problems, choices as for "cut:cuts".

cut:clique (cliquecuts)
      Whether to use clique cuts in solving MIPs, choices as for "cut:cuts".

cut:cover (covercuts, covers)
      Whether to use cover cuts in solving MIPs, choices as for "cut:cuts".

cut:cuts (cuts, mipcuts)
      Global cut generation control, valid unless overridden by individual
      cut-type controls:

      -1 - Disallow
      0  - Automatic (default)
      1  - Enable moderate cuts generation
      2  - Enable aggressive cuts generation.
      3  - Enable very aggressive cuts generation.

cut:disj (disjcuts)
      Whether to use disjunctive cuts in solving MIPs, choices as for
      "cut:cuts".

cut:eachcutlim (eachcutlim)
      Limit on the number of cuts of each time; default=2100000000.

cut:factor (cutsfactor, cutfactor)
      Limit on MIP cuts added:

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

cut:liftandproject (liftandproject, liftandprojectcuts)
      Whether to use lift and project cuts in solving MIPs, choices as for
      "cut:cuts".

cut:localimplied (localimplied, localimpliedcuts)
      Whether to use locally valid implied cuts in solving MIPs, choices as
      for "cut:cuts".

cut:mfc (mfccuts)
      Whether to use multi-commodity flow (MCF) cuts in solving MIPs, choices
      as for "cut:flowcover".

cut:mir (mircuts)
      Whether to use MIP roundind cuts in solving MIPs, choices as for
      "cut:flowcover".

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

lim:dettime (dettimelim)
      Time limit in platform-dependent "ticks".

lim:iter (iterlim, iterlimit, iterations)
      LP iteration limit (default: large).

lim:netiterations (netiterations, netiter)
      Limit on network simplex iterations (default: large).

lim:nodes (node, nodelim, nodelimit)
      Maximum MIP nodes to explore (default: 2^31 - 1).

lim:sol (sollimit, solutionlimit, mipsolutions)
      Limit the number of feasible MIP solutions found, causing early
      termination if exceeded; default = 2e31-1

lim:time (timelim, timelimit, time)
      limit on solve time (in seconds; default: no limit).

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

lp:doperturb (doperturb)
      Decides whether to perturb problems when using simplex, setting it to 1
      is occasionally helpful for highly degenerate problems.:

      0 - No (default)
      1 - Yes.

lp:perturb (perturb)
      Amount by which to perturb variable bounds when perturbing problems (see
      "perturb"); default=1e-6, must be positive.

lp:perturblim (perturblim, perturblimit)
      Number of stalled simplex iterations before the problem is perturbed;
      default=0 => automatic.

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
      Whether to compute duals / basis / sensitivity for MIP models:

      0 - No (default)
      1 - Yes.

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

mip:focus (mip:emphasis, mipemphasis, mipfocus)
      MIP solution strategy:

      0 - Balance finding good feasible solutions and proving optimality
          (default)
      1 - Favor finding feasible solutions
      2 - Favor providing optimality
      3 - Focus on improving the best objective bound
      4 - Focus on finding hidden feasible solutions
      5 - Focus on finding high quality solutions earlier (heuristic).

mip:fpheur (fpheur)
      Whether to use the feasibility pump heuristic on MIP problems:

      -1 - No
      0  - Automatic (default)
      1  - Yes, focus on finding a feasible solution
      2  - Yes, focus on finding a good objective value at a feasible
           solution

mip:gap (mipgap)
      Max. relative MIP optimality gap (default 1e-4).

mip:gapabs (mipgapabs, absmipgap)
      Max. absolute MIP optimality gap (default 1e-6).

mip:inttol (inttol, intfeastol, integrality)
      Feasibility tolerance for integer variables (default 1e-05, must be in
      [0.0, 0.5])

mip:nodefile (nodefile)
      Whether to save node information in a temporary file:

      0 - No
      1 - Compressed node file in memory (default)
      2 - Node file on disk
      3 - Compressed node file on disk

mip:nodemethod (nodemethod, mipalg, mipalgorithm)
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

mip:search (mipsearch)
      Search strategy for mixed-integer problems:

      0 - Automatic (default)
      1 - Traditional branch and cut
      2 - Dynamic search

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

mip:submipscale (submipscale)
      Rarely used choice of scaling for auxiliary subMIPs (described with
      "submipalg"):

      -1 - No scaling
      0  - Equilibration (default)
      1  - More aggressive

mip:submipstartalg (submipstartalg)
      Rarely used choice of algorithm for the initial relaxation of a subMIP
      (described with "submipalg"):

      0 - Automatic (default)
      1 - Primal simplex
      2 - Dual simplex
      3 - Network simplex
      4 - Barrier
      5 - Sifting
      6 - Concurrent (dual, barrier and primal in opportunistic mode; dual
          and barrier in deterministic mode; 4 is used for MIPQs).

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

pre:dual (predual)
      Whether CPLEX' presolve phase should present the CPLEX solution
      algorithm with the primal(-1) or dual(1) problem or (default = 0) should
      decide automatically.

      For compatibility, pre:dual interacts with alg:dualproblem.

pre:node (presolvenode)
      Whether to run presolve at each node of the MIP branch-and-bound:

      -1 - No
      0  - Automatic choice (default)
      1  - Yes.

pre:passes (prepasses, prepass)
      Limit on the number of CPLEX presolve passes:

      -1 - Automatic choice (default)
      n>=0 - At most n passes.

pre:reformulations (prereformulations)
      Kinds of reductions permitted during CPLEX presolve:

      0 - None
      1 - Allow reformulations that interphere with crushing forms
      2 - Allow reformulations that interphere with uncrushing forms
      3 - All reformulations (default)

pre:relax (prerelax)
      Whether to use CPLEX's presolve on the initial LP relaxation of a MIP:

      -1 - Automatic choice (default)
      0  - No
      1  - Yes.

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

sol:stub (ams_stub, solstub, solutionstub)
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

tech:debug (debug)
      0*/1: whether to assist testing & debugging, e.g., by outputting
      auxiliary information (mostly via suffixes).

tech:endbasis (writebas, endbasis)
      Write the final basis to the specified file (in BAS format).

tech:logfile (logfile)
      Log file name.

tech:lpdisplay (display, lpdisplay)
      Frequency of displaying LP progress information:

      0 - never (default)
      1 - each factorization
      2 - each iteration

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

tech:outlev (outlev)
      Whether to write CPLEX log lines (chatter) to stdout,for granular
      control see "tech:lpdisplay", "tech:mipdisplay",
      "tech:bardisplay".Values:

      0 - no output (default)
      1 - equivalent to "bardisplay"=1, "display"=1, "mipdisplay"=2
      2 - equivalent to "bardisplay"=2, "display"=2, "mipdisplay"=5

tech:outlev_mp (outlev_mp)
      0*/1: whether to print MP model information.

tech:seed (seed)
      Seed for random number generator used internally by CPLEX.Use "seed=?"
      to see the default, which depends on the CPLEX release.

tech:threads (threads)
      How many threads to use when using the barrier algorithm
      or solving MIP problems; default 0 ==> automatic choice.

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

tech:workdir (nodefiledir, workfiledir, workdir)
      Directory where CPLEX creates a temporary subdirectory for temporary
      files, e.g., for node information and Cholesky factors.

tech:workfilelim (workfilelim)
      Maximum size in megabytes for in-core work "files". Default 2048.

tech:writegraph (cvt:writegraph, writegraph, exportgraph)
      File to export conversion graph. Format: JSON Lines.

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
      result files in solver's native formats. Option can be repeated. File
      name extensions can be ".sol[.tar.gz]", ".json", ".bas", ".ilp", etc.
```

