# Define indexing sets
set PROD;
set INGR;
set DAYS;
set WEEKEND within DAYS;

# Make sure DAYS and WEEKEND have correct cardinality
check: card(DAYS) == 7;
check: card(WEEKEND) == 2;

# Define the decision variables
var make{PROD} integer, >= 0;

# Define model parameters
param weekday_fee;
param weekend_fee;
param today symbolic;
param fee := if today in WEEKEND then weekend_fee else weekday_fee;
param profit_per_product{PROD};
param limit{INGR};
param usage{INGR, PROD};

# Make sure today is a valid day
check: today in DAYS;

# Define the objective function
maximize total_profit: 
    sum {i in PROD} profit_per_product[i] * make[i] - fee;

# Define the constraints
subject to ingredient_constraints {i in INGR}:
    sum {j in PROD} usage[i,j] * make[j] <= limit[i];
