
# MINOS Options

Obtained with `$ minos -=`.

```
ftimes   report function eval. times
maxfwd   max vars in fwd AD of common exprs (default 5)
meminc   extra megabytes of memory to give MINOS initially
objno    objective number: 0 = none, 1 = first (default)
objrep   Whether to replace
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
			1 = yes for v >= f(x)
			2 = yes for v == f(x)
			3 = yes in both cases (default)
outlev   output level; 1 = default
timing   report I/O and solution times: 1 = stdout, 2 = stderr, 3 = both
version  report version
wantsol  solution report without -AMPL: sum of
		1 ==> write .sol file
		2 ==> print primal variable values
		4 ==> print dual variable values
		8 ==> do not print solution message

```

