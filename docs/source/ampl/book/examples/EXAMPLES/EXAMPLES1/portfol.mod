# quadratic programming for portfolio analysis.
# adapted from gams book, p108.

set Sec;	# securities

param target;	# target mean annual return on portfolio (%)
param mean {Sec};	# mean annual returns on individual securities (%)
param covar {Sec, Sec};	# covariance (%-squared annual return)

var x {Sec} >= 0;	# fraction to invest in each

minimize variance: sum {i in Sec} x[i] * sum {j in Sec} x[j] * covar[i,j];

subject to fractions: sum {i in Sec} x[i] = 1;
subject to meanret: sum {i in Sec} x[i] * mean[i] >= target;

data;

set Sec := hardware, software, showbiz, tbills;

param target := 10;
param mean := hardware 8, software 9, showbiz 12, tbills 7;
param covar:
	hardware software showbiz tbills :=
hardware   4	    3        -1      0
software   3        6         1      0
showbiz   -1        1        10      0
tbills     0        0         0      0 ;
