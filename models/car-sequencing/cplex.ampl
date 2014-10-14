# AMPL script to find a solution to the car sequencing model using CPLEX.

model mip.ampl;
commands read-data.ampl;
option cplex_options 'timelimit=5 mipdisplay=1';
option solver cplex;
solve;
