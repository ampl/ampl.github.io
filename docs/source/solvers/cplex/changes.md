# CPLEX Changelog

## 20230228
- Relinked with CPLEX 22.01.01

## 20210614.1
- Possible problem in the licencing routines for computer with many MAC addresses.
 
## 20210614
- Relink with ASL version 20210613 to fix a fault with indicator constraints.

## 20210726
- Added options presos1reformulations, presos2reformulations and 
  prereformulations_desc that control various aspects of reformulations.
- Renamed submipstart to submipstartalg
- Added parameter finalmipalg to control the algorithm used in the solution
  of the final LP after solving a MIP problem

## 20210206
- Added option benders_worker to control the algorithm used when 
  solving subproblems using Benders decomposition.

## 20210105
- Updated to CPLEX 20.1, which includes algorithmic improvements,
  a new possible value for 'mipemphasis' and the new option 
  'nodecuts'. See -= output for details.

## 20201020
- Fixed a problem occuring when both lazy constraints and user cuts
  are specified via the suffix 'lazy'

## 20201005
- [MacOS] Added support for older version of MacOS

## 20200921
- In case of error the driver now returns CPLEX error description 
  together with the error code.
- Linux and OSX versions of the driver are now dynamically linked.

## 20200914
- cplex.c:  add possible values 3-7 for (mipstart =) mipstartvalue.
  These values are probably rarely helpful, but a user reported having
  an instance where mipstart=4 was much faster than the default.

## 20200412
- cplex.c:  fix a bug (possible fault) with SOS sets; suppress some
  new, unwanted output (described in the entry for 20200205 below).

## 20200205
- Update to CPLEX 12.10.  
- New keyword heureffort.  See the ```cplex -=``` output or updated README.cplex for more details.
- CPLEX 12.10 now produces undesirable output of the form
	```Version identifier: 12.10.0.0 | 2019-11-26 | 843d4de```. 
  If IBM tells us how to suppress this output, we will update cplex.c
  to do so.

## 20190908
- Relink to ignore any LOGWAIT keywords in the ampl.lic or ampl.netlic file.

## 20190815
- Relink to fix a possible (seldom-seen) fault with indicator constraints.

## 20190522
- Relink to fix a bug with indicator constraints, which were incorrectly diagnosed as invalid when irrelevant defined variables where present.

## 20190501
- Adjust "cplex -=" output and README.cplex to reflect changes to defaults and, in some cases, new possible values for various keywords that have arisen since the keywords were introduced. Note that you can see the current default for, say, "keywd" by specifying "keywd=?" in $cplex_options or on the cplex command line.

## 20190315
- Relink to fix bugs with "objrep" when several objectives can be adjusted.

## 20190312
- Update to CPLEX 12.9.0. New keywords modisplay, multiobj, warninglimit. See the "cplex -=" output or updated README.cplex for more details.

## 20190216
- Add a case that affects feasopt with 32-bit binaries.

## 20190215
- Add solve_result_num values and descriptions for various returns associated with feasopt and feasoptobj.

## 20181120
- Relink to ignore HEARTBEAT lines in the ampl.lic file.

## 20180816
- Relink to fix possible trouble with identifying quadratic objectives and constraints on large problems.

## 20180709
- Relink to fix a bug with indicator constraints that use defined variables.

## 20180421
- Relink to fix bugs that could cause some indicator constraints to be rejected.

## 20180418
- Update 32-bit Windows cplex.exe to fix a fault with "logfile=..." that has only been seen in a Windows cplex.exe prior to CPLEX 12.8.

## 20180305
- Relink to fix a rately seen bug with indicator constraints.

## 20180302
- Relink to fix a bug with indicator constraints having an "else" clause.

## 20180220
- Relink to get a better error message with inappropriate logical constraints.

## 20171222
- Update to CPLEX 12.8.0. New keywords record, submipalg, submipscale, submipstart. See the "cplex -=" output or updated README.cplex for details.

## 20171218
- Relink to fix a possible fault introduced 20171215.

## 20171215
- Relink to fix possible trouble with quadratic objectives and constraints involving defined variables.

## 20171211
- Relink to fix more possible (probably unlikely) trouble with quadratic objectives and constraints.

## 20171107
- Relink to fix some trouble with quadratic forms. (No update was needed to the 32-bit cplex.exe.)

## 20170806
- Adjust treatment of mipbasis to accord with "cplex -=". Since 20141209 mipbasis=0 was incorrectly assumed for linear MIP problems.
- Minor updates (for 12.7.1) to README.cplex.

