# CONOPT Changelog

## 20250918
- Driver rewritten to use Conopt 4 style options (see -= output)
- Updated libs to CONOPT 4.38


## 20250527
- Fixed inconsistencies in the iterations log


## 20250312
- The default distribution of CONOPT is now this package, based on CONOPT 4. To
  obtain the vestigial CONOPT package, contact AMPL support.
- Updated libs to CONOPT 4.36
- MacOS version is now distributed as a universal binary


## 20240710
- Updated libs to CONOPT 4.35


## 20240418
- CONOPT 4 release


## 20240201
- Relinked with ASL2 20240106 which fixes a bug with constant terms that apparently involve variables, such as (x-x)^2,

## 20211109
- Relinked with ASL2 20211109, which allows the use of functions with output arguments in the AMPL session.

## 20210410.1
- Fixed a possible problem in the licencing routines for computer with many MAC addresses.

## 20210410
- Relinked with ASL2 version 20210410; fixes some problems affecting Hessian computations.

## 20201029
- Relinked with an updated ASL2, which fixes some more minor problems affecting Hessian computations.

## 20201018
- Relinked with an updated ASL2, fixing a bug affecting Hessian computations.

## 20201005
- Relinked with an updated ASL2, fixing a possible problem with piecewise linear terms.

## 20190908
- Relink to ignore any LOGWAIT keywords in the ampl.lic or ampl.netlic file.

## 20190715
- Fix handling of the workmeg keyword to accord with the documentation. It now specifies a (possibly fractional) number of megabytes to allocate. The default value of 0 provides an automatic choice, which usually works well.

## 20190315
- Fix bugs that occasionally affected sparsity computations and that affected "objrep" when several objectives can be adjusted.

## 20181221
- Relink to fix a bug with piecewise-linear terms when "option pl_linearize 0;" is specified in AMPL.

## 20181221
- Relink to fix possible trouble with complicated uses of more than one imported function.

## 20181210
- Relink to fix possible trouble with "and" and "or" expressions in 64-bit binaries.

## 20181120
- Relink to ignore HEARTBEAT lines in the ampl.lic file.

## 20180609
- Relink to fix a fault with an example that used option presolve 0 (a bad idea).

## 20180525
- Relink to compute tanh(x) and tanh'(x) for large |x| without complaint.

## 20180519
- Relink to compute tanh(x) for large x without complaint.

## 20180503
- Relink to fix a bug (wrong gradients) with "hess=0" and some uses of defined variables.

## 20180402
- Relink to fix a bug with nonlinear "if" expressions. Wrong gradients were possible.

## 20180314
- Add a check for complementarity conditions, which conopt does not handle. They now cause conopt to give solve_result_num = 550, which now is mentioned in README.conopt.
- Fix a bug that gave error message "bad *o = ... in heswork".

## 20180302
- Relink to fix error messages "Bad *o = 159 ..." or "... 127 ..." and to fix a bug (e.g., fault) with reading some large .nl files.

## 20180121
- Relink with current ASL to fix a rarely seen bug.

## 20171129
- Relink with current solver-interface library (to be safe).

## 20170801
- Relink to fix a bug, introduced 20170511, with derivatives of abs().

## 20170619
- Relink to fix several obscure bugs.

## 20170515
- Relink to fix a glitch that caused an error message of the form "bad *o = ... in hfg_fwd".

## 20170511
- Relink to fix a bug with defined variables shared by several constraints or objectives: under complicated conditions, it was possible for derivative evaluation errors to be ignored.

## 20160831
- Relink to fix a bug in computing Hessians or Hessian-vector products when the same variable appears alone as the "then" or "else" part of two or more if-then-else expressions.

## 20160608
- Relink to fix a bug with expressions of the form expr^num (with num a numeric constant) in "group partially-separable" contexts.

## 20160329
- Obscure bug fix: relink to fix a differentiation bug with the mod function.

## 20160126
- Update to CONOPT 3.17A, which has some bug fixes and may have improved performance on some problems.

## 20151208
- For those who do not have it, add libgfortran.so.3 to Linux and libgfortran.3.dylib to MacOSX bundles.

## 20150814
- MacOSX binaries relinked to catch errors not reported via errno in evaluating some math functions.

## 20150630
- Fix some possible trouble with a single-use license.

## 20150602
- Relink to fix a bug that could afflict imported functions.

## 20150524
- Relink Linux binaries to look in the current directory for libraries, such as libgfortran*.so*.

## 20150424
- Fix a rarely seen licensing glitch.

## 20150122
- Adjust a test for updated variables. This may sometimes give a small efficiency improvement and may cause smaller numbers of function evaluations to be reported.

## 20141124
- Relink for better handling of imported functions that report an inability compute derivatives.

## 20141013
- Relink macosx binaries so licenses can consider both hostname and local hostname.

## 20141004
- Relink to fix a rarely seen bug in computing derivatives (incorrectly "fixed" in 20140929).

## 20140409
- Recompile Linux binaries with an older gfortran to remove dependencies on GLIBC_2.14 and GFORTRAN_1.4. "conopt -v" shows "driver(20130823), ASL(20140313)".

## 20131023
- Ignore case in MAC addresses during license checks (an issue rarely seen). When ending execution under a floating license, try to read a reply from the license manager to circumvent bug sometimes seen in MS Windows. "conopt -v" shows "driver (20131023)" to reflect today's change.

## 20131018
- Relink to extend library renaming: if an imported-function library name has "_32" or "_64" before the final "." and fails to load (perhaps after changing "32" to "64" or vice versa, as appropriate), try omitting the "_32" or "_64".

## 20130823
- Fix possible litch (error message "bad e->a = ...") with Hessian computations when if-then-else, min(...), and max(...) are involved. Fix bugs with "objno=..." when there are multiple objectives (possible wrong weight in Lagrangian Hessian; trouble when variables appear neither in the selected objective nor in any constraint).

## 20130419
- Fix a rarely seen bug (possible fault) with defined variables.

## 20130320
- Relink MS Windows versions to make automatic starting of ampl_lic work better on some versions of MS Windows (not XP). It is still recommended not to rely on automatically starting ampl_lic.

## 20120320
- Adjust license-check in Linux versions for use with FreeBSD.

## 20120126
- For 64-bit Linux, recompiled under an older Linux to remove dependency on GLIB_2.14.

## 20120120
- Update to version 3.15C.

## 20120117
- Relink to simplify using a 64-bit conopt with a 32-bit AMPL or vice versa when imported functions are involved (loaded from a *.dll file). For a 64-bit conopt, if the library name involves '.' and the final '.' is preceded by "_32", change the "32" to "64". Otherwise, if the library fails to load and there is a '.' in the name, insert "_64" before the final '.'. (For 32-bit solvers, the rules are similar, with the roles of "32" and "64" reversed.)

## 20111229
- Relink for use with single-user licenses.

## 20111220
- Fix a bug with constant (or missing) objectives that sometimes led to an error return (e.g., under Linux).

## 20111107
- Permit use of single-user licenses.

## 20111003
- When processing ampl.lic, ignore new keywords for ampl.netlic.

## 20110527
- Relink to permit a quoted "hostname" for MGR_IP in the ampl.lic file for a floating license. The 32-bit MS Windows version no longer needs any separate *.dll files.

## 20110426
- Tweak license checker to correct a rare problem on MS Windows systems.

## 20110315
- Handle constant objectives without complaint.

## 20110125
- Update to version 3.14V.
- Binaries for MacOSX are now available.