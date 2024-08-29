
# IPOPT Options

```ampl
ampl: option solver ipopt; # change the solver
ampl: option ipopt_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

Solver options obtained with `$ ipopt -=`.

```
acceptable_compl_inf_tol          Acceptance threshold for the complementarity conditions
acceptable_constr_viol_tol        Acceptance threshold for the constraint violation
acceptable_dual_inf_tol           Acceptance threshold for the dual infeasibility
acceptable_tol                    Acceptable convergence tolerance (relative)
alpha_for_y                       Step size for constraint multipliers
bound_frac                        Desired minimal relative distance of initial point to bound
bound_mult_init_val               Initial value for the bound multipliers
bound_push                        Desired minimal absolute distance of initial point to bound
bound_relax_factor                Factor for initial relaxation of the bounds
compl_inf_tol                     Acceptance threshold for the complementarity conditions
constr_mult_init_max              Maximal allowed least-square guess of constraint multipliers
constr_viol_tol                   Desired threshold for the constraint violation
diverging_iterates_tol            Threshold for maximal value of primal iterates
dual_inf_tol                      Desired threshold for the dual infeasibility
expect_infeasible_problem         Enable heuristics to quickly detect an infeasible problem
file_print_level                  Verbosity level for output file
halt_on_ampl_error                Exit with message on evaluation error
hessian_approximation             Can enable Quasi-Newton approximation of hessian
honor_original_bounds             If no, solution might slightly violate bounds
linear_scaling_on_demand          Enables heuristic for scaling only when seems required
linear_solver                     Linear solver to be used for step calculation
linear_system_scaling             Method for scaling the linear systems
ma27_pivtol                       Pivot tolerance for the linear solver MA27
ma27_pivtolmax                    Maximal pivot tolerance for the linear solver MA27
ma57_pivot_order                  Controls pivot order in MA57
ma57_pivtol                       Pivot tolerance for the linear solver MA57
ma57_pivtolmax                    Maximal pivot tolerance for the linear solver MA57
max_cpu_time                      CPU time limit
max_iter                          Maximum number of iterations
max_refinement_steps              Maximal number of iterative refinement steps per linear system solve
max_soc                           Maximal number of second order correction trial steps
maxit                             Maximum number of iterations
min_refinement_steps              Minimum number of iterative refinement steps per linear system solve
mu_init                           Initial value for the barrier parameter
mu_max                            Maximal value for barrier parameter for adaptive strategy
mu_oracle                         Oracle for a new barrier parameter in the adaptive strategy
mu_strategy                       Update strategy for barrier parameter
nlp_scaling_max_gradient          Maximum gradient after scaling
nlp_scaling_method                Select the technique used for scaling the NLP
obj_scaling_factor                Scaling factor for the objective function
option_file_name                  File name of options file (default: ipopt.opt)
outlev                            Verbosity level
output_file                       File name of an output file (leave unset for no file output)
pardiso_matching_strategy         Matching strategy for linear solver Pardiso
print_level                       Verbosity level
print_options_documentation       Print all available options (for ipopt.opt)
print_user_options                Toggle printing of user options
required_infeasibility_reduction  Required infeasibility reduction in restoration phase
slack_bound_frac                  Desired minimal relative distance of initial slack to bound
slack_bound_push                  Desired minimal absolute distance of initial slack to bound
tol                               Desired convergence tolerance (relative)
wantsol                           solution report without -AMPL: sum of
		1 ==> write .sol file
		2 ==> print primal variable values
		4 ==> print dual variable values
		8 ==> do not print solution message
warm_start_bound_push             Enables to specify how much should variables should be pushed inside the feasible region
warm_start_init_point             Enables to specify bound multiplier values
warm_start_mult_bound_push        Enables to specify how much should bound multipliers should be pushed inside the feasible region
watchdog_shortened_iter_trigger   Trigger counter for watchdog procedure
