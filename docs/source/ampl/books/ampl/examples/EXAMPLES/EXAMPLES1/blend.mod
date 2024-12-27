set IN;    # inputs
set OUT;   # outputs

param cost {IN} > 0;
param in_min {IN} >= 0;
param in_max {j in IN} >= in_min[j];

param out_min {OUT} >= 0;
param out_max {i in OUT} >= out_min[i];

param io {IN,OUT} >= 0;

var X {j in IN} >= in_min[j], <= in_max[j];

minimize total_cost:  sum {j in IN} cost[j] * X[j];

subject to outputs {i in OUT}:
   out_min[i] <= sum {j in IN} io[i,j] * X[j] <= out_max[i];
