
# KNITRO Options

```ampl
ampl: option solver knitro; # change the solver
ampl: option knitro_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

Solver options obtained with `$ knitro -=`.

```
act_lpalg                            LP algorithm for subproblems in active-set/SQP algorithms.
                                    0 (default): Use the default algorithm for the chosen LP solver.
                                    1 (primal): Use a primal simplex algorithm.
                                    2 (dual): Use a dual simplex algorithm.
                                    3 (barrier): Use a barrier/interior-point algorithm.
act_lpdumpmps                        Dump LP subproblems to MPS files in active-set algorithm.
                                    0 (no): Dump is disabled
                                    1 (yes): Dump is enabled
act_lpfeastol                        Feasibility tolerance for LP subproblems in Active or SQP algorithms.
act_lppenalty                        Constraint penalization for LP subproblems.
                                    1 (all): Penalize all constraints.
                                    2 (nonlinear): Penalize only nonlinear constraints.
                                    3 (dynamic): Dynamically choose which constraints to penalize.
act_lppresolve                       Controls LP presolve for subproblems in active-set/SQP algorithms.
                                    0 (off): Presolve turned off for LP subproblems.
                                    1 (on): Presolve turned on for LP subproblems.
act_lpsolver                         Which LP solver to use in the Active or SQP algorithm.
                                    1 (internal): Use internal LP solver
                                    2 (cplex): CPLEX (if user has a valid license)
                                    3 (xpress): XPRESS (if user has a valid license)
act_parametric                       Use parametric approach in active-set algorithm.
                                    0 (no): Never
                                    1 (maybe): Use selectively
                                    2 (yes): Always use parametric approach
act_qpalg                            Which algorithm to use for QP subproblem solves in Active or SQP algorithms.
                                    0 (auto): Let Knitro choose the algorithm
                                    1 (direct): Use Interior (barrier) Direct algorithm
                                    2 (cg): Use Interior (barrier) CG algorithm
                                    3 (active): Use Active Set SLQP algorithm
act_qppenalty                        Constraint penalization for QP subproblems.
                                    -1 (auto): Let Knitro automatically decide.
                                    0 (none): Do not penalize constraints in QP subproblems.
                                    1 (all): Penalize all constraints in QP subproblems.
alg                                  Deprecated (use 'algorithm' option)
algorithm                            Which algorithm to use.
                                    0 (auto): Let Knitro choose the algorithm
                                    1 (direct): Use Interior (barrier) Direct algorithm
                                    2 (cg): Use Interior (barrier) CG algorithm
                                    3 (active): Use Active Set SLQP algorithm
                                    4 (sqp): Use Active Set SQP algorithm
                                    5 (multi): Run multiple algorithms (perhaps in parallel)
bar_conic_enable                     Enable specialized algorithm for conic constraints.
                                    -1 (auto): Let Knitro automatically choose the strategy.
                                    0 (none): Do not apply any special treatment for conic constraints.
                                    1 (soc): Apply special treatments for any Second Order Cone (SOC) constraints identified in the model.
bar_directinterval                   When using the Interior/Direct algorithm, this parameter controls the maximum number of consecutive CG steps before trying to force the algorithm to take a direct step again. (negative implies auto; only used for alg=1).
bar_feasible                         Whether feasibility is given special emphasis.
                                    0 (no): No emphasis on feasibility
                                    1 (stay): Iterates must honor inequalities
                                    2 (get): Emphasize first getting feasible before optimizing
                                    3 (get_stay): Implement both options 1 and 2 above
bar_feasmodetol                      Specifies the tolerance for entering the stay feasible mode (only valid when bar_feasible = stay or bar_feasible = get_stay).
bar_globalize                        The globalization strategy used for the interior-point algorithm.
                                    0 (none): Do not apply any globalization strategy
                                    1 (kkt): Apply a globalization strategy based on decreasing the KKT error
                                    2 (filter): Apply a globalization strategy using a filter based on the objective and constraint violation
bar_initmu                           Initial value for the barrier parameter (non-positive implies auto).
bar_initpi_mpec                      Initial value for the barrier MPEC penalty parameter.
bar_initpt                           Strategy for setting initial x, lambda and slacks with barrier algorithms. This option only affects the initial x value when not provided by user.
                                    0 (auto): Let Knitro choose the strategy
                                    1 (convex): Initial point strategy 1 (mainly for convex problems)
                                    2 (nearbnd): Initial point strategy staying closer to bounds
                                    3 (central): More central initial point strategy
bar_initshiftol                      Deprecated (use 'bar_initshifttol' option)
bar_initshifttol                     Tolerance for enabling shifting of the initial point.
bar_linsys                           Linear system form for barrier algorithms.
                                    -1 (auto): Automatically determine
                                    0 (full): Full augmented system
                                    1 (slacks): Eliminate slacks
                                    2 (bounds): Also eliminate bounds
                                    3 (ineqs): Also eliminate inequalities
bar_linsys_storage                   Linear system storage for barrier algorithms.
                                    -1 (auto): Automatically determine
                                    1 (lowmem): Use one storage location for multiple systems
                                    2 (normal): Store systems separately
bar_maxcorrectors                    Maximum number of correctors allowed when computing primal-dual barrier step (negative implies auto).
bar_maxcrossit                       Maximum number of crossover iterations to allow for barrier algorithms.
bar_maxmu                            Maximum allowed barrier parameter value for the interior-point algorithm.
bar_maxrefactor                      Maximum number of refactorizations of the KKT system per iteration of the Interior Direct algorithm before reverting to a CG step. (negative implies auto; only used for alg=1).
bar_mpec_heuristic                   Barrier heuristic for MPEC models.
                                    0 (no): No mpec heuristic enabled
                                    1 (yes): Mpec heuristic is enabled
