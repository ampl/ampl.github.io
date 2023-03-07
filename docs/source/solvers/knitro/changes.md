# KNITRO Changelog

## 20221213
- Updated to Knitro 13.2, changes include:
   - Improved cuts and cut selection strategies for branch-and-bound
   - Several presolve improvements; added keyword: *presolveop_redundant* 
   - Added Gomory cuts, controlled by the keyword: *mip_gomory*
   - Updated settings values for *mip_clique*, *mip_knapsack*, *mip_liftproject*,
     *mip_zerohalf* and *mip_mir*
   - Many buggixes

## 20221123
- Relinked with ASL 20221115, which fixes a rare memory (de)allocation problem

## 20220704
- Updated to Knitro 13.1, changes include:
   - Performance improvements when using the BFGS/LBFGS Hessian approximation.
   - New options : *findiff_estnoise*, *findiff_numthreads*, *bar_mpec_heuristic*,
     *mip_restart*, *mip_heuristic_misqp*"
   - Fixed issue that could lead to non-deterministic behavior on mixed-integer models
		 when applying mixed-integer rounding cuts and using more than one thread.
   - Fixed issue with parallel finite-difference gradients used with mixed-integer
     models in the branch-and-bound algorithm.

## 20220215
- Relinked with Knitro 13.0.1, fixing a bug that could cause a segfault on mixed-integer models with range constraints.

## 20220124
- Relinked to fix a problem arising when solving certain models.

## 20220118
- Updated to be able to use XPRESS libs version 39.01.02.

## 20220104
- Updated to Knitro 13; changes include:
	- an updated, parallel, branch-and bound solvers for MIP optimization (keywords: `mip_numthreads`, `mip_liftproject`,
	  `mip_heuristic_lns`, `mip_cutoff`, `mip_multistart` and `mip_heuristic_diving`).
	- new initial point strategies for non-convex QPs and for QCPs (see keyword `ncvx_qcqp_init`).
	- significant robustness and speed improvements on difficult nonlinear optimization problems.
	- option to use BLIS as a basic linear algebra subroutine library, which offers significant
	  speedups on ARM; it is selectable via the option `blasoption`
	- renamed keywords related to parallelism (see the `knitro -=` output for details)
	- improved performance when using SQP and MISQP algorithms on larger models.

## 20211109
- Relinked with ASL 20211109, which allows the use of functions with output arguments in the AMPL session.

## 20211006
- Relinked with ASL2 version 20211001, fixing a fault arising when cancellation causes a term to completely vanish.

## 20210820
- Fixed a bug involving a defined variable that references another defined variable and that is shared by two or more objectives or constraints.
- Adjust the license check to be more robust when there are many solver threads.
- Fixed a possible problem in the licencing routines for computer with many MAC addresses.

## 20210622
- Updated to Knitro 12.4, which includes bug fixes and improvements on heuristics to solve MIP problems.
- New keywords: `mip_cutting_plane`, `mip_heuristic_diving`, `mip_heuristic_feaspump`, `mip_heuristic_mpec`, 
  `mip_heuristic_strategy`.
- Updated licensing routines to handle busy IP ports when contacting ampl_lic server.

## 20210410
- Relinked with ASL2 version 20210410; fixes some problems affecting Hessian computations.

## 20210330
- Relinked with ASL2 version 20210327: fixes a bug that could cause a fault on some complementarity problems.

## 20210111
- Relinked to be able to use XPRESS libs version 37.01.01. 
- Default outlev is now 0.

## 20201030
- Update to KNITRO 12.3, with bug fixes and improvements in memory usage, speedupds on solving large models with the interior-point algorithm and on least-squares models. 
- New keywords `bar_linsys_storage`, `linsolver_maxitref`, `bfgs_scaling` and new values for `bar_linsys`, `mip_heuristic`, `bar_conic_enable` (see `-=` output).

## 20201030
- Relinked with an updated ASL2, which fixes some more minor problems affecting Hessian computations.

## 20201018
- Relinked with an updated ASL2, fixing a bug affecting Hessian computations.

## 20201005
- Relinked with an updated ASL2, fixing a possible problem with piecewise linear terms.
- [MacOS] Added support for older versions of MacOS.

## 20200914
- Relink to fix problem with the licensing routines.

## 20200905
- Relink with the new version of ASL, which includes a fix related to large blocks of memory.

