
# Gecode Options

```ampl
ampl: option solver gecode; # change the solver
ampl: option gecode_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

Solver options obtained with `$ gecode -=`.

```
Gecode Options for AMPL
-----------------------

To set these options, assign a string specifying their values to the AMPL
option "gecode_options". For example:

   ampl: option gecode_options 'version nodelimit=30000 val_branching=min';

'' Options:

cp:a_d (a_d)
      Adaptive recomputation distance.

cp:c_d (c_d)
      Commit recomputation distance.

cp:decay (decay)
      Decay factor for AFC and activity branchings. Default = 1.

cp:ipl (ipl)
      Propagation level for integer propagators. Possible values:

      val - value propagation or consistency (naive)
      bnd - bounds propagation or consistency
      dom - domain propagation or consistency
      def - the default propagation for a constraint

cp:restart (restart)
      Restart sequence type. Possible values:

      none      - no restarts
      constant  - restart with constant sequence
      linear    - restart with linear sequence
      luby      - restart with Luby sequence
      geometric - restart with geometric sequence

cp:restart_base (restart_base)
      Base for geometric restart sequence. Default = 1.5.

cp:restart_scale (restart_scale)
      Scale factor for restart sequence. Default = 250.

cp:val_branching (val_branching)
      Value branching. Possible values:

      min        - smallest value (default)
      med        - greatest value not greater than the median
      max        - largest value
      rnd        - random value
      split_min  - values not greater than mean of smallest and largest value
      split_max  - values greater than mean of smallest and largest value
      range_min  - values from smallest range, if domain has several ranges;
                   otherwise, values not greater than mean of smallest and
                   largest value
      range_max  - values from largest range, if domain has several ranges;
                   otherwise, values greater than mean of smallest and largest
                   value
      values_min - all values starting from smallest
      values_max - all values starting from largest

cp:var_branching (var_branching)
      Variable branching. Possible values:

      none            - first unassigned
      rnd             - random
      degree_min      - smallest degree
      degree_max      - largest degree
      afc_min         - smallest accumulated failure count (AFC)
      afc_max         - largest accumulated failure count (AFC)
      action_min      - lowest action
      action_max      - highest action
      min_min         - smallest minimum value
      min_max         - largest minimum value
      max_min         - smallest maximum value
      max_max         - largest maximum value
      size_min        - smallest domain size (default)
      size_max        - largest domain size
      degree_size_min - smallest domain size divided by degree
      degree_size_max - largest domain size divided by degree
      afc_size_min    - smallest domain size divided by AFC
      afc_size_max    - largest domain size divided by AFC
      action_size_min - smallest action divided by domain size
      action_size_max - largest action divided by domain size
      regret_min_min  - smallest minimum-regret
      regret_min_max  - largest minimum-regret
      regret_max_min  - smallest maximum-regret
      regret_max_max  - largest maximum-regret

lim:fail (faillim, faillimit)
      Fail limit.

lim:nodes (nodelim, nodelimit)
      Node limit.

lim:sol (solutionlimit)
      Limit on the number of feasible solutions found before terminating a
      search. Leaving the solution limit unspecified will make the optimizer
      search for an optimal solution if there is an objective function or for
      a feasible solution otherwise.

lim:time (timelim, timelimit)
      Time limit in seconds.

log:freq (logfreq, outfreq)
      Output frequency in seconds. The value should be a positive number.

log:lev (outlev)
      0 or 1 (default 0): Whether to print solution log.

obj:no (objno)
      Objective to optimize:

      0 - None
      1 - First (default, if available)
      2 - Second (if available), etc.

sol:count (countsolutions)
      0*/1: Whether to count the number of solutions and return it in the
      ".nsol" problem suffix.

sol:report_uncertain (report_uncertain_sol)
      0/1*: whether to report objective value(s) in solve_message when
      solve_result is '?' (unknown).

sol:stub (solstub, solutionstub)
      Stub for solution files. If "solutionstub" is specified, found solutions
      are written to files ("solutionstub & '1' & '.sol'") ... ("solutionstub
      & Current.nsol & '.sol'"), where "Current.nsol" holds the number of
      returned solutions. That is, file names are obtained by appending 1, 2,
      ... "Current.nsol" to "solutionstub".

tech:debug (debug)
      0*/1: whether to assist testing & debugging, e.g., by outputting
      auxiliary information (mostly via suffixes).

tech:optionfile (optionfile, option:file)
      Name of an AMPL solver option file to read (surrounded by 'single' or
      "double" quotes if the name contains blanks). Lines that start with #
      are ignored. Otherwise, each nonempty line should contain "name=value",
      e.g., "lim:iter=500".

tech:outlev_mp (outlev_mp)
      0*/1: whether to print MP model information.

tech:stats (stats, tech:report_stats, solve_stats)
      Whether to return solve statistics and timings; the information will be
      stored in the problem suffixes: 'simplex_iterations',
      'barrier_iterations', 'nodes' and possibly other solver-dependent
      suffixes. A JSON representation of the information above is returned in
      the problem suffix `stats`.
      Note that timing information will also be included in the JSON
      representation if tech:timing>0. Values:

      0 - Do not report statistics (default)
      1 - Report statistics in JSON format in the problem suffix 'stats'
      2 - Report statistics in suffixes
      3 - Report statistics both in suffixes and the suffix 'stats'.

      See also obj:multi:stats.

tech:threads (threads)
      The number of parallel threads to use. Assume that your computer has m
      processing units and that the value for threads is n.

      * If n = 0, then m threads are used (as many as available processing
        units).

      * If n >= 1, then n threads are used (absolute number of threads to be
        used).

      * If n <= -1, then m + n threads are used (absolute number of processing
        units not to be used). For example, when n = -6 and m = 8, then 2
        threads are used.

      * If 0 < n < 1, then n * m threads are used (relative number of
        processing units to be used). For example, when n = 0.5 and m = 8,
        then 4 threads are used.

      * If -1 < n < 0, then (1 + n) * m threads are used (relative number of
        processing units not to be used). For example, when n = -0.25 and m =
        8, then 6 threads are used.

      All values are rounded and at least one thread is used.

tech:timing (timing, tech:report_times, report_times)
      0*/1/2: Whether to print and return timings for the run, all times are
      wall times. If set to 1, return the solution times in the problem
      suffixes 'time_solver', 'time_setup' and 'time', 'time'=
      time_solver+time_setup+time_output is a measure of the total time spent
      in the solver driver. If set to 2, return more granular times, including
      'time_read', 'time_conversion' and 'time_output'.

tech:version (version)
      Single-word phrase: report version details before solving the problem.

tech:wantsol (wantsol)
      In a stand-alone invocation (no "-AMPL" on the command line), what
      solution information to write. Sum of

      1 - Write ".sol" file
      2 - Primal variables to stdout
      4 - Dual variables to stdout
      8 - Suppress solution message.
```