bar_murule                           Which barrier parameter update strategy.
                                    0 (auto): Let Knitro choose the strategy
                                    1 (monotone): Monotonically decrease the barrier parameter. Available for both barrier algorithms.
                                    2 (adaptive): Use an adaptive rule based on the complementarity gap to determine the value of the barrier parameter. Available for both barrier algorithms.
                                    3 (probing): Use a probing (affine-scaling) step to dynamically determine the barrier parameter. Available only for the Interior/Direct algorithm.
                                    4 (dampmpc): Use a Mehrotra predictor-corrector type rule to determine the barrier parameter, with safeguards on the corrector step. Available only for the Interior/Direct algorithm.
                                    5 (fullmpc): Use a Mehrotra predictor-corrector type rule to determine the barrier parameter, without safeguards on the corrector step. Available only for the Interior/Direct algorithm.
                                    6 (quality): Minimize a quality function at each iteration to determine the barrier parameter. Available only for the Interior/Direct algorithm.
bar_penaltycons                      Whether or not to penalize constraints in the barrier algorithms.
                                    -1 (auto): Let Knitro choose the strategy
                                    0 (none): Do not apply penalty approach to any constraints
                                    2 (all): Apply a penalty approach to all general constraints
                                    3 (equalities): Apply a penalty approach to equality constraints only
bar_penaltyrule                      Which penalty parameter update strategy for barrier algorithms.
                                    0 (auto): Let Knitro choose the strategy
                                    1 (single): Use single penalty parameter approach
                                    2 (flex): Use more tolerant flexible strategy
bar_refinement                       Whether to try to refine the barrier solution for better precision.
                                    0 (no): Do not refine the barrier solution
                                    1 (yes): Try to refine the barrier solution
bar_relaxcons                        Whether to relax the general constraints for barrier algorithms.
                                    0 (none): Do not relax any constraints
                                    1 (eqs): Relax only equality constraints
                                    2 (ineqs): Relax only inequality constraints
                                    3 (all): Relax all general constraints
bar_slackboundpush                   Amount by which barrier slacks are initially pushed interior (non-positive implies auto).
bar_switchobj                        Objective form when switching to feasibility phase.
                                    0 (none): No objective
                                    1 (scalarprox): Proximal point objective with scalar weighting
                                    2 (diagprox): Proximal point objective with diagonal weighting
bar_switchrule                       Switching rule strategy for barrier algorithms that controls switching between optimality and feasibility phases.
                                    -1 (auto): Let Knitro choose the strategy
                                    0 (never): Never switch
                                    2 (moderate): Allow moderate switching
                                    3 (aggressive): More aggressive switching
bar_watchdog                         Whether to activate watchdog heuristic for barrier algorithms.
                                    0 (no): No watchdog heuristic
                                    1 (yes): Allow watchdog heuristic to be used
bfgs_scaling                         Initial scaling used for BFGS/L-BFGS Hessian.
                                    0 (dynamic): Dynamically determine
                                    1 (invhess): Approximate scale of the inverse Hessian
                                    2 (hess): Approximate the scale of the Hessian
blas_numthreads                      Number of threads to use in parallel BLAS. choose any positive integer, or 0 = determine automatically based on numthreads
blasoption                           Which BLAS/LAPACK library to use.  Intel MKL library is only available on some platforms; see the User Manual for details.
                                    -1 (auto): Automatically determine based on platform
                                    0 (knitro): Use Knitro version of netlib functions
                                    1 (intel): Use Intel MKL functions
                                    2 (dynamic): Use dynamic library of functions
                                    3 (blis): Use BLIS functions
                                    4 (apple): Use Apple Accelerate functions
blasoptionlib                        Name of the dynamic BLAS/LAPACK function library if using blasoption=2.
bndrange                             Valid range for constraint or variable bounds.
cg_maxit                             Maximum allowable CG iterations per trial step (-1: auto; 0: max limit based on problem size).
cg_pmem                              Amount of memory used by incomplete Choleski preconditioner.
cg_precond                           Whether or not to use incomplete Choleski preconditioner.
                                    0 (no): Not applied
                                    1 (chol): Preconditioner is applied
cg_stoptol                           Stopping tolerance for CG subproblems.
concurrent_evals                     Whether to allow simultaneous evaluations in parallel.
                                    0 (no): Only one thread can perform an evaluation at a time
                                    1 (yes): Allow multi-threaded simultaneous evaluations
conic_numthreads                     Number of threads to do conic operations in parallel. choose any positive integer, or 0 = determine automatically based on numthreads
convex                               Declare the problem as convex.
                                    -1 (auto): Knitro will try to determine this automatically, but may only be able to do so for simple model forms such as QPs or QCQPs.
                                    0 (no): Declare problem as non-convex
                                    1 (yes): Declare problem as convex
cplexlibname                         Name of the CPLEX library if using act_lpsolver=cplex
cpuplatform                          target CPU platform/architecture.
                                    -1 (auto): Determine automatically
                                    1 (compatible): Aim for more compatible performance across architectures
                                    2 (sse2): SSE2
                                    3 (avx): AVX
                                    4 (avx2): AVX-2
                                    5 (avx512): AVX-512 (experimental)
