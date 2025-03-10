
# CBC Options

```ampl
ampl: option solver cbc; # change the solver
ampl: option cbc_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

Solver options obtained with `$ cbc -=`.

```
CBC Optimizer Options for AMPL
--------------------------------------------

To set these options, assign a string specifying their values to the AMPL
option "cbc_options". For example:

   ampl: option cbc_options 'presolve=more';

 Options:

:cplexUse (cplexUse)
      Whether to use Cplex!

      off - Turn off
      on  - Turn on

:mixedIntegerRoundingCuts (mixedIntegerRoundingCuts)
      Whether to use Mixed Integer Rounding cuts

      off      - disabled
      on       - enabled
      root     - enabled only on root node
      ifmove   - enabled in the tree if it moves the objective value
      forceOn  - enabled at every node
      onglobal - 

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

alg:basis (basis)
      Whether to use or return a basis:

      0 - No
      1 - Use incoming basis (if provided)
      2 - Return final basis
      3 - Both (1 + 2 = default)

alg:perturbation (perturbation)
      Whether to perturb the problem

      off - Turn off
      on  - Turn on

alg:relax (relax)
      0*/1: Whether to relax integrality of variables.

alg:start (warmstart)
      Whether to use incoming primal (and dual, for LP) variable values in a
      warmstart:

      0 - No
      1 - Yes (for LP: if there is no incoming alg:basis) (default)
      2 - Yes (for LP: ignoring the incoming alg:basis, if any.)

bar:bscale (bscale)
      Whether to scale in barrier (and ordering speed)

      off  - 
      on   - 
      off1 - 
      on1  - 
      off2 - 
      on2  - 

bar:cholesky (cholesky)
      Which cholesky algorithm

      native                    - 
      dense                     - 
      fudgeLong_dummy           - 
      wssmp_dummy               - 
      UniversityOfFlorida_dummy - 
      Taucs_dummy               - 
      Mumps_dummy               - 
      Pardiso_dummy             - 

bar:crash (crash)
      Whether to create basis for problem

      off - Turn off
      on  - Turn on

bar:crossover (crossover)
      Whether to get a basic solution with the simplex algorithm after the
      barrier algorithm finished

      on       - 
      off      - 
      maybe    - 
      presolve - 

bar:gammadelta (gamma(Delta))
      Whether to regularize barrier

      off         - 
      on          - 
      gamma       - 
      delta       - 
      onstrong    - 
      gammastrong - 
      deltastrong - 

bar:kkt (KKT)
      Whether to use KKT factorization in barrier

      off - Turn off
      on  - Turn on

cut:cliqueCuts (cliqueCuts)
      Whether to use Clique cuts

      off      - disabled
      on       - enabled
      root     - enabled only on root node
      ifmove   - enabled in the tree if it moves the objective value
      forceOn  - enabled at every node
      onglobal - 

cut:cut (cutsOnOff)
      Switches all cut generators on or off

      off     - disabled
      on      - enabled
      root    - enabled only on root node
      ifmove  - enabled in the tree if it moves the objective value
      forceOn - enabled at every node

cut:flowcovercuts (flowCoverCuts)
      Whether to use Flow Cover cuts

      off      - disabled
      on       - enabled
      root     - enabled only on root node
      ifmove   - enabled in the tree if it moves the objective value
      forceOn  - enabled at every node
      onglobal - 

cut:gmicuts (GMICuts)
      Whether to use alternative Gomory cuts

      off         - 
      on          - 
      root        - 
      ifmove      - 
      forceOn     - 
      endonly     - 
      long        - 
      longroot    - 
      longifmove  - 
      forceLongOn - 
      longendonly - 

cut:gomorycuts (gomoryCuts)
      Whether to use Gomory cuts

      off            - 
      on             - 
      root           - 
      ifmove         - 
      forceOn        - 
      onglobal       - 
      forceandglobal - 
      forceLongOn    - 
      long           - 

cut:knapsackcuts (knapsackCuts)
      Whether to use Knapsack cuts

      off            - 
      on             - 
      root           - 
      ifmove         - 
      forceOn        - 
      onglobal       - 
      forceandglobal - 

cut:lagomorycuts (lagomoryCuts)
      Whether to use Lagrangean Gomory cuts

      off             - 
      endonlyroot     - 
      endcleanroot    - 
      root            - 
      endonly         - 
      endclean        - 
      endboth         - 
      onlyaswell      - 
      cleanaswell     - 
      bothaswell      - 
      onlyinstead     - 
      cleaninstead    - 
      bothinstead     - 
      onlyaswellroot  - 
      cleanaswellroot - 
      bothaswellroot  - 

