
# ILOGCP Options

```ampl
ampl: option solver ilogcp; # change the solver
ampl: option ilogcp_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

Solver options obtained with `$ ilogcp -=`.

```
IBM ILOG CPLEX CP Optimizer Options for AMPL
--------------------------------------------

To set these options, assign a string specifying their values to the AMPL
option "ilogcp_options". For example:

   ampl: option ilogcp_options 'optimalitytolerance=1e-6 searchtype=restart';

'' Options:

cp:alldiffinferencelevel (alldiffinferencelevel)
      Inference level for "alldiff" constraints. Possible values:

        default 
        low     
        basic   
        medium  
        extended

      The default value is "default", which allows the inference strength of
      all "alldiff" constraints to be controlled via
      "cp:defaultinferencelevel".

cp:defaultinferencelevel (defaultinferencelevel)
      Inference level for constraints that have inference level set to
      "default". Possible values:

        low     
        basic   
        medium  
        extended

      The default value is "basic".

cp:distributeinferencelevel (distributeinferencelevel)
      Inference level for aggregated "numberof" ("IloDistribute") constraints.
      Possible values:

        default 
        low     
        basic   
        medium  
        extended

      The default value is "default", which allows the inference strength of
      all aggregated "numberof" constraints to be controlled via
      "cp:defaultinferencelevel".

cp:dynamicprobing (dynamicprobing)
      Use probing during search. Possible values:

        auto
        off 
        on  

      The default value is "auto".

cp:dynamicprobingstrength (dynamicprobingstrength)
      Effort dedicated to dynamic probing as a factor of the total search
      effort. Default = 0.03; must be between 0.001 and 1000.

cp:elementinferencelevel (elementinferencelevel)
      Inference level for "element" ("IloElement") constraints. Possible
      values:

        default 
        low     
        basic   
        medium  
        extended

      The default value is "default", which allows the inference strength of
      all "element" constraints to be controlled via
      "cp:defaultinferencelevel".

cp:fds (failuredirectedsearch)
      0 or 1 (default 1): Whether to use failure-directed search.

cp:fdsemphasis (failuredirectedsearchemphasis)
      Specifies the number of workers that use failure-directed search once it
      has started. The value does not have to be integer. For example, value
      1.5 means that first worker spends 100% of the time by failure-directed
      search, second worker 50% and remaining workers 0%. Default = auto (-1;
      depends on actual performance of the failure-directed search).

cp:fdsmaxmemory (failuredirectedsearchmaxmemory)
      Maximum memory in bytes available to failure-directed search. Default =
      104857600 (100 MB).

cp:multipointnumberofsearchpoints (multipointnumberofsearchpoints)
      Number of solutions for the multi-point search algorithm. Default = 30.

cp:restartfaillimit (restartfaillimit)
      Number of failures allowed before restarting search
      ("cp:searchtype=restart"). Default = 100.

cp:restartgrowthfactor (restartgrowthfactor)
      Increase of the number of allowed failures before restarting search.
      Default = 1.15; must be >= 1.

cp:searchtype (searchtype)
      Type of search used for solving a problem. Possible values:

        auto           
        depthfirst     
        restart        
        multipoint     
        iterativediving
        neighborhood    - (beta in CP Optimizer 22.1)

      The default value is "auto".

cp:temporalrelaxation (temporalrelaxation)
      Whether to use the internal temporal relaxation. Possible values:

        auto
        off 
        on  

      The default value is "auto".

cvt:usenumberof (usenumberof)
      0 or 1 (default 1): Whether to aggregate "numberof" expressions by use
      of "IloDistribute" constraints.

iis:find (iisfind, iis)
      0 or 1 (default 0): Whether to run the conflict refiner when the problem
      is infeasible and return an IIS in suffix .iis ("mem" = member, "pmem" =
      possible member, "non" = not in the IIS) on constraints and, with CP
      Optimizer, on variables. Members among logical constraints are counted
      in the solve message.

iis:onvariables (conflictrefineronvariables)
      0 or 1 (default 0): Whether the CP Optimizer conflict refiner also
      refines variable domains.

