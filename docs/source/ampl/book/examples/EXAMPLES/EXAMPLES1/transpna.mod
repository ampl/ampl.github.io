set ORIG;   # origins
set DEST;   # destinations

param supply {ORIG} >= 0;   # amounts available at origins
param demand {DEST} >= 0;   # amounts required at destinations

   check: sum {i in ORIG} supply[i] = sum {j in DEST} demand[j];

param rate {ORIG,DEST} >= 0;   # base shipment costs per unit
param limit {ORIG,DEST} > 0;   # limit on units shipped

param alpha >=0, <= 1;

var Trans {i in ORIG, j in DEST}
   >= 1e-10, <= .9999 * limit[i,j], := alpha * limit[i,j];
                               # actual units to be shipped

minimize total_cost:
   sum {i in ORIG, j in DEST}
      rate[i,j] * Trans[i,j]^0.8 / (1 - Trans[i,j]/limit[i,j]);

subject to Supply {i in ORIG}:  
   sum {j in DEST} Trans[i,j] = supply[i];

subject to Demand {j in DEST}:  
   sum {i in ORIG} Trans[i,j] = demand[j];
