# Lindo Global Changelog

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