cut:latwomircuts (latwomirCuts)
      Whether to use Lagrangean TwoMir cuts

      off          - 
      endonlyroot  - 
      endcleanroot - 
      endbothroot  - 
      endonly      - 
      endclean     - 
      endboth      - 
      onlyaswell   - 
      cleanaswell  - 
      bothaswell   - 
      onlyinstead  - 
      cleaninstead - 
      bothinstead  - 

cut:liftandprojectcuts (liftAndProjectCuts)
      Whether to use Lift and Project cuts

      off     - disabled
      on      - enabled
      root    - enabled only on root node
      ifmove  - enabled in the tree if it moves the objective value
      forceOn - enabled at every node

cut:probingCuts (probingCuts)
      Whether to use Probing cuts

      off              - 
      on               - 
      root             - 
      ifmove           - 
      forceOn          - 
      onglobal         - 
      forceonglobal    - 
      forceOnBut       - 
      forceOnStrong    - 
      forceOnButStrong - 
      strongRoot       - 

cut:reduce2andsplitcts (reduce2AndSplitCuts)
      Whether to use Reduce-and-Split cuts - style 2

      off      - 
      on       - 
      root     - 
      longOn   - 
      longRoot - 

cut:reduceandsplitcuts (reduceAndSplitCuts)
      Whether to use Reduce-and-Split cuts

      off     - disabled
      on      - enabled
      root    - enabled only on root node
      ifmove  - enabled in the tree if it moves the objective value
      forceOn - enabled at every node

cut:residualcapacitycuts (residualCapacityCuts)
      Whether to use Residual Capacity cuts

      off     - disabled
      on      - enabled
      root    - enabled only on root node
      ifmove  - enabled in the tree if it moves the objective value
      forceOn - enabled at every node

cut:twomircuts (twoMirCuts)
      Whether to use Two phase Mixed Integer Rounding cuts

      off            - 
      on             - 
      root           - 
      ifmove         - 
      forceOn        - 
      onglobal       - 
      forceandglobal - 
      forceLongOn    - 

cut:zeroHalfCuts (zeroHalfCuts)
      Whether to use zero half cuts

      off      - disabled
      on       - enabled
      root     - enabled only on root node
      ifmove   - enabled in the tree if it moves the objective value
      forceOn  - enabled at every node
      onglobal - 

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

cvt:quadcon (passquadcon)
      Convenience option. Set to 0 to disable quadratic constraints. Synonym
      for acc:quad..=0. Currently this disables out-multiplication of
      quadratic terms, then they are linearized.

cvt:quadobj (passquadobj)
      0*/1: Pass quadratic objective terms to the solver, If the solver
      accepts quadratic constraints, such a constraint will be created with
      those, otherwise linearly approximated.

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
      0/1*: Whether to honor SOS2 constraints for nonconvex piecewise-linear
      terms, using suffixes .sos and .sosref provided by AMPL.

cvt:uenc:negctx:max (uenc:negctx:max, uenc:negctx)
      If cvt:uenc:ratio applies, max number of constants in comparisons
      x==const in negative context (equivalently, x!=const in positive
      context) to skip UEnc(x). Default 1.

cvt:uenc:ratio (uenc:ratio)
      Min ratio (ub-lb)/Nvalues to skip unary encoding for a variable x, where
      Nvalues is the number of constants used in conditional comparisons
      x==const. Instead, indicator constraints (or big-Ms) are used, if
      uenc:negctx also applies. Default 0.

double:allowableGap (allowableGap)
      Stop when gap between best possible and best less than this (default 0).

double:artificialCost (artificialCost)
      Costs >= this treated as artificials in feasibility pump (default 0).

double:cutoff (cutoff)
      Bound on the objective value for all solutions (default 1e+50).

double:dextra3 (dextra3)
      Extra double parameter 3 (default 0).

double:dextra4 (dextra4)
      Extra double parameter 4 (default 0).

double:dextra5 (dextra5)
      Extra double parameter 5 (default 0).

double:dualBound (dualBound)
      Initially algorithm acts as if no gap between bounds exceeds this value
      (default 1e+10).

double:dualTolerance (dualTolerance)
      For an optimal solution no dual infeasibility may exceed this value
      (default 1e-07).

double:fixOnDj (fixOnDj)
      Try heuristic based on fixing variables with reduced costs greater than
      this (default -1).

double:fractionforBAB (fractionforBAB)
      Fraction in feasibility pump (default 0.5).

double:increment (increment)
      A valid solution must be at least this much better than last integer
      solution (default 1e-05).

double:infeasibilityWeight (infeasibilityWeight)
      Each integer infeasibility is expected to cost this much (default 0).