datacheck                            Whether to perform extra data checks on the model.
                                    0 (no): No extra data checks
                                    1 (yes): Perform extra data checks
debug                                Specifies debugging level of output.  Debugging output is intended for Artelys developers.  Debugging mode may impact performance and is NOT recommended for production operation.
                                    0 (none): No extra debugging
                                    1 (problem): Help debug solution of the problem
                                    2 (execution): Help debug execution of the solver
debugoptionsname                     Internal parameter
delta                                Initial trust region radius scaling factor, used to determine the initial trust region size.
derivcheck                           Whether to perform a derivative check on the model.
                                    0 (none): No derivative check
                                    1 (first): Check first derivatives
                                    2 (second): Check second derivatives
                                    3 (all): Check all derivatives
derivcheck_terminate                 Termination for derivative check.
                                    1 (error): Stop when there is an error detected
                                    2 (always): Always stop after the derivative check
derivcheck_tol                       Specifies the relative tolerance used for the derivative check.
derivcheck_type                      Type of derivative check.
                                    1 (forward): Check using forward finite-differences
                                    2 (central): Check using central finite-differences
eval_cost                            Specifies the relative cost of performing callback evaluations.
                                    0 (unspecified): Evaluation cost is not specified
                                    1 (inexpensive): Evaluation cost is relatively inexpensive
                                    2 (expensive): Evaluation cost is relatively expensive
eval_fcga                            Enable evaluating gradients with functions in one callback.
                                    0 (no): Gradients are not evaluated in the function evaluation callback
                                    1 (yes): Gradients are evaluated in the function evaluation callback
feasible                             Deprecated (use 'bar_feasible' option)
feasmodetol                          Deprecated (use 'bar_feasmodetol' option)
feastol                              Specifies the final relative stopping tolerance for the feasibility error. Smaller values of feastol result in a higher degree of accuracy in the solution with respect to feasibility.
feastol_abs                          Specifies the final absolute stopping tolerance for the feasibility error. Smaller values of feastol_abs result in a higher degree of accuracy in the solution with respect to feasibility. Default value is  1e-3 for NLP, 1e-6 for MINLP.
feastolabs                           Deprecated (use 'feastol_abs' option)
findiff_estnoise                     Noise estimation when using finite-difference gradients.
                                    0 (no): No estimation of noise performed
                                    1 (yes): Estimate the noise and perhaps use it to determine a finite-difference steplength
                                    2 (withcurv): Estimate a curvature factor as well as the noise and perhaps use it to determine a finite-difference steplength
findiff_numthreads                   Number of threads to use in finite-differencing. choose any positive integer, or 0 = determine automatically based on numthreads
findiff_relstepsize                  Relative stepsize for finite-difference gradients.
findiff_terminate                    Termination method when using finite-difference gradients.
                                    0 (none): No special termination
                                    1 (errest): Terminate on gradient error estimates
fstopval                             Value used for objective function value based termination.
ftol                                 Tolerance for stopping on small changes to the objective.
ftol_iters                           Consecutive iterations for stopping on small changes to the objective.
gradopt                              How to compute/approximate the gradient of the objective and constraint functions.
                                    1 (exact): User supplies exact first derivatives
                                    2 (forward): Gradients computed by internal forward finite differences
                                    3 (central): Gradients computed by internal central finite differences
                                    4 (user_forward): Gradients computed by user-provided forward finite differences
                                    5 (user_central): Gradients computed by user-provided central finite differences
hesevalthreads                       Number of threads for hessian evaluations
hessetupthreads                      Number of threads for hessian setup
hessian_no_f                         Whether to allow computing the Hessian of the Lagrangian without objective component.
                                    0 (forbid): Not allowed
                                    1 (allow): User can provide this version of the Hessian if requested
hessopt                              How to compute/approximate the Hessian of the Lagrangian.
                                    0 (auto): Determined automatically by Knitro
                                    1 (exact): User supplies exact second derivatives
                                    2 (bfgs): Knitro computes a dense quasi-Newton BFGS Hessian
                                    3 (sr1): Knitro computes a dense quasi-Newton SR1 Hessian
                                    4 (product_findiff): Knitro computes Hessian-vector products by finite differences
                                    5 (product): User supplies exact Hessian-vector products
                                    6 (lbfgs): Knitro computes a limited-memory quasi-Newton BFGS Hessian
hesthreads                           Number of threads for hessian setup and evaluations
honorbnds                            Whether to enforce satisfaction of simple bounds at all iterations.
                                    -1 (auto): Setting determined automatically by Knitro
                                    0 (no): Allow iterations to violate the bounds
                                    1 (always): Enforce bounds satisfaction of all iterates
                                    2 (initpt): Enforce bounds satisfaction of initial point
infeastol                            Specifies relative stopping tolerance used to declare infeasibility.
infeastol_iters                      Consecutive iterations for stopping on small changes to the feasibility error.
initpenalty                          Initial value for the merit function penalty parameter.
initpt_strategy                      Specifies the initial point strategy used for the continuous algorithms.
                                    -1 (auto): Automatic initial point strategy
                                    1 (basic): Try basic initial point strategy
                                    2 (advanced): Try more advanced initial point strategy
initptfile                           Name for the file from which to read the initial point (default 'NULL', no initial point read from file).
leastsquares                         Solve as a least-squares model
linesearch                           Which linesearch method to use.
                                    0 (auto): Let Knitro choose the linesearch method
                                    1 (backtrack): Backtracking linesearch
                                    2 (interpolate): Interpolation based linesearch
                                    3 (weakwolfe): Weak Wolfe linesearch
