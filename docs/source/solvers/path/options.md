
# PATH Options

```ampl
ampl: option solver path; # change the solver
ampl: option path_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

Solver options obtained with `$ path -=`.

```
convtol         Stopping criterion (default 1e-6)
crashiterlim    Maximum iterations allowed in crash (default 50)
crashmethod     Crash method:
                0 = none 
                1 = automatic
                2 = pnewton (default)
                3 = bdiff
                4 = smooth
crashmindim     Minimum problem dimension required to perform crash (default 1)
crashchglim     Number of changes to the basis allowed (default 1)
debug           debug level (default 0): sum of
                1 = show initial z and bounds
                2 = show z and f(z)
                4 = show z and J = f'(z)
                8 = show sparsity of J
cumuliterlim    Maximum minor iterations allowed (default 10000)
lemkestart      Frequency of lemke starts:
                0 = automatic (default)
                1 = first
                2 = always
logfile         name of log file
license         license string to activate Path
majiterlim      Maximum major iterations allowed (default 500)
maxfwd          max vars in fwd AD of common exprs (default 5)
miniterlim      Maximum minor iterations allowed in each major iteration (default 1000)
nms             Allow searching, watchdogging, and non-monotone descent:
                0 = no
                1 = yes (default)
nmsreffactor    Controls size of initial reference value (default 20)
nmsmemsize      Number of reference values kept (default 10)
nmsmstepfreq    Frequency at which m steps are performed (default 10)
nmssearchtype   Search type:
                0 = path (default)
                1 = line
optfile         name of options file
outlev          Turn output on or off:
                0 = off
                1 = on (default)
outcrashiter    Output information on crash iterations:
                0 = no
                1 = yes (default)
outcrashiteraf  Frequency at which crash iteration log is printed (default 1)
outerrors       Output error messages:
                0 = no
                1 = yes (default)
outlinearmodel  Output linear model each major iteration:
                0 = no (default)
                1 = yes
outmajiter      Output information on major iterations:
                0 = no
                1 = yes (default)
outmajiterf     Frequency at which major iteration log is printed (default 1)
outminiter      Output information on minor iterations:
                0 = no
                1 = yes (default)
outminiterf     Frequency at which minor iteration log is printed (default 500)
outoptions      Output all options and their values:
                0 = no (default)
                1 = yes
outwarnings     Output warning messages:
                0 = no (default)
                1 = yes
proxpertur      Initial perturbation (default 0.0)
restartlim      Maximum number of restarts (default 10)
sideineq        handling of side inequalities:
                0 = no warning
                1 = warn (default)
                2 = quit, permitting AMPL loops to test solve_result
                3 = quit, terminating AMPL loops and scripts
                4 = do not make Jacobian nonsingular (avoid nonuniqueness)
                5 = warn and do not make Jacobian nonsingular
sqwarn          whether to warn of nonsquare systems:
                0 = no
                1 = yes (default)
                2 = quit, permitting AMPL loops to test solve_result
                3 = quit, terminating AMPL loops and scripts
statusfile      name of status file
timelim         Maximum number of seconds algorithm is allowed to run (default 3600)
version         report version
wantsol         solution report without -AMPL: sum of
		1 ==> write .sol file
		2 ==> print primal variable values
		4 ==> print dual variable values
		8 ==> do not print solution message
```