double:integerTolerance (integerTolerance)
      For a feasible solution no integer variable may be more than this away
      from an integer value (default 1e-07).

double:objectiveScale (objectiveScale)
      Scale factor to apply to objective (default 1).

double:preTolerance (preTolerance)
      Tolerance to use in presolve (default 1e-08).

double:primalTolerance (primalTolerance)
      For a feasible solution no primal infeasibility, i.e., constraint
      violation, may exceed this value (default 1e-07).

double:primalWeight (primalWeight)
      Initially algorithm acts as if it costs this much to be infeasible
      (default 1e+10).

double:psi (psi)
      Two-dimension pricing factor for Positive Edge criterion (default -0.5).

double:pumpCutoff (pumpCutoff)
      Fake cutoff for use in feasibility pump (default 0).

double:pumpIncrement (pumpIncrement)
      Fake increment for use in feasibility pump (default 0).

double:ratioGap (ratioGap)
      Stop when gap between best possible and best known is less than this
      fraction of larger of two (default 0).

double:reallyObjectiveScale (reallyObjectiveScale)
      Scale factor to apply to objective in place (default 1).

double:rhsScale (rhsScale)
      Scale factor to apply to rhs and bounds (default 1).

double:seconds (seconds)
      maximum seconds (default 1e+08).

double:tightenFactor (tightenFactor)
      Tighten bounds using this times largest activity at continuous solution
      (default -1).

double:zeroTolerance (zeroTolerance)
      Kill all coefficients whose absolute value is less than this value
      (default 1e-20).

int:cppGenerate (cppGenerate)
      Generates C++ code (default -1).

int:cutDepth (cutDepth)
      Depth in tree at which to do cuts (default -1).

int:cutLength (cutLength)
      Length of a cut (default -1).

int:decompose (decompose)
      Whether to try decomposition (default 0).

int:denseThreshold (denseThreshold)
      Threshold for using dense factorization (default -1).

int:depthMiniBab (depthMiniBab)
      Depth at which to try mini branch-and-bound (default -1).

int:diveOpt (diveOpt)
      Diving options (default -1).

int:diveSolves (diveSolves)
      Diving solve option (default 100).

int:dualize (dualize)
      Solves dual reformulation (default 3).

int:expensiveStrong (expensiveStrong)
      Whether to do even more strong branching (default 0).

int:experiment (experiment)
      Whether to use testing features (default 0).

int:extra1 (extra1)
      Extra integer parameter 1 (default -1).

int:extra2 (extra2)
      Extra integer parameter 2 (default -1).

int:extra3 (extra3)
      Extra integer parameter 3 (default -1).

int:extra4 (extra4)
      Extra integer parameter 4 (default -1).

int:extraVariables (extraVariables)
      Allow creation of extra integer variables (default 0).

int:forceSolution (forceSolution)
      Whether to use given solution as crash for BAB (default -1).

int:hOptions (hOptions)
      Heuristic options (default 0).

int:hotStartMaxIts (hotStartMaxIts)
      Maximum iterations on hot start (default 100).

int:idiotCrash (idiotCrash)
      Whether to try idiot crash (default -1).

int:logLevel (logLevel)
      Level of detail in Coin branch and Cut output (default 1).

int:maxFactor (maxFactor)
      Maximum number of iterations between refactorizations (default 200).

int:maxIterations (maxIterations)
      Maximum number of iterations before stopping (default 2147483647).

int:maxNodes (maxNodes)
      Maximum number of nodes to do (default 2147483647).

int:maxSavedSolutions (maxSavedSolutions)
      Maximum number of solutions to save (default -1).

int:maxSolutions (maxSolutions)
      Maximum number of feasible solutions to get (default -1).

int:mipOptions (mipOptions)
      Dubious options for mip (default 1057).

int:moreMipOptions (moreMipOptions)
      More dubious options for mip (default -1).

int:moreSpecialOptions (moreSpecialOptions)
      Yet more dubious options for Simplex - see ClpSimplex.hpp (default -1).

int:moreTune (moreTune)
      Yet more dubious ideas for feasibility pump (default 0).

int:multipleRootPasses (multipleRootPasses)
      Do multiple root passes to collect cuts and solutions (default 0).

int:numberAnalyze (numberAnalyze)
      Number of analysis iterations (default -1).

int:outputFormat (outputFormat)
      Which output format to use (default 2).

int:passCuts (passCuts)
      Number of rounds that cut generators are applied in the root node
      (default 20).

int:passFeasibilityPump (passFeasibilityPump)
      How many passes to do in the Feasibility Pump heuristic (default 20).

