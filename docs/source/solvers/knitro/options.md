
# KNITRO Options

```ampl
ampl: option solver knitro; # change the solver
ampl: option knitro_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

Solver options obtained with `$ knitro -=`.

```
act_lpalg                    Indicates which algorithm to use to solve linear programming (LP) subproblems when using the Knitro Active Set or SQP algorithms.
                                    0 (default): Use the default algorithm for the chosen LP solver.
                                    1 (primal): Use a primal simplex algorithm.
                                    2 (dual): Use a dual simplex algorithm.
                                    3 (barrier): Use a barrier/interior-point algorithm.
act_lpfeastol                Specifies the feasibility tolerance used for linear programming subproblems solved when using the Active Set or SQP algorithms.
act_lppenalty                Indicates whether to use a penalty formulation for linear programming subproblems in the Knitro Active Set or SQP algorithms.
                                    1 (all): Penalize all constraints.
                                    2 (nonlinear): Penalize only nonlinear constraints.
                                    3 (dynamic): Dynamically choose which constraints to penalize.
act_lppresolve               Indicates whether to apply a presolve for linear programming subproblems in the Knitro Active Set or SQP algorithms.
                                    0 (off): Presolve turned off for LP subproblems.
                                    1 (on): Presolve turned on for LP subproblems.
act_lpsolver                 Indicates which linear programming simplex solver the Knitro Active Set or SQP algorithms use when solving internal LP subproblems.
                                    1 (internal): Use internal LP solver
                                    2 (cplex): CPLEX (if user has a valid license)
                                    3 (xpress): XPRESS (if user has a valid license)
act_parametric               Indicates whether to use a parametric approach when solving linear programming (LP) subproblems when using the Knitro Active Set or SQP algorithms.
                                    0 (no): Never
                                    1 (maybe): Use selectively
                                    2 (yes): Always use parametric approach
act_qpalg                    Indicates which algorithm to use to solve quadratic programming (QP) subproblems when using the Knitro Active Set or SQP algorithms.
                                    0 (auto): Let Knitro choose the algorithm
                                    1 (direct): Use Interior (barrier) Direct algorithm
                                    2 (cg): Use Interior (barrier) CG algorithm
                                    3 (active): Use Active Set SLQP algorithm
act_qppenalty                Indicates whether to use a penalty formulation for quadratic programming subproblems in the Knitro SQP algorithm.
                                    -1 (auto): Let Knitro automatically decide.
                                    0 (none): Do not penalize constraints in QP subproblems.
                                    1 (all): Penalize all constraints in QP subproblems.
al_initpenalty               Specifies the initial penalty parameter value used in the Augmented Lagrangian (AL) algorithm.
al_maxpenalty                Specifies the maximum allowable penalty parameter value used in the Augmented Lagrangian (AL) algorithm.
alg                          Deprecated (use 'nlp_algorithm' option)
algorithm                    Deprecated (use 'nlp_algorithm' option)
bar_conic_enable             Enable special treatments for conic constraints.
                                    -1 (auto): Let Knitro automatically choose the strategy.
                                    0 (none): Do not apply any special treatment for conic constraints.
                                    1 (soc): Apply special treatments for any Second Order Cone (SOC) constraints identified in the model.
bar_directinterval           Controls the maximum number of consecutive conjugate gradient (CG) steps before Knitro will try to enforce that a step is taken using direct linear algebra.
bar_feasible                 Specifies whether special emphasis is placed on getting and staying feasible in the interior-point algorithms.
                                    0 (no): No emphasis on feasibility
                                    1 (stay): Iterates must satisfy inequality constraints once they become sufficiently feasible.
                                    2 (get): Special emphasis is placed on getting feasible before trying to optimize.
                                    3 (get_stay): Implement both options 1 and 2 above.
bar_feasmodetol              Tolerance used in the feasibility condition that determines whether Knitro will force subsequent iterates to remain feasible.
bar_globalize                Specifies the globalization strategy used in the interior-point algorithms.
                                    0 (none): Do not apply any globalization strategy
                                    1 (kkt): Apply a globalization strategy based on decreasing the KKT error
                                    2 (filter): Apply a globalization strategy using a filter based on the objective and constraint violation
bar_initmu                   Specifies the initial value for the barrier parameter $\mu$ used with the barrier algorithms.
bar_initpi_mpec              Specifies the initial value for the MPEC penalty parameter $\pi$ used when solving problems with complementarity constraints using the barrier algorithms.
bar_initpt                   Indicates initial point strategy for `x`, slacks and multipliers when using a barrier algorithm.
                                    0 (auto): Let Knitro choose the strategy
                                    1 (convex): Initialization designed for convex models.
                                    2 (nearbnd): Initialization strategy that stays closer to the bounds.
                                    3 (central): Initialization strategy that is more central on double-bounded variables.
bar_initshiftol              Deprecated (use 'bar_initshifttol' option)
bar_linsys                   Indicates which linear system form is used inside the Interior/Direct algorithm for computing primal-dual steps.
                                    -1 (auto): Let Knitro automatically choose the linear system form.
                                    0 (full): Use the full linear system.
                                    1 (slacks): Eliminate the slack variables.
                                    2 (bounds): Eliminate the slack variables and bounds.
                                    3 (ineqs): Eliminate the slack variables, bounds, and some inequalities.
bar_linsys_storage           Indicates how to store in memory the linear systems used inside the Interior/Direct algorithm for computing primal-dual steps.
                                    -1 (auto): Let Knitro automatically choose the linear system storage approach.
                                    1 (lowmem): Use common storage for multiple linear systems.
                                    2 (normal): Use separate storage for different linear systems.
bar_maxcorrectors            Specifies the maximum number of corrector steps allowed for primal-dual steps.
bar_maxcrossit               Specifies the maximum number of crossover iterations before termination.
bar_maxmu                    Specifies the maximum allowable value for the barrier parameter $\mu$ used with the barrier algorithms.
bar_maxrefactor              Indicates the maximum number of refactorizations of the KKT system per iteration of the Interior/Direct algorithm before reverting to a CG step.
bar_mpec_heuristic           Specifies whether or not to use a heuristic approach when solving MPEC models with the barrier algorithm.
                                    0 (no): No MPEC heuristic enabled
                                    1 (yes): MPEC heuristic is enabled