lim:branch (branchlimit)
      Limit on the number of branches made before terminating a search.
      Default = no limit.

lim:choicepoint (choicepointlimit)
      Limit on the number of choice points created before terminating a
      search. Default = no limit.

lim:conflictbranch (conflictrefinerbranchlimit)
      Limit on the total number of branches of the CP Optimizer conflict
      refiner. Default = no limit.

lim:conflictfail (conflictrefinerfaillimit)
      Limit on the total number of failures of the CP Optimizer conflict
      refiner. Default = no limit.

lim:conflictiter (conflictrefineriterationlimit)
      Limit on the number of iterations of the CP Optimizer conflict refiner.
      Default = no limit.

lim:conflicttime (conflictrefinertimelimit)
      Time limit in seconds for the CP Optimizer conflict refiner. Default =
      no limit.

lim:fail (faillimit)
      Limit on the number of failures allowed before terminating a search.
      Default = no limit.

lim:sol (solutionlimit, sollimit)
      Limit on the number of feasible solutions found before terminating a
      search. Leaving the solution limit unspecified will make the optimizer
      search for an optimal solution if there is an objective function or for
      a feasible solution otherwise. Also applied to the CPLEX optimizer.

lim:time (timelimit, timelim)
      Limit on the time (measured as specified by tech:timemode, elapsed time
      by default) spent solving before terminating a search. Default = no
      limit. Also applied to the CPLEX optimizer.

mip:gap (relativeoptimalitytolerance, mipgap)
      Relative tolerance on the objective value. Default = 1e-4; with the
      CPLEX optimizer, a non-default value is applied as the relative MIP gap.

mip:gapabs (optimalitytolerance, absmipgap)
      Absolute tolerance on the objective value. Default = 1e-9 (CP
      Optimizer); with the CPLEX optimizer, a non-default value is applied as
      the absolute MIP gap.

obj:multi (multiobj)
      Whether to use multi-objective optimization:

      0 - Single objective, see option obj:no (default)
      1 - Multi-objective, solver's native handling if available
      2 - Multi-objective, force emulation

      When obj:multi>0 and several objectives are present, suffixes
      .objpriority, .objweight, .objreltol, and .objabstol on the objectives
      are relevant. Objectives with greater .objpriority values (integer
      values) have higher priority. Objectives with the same .objpriority are
      weighted by .objweight, according to the option obj:multi:weight.

      Objectives with positive .objabstol or .objreltol are allowed to be
      degraded by lower priority objectives by amounts not exceeding the
      .objabstol (absolute) and .objreltol (relative) limits.

      Note that with solver's native handling (when obj:multi=1 and
      supported), some solvers might have special rules for the tolerances,
      especially for LP, and only allow linear objectives. See the solver
      documentation and options cvt:quadobj, cvt:nlobj.

obj:multi:weight (multiobjweight, obj:multi:weights, multiobjweights)
      How to interpret each objective's weight sign:

      1 - relative to the sense of the 1st objective
      2 - relative to its own sense (default)

      With the 1st option (legacy behaviour), negative .objweight for
      objective i would make objective i's sense the opposite of the model's
      1st objective. Otherwise, it would make objective i's sense the opposite
      to its sense defined in the model.

obj:no (objno)
      Objective to optimize:

      0 - None
      1 - First (default, if available)
      2 - Second (if available), etc.

pre:solve (cppresolve, presolve)
      0 or 1 (default 1): Whether to activate presolve on the CP optimizer.

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

tech:debugexpr (debugexpr)
      0 or 1 (default 0): Whether to print debugging information for
      expression trees.

tech:dumpfile (dumpfile)
      Specifies the name of a file where to dump the model before solving it.
      This file name must have extension ".cpo". Default = "" (don't dump the
      model).

tech:kpidisplay (kpidisplay)
      How KPIs are displayed in the CP Optimizer log. Possible values:

      singleline    - all KPIs on one line (default)
      multiplelines - one line per KPI

tech:logperiod (logperiod)
      Specifies how often (in branches) the information in the search log is
      displayed. Default = 1000.

