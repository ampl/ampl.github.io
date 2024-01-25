# NEOS: Kestrel client

To simplify the work of comparing and testing solvers, we have made AMPL and solver resources available online in collaboration with the [NEOS Server](https://www.neos-server.org/) project, under the auspices of the [Wisconsin Institutes for Discovery](https://www.discovery.wisc.edu/) at the University of Wisconsin, Madison. AMPL users can interact with the NEOS server in either of two ways:

-   by requesting execution of both AMPL and solvers at a remote site, or
-   by using a local AMPL session to send optimization problems to remote solvers.
    
These services are available free of charge through any Internet connection. They are intended mainly for testing, prototyping, and instructional purposes, however; pursuant to the posted [terms of use](https://www.neos-server.org/neos/termofuse.html), there are no guarantees of performance or confidentiality.

[[Read More](https://ampl.com/products/ampl/run-ampl-on-neos/)]
[[Download](https://portal.ampl.com)]

## How to use it

```{eval-rst}

.. tabs::

   .. tab:: AMPL

        .. code-block:: ampl

            ampl: option solver kestrel; # change the solver
            ampl: option kestrel_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem

   .. tab:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install gokestrel # install Kestrel

            # Activate your license (e.g., free ampl.com/ce or ampl.com/courses licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="kestrel", kestrel_options="option1=value1 option2=value2")
```

## Local AMPL with remote solvers

In this mode of operation, you run your own copy of AMPL on your local computer. But instead of specifying a solver installed on your computer or local network, you invoke _Kestrel,_ a “client” program that sends your problem to a solver running on one of the NEOS Server’s remote computers. The results from the NEOS Server are eventually returned through Kestrel to AMPL, where you can view and manipulate them locally in the usual way. Thus you get all the benefits of using AMPL environment, without having to first obtain and install each solver you want to try.

The introduction below covers everything you need to know to start using Kestrel with AMPL. There is also a [paper about Kestrel](https://ampl.com/learn/docs/reports-papers/#kestrel) that describes more advanced features and other uses.

## Downloading and installing the Kestrel client

To get started using this feature, you must obtain the free Kestrel program (called `gokestrel`). Kestrel downloads are available from the My Downloads page of your account at the [AMPL Portal](https://portal.ampl.com), and are included in the [demo bundles](https://portal.ampl.com/user/ampl/download/demo) that are used for free trials. The gokestrel program is one of open-source projects developed at AMPL and its source code is available at <https://github.com/ampl/gokestrel>.

To install, copy the downloaded file to the same folder or directory as your AMPL executable (`ampl` or `ampl.exe`). Then extract the kestrel program by double-clicking the downloaded file’s icon on Windows and macOS systems, or by invoking

```
gzip -dc gokestrel.linux-intel64.tgz | tar xf -
```

in a Linux command window.

## Selecting and running a solver with the Kestrel client

The Kestrel client program works like a special kind of solver. Once you have installed the Kestrel executable, you tell AMPL to use Kestrel by setting the option solver to kestrel. You then set the option `kestrel_options` to indicate which remote solver you want to access through Kestrel. Directives for the chosen solver are specified in the usual way through an option having a name of the form `solvername_options`.

Additionally, NEOS now requires an email address with every submission. You send your address to Kestrel by setting option email.

As an example, here is how you might invoke Kestrel from a local AMPL session, using LOQO as your remote solver:

```
ampl: model steelT.mod;
ampl: data steelT.dat;
ampl: option solver kestrel;
ampl: option kestrel_options 'solver=loqo';
ampl: option loqo_options 'minlocfil sigfig=8 outlev=2';
ampl: option email "neos@ampl.com";
ampl: solve;
```

After Kestrel is invoked by solve, it establishes communication with the NEOS Server and sends the AMPL problem file. The NEOS Server’s successful receipt of the problem file is indicated by messages like these:

```
Connecting to: neos-server.org:3333
Job 11200647 submitted to NEOS, password='FHWZCubo'
Check the following URL for progress report:
https://neos-server.org/neos/cgi-bin/nph-neos-solver.cgi?admin=results&jobnumber=11200647&pass=FHWZCubo
Job 11200647 dispatched
password: FHWZCubo
---------- Begin Solver Output -----------
Condor submit: 'neos.submit'
Condor submit: 'watchdog.submit'
Job submitted to NEOS HTCondor pool.
kestrel_options:solver=loqo
loqo_options:minlocfil sigfig=8 outlev=2
You are using the solver loqo.
Executing on prod-exec-1.neos-server.org
```

The job number and password are sometimes useful in retrieving the results, as we’ll explain in a moment, but in the simplest mode of operation Kestrel simply displays any output produced by the solver in the course of its run, and eventually retrieves the solution files when the solver is finished:

```
LOQO 7.00: minlocfil
sigfig=8
outlev=2
It's a QP.
variables: non-neg     16,  free        0,  bdd          8,  total       24
constraints: eq         8,  ineq        4,  ranged       0,  total       12
nonzeros:    A         38,  Q           0
-----------------------------------------------------------------------------
     |         Primal          |           Dual          | Sig
Iter |  Obj Value     Infeas   |   Obj Value     Infeas  | Fig  Status  P   M
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
nonzeros:    L         59,  arith_ops                320
  1    0.000000e+00   1.3e-01     3.685200e+06   0.0e+00           DF
  2    1.355005e+04   9.6e-02     8.102539e+05   1.4e-01
  3    5.003331e+04   6.4e-03     4.966615e+05   1.0e-01
  4    2.265421e+05   1.3e-02     5.575060e+05   5.5e-02
  5    3.900414e+05   7.4e-03     7.171113e+05   4.9e-02
  6    4.361999e+05   2.8e-03     7.365406e+05   4.1e-02
  7    4.524115e+05   1.5e-03     7.029543e+05   3.2e-02
  8    4.721932e+05   2.6e-04     5.724328e+05   3.6e-03    1
  9    5.076870e+05   3.2e-05     5.287918e+05   1.4e-03    1
 10    5.124574e+05   1.3e-05     5.190324e+05   3.2e-04    2
 11    5.146851e+05   1.8e-06     5.153676e+05   2.4e-05    3
 12    5.150152e+05   9.1e-08     5.150530e+05   1.4e-06    4   PF
 13    5.150321e+05   4.5e-09     5.150340e+05   7.1e-08    5   PF DF
 14    5.150330e+05   2.3e-10     5.150330e+05   3.6e-09    7   PF DF
 15    5.150330e+05   1.1e-11     5.150330e+05   1.8e-10    8   PF DF
----------------------
OPTIMAL SOLUTION FOUND
Writing solution to C:\Users\4er\AppData\Local\Temp\at5248.sol
```

Kestrel then disconnects from the NEOS Server and terminates its execution. Finally, the solve command completes its work by reading the solution file and displaying its usual solution summary:

```
LOQO 7.00: optimal solution (15 QP iterations, 15 evaluations)
primal objective 515032.9977724714
  dual objective 515033.0024976235
```

That’s it! You are returned to the ampl: prompt and can proceed to display or manipulate the solution or to do anything else that you would have done if the problem had been solved by a local copy of LOQO. Subsequent uses of the solve command will continue to invoke a remote solver, until you change the option solver or conclude the AMPL session.

In general, you choose a remote solver through your setting of the AMPL option `kestrel_options`. The form of the AMPL command for this purpose is

```
option kestrel_options 'solver=solvername';
```

The following choices for solvername are currently recognized (with links to their NEOS pages for informational purposes):

-   Bound-Constrained Optimization  
    [L-BFGS-B](https://www.neos-server.org/neos/solvers/bco:L-BFGS-B/AMPL.html)
    
-   Complementarity Problems  
    [Knitro](https://www.neos-server.org/neos/solvers/cp:Knitro/AMPL.html), [PATH](https://www.neos-server.org/neos/solvers/cp:PATH/AMPL.html)
    
-   Global Optimization  
    [Couenne](https://www.neos-server.org/neos/solvers/go:Couenne/AMPL.html), [LGO](https://www.neos-server.org/neos/solvers/go:LGO/AMPL.html), [Octeract](https://www.neos-server.org/neos/solvers/go:OCTERACT/AMPL.html), [RAPOSa](https://www.neos-server.org/neos/solvers/go:RAPOSa/AMPL.html)
    
-   Linear Programming  
    [CPLEX](https://www.neos-server.org/neos/solvers/lp:CPLEX/AMPL.html), [MOSEK](https://www.neos-server.org/neos/solvers/lp:MOSEK/AMPL.html), [Octeract](https://www.neos-server.org/neos/solvers/lp:OCTERACT/AMPL.html), [OOQP](https://www.neos-server.org/neos/solvers/lp:OOQP/AMPL.html)
    
-   Mathematical Programs with Equilibrium Constraints  
    [Knitro](https://www.neos-server.org/neos/solvers/mpec:Knitro/AMPL.html)
    
-   Mixed Integer Linear Programming  
    [Cbc](https://www.neos-server.org/neos/solvers/milp:Cbc/AMPL.html), [CPLEX](https://www.neos-server.org/neos/solvers/milp:CPLEX/AMPL.html), [MINTO](https://www.neos-server.org/neos/solvers/milp:MINTO/AMPL.html), [MOSEK](https://www.neos-server.org/neos/solvers/milp:MOSEK/AMPL.html), [Octeract](https://www.neos-server.org/neos/solvers/milp:OCTERACT/AMPL.html)
    
-   Mixed Integer Nonlinearly Constrained Optimization  
    [Bonmin](https://www.neos-server.org/neos/solvers/minco:Bonmin/AMPL.html), [Couenne](https://www.neos-server.org/neos/solvers/minco:Couenne/AMPL.html), [FilMINT](https://www.neos-server.org/neos/solvers/minco:FilMINT/AMPL.html), [Knitro](https://www.neos-server.org/neos/solvers/minco:Knitro/AMPL.html), [MINLP](https://www.neos-server.org/neos/solvers/minco:MINLP/AMPL.html), [Octeract](https://www.neos-server.org/neos/solvers/minco:OCTERACT/AMPL.html)
    
-   Nonlinearly Constrained Optimization  
    [CONOPT](https://www.neos-server.org/neos/solvers/nco:CONOPT/AMPL.html), [filter](https://www.neos-server.org/neos/solvers/nco:filter/AMPL.html), [Ipopt](https://www.neos-server.org/neos/solvers/nco:Ipopt/AMPL.html), [KNITRO](https://www.neos-server.org/neos/solvers/nco:KNITRO/AMPL.html), [LANCELOT](https://www.neos-server.org/neos/solvers/nco:LANCELOT/AMPL.html), [LOQO](https://www.neos-server.org/neos/solvers/nco:LOQO/AMPL.html), [MINOS](https://www.neos-server.org/neos/solvers/nco:MINOS/AMPL.html), [Octeract](https://www.neos-server.org/neos/solvers/nco:OCTERACT/AMPL.html), [SNOPT](https://www.neos-server.org/neos/solvers/nco:SNOPT/AMPL.html)
    

A current list can be obtained by leaving out the solver name:

```
option kestrel_options 'solver';
```

You can pass directives to any of these solvers by assigning an appropriate directive string to the AMPL option consisting of the solver’s name followed by \_options. In the previous example, we requested LOQO’s “min local fill” option, specified agreement of primal and dual objectives to 8 significant figures, and turned on detailed iteration output by giving the following AMPL command prior to solving:

```
option loqo_options 'minlocfil sigfig=8 outlev=2';
```

For information on directives recognized by the available solvers, follow the links from their names in the listing above.

## Viewing output and results

By default, kestrel runs jobs with “short” priority: all solver output is displayed, but _execution time is limited to 5 minutes._ To run longer jobs, add `priority=long` to your `kestrel_options` string; this allows execution time up to 8 hours, but does not show solver output.

To retrieve results from current Kestrel run (if you are disconnected) or from a previous Kestrel run, first set up the same AMPL model and data that you used when submitting your problem. Then set `kestrel_options` to specify the job number and password that Kestrel reported when it processed the job. For the example above, the appropriate AMPL commands would be as follows:

```
ampl: model steelT.mod;
ampl: data steelT.dat;
ampl: option solver kestrel;
ampl: option kestrel_options 'job=2746671 password=AnVsgUKc';
ampl: solve;
```

Kestrel contacts the NEOS Server to reconnect to the specified job (if it is still running) or to retrieve the results from the specified job (if it has finished). The display of the solver output and the return of the results to AMPL then proceed exactly as previously described. The NEOS Server only keeps previous results for a short time, however — typically a day — so this feature is not appropriate for archiving of runs.

If you have set up an account at the [NEOS website](https://neso-server.org), you can run jobs as an authenticated user by by setting AMPL options that specify your NEOS login credentials:

```
option neos_username 'your_username';
option neos_user_password 'your_neos_password';
```

This will give you extended access to your recent jobs.

## Managing Kestrel runs

To submit multiple optimization runs and then retrieve them in the order that they were submitted, see the detailed instructions in [Kestrel: An Interface from Optimization Modeling Systems to the NEOS Server](https://ampl.com/learn/docs/reports-papers/#kestrel). This feature should be used with care, so as not to overload the Server resources.

To cancel a NEOS job before the solver has completed execution, set option `kestrel_options` to specify the appropriate job number and password, and then run the Kestrel program with the special argument kill. For example:

```
ampl: option kestrel_options 'job=11200647 password=FHWZCubo';
ampl: option email 'neos@ampl.com';
ampl: shell 'kestrel kill';
Connecting to: neos-server.org:3333
Kill Job #11200670 Request sent to prod-sub-1.neos-server.org
```

Normally Kestrel will still be running at this point, so you will need to start up a second AMPL process to enter these commands. After the job has been terminated, the Kestrel run in your original AMPL window will complete and return you to the `ampl:` prompt. If the solver is set up to handle interruptions, Kestrel will return the best solution that the solver was able to find.