bar_murule                   Indicates which strategy to use for modifying the barrier parameter $\mu$ in the barrier algorithms.
                                    0 (auto): Let Knitro choose the strategy
                                    1 (monotone): Monotonically decrease the barrier parameter. Available for both barrier algorithms.
                                    2 (adaptive): Use an adaptive rule based on the complementarity gap to determine the value of the barrier parameter. Available for both barrier algorithms.
                                    3 (probing): Use a probing (affine-scaling) step to dynamically determine the barrier parameter. Available only for the Interior/Direct algorithm.
                                    4 (dampmpc): Use a Mehrotra predictor-corrector type rule to determine the barrier parameter, with safeguards on the corrector step. Available only for the Interior/Direct algorithm.
                                    5 (fullmpc): Use a Mehrotra predictor-corrector type rule to determine the barrier parameter, without safeguards on the corrector step. Available only for the Interior/Direct algorithm.
                                    6 (quality): Minimize a quality function at each iteration to determine the barrier parameter. Available only for the Interior/Direct algorithm.
bar_penaltycons              Indicates whether a penalty approach is applied to the constraints.
                                    -1 (auto): Let Knitro choose the strategy
                                    0 (none): Do not apply penalty approach to any constraints
                                    2 (all): Apply a penalty approach to all general constraints
                                    3 (equalities): Apply a penalty approach to equality constraints only
bar_penaltyrule              Indicates which penalty parameter strategy to use for determining whether or not to accept a trial iterate.
                                    0 (auto): Let Knitro choose the strategy
                                    1 (single): Use a single penalty parameter in the merit function to weight feasibility versus optimality.
                                    2 (flex): Use a more tolerant and flexible step acceptance procedure based on a range of penalty parameter values.
bar_refinement               Specifies whether to try to refine the barrier solution for better precision.
                                    0 (no): Do not refine the barrier solution
                                    1 (yes): Try to refine the barrier solution
bar_relaxcons                Indicates whether a relaxation approach is applied to the constraints.
                                    0 (none): Do not relax any constraints
                                    1 (eqs): Relax only equality constraints
                                    2 (ineqs): Relax only inequality constraints
                                    3 (all): Relax all general constraints
bar_slackboundpush           Specifies the amount by which the barrier slack variables are initially pushed inside the bounds.
bar_switchobj                Indicates which objective function to use when the barrier algorithms switch to a pure feasibility phase.
                                    0 (none): No objective
                                    1 (scalarprox): Proximal point objective with scalar weighting
                                    2 (diagprox): Proximal point objective with diagonal weighting
bar_switchrule               Indicates whether or not the barrier algorithms will allow switching from an optimality phase to a pure feasibility phase.
                                    -1 (auto): Let Knitro choose the strategy
                                    0 (never): Never switch
                                    2 (moderate): Allow moderate switching
                                    3 (aggressive): More aggressive switching
bar_watchdog                 Specifies whether to enable watchdog heuristic for barrier algorithms.
                                    0 (no): No watchdog heuristic
                                    1 (yes): Allow watchdog heuristic to be used
bfgs_scaling                 Specify the initial scaling to use for the BFGS or L-BFGS Hessian approximation.
                                    0 (dynamic): Dynamically determine
                                    1 (invhess): Approximate scale of the inverse Hessian
                                    2 (hess): Approximate the scale of the Hessian
blas_numthreads              Specify the number of threads to use for BLAS operations when `blasoption` = `1`
blasoption                   Specifies the BLAS/LAPACK function library to use for basic vector and matrix computations.
                                    -1 (auto): Let Knitro automatically choose which BLAS to use
                                    0 (knitro): Use Knitro built-in functions
                                    1 (intel): Use Intel Math Kernel Library (MKL) functions on available platforms.
                                    2 (dynamic):  Use the dynamic library specified with option `blasoptionlib`
                                    3 (blis): Use BLIS functions on available platforms (currently not available on Windows OS).
                                    4 (apple): Use Apple Accelerate (only available on Mac with M1 processor).
blasoptionlib                Specifies a dynamic library name that contains object code for BLAS/LAPACK functions.
bndrange                     Specifies max limits on the magnitude of constraint and variable bounds.
cg_maxit                     Determines the maximum allowable number of inner conjugate gradient (CG) iterations per Knitro minor iteration.
cg_pmem                      Specifies the amount of nonzero elements per column of the Hessian of the Lagrangian which are retained when computing the incomplete Cholesky preconditioner.
cg_precond                   Specifies whether an incomplete Cholesky preconditioner is applied during CG iterations in barrier algorithms.
                                    0 (no): Not applied
                                    1 (chol): Preconditioner is applied
cg_stoptol                   Specifies the relative stopping tolerance used for the conjugate gradient (CG) subproblem solves.
concurrent_evals             Determines whether or not the user provided callback functions used for function and derivative evaluations can take place concurrently in parallel (for possibly different values of `x`).
                                    0 (no): Only one thread can perform an evaluation at a time
                                    1 (yes): Allow multi-threaded simultaneous evaluations
concurrent_lpalg             Specifies the LP algorithms to run concurrently when the concurrent solver is enabled on an LP.
                                    -1 (auto): Automatically determine LP algorithm for concurrent solver
                                    0 (nlp): Use algorithms specified in concurrent_nlpalg
                                    1 (primalsimplex): Enable Primal Simplex algorithm for concurrent solver
                                    2 (dualsimplex): Enable Dual Simplex algorithm for concurrent solver
                                    4 (barrier): Enable Interior-Point/Barrier algorithm for concurrent solver
                                    8 (pdlp): Enable Primal-Dual Linear Programming algorithm for concurrent solver
concurrent_maxsolves         Specifies the maximum number of solves when using the concurrent solver (should be more than 1 and <= `numthreads`).
concurrent_nlpalg            Specifies the NLP algorithms to run concurrently when the concurrent solver is enabled on an NLP.
                                    -1 (auto): Automatically determine NLP algorithm for concurrent solver
                                    1 (direct): Enable Barrier Direct algorithm for concurrent solver
                                    2 (cg): Enable Interior Barrier CG algorithm for concurrent solver
                                    4 (active): Enable Active-Set SLQP algorithm for concurrent solver
                                    8 (sqp): Enable SQP algorithm for concurrent solver
                                    16 (al): Enable Augmented Lagrangian algorithm for concurrent solver
concurrent_outlog            Specifies the output logging options when the concurrent solver is enabled.
                                    1 (all): Show all iteration information on all concurrent solves
                                    2 (objfeas): Show objective and feasibility error on all concurrent solves
                                    3 (best): Show information from the current best concurrent solve iterate
