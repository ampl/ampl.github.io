
# ----------------------------------------
# LOCATION-TRANSPORTATION PROBLEM 
# ----------------------------------------

set ORIG;   # shipment origins (warehouses)
set DEST;   # shipment destinations (stores)

param supply {ORIG} > 0;
param demand {DEST} > 0;

var Build {ORIG} binary;    # 1 iff it is built
param fix_cost {ORIG} > 0;

var Ship {ORIG,DEST} >= 0;  # amounts shipped
param var_cost {ORIG,DEST} > 0;

minimize Total_Cost:
   sum {i in ORIG} fix_cost[i] * Build[i] +
   sum {i in ORIG, j in DEST} var_cost[i,j] * Ship[i,j];

subj to Supply {i in ORIG}:
   sum {j in DEST} Ship[i,j] <= supply[i] * Build[i];

subj to Demand {j in DEST}:
   sum {i in ORIG} Ship[i,j] = demand[j];
