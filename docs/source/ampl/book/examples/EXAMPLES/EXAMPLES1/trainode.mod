set cities;             # Set of cities
param last > 0 integer; # Number of intervals into which
			# a schedule-period is divided
set times := 1..last;   # Set of intervals into which
			# a schedule-period is divided
set schedule within 
    {c1 in cities, t1 in times, c2 in cities, t2 in times: c1 <> c2};
			# Member (c1,t1,c2,t2) of this set represents
			# a train that leaves city c1 at time t1 
			# and arrives at city c2 at time t2
param section > 0 integer;
			# Maximum number of cars in one section of a train
param demand {schedule} > 0 ;
			# For each scheduled train:
			# the smallest number of cars that
			# can meet demand for the train
param distance {c1 in cities, c2 in cities: 
	    exists {t1 in times, t2 in times} (c1,t1,c2,t2) in schedule} > 0;
			# Inter-city distances: distance[c1,c2] is miles
			# between city c1 and city c2
minimize cars: to_come; # Number of cars in the system: 
			# sum of unused cars and cars in trains during
			# the last interval of the schedule-period
minimize miles: to_come; # Total car-miles run by all scheduled trains
			 # in one schedule-period

#  Nodes (constraints)

node N {c in cities, t in times};
			# For every city and time: 
			# unused cars in present interval will equal
			# unused cars in previous interval, 
			# plus cars just arriving in trains,
			# minus cars just leaving in trains

#  Arcs (variables)

arc U {c in cities, t in times} >= 0
      from N[c,t]  to N[c, if t < last then t+1 else 1]
      obj cars (if t = last then 1 else 0);
			# U[c,t] is the number of unused cars stored 
			# at city c in the interval beginning at time t
arc X {(c1,t1,c2,t2) in schedule}
      >= demand[c1,t1,c2,t2]
      <= section * ceil(demand[c1,t1,c2,t2]/section)
      from N[c1,t1]  to N[c2,t2]
      obj cars (if t2 < t1 then 1 else 0)
      obj miles distance[c1,c2];
			# X[c1,t1,c2,t2] is the number of cars assigned
			# to the scheduled train that leaves c1 at t1
			# and arrives in c2 at t2
			# The bounds insure that the cars meet demand,
			# but that they are not so far in excess of demand
			# that unnecessary sections are required
