# AMPL script to find a solution to the car sequencing model using CPLEX.

model mip.ampl;
commands read-data.ampl;

if $timelimit = "" then option timelimit 5;
option cplex_options ('mipdisplay=1 timelimit=' & $timelimit);
option solver cplex;
solve;
display optionAtPosition;
