
# Lindo Global Options

Obtained with `$ lindoglobal -=`.

```
epsa           Absolute convergence tolerance (default 1e-6).
epsr           Relative convergence tolerance (default 1e-5).
maxtime        Maximum CPU seconds allowed (default -1, means no limit).
outlev         Whether to chatter: 0 ==> no(default), 1 ==> yes.
threadingmode  Threading mode for solvers with multithreading support:
		   -1 = solver decides (default)
		    0 = try parallel mode, if not available try concurrent mode
		    1 = force parallel mode
		    2 = try concurrent mode, if not available try parallel mode
		    3 = force concurrent mode.
threads        Number of threads to be used (default -1, uses solver default).
wantsol        Solution report without -AMPL: sum of
		1 ==> write .sol file
		2 ==> print primal variable values
		4 ==> print dual variable values
		8 ==> do not print solution message

```

