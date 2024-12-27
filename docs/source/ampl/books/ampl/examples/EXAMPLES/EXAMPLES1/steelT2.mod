set PROD;           # products
set WEEKS ordered;  # number of weeks

param rate {PROD} > 0;           # tons per hour produced
param inv0 {PROD} >= 0;          # initial inventory
param avail {WEEKS} >= 0;        # hours available in week
param market {PROD,WEEKS} >= 0;  # limit on tons sold in week

param prodcost {PROD} >= 0;      # cost per ton produced
param invcost {PROD} >= 0;       # carrying cost/ton of inventory
param revenue {PROD,WEEKS} >= 0; # revenue/ton sold

var Make {PROD,WEEKS} >= 0;      # tons produced
var Inv {PROD,WEEKS} >= 0;       # tons inventoried
var Sell {j in PROD, t in WEEKS} >= 0, <= market[j,t]; # tons sold

maximize total_profit: 
   sum {j in PROD, t in WEEKS} (revenue[j,t]*Sell[j,t] -
      prodcost[j]*Make[j,t] - invcost[j]*Inv[j,t]);

          # Objective: total revenue less costs in all weeks

subject to time {t in WEEKS}:  
   sum {j in PROD} (1/rate[j]) * Make[j,t] <= avail[t];

          # Total of hours used by all products
          # may not exceed hours available, in each week

subject to balance0 {j in PROD}:
   Make[j,first(WEEKS)] + inv0[j]
      = Sell[j,first(WEEKS)] + Inv[j,first(WEEKS)];

subject to balance {j in PROD, t in WEEKS: ord(t) > 1}:
   Make[j,t] + Inv[j,prev(t)] = Sell[j,t] + Inv[j,t];

          # Tons produced and taken from inventory
          # must equal tons sold and put into inventory

