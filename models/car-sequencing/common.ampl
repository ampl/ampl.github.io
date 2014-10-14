# Car sequencing problem - common declarations.

# Number of cars to produce
param NumCars >= 0;

# Positions of cars in the production sequence
set Positions = 1..NumCars;

# Number of options that can be installed in a car
# (air-conditioning, sun-roof, etc.)
param NumOptions >= 0;
set Options = 1..NumOptions;

# Number of car classes
param NumClasses >= 0;
set Classes = 1..NumClasses;

# Number of cars in class c
param NumCarsInClass{c in Classes} >= 0;
check sum{c in Classes} NumCarsInClass[c] = NumCars;

# Require[c, o] specifies whether class c requires option o.
param Require{Classes, Options} binary;

# The maximum number of cars with option o in a block (sequence).
param MaxCarsInBlock{o in Options} >= 0;

# The block size to which the maximum number refers.
param BlockSize{Options} >= 0;

# Sets of blocks identified by their start positions
set Blocks{o in Options} = 1..NumCars - BlockSize[o] + 1;

# build[c, p] specifies whether class c is built in position p.
var build{c in Classes, p in Positions} binary;

# For each class c, build exactly NumCarsInClass[c] cars of this class.
s.t. numCarsPerClass{c in Classes}:
  sum{p in Positions} build[c, p] = NumCarsInClass[c];

# Build exactly one car in each position of the build sequence.
s.t. oneCarPerPosition{p in Positions}:
  sum{c in Classes} build[c, p] = 1;
