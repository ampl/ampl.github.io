set PROD;     # products
param T > 0;  # number of weeks

param rate {PROD} > 0;         # tons per hour produced
param avail {1..T} >= 0;       # hours available in week
param profit {PROD,1..T};      # profit per ton
param market {PROD,1..T} >= 0; # limit on tons sold in week

var Make {p in PROD, t in 1..T} >= 0, <= market[p,t];
			       # tons produced

maximize total_profit:
   sum {p in PROD, t in 1..T} profit[p,t] * Make[p,t];

	# total profits from all products in all weeks

subject to time {t in 1..T}:
   sum {p in PROD} (1/rate[p]) * Make[p,t] <= avail[t];

	# total of hours used by all products
	# may not exceed hours available, in each week
