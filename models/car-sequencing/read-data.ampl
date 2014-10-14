# This script reads the data for the car sequencing problem from file $file.
# See README.rst for the description of the data format.

# Read data from 10_93.in if $file is not set.
if $file = "" then option file "data/10_93.in";

read NumCars, NumOptions, NumClasses < ($file);
read{o in Options} MaxCarsInBlock[o] < ($file);
read{o in Options} BlockSize[o] < ($file);
param index;
for {c in Classes} {
  read index < ($file);
  let index := index + 1;
  read NumCarsInClass[index], {o in Options} Require[index, o] < ($file);
}
