
# RAPOSa Options

```ampl
ampl: option solver raposa; # change the solver
ampl: option raposa_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

Solver options obtained with `$ raposa -=`.

```
V                   Print the version of RAPOSa.
                    
boundtightening     Type of bound tightening used (if the problem has integer
                    variables, 'INT' prefix means that the OBBT solves
                    the mixed-integer relaxation aswell):
                        NoBT ==> Donot perform bound tightening
                        OBBT ==> Perform OBBT at root node
                        FBBT ==> Perform FBBT at each node
                        OBBT+FBBT ==> Perform OBBT atrootnode and FBBT at each node
                        SOCPOBBT ==> Perform SOCPOBBT at root node
                        SOCPOBBT+FBBT ==> Perform SOCP OBBT at root node and FBBT
                            at each node
                        SDPOBBT ==> Perform SDP OBBT at root node
                        SDPOBBT+FBBT ==> Perform SDP OBBT at root node and FBBT
                            at each node.
                    (default: OBBT+FBBT)

branchingconvex     Strategy to choose the branching point. The following
                    convex combination will be the branching value, where t is 
                    the value of this option, opt is the optimal value and
                    middle is the middle point of the interval: (1-t)*opt + t*middle
                    (default: 0.25). Possible values: [0,1].
                    
branchingrule       Branching rule (default dual):
                        max ==> Use maximums of RLT violations
                        sum ==> Use sums of RLT violations
                        coeffs ==> Weigh RLT violations with the coefficients of the problem
                        dual ==> Weigh RLT violations with the dual values of the constraints
                        range ==> Weigh RLT violations with the range of the variables
                        density ==> Weigh RLT violations with the density of the variables
                       
branchingtol        Tolerance for branching criterion (default: 0.0001).
                    Possible values: [0,inf].

condnumber          Print a warning if the condition number of a linear problem is
                    greater than this value (default: 0 [do not print]).
                    Possible values: [0,inf].

feastol             Feasibility tolerance (default: 0.0001). Possible values: [0,inf].

gurobifeastol       Feasibility tolerance for gurobi when solving the linear relaxations
                    (default: 1e-6). Possible values: [0,inf].

gurobithreads       Number of threads gurobi will use (only for linsolver=gurobi)
                    (default: 0 [automatic]). Possible values: [0,inf].

help                Print the help.

inls                Frecuency to call the mixed-integer non linear solver:
                        0 ==> Do not call the non linear solver
                        negative number t ==> Call the solver every 2^(-t) nodes
                        positive number t ==> Call the solver every tseconds (default: 0)
                    Possible values: [-inf,inf].

inlsopts            String with the options for the mixed-integer non linear solver.

branchingtol        Tolerance for branching criterion (default: 0.0001).

intnonlinsolver     Mixed-integer nonlinear programming solver (the user needs
                    to have the corresponding license and the corresponding
                    executable of the solver in the path, except for bonmin
                    which is freely available) (default: bonmin).
                    Possible values: bonmin, knitro.

linsolver           Linear programming solver (default: gurobi if the user
                    has a license, googleor-glop otherwise). Possible values:
                    gurobi, googleor-clp, googleor-glop, googleor-gurobi, 
                    googleor-cplex, googleor-xpress, googleor-glpk, googleor-pdlp.

lowerbound_threshold   If the lowerbound is greater than this threshold,
                       RAPOSa will stop (default: inf). Possible values: [-inf,inf].

maxiter             Limit of iterations (default: inf). Possible values: [1,inf].

maxtime             Time limit (in seconds) (default: 300). Possible values: (0,inf].

maxtime_intnonlinsolver    Time limit (in seconds) for mixed-integer non linear
                           solver (default: inf). Possible values: (0,inf].

maxtime_nonlinsolver       Time limit (in seconds) for non linear solver (not supported
                           for minos) (default: inf).Possible values: (0,inf].

milpsolver          Mixed-integer linear programming solver (default: gurobi if the user
                    has a license, googleor-cbc otherwise). Possible values: gurobi, googleor-cbc,
                    googleor-scip, googleor-gurobi, googleor-cplex, googleor-xpress, googleor-glpk.

nls                 Frecuency to call the non linear solver (default: -1.5):
                        0 ==> Do not call the non linear solver
                        negative number t ==> Call the solver every 2^(-t) nodes
                        positive number t ==> Call the solver every t seconds.

nlsopts             String with the options for the non linear solver.

nonlinsolver        Nonlinear programmingsolver (the user needs to have the
                    corresponding license and the corresponding executable ofthe solver in the path,
                    except for ipopt which is freely available) (default: ipopt).
                    Possible values: ipopt, knitro, minos, conopt.

outlev              0 ==> Only display solution
                    1 ==> Display real time reporting (default: 0).

output              Name for the output file in json format (default: do not create 
                    an output file).

repfreq             Display report frequency (in seconds) (default: 30).
                    Possible values: [0,inf].

sdp                 Add SDP constraints to relaxations.

sdpcuts             Add SDP-based linear cuts to the linear relaxations.

sdpsolver           SDP solver (default: mosek if the user has a license).
                    Possible values: mosek.
               
socp                Add SOCP constraints to relaxations.

socpsolver          Second-order cone programming solver (default: gurobi if the user
                    has a license, mosek otherwise (it also needs a license)).
                    Possible values: gurobi, mosek.
                    tolabs *double*:Absolute convergence tolerance (default: 0.001).
                    Possible values: [0,inf].

tolrel              Relative convergence tolerance (default: 0.001). Possible values: [0,inf].

upperbound          Initial upper bound (default: inf). Possible values: [-inf,inf].

upperbound_threshold    If the upperbound is lower than this threshold, RAPOSa will stop
                        (default: -inf). Possible values: [-inf,inf].

varbound            Bounds for all unbounded variables. Given a value v, lower bound
                    will be -v and upper bound will be v for each unbounded variable
                    (unstable and under development) (default: 100). Possible values: [0,inf].

varboundcons        Add products of bound factors and constraints:
                        0 ==> Do not add anything
                        1 ==> Add products prioritizing more in common variables
                        2 ==> Add products prioritizing less in common variables (default: 2).

wantsol             Solution report for AMPL: sum of
                        1 ==> write .sol file
                        2 ==> print primal variable values
                        4 ==> print dual variable values
                        8 ==> do not print solution message (default: 0 [do not print anything]).
                    Possible values: [0,8].

warmstart           0 ==> Do not use warmstart in linear solver
                    1 ==> Use basis warmstart in linear solver (default: 1)
                    2 ==> Use solution warmstart in linear solver
                    3 ==> Use basis and solution warmstart in linear solver (only for linsolver=gurobi)
```