tech:logsearchtags (logsearchtags)
      0 or 1 (default 0): Whether to display failure tags in the CP Optimizer
      log.

tech:mipdisplay (mipdisplay)
      Frequency of displaying branch-and-bound information (for optimizing
      integer variables with the CPLEX optimizer):

      0 (default) - never
      1 - each integer feasible solution
      2 - every "tech:mipinterval" nodes
      3 - every "tech:mipinterval" nodes plus cutting planes info
      4 - same as 3, plus LP relaxation info
      5 - same as 4, plus LP subproblem info.

tech:mipinterval (mipinterval)
      Frequency of node logging for tech:mipdisplay >= 2. Default = 0
      (automatic).

tech:modelanonymizer (modelanonymizer)
      0 or 1 (default 0): Whether to anonymize names in models written by
      tech:dumpfile.

tech:optimizer (optimizer)
      Specifies which optimizer to use. Possible values:

      auto  - CP Optimizer if the problem has nonlinear objective/constraints
              or logical constraints, CPLEX otherwise
      cp    - CP Optimizer
      cplex - CPLEX Optimizer

      The default value is "auto".

tech:optionfile (optionfile, option:file)
      Name of an AMPL solver option file to read (surrounded by 'single' or
      "double" quotes if the name contains blanks). Lines that start with #
      are ignored. Otherwise, each nonempty line should contain "name=value",
      e.g., "lim:iter=500".

tech:outlev (outlev, logverbosity)
      Verbosity of the search log. Possible values:

        quiet  
        terse  
        normal 
        verbose

      The default value is "quiet". With the CPLEX optimizer, values other
      than "quiet" turn on the CPLEX log (see tech:mipdisplay).

tech:outlev_mp (outlev_mp)
      0*/1: whether to print MP model information.

tech:printmodeldetails (printmodeldetailsinmessages)
      0 or 1 (default 1): Whether CP Optimizer prints relevant model fragments
      in error and warning messages.

tech:seed (randomseed, seed)
      Seed for the random number generator. Default = 0. With the CPLEX
      optimizer, a non-default value is applied as the CPLEX random seed.

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

tech:threads (workers, threads)
      Number of workers to run in parallel to solve a problem. In addition to
      numeric values this option accepts the value "auto". Default = "auto"
      (one worker per CPU core). Also applied as the number of threads of the
      CPLEX optimizer.

tech:timemode (timemode)
      Specifies how the time is measured in CP Optimizer. Possible values:

        cputime    
        elapsedtime

      The default value is "elapsedtime".

tech:timing (timing, tech:report_times, report_times)
      0*/1/2: Whether to print and return timings for the run, all times are
      wall times. If set to 1, return the solution times in the problem
      suffixes 'time_solver', 'time_setup' and 'time', 'time'=
      time_solver+time_setup+time_output is a measure of the total time spent
      in the solver driver. If set to 2, return more granular times, including
      'time_read', 'time_conversion' and 'time_output'.

tech:usefilelocations (usefilelocations)
      0 or 1 (default 1): Whether source file locations are processed and
      exported by CP Optimizer.

tech:version (version)
      Single-word phrase: report version details before solving the problem.

tech:wantsol (wantsol)
      In a stand-alone invocation (no "-AMPL" on the command line), what
      solution information to write. Sum of

      1 - Write ".sol" file
      2 - Primal variables to stdout
      4 - Dual variables to stdout
      8 - Suppress solution message.

tech:warninglevel (warninglevel)
      Specifies the highest warning level to be displayed, all warnings higher
      than this level are masked. CP Optimizer warning levels run from 1 to 3,
      so setting this option to 0 turns off all warnings. Warnings issued may
      indicate potential errors or inefficiencies in your model. Default = 2.

tech:writemodel (exportfile, writeprob, writemodel)
      Specifies the name of a file where to export the model before solving
      it. With CP Optimizer this file name must have extension ".cpo"; with
      the CPLEX optimizer the usual CPLEX formats (".lp", ".mps", ".sav") can
      be used. Default = "" (don't export the model).
```