## 20200503
- Relink the macosx binary to make the fix of 209200414 take full effect.

## 20200502
- Relink the mswin64 binary to make the fix of 209200414 take full effect.

## 20200414
- Relink to fix a rarely seen bug in the interface library. When the bug bit, an error message of the form `Unexpected opno 179 in eval2_ASL()` appeared.

## 20191219
- Relink to fix a rarely seen bug in the interface library. When the bug bit, an error message of the form `Error: Knitro-AMPL failed to add quadratic constraint structure.` appeared.

## 20191204
- Update to KNITRO 12.1.0. New keywords `findiff_relstepsize`, `infeastol_iters`, `pre_improvecoefficients`, `pre_redundancylevel`, `presolveop_tighten`.

## 20190908
- Relink to ignore any LOGWAIT keywords in the ampl.lic or ampl.netlic file.

## 20190711
- Update 64-bit Linux binary so that `lpsolver=xpress` will work with Xpress 8.6.

## 20190605, 20190606
- Update to KNITRO 12.0.0, which has some improvements for mixed-integer programming.

## 20190315
- Fix bugs that occasionally affected sparsity computations and that affected `objrep` when several objectives can be adjusted.

## 20181221
- Relink to fix a bug with piecewise-linear terms when `option pl_linearize 0;` is specified in AMPL.

## 20190207
- Update to KNITRO 11.1.2, which has some bug fixes and (on average) performance improvements. New keywords `bar_maxcorrectors`, `cpuplatform`, `findiff_terminate`, `mip_cutfactor`, `strat_warm_start`. Withdrawn keyword `act_lpsolver` (instead use `lpsolver`).

## 20181221
- Relink to fix possible trouble with complicated uses of more than one imported function.

## 20181210
- Relink to fix possible trouble with `and` and `or` expressions in 64-bit binaries.

## 20181120
- Relink to ignore HEARTBEAT lines in the ampl.lic file.

## 20180925
- Recreate the MacOSX64 bundle so libomp.dylib is a file rather than a MacOSX symbolic link to libomp5.dylib. This only matters to MacOSX systems that do not have libomp5.dylib in one of the usual places.

## 20180816
- Relink to fix possible trouble with identifying quadratic objectives and constraints on large problems.

## 20180619
- Update to KNITRO 11.0.1 to fix a bug seen in a problem with some integer variables and quadratic constraints.

## 20180609
- Relink to fix a fault with an example that used option presolve 0 (a bad idea).

## 20180525
- Relink to compute `tanh(x)` and `tanh'(x)` for large `|x|` without complaint.

## 20180519
- Relink to compute `tanh(x)` for large x without complaint.

## 20180515
- Update to KNITRO 11.0.0, which has some bug fixes and (for some problems) performance improvements. 
- The `lpsolver` keyword now supplies cplexlibname=... or xpresslibname=... when appropriate.

## 20180402
- Relink to fix a bug with nonlinear `if` expressions. Wrong gradients were possible.

## 20180314
- Relink to fix a bug that gave error message `bad *o = ... in heswork`.

## 20180302
- Relink to fix error messages `Bad *o = 159 ...` or `... 127 ...` and to fix a bug (e.g., fault) with reading some large .nl files.

## 20180209
- Fix a KNITRO bug with failed constraint evaluations.

## 20180121
- Relink with current ASL to fix rarely seen bugs.

## 20171218
- Relink to fix possible trouble with defined variables.

## 20171211
- Relink to fix possible (probably unlikely) trouble with quadratic objectives and constraints.

## 20171129
- Relink with current solver-interface library (to be safe).

## 20170803
- Relink to fix possible trouble with `objrep` when the last constraint replaces the objective.

## 20170801
- Relink to fix a bug, introduced 20170511, with derivatives of abs().

## 20170723
- Update to KNITRO 10.3.0, which has some bug fixes and (for some problems) performance improvements.

## 20170619
- Relink to fix several obscure bugs.

## 20170515
- Relink to fix a glitch that caused an error message of the form `bad *o = ... in hfg_fwd`.

## 20170514
- Fix a bug in the KNITRO driver that caused trouble on some problems.

## 20170511
- Relink to fix a bug with defined variables shared by several constraints or objectives: under complicated conditions, it was possible for derivative evaluation errors to be ignored.

