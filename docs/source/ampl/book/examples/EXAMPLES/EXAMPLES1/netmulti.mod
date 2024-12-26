set CITIES;
set LINKS within (CITIES cross CITIES);

set PRODS;

param supply {PRODS,CITIES} >= 0;  # amounts available at cities
param demand {PRODS,CITIES} >= 0;  # amounts required at cities

check {p in PRODS}: 
   sum {i in CITIES} supply[p,i] = sum {j in CITIES} demand[p,j];

param cost {PRODS,LINKS} >= 0;     # shipment costs/100 packages
param capacity {PRODS,LINKS} >= 0; # max packages shipped of product
param cap_joint {LINKS} >= 0;      # max total packages shipped/link

minimize Total_Cost;

node Balance {p in PRODS, k in CITIES}: 
   net_in = demand[p,k] - supply[p,k];

arc Ship {p in PRODS, (i,j) in LINKS} >= 0, <= capacity[p,i,j],
   from Balance[p,i], to Balance[p,j], obj Total_Cost cost[p,i,j]; 

subject to Multi {(i,j) in LINKS}:
   sum {p in PRODS} Ship[p,i,j] <= cap_joint[i,j];

