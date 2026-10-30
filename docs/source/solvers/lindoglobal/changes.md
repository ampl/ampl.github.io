# Lindo Global Changelog

## 20261029
- Fix: with mp2nl=1, multiobjective models (emulated by MP2NL)
  crashed or returned no solution.
- With mp2nl=1, an invalid option or another MP2NL error is reported
  in the solution file (solve_result_num 500 and the message); before,
  the driver exited without a solution file (AMPL reported 999).
- With mp2nl=1 (in lindoglobal_options or on the command line), the
  model is reformulated by MP2NL before LINDO Global solves it.
- New keywords for LINDO global-solver and solver parameters:
  bbsrchmd, bndlim, boxtol, branchlimit, branchmd, cutoff, decomppt,
  deltatol, feastol, heumode, itrlim, iusol, lsolbranlim,
  maxlocalsearch, maxwidmd, nlpsolver, optchkmd, optmode, opttol,
  postlevel, prelevel, quadmd, sollim, usebndlim, widtol;
  param=LS_xPARAM_NAME=value for any LINDO parameter (unknown names and
  rejected values abort with a message); paramfile=name reads a LINDO
  parameter file.
- epsa/epsr descriptions name the LINDO parameters they set.

## 20260615
- Updated to Lindo API 16.
- Added support for ARM-based MacOS.

## 20250527
- Added support for Lindo licenses.
- Updated to Lindo API 15

## 20210406.1
- Possible problem in the licencing routines for computer with many MAC addresses.

## 20210406
- Updated to LINDO API 13, which includes various improvements:

- Global solver
  - Improved recognition and exploitation of convexity of various composite functions.
  - Improved performance for models with convex-concave functions.
  - Models with ratio/fractional terms, including MIP, tend to solve faster, sometimes order of magnitude.
    non-convex quadratically constrained models are solved substantial faster. 
  - Models with e^x and x^k terms are solved faster, "at LP speed."
- Integer Solver  
  - Smarter selection of settings for cut generation and solution heuristics.
- Concurrent LP solver 
  - Improved: (Run Primal, Dual, Barrier simultaneously - stop when any finish)

## 20201005
[MacOS] Added support for older version of MacOS

## 20200914
Added changelog