linesearch_maxtrials                 Maximum allowable number of trial values during the linesearch of the Interior Direct or SQP algorithm.
linsolver                            Which linear system solver to use.
                                    0 (auto): Let Knitro choose the solver
                                    1 (internal): Use internal solver provided with Knitro
                                    2 (hybrid): Use a mixture of linear solvers depending on the linear systems
                                    3 (qr): Use dense QR solver always (only for small problems)
                                    4 (ma27): Use sparse HSL solver ma27 always
                                    5 (ma57): Use sparse HSL solver ma57 always
                                    6 (mklpardiso): Use sparse Intel MKL Pardiso solver always
                                    7 (ma97): Use parallel, deterministic HSL ma97 solver
                                    8 (ma86): Use parallel, non-deterministic HSL ma86 solver
linsolver_inexact                    Internal parameter
linsolver_inexacttol                 Internal parameter
linsolver_maxitref                   Maximum number of iterative refinement steps for the linear solver.
linsolver_nodeamalg                  Controls node amalgamation for MA57, MA86 and MA97 linear solvers.
linsolver_numthreads                 Number of threads to use in parallel linear solver. choose any positive integer, or 0 = determine automatically based on numthreads
linsolver_ooc                        Whether to use out-of-core version of linsolver=mklpardiso.
                                    0 (no): Always use in-core version
                                    1 (maybe): Will use out-of-core version beyond a certain size
                                    2 (yes): Always use out-of-core version
linsolver_ordering                   Controls ordering method for linear solvers.
                                    -1 (auto): Automatically determine ordering procedure
                                    0 (best): Choose the best between AMD and METIS
                                    1 (amd): Use AMD ordering (min degree for MKL PARDISO)
                                    2 (metis): Use METIS ordering
linsolver_pivottol                   Specifies the initial pivot threshold used in the factorization routine. The value must be in the range [0 0.5] with higher values resulting in more pivoting (more stable factorization). Values less than 0 will be set to 0 and values larger than 0.5 will be set to 0.5. If pivot is non-positive initially no pivoting will be performed. Smaller values may improve the speed of the code but higher values are recommended for more stability.
linsolver_scaling                    Controls scaling method for linear solvers.
                                    0 (none): No scaling is applied in the linear system solves
                                    1 (always): Always apply scaling in the linear system solves
                                    2 (dynamic): Dynamically apply scaling in the linear system solves
lmsize                               Number of limited memory pairs to store when Hessian choice is lbfgs.
lpsolver                             Solver used with 'act_lpalg'.  Should be 'internal',
                                     'cplex', or 'xpress'.  Default = 'internal'; cplex or
                                     xpress must be suitably licensed.  For lpsolver=...
                                     to be useful, alg=2, 3, or 4 may also be needed.
                                     Implicitly sets omitted keywords act_lpsolver and,
                                     if appropriate, cplexlibname ot xpresslibname.
ma_maxtime_cpu                       Deprecated (use 'maxtime' option)
ma_maxtime_real                      Maximum allowable real time in seconds for the complete multi algorithm solution when 'alg=multi'.  Use maxtime_real to additionally limit time spent per each algorithm.
ma_outsub                            Specifies multi algorithm subproblem solve output control. Output is directed to a file 'knitro_ma_*.log'.
                                    0 (none): No output from subproblem solves
                                    1 (yes): Subproblem output enabled, controlled by option 'outlev'
ma_sub_maxtime                       Maximum allowable real time in seconds for individual multi-algorithm subproblems. Use maxtime to set a global time limit for the multi-algorithm solver.
ma_terminate                         Specifies conditions for terminating when 'algorithm=multi'.
                                    0 (all): Terminate after all algorithms complete
                                    1 (optimal): Terminate at first local optimum
                                    2 (feasible): Terminate at first feasible solution estimate
                                    3 (any): Terminate at first completed solve
maxcgit                              Deprecated (use 'cg_maxit' option)
maxcrossit                           Deprecated (use 'bar_maxcrossit' option)
maxfevals                            Maximum number of function evaluations to allow (a negative number implies no limit is imposed).
maxit                                Maximum number of iterations to allow (if 0 then Knitro determines the best value). Default values are 10000 for NLP and 3000 for MIP.
maxtime                              Maximum allowable real time in seconds for an optimization solve. This is a global time limit parameter that applies to single solves as well as multi-start, multi-algorithm, tuner or MIP solves.
maxtime_cpu                          Deprecated (use 'maxtime' option)
maxtime_real                         Maximum allowable real time in seconds for one algorithm solve. If multistart, multi algorithm or MIP is active, this limits time spent on just one subproblem solve (deprecated - use maxtime and *_sub_maxtime).
mip_branchrule                       Specifies the MIP branching rule for choosing a variable.
                                    0 (auto): Let Knitro choose the rule
                                    1 (most_frac): Most fractional (most infeasible) variable
                                    2 (pseudocost): Use pseudo-cost value
                                    3 (strong): Use strong branching
mip_clique                           Specifies rules for adding MIP Clique cuts.
                                    -1 (auto): Determine automatically
                                    0 (none): Do not add clique cuts
                                    1 (root): Add clique cuts at root node
                                    2 (tree): Add clique cuts in the whole tree
