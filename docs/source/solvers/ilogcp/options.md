
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

 Options:

alldiffinferencelevel
      Inference level for "alldiff" constraints. Possible values:

        default 
        low     
        basic   
        medium  
        extended

      The default value is "default", which allows the inference strength of
      all "alldiff" constraints to be controlled via "defaultinferencelevel".

branchlimit
      Limit on the number of branches made before terminating a search.
      Default = no limit.

choicepointlimit
      Limit on the number of choice points created before terminating a
      search. Default = no limit.

cppresolve
      0 or 1 (default 1): Whether to activate presolve on the CP optimizer.

debugexpr
      0 or 1 (default 0): Whether to print debugging information for
      expression trees.

defaultinferencelevel
      Inference level for constraints that have inference level set to
      "default". Possible values:

        low     
        basic   
        medium  
        extended

      The default value is "basic".

distributeinferencelevel
      Inference level for aggregated "numberof" ("IloDistribute") constraints.
      Possible values:

        default 
        low     
        basic   
        medium  
        extended

      The default value is "default", which allows the inference strength of
      all aggregated "numberof" constraints to be controlled via
      "defaultinferencelevel".

dumpfile
      Specifies the name of a file where to dump the model before solving it.
      This file name must have extension ".cpo". Default = "" (don't dump the
      model).

dynamicprobing
      Use probing during search. Possible values:

        auto
        off 
        on  

      The default value is "auto".

dynamicprobingstrength
      Effort dedicated to dynamic probing as a factor of the total search
      effort. Default = 0.03.

elementinferencelevel
      Inference level for "element" ("IloElement") constraints. Possible
      values:

        default 
        low     
        basic   
        medium  
        extended

      The default value is "default", which allows the inference strength of
      all "element" constraints to be controlled via "defaultinferencelevel".

exportfile
      Specifies the name of a file where to export the model before solving
      it. This file name must have extension ".cpo". Default = "" (don't
      export the model).

faillimit
      Limit on the number of failures allowed before terminating a search.
      Default = no limit.

failuredirectedsearchemphasis
      Specifies the number of workers that use failure-directed search once it
      has started. The value does not have to be integer. For example, value
      1.5 means that first worker spends 100% of the time by failure-directed
      search, second worker 50% and remaining workers 0%. Default = auto
      (depends on actual performance of the failure-directed search).

logperiod
      Specifies how often the information in the search log is displayed.

logverbosity
      Verbosity of the search log. Possible values:

        quiet  
        terse  
        normal 
        verbose

      The default value is "quiet".

mipdisplay
      Frequency of displaying branch-and-bound information (for optimizing
      integer variables):

      0 (default) - never
      1 - each integer feasible solution
      2 - every "mipinterval" nodes
      3 - every "mipinterval" nodes plus information on LP relaxations (as
      controlled by "display")
      4 - same as 2, plus LP relaxation info.
      5 - same as 2, plus LP subproblem info.

mipinterval
      Frequency of node logging for mipdisplay 2 or 3. Default = 0.

multipointnumberofsearchpoints
      Number of solutions for the multi-point search algorithm. Default = 30.

obj:multi (multiobj)
      0*/1: Whether to use multi-objective optimization. If set to 1
      multi-objective optimization is performed using lexicographic method
      with the first objective treated as the most important, then the second
      objective and so on.

obj:no (objno)
      Objective to optimize:

      0 - None
      1 - First (default, if available)
      2 - Second (if available), etc.

optimalitytolerance
      Absolute tolerance on the objective value. Default = 0.

optimizer
      Specifies which optimizer to use. Possible values:

      auto  - CP Optimizer if the problem has nonlinear objective/constraints
              or logical constraints, CPLEX otherwise
      cp    - CP Optimizer
      cplex - CPLEX Optimizer

      The default value is "auto".

outlev
      Synonym for "logverbosity".

randomseed
      Seed for the random number generator. Default = 0.

relativeoptimalitytolerance
      Relative tolerance on the objective value. Default = 1e-4.

restartfaillimit
      Number of failures allowed before restarting search. Default = 100.

restartgrowthfactor
      Increase of the number of allowed failures before restarting search.
      Default = 1.05.

searchtype
      Type of search used for solving a problem. Possible values:

        auto           
        depthfirst     
        restart        
        multipoint     
        iterativediving

      The default value is "auto".

sol:count (countsolutions)
      0*/1: Whether to count the number of solutions and return it in the
      ".nsol" problem suffix.

sol:stub (solstub, solutionstub)
      Stub for solution files. If "solutionstub" is specified, found solutions
      are written to files ("solutionstub & '1' & '.sol'") ... ("solutionstub
      & Current.nsol & '.sol'"), where "Current.nsol" holds the number of
      returned solutions. That is, file names are obtained by appending 1, 2,
      ... "Current.nsol" to "solutionstub".

solutionlimit
      Limit on the number of feasible solutions found before terminating a
      search. Leaving the solution limit unspecified will make the optimizer
      search for an optimal solution if there is an objective function or for
      a feasible solution otherwise.

tech:debug (debug)
      0*/1: whether to assist testing & debugging, e.g., by outputting
      auxiliary information.

tech:optionfile (optionfile, option:file)
      Name of solver option file. (surrounded by 'single' or "double" quotes
      if the name contains blanks). Lines that start with # are ignored.
      Otherwise, each nonempty line should contain "name=value".

tech:timing (timing)
      0*/1: Whether to display timings for the run.

tech:version (version)
      Single-word phrase: report version details before solving the problem.

tech:wantsol (wantsol)
      In a stand-alone invocation (no "-AMPL" on the command line), what
      solution information to write. Sum of

      1 - Write ".sol" file
      2 - Primal variables to stdout
      4 - Dual variables to stdout
      8 - Suppress solution message.

temporalrelaxation
      0 or 1 (default 1): Whether to use temporal relaxation.

timelimit
      Limit on the CPU time spent solving before terminating a search. Default
      = no limit.

timemode
      Specifies how the time is measured in CP Optimizer. Possible values:

        cputime    
        elapsedtime

      The default value is "cputime".

usenumberof
      0 or 1 (default 1): Whether to aggregate "numberof" expressions by use
      of "IloDistribute" constraints.

warninglevel
      Specifies the highest warning level to be displayed, all warnings higher
      than this level are masked. CP Optimizer warning levels run from 1 to 4,
      so setting this option to 0 turns off all warnings. Warnings issued may
      indicate potential errors or inefficiencies in your model. Default = 2.

workers
      Number of workers to run in parallel to solve a problem. In addition to
      numeric values this option accepts the value "auto" since CP Optimizer
      version 12.3. Default = "auto".

```

