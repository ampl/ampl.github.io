
# LOQO Options

```ampl
ampl: option solver loqo; # change the solver
ampl: option loqo_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

Solver options obtained with `$ loqo -=`.

```
bndpush          initial distance from bounds

bounds           name of MPS BOUNDS section

convex           assert problem is convex

dense            dense window threshold

dual             dual-favored matrix reordering

epsdiag          eps tol diag perturbation

epsnum           eps tol for numerical factorization

epssol           eps tol for forward/backward solve

honor_bnds       honor bounds on variables

honor_bnds_init  honor bnds initially

ignore_initsol   ignore given initial guesses; make automatic choice

inftol           Feasibility tolerance

inftol2          Feasibility tolerance 2

iterlim          Iteration Limit (ITERLIM)

lp_only          linearize only---don't quadraticize

max              maximize the objective

maximize         maximize the objective

maxit            Iteration Limit (ITERLIM)

min              minimize the objective

mindeg           minimum degree matrix reordering

minimize         minimize the objective

minlocfil        minimum local fill matrix reordering

mufactor         mu factor

noreord          no matrix reordering

obj              name of MPS objective row

objno            objective number: 1= first, 0= none

outlev           output level

penalty          penalty parameter

pred_corr        pred= 0, pred_corr= 1, unset= -1

primal           primal-favored matrix reordering

ranges           name of MPS RANGES section

rhs              name of MPS right-hand side section

sdp              assert problem is an SDP

sigfig           significant digits (agreement in primal and dual objectives)

stablty          mixing factor for matrix reordering

steplen          step length reduction factor

timing           timing destination: 1 = stdout, 2 = stderr, 3 = both

timlim           Time limit

verbose          synonym for outlev

version          single-word phrase: report version before solving

wantsol          solution report without -AMPL: sum of
                 1 ==> write .sol file
                 2 ==> print primal variable values
                 4 ==> print dual variable values
                 8 ==> do not print solution message

zero_initsol     start at the origin
```

