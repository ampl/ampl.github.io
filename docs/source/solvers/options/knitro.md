
# KNITRO Options

```ampl
ampl: option solver knitro; # change the solver
ampl: option knitro_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

Solver options obtained with `$ knitro -=`.

```
act_lpalg                LP algorithm used in Active or SQP subproblems:
                                0 (default) = automatic choice
                                1 = primal
                                2 = dual
                                3 = barrier
act_lpdumpmps            Dump LPs to MPS files in Active or SQP algorithm
act_lpfeastol            Feasibility tolerance for LP subproblems
act_lppenalty            Controls constraint penalization in LP subproblems
act_lppresolve           Controls LP presolve in Active or SQP subproblems
act_parametric           Use parametric LP in Active or SQP algorithm
act_qpalg                QP subproblem alg used by Active or SQP algorithm
act_qppenalty            Controls constraint penalization in QP subproblems
alg                      Algorithm (0=auto, 1=direct, 2=cg, 3=active,
                         4=sqp, 5=multi)
algorithm                Synonym for alg
bar_conic_enable         Special handling of conic constraints
bar_directinterval       Frequency for trying to force direct steps
bar_feasible             Emphasize feasibility
bar_feasmodetol          Tolerance for entering stay feasible mode
bar_initmu               Initial value for barrier parameter (non-positive=auto)
bar_initpi_mpec          Initial value for barrier MPEC penalty parameter
bar_initpt               Barrier initial point strategy
bar_initshifttol         Tolerance for shifting initial point
bar_linsys               Barrier linear system form
bar_linsys_storage       Barrier linear system storage
bar_maxcorrectors        Maximum number of corrector steps
bar_maxcrossit           Maximum number of crossover iterations
bar_maxrefactor          Maximum number of KKT refactorizations allowed
bar_mpec_heuristic       Whether to enable barrier MPEC heuristic
bar_murule               Rule for updating the barrier parameter
bar_penaltycons          Apply penalty method to constraints
bar_penaltyrule          Rule for updating the penalty parameter
bar_refinement           Whether to refine barrier solution
bar_relaxcons            Whether to relax constraints
bar_slackboundpush       Amount by which slacks are pushed inside bounds
bar_switchobj            Objective for barrier switching alg
bar_switchrule           Rule for barrier switching alg
bar_watchdog             Enable watchdog heuristic for barrier algs?
bfgs_scaling             Initial scaling for BFGS/L-BFGS Hessian
blas_numthreads          Number of parallel threads for BLAS
blasoption               Which BLAS/LAPACK library to use
blasoptionlib            Name of dynamic BLAS/LAPACK library
bndrange                 Constraint/variable bound range
cg_maxit                 Maximum number of conjugate gradient iterations
cg_pmem                  Memory for incomplete Choleski
cg_precond               Preconditioning method
cg_stoptol               Stopping tolerance for CG subproblems
conic_numthreads         Number of parallel threads for conic operations
convex                   Declare the problem as convex
cplexlibname             Name of dynamic CPLEX library
cpuplatform              Target CPU platform/architecture
debug                    Debugging level (0=none, 1=problem, 2=execution)
delta                    Initial trust region radius
derivcheck               Whether to use derivative checker
derivcheck_terminate     Derivative checker type (1=error, 2=always)
derivcheck_tol           Relative tolerance for derivative checker
derivcheck_type          Derivative checker type (1=forward, 2=central)
feasible                 Enable feasible version
feasmodetol              Tolerance for entering feasible mode
feastol                  Feasibility stopping tolerance
feastol_abs              Absolute feasibility tolerance
feastolabs               Absolute feasibility tolerance
findiff_estnoise         Noise estimate for finite-difference gradients
findiff_numthreads       Number of threads for finite-difference gradients
findiff_relstepsize      Relative stepsize for finite-difference gradients
findiff_terminate        Termination for finite-difference gradients
fstopval                 Stop based on obj. function value
ftol                     Stop based on small change in obj. function
ftol_iters               Stop based on small change in obj. function
gradopt                  Gradient computation method
hessopt                  Hessian computation method
honorbnds                Enforce satisfaction of the bounds
infeastol                Infeasibility stopping tolerance
infeastol_iters          Stop based on small change in feas. error
initpenalty              Initial merit function penalty value
leastsquares             Solve as a least-squares model
linesearch               Which linesearch method to use
linesearch_maxtrials     Maximum number of linesearch trial points
linsolver                Which linear solver to use
linsolver_inexact        Use inexact solver (experimental option)
linsolver_inexacttol     Inexact solver tolerance (experimental option)
linsolver_maxitref       Max iterative refinement steps
linsolver_numthreads     Number of parallel threads for linear solver
linsolver_ooc            Use out-of-core option?
linsolver_pivottol       Initial pivot tolerance for linear solvers
lmsize                   Number of limited-memory pairs stored for LBFGS
lpsolver                 Solver used with 'act_lpalg'.  Should be 'internal',
                         'cplex', or 'xpress'.  Default = 'internal'; cplex or
                         xpress must be suitably licensed.  For lpsolver=...
                         to be useful, alg=2, 3, or 4 may also be needed.
                         Implicitly sets omitted keywords act_lpsolve and,
                         if appropriate, cplex_libname ot xpress_libname.
