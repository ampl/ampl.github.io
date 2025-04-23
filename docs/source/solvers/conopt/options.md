
# CONOPT Options

```ampl
ampl: option solver conopt; # change the solver
ampl: option conopt_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

Solver options obtained with `$ conopt -=`.

```
debug        when to use finite differences to check derivatives:
		0 (default) ==> never;
		-1 ==> only at the starting point;
		> 0 ==> each that many iterations.
debug2d      when to use finite differences to check the Lagrangian Hessian:
		0 (default) ==> never;
		-1 ==> only at the starting point;
		> 0 ==> each that many iterations.
errlim       evaluation-error limit (default 500)
hess         whether to use the Hessian:
		0 = no,
		1 = yes: just the explicit Hessian,
		2 = yes: just Hessian-vector products,
		3 = yes (default) both explicit and Hessian-vector products,
		-1 = no, but evaluate gradients as for
			Hessian computations (debug option).
iterlim      iteration limit (default 1000000)
licshow      show license details
logfreq      frequency of log lines when outlev = 3
maxftime     time limit (default 999999 seconds)
maxfwd       max vars in fwd AD of common exprs (default 5)
maximize     maximize the objective (no matter what the model says)
maxiter      synonymn for iterlim
minimize     minimize the objective (no matter what the model says)
objno        objective number: 0 = none, 1 = first (default)
outlev       output level:
		0 no chatter.
		1 = options but no iteration log on stdout (default).
		2 = CONOPT "SCREEN" output on stdout.
		3 = log line every logfreq iterations.
		4 = also show preprocessing information.
superbasics  limit on number of superbasic variables (default >= 500)
timing       report I/O and solution times: 1 = stdout, 2 = stderr, 3 = both
version      report version
wantsol      solution report without -AMPL: sum of
		1 ==> write .sol file
		2 ==> print primal variable values
		4 ==> print dual variable values
		8 ==> do not print solution message
```