## 20170619
- Relink to fix a glitch with handling quadratic forms in large problem instances.

## 20170513
- Update to CPLEX 12.7.1. New keyword "simplexsifting". See the "cplex -=" output for details.

## 20170429
- Relink to fix bugs converting:

        var o;
        minimize O: o;
        s.t. c: o = q(x);
  to:

        minimize O: q(x);  
  where q(x) is quadratic. Linear and constant terms were sometimes mishandled.

## 20170222
- Fix some typos in the "cplex -=" output.

## 20170221
- Add keyword qcdmax for the maximum value of k*n*n for computing dual values for quadratic constraints, where k = number of quadratic constraints and n = number of variables. Default = 1e9. New solve_result_num value 5 indicates an optimal solution without dual values for quadratic constraints.

## 20161221
- Fix a bug in computing dual variable values for problems with quadratic constraints. NaNs were possible.

## 20161219
- Undo an "efficiency" change on 20161121 that caused a BUG message when computing duals for quadratic problems.

## 20161121
- Update to CPLEX 12.7. New keywords: benders_feascut_tol, benders_optcut_tol, benders_strategy, bendersopt, datacheck, rltcuts. See the "cplex -=" output for details.
- Withdrawn keywords: endvector, writevector. (Use endsol instead.)
- Only 64-bit Linux, MacOSX, and MS Windows are available for CPLEX 12.7.

## 20160818
- Fix bugs with "iisfind=1": sometimes constraints had .iis = "bug" and sometimes the solve_message reported the wrong number of variables in the IIS.

## 20160804
- Fix a bug (out-of-bounds subscript, possibly leading, e.g., to a fault) with "iisfind=1".

## 20160502
- Take optimization sense (minimize or maximize) into account when computing dual values for quadratic constraints. The versions of 20160409 and 20160411 implicitly assumed "minimize".

## 20160411
- Fix some other possible trouble with computing dual values for quadratic constraints.

## 20160409
- Fix some bugs with computing dual values for quadratic constraints.

## 20160118
- When dettimelim=... in $cplex_options causes the "solve" to stop, give solve_result_num = 440 if a feasible solution is returned and solve_result_nun = 441 otherwise. Previously an "unrecoverable failure" was reported.
- New keywords nosolve and writemipstart, and new possible solve_result_num values 581 for writeprob=... failure, 582 for writemipstart=... failure, and 600 for "not solved because of nosolve". See the updated README.cplex or "cplex -=" output.

## 20151209
- Relink to fix a bug with quadratic objectives or constraints with diagonal elements that sum to zero and whose rows contain nonzeros to the left but not to the right of the diagonal.

## 20151205
- Update to CPLEX 12.6.3, which presumably has some bug fixes.

## 20151125
- Fix a possible glitch in setting solve_result_num for infeasible or unbounded problems.
- For Linux binaries, add the directory containing the binary to the library search rules.

## 20151026
- Relink to fix a bug with "objrep" when the problem has several objectives.

## 20151005
- Relink to fix a fault with some quadratic objectives or constraints.

## 20150829
- Relink to fix a bug with quadratic objectives and constraints in which cancellation causes fewer than the generic number of quadratic nonzeros.

## 20150826
- Update the description of keywork mipinterval in the "cplex -=" output and README.cplex.

## 20150630
- Fix some possible trouble with a single-use license.

## 20150623
- Update to CPLEX 12.6.2. 
- New keywords bqpcuts, cpumask, solutiontype, sparam; change to the meaning of cutsfactor. See the "cplex -=" output or the updated README.cplex for details.

## 20150529
- Provide missing detail in descriptions of bestbound and bestnode in "cplex -=" output.

## 20150524
- Restore keyword "heurfreq", which was mistakenly removed in version 20141209.

## 20150427
- Fix a bug with "objrep" on problems with quadratic constraints.
- Fix a rarely seen licensing glitch.

## 20150421
- Update the descriptions of mipalg and mipstartalg.

## 20150327
- Fix a bug (possible fault or surprising behavior) with quadratic objectives that do not involve all variables.

## 20150304
- Relink to make keywords rampup_duration, rampup_timelim, rampup_walltimelim and vmconf available. See the output of "cplex -=" for details.
- When returning suffix .npool on the problem, also return it on the objective.

## 20141223
- Relink to fix a fault that was possible under unusual conditions.