int:passPresolve (passPresolve)
      How many passes in presolve (default 5).

int:passTreeCuts (passTreeCuts)
      Number of rounds that cut generators are applied in the tree (default
      1).

int:pertValue (pertValue)
      Method of perturbation (default 50).

int:pOptions (pOptions)
      Dubious print options (default 0).

int:preOpt (preOpt)
      Presolve options (default -1).

int:pumpTune (pumpTune)
      Dubious ideas for feasibility pump (default 1003).

int:randomCbcSeed (randomCbcSeed)
      Random seed for Cbc (default -1).

int:randomSeed (randomSeed)
      Random seed for Clp (default 1234567).

int:slogLevel (slogLevel)
      Level of detail in (LP) Solver output (default 1).

int:slowcutpasses (slowcutpasses)
      Maximum number of rounds for slower cut generators (default 10).

int:slpValue (slpValue)
      Number of slp passes before primal (default -1).

int:smallFactorization (smallFactorization)
      Threshold for using small factorization (default -1).

int:specialOptions (specialOptions)
      Dubious options for Simplex - see ClpSimplex.hpp (default -1).

int:sprintCrash (sprintCrash)
      Whether to try sprint crash (default -1).

int:strategy (strategy)
      Switches on groups of features (default 1).

int:strongBranching (strongBranching)
      Number of variables to look at in strong branching (default 5).

int:substitution (substitution)
      How long a column to substitute for in presolve (default 3).

int:testOsi (testOsi)
      Test OsiObject stuff (default -1).

int:trustPseudoCosts (trustPseudoCosts)
      Number of branches before we trust pseudocosts (default 5).

int:tunePreProcess (tunePreProcess)
      Dubious tuning parameters for preprocessing (default -1).

int:verbose (verbose)
      Switches on longer help on single ? (default 0).

int:vubheuristic (vubheuristic)
      Type of VUB heuristic (default -1).

lim:time (timelim, timelimit)
      Limit on solve time (in seconds; default: no limit).

lp:dualpivot (dualPivot)
      Dual pivot choice algorithm

      automatic  - 
      dantzig    - 
      partial    - 
      steepest   - 
      PEsteepest - 
      PEdantzig  - 

lp:pfi (PFI)
      Whether to use Product Form of Inverse in simplex

      off - Turn off
      on  - Turn on

lp:primalpivot (primalPivot)
      Primal pivot choice algorithm

      auto!matic - 
      exact      - 
      dantzig    - 
      partial    - 
      steepest   - 
      change     - 
      sprint     - 
      PEsteepest - 
      PEdantzig  - 

mip:combine2Solutions (combine2Solutions)
      Whether to use crossover solution heuristic

      off    - disabled
      on     - use every node in the tree
      both   - 
      before - 

mip:combineSolutions (combineSolutions)
      Whether to use combine solution heuristic

      off         - 
      on          - 
      both        - 
      before      - 
      onquick     - 
      bothquick   - 
      beforequick - 

mip:constraintfromCutoff (constraintfromCutoff)
      Whether to use cutoff as constraint

      off           - 
      on            - 
      variable      - 
      forcevariable - 
      conflict      - 

mip:costStrategy (costStrategy)
      How to use costs for branching priorities

      off          - 
      priorities   - 
      columnOrder  - 
      01first      - 
      01last       - 
      length       - 
      singletons   - 
      nonzero      - 
      generalForce - 

mip:dins (Dins)
      Whether to try Distance Induced Neighborhood Search

      off    - 
      on     - 
      both   - 
      before - 
      often  - 

mip:divingcoefficient (DivingCoefficient)
      Whether to try Coefficient diving heuristic

      off    - disabled
      on     - use every node in the tree
      both   - 
      before - 

mip:divingfractional (DivingFractional)
      Whether to try Fractional diving heuristic

      off    - disabled
      on     - use every node in the tree
      both   - 
      before - 

mip:divingguided (DivingGuided)
      Whether to try Guided diving heuristic

      off    - disabled
      on     - use every node in the tree
      both   - 
      before - 

mip:divinglinesearch (DivingLineSearch)
      Whether to try Linesearch diving heuristic

      off    - disabled
      on     - use every node in the tree
      both   - 
      before - 

mip:divingpseudocost (DivingPseudoCost)
      Whether to try Pseudocost diving heuristic

      off    - disabled
      on     - use every node in the tree
      both   - 
      before - 

mip:divingsome (DivingSome)
      Whether to try Diving heuristics

      off    - disabled
      on     - use every node in the tree
      both   - 
      before - 

