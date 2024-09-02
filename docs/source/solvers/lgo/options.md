
# LGO Options

```ampl
ampl: option solver lgo; # change the solver
ampl: option lgo_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

Solver options obtained with `$ lgo -=`.

```
con_tol   max. constraint violation in local search; default 1e-8

fi_tol    local search merit function precision improvement target;
          default = 1e-8

flog      name of log file for function evaluations (debug option,
          default = not written)

g_maxfct  factor affecting max. merit function evals in global phase.
          The limit is often 2*g_maxfct but may be more when the starting
          point is infeasible.  Default g_maxfct = 50*(m+n+2)^2, in which
          n = _snvars (number of decision variables the solver sees)
          and m = _sncons (number of constraints the solver sees).

g_target  global search target objective function value; default -1e10

irngs     random number seed (default 0) for LGO's built-in random-number
          generator

kt_tol    local Kuhn-Tucker optimality tolerance; default 1e-8

l_maxfct  max. merit function evals in global phase; default 50*(m+n+2)^2,
          with m and n as for g_maxfct

l_target  local search target objective function value; default -1e10

lbound    lower bound imposed on variables unbounded below:
                change -Infinity <= x <= U
                to min(0,U) + lbound <= x <= U;
                default lbound = -1e4

linwarn   Whether to warn about or object to purely linear problems:
          sum of
                1 = yes (default)
                2 = abort execution if purely linear
                4 = abort execution if integer variables are present

logfile   name of log file written when outlev >= 3 (default "LGO.LOG")

maxnosuc  limit on global phase merit evals without improvement;
          default = 50*(m+n+2)^2

objno     objective number: 1 = first (default)

objrep    Whether to replace
                minimize obj: v;
          with
                minimize obj: f(x)
          when variable v appears linearly
          in exactly one constraint of the form
                s.t. c: v >= f(x);
          or
                s.t. c: v == f(x);
          Possible objrep values:
          0 = no
          1 = yes for v >= f(x)
          2 = yes for v == f(x)
          3 = yes in both cases (default)

opmode    synonym for "search" (see below)

outfile   name of file written when outlev >= 2 (default "LGO.OUT")

outlev    output level:
                0 (default) ==> no output
                1 ==> write sumfile
                2 ==> also outfile
                3 ==> also logfile

penmult   constraint penalty multiplier; default 1.0

search    search kind:
                0 = just local optimization
                1 = global branch-and-bound + local optimization
                2 = global adaptive random  + local optimization
                3 = multi-start local search (default)

sumfile   name of summary file written when outlev >= 1 (default "LGO.SUM")

timelim   time limit in seconds; default 300

timing    report I/O and solution times: 1 = stdout, 2 = stderr, 3 = both

ubound    upper bound imposed on variables unbounded above:
                change L <= x <= Infinity
                to L <= x <= max(L,0) + ubound;
                default ubound = 1e4

version   single-word phrase:  show the current version

wantsol   solution report without -AMPL: sum of
                1 ==> write .sol file
                2 ==> print primal variable values
                4 ==> print dual variable values
                8 ==> do not print solution message
```

