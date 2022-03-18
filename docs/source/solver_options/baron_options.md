
# BARON Options

Obtained with `$ baron -=`.

```
barstats   Report detailed Baron statistics.  No is value expected.

deltaa     Absolute tolerance used when deltaterm=1 is specified.
           Default = Infinity.

deltar     Relative tolerance used when deltaterm=1 is specified.
           Default = 1.

deltat     Used to specifiy ndeltat, which is used when deltaterm=1 is
           specified.  If deltat > 0, then ndelta = deltat.  If deltat < 0,
           then ndeltat = -deltat times the CPU time for root processing.
           If deltat = 0, then deltaterm = 0 is assumed.  Default = -100.

deltaterm  Whether to check for "insufficient progress", which is
           detected if the objective has not improved by more than
           min(deltaa, deltar*abs(objective)) after ndelta seconds.
                0 = no (default)
                1 = yes.
           See the descriptions of deltaa, deltar, deltat.

epsa       BARON's EpsA convergence tolerance (default 1e-6).  BARON stops if
           the current function value f satisfies abs(f - L) <= epsa,
           where L is the currently best available bound on f.

epsr       BARON's EpsR convergence tolerance (default 1e-6).  BARON stops if
           the current function value f satisfies abs(f - L) <= abs(L*epsr),
           where L is the currently best available bound on f.

filter     Allow BARON to use the FilterSD solver.  No value is expected.
           Deprecated:  use nlpsol=... instead.

firstloc   Whether to stop at the first local solution found:
                0 = no (default)
                1 = yes.

iisfind    Whether to find and return an IIS (irreducible infeasible set of
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

iisint     Whether to include integer variables in an IIS (see iisfind):
                0 = no
                1 = yes (default).
           Binary variables are always excluded.

iisorder   How to order constraints when seeking an IIS (see iisfind):
                -1 = automatic choice
                 1 = problem order (as in .nl file)
                 2 = ascending order by degree
                 3 = descending order by degree
                >= 4 = random order with seed iis_order.

keepsol    Keep BARON's solution files.  No value is expected.

lpsolver   Choice of LP solver, which matters mainly when there are integer
           variables:  one of cbc (default), cplex, or xpress.  The last two
           must be suitably licensed to be used.

lsolmsg    Show solution messages for lsolver.  No value is expected.

lsolver    Local nonlinear solver that Baron should call.
           The local solver should have an AMPL interface and, if needed,
           its own license.  Default:  use a builtin local solver.

maxiter    Maximum number of branch-and-reduce iterations; -1 (the default)
           means no limit; 0 forces BARON to stop after root-node processing.

maxtime    Maximum CPU seconds allowed (default 1000); -1 means no limit.

nlpsol     Local nonlinear solvers BARON is allowed to use: sum (mod 16) of
                1 ==> IPOPT (builtin)
                2 ==> FilterSD (builtin)
                4 ==> FilterSQP (builtin)
                8 ==> lsolver (if lsolver=... is specified)
           Default 0 ==> allow all.

numsol     Number of near optimal solutions to find.
           Default = 1; values > 1 imply keepsol and cause suffix .numsol
           on the objective and problem to be returned.

objbound   Return suffixes .obj_lb and .obj_ub on the problem and objective
           with Baron's final lower and upper bounds on the objective value.
           No value is expected.

objno      objective number: 1 = first (default).

optfile    Name of BARON option file (not required).  If given, the file should
           contain name-value pairs, one per line, with the name and value
           separated by a blank, a colon, or an equal sign, possibly surrounded
           by white space.  The names and possible values are summarized in
           section 6 of the BARON user manual (baron_manual.pdf).  Empty lines
           and lines that start with # are ignored.

outlev     Whether to chatter: 0 ==> no (default), 1 ==> yes.

prfreq     Report progress every prfreq nodes (default 1e6).

prloc      Whether to report local searches: 0 ==> no (default), 1 = yes.

problem    Problem name printed in logfile.

prtime     Report progress every prtime seconds (default 30).

scratch    Directory for temporary files; will be removed unless keepsol
           is specified.

sumfile    Name of summary file; default = none (not written).

threads    Maximum threads to use (default 1) when there are integer variables.

trace      Name of Baron "trace" file; none if not specified.

version    Single-word phrase:  show the current version.

wantsol    solution report without -AMPL: sum of
                1 ==> write .sol file
                2 ==> print primal variable values
                4 ==> print dual variable values
                8 ==> do not print solution message


```