concurrent_solver            Specifies whether or not to enable the concurrent solver.
                                    -1 (auto): Determine automatically whether to enable the concurrent solver.
                                    0 (no): Do not enable the concurrent solver.
                                    1 (yes): Enable the concurrent solver.
conic_numthreads             Number of threads to do conic operations in parallel. Choose any positive integer, or 0 = determine automatically based on numthreads
convex                       Declare the problem as convex by setting `KN_CONVEX_YES` or non-convex by setting `KN_CONVEX_NO`.
                                    -1 (auto): Knitro will try to determine this automatically, but may only be able to do so for simple model forms such as QPs or QCQPs.
                                    0 (no): Declare problem as non-convex
                                    1 (yes): Declare problem as convex
cplexlibname                 See option `act_lpsolver`.
cpuplatform                  This option can be used to specify the target instruction set architecture for the machine on which Knitro is running.
                                    -1 (auto): Determine automatically
                                    1 (compatible): Aim for more compatible performance across architectures
                                    2 (sse2): SSE2
                                    3 (avx): AVX
                                    4 (avx2): AVX-2
                                    5 (avx512): AVX-512 (experimental)
datacheck                    Specifies whether to perform more extensive data checks to look for errors in the problem input to Knitro (in particular, this option looks for errors in the sparse Jacobian and/or sparse Hessian structure).
                                    0 (no): No extra data checks
                                    1 (yes): Perform extra data checks
debug                        Controls the level of debugging output.
                                    0 (none): No debugging output
                                    1 (problem): Print algorithm information to `kdbg*.log` output files.
                                    2 (execution): Print program execution information.
delta                        Specifies the initial trust region radius scaling factor used to determine the initial trust region size.
derivcheck                   Determine whether or not to perform a derivative check
                                    0 (none): No derivative check
                                    1 (first): Check first derivatives
                                    2 (second): Check second derivatives
                                    3 (all): Check all derivatives
derivcheck_terminate         Determine whether to always terminate after the derivative check or only when the derivative checker detects a possible error.
                                    1 (error): Stop when there is an error detected
                                    2 (always): Always stop after the derivative check
derivcheck_tol               Specifies the relative tolerance used for detecting derivative errors, when the Knitro derivative checker is enabled.
derivcheck_type              Specifies whether to use forward or central finite differencing for the derivative checker when it is enabled.
                                    1 (forward): Check using forward finite-differences
                                    2 (central): Check using central finite-differences
deterministic                This option specifies whether to always enforce deterministic behavior for Knitro.
                                    0 (no): Do not enforce deterministic behavior in Knitro.
                                    1 (yes): Enforce deterministic behavior in Knitro.
eval_cost                    Use this option to tell Knitro the relative cost of performing a callback.
                                    0 (unspecified): Evaluation cost is not specified
                                    1 (inexpensive): Evaluation cost is relatively inexpensive
                                    2 (expensive): Evaluation cost is relatively expensive
eval_fcga                    Use this option to tell Knitro that you are providing the first derivatives in the same callback routine used for your function evaluations.
                                    0 (no): Gradients are not evaluated in the function evaluation callback
                                    1 (yes): Gradients are evaluated in the function evaluation callback
feaserr_level                This option specifies the feasibility error measure used at the algorithm level and for termination.
                                    1 (application): Use feasibility error based on application level (original) problem form
                                    2 (internal): Use feasibility error based on internal (presolved, scaled) problem form
feasible                     Deprecated (use 'bar_feasible' option)
feasmodetol                  Deprecated (use 'bar_feasmodetol' option)
feastol                      Specifies the final relative stopping tolerance for the feasibility error.
feastol_abs                  Specifies the final absolute stopping tolerance for the feasibility error.
feastolabs                   Deprecated (use 'feastol_abs' option)
findiff_estnoise             This option can be used to enable an estimate of the noise in the model when using finite-difference gradients.
                                    0 (no): No estimation of noise performed
                                    1 (yes): Estimate the noise and perhaps use it to determine a finite-difference steplength
                                    2 (withcurv): Estimate a curvature factor as well as the noise and perhaps use it to determine a finite-difference steplength
findiff_numthreads           Number of threads to use in finite-differencing.
findiff_relstepsize          Specifies the relative stepsize used for finite-difference gradients during the optimization.
findiff_terminate            This option specifies the termination criteria when using finite-difference gradients.
                                    0 (none): No special criteria; use the standard stopping conditions.
                                    1 (errest): Allow termination based on estimates of the finite-difference error (when no more significant progress is likely).
fstopval                     Used to implement a custom stopping condition based on the objective function value.
ftol                         The optimization process will terminate if the relative change in the objective function is less than `ftol` for `ftol_iters` consecutive feasible iterations.
ftol_iters                   The optimization process will terminate if the relative change in the objective function is less than `ftol` for `ftol_iters` consecutive feasible iterations.
gradopt                      Specifies how to compute the gradients of the objective and constraint functions.
                                    1 (exact): User supplies exact first derivatives
                                    2 (forward): Gradients computed by internal forward finite differences
                                    3 (central): Gradients computed by internal central finite differences
                                    4 (user_forward): Gradients computed by user-provided forward finite differences
                                    5 (user_central): Gradients computed by user-provided central finite differences
hesevalthreads               Number of threads for hessian evaluations
hessetupthreads              Number of threads for hessian setup
hessian_no_f                 Determines whether or not to allow Knitro to request Hessian (or Hessian-vector product) evaluations without the objective component included.
                                    0 (forbid): Not allowed
                                    1 (allow): User can provide this version of the Hessian if requested
hessopt                      Specifies how to compute the (approximate) Hessian of the Lagrangian.
                                    0 (auto): Knitro will use exact Hessians if provided; otherwise it uses an appropriate approximation.
                                    1 (exact): Knitro uses supplied exact second derivatives
                                    2 (bfgs): Knitro computes a dense quasi-Newton BFGS Hessian
                                    3 (sr1): Knitro computes a dense quasi-Newton SR1 Hessian
                                    4 (product_findiff): Knitro computes Hessian-vector products by finite differences
                                    5 (product): User supplies exact Hessian-vector products
                                    6 (lbfgs): Knitro computes a limited-memory quasi-Newton BFGS Hessian
                                    7 (gauss_newton): Knitro computes a Gauss-Newton approximation of the Hessian (available for least-squares only, and default value for least-squares)
