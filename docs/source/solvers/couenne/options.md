
# COUENNE Options

```ampl
ampl: option solver couenne; # change the solver
ampl: option couenne_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

Solver options obtained with `$ couenne -=`.

```
Couenne 0.5.8 -- an Open-Source solver for Mixed Integer Nonlinear Optimization
Mailing list: couenne@list.coin-or.org
Instructions: http://www.coin-or.org/Couenne
acceptable_compl_inf_tol                       Acceptance threshold for the complementarity conditions
acceptable_constr_viol_tol                     Acceptance threshold for the constraint violation
acceptable_dual_inf_tol                        Acceptance threshold for the dual infeasibility
acceptable_tol                                 Acceptable convergence tolerance (relative)
alpha_for_y                                    Step size for constraint multipliers
bonmin.add_only_violated_oa                    Do we add all OA cuts or only the ones violated by current point?
bonmin.algorithm                               Choice of the algorithm.
bonmin.allowable_fraction_gap                  Specify the value of relative gap under which the algorithm stops.
bonmin.allowable_gap                           Specify the value of absolute gap under which the algorithm stops.
bonmin.bb_log_interval                         Interval at which node level output is printed.
bonmin.bb_log_level                            specify main branch-and-bound log level.
bonmin.candidate_sort_criterion                Choice of the criterion to choose candidates in strong-branching
bonmin.coeff_var_threshold                     Coefficient of variation threshold (for dynamic definition of cutoff_decr).
bonmin.cutoff                                  Specify cutoff value.
bonmin.cutoff_decr                             Specify cutoff decrement.
bonmin.dynamic_def_cutoff_decr                 Do you want to define the parameter cutoff_decr dynamically?
bonmin.enable_dynamic_nlp                      Enable dynamic linear and quadratic rows addition in nlp
bonmin.feasibility_pump_objective_norm         Norm of feasibility pump objective function
bonmin.file_solution                           Write a file bonmin.sol with the solution
bonmin.first_perc_for_cutoff_decr              The percentage used when, the coeff of variance is smaller than the threshold, to compute the cutoff_decr dynamically.
bonmin.heuristic_RINS                          if yes runs the RINS heuristic
bonmin.heuristic_dive_MIP_fractional           if yes runs the Dive MIP Fractional heuristic
bonmin.heuristic_dive_MIP_vectorLength         if yes runs the Dive MIP VectorLength heuristic
bonmin.heuristic_dive_fractional               if yes runs the Dive Fractional heuristic
bonmin.heuristic_dive_vectorLength             if yes runs the Dive VectorLength heuristic
bonmin.heuristic_feasibility_pump              whether the heuristic feasibility pump should be used
bonmin.integer_tolerance                       Set integer tolerance.
bonmin.iteration_limit                         Set the cumulative maximum number of iteration in the algorithm used to process nodes continuous relaxations in the branch-and-bound.
bonmin.lp_log_level                            specify LP log level.
bonmin.max_consecutive_failures                (temporarily removed) Number $n$ of consecutive unsolved problems before aborting a branch of the tree.
bonmin.max_consecutive_infeasible              Number of consecutive infeasible subproblems before aborting a branch.
bonmin.max_random_point_radius                 Set max value r for coordinate of a random point.
bonmin.maxmin_crit_have_sol                    Weight towards minimum in of lower and upper branching estimates when a solution has been found.
bonmin.maxmin_crit_no_sol                      Weight towards minimum in of lower and upper branching estimates when no solution has been found yet.
bonmin.milp_solver                             Choose the subsolver to solve MILP sub-problems in OA decompositions.
bonmin.milp_strategy                           Choose a strategy for MILPs.
bonmin.min_number_strong_branch                Sets minimum number of variables for strong branching (overriding trust)
bonmin.nlp_failure_behavior                    Set the behavior when an NLP or a series of NLP are unsolved by Ipopt (we call unsolved an NLP for which Ipopt is not able to guarantee optimality within the specified tolerances).
bonmin.nlp_log_at_root                         specify a different log level for root relaxation.
bonmin.nlp_log_level                           specify NLP solver interface log level (independent from ipopt print_level).
bonmin.nlp_solver                              Choice of the solver for local optima of continuous NLP's
bonmin.node_comparison                         Choose the node selection strategy.
bonmin.node_limit                              Set the maximum number of nodes explored in the branch-and-bound search.
bonmin.num_cut_passes                          Set the maximum number of cut passes at regular nodes of the branch-and-cut.
bonmin.num_cut_passes_at_root                  Set the maximum number of cut passes at regular nodes of the branch-and-cut.
bonmin.num_iterations_suspect                  Number of iterations over which a node is considered "suspect" (for debugging purposes only, see detailed documentation).
bonmin.num_resolve_at_infeasibles              Number $k$ of tries to resolve an infeasible node (other than the root) of the tree with different starting point.
bonmin.num_resolve_at_node                     Number $k$ of tries to resolve a node (other than the root) of the tree with different starting point.
bonmin.num_resolve_at_root                     Number $k$ of tries to resolve the root node with different starting points.
bonmin.num_retry_unsolved_random_point         Number $k$ of times that the algorithm will try to resolve an unsolved NLP with a random starting point (we call unsolved an NLP for which Ipopt is not able to guarantee optimality within the specified tolerances).
bonmin.number_before_trust                     Set the number of branches on a variable before its pseudo costs are to be believed in dynamic strong branching.
bonmin.number_before_trust_list                Set the number of branches on a variable before its pseudo costs are to be believed during setup of strong branching candidate list.
bonmin.number_look_ahead                       Sets limit of look-ahead strong-branching trials
bonmin.number_strong_branch                    Choose the maximum number of variables considered for strong branching.
bonmin.number_strong_branch_root               Maximum number of variables considered for strong branching in root node.
bonmin.oa_cuts_log_level                       level of log when generating OA cuts.
bonmin.oa_cuts_scope                           Specify if OA cuts added are to be set globally or locally valid
bonmin.oa_rhs_relax                            Value by which to relax OA cut
bonmin.pump_for_minlp                          whether to run the feasibility pump heuristic for MINLP
bonmin.random_generator_seed                   Set seed for random number generator (a value of -1 sets seeds to time since Epoch).
bonmin.random_point_perturbation_interval      Amount by which starting point is perturbed when choosing to pick random point by perturbing starting point
bonmin.random_point_type                       method to choose a random starting point
bonmin.read_solution_file                      Read a file with the optimal solution to test if algorithms cuts it.
bonmin.resolve_on_small_infeasibility          If a locally infeasible problem is infeasible by less than this, resolve it with initial starting point.
bonmin.second_perc_for_cutoff_decr             The percentage used when, the coeff of variance is greater than the threshold, to compute the cutoff_decr dynamically.
bonmin.setup_pseudo_frac                       Proportion of strong branching list that has to be taken from most-integer-infeasible list.
bonmin.solution_limit                          Abort after that much integer feasible solution have been found by algorithm
bonmin.sos_constraints                         Whether or not to activate SOS constraints.
bonmin.time_limit                              Set the global maximum computation time (in secs) for the algorithm.
bonmin.tiny_element                            Value for tiny element in OA cut
bonmin.tree_search_strategy                    Pick a strategy for traversing the tree
bonmin.trust_strong_branching_for_pseudo_cost  Whether or not to trust strong branching results for updating pseudo costs.
bonmin.variable_selection                      Chooses variable selection strategy
bonmin.very_tiny_element                       Value for very tiny element in OA cut
bonmin.warm_start                              Select the warm start method
bound_frac                                     Desired minimal relative distance of initial point to bound
bound_mult_init_val                            Initial value for the bound multipliers
bound_push                                     Desired minimal absolute distance of initial point to bound
bound_relax_factor                             Factor for initial relaxation of the bounds
compl_inf_tol                                  Acceptance threshold for the complementarity conditions
constr_mult_init_max                           Maximal allowed least-square guess of constraint multipliers
constr_viol_tol                                Desired threshold for the constraint violation
diverging_iterates_tol                         Threshold for maximal value of primal iterates
dual_inf_tol                                   Desired threshold for the dual infeasibility
expect_infeasible_problem                      Enable heuristics to quickly detect an infeasible problem
file_print_level                               Verbosity level for output file
halt_on_ampl_error                             Exit with message on evaluation error
hessian_approximation                          Can enable Quasi-Newton approximation of hessian
honor_original_bounds                          If no, solution might slightly violate bounds
linear_scaling_on_demand                       Enables heuristic for scaling only when seems required
linear_solver                                  Linear solver to be used for step calculation
linear_system_scaling                          Method for scaling the linear systems
ma27_pivtol                                    Pivot tolerance for the linear solver MA27
ma27_pivtolmax                                 Maximal pivot tolerance for the linear solver MA27
ma57_pivot_order                               Controls pivot order in MA57
ma57_pivtol                                    Pivot tolerance for the linear solver MA57
ma57_pivtolmax                                 Maximal pivot tolerance for the linear solver MA57
max_cpu_time                                   CPU time limit
max_iter                                       Maximum number of iterations
max_refinement_steps                           Maximal number of iterative refinement steps per linear system solve
max_soc                                        Maximal number of second order correction trial steps
maxit                                          Maximum number of iterations
min_refinement_steps                           Minimum number of iterative refinement steps per linear system solve
mu_init                                        Initial value for the barrier parameter
mu_max                                         Maximal value for barrier parameter for adaptive strategy
mu_oracle                                      Oracle for a new barrier parameter in the adaptive strategy
mu_strategy                                    Update strategy for barrier parameter
nlp_scaling_max_gradient                       Maximum gradient after scaling
nlp_scaling_method                             Select the technique used for scaling the NLP
obj_scaling_factor                             Scaling factor for the objective function
option_file_name                               File name of options file (default: ipopt.opt)
outlev                                         Verbosity level
output_file                                    File name of an output file (leave unset for no file output)
pardiso_matching_strategy                      Matching strategy for linear solver Pardiso
print_level                                    Verbosity level
print_options_documentation                    Print all available options (for ipopt.opt)
print_user_options                             Toggle printing of user options
required_infeasibility_reduction               Required infeasibility reduction in restoration phase
slack_bound_frac                               Desired minimal relative distance of initial slack to bound
slack_bound_push                               Desired minimal absolute distance of initial slack to bound
tol                                            Desired convergence tolerance (relative)
wantsol                                        solution report without -AMPL: sum of
		1 ==> write .sol file
		2 ==> print primal variable values
		4 ==> print dual variable values
		8 ==> do not print solution message
warm_start_bound_push                          Enables to specify how much should variables should be pushed inside the feasible region
warm_start_init_point                          Enables to specify bound multiplier values
warm_start_mult_bound_push                     Enables to specify how much should bound multipliers should be pushed inside the feasible region
watchdog_shortened_iter_trigger                Trigger counter for watchdog procedure
```