mip_cut_flowcover                    Specifies rules for adding MIP flow cover cuts.
                                    -1 (auto): Determine automatically
                                    0 (none): Do not add flow cover cuts
                                    1 (root): Add flow cover cuts at root node only
                                    2 (tree): Add flow cover cuts at any tree node
mip_cut_probing                      Specifies rules for adding MIP probing cuts.
                                    -1 (auto): Determine automatically
                                    0 (none): Do not add probing cuts
                                    1 (root): Add probing cuts at root node only
                                    2 (tree): Add probing cuts at any tree node
mip_cut_strategy                     Internal parameter
mip_cutfactor                        Limit on the number of cuts added to node NLP; if nonnegative, a maximum of mip_cutfactor times number of constraints cuts is possibly appended.
mip_cutoff                           MIP objective cutoff value.
mip_cutting_plane                    Specifies where to perform the cutting plane routine.
                                    0 (none): Do not perform cutting plane
                                    1 (root): Only perform root-cutting
mip_cutting_plane_reltol             Internal parameter
mip_debug                            Specifies debugging level for MIP solution.
                                    0 (none): No MIP debugging info
                                    1 (all): Write debugging to the file kdbg_mip.log
mip_gomory                           Specifies rules for adding MIP Gomory cuts.
                                    -1 (auto): Determine automatically
                                    0 (none): Do not add gomory cuts
                                    1 (root): Add gomory cuts at root node only
                                    2 (tree): Add gomory cuts at any tree node
mip_gub_branch                       Whether to branch on generalized upper bounds (GUBs).
                                    0 (no): Do not branch on GUBs
                                    1 (yes): Branch on GUBs
mip_heuristic_diving                 Controls use of the diving MIP heuristic.
mip_heuristic_feaspump               Whether to use the feasibility pump MIP heuristic.
                                    -1 (auto): Determine automatically
                                    0 (off): Feasibility pump heuristic is turned off
                                    1 (on): Feasibility pump heuristic is turned on
mip_heuristic_lns                    Controls use of the Large Neighborhood Search (LNS) MIP heuristic.
mip_heuristic_localsearch            Whether to use the MIP local search heuristic.
                                    -1 (auto): Determine automatically
                                    0 (off): MIP local search heuristic is turned off
                                    1 (on): MIP local search heuristic is turned on
mip_heuristic_maxit                  Maximum number of iterations to allow for MIP heuristic.
mip_heuristic_misqp                  Whether to use the MISQP MIP heuristic.
                                    -1 (auto): Determine automatically
                                    0 (off): MISQP heuristic is turned off
                                    1 (on): MISQP heuristic is turned on
mip_heuristic_mpec                   Whether to use the MPEC MIP heuristic.
                                    -1 (auto): Determine automatically
                                    0 (off): MPEC heuristic is turned off
                                    1 (on): MPEC heuristic is turned on
mip_heuristic_strategy               Specifies the strategy used for the MIP heuristics.
                                    -1 (auto): Automatic strategy
                                    0 (none): No heuristics are used
                                    1 (basic): Try basic heuristics
                                    2 (advanced): Try more advanced heuristics
                                    3 (extensive): Try most extensive heuristics
mip_heuristic_terminate              Specifies conditions for terminating the MIP heuristic.
                                    1 (feasible): Terminate at first feasible point
                                    2 (limit): Run heuristic until it hits limit
mip_implications                     Whether to add logical implications deduced from branching decisions at a MIP node.
                                    0 (no): Do not add logical implications
                                    1 (yes): Add logical implications
mip_initptfile                       Name for the file from which to read the MIP initial point (default 'NULL', no MIP initial point read from file).
mip_integer_tol                      Threshold for deciding if a variable value is integral.
mip_integral_gap_abs                 Deprecated (use 'mip_opt_gap_abs' option)
mip_integral_gap_rel                 Deprecated (use 'mip_opt_gap_rel' option)
mip_intvar_strategy                  How to handle integer variables by default.
                                    0 (none): No special treatment
                                    1 (relax): Relax integer variables
                                    2 (mpec): Convert to mpec constraints
mip_knapsack                         Specifies rules for adding MIP knapsack cuts.
                                    -1 (auto): Determine automatically
                                    0 (none): Do not add knapsack cuts
                                    1 (root): Add knapsack cuts derived in the root node
                                    2 (tree): Add knapsack cuts in the whole tree
mip_liftproject                      Specifies rules for adding MIP Lift and Project cuts.
                                    -1 (auto): Determine automatically
                                    0 (none): Do not add lift and project cuts
                                    1 (root): Add lift and project cuts at root node
mip_lpalg                            Specifies which algorithm to use for LP subproblem solves in MIP.
                                    0 (auto): Let Knitro choose the algorithm
                                    1 (direct): Use Interior (barrier) Direct algorithm
                                    2 (cg): Use Interior (barrier) CG algorithm
                                    3 (active): Use Active Set (simplex) algorithm
mip_maxnodes                         Maximum number of nodes explored (0 means no limit).
mip_maxsepcons                       Internal parameter
mip_maxsolves                        Maximum number of subproblem solves allowed (0 means no limit).
mip_maxtime_cpu                      Deprecated (use 'maxtime' option)
mip_maxtime_real                     Maximum allowable real time in seconds for the complete MIP solution. Use maxtime_real to additionally limit time spent per subproblem solve.
mip_method                           Which MIP method to use.
                                    0 (auto): Let Knitro choose the method
                                    1 (BB): Standard branch and bound
                                    2 (HQG): Hybrid Quesada-Grossman
                                    3 (MISQP): Mixed-integer SQP