mip:divingvectorlength (DivingVectorLength)
      Whether to try Vectorlength diving heuristic

      off    - disabled
      on     - use every node in the tree
      both   - 
      before - 

mip:dwHeuristic (dwHeuristic)
      Whether to try Dantzig Wolfe heuristic

      off    - disabled
      on     - use every node in the tree
      both   - 
      before - 

mip:feasibilitypumpfeasibilityPump
      Whether to try the Feasibility Pump heuristic

      off    - disabled
      on     - use every node in the tree
      both   - 
      before - 

mip:greedyheuristic (greedyHeuristic)
      Whether to use a greedy heuristic

      off    - disabled
      on     - use every node in the tree
      both   - 
      before - 

mip:heuristics (heuristicsOnOff)
      Switches most primal heuristics on or off

      off - Turn off
      on  - Turn on

mip:localtreesearch (localTreeSearch)
      Whether to use local tree search when a solution is found

      off - Turn off
      on  - Turn on

mip:naiveheuristics (naiveHeuristics)
      Whether to try some stupid heuristic

      off    - disabled
      on     - use every node in the tree
      both   - 
      before - 

mip:nodestrategy (nodeStrategy)
      What strategy to use to select the next node from the branch and cut
      tree

      hybrid     - 
      fewest     - 
      depth      - 
      upfewest   - 
      downfewest - 
      updepth    - 
      downdepth  - 

mip:pivotandcomplement (pivotAndComplement)
      Whether to try Pivot and Complement heuristic

      off    - disabled
      on     - use every node in the tree
      both   - 
      before - 

mip:pivotandfix (pivotAndFix)
      Whether to try Pivot and Fix heuristic

      off    - disabled
      on     - use every node in the tree
      both   - 
      before - 

mip:proximitysearch (proximitySearch)
      Whether to do proximity search heuristic

      off    - 
      on     - 
      both   - 
      before - 
      10     - 
      100    - 
      300    - 

mip:randomizedrounding (randomizedRounding)
      Whether to try randomized rounding heuristic

      off    - disabled
      on     - use every node in the tree
      both   - 
      before - 

mip:rens (Rens)
      Whether to try Relaxation Enforced Neighborhood Search

      off         - 
      on          - 
      both        - 
      before      - 
      200         - 
      1000        - 
      10000       - 
      dj          - 
      djbefore    - 
      usesolution - 

mip:rins (Rins)
      Whether to try Relaxed Induced Neighborhood Search

      off    - 
      on     - 
      both   - 
      before - 
      often  - 

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

mip:roundingheuristic (roundingHeuristic)
      Whether to use simple (but effective) Rounding heuristic

      off    - disabled
      on     - use every node in the tree
      both   - 
      before - 

mip:vndvariableneighborhoodsearch (VndVariableNeighborhoodSearch)
      Whether to try Variable Neighborhood Search

      off    - 
      on     - 
      both   - 
      before - 
      intree - 

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

pre:autoScale
      Whether to scale objective, rhs and bounds of problem if they look odd:

      off - Turn off
      on  - Turn on

pre:biasLU
      Whether factorization biased towards U:

      UU - 
      UX - 
      LX - 
      LL - 

pre:factorization (factorization)
      Which factorization to use

      normal - 
      dense  - 
      simple - 
      osl    - 

pre:preprocess (preprocess)
      Whether to use integer preprocessing

      off             - 
      on              - 
      save            - 
      equal           - 
      sos             - 
      trysos          - 
      equalall        - 
      strategy        - 
      aggregate       - 
      forcesos        - 
      stopaftersaving - 

pre:presolve (presolve)
      Whether to presolve problem

      on   - 
      off  - 
      more - 
      file - 

pre:scaling (scaling)
      Whether to scale problem

      off         - 
      equilibrium - 
      geometric   - 
      automatic   - 
      dynamic     - 
      rowsonly    - 

pre:sparsefactor (sparseFactor)
      Whether factorization treated as sparse

      off - Turn off
      on  - Turn on

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

tech:debug (debug)
      0*/1: whether to assist testing & debugging, e.g., by outputting
      auxiliary information (mostly via suffixes).

tech:messages (messages)
      Controls if Clpnnnn is printed

      off - Turn off
      on  - Turn on

tech:optionfile (optionfile, option:file)
      Name of an AMPL solver option file to read (surrounded by 'single' or
      "double" quotes if the name contains blanks). Lines that start with #
      are ignored. Otherwise, each nonempty line should contain "name=value",
      e.g., "lim:iter=500".

tech:outlev (outlev)
      0*-4: Whether to write log lines (chatter) to stdout and to file.

tech:outlev_mp (outlev_mp)
      0*/1: whether to print MP model information.

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
```