ma_maxtime_cpu           Maximum CPU time when 'alg=multi', in seconds
ma_maxtime_real          Maximum real time when 'alg=multi', in seconds
ma_outsub                Enable subproblem output when 'alg=multi'
ma_terminate             Termination condition when option 'alg=multi'
maxcgit                  deprecated, use 'cg_maxit'
maxcrossit               deprecated, use 'bar_maxcrossit'
maxfevals                Maximum number of function evaluations
maxit                    Maximum number of iterations
maxtime_cpu              Maximum CPU time in seconds, per start point
maxtime_real             Maximum real time in seconds, per start point
mip_branchrule           MIP branching rule
mip_clique               Add clique cuts (0=none, 1=root, 2=tree, 3=root+tree)
mip_cutfactor            Limit on the number of cuts allowed in node subproblem (maximum number of cuts is mip_cutfactor times number of constraints in model)
mip_cutoff               MIP objective cutoff value
mip_cutting_plane        When to perform cutting plane procedure
mip_debug                MIP debugging level (0=none, 1=all)
mip_gub_branch           Branch on GUBs (0=no, 1=yes)
mip_heuristic            MIP heuristic search (deprecated, use mip_heuristic_strategy)
mip_heuristic_diving     MIP diving heuristic
mip_heuristic_feaspump   MIP feasibility pump heuristic
mip_heuristic_lns        MIP LNS heuristic
mip_heuristic_maxit      MIP heuristic iteration limit
mip_heuristic_misqp      MIP MISQP heuristic
mip_heuristic_mpec       MIP MPEC heuristic
mip_heuristic_strategy   MIP heuristic strategy
mip_heuristic_terminate  MIP heuristic termination
mip_implications         Add logical implications (0=no, 1=yes)
mip_integer_tol          Threshold for deciding integrality
mip_integral_gap_abs     deprecated, use 'mip_opt_gap_abs'
mip_integral_gap_rel     deprecated, use 'mip_opt_gap_rel'
mip_intvar_strategy      Treatment of integer variables
mip_knapsack             Add knapsack cuts (0=none, 1=ineqs, 2=lifted, 3=all)
mip_liftproject          Add lift and project cuts (0=none, 1=root)
mip_lpalg                LP subproblem algorithm
mip_maxnodes             Maximum nodes explored
mip_maxsepcons           Maximum constraints to consider for the cut separation
mip_maxsolves            Maximum subproblem solves
mip_maxtime_cpu          Maximum CPU time in seconds for MIP
mip_maxtime_real         Maximum real in seconds time for MIP
mip_method               MIP method (0=auto, 1=BB, 2=HQG, 3=MISQP)
mip_mir                  Add mixed integer rounding cuts
mip_multistart           Enable MIP multistart
mip_nodealg              Standard node relaxation algorithm
mip_numthreads           Number of threads for MIP
mip_opt_gap_abs          Absolute optimality gap stop tolerance
mip_opt_gap_rel          Relative optimality gap stop tolerance
mip_outinterval          MIP output interval
mip_outlevel             MIP output level
mip_outsub               Enable MIP subproblem output
mip_pseudoinit           Pseudo-cost initialization
mip_relaxable            Are integer variables relaxable?
mip_restart              Enable MIP restart
mip_rootalg              Root node relaxation algorithm
mip_rounding             MIP rounding rule
mip_selectdir            MIP node selection direction
mip_selectrule           MIP node selection rule
mip_skipfactor           MIP number of nodes to skip for the next cut separation round
mip_strong_candlim       Strong branching candidate limit
mip_strong_level         Strong branching tree level limit
mip_strong_maxit         Strong branching iteration limit
mip_terminate            Termination condition for MIP
mip_zerohalf             Add zero half cuts (0=no, 1=root, 2=tree, 3=all)
ms_deterministic         Use deterministic multistart
ms_enable                Enable multistart
ms_maxbndrange           Maximum unbounded variable range for multistart
ms_maxsolves             Maximum Knitro solves for multistart
ms_maxtime_cpu           Maximum CPU time for multistart, in seconds
ms_maxtime_real          Maximum real time for multistart, in seconds
ms_num_to_save           Feasible points to save from multistart
ms_numthreads            Number of parallel threads for multi-start
ms_outsub                Enable subproblem output for parallel multistart
ms_savetol               Tol for feasible points being equal
ms_seed                  Seed for multistart random generator
ms_startptrange          Maximum variable range for multistart
ms_terminate             Termination condition for multistart
multistart               Enable multistart
ncvx_qcqp_init           Initialization strategy for nonconvex QCQPs
newpoint                 Use newpoint feature
numthreads               Number of parallel threads
objno                    objective number: 0 = none, 1 = first (default),
                           2 = second (if _nobjs > 1), etc.