mip_mir                              Specifies rules for adding MIP Mixed Integer Rounding cuts.
                                    -1 (auto): Automatically determine whether to add mir cuts
                                    0 (none): Do not add mir cuts
                                    1 (root): Add mir cuts derived in the root node
                                    2 (tree): Add mir cuts in the whole tree
mip_multistart                       Enables the MIP multistart procedure.
                                    0 (off): MIP multistart turned off
                                    1 (on): MIP multistart turned on
mip_nodealg                          Specifies which algorithm to use for standard node subproblem solves in MIP
                                    0 (auto): Let Knitro choose the algorithm
                                    1 (direct): Use Interior (barrier) Direct algorithm
                                    2 (cg): Use Interior (barrier) CG algorithm
                                    3 (active): Use Active Set SLQP algorithm
                                    4 (sqp): Use Active Set SQP algorithm
                                    5 (multi): Run multiple algorithms (perhaps in parallel)
mip_numthreads                       Number of threads to use for MIP solvers. choose any positive integer, or 0 = determine automatically
mip_opt_gap_abs                      Specifies absolute stop tolerance for sufficiently small optimality gap.
mip_opt_gap_rel                      Specifies relative stop tolerance for sufficiently small optimality gap.
mip_outinterval                      Specifies printing interval for mip_outlevel. 1 = print every node 2 = print every 2nd node N = print every Nth node
mip_outlevel                         How much MIP information to print.
                                    0 (none): Nothing
                                    1 (iters): One line for every node
                                    2 (iterstime): Also print accumulated time every node
                                    3 (root): Also print output from root node relaxation solve
mip_outsub                           Specifies MIP subproblem solve output control.
                                    0 (none): Do not print any debug output from subproblem solves.
                                    1 (yes): Subproblem debug output enabled, controlled by option `outlev`.
                                    2 (yesprob): Subproblem debug output enabled and print problem characteristics.
mip_pseudoinit                       How to initialize pseudo-costs.
                                    0 (auto): Let Knitro choose the method
                                    1 (ave): Use average value
                                    2 (strong): Use strong branching
mip_relaxable                        Whether integer variables are relaxable.
                                    0 (none): Integer variables not relaxable
                                    1 (all): All integer variables are relaxable
mip_restart                          Enables the MIP restart procedure.
                                    0 (off): MIP restart turned off
                                    1 (on): MIP restart turned on
mip_rootalg                          Specifies which algorithm to use for the root node solve in MIP
                                    0 (auto): Let Knitro choose the algorithm
                                    1 (direct): Use Interior (barrier) Direct algorithm
                                    2 (cg): Use Interior (barrier) CG algorithm
                                    3 (active): Use Active Set SLQP algorithm
                                    4 (sqp): Use Active Set SQP algorithm
                                    5 (multi): Run multiple algorithms (perhaps in parallel)
mip_rounding                         Specifies the MIP rounding rule to apply.
                                    -1 (auto): Let Knitro choose the rule
                                    0 (none): Do not round if a node is infeasible
                                    2 (heur_only): Round using heuristic only (fast)
                                    3 (nlp_sometimes): Round and solve NLP if likely to succeed
                                    4 (nlp_always): Always round and solve NLP
mip_selectdir                        Specifies the MIP select direction for choosing a node.
                                    0 (down): Choose the lesser-than node first
                                    1 (up): Choose the greater-than node first
mip_selectrule                       Specifies the MIP select rule for choosing a node.
                                    0 (auto): Let Knitro choose the rule
                                    1 (depth_first): Search the tree depth first
                                    2 (best_bound): Node with the best relaxation bound
                                    3 (combo_1): Depth first unless pruned, then best bound
mip_skipfactor                       Internal parameter
mip_strong_candlim                   Maximum number of candidates to explore for MIP strong branching.
mip_strong_level                     Maximum number of levels on which to perform MIP strong branching.
mip_strong_maxit                     Maximum number of iterations to allow for MIP strong branching solves.
mip_sub_maxtime                      Maximum allowable real time in seconds for individual MIP subproblems. Use maxtime to set a global time limit for the MIP solver.
mip_terminate                        Specifies conditions for terminating the MIP algorithm.
                                    0 (optimal): Terminate at optimum
                                    1 (feasible): Terminate at first integer feasible point
mip_zerohalf                         Specifies rules for adding MIP zero-half cuts.
                                    -1 (auto): Determine automatically
                                    0 (none): Do not add zero-half cuts
                                    1 (root): Add cuts derived in the root node
                                    2 (tree): Add zero-half cuts in the whole tree
ms_deterministic                     Whether to use a deterministic version of multistart.
                                    0 (no): Multithreaded multistart is non-deterministic
                                    1 (yes): Multithreaded multistart is deterministic
ms_enable                            Whether to enable multistart to find a better local minimum.
                                    0 (no): Knitro solves from a single initial point
                                    1 (yes): Knitro solves using multiple start points
ms_initpt_cluster                    The strategy for clustering initial points in multistart.
                                    0 (none): Do not apply clustering
                                    1 (sl): Apply single linkage based clustering