## 20161208
- Update to Knitro 10.2.0, which has some bug fixes and performance improvements (64-bit Linux and MacOSX, 32- and 64-bit MS Windows only).

## 20160908
- Update to Knitro 10.1.2, which has some bug fixes.

## 20160831
- Relink to fix a bug in computing Hessians or Hessian-vector products when the same variable appears alone as the `then` or `else` part of two or more if-then-else expressions.

## 20160608
- Update to Knitro 10.1.0, which has some bug fixes. Also fixed: a bug with expressions of the form expr^num (with num a numeric constant) in `group partially-separable` contexts.

## 20160329
- Obscure bug fix: relink to fix a differentiation bug with the mod function.

## 20160111
- Update to Knitro 10.0.1, which has some bug fixes.

## 20151211
- Fix knitro.mswin*.zip bundles: knitro.mswin*.20151210.zip mistakenly contained outdated knitro.exe files.

## 20151210
- Enable demo licenses.

## 20151208
- Linux library search rules adjusted for consistency with other solvers; this should be invisible to most users.

## 20151031
- Update to Knitro 10.0. 
- Changed keyword: `lpsolver` --> `act_lpsolver`. New keywords: `act_qpalg`, `bar_watchdog`, `derivcheck_terminate`, `fstopval`, `ftol`, `ftol_iters`, `maxfevals`. See the `knitro -=` output for details.

## 20150814
- MacOSX binary relinked to catch errors not reported via errno in evaluating some math functions.

## 20150630
- Fix some possible trouble with a single-use license.

## 20150602
- Relink to fix a bug that could afflict imported functions.

## 20150529
- Relink Linux binaries to look initially in the current directory for system libraries.

## 20150424
- Fix a rarely seen licensing glitch.

## 20150226
- Fix a glitch that could give rise to an error message such as `can't evaluate exp(718.754)`.

## 20150203
- Fix a glitch with par_numthreads > 1 that caused some threads to see permuted Jacobian values and perform poorly.

## 20150126
- Relink Linux binaries to not require GLIBC 2.14.

## 20150122
- Relink to avoid trouble from miscomputed function values under unlikely conditions.

## 20150114
- Relink so `par_numthreads=n` with `n` > 1 works as intended. (Version 20150112 was an initial attempt at this that could fault.)

## 20141210
- Update to KNITRO 9.1, which has a new SQP algorithm and changes to some keywords; invoke `knitro -=` for a summary of the keywords.

## 20141124
- Relink for better handling of imported functions that report an inability compute derivatives.

## 20141102
- Relink to catch errors reported by imported functions.

## 20141013
- Relink macosx binary so licenses can consider both hostname and local hostname.

## 20141004
- Relink to fix a rarely seen bug in computing derivatives (incorrectly `fixed` in 20140929).

## 20140918
- Relink MacOSX binary so it will look in the directory containing the knitro binary (as well as in the standard places) for libiomp5.dylib. This library (libiomp5.dylib, a support library for OpenMP) could well be used by other programs (if installed on the current system), in which case the best place for it is probably /usr/local/lib. The updated knitro binary, like the previous one, will also look in /usr/local/lib for libiomp5.dylib.

## 20140409
- Relink 64-bit Linux binary to remove a dependency on GLIBC_2.14. `knitro -v` shows `driver(20140407), ASL(20140313)`.

## 20140306
- Update to KNITRO 9.0.1, which has some bug fixes.

## 20140305
- Relink to fix a possible fault on problems where `objrep` matters. The 32-bit Linux and Solaris-Intel binaries remain at KNITRO 8.1.1.

## 20131219
- Update to KNITRO 9.0.0. New keywords `bar_relaxcons`, `linsolver_ooc`, `lsnumthreads` (synonym `par_lsnumthreads`), `optionsfile`, `tuner`, `tuner_maxtime_cpu`, `tuner_maxtime_real`, `tuner_optionsfile`, `tuner_outsub`, `tuner_terminate`. More values (2 and 3, rather than just 0 and 1) for `feasible`. New suffixes `cfeastol`, `relaxbnd`, `xfeastol`. See the updated documentation.

## 20131023
- Ignore case in MAC addresses during license checks (an issue rarely seen). When ending execution under a floating license, try to read a reply from the license manager to circumvent bug sometimes seen in MS Windows.

