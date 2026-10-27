
# BARON Options

```ampl
ampl: option solver baron; # change the solver
ampl: option baron_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

Solver options obtained with `$ baron -=`.

```
absconfeastol  Absolute constraint and bound feasibility tolerance (BARON
               AbsConFeasTol, default 1e-6, >= 1e-12).

absintfeastol  Absolute integer feasibility tolerance (AbsIntFeasTol, default 1e-5).

barstats       Report detailed Baron statistics.  No value is expected.

boxtol         Boxes smaller than this are eliminated (BoxTol, default 1e-8).

brptstra       Branching point selection strategy (BrPtStra):
                0 = dynamic (default)
                1 = omega-branching
                2 = bisection
                3 = convex combination.

brvarstra      Branching variable selection strategy (BrVarStra):
                0 = dynamic (default)
                1 = largest violation
                2 = longest edge.

cutoff         Ignore solutions that are no better than this value (CutOff; default:
               no cutoff).

deltaa         Absolute tolerance used when deltaterm=1 is specified.
               Default = Infinity.

deltar         Relative tolerance used when deltaterm=1 is specified.
               Default = 1.

deltat         Used to specifiy ndeltat, which is used when deltaterm=1 is
               specified.  If deltat > 0, then ndelta = deltat.  If deltat < 0,
               then ndeltat = -deltat times the CPU time for root processing.
               If deltat = 0, then deltaterm = 0 is assumed.  Default = -100.

deltaterm      Whether to check for "insufficient progress", which is
               detected if the objective has not improved by more than
               min(deltaa, deltar*abs(objective)) after ndelta seconds.
                0 = no (default)
                1 = yes.
               See the descriptions of deltaa, deltar, deltat.

dolocal        Whether to use local search during upper bounding (DoLocal):
                0 = no
                1 = yes (default).

epsa           BARON's EpsA convergence tolerance (default 1e-6).  BARON stops if
               the current function value f satisfies abs(f - L) <= epsa,
               where L is the currently best available bound on f.

epsr           BARON's EpsR convergence tolerance (default 1e-6 in this
               driver; BARON's own default is 1e-9).  BARON stops if
               the current function value f satisfies abs(f - L) <= abs(L*epsr),
               where L is the currently best available bound on f.

filter         Allow BARON to use the FilterSD solver.  No value is expected.
               Deprecated:  use nlpsol=... instead.

firstloc       Whether to stop at the first local solution found:
                0 = no (default)
                1 = yes.

iisfind        Whether to find and return an IIS (irreducible infeasible set of
               variables and constraints) if the problem is infeasible:
                0 = no (default)
                1 = yes, using a fast heuristic
                2 = yes, using a deletion filtering algorithm
                3 = yes, using an addition filtering algorithm
                4 = yes, using an addition-deletion filtering algorithm
                5 = yes, using a depth-first search algorithm.
               IIS details are returned in suffix .iis, which assumes one of the
               values "non" for variables and constraints not in the IIS; "low"
               for variables or inequality constraint bodies whose lower bounds
               are in the IIS; "upp" for variables and inequality constraint
               bodies whose upper bounds are in the IIS, "both" for variables
               and inequality constraints whose lower and upper bounds are in
               the IIS and "fix" for equality constraints that are in the IIS.

iisint         Whether to include general integer variables in an IIS (see iisfind):
                0 = no (default)
                1 = yes.

iisorder       How to order constraints when seeking an IIS (see iisfind):
                -1 = automatic choice
                 1 = problem order (as in .nl file)
                 2 = ascending order by degree
                 3 = descending order by degree
                >= 4 = random order with seed iis_order.

isoltol        Feasible solutions closer than this are considered identical
               (ISolTol, default 1e-4).

keepsol        Keep BARON's solution files.  No value is expected.

lbttdo         Whether to do linear-feasibility-based range reduction (LBTTDo):
                0 = no
                1 = yes (default).

lpalg          LP algorithm when CPLEX is the LP solver (LPAlg):
                0 = automatic (default)
                1 = primal simplex
                2 = dual simplex
                3 = barrier.

lpsolver       Choice of LP solver, which matters mainly when there are integer
               variables:  one of cbc (default), cplex, la04, or xpress.  Cplex
               and xpress must be suitably licensed to be used.

