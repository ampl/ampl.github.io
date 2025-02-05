# SNOPT Changelog

## 20140313
- snopt.c: new keyword objrep: Whether to replace

        minimize obj: v;
	with

        minimize obj: f(x)

        when variable v appears linearly in exactly one constraint of the form

        s.t. c: v >= f(x);
	
        or
        s.t. c: v == f(x);

        Possible objrep values:

        0 = no
        1 = yes for v >= f(x) (default)
        2 = yes for v == f(x)
        3 = yes in both cases

- snopt.c and README: new solve_result_num value 530 for
  "Indefinite Hessian", which is possible with the default qpcheck = 1
  when the objective is quadratic and the constraints are linear.

## 20140324
- snopt.c: correct last argument passed to sninit_.  This change should
be invisible.

## 20140828
- snopt.c: omit unnecessary include "f2c.h".

## 20150217
- snopt.c:  fix a possible fault with "objrep" on problems with nonlinear
constraints and a linear objective; change objrep default to 3.

## 20150525
- snopt.c:  fix a bug that caused keyword meminc to be ignored, and
arrange for "snopt stub meminc=? ..." to show the default meminc value
(which is 20*(M + N), where M = number of constraints and N = number of
variables).

## 20150821
- snopt.c:  changes sntitl_ to sntitle_ (for SNOPT 7.5).

## 20151025
- snopt.c:  fix incorrect handling of "objno" keyword.

## 20181101
- snopt.c:  fix a glitch with a starting point where a derivative cannot be evaluated.  
  Instead of saying, e.g.,

       SNOPT 7.5-1.2 : Bug: "scream" called.
       -11111 iterations

   say

       SNOPT 7.5-1.2 : Derivative evaluation error.
       0 iterations, infeasibility sum 0

- snopt.c, README.snopt:  add some solve_result_num values for
  unlikely errors:
	
       517	Bad "nn=filename" assignment
       561	Bug: "scream" called
       562	Evaluation error
       563	Derivative evaluation error
       564	Bug: surprise setjmp() return
       565	Floating-point error

## 20190314
- snopt.c:  fix a bug with "objrep" with "var v; minimize c*v;" for c
  values other than 1, and relink to fix objrep bugs with several
  adjustable objectives.

## 20201018
- Relinked with an updated ASL2, fixing a bug affecting Hessian computations.

## 20201030
- Relinked with and updated ASL2, which fixes some minor problems.

## 20201030.1
- Fixed a possible problem in the licencing routines for computer with many MAC addresses.

## 20211109
- Relinked with ASL 20211109, which allows the use of functions with output arguments in the AMPL session.