## 20131018
- Relink to extend library renaming: if an imported-function library name has `_32` or `_64` before the final `.` and fails to load (perhaps after changing `32` to `64` or vice versa, as appropriate), try omitting the `_32` or `_64`.

## 20131011
- When more than one objective is present, if objno is not specified in $knitro_options, behave like other solvers by assuming objno=1, rather than giving exit code 1.

## 20130823
- Fix possible litch (error message `bad e->a = ...`) with Hessian computations when if-then-else, min(...), and max(...) are involved. Fix bug with `objno=...` when there are multiple objectives (possible wrong weight in Lagrangian Hessian).

## 20130606
- Relink to fix a fault that was sometimes possible with `objrep`=2 or `objrep`=3.

## 20130525
- Adjust driver to accept problems with nodes and arcs.

## 20130419
- Fix a rarely seen bug (possible fault) with defined variables.

## 20130320
- Relink MS Windows versions to make automatic starting of ampl_lic work better on some versions of MS Windows (not XP). It is still recommended not to rely on automatically starting ampl_lic.

## 20130308
- Relink MacOSX version to remove dependency on /usr/local/lib/libgomp1.dylib .

## 20130130
- Relink 64-bit Linux version to avoid the need for GLIBC_2.14.

## 20121220
- Update to KNITRO 8.1 (currently 8.1.1).

## 20120813
- Relink 64-bit Linux version to avoid the need for GLIBC_2.14.

## 20120624
- Relink to fix a bug with complementarity problems having integer variables. (KNITRO still does not handle such problems well.) Again add vcomp100.dll to the mswin64 bundle; it was mistakenly left out of recent versions of this bundle.

## 20120620
- Relink to give a sparser Hessian in some cases of division by a constant.

## 20120608
- Fix a glitch that prevented a .sol file from being written when hessopt=n appears in $knitro_options with n = 2, 3, 4, or 6. (These settings are probably seldom if ever desirable.)

## 20120320
- Adjust license-check in Linux versions for use with FreeBSD.

## 20120120
- Relink to handle library names with '.' in a directory name but not in the basename (i.e., the name of the imported-function library).

## 20120117
- Relink to simplify using a 64-bit knitro with a 32-bit AMPL or vice versa when imported functions are involved (loaded from a *.dll file). For a 64-bit knitro, if the library name involves '.' and the final '.' is preceded by `_32`, change the `32` to `64`. Otherwise, if the library fails to load and there is a '.' in the name, insert `_64` before the final '.'. (For 32-bit solvers, the rules are similar, with the roles of `32` and `64` reversed.)

## 20120115
- Adding Microsoft's `redistributable` vcomp100.dll to the mswin64 bundle for KNITRO. It (vcomp100.dll) is only licensed for use with knitro.exe and other programs compiled by Microsoft's Visual Studio 10. If knitro.exe runs on your system without adding vcomp100.dll from the knitro.mswin64.*.zip bundle, then your system must already have a copy of vcomp100.dll in $Path, in which case you do not need a second copy.

## 20111229
- Relink for use with single-user licenses.

## 20111206
- Update to KNITRO 8.0. There is no 32-bit MacOSX version; use the 64-bit version instead. (You can use a 32-bit AMPL with a 64-bit solver, and vice versa.) The MKL blas are now built into the knitro binaries.

## 20111107
- Permit use of single-user licenses.

## 20111018
- Relink to fix possible trouble with some complementarity problems.

## 20111005
- Fix a possible fault in some cases when `objrep` > 0.

## 20111003
- When processing ampl.lic, ignore new keywords for ampl.netlic.

## 20110915
- Adding MKL blas libraries to mswin32 and mswin64 bundles.

## 20110822
- New keyword available in $knitro_options: `objrep` controls whether a linear objective involving a single variable that appears linearly in exactly one constraint is replaced by the body of the constraint. Invoke `knitro -=` for details.
- Complementarity problems are now handled in full generality.
- A rarely-seen fault (a bug in the solver-interface library) is now fixed.

## 20110527
- Relink to permit a quoted `hostname` for MGR_IP in the ampl.lic file for a floating license.

## 20110426
- Tweak license checker to correct a rare problem on MS Windows systems.

## 20110117
- Mention `knitro` in the `No license for this machine` message.

## 20101013
- Update to KNITRO 7.0.