lsolmsg        Show solution messages for lsolver.  No value is expected.

lsolver        Local nonlinear solver that Baron should call.
               The local solver should have an AMPL interface and, if needed,
               its own license.  Default:  use a builtin local solver.

maxiter        Maximum number of branch-and-reduce iterations; -1 (the default)
               means no limit; 0 forces BARON to stop after root-node processing.

maxtime        Maximum CPU seconds allowed (default 1000); -1 means no limit
               (BARON raises other non-positive values to a positive time limit).

mdo            Whether to do marginals-based range reduction (MDo):
                0 = no
                1 = yes (default).

nlpsol         Local nonlinear solvers BARON is allowed to use: sum (mod 16) of
                1 ==> IPOPT (builtin)
                2 ==> FilterSD (builtin)
                4 ==> FilterSQP (builtin)
                8 ==> lsolver (if lsolver=... is specified)
               Default 0 ==> allow all.

nodesel        Node selection strategy (NodeSel):
                0 = mixed (default)
                1 = best bound
                2 = LIFO
                3 = minimum infeasibilities.

nouter1        Number of outer approximators of convex univariate functions
               (NOuter1, default 4).

noutiter       Number of rounds of cutting-plane generation at each node
               (NOutIter, default 4).

noutpervar     Number of outer approximators per variable for convex multivariate
               functions (NOutPerVar, default 4).

numloc         Number of local searches in preprocessing (NumLoc):
                -2 = automatic (default)
                -1 = until global optimality is proven or
                     maxtime is reached
                n >= 0 = n local searches.

numsol         Number of near optimal solutions to find.
               Default = 1; values > 1 imply keepsol and cause suffix .numsol
               on the objective and problem to be returned.

objbound       Return suffixes .obj_lb and .obj_ub on the problem and objective
               with Baron's final lower and upper bounds on the objective value.
               No value is expected.

objno          objective number: 1 = first (default).

obttdo         Whether to do optimality-based range tightening (OBTTDo):
                0 = no
                1 = yes (default).

optfile        Name of BARON option file (not required).  If given, the file should
               contain name-value pairs, one per line, with the name and value
               separated by a blank, a colon, or an equal sign, possibly surrounded
               by white space.  The names and possible values are summarized in
               section 6 of the BARON user manual (baron_manual.pdf).  Empty lines
               and lines that start with # are ignored.

outgrid        Number of grid points per variable for the outer approximators of
               convex multivariate functions (OutGrid, default 20).

outlev         Whether to chatter: 0 ==> no (default), 1 ==> yes.

param          Any BARON option as Name=value, written to the OPTIONS block
               unchanged; can be repeated.  Example:  param=DeltaTerm=1.
               Option names and values: BARON manual, section "BARON options".

pdo            Number of probing problems in range reduction (PDo):
                -2 = automatic (default)
                -1 = all
                0 = none
                n > 0 = n problems.

prfreq         Report progress every prfreq nodes (default 1e6).

prloc          Whether to report local searches: 0 ==> no (default), 1 = yes.

problem        Problem name printed in logfile.

prtime         Report progress every prtime seconds (default 30).

relconfeastol  Relative constraint feasibility tolerance (RelConFeasTol, default 0,
               at most 0.1).

relintfeastol  Relative integer feasibility tolerance (RelIntFeasTol, default 0,
               at most 0.1).

scratch        Directory for temporary files; will be removed unless keepsol
               is specified.

seed           Initial seed for the random number generator. Must be
               a positive integer (default 19631963).

sumfile        Name of summary file; default = none (not written).

tdo            Whether to do nonlinear-feasibility-based range reduction (TDo):
                0 = no
                1 = yes (default).

threads        Maximum threads to use (default 1) when there are integer variables.

trace          Name of Baron "trace" file; none if not specified.

version        Single-word phrase:  show the current version.

wantdual       Whether BARON should compute dual values for the best solution
               (WantDual):
                0 = no
                1 = yes.

wantsol        solution report without -AMPL: sum of
                1 ==> write .sol file
                2 ==> print primal variable values
                4 ==> print dual variable values
                8 ==> do not print solution message
```

