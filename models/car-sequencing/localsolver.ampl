# AMPL script to find a solution to the car sequencing model using LocalSolver.

model cp.ampl;
commands read-data.ampl;
option localsolver_options 'timelimit=5';
option solver localsolver;
solve;
display optionAtPosition;
