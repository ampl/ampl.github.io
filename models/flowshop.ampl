# Flowshop problem formulation in AMPL based on
# http://www.localsolver.com/flowshop.html

# Number of jobs
param NumJobs > 0;

# Number of machines
param NumMachines > 0;

# Set of machines
set Machines = 0..NumMachines-1;

# Set of jobs
set Jobs = 0..NumJobs-1;

# Time to process job j on machine m
param ProcessingTime{m in Machines, j in Jobs} >= 0;

# Permutation of jobs
var job{Jobs} in Jobs;

function element;

# End of job j on machine m.
# On machine 0, the first job ends after it has been processed and
# the jth job ends on the time it took to be processed after
# the end of the previous job.
# On machine m, the first job ends on the time it took to be processed after
# the end on the previous machine.
# The jth job on machine m starts when it has been processed by machine m - 1 AND when 
# job j - 1 has been processed on machine m. It ends after it has been processed.
var end{m in Machines, j in Jobs} =
  element({k in Jobs} ProcessingTime[m, k], job[j]) +
  if m = 0 then (if j > 0 then end[m, j - 1])
           else (if j = 0 then end[m - 1, j] else max(end[m, j - 1], end[m - 1, j]));

minimize makespan: end[NumMachines - 1, NumJobs - 1];

s.t. alldiffJobs: alldiff{j in Jobs} job[j];

data;

# Data from Taillard, 20 jobs 5 machines:
# http://mistic.heig-vd.ch/taillard/problemes.dir/ordonnancement.dir/ordonnancement.html

param NumJobs := 20;
param NumMachines := 5;

param ProcessingTime:
   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 :=
0 54 83 15 71 77 36 53 38 27 87 76 91 14 29 12 77 32 87 68 94
1 79  3 11 99 56 70 99 60  5 56  3 61 73 75 47 14 21 86  5 77
2 16 89 49 15 89 45 60 23 57 64  7  1 63 41 63 47 26 75 77 40
3 66 58 31 68 78 91 13 59 49 85 85  9 39 41 56 40 54 77 51 31
4 58 56 20 85 53 35 53 41 69 13 86 72  8 49 47 87 58 18 68 28;