hesthreads                   Number of threads for hessian setup and evaluations
honorbnds                    Indicates whether or not to enforce satisfaction of simple variable bounds throughout the optimization.
                                    -1 (auto): Setting determined automatically by Knitro
                                    0 (no): Allow iterations to violate the bounds
                                    1 (always): Enforce bounds satisfaction of all iterates
                                    2 (initpt): Enforce bounds satisfaction of initial point
infeastol                    Specifies the (relative) tolerance used for declaring infeasibility of a model.
infeastol_iters              Controls the termination for consecutive infeasible iterations.
initpenalty                  Specifies the initial penalty parameter used in the Knitro merit functions.
initpt_strategy              Specifies the initial point strategy used for the continuous algorithms.
                                    -1 (auto): Automatic initial point strategy
                                    1 (basic): Try basic initial point strategy
                                    2 (advanced): Try more advanced initial point strategy
initptfile                   Specifies a file from which to read the initial point used for the Knitro algorithms.
leastsquares                 Solve as a least-squares model
linesearch                   Indicates which linesearch strategy to use for the Interior/Direct or SQP algorithm to search for a new acceptable iterate.
                                    0 (auto): Let Knitro choose the linesearch method
                                    1 (backtrack): Backtracking linesearch
                                    2 (interpolate): Interpolation based linesearch
                                    3 (weakwolfe): Weak Wolfe linesearch
linesearch_maxtrials         Indicates the maximum allowable number of trial points during the linesearch of the Interior/Direct or SQP algorithm before treating the linesearch step as a failure and generating a new step.
linsolver                    Indicates which linear solver to use to solve linear systems arising in Knitro algorithms.
                                    0 (auto): Let Knitro automatically choose the linear solver.
                                    1 (internal): Use internal solver provided with Knitro.
                                    2 (hybrid): Use a hybrid approach where the solver chosen depends on the particular linear system which needs to be solved.
                                    3 (qr): Use a dense QR method. This approach uses LAPACK QR routines. Since it uses a dense method, it is only efficient for small problems. It may often be the most efficient method for small problems with dense Jacobians or Hessian matrices.
                                    4 (ma27): Use the HSL MA27 sparse symmetric indefinite solver.
                                    5 (ma57): Use the HSL MA57 sparse symmetric indefinite solver.
                                    6 (mklpardiso): Use the Intel MKL PARDISO (parallel, deterministic) sparse symmetric indefinite solver (x86-64 only).
                                    7 (ma97): Use the HSL MA97 (parallel, deterministic) sparse symmetric indefinite solver.
                                    8 (ma86): Use the HSL MA86 (parallel, non-deterministic) sparse symmetric indefinite solver.
                                    9 (apple): Use the Apple Accelerate (parallel, non-deterministic) sparse symmetric indefinite solver (macOS only).
linsolver_maxitref           Indicates the maximum allowable number of iterative refinement steps applied when a linear system is solved inside Knitro.
linsolver_nodeamalg          Controls the node amalgamation setting for the MA57, MA86 and MA97 linear solvers.
linsolver_numthreads         Specify the number of threads to use for linear system solve operations when `linsolver` = `6`.
linsolver_ooc                Indicates whether to use Intel MKL PARDISO out-of-core solve of linear systems when `linsolver` = `mklpardiso`.
                                    0 (no): Always use in-core version
                                    1 (maybe): Will use out-of-core version beyond a certain size
                                    2 (yes): Always use out-of-core version
linsolver_ordering           Sets the ordering method used for the linear system solver.
                                    -1 (auto): Automatically determine ordering procedure
                                    0 (best): Choose the best between AMD and METIS
                                    1 (amd): Use AMD ordering (min degree for MKL PARDISO)
                                    2 (metis): Use METIS ordering
linsolver_pivottol           Specifies the initial pivot threshold used in factorization routines.
linsolver_scaling            Enables scaling for the linear system solver.
                                    0 (none): No scaling is applied in the linear system solves
                                    1 (always): Always apply scaling in the linear system solves
                                    2 (dynamic): Dynamically apply scaling in the linear system solves
lmsize                       Specifies the number of limited memory pairs stored when approximating the Hessian using the limited-memory quasi-Newton BFGS option.
lp_algorithm                 Indicates which algorithm to use to solve linear problems (LPs).
                                    -1 (auto): Let Knitro automatically decide.
                                    0 (nlp): Use algorithm specified in nlp_algorithm.
                                    1 (primalsimplex): Use Primal Simplex algorithm.
                                    2 (dualsimplex): Use Dual Simplex algorithm.
                                    3 (barrier): Use Interior-Point/Barrier algorithm.
                                    4 (pdlp): Use Primal-Dual Linear Programming algorithm.
lpsolver                     Solver used with 'act_lpalg'.  Should be 'internal',
                             'cplex', or 'xpress'.  Default = 'internal'; cplex or
                             xpress must be suitably licensed.  For lpsolver=...
                             to be useful, alg=2, 3, or 4 may also be needed.
                             Implicitly sets omitted keywords act_lpsolver and,
                             if appropriate, cplexlibname ot xpresslibname.
ma_maxtime_cpu               Deprecated (use 'maxtime' option)
ma_maxtime_real              Deprecated (use 'maxtime' option)
maxcgit                      Deprecated (use 'cg_maxit' option)
maxcrossit                   Deprecated (use 'bar_maxcrossit' option)
maxfevals                    Specifies the maximum number of function evaluations before termination.
maxit                        Specifies the maximum number of iterations before termination.
maxstepsize                  This option enforces a maximum step size limit at every iteration of the continuous NLP algorithms in Knitro (as well as the barrier LP algorithm).
maxstepsize_maxit            This option specifies the maximum number of iterations where the `maxstepsize` restriction is enforced (if 0 then no iteration limit is imposed for this).
maxtime                      Specifies, in seconds, the maximum allowable real time before termination.
maxtime_cpu                  Deprecated (use 'maxtime' option)
maxtime_real                 Deprecated (use 'maxtime' option)
mip_branchrule               Specifies which branching rule to use for MIP branch and bound procedure.
                                    0 (auto): Let Knitro choose the rule
                                    1 (most_frac): Most fractional (most infeasible) variable
                                    2 (pseudocost): Use pseudo-cost value
                                    3 (strong): Use strong branching
