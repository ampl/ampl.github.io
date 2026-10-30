
# IPOPT Options

```ampl
ampl: option solver ipopt; # change the solver
ampl: option ipopt_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

Solver options obtained with `$ ipopt -=`.

```
accept_after_max_steps                Accept a trial point after maximal this number of steps even if it does not satisfy line search conditions.
accept_every_trial_step               Always accept the first trial step.
acceptable_compl_inf_tol              "Acceptance" threshold for the complementarity conditions.
acceptable_constr_viol_tol            "Acceptance" threshold for the constraint violation.
acceptable_dual_inf_tol               "Acceptance" threshold for the dual infeasibility.
acceptable_iter                       Number of "acceptable" iterates before triggering termination.
acceptable_obj_change_tol             "Acceptance" stopping criterion based on objective function change.
acceptable_tol                        "Acceptable" convergence tolerance (relative).
adaptive_mu_globalization             Globalization strategy for the adaptive mu selection mode.
adaptive_mu_kkt_norm_type             Norm used for the KKT error in the adaptive mu globalization strategies.
adaptive_mu_kkterror_red_fact         Sufficient decrease factor for "kkt-error" globalization strategy.
adaptive_mu_kkterror_red_iters        Maximum number of iterations requiring sufficient progress.
adaptive_mu_monotone_init_factor      Determines the initial value of the barrier parameter when switching to the monotone mode.
adaptive_mu_restore_previous_iterate  Indicates if the previous accepted iterate should be restored if the monotone mode is entered.
adaptive_mu_safeguard_factor          
alpha_for_y                           Method to determine the step size for constraint multipliers (alpha_y) .
alpha_for_y_tol                       Tolerance for switching to full equality multiplier steps.
alpha_min_frac                        Safety factor for the minimal step size (before switching to restoration phase).
alpha_red_factor                      Fractional reduction of the trial step size in the backtracking line search.
barrier_tol_factor                    Factor for mu in barrier stop test.
bound_frac                            Desired minimum relative distance from the initial point to bound.
bound_mult_init_method                Initialization method for bound multipliers
bound_mult_init_val                   Initial value for the bound multipliers.
bound_mult_reset_threshold            Threshold for resetting bound multipliers after the restoration phase.
bound_push                            Desired minimum absolute distance from the initial point to bound.
bound_relax_factor                    Factor for initial relaxation of the bounds.
check_derivatives_for_naninf          Indicates whether it is desired to check for Nan/Inf in derivative matrices
chi_cup                               
chi_hat                               
chi_tilde                             
compl_inf_tol                         Desired threshold for the complementarity conditions.
constr_mult_init_max                  Maximum allowed least-square guess of constraint multipliers.
constr_mult_reset_threshold           Threshold for resetting equality and inequality multipliers after restoration phase.
constr_viol_tol                       Desired threshold for the constraint and variable bound violation.
constraint_violation_norm_type        Norm to be used for the constraint violation in the line search.
corrector_compl_avrg_red_fact         Complementarity tolerance factor for accepting corrector step.
corrector_type                        The type of corrector steps that should be taken.
delta                                 Multiplier for constraint violation in the switching rule.
delta_y_max                           a parameter used to check if the fast direction can be used as the line search direction (for Chen-Goldfarb line search).
dependency_detection_with_rhs         Indicates if the right hand sides of the constraints should be considered in addition to gradients during dependency detection
dependency_detector                   Indicates which linear solver should be used to detect linearly dependent equality constraints.
derivative_test                       Enable derivative checker
derivative_test_first_index           Index of first quantity to be checked by derivative checker
derivative_test_perturbation          Size of the finite difference perturbation in derivative test.
derivative_test_print_all             Indicates whether information for all estimated derivatives should be printed.
derivative_test_tol                   Threshold for indicating wrong derivative.
diverging_iterates_tol                Threshold for maximal value of primal iterates.
dual_inf_tol                          Desired threshold for the dual infeasibility.
epsilon_c                             
eta_min                               
eta_penalty                           Relaxation factor in the Armijo condition for the penalty function.
eta_phi                               Relaxation factor in the Armijo condition.
evaluate_orig_obj_at_resto_trial      Determines if the original objective function should be evaluated at restoration phase trial points.
expect_infeasible_problem             Enable heuristics to quickly detect an infeasible problem.
expect_infeasible_problem_ctol        Threshold for disabling "expect_infeasible_problem" option.
expect_infeasible_problem_ytol        Multiplier threshold for activating "expect_infeasible_problem" option.
fast_des_fact                         a parameter used to check if the fast direction can be used as the line search direction (for Chen-Goldfarb line search).
fast_step_computation                 Indicates if the linear system should be solved quickly.
file_append                           Whether to append to output file, if set, instead of truncating.
file_print_level                      Verbosity level for output file.
filter_margin_fact                    Factor determining width of margin for obj-constr-filter adaptive globalization strategy.
filter_max_margin                     Maximum width of margin in obj-constr-filter adaptive globalization strategy.
filter_reset_trigger                  Number of iterations that trigger the filter reset.
findiff_perturbation                  Size of the finite difference perturbation for derivative approximation.
first_hessian_perturbation            Size of first x-s perturbation tried.
fixed_mu_oracle                       Oracle for the barrier parameter when switching to fixed mode.
fixed_variable_treatment              Determines how fixed variables should be handled.
gamma_hat                             
gamma_phi                             Relaxation factor in the filter margin for the barrier function.
gamma_theta                           Relaxation factor in the filter margin for the constraint violation.
gamma_tilde                           
grad_f_constant                       Indicates whether to assume that the objective function is linear
gradient_approximation                Specifies technique to compute objective Gradient
halt_on_ampl_error                    Exit with message on evaluation error
hessian_approximation                 Indicates what Hessian information is to be used.
hessian_approximation_space           Indicates in which subspace the Hessian information is to be approximated.
hessian_constant                      Indicates whether to assume the problem is a QP (quadratic objective, linear constraints)
honor_original_bounds                 Indicates whether final points should be projected into original bounds.
inf_pr_output                         Determines what value is printed in the "inf_pr" output column.
jac_c_constant                        Indicates whether to assume that all equality constraints are linear
jac_d_constant                        Indicates whether to assume that all inequality constraints are linear
jacobian_approximation                Specifies technique to compute constraint Jacobian
jacobian_regularization_exponent      Exponent for mu in the regularization for rank-deficient constraint Jacobians.
jacobian_regularization_value         Size of the regularization for rank-deficient constraint Jacobians.
kappa_d                               Weight for linear damping term (to handle one-sided bounds).
kappa_sigma                           Factor limiting the deviation of dual variables from primal estimates.
kappa_soc                             Factor in the sufficient reduction rule for second order correction.
kappa_x_dis                           a parameter used to check if the fast direction can be used as the line search direction (for Chen-Goldfarb line search).
kappa_y_dis                           a parameter used to check if the fast direction can be used as the line search direction (for Chen-Goldfarb line search).
least_square_init_duals               Least square initialization of all dual variables
least_square_init_primal              Least square initialization of the primal variables
limited_memory_aug_solver             Strategy for solving the augmented system for low-rank Hessian.
limited_memory_init_val               Value for B0 in low-rank update.
limited_memory_init_val_max           Upper bound on value for B0 in low-rank update.
limited_memory_init_val_min           Lower bound on value for B0 in low-rank update.
limited_memory_initialization         Initialization strategy for the limited memory quasi-Newton approximation.
limited_memory_max_history            Maximum size of the history for the limited quasi-Newton Hessian approximation.
limited_memory_max_skipping           Threshold for successive iterations where update is skipped.
limited_memory_special_for_resto      Determines if the quasi-Newton updates should be special during the restoration phase.
limited_memory_update_type            Quasi-Newton update formula for the limited memory quasi-Newton approximation.
line_search_method                    Globalization method used in backtracking line search
linear_scaling_on_demand              Flag indicating that linear scaling is only done if it seems required.
linear_solver                         Linear solver used for step computations.
linear_system_scaling                 Method for scaling the linear system.
magic_steps                           Enables magic steps.
max_cpu_time                          Maximum number of CPU seconds.
max_filter_resets                     Maximal allowed number of filter resets
max_hessian_perturbation              Maximum value of regularization parameter for handling negative curvature.
max_iter                              Maximum number of iterations.
max_refinement_steps                  Maximum number of iterative refinement steps per linear system solve.
max_resto_iter                        Maximum number of successive iterations in restoration phase.
max_soc                               Maximum number of second order correction trial steps at each iteration.
max_soft_resto_iters                  Maximum number of iterations performed successively in soft restoration phase.
max_wall_time                         Maximum number of walltime clock seconds.
maxit                                 Maximum number of iterations
mehrotra_algorithm                    Indicates whether to do Mehrotra's predictor-corrector algorithm.
min_alpha_primal                      
min_hessian_perturbation              Smallest perturbation of the Hessian block.
min_refinement_steps                  Minimum number of iterative refinement steps per linear system solve.
mu_allow_fast_monotone_decrease       Allow skipping of barrier problem if barrier test is already met.
mu_init                               Initial value for the barrier parameter.
mu_linear_decrease_factor             Determines linear decrease rate of barrier parameter.
mu_max                                Maximum value for barrier parameter.
mu_max_fact                           Factor for initialization of maximum value for barrier parameter.
mu_min                                Minimum value for barrier parameter.
mu_oracle                             Oracle for a new barrier parameter in the adaptive strategy.
mu_strategy                           Update strategy for barrier parameter.
mu_superlinear_decrease_power         Determines superlinear decrease rate of barrier parameter.
mu_target                             Desired value of complementarity.
mult_diverg_feasibility_tol           tolerance for deciding if the multipliers are diverging
mult_diverg_y_tol                     tolerance for deciding if the multipliers are diverging
mumps_dep_tol                         Threshold to consider a pivot at zero in detection of linearly dependent constraints with MUMPS.
mumps_mem_percent                     Percentage increase in the estimated working space for MUMPS.
mumps_mpi_communicator                MPI communicator used for matrix operations
mumps_permuting_scaling               Controls permuting and scaling in MUMPS
mumps_pivot_order                     Controls pivot order in MUMPS
mumps_pivtol                          Pivot tolerance for the linear solver MUMPS.
mumps_pivtolmax                       Maximum pivot tolerance for the linear solver MUMPS.
mumps_print_level                     Debug printing level for the linear solver MUMPS
mumps_scaling                         Controls scaling in MUMPS
neg_curv_test_reg                     Whether to do the curvature test with the primal regularization (see Zavala and Chiang, 2014).
neg_curv_test_tol                     Tolerance for heuristic to ignore wrong inertia.
never_use_fact_cgpen_direction        Toggle to switch off the fast Chen-Goldfarb direction
never_use_piecewise_penalty_ls        Toggle to switch off the piecewise penalty method
nlp_lower_bound_inf                   any bound less or equal this value will be considered -inf (i.e. not lower bounded).
nlp_scaling_constr_target_gradient    Target value for constraint function gradient size.
nlp_scaling_max_gradient              Maximum gradient after NLP scaling.
nlp_scaling_method                    Select the technique used for scaling the NLP.
nlp_scaling_min_value                 Minimum value of gradient-based scaling values.
nlp_scaling_obj_target_gradient       Target value for objective function gradient size.
nlp_upper_bound_inf                   any bound greater or this value will be considered +inf (i.e. not upper bounded).
nu_inc                                Increment of the penalty parameter.
nu_init                               Initial value of the penalty parameter.
num_linear_variables                  Number of linear variables
obj_max_inc                           Determines the upper bound on the acceptable increase of barrier objective function.
obj_scaling_factor                    Scaling factor for the objective function.
option_file_name                      File name of options file.
outlev                                Verbosity level
output_file                           File name of desired output file (leave unset for no file output).
pardisolib                            Name of library containing Pardiso routines (from pardiso-project.org) for load at runtime
pen_des_fact                          a parameter used in penalty parameter computation (for Chen-Goldfarb line search).
pen_init_fac                          a parameter used to choose initial penalty parameters when the regularized Newton method is used.
pen_theta_max_fact                    Determines upper bound for constraint violation in the filter.
penalty_init_max                      Maximal value for the initial penalty parameter (for Chen-Goldfarb line search).
penalty_init_min                      Minimal value for the initial penalty parameter for line search (for Chen-Goldfarb line search).
penalty_max                           Maximal value for the penalty parameter (for Chen-Goldfarb line search).
penalty_update_compl_tol              
penalty_update_infeasibility_tol      Threshold for infeasibility in penalty parameter update test.
perturb_always_cd                     Active permanent perturbation of constraint linearization.
perturb_dec_fact                      Decrease factor for x-s perturbation.
perturb_inc_fact                      Increase factor for x-s perturbation.
perturb_inc_fact_first                Increase factor for x-s perturbation for very first perturbation.
piecewisepenalty_gamma_infeasi        
piecewisepenalty_gamma_obj            
point_perturbation_radius             Maximal perturbation of an evaluation point.
print_advanced_options                whether to print also advanced options
print_frequency_iter                  Determines at which iteration frequency the summarizing iteration output line should be printed.
print_frequency_time                  Determines at which time frequency the summarizing iteration output line should be printed.
print_info_string                     Enables printing of additional info string at end of iteration output.
print_level                           Output verbosity level.
print_options_documentation           Switch to print all algorithmic options with some documentation before solving the optimization problem.
print_options_mode                    format in which to print options documentation
print_timing_statistics               Switch to print timing statistics.
print_user_options                    Print all options set by the user.
quality_function_balancing_term       The balancing term included in the quality function for centrality.
quality_function_centrality           The penalty term for centrality that is included in quality function.
quality_function_max_section_steps    Maximum number of search steps during direct search procedure determining the optimal centering parameter.
quality_function_norm_type            Norm used for components of the quality function.
quality_function_section_qf_tol       Tolerance for the golden section search procedure determining the optimal centering parameter (in the function value space).
quality_function_section_sigma_tol    Tolerance for the section search procedure determining the optimal centering parameter (in sigma space).
recalc_y                              Tells the algorithm to recalculate the equality and inequality multipliers as least square estimates.
recalc_y_feas_tol                     Feasibility threshold for recomputation of multipliers.
replace_bounds                        Whether all variable bounds should be replaced by inequality constraints
required_infeasibility_reduction      Required reduction of infeasibility before leaving restoration phase.
residual_improvement_factor           Minimal required reduction of residual test ratio in iterative refinement.
residual_ratio_max                    Iterative refinement tolerance
residual_ratio_singular               Threshold for declaring linear system singular after failed iterative refinement.
resto_failure_feasibility_threshold   Threshold for primal infeasibility to declare failure of restoration phase.
resto_penalty_parameter               Penalty parameter in the restoration phase objective function.
resto_proximity_weight                Weighting factor for the proximity term in restoration phase objective.
rho                                   Value in penalty parameter update formula.
s_max                                 Scaling threshold for the NLP error.
s_phi                                 Exponent for linear barrier function model in the switching rule.
s_theta                               Exponent for current constraint violation in the switching rule.
sb                                    whether to skip printing Ipopt copyright banner
sigma_max                             Maximum value of the centering parameter.
sigma_min                             Minimum value of the centering parameter.
skip_corr_if_neg_curv                 Whether to skip the corrector step in negative curvature iteration.
skip_corr_in_monotone_mode            Whether to skip the corrector step during monotone barrier parameter mode.
skip_finalize_solution_call           Whether a call to NLP::FinalizeSolution after optimization should be suppressed
slack_bound_frac                      Desired minimum relative distance from the initial slack to bound.
slack_bound_push                      Desired minimum absolute distance from the initial slack to bound.
slack_move                            Correction size for very small slacks.
soc_method                            Ways to apply second order correction
soft_resto_pderror_reduction_factor   Required reduction in primal-dual error in the soft restoration phase.
start_with_resto                      Whether to switch to restoration phase in first iteration.
suppress_all_output                   
tau_min                               Lower bound on fraction-to-the-boundary parameter tau.
theta_max_fact                        Determines upper bound for constraint violation in the filter.
theta_min                             
theta_min_fact                        Determines constraint violation threshold in the switching rule.
timing_statistics                     Indicates whether to measure time spend in components of Ipopt and NLP evaluation
tiny_step_tol                         Tolerance for detecting numerically insignificant steps.
tiny_step_y_tol                       Tolerance for quitting because of numerically insignificant steps.
tol                                   Desired convergence tolerance (relative).
vartheta                              a parameter used to check if the fast direction can be used as the line search direction (for Chen-Goldfarb line search).
wantsol                               solution report without -AMPL: sum of 1 (write .sol file), 2 (print primal variable values), 4 (print dual variable values), 8 (do not print solution message)
warm_start_bound_frac                 same as bound_frac for the regular initializer
warm_start_bound_push                 same as bound_push for the regular initializer
warm_start_entire_iterate             Tells algorithm whether to use the GetWarmStartIterate method in the NLP.
warm_start_init_point                 Warm-start for initial point
warm_start_mult_bound_push            same as mult_bound_push for the regular initializer
warm_start_mult_init_max              Maximum initial value for the equality multipliers.
warm_start_same_structure             Indicates whether a problem with a structure identical to the previous one is to be solved.
warm_start_slack_bound_frac           same as slack_bound_frac for the regular initializer
warm_start_slack_bound_push           same as slack_bound_push for the regular initializer
warm_start_target_mu                  
watchdog_shortened_iter_trigger       Number of shortened iterations that trigger the watchdog.
watchdog_trial_iter_max               Maximum number of watchdog iterations.
wsmp_iterative                        Switches to use iterative instead of direct solver in WSMP.
```