## 20141209
- New keyword qcdual plus update for CPLEX 12.6.1.0: new keywords conflictalg, localimpliedcuts, qpmethod, qtolin; removed keywords basisinterval, heurfreq, oldpricing, pdswitch, xxxstart; new possible value 3 for netopt. See the updated README.cplex for details, which now also appear in the "cplex -=" output. 
- Internal changes should banish the error message "CPLEX solution status 101 with fixed integers" on some problems.

## 20141124
- Fix a bug (possible fault) in 64-bit cplex binaries with their handling of lazy constraints.

## 20141017
- Relink 64-bit binaries to fix possible trouble with SOS structures.

## 20141013
- Relink macosx binary so licenses can consider both hostname and local hostname.

## 20140828
- Fix a glitch seen only on a bizarre MS Windows system that got eror message "Bad LOCAL_MGR = 0.0.0.0" with a floating license. Only the MS Windows bundles are updated. If you have not seen the "Bad LOCAL_MGR" message, you do not need this update. With the updated cplex.exe, invoking "cplex -v" will show ASL(20140826).

## 20140718
- Update to CPLEX 12.6.0.1, which has some CPLEX bug fixes.

## 20140618
- Fix a glitch in the solve_message: the strings for "netopt found an infeasible network" and "netopt found an unbounded network" were interchanged.

## 20140313
- Fix a glitch (possible fault) sometimes seen with objrep.

## 20140205
- Relink to correct trouble (e.g., a fault) with objrep on 64-bit binaries.

## 20140204
- Correct the description of objno in the README.cplex files (in cplex.doc.*).

## 20140131
- Fix a glitch with a nonconvex diagonal QP when solved with reqconvex=3. When reqconvex=2 is specified for a quadratic MIP, complain and change reqconvex to 3 to bypass an apparent CPLEX bug.

## 20131210
- Updates for CPLEX 12.6, which has some bug fixes. 
- New keyword droptol (see README.cplex). 
- Better error message for a failed solve of a MIP subproblem and new solve_result_num value 513 for "failed to solve a MIP subproblem".

## 20131029
- Fix a bug (fault) in some recent 64-bit binaries with SOS sets, e.g., for piecewise-linear terms.

## 20131023
- Ignore case in MAC addresses during license checks (an issue rarely seen). When ending execution under a floating license, try to read a reply from the license manager to circumvent bug sometimes seen in MS Windows.

## 20130919
- Fix a fault that was possible with quadratic constraints under complicated conditions. 
- Fix a bug that sometimes caused an incorrect solution to be returned when quadratic objectives or constraints were present.
- Change defaults for qctol1, qctol2, and qctol3 to 1e-5, which might be more appropriate than 1e-6 when the barrier algorithm is involved.

## 20130916
- Fix a glitch in computing duals for quadraticallyconstrained problems with no objective (i.e., feasibility problems).
- Fix a recently introduced fault in 64-bit versions with linear objectives involving just one variable.

## 20130801
- Add a least-squares computation of dual variables for quadratically-constrained problems. Previously on such problems, the dual variables for linear constraints may have been wrong. Three new tolerances are involved (all with default 1e-6 and each quietly replaced by zero if a negative value is specified): for a quadratic constraint to be considered active, its slack must be at most qctol1 and the maxnorm of the constraint's gradient (i.e., the largest gradient component in absolute value) must be more than qctol2. An "active" quadratic constraint is considered dependent on other such constraints if during QR factorization its gradient's maxnorm is reduced to no more than qctol3 of its original maxnorm.

## 20130622
- Update to CPLEX 12.5.1. 

- New keyword "splitcuts" to control use of lift-and-project cuts on MIP problems.
- New keyword "objrep" controlling whether to replace
  
        minimize obj: v;
  with

        minimize obj: f(x)

  when variable v appears linearly in exactly one constraint of the form::

        s.t. c: v >= f(x);

  or

        s.t. c: v == f(x);

  Default is no for the former, yes for the latter. For more details, see the updated README.cplex.

## 20130606
- Do not complain about a diagonal objective Hessian element of the "wrong" sign if the associated variable is an integer variable, in which case CPLEX seems to not to care about signs, or if reqconvex=2 is specified.

## 20130604
- Fix a bug that led to an error message of the form "logical constraint ... is not an indicator constraint."

## 20130530
- Fix a bug with ignoring SOS1 sets of one element (specified with .sosno).

## 20130522
- Fix bugs with suffix .lazy: problems with quadratic constraints were not handled properly, and a rare case requiring allocation of longer arrays was botched. Now nonzero .lazy values on quadratic constraints give a warning message that such .lazy values are ignored.