mip_clique                   Specifies rules for adding clique cuts.
                                    -1 (auto): Determine automatically
                                    0 (none): Do not add clique cuts
                                    1 (root): Add clique cuts at root node
                                    2 (tree): Add clique cuts in the whole tree
mip_cut_flowcover            Specifies rules for adding flow cover cuts.
                                    -1 (auto): Determine automatically
                                    0 (none): Do not add flow cover cuts
                                    1 (root): Add flow cover cuts at root node only
                                    2 (tree): Add flow cover cuts at any tree node
mip_cut_probing              Specifies rules for adding probing cuts.
                                    -1 (auto): Determine automatically
                                    0 (none): Do not add probing cuts
                                    1 (root): Add probing cuts at root node only
                                    2 (tree): Add probing cuts at any tree node
mip_cutfactor                This value specifies a limit on the number of cuts added to a node subproblem.
mip_cutoff                   This value specifies the objective cutoff value for MIP.
mip_cutoff_abs               This value specifies the absolute improvement cutoff value for MIP.
mip_cutoff_rel               This value specifies the relative improvement cutoff value for MIP.
mip_cutting_plane            Specifies when to apply the cutting plane procedure.
                                    0 (none): Do not perform cutting plane
                                    1 (root): Only perform root-cutting
mip_debug                    Specifies debugging level for MIP solution.
                                    0 (none): No MIP debugging info
                                    1 (all): Write debugging to the file kdbg_mip.log
mip_gomory                   Specifies rules for adding Gomory mixed-integer cuts.
                                    -1 (auto): Determine automatically
                                    0 (none): Do not add Gomory cuts
                                    1 (root): Add Gomory cuts at root node only
                                    2 (tree): Add Gomory cuts at any tree node
mip_gub_branch               Specifies whether or not to branch on generalized upper bounds (GUBs).
                                    0 (no): Do not branch on GUBs
                                    1 (yes): Branch on GUBs
mip_heuristic_diving         Specifies whether or not to enable the MIP diving heuristic.
                                    1 (auto): Automatically determined. If enabled, other bits are ignored.
                                    2 (d1): Pure fractional diving.
                                    4 (d2): Objective-guided fractional diving.
                                    8 (d3): Vectorlength diving (obsolete).
                                    16 (d4): Coefficient-branching diving (obsolete).
                                    32 (d5): Guided-branching diving (obsolete).
                                    64 (d6): Linesearch diving (obsolete).
                                    128 (d7): Pseudo-random diving using both fractionality and cliques.
                                    256 (d8): Fractional diving followed by lock-based diving.
                                    512 (d9): Fractional diving followed by objective-based diving.
                                    1024 (d10): Fractional diving skewed towards fixing binaries to 1.
mip_heuristic_feaspump       Specifies whether or not to enable the MIP feasibility pump heuristic.
                                    -1 (auto): Determine automatically
                                    0 (off): Feasibility pump heuristic is turned off
                                    1 (on): Feasibility pump heuristic is turned on
mip_heuristic_fixpropagate   Specifies whether or not to enable the MIP fix-and-propagate heuristic.
                                    1 (auto): Automatically determined. If enabled, other bits are ignored.
                                    2 (fixprop1): Activate fix & propagate heuristic 1.
                                    4 (fixprop2): Activate fix & propagate heuristic 2.
                                    8 (fixprop3): Activate fix & propagate heuristic 3.
                                    16 (fixprop4): Activate fix & propagate heuristic 4.
                                    32 (fixprop5): Activate fix & propagate heuristic 5.
mip_heuristic_lns            Specifies whether or not to enable the MIP large neighborhood search (LNS) heuristics.
mip_heuristic_localsearch    Specifies whether or not to enable the MIP local search heuristic.
                                    -1 (auto): Determine automatically
                                    0 (off): MIP local search heuristic is turned off
                                    1 (on): MIP local search heuristic is turned on
mip_heuristic_maxit          Maximum number of iterations to allow for MIP heuristic.
mip_heuristic_misqp          Specifies whether or not to enable the MIP MISQP heuristic.
                                    -1 (auto): Determine automatically
                                    0 (off): MISQP heuristic is turned off
                                    1 (on): MISQP heuristic is turned on
mip_heuristic_mpec           Specifies whether or not to enable the MIP MPEC heuristic.
                                    -1 (auto): Determine automatically
                                    0 (off): MPEC heuristic is turned off
                                    1 (on): MPEC heuristic is turned on
mip_heuristic_strategy       Specifies the level of effort applied for the MIP heuristic search used to try to find an initial integer feasible point.
                                    -1 (auto): Automatic strategy
                                    0 (none): No heuristics are used
                                    1 (basic): Try basic heuristics
                                    2 (advanced): Try more advanced heuristics
                                    3 (extensive): Try most extensive heuristics
mip_heuristic_terminate      Specifies the condition for terminating the MIP heuristic.
                                    1 (feasible): Terminate at first feasible point
                                    2 (limit): Run heuristic until it hits limit
mip_implications             Whether to add logical implications deduced from branching decisions at a MIP node.
                                    0 (no): Do not add logical implications
                                    1 (yes): Add logical implications
mip_initptfile               Name for the file from which to read the MIP initial point.
mip_integer_tol              This value specifies the threshold for deciding whether or not a variable is determined to be an integer.
mip_integral_gap_abs         Deprecated (use 'mip_opt_gap_abs' option)
mip_integral_gap_rel         Deprecated (use 'mip_opt_gap_rel' option)
mip_intvar_strategy          Specifies how to handle integer variables.
                                    0 (none): No special treatment
                                    1 (relax): Relax integer variables
                                    2 (mpec): Convert to mpec constraints
mip_knapsack                 Specifies rules for adding MIP knapsack cuts.
                                    -1 (auto): Determine automatically
                                    0 (none): Do not add knapsack cuts
                                    1 (root): Add knapsack cuts derived in the root node
                                    2 (tree): Add knapsack cuts in the whole tree
mip_liftproject              Specifies rules for adding lift and project cuts.
                                    -1 (auto): Determine automatically
                                    0 (none): Do not add lift and project cuts
                                    1 (root): Add lift and project cuts at root node
mip_maxnodes                 Specifies the maximum number of nodes explored (0 means no limit).
mip_maxtime_cpu              Deprecated (use 'maxtime' option)
mip_maxtime_real             Deprecated (use 'maxtime' option)
mip_method                   Specifies which MIP method to use.
                                    0 (auto): Let Knitro choose the method
                                    1 (BB): Standard branch and bound
                                    3 (MISQP): Mixed-integer SQP