ms_maxbndrange                       Specifies the maximum range that an unbounded variable can vary over when multistart computes new start points.
ms_maxsolves                         How many Knitro solutions to compute if multistart is enabled. choose any positive integer, or 0 = Knitro sets a default value depending on context
ms_maxtime_cpu                       Deprecated (use 'maxtime' option)
ms_maxtime_real                      Maximum allowable real time in seconds for the complete multistart solution.  Use maxtime_real to additionally limit time spent per start point.
ms_num_to_save                       How many feasible multistart points to save in file knitro_mspoints.log. choose any positive integer, or 0 = save none
ms_numthreads                        Number of threads to use in parallel multistart. choose any positive integer, or 0 = determine automatically based on numthreads
ms_outsub                            Specifies parallel multistart subproblem solve output control. Output is directed to a file 'knitro_ms_*.log'.
                                    0 (none): No output from subproblem solves
                                    1 (yes): Subproblem output enabled, controlled by option 'outlev'.
ms_savetol                           Specifies the tolerance for deciding two feasible points are the same.
ms_seed                              Specifies the seed for random initialization of the multistart procedure. Seed value should an integer >= 0.  Negative values will be reset to 0.
ms_startptrange                      Specifies the maximum range that any variable can vary over when multistart computes new start points.
ms_sub_maxtime                       Maximum allowable real time in seconds for individual multi-start subproblems. Use maxtime to set a global time limit for the multi-start solver.
ms_terminate                         Specifies conditions for terminating the multistart procedure.
                                    0 (maxsolves): Terminate after maxsolves
                                    1 (optimal): Terminate at first local optimum
                                    2 (feasible): Terminate at first feasible solution estimate
                                    3 (any): Terminate at first completed solve
                                    4 (rulebased): Terminate when the estimated probability of finding a new local solution is low
ms_terminaterule_tol                 The tolerance in (0,1] for the rule-based termination of multistart.
mu                                   Deprecated (use 'bar_initmu' option)
multistart                           Deprecated (use 'ms_enable' option)
ncvx_qcqp_init                       Initialization strategy for non-convex QCQPs.
                                    -1 (auto): Knitro will automatically determine the strategy.
                                    0 (none): No special initialization strategy is used.
                                    1 (linear): Initialize by solving a linear relaxation.
                                    2 (hybrid): Initialize by solving a hybrid formulation.
                                    3 (penalty): Initialize by solving a penalty formulation.
                                    4 (cvxquad): Initialize by solving a convex quadratic relaxation.
newpoint                             Specifies additional action to take after every iteration. Iterations result in a new solution estimate.
                                    0 (none): No additional action
                                    1 (saveone): Save the latest new point to file knitro_newpoint.log
                                    2 (saveall): Append the latest new point to file knitro_newpoint.log
numthreads                           Number of threads to use in parallel features. choose any positive integer, or -1 = let Knitro automatically choose the number of threads to use 0 = value determined by OMP_NUM_THREADS environment variable
objno                                objective number: 0 = none, 1 = first (default),
                                       2 = second (if _nobjs > 1), etc.
objrange                             Valid range of objective values.
objrep                               Whether to replace
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
optionsfile                          Name/location of Knitro options file if provided
opttol                               Specifies the final relative stopping tolerance for the KKT (optimality) error. Smaller values of opttol result in a higher degree of accuracy in the solution with respect to optimality.
opttol_abs                           Specifies the final absolute stopping tolerance for the KKT (optimality) error. Smaller values of opttol_abs result in a higher degree of accuracy in the solution with respect to optimality.
opttolabs                            Deprecated (use 'opttol_abs' option)
out_csvinfo                          Whether to generate a csv solution file.
                                    0 (no): No csv solution file is generated
                                    1 (yes): Generate a solution file 'knitro_solve.csv'
out_csvname                          Name for the csv file generated by 'out_csvinfo' (default 'knitro_solve.csv').
out_hints                            Enable output printing of hints for setting parameters.
                                    0 (no): Do not print any hints.
                                    1 (yes): Print diagnostic hints on occasion.
out_jsoninfo                         Internal parameter
out_jsonname                         Internal parameter
outappend                            Specifies whether to append to output files.
                                    0 (no): Erase existing files when opening
                                    1 (yes): Append to existing files
outdir                               Directory for all output files.
outlev                               Specifies the verbosity of output.
                                    0 (none): Nothing
                                    1 (summary): Only final summary information
                                    2 (iter_10): Information every 10 iterations is printed
                                    3 (iter): Information at each iteration is printed
                                    4 (iter_verbose): More verbose information at each iteration is printed
                                    5 (iter_x): In addition, values of solution vector (x) are printed
                                    6 (all): In addition, constraints (c) and multipliers (lambda)
outmode                              Where to direct the output.
                                    0 (screen): Directed to stdout
                                    1 (file): Directed to a file (default name 'knitro.log')
                                    2 (both): Both stdout and file (default name 'knitro.log')
outname                              Name for the standard log file generated by Knitro (default 'knitro.log').
par_blasnumthreads                   Deprecated (use 'blas_numthreads' option)
par_concurrent_evals                 Deprecated (use 'concurrent_evals' option)
par_conicnumthreads                  Deprecated (use 'conic_numthreads' option)
par_lsnumthreads                     Deprecated (use 'linsolver_numthreads' option)
par_msnumthreads                     Deprecated (use 'ms_numthreads' option)
par_numthreads                       Deprecated (use 'numthreads' option)
pivot                                Deprecated (use 'linsolver_pivottol' option)
presolve                             Whether to apply any presolve operations to the model.
                                    0 (no): No presolve
                                    1 (yes): Knitro performs presolve
