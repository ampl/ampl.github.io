# AMPL script to find a solution to the car sequencing model using LocalSolver.

model cp.ampl;
commands read-data.ampl;

if $timelimit = "" then option timelimit 5;
option localsolver_options ('timelimit=' & $timelimit);
option solver localsolver;
solve;
display optionAtPosition;