mip_mir                      Specifies rules for adding mixed-integer rounding (MIR) cuts.
                                    -1 (auto): Automatically determine whether to add MIR cuts
                                    0 (none): Do not add MIR cuts
                                    1 (root): Add MIR cuts derived in the root node
                                    2 (tree): Add MIR cuts in the whole tree
mip_multistart               Use to enable MIP multi-start at the branch-and-bound level.
                                    0 (off): MIP multistart turned off
                                    1 (on): MIP multistart turned on
mip_node_lpalg               Specifies which algorithm to use for standard node LP subproblem solves in MIP (same options as `lp_algorithm` user option).
                                    -1 (auto): Let Knitro automatically decide.
                                    0 (nlp): Use algorithm specified in mip_node_nlpalg.
                                    1 (primalsimplex): Use Primal Simplex algorithm.
                                    2 (dualsimplex): Use Dual Simplex algorithm.
                                    3 (barrier): Use Interior-Point/Barrier algorithm.
                                    4 (pdlp): Use Primal-Dual Linear Programming algorithm.
mip_node_nlpalg              Specifies which algorithm to use for standard node NLP subproblem solves in MIP (same options as `nlp_algorithm` user option).
                                    0 (auto): Let Knitro choose the algorithm
                                    1 (direct): Use Interior (barrier) Direct algorithm
                                    2 (cg): Use Interior (barrier) CG algorithm
                                    3 (active): Use Active Set SLQP algorithm
                                    4 (sqp): Use Active Set SQP algorithm
                                    5 (multi): Run multiple algorithms (deprecated)
                                    6 (al): Use Augmented Lagrangian algorithm
mip_nodealg                  Deprecated (use 'mip_node_nlpalg' option)
mip_numthreads               Number of threads to use for MIP solvers.
mip_opt_gap_abs              The absolute optimality gap stop tolerance for MIP.
mip_opt_gap_rel              The relative optimality gap stop tolerance for MIP.
mip_outinterval              Specifies node printing interval for `mip_outlevel` when `mip_outlevel` > 0.
mip_outlevel                 Specifies how much MIP information to print.
                                    0 (none): Nothing
                                    1 (iters): One line for every node
                                    2 (iterstime): Also print accumulated time every node
                                    3 (root): Also print output from root node relaxation solve
mip_outsub                   Specifies MIP subproblem solve debug output control.
                                    0 (none): Do not print any debug output from subproblem solves.
                                    1 (yes): Subproblem debug output enabled, controlled by option `outlev`.
                                    2 (yesprob): Subproblem debug output enabled and print problem characteristics.
mip_pseudoinit               Specifies the method used to initialize pseudo-costs corresponding to variables that have not yet been branched on in the MIP method.
                                    0 (auto): Let Knitro choose the method
                                    1 (ave): Use average value
                                    2 (strong): Use strong branching
mip_relaxable                Specifies whether integer variables are relaxable.
                                    0 (none): Integer variables not relaxable
                                    1 (all): All integer variables are relaxable
mip_restart                  Specifies whether to enable the MIP restart procedure.
                                    0 (off): MIP restart turned off
                                    1 (on): MIP restart turned on
mip_root_lpalg               Specifies which algorithm to use for root node LP subproblem solves in MIP (same options as `lp_algorithm` user option).
                                    -1 (auto): Let Knitro automatically decide.
                                    0 (nlp): Use algorithm specified in mip_root_nlpalg.
                                    1 (primalsimplex): Use Primal Simplex algorithm.
                                    2 (dualsimplex): Use Dual Simplex algorithm.
                                    3 (barrier): Use Interior-Point/Barrier algorithm.
                                    4 (pdlp): Use Primal-Dual Linear Programming algorithm.
mip_root_nlpalg              Specifies which algorithm to use for root node NLP solves in MIP (same options as `nlp_algorithm` user option).
                                    0 (auto): Let Knitro choose the algorithm
                                    1 (direct): Use Interior (barrier) Direct algorithm
                                    2 (cg): Use Interior (barrier) CG algorithm
                                    3 (active): Use Active Set SLQP algorithm
                                    4 (sqp): Use Active Set SQP algorithm
                                    5 (multi): Run multiple algorithms (deprecated)
                                    6 (al): Use Augmented Lagrangian algorithm
mip_rootalg                  Deprecated (use 'mip_root_nlpalg' option)
mip_rounding                 Specifies the MIP rounding rule to apply.
                                    -1 (auto): Let Knitro choose the rule
                                    0 (none): Do not round if a node is infeasible
                                    2 (heur_only): Round using heuristic only (fast)
                                    3 (nlp_sometimes): Round and solve NLP if likely to succeed
                                    4 (nlp_always): Always round and solve NLP
mip_selectdir                Specifies the MIP node selection direction rule (for tiebreakers) for choosing the next node in the branch-and-bound tree.
                                    0 (down): Choose the less-than node first
                                    1 (up): Choose the greater-than node first
mip_selectrule               Specifies the MIP select rule for choosing the next node in the branch-and-bound tree.
                                    0 (auto): Let Knitro choose the rule
                                    1 (depth_first): Search the tree depth first
                                    2 (best_bound): Node with the best relaxation bound
                                    3 (combo_1): Depth first unless pruned, then best bound
mip_strong_candlim           Specifies the maximum number of candidates to explore for MIP strong branching.
mip_strong_level             Specifies the maximum number of tree levels on which to perform MIP strong branching.
mip_strong_maxit             Specifies the maximum number of iterations to allow for MIP strong branching solves.
mip_sub_maxtime              Specifies the maximum allowable real time in seconds for MIP node subproblems.
mip_terminate                Specifies conditions for terminating the MIP algorithm.
                                    0 (optimal): Terminate at optimum
                                    1 (feasible): Terminate at first integer feasible point
mip_zerohalf                 Specifies rules for adding zero-half cuts.
                                    -1 (auto): Determine automatically
                                    0 (none): Do not add zero-half cuts
                                    1 (root): Add cuts derived in the root node
                                    2 (tree): Add zero-half cuts in the whole tree
ms_enable                    Whether to enable multistart to find a better local minimum.
                                    0 (no): Knitro solves from a single initial point
                                    1 (yes): Knitro solves using multiple start points
ms_initpt_cluster            The strategy for clustering initial points in multi-start.
                                    0 (none): Do not apply clustering
                                    1 (sl): Apply single linkage based clustering