objrange                 Objective range
objrep                   Whether to replace
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
                         1 = yes for v >= f(x) (default)
                         2 = yes for v == f(x)
                         3 = yes in both cases
optionsfile              Name/location of Knitro options file if provided
opttol                   Optimality stopping tolerance
opttol_abs               Absolute optimality tolerance
opttolabs                Absolute optimality tolerance
out_csvinfo              Create csv info file
out_csvname              Name for csv info file
out_hints                Print hints for parameter settings
out_jsoninfo             Create json info file
out_jsonname             Name for json info file
outappend                Append to output files (0=no, 1=yes)
outdir                   Directory for output files
outlev                   Control printing level
outmode                  Where to direct output (0=screen, 1=file, 2=both)
outname                  Name for output file
par_blasnumthreads       Number of parallel threads for BLAS
par_conicnumthreads      Number of parallel threads for conic operations
par_lsnumthreads         Number of parallel threads for linear solver
par_msnumthreads         Number of parallel threads for multi-start
par_numthreads           Number of parallel threads
pivot                    deprecated, use 'linsolver_pivottol'
pre_improvecoefficients  Improve Coefficinets
pre_redundancylevel      Constraint redundancy detection level
presolve                 Enable Knitro presolver
presolve_dbg             Knitro presolver debugging level
presolve_initpt          Knitro presolver initial point handling
presolve_level           Knitro presolver level
presolve_passes          Knitro presolver pass limit
presolve_tol             Knitro presolver tolerance
presolveop_tighten       Knitro presolve tightening operations
qpcheck                  whether to check for a QP: deprecated
relax                    whether to ignore integrality: 0 (default) = no, 1 = yes
restarts                 Maximum number of restarts allowed
restarts_maxit           Maximum number of iterations before restarting
scale                    Scaling option
soc                      Second order correction options
storequadcoefs           Store quadratic coefficients when solving QCQPs
strat_warm_start         Enable warm-start strategy?
threads                  Number of parallel threads
timing                   Whether to report problem I/O and solve times:
                         0 (default) = no
                         1 = yes, on stdout
                         2 = yes, on stderr
                         3 = yes, on both stdout and stderr
tuner                    Enables Knitro Tuner
tuner_maxtime_cpu        Maximum CPU time when 'tuner=on', in seconds
tuner_maxtime_real       Maximum real time when 'tuner=on', in seconds
tuner_optionsfile        Name/location of Tuner options file if provided
tuner_outsub             Enable subproblem output when 'tuner=on'
tuner_terminate          Termination condition when 'tuner=on'
version                  Report software version
wantsol                  Solution report without -AMPL: sum of
                         1 ==> write .sol file
                         2 ==> 1 ==> write .sol file
                         4 ==> print dual variable values
                         8 ==> do not print solution message
xpresslibname            Name of dynamic Xpress library
xtol                     Stepsize stopping tolerance
xtol_iters               Stop based on small change in variables

```