## 20130320
- Update to CPLEX 12.5.0.1 (bug fixes from IBM) and, for MS Windows, to incorporate a bug fix to automatic staring of ampl_lic, which now may work better on some versions of MS Windows (not XP). It is still recommended not to rely on automatically starting ampl_lic.

## 20121116
- Add zerohalfcuts to the cuts simultaneously controlled by mipcuts. 
- Update to CPLEX 12.5: add keywords dettimelim, polishafter_timedet, probetimedet, seed, and tunetimedet, and extend timing keyword to allow requesting times in platform-specific "ticks", which CPLEX computes in an unspecified way.

## 20121022
- Add keyword "incompat" with description

  How to treat parameter settings that CPLEX finds incompatible:

      0 = quietly ignore incompatibilities
      1 = report and ignore them (default)
      2 = reject them, refusing to solve.
  or example, CPLEX regards the polishafter_* parameters introduced in CPLEX 11.2 as incompatible with the older polishtime parameter.

## 20121016
- Relink to fix bugs (likely fault) with problems having many indicator constraints (more than 6000 in the example behind this bug fix).

## 20121012
- Relink macosx64 version in hopes of working with MacOSX versions as old as 10.4.

## 20121005
- Fix a glitch with discarding SOS1 sets of size 1 and SOS2 sets of size 2 when explicitly specified by suffixes sosno and ref (a bad idea -- it is much less error prone to use AMPL's <<...>> notation for piecewise-linear terms).

## 20120411
- Update to CPLEX 12.4.0.1 for bug fixes in CPLEX itself.

## 20120405
- For MIP problems, when basis = 1 is in effect and the attempt to return a basis fails, correctly report the objective value of the solution returned.

## 20120320
- Adjust license-check in Linux versions for use with FreeBSD.

## 20111203
- Update to CPLEX 12.4.

## 20111120
- Relink to fix a possible fault with piece-wise linear terms. Absent a fault, the bug was harmless.

## 20111107
- Permit use of single-user licenses.

## 20111003
- Allow double inequalities in indicator constraints, as well as multiple linear constraints connected with && or given in a forall{...} construct.
- When processing ampl.lic, ignore new keywords for ampl.netlic.

## 20110928
- Relink to fix another bug with piece-wise linear terms.

## 20110927
- Fix a bug introduced in 20110909 with handling piecewise-linear terms.

## 20110913
- Increase some array sizes that may have been too small for indicator constraints with an "else" clause, such as

       s.t. bletch: y == 0 ==> z >= zlb else z <= -zub;

## 20110909
- Update to CPLEX 12.3.0.1, which should fix bugs sometimes seen in doing parallel MIP solves and in polishing MIP solutions.

## 20110611
- Correct the signs of .dunbdd values when the primal objective is to be maximized. (CPLEX appears not to take the sense of the primal objective into account when computing a ray of dual unboundedness.)
- Add a description of the new "reqconvex" keyword to README.cplex, and add a note that it may be necessary to specify presolve=0 in $cplex_options to get .dunbdd values.

## 20110607
- Update to CPLEX 12.3.

## 20110527
- Relink to permit a quoted "hostname" for MGR_IP in the ampl.lic file for a floating license.

## 20110512
- Add logic so specifying "prestats=1" for a MIP problem does not disable use of multiple threads.

## 20110426
- Tweak license checker to correct a rare problem on MS Windows systems.

## 20110421
- Adjust basis manipulations so netopt=1 or netopt=2 may provide a better starting basis for finishing the solution of a problem after CPLEX has dealt with an embedded network.
- Adjust prestats to work independently of mipdisplay and display. Now prestats=1 causes summary statistics (if nonzero) for CPLEX's "aggregate" and "presolve" algorithms to be reported in the solve_message. Unfortunately, setting prestats=1 may disable use of multiple threads.

## 20110117
- Mention "cplex" in the "No license for this machine" message.

## 20110113
- Fix operation of "prestats=1", and add "cutstats" keyword (0 or 1, default 0) to control whether the kinds and numbers of cuts are reported in the solve_message.

## 20101211
- Fix bugs in handling nonlinear integer variables. When indicator constraints were present, an erroenous message about a logical constraint not being an integer constraint was possible. In some other cases, wrong initial values might have been provided.

## 20101206
- Set solve_result_num = 567 if the problem has complementarity constraints.

## 20101109
- Adjust to quietly ignore baropt on quadratically-constrained problems (as we get a surprising failure otherwise).

## 20100912
- Update to CPLEX 12.2.