ms_maxbndrange               Specifies the maximum range that an unbounded variable can vary over when multistart computes new start points.
ms_maxsolves                 How many Knitro solutions to compute if multistart is enabled.
ms_maxtime_cpu               Deprecated (use 'maxtime' option)
ms_maxtime_real              Deprecated (use 'maxtime' option)
ms_num_to_save               How many feasible multistart points to save in file `knitro_mspoints.log`.
ms_numthreads                Number of threads to use in parallel multistart.
ms_outsub                    Enable writing algorithm output to files for the parallel multi-start procedure.
                                    0 (none): No output from subproblem solves
                                    1 (yes): Subproblem output enabled, controlled by option `outlev`.
ms_savetol                   Specifies the tolerance for deciding two feasible points are the same.
ms_seed                      Seed value used to generate random initial points in multi-start; should be a non-negative integer.
ms_startptrange              Specifies the maximum range that any variable can vary over when multistart computes new start points.
ms_sub_maxtime               Specifies, in seconds, the maximum allowable real time for multi-start subproblems.
ms_terminate                 Specifies conditions for terminating the multistart procedure.
                                    0 (maxsolves): Terminate after maxsolves
                                    1 (optimal): Terminate at first local optimum
                                    2 (feasible): Terminate at first feasible solution estimate
                                    3 (any): Terminate at first completed solve
                                    4 (rulebased): Terminate when the estimated probability of finding a new local solution is low
ms_terminaterule_tol         The tolerance in `(0,1]` for the rule-based termination of multi-start.
mu                           Deprecated (use 'bar_initmu' option)
multistart                   Deprecated (use 'ms_enable' option)
ncvx_qcqp_init               Specifies the initialization strategy used for non-convex QPs and QCQPs.
                                    -1 (auto): Knitro will automatically determine the strategy.
                                    0 (none): No special initialization strategy is used.
                                    1 (linear): Initialize by solving a linear relaxation.
                                    2 (hybrid): Initialize by solving a hybrid formulation.
                                    3 (penalty): Initialize by solving a penalty formulation.
                                    4 (cvxquad): Initialize by solving a convex quadratic relaxation.
newpoint                     Specifies additional action to take after every iteration in a solve of a continuous problem, or after every new incumbent of the NLPBB algorithm.
                                    0 (none): No additional action
                                    1 (saveone): Save the latest new point to file `knitro_newpoint.knsol`. Previous contents of the file are overwritten.
                                    2 (saveall): Export one file per iteration with the new point, named `knitro_newpoint_#.knsol` where `#` is the iteration number.
nlp_algorithm                Indicates which algorithm to use to solve nonlinear problems (e.g. NLPs, QPs, QCQPs)
                                    0 (auto): Let Knitro choose the algorithm
                                    1 (direct): Use Interior (barrier) Direct algorithm
                                    2 (cg): Use Interior (barrier) CG algorithm
                                    3 (active): Use Active Set SLQP algorithm
                                    4 (sqp): Use Active Set SQP algorithm
                                    5 (multi): Run multiple algorithms (perhaps in parallel)
                                    6 (al): Use Augmented Lagrangian algorithm
numthreads                   Specify the number of threads to use for parallel computing features.
objno                        objective number: 0 = none, 1 = first (default),
                               2 = second (if _nobjs > 1), etc.
objrange                     Specifies the extreme limits of the objective function for purposes of determining unboundedness.
objrep                       Whether to replace
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
optionsfile                  Name/location of Knitro options file if provided
opttol                       Specifies the final relative stopping tolerance for the KKT (optimality) error.
opttol_abs                   Specifies the final absolute stopping tolerance for the KKT (optimality) error.
opttolabs                    Deprecated (use 'opttol_abs' option)
out_csvinfo                  Controls whether or not to generate a file `knitro_solve.csv` containing solve information in comma separated format.
                                    0 (no): No csv solution file is generated
                                    1 (yes): Generate a solution file `knitro_solve.csv`
out_csvname                  Use to specify a custom csv filename when using `out_csvinfo`.
out_hints                    Specifies whether to print diagnostic hints (e.g. about user option settings) after solving.
                                    0 (no): Do not print any hints.
                                    1 (yes): Print diagnostic hints on occasion.
outappend                    Specifies whether output should be started in a new file, or appended to existing files.
                                    0 (no): Erase existing files when opening
                                    1 (yes): Append to existing files
outdir                       Specifies a single directory as the location to write all output files.
outlev                       Controls the level of output produced by Knitro.
                                    0 (none): Printing of all output is suppressed
                                    1 (summary): Print only summary information
                                    2 (iter_10): Print basic information every 10 iterations
                                    3 (iter): Print basic information at each iteration
                                    4 (iter_verbose): Print basic information and the function count at each iteration
                                    5 (iter_x): Print all the above, and the values of the solution vector `x`
                                    6 (all): Print all the above, and the values of the constraints `c` at `x` and the Lagrange multipliers lambda
outmode                      Specifies where to direct the output from Knitro.
                                    0 (screen): Directed to standard output (stdout)
                                    1 (file): Directed to a file (default name `knitro.log`, see option `outname`)
                                    2 (both): Both standard output and file
outname                      Use to specify a custom filename when output is written to a file using `outmode`.
par_blasnumthreads           Deprecated (use 'blas_numthreads' option)
par_concurrent_evals         Deprecated (use 'concurrent_evals' option)
par_conicnumthreads          Deprecated (use 'conic_numthreads' option)
par_lsnumthreads             Deprecated (use 'linsolver_numthreads' option)
par_msnumthreads             Deprecated (use 'ms_numthreads' option)
par_numthreads               Deprecated (use 'numthreads' option)
pivot                        Deprecated (use 'linsolver_pivottol' option)
presolve                     Determine whether or not to use the Knitro presolver to try to simplify the model by removing variables or constraints.
                                    0 (no): No presolve
                                    1 (yes): Knitro performs presolve
presolve_initpt              Control whether the Knitro presolver can shift a user-supplied initial point.
                                    -1 (auto): Determine automatically
                                    0 (noshift): Do not shift initial point in presolve
                                    1 (linshift): Allow shifting variables in linear constraints
                                    2 (anyshift): Allow shifting any variable
presolve_level               Set the level of presolve operations to enable through the Knitro presolver.
                                    -1 (auto): Determine automatically
                                    1 (level1): Most basic presolve
                                    2 (level2): More advanced presolve
