
# Lindo Global Options

```ampl
ampl: option solver lindoglobal; # change the solver
ampl: option lindoglobal_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

Solver options obtained with `$ lindoglobal -=`.

```
bbsrchmd        Node selection in the global branch-and-bound
		(GOP_BBSRCHMD): 0 = depth first, 1 = worst bound (default).
bndlim          Maximal magnitude of variable bounds used in the
		convexification (GOP_BNDLIM, default 1e10).
boxtol          Minimal width of a variable interval allowed to branch on
		(GOP_BOXTOL, default 1e-6).
branchlimit     Limit on the number of branches in the global
		branch-and-bound (GOP_BRANCH_LIMIT, default -1 = no limit).
branchmd        Direction to branch first on a variable (GOP_BRANCHMD,
		0..5, default 5).
cutoff          Stop when the objective is proven worse than this value
		(SOLVER_CUTOFFVAL; default: no cutoff).
decomppt        Branching point selection (GOP_DECOMPPTMD): 0 = midpoint,
		1 = local or convex minimum (default).
deltatol        Delta tolerance in the convexification (GOP_DELTATOL,
		default 1e-7).
epsa            Absolute optimality tolerance for accepting a new incumbent
		(GOP_ABSOPTTOL, default 1e-6).
epsr            Relative optimality tolerance for accepting a new incumbent
		(GOP_RELOPTTOL, default 1e-5).
feastol         Primal feasibility tolerance of the continuous solvers
		(SOLVER_FEASTOL, default 1e-7).
heumode         Global heuristic mode (GOP_HEU_MODE): 0 = none (default),
		1 = simple heuristic.
itrlim          Total iteration limit (simplex + barrier + NLP) over all
		branches (GOP_ITRLIM, default -1 = no limit).
iusol           0/1: whether a basic solution is computed for an infeasible
		model (SOLVER_IUSOL, default 0).
lsolbranlim     Number of branches before a new nonlinear solution is
		required (GOP_LSOLBRANLIM, default -1 = no limit).
maxlocalsearch  Maximum number of local searches of the nonlinear solver
		(NLP_MAXLOCALSEARCH, default 5).
maxtime         Maximum CPU seconds allowed (GOP_TIMLIM; default -1, means no limit).
maxwidmd        0/1: whether the maximum-width criterion (widtol) is used
		(GOP_MAXWIDMD, default 0).
nlpsolver       Type of nonlinear solver (NLP_SOLVER, default 7;
		9 = multistart; see the LINDO API manual).
optchkmd        Optimality certificate (GOP_OPTCHKMD): 0 = absolute,
		1 = relative, 2 = either (default).
optmode         Search mode (GOP_OPT_MODE): 0 = feasibility,
		1 = optimality (default), 2 = unboundedness.
opttol          Dual feasibility (optimality) tolerance of the continuous
		solvers (SOLVER_OPTTOL, default 1e-7).
outlev          Whether to chatter: 0 ==> no(default), 1 ==> yes.
param           Any LINDO parameter as LS_IPARAM_NAME=value or
		LS_DPARAM_NAME=value, e.g. param=LS_IPARAM_GOP_PRINTLEVEL=1;
		can be repeated.  Names: LINDO API manual.
paramfile       Name of a LINDO parameter file to read (LSreadModelParameter).
postlevel       Postsolve level bits (GOP_POSTLEVEL, default 6):
		+2 = apply best-bound retrieval, +4 = reoptimize variable bounds.
prelevel        Presolve level bits (GOP_PRELEVEL, default 30): +2 = initial
		local optimization, +4 = linear propagation, +8 = recursive
		linear, +16 = recursive nonlinear propagation.
quadmd          Exploit quadratic features (GOP_QUADMD): -1 = solver decides
		(default), 0 = no, 1 = yes.
sollim          Limit on the number of integer solutions in the global
		branch-and-bound (GOP_SOLLIM, default -1 = no limit).
threadingmode   Threading mode for solvers with multithreading support:
		   -1 = solver decides (default)
		    0 = try parallel mode, if not available try concurrent mode
		    1 = force parallel mode
		    2 = try concurrent mode, if not available try parallel mode
		    3 = force concurrent mode.
threads         Number of threads to be used (default -1, uses solver default).
usebndlim       When bndlim applies (GOP_USEBNDLIM): 0 = never, 1 = from
		the start, 2 = after the initial local optimization (default).
wantsol         Solution report without -AMPL: sum of
		1 ==> write .sol file
		2 ==> print primal variable values
		4 ==> print dual variable values
		8 ==> do not print solution message
```

