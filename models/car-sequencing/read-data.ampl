# This script reads the data for the car sequencing problem from file $file.
#
# The format of the data files is as follows:
#
# * First line: number of cars; number of options; number of classes.
# * Second line: for each option, the maximum number of cars with that
#   option in a block.
# * Third line: for each option, the block size to which the maximum
#   number refers.
# * Then for each class: index no.; no. of cars in this class; for each
#   option, whether or not this class requires it (1 or 0).

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
