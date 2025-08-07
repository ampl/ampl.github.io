# BARON Changelog

## 20250806
- Updated to Baron 25.8.5, which inlcludes bug fixes.

## 20241227
- Updated to baron 24.12.21. In addition to bug fixes, this version comes with improvements 
  in memory management, convexity identification, branching, and new relaxation and reduction 
  strategies for certain quadratic and concave programs.

## 20240508
- Updated to baron 24.05.08, that includes improvements in convexity identification, 
  facilities for handling quadratic programs, scaling numerically challenging 
  problems, and range reduction via Fourier-Motzkin elimination
- Added option `seed` to specify the seed for BARON’s random number generator. 
  Changing the value of this option is likely to change the outcome of BARON’s 
  randomized search steps, including starting points and solutions obtained 
  from local search heuristics.

## 20240130
- Updated to baron 24.01.30; In addition to bug fixes, this version comes with a 
  large number of improved algorithms for NLPs, MIQPs, and MINLPs, including local search, 
  reformulations, relaxations, cutting planes, and presolve.

## 20230405
- Fixed baron bundle packaging

## 20230321
- Updated to baron version 20230311; In addition to bug fixes, 
  this version comes with significant improvements in BARON's CPLEX, 
  CBC and IPOPT interfaces, better treatment of convex and quadratic 
  problems, improved cutting, reduction and branching strategies, 
  and much improved continuous and integer presolve algorithms.

## 20220118
- Update to find xpress version 39.01.02

## 20220105
- Fixed bug that was causing `threads` option to fail.

## 20211123
- Fixed a problem where with `iisfind` > 1 IIS were found but not communicated back to AMPL.

## 20211109
- Relinked with ASL 20211109, which allows the use of functions with output arguments in the AMPL session.

## 20210226.1
- Possible problem in the licencing routines for computer with many MAC addresses.

## 20210226
- Relinked with Baron 21.01.13, which includes some bug fixes
- [Linux] Upped minimum requirement to glibc 2.17 due to constraint in the baron library

## 20210111
- Update to Baron 21.01.07, which includes some bug fixes and performance improvements.
- Update to find xpress version 37.01.01

## 20201022
- Update to Baron 20.10.16; which inlcudes some bug fixes and performance improvements 
- [Linux] update to find xpress version 36.01.11

## 20201005
- [MacOS] Added support for older version of MacOS

## 20200921
- [Linux] update to correctly find version 36 of xpress library.

## 20200905
- Update to Baron 20.04.14
- Fixed a bug with iisfind, where the infeasible subset was not returned due to changes in how Baron passes the information back to AMPL
- Fixed a problem with rpath of the OSX shared library.
- Added value `Both` for  the iis suffix, to identify variables and inequality constraints whose lower or upper bounds are in the IIS.

## 20200820
Minor tweaks to -= output.

## 20191216
- Update to Baron 19.12.07, which has performance improvements on large-scale problems and mised-integer QPs.

## 20190908
- Relink to ignore any LOGWAIT keywords in the ampl.lic or ampl.netlic file.

## 20190713
- Update to Baron 19.7.13 to fix a fault seen in the MS Windows binary.

## 20190711
- Update to Baron 19.7.9, which has various improvements and bug fixes.

## 20190322
- Update to Baron 19.3.22, which has various improvements and a new keyword, firstloc. See the updated README.baron or "baron -=" output. The 32-bit binaries remain at version 18.5.8 and do not have the new keyword.

## 20190320
- Fix a bug with unary minus applied to a sum or difference. The resulting nonlinear evaluations were wrong.
- New keywords deltaa, deltar, deltat, deltaterm and associated new solve_result_num = 150. See the updated README.baron or "baron -=" output.

## 20190116
- Fix a glitch with "maxtime=1000". Other maxtime values were unaffected.

## 20181116
- Update to Baron 18.11.12, which has a more robust treatment of cutting planes and better optimality-based range reductions.
- Ignore HEARTBEAT lines in the ampl.lic file.

## 20180928
- Add keywords iisfind, iisint, iisorder related to finding an irreducible infeasible set of constraints and variable bounds for infeasible problems. Baron often reports that the sets it finds may not be irreducible. See the "baron -=" output for more details. New solve_result_num values:
```
201 → infeasible, IIS found
202 → infeasible, IS found, possibly not irreducible
203 → infeasible, IIS sought but not found
```

## 20180925
- Recreate the MacOSX64 bundle so libbaron-osx64.dylib knows to look in the directory containing baron for libiomp5.dylib. This does not matter for some systems.

## 20180823
- Update to Baron 18.8.23, which has some bug fixes and improvements and is only available for 64-bit versions of Linux, MacOSX, and MS Windows. No further updates to 32-bit binaries are expected.

## 20180813
- Fix some trouble with numsol=n for n >= 2: only one solution file was produced, likely not for the best solution found.

## 20180508
- Update to Baron 18.5.8, which has various improvements and bug fixes.

