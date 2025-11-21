
# CONOPT Options

```ampl
ampl: option solver conopt; # change the solver
ampl: option conopt_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

Solver options obtained with `$ conopt -=`.

```
debug             when to use finite differences to check derivatives:
		      0 (default) ==> never
		     -1 ==> only at the starting point
		    > 0 ==> each that many iterations
debug2d           when to use finite differences to check the Lagrangian Hessian:
		      0 (default) ==> never
		     -1 ==> only at the starting point
		    > 0 ==> each that many iterations.
errlim            evaluation-error limit (default 500)
flg_adjinip       adjust initial point (0/1*)
flg_convex        convex model flag (0*/1)
flg_crash_slack   preselect slacks for initial basis (0*/1)
flg_dbg_intv      debug interval evaluations (0*/1)
flg_fordefc       force definitional constraints on (0*/1)
hess              whether to use the Hessian:
		    0 = no
		    1 = yes: just the explicit Hessian
		    2 = yes: just Hessian-vector products
		    3 = yes (default) both explicit and Hessian-vector products
		   -1 = no, but evaluate gradients as for
		        Hessian computations (debug option).
iterlim           iteration limit (default 1000000)
licshow           show license details
lim_err_2ddir     limit on directional 2nd-derivative errors (int, default 10)
lim_err_fnc_drv   limit on function evaluation errors (int, default gams domlim)
lim_err_hessian   limit on hessian evaluation errors (int, default 10)
lim_iteration     synonym for iterlimit
lim_msg_large     Limit on number of error messages related to large function value and Jacobian elements (int, default 10)
lim_newsuper      max new superbasic vars per iteration (int, default auto)
lim_pre_msg       Limit on number of error messages related to infeasible pre-triangle (int, default 25)
lim_redhess       max superbasic vars in reduced hessian approx (int, default auto)
lim_slowprg       iterations with slow progress limit (int, default 20)
lim_stalliter     stalled iterations limit (int, default 100)
lim_start_degen   degenerate iterations before degen-breaking (int, default 100)
lim_time          synonym for maxtime
lim_variable      upper bound on solution/activities (double, default 1.e15)
lin_method        method for linear feasibility models (int, default 1)
logfreq           frequency of log lines when outlev = 3
maxftime          time limit (default 999999 seconds)
maxfwd            max vars in fwd AD of common exprs (default 5)
maximize          maximize the objective (no matter what the model says)
maxiter           synonymn for iterlim
minimize          minimize the objective (no matter what the model says)
mtd_dbg_1drv      method for function/derivative debugger (int, default 0)
mtd_redhess       init diagonal of approx reduced hessian (int, default 0)
mtd_scale         scaling method (int, default 3)
mtd_step_phase0   step method in phase 0 (int, default -1)
mtd_step_tight    max step while tightening tolerances (int, default 0)
num_rounds        number of rounds with linear feasibility model (int, default 4)
objno             objective number: 0 = none, 1 = first (default)
outlev            output level:
		    0 no chatter.
		    1 = options but no iteration log on stdout (default).
		    2 = CONOPT "SCREEN" output on stdout.
		    3 = log line every logfreq iterations.
		    4 = also show preprocessing information.
rat_nopen         ratio limit of penalty constraints for no-penalty model (double, default 0.1)
superbasics       limit on number of superbasic variables (default >= 500)
threads           maximum number of threads to use. Override specific threads settings
		  with options threads_2d and threads_fd (default=0, automatic)
threads_2d        maximum number of threads to use for second derivative evaluations
threads_fd        maximum number of threads to use for function and derivative evaluations
timing            report I/O and solution times: 1 = stdout, 2 = stderr, 3 = both
tol_bound         bound filter tolerance (double, default 1e-07)
tol_box_linfac    trust-region box factor for linear vars (double, default 10)
tol_boxsize       initial trust-region box size (double, default 10)
tol_boxsize_lin   initial box size for linear feasibility model (double, default 1000)
tol_def_mult      max growth in definitional constraints block (double, default 1.e4)
tol_feas_max      max feasibility tolerance (double, default 1e-07)
tol_feas_min      min feasibility tolerance (double, default 4e-10)
tol_feas_tria     feasibility tol for triangular eqs (double, default 1e-08)
tol_fixed         tol to treat vars as fixed (double, default 4e-10)
tol_jac_min       filter for small jacobian elements (double, default 1e-05)
tol_linesearch    1-D line search accuracy (double, default 0.2)
tol_obj_acc       relative objective accuracy (double, default 3e-13)
tol_obj_change    relative objective change threshold (double, default 3e-12)
tol_opt_infeas    optimality tol when infeasible (double, default 1e-07)
tol_opt_linf      optimality tol in linear feasibility model (double, default 1e-10)
tol_optimality    optimality tolerance when feasible (double, default 1e-07)
tol_piv_abs       absolute pivot tolerance (double, default 1e-10)
tol_piv_abs_ini   abs pivot tol for initial basis (double, default 1e-07)
tol_piv_abs_nltr  abs pivot tol for NL terms in pre-triangular eqs (double, default 1e-05)
tol_piv_ratio     relative pivot tol during ratio test (double, default 1e-08)
tol_piv_rel       relative pivot tol in factorizations (double, default 0.05)
tol_piv_rel_ini   relative pivot tol for initial basis (double, default 0.001)
tol_piv_rel_updt  relative pivot tol during updates (double, default 0.05)
tol_scale_max     upper bound on scale factors (double, default 1.e25)
tol_scale_min     lower bound for scale factors (double, default 1)
tol_scale_var     lower bound on x in x*Jac for scaling (double, default 1e-05)
tol_zero          zero filter for Jacobian/echelon results (double, default 1e-20)
trace_minstep     minimum step between reinversions in tracecns (double, default 0.001)
version           report version
wantsol           solution report without -AMPL: sum of
		1 ==> write .sol file
		2 ==> print primal variable values
		4 ==> print dual variable values
		8 ==> do not print solution message
```