presolve_dbg                         Internal parameter
presolve_initpt                      Presolve handling of user-specified initial point.
                                    -1 (auto): Determine automatically
                                    0 (noshift): Do not shift initial point in presolve
                                    1 (linshift): Allow shifting variables in linear constraints
                                    2 (anyshift): Allow shifting any variable
presolve_level                       Presolve level.
                                    -1 (auto): Determine automatically
                                    1 (level1): Most basic presolve
                                    2 (level2): More advanced presolve
presolve_passes                      Maximum number of presolve passes allowed.
presolve_tol                         Specifies the tolerance used to determine whether or not deduced bounds from the presolve operation are infeasible.
presolveop_bigm                      Internal parameter
presolveop_redundant                 Detection/removal degree of redundant constraints
                                    0 (none): Do not detect redundant constraints
                                    1 (dupcon): Detect and remove duplicate constraints
                                    2 (depcon): Detect and remove linearly dependent constraints
presolveop_substitution              Substitution of variable involved in an equality constraint
                                    -1 (auto): Automatic substitution procedure
                                    0 (none): No substitution
                                    1 (simple): Only doubleton equality substitutions
                                    2 (all): All possible substitutions
presolveop_substitution_fillin       Internal parameter
presolveop_substitution_relfeasincr  Internal parameter
presolveop_substitution_tol          Tolerance for applying a substitution. This is a relative tolerance on coefficients involved with the substituted variable. Higher values mean that less reductions will be applied (potentially improving numerical focus). Zero value means all possible substitutions are applied.
presolveop_substitution_zero_tol     Internal parameter
presolveop_tighten                   Presolve tightening operations.
                                    -1 (auto): Automatic tightening procedure
                                    0 (none): No tightening
                                    1 (varbnd): Tighten variable bounds
                                    2 (coef): Tighten coefficients in linear constraints
                                    3 (all): Variable bounds and coefficients
presolveop_varbnd_abs_max_val        Internal parameter
presolveop_varbnd_drop_redundant     Internal parameter
presolveop_varbnd_rel_min_change     Internal parameter
qpcheck                              whether to check for a QP: deprecated
relax                                whether to ignore integrality: 0 (default) = no, 1 = yes
restarts                             Maximum number of internal restarts to allow.
restarts_maxit                       Maximum number of iterations before invoking restart heuristic.
scale                                Whether to perform scaling of the problem.
                                    0 (no): No scaling done
                                    1 (user_internal): User, if defined, otherwise internal
                                    2 (user_none): User, if defined, otherwise none
                                    3 (internal): Knitro performs internal scaling
scale_vars                           The strategy for scaling variables.
                                    0 (none): Do not apply any variable scaling
                                    1 (bnds): Apply variable scaling based on their bound values
simplex_maxit                        Internal parameter
soc                                  Whether to use the Second Order Correction (SOC) option.
                                    0 (no): Never do second order corrections
                                    1 (maybe): SOC steps attempted on some iterations
                                    2 (yes): SOC steps always attempted when constraints are nonlinear
soltype                              Specifies the solution returned by Knitro.
                                    0 (final): Return the final iterate
                                    1 (bestfeas): Return the best feasible iterate found
sph_opts                             Sparse Hessian options (bits)
storequadcoefs                       Store quadratic coefficients when solving QCQPs
strat_warm_start                     Enable a warm-start strategy.
                                    0 (no): No warm-start strategy is applied.
                                    1 (yes): Knitro will apply a warm-start strategy with special tunings.
threads                              Deprecated (use 'numthreads' option)
timing                               Whether to report problem I/O and solve times:
                                     0 (default) = no
                                     1 = yes, on stdout
                                     2 = yes, on stderr
                                     3 = yes, on both stdout and stderr
tuner                                Whether to use the Knitro Tuner.
                                    0 (off): Knitro Tuner turned off
                                    1 (on): Knitro Tuner enabled
tuner_maxtime_cpu                    Deprecated (use 'maxtime' option)
tuner_maxtime_real                   Maximum allowable real time in seconds for the complete Tuner procedure when 'tuner=on'.  Use maxtime_real to additionally limit time spent per each individual solve.
tuner_optionsfile                    Can be used to specify the location of a tuner options file
tuner_outsub                         Specifies Tuner subproblem solve output control. Output is directed to a file 'knitro_tuner_*.log'
                                    0 (none): No output from subproblem solves and no subproblem summary file
                                    1 (summary): Subproblem output summary directed to a file 'knitro_tuner_summary.log'
                                    2 (all): Subproblem output enabled, controlled by option 'outlev'.
tuner_sub_maxtime                    Maximum allowable real time in seconds for individual Tuner subproblems when 'tuner=on'.  Use maxtime to set a global time limit for the Tuner.
tuner_terminate                      Specifies conditions for terminating Tuner procedure.
                                    0 (all): Terminate after all Tuner runs complete
                                    1 (optimal): Terminate at first local optimum
                                    2 (feasible): Terminate at first feasible solution estimate
                                    3 (any): Terminate at first completed solve
version                              Report software version
wantsol                              Solution report without -AMPL: sum of
                                     1 ==> write .sol file
                                     2 ==> 1 ==> write .sol file
                                     4 ==> print dual variable values
                                     8 ==> do not print solution message
xpresslibname                        Name of the XPRESS library if using act_lpsolver=xpress
xtol                                 Step size tolerance used for terminating the optimization.
xtol_iters                           Consecutive iterations for stopping on small changes in the solution estimate.
```