## 20180307
- Arrange for lpsolver=cplex and lpsolver=xpress to work with more recent versions of cplex and xpress, respectively. For MS Windows, currently cplex1280.dll, cplex1271.dll, cplex1270.dll and cplex1263.dll are explicitly recognized. Copying another cplex*.dll to cplex.dll may work if not too old. For example, cplex124.dll is too old.

## 20171013
- Update to Baron 17.10.13 to fix a glitch -- undesired output -- under MS Windows.

## 20171011
- Update to Baron 17.10.10, which has some bug fixes.

## 20170812
- Update to Baron 17.8.7, which has bug fixes, performance improvements, and another builtin local nonlinear solver (FilterSQP). New keyword "nlpsol"; see the "baron -=" output for details. 
- Keyword "filter" is now deprecated (replaced by suitable nlpsol assignments).

## 20170628
- Update to Baron 17.6.24, which has bug fixes and performance improvements.

## 20170511
### Added
- New keyword "version" (no value) causes version, platform, and license to be reported.

## 20170401
- Update to Baron 17.4.1, which has some bug fixes and performance improvements.

## 20170321
- Update libbaron-osx64.dylib (MacOSX only) to look in the directory containing baron (as well as standard places) for libiomp5.dylib.

## 20170121
- Update so lpsolver=cplex and lpsolver=xpress work with current versions of cplex and xpress. This was already true for MacOSX (version 20170116).

## 20170116
- Fix a glitch with multiple objectives: the objective used was not transmitted (via the .sol file) to the AMPL session.
- In the binary for 32-bit MS Windows, fix trouble with "lpsolver=xpress".

## 20170112
- Update to Baron 17.1.2, which has some bug fixes and performance improvements. 
- Specifying "lpsolver=xpress" (when permitted by licensing) now works except for 32-bit MS Windows.

## 20161207
- Update to Baron 16.12.7, which has some bug fixes and performance improvements.

## 20161001
- Fix a bug that sometimes caused baron to go into an infinite loop after solving a problem with defined variables.

## 20160927
- Fix a bug with temporary or time-limited cplex or xpress licenses in conjunction with lpsolver=cplex or lpsolver=xpress. The bug led to a "license not found" message.

## 20160921
- Add "No value is expected." to the description of objbound in the "baron -=" output.

## 20160920
- Fix glitches with keyword lpsolver. If given a bad value, the error message involved some erroneous text. If lpsolver appeared in $baron_options and other settings followed, lpsolver was incorrectly diagnosed as having an incorrect value.
- New keyword "objbound" requests return of suffixes .obj_lb and .obj_ub on the problem and objective for Baron's final lower and upper bounds on the objective value.

## 20160729
- Update to BARON 16.7.29, which has various bug fixes and improvements. No changes to $baron_options.

## 20160531
- Relink MacOSX version so libbaron-osx64.dylib will look for libiomp5.dylib in the directory containing "baron".

## 20160407
- Update to BARON 16.4.4, which has some bug fixes and improvements. Dual variable values are now returned.

## 20160316
- Update to BARON 16.3.16, which has various bug fixes and improvements. No changes to $baron_options.

## 20160129
- Adjust to work when one uses "option presolve 0" (a bad idea) and the problem has some empty constraints.

## 20160122
- Linux 64-bit binary relinked so as not to require GLIBC 2.14.

## 20151205
- Fix a bug affecting "baron ... lpsolver=..." that could cause some licenses not to be returned.
- Update to CPLEX 12.6.3, which affects "lpsolver=cplex".

## 20151125
- For Linux binaries, add the directory containing the binary to the library search rules.

## 20151120
- Update driver to deal with complementarity constraints.

## 20150929
- Update to BARON 15.9.22, to fix a fault that was possible under some conditions.
- New keyword "lpsolver" to specify the choice of LP solver, which matters mainly when there are integer variables: possible values are cbc (default), cplex, or xpress. The last two must be suitably licensed to be used.

## 20150911
- Fix a bug that sometimes affected keyword lsolver under MS Windows.

## 20150826
- Update to version 15.8.26, which has many bug fixes and small performance improvements.

## 20150729
- Add possible solve_result_num value 100 for "numerical difficulties but possibly optimal".
- Adjust MacOSX version so __ZNKSt5ctypeIcE13_M_widen_initEv is not required. It is missing in the C++ run-time libraries on some MacOSX systems.

## 20150630
- Fix some possible trouble with a single-use license.

## 20150605
- Update to BARON 15.6.5, which has various bug fixes.

## 20150529
- Fix a typo in the baron.doc* bundles and add an "INSTALLING" section. 
- Relink the 64-bit Linux version to not require GLIBC 2.14.

## 20150424
- Fix a rarely seen licensing glitch.

## 20150416
- Add keywords maxiter and maxtime; expand description of optfile in the "baron -=" output. Recognize comment lines in optfile (starting with #).

## 20150319
- Improved handling of keyword "numsol"; values > 1 now imply keepsol.