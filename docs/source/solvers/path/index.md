# PATH

Solver path solvers "square" nonlinear complementarity problem;
it is based on the PATH solver of Professor Michael C. Ferris and
his (current or former) students Steven P. Dirkse and Todd S. Munson.

## License setup

To setup a license see:
	https://pages.cs.wisc.edu/~ferris/path/LICENSE

Note that further to the methods shown in the page, the license string
can also be passed as a solver option from AMPL via:

option path_options "license=LicenseStringFoundOnThePageAbove";

## References

Papers related to PATH include

S. P. Dirkse, "Robust Solution of Mixed Complementarity Problems",
	Ph.D. thesis, Computer Sciences Dept., Univ. of Wisconsin,
	Madison, 1994.  Available from
	ftp://ftp.cs.wisc.edu/math-prog/tech-reports/.

Steven P. Dirkse and Michael C. Ferris, "The PATH Solver: A
	Non-Monotone Stabilization Scheme for Mixed Complementarity
	Problems", Optimization Methods and Software 5 (1995),
	pp. 123-156.

M. C. Ferris and T. S. Munson, "Interfaces to PATH 3.0: Design,
	Implementation and Usage", Math. Prog. Tech. Rep. 97-12,
	Univ. of Wisconsin, Madison, Computer Sciences Dept., 1997.
	Available from ftp://ftp.cs.wisc.edu/math-prog/tech-reports/.

Pointers to other relevant papers appear in
	http://www.cs.wisc.edu/~ferris/papers.html


## solve_result_num values

Here is a table of solve_result_num values that "path" can return
to an AMPL session, along with the text that appears in the associated
solve_message.

```
	Value	Message

	0	Solution found
	200	Inconsistent bounds
	201	Infeasible
	400	Major iteration limit
	401	Cumulative iteration limit
	402	Time limit
	403	User interrupt (such as control-C)
	500	Bug -- unexpected return code from PATH
	501	Solver error
	503	Domain error
	504	Nonsquare system (when "sqwarn" requires square)
	505	Problem has side inequalities (when "sideineq" allows none)
	510	Not enough progress
```

## Solver options

Full list of solver options:
```{toctree}
options.md
```

## Changelog

```{toctree}
changes.md
```