presolve_passes              Set a maximum limit on the number of passes through the Knitro presolve operations.
presolve_tol                 Determines the tolerance used by the Knitro presolver to remove variables and constraints from the model.
presolve_zero_tol            Tolerance for rounding to zero linear coefficients in presolve. Higher values mean that more reductions will be applied. Zero value is not recommended as it means no rounding is done, which can lead to numerical instability.
presolveop_clique_merging    Determine whether or not to enable the Knitro presolve operations that attempt to merge cliques to strengthen the formulation.
                                    -1 (auto): Determine automatically
                                    0 (no): Disabled
                                    1 (yes): Enabled
presolveop_implied_mpec      Transforms quadratic constraints into MPEC constraints.
                                    0 (no): Disabled
                                    1 (yes): Enabled
presolveop_probing           Determine whether or not to enable the Knitro presolve operations that analyze deductions made by fixing integer variables.
                                    -1 (auto): Automatic selection
                                    0 (no): Disabled
                                    1 (light): Light probing
                                    2 (full): Full probing until no more deductions are found
presolveop_redundant         Determine whether or not to enable the Knitro presolve operation to detect and remove redundant constraints.
                                    0 (none): Do not detect redundant constraints
                                    1 (dupcon): Detect and remove duplicate constraints
                                    2 (depcon): Detect and remove linearly dependent constraints
presolveop_substitution      Determine whether or not to enable the Knitro presolve operation to substitute out variables when possible.
                                    -1 (auto): Automatic substitution procedure
                                    0 (none): No substitution
                                    1 (simple): Only doubleton equality substitutions
                                    2 (all): All possible substitutions
presolveop_substitution_tol  Tolerance for applying a substitution.
presolveop_tighten           Determine whether or not to enable the Knitro presolve operation to tighten variable bounds or coefficients.
                                    -1 (auto): Automatic tightening procedure
                                    0 (none): No tightening
                                    1 (varbnd): Tighten variable bounds
qpcheck                      whether to check for a QP: deprecated
relax                        whether to ignore integrality: 0 (default) = no, 1 = yes
restarts                     Specifies whether or not to enable automatic restarts in Knitro.
restarts_maxit               When restarts are enabled, this option can be used to specify a maximum number of iterations before enforcing a restart.
scale                        Specifies whether to perform problem scaling of the objective function, constraint functions, or possibly variables.
                                    0 (no): No scaling done
                                    1 (user_internal): User, if defined, otherwise internal
                                    2 (user_none): User, if defined, otherwise none
                                    3 (internal): Knitro performs internal scaling
scale_strategy               Strategies for problem scaling. Multiple strategies can be selected at once using multiple bits.
                                    0 (auto): Let Knitro choose the scaling strategy. Use option `scale` for fully disabling scaling.
                                    1 (cons): Apply constraint scaling.
                                    2 (vars): Apply variable scaling.
                                    4 (obj): Apply objective scaling.
                                    8 (equilibration): Apply Equilibration scaling. If enabled, `curtisreid` and `ruizpock` bits are ignored.
                                    16 (curtisreid): Apply Curtis-Reid scaling.
                                    32 (ruizpock): Apply Ruiz and Pock scalings.
                                    64 (geomean): Use geometric mean in scaling computation rather than the infinity norm.
                                    128 (varscaling_bounds): Apply variable scaling based on bounds. If disabled, the strategy given by the previous three bits is applied for variable scaling.
                                    256 (scaling_up): Allow scaling factors larger than one.
                                    512 (poweroftwo): Force scaling factors to be powers of two.
                                    1024 (repeat): Allow scaling factor computation in a loop.
                                    2048 (dynamic): Allow dynamic scaling (only for NLPs).
soc                          Specifies whether or not to try second order corrections (SOC).
                                    0 (no): Never do second order corrections
                                    1 (maybe): SOC steps attempted on some iterations
                                    2 (yes): SOC steps always attempted when constraints are nonlinear
soltype                      This option specifies the solution returned by Knitro.
                                    0 (final): Return the final iterate
                                    1 (bestfeas): Return the best feasible iterate found
sph_opts                     Sparse Hessian options (bits)
storequadcoefs               Store quadratic coefficients when solving QCQPs
strat_warm_start             Specifies whether or not to invoke a warm-start strategy.
                                    0 (no): No warm-start strategy is applied.
                                    1 (yes): Knitro will apply a warm-start strategy with special tunings.
threads                      Deprecated (use 'numthreads' option)
timing                       Whether to report problem I/O and solve times:
                             0 (default) = no
                             1 = yes, on stdout
                             2 = yes, on stderr
                             3 = yes, on both stdout and stderr
tuner                        Indicates whether to invoke the Knitro-Tuner.
                                    0 (off): Knitro Tuner turned off
                                    1 (on): Knitro Tuner enabled
tuner_maxtime_cpu            Deprecated (use 'maxtime' option)
tuner_maxtime_real           Deprecated (use 'maxtime' option)
tuner_optionsfile            Can be used to specify the location of a Tuner options file.
tuner_outsub                 Enable writing additional Tuner subproblem solve output to files for the Knitro-Tuner procedure (`tuner` = `1`).
                                    0 (none): No output from subproblem solves and no subproblem summary file
                                    1 (summary): Subproblem output summary directed to a file `knitro_tuner_summary.log`
                                    2 (all): Subproblem output enabled, controlled by option `outlev`.
tuner_sub_maxtime            Specifies, in seconds, the maximum allowable real time for Knitro-Tuner subproblems (i.e. individual solves with a particular option setting).
tuner_terminate              Define the termination condition for the Knitro-Tuner procedure (`tuner` = `1`).
                                    0 (all): Terminate after all Tuner runs complete
                                    1 (optimal): Terminate at first local optimum
                                    2 (feasible): Terminate at first feasible solution estimate
                                    3 (any): Terminate at first completed solve
use_asl                      If 1, use AMPL ASL for nonlinear evaluations. If 0, use Knitro nl modeler
version                      Report software version
wantsol                      Solution report without -AMPL: sum of
                             1 ==> write .sol file
                             2 ==> 1 ==> write .sol file
                             4 ==> print dual variable values
                             8 ==> do not print solution message
xpresslibname                See option `act_lpsolver`.
xtol                         Tolerance for convergence criterion based on relative change between successive solution points.
xtol_iters                   Number of iterations for convergence criterion based on relative change between successive solution points.
```

