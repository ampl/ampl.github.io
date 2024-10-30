# Define indexing sets
set PROD;
set INGR;

# Define the decision variables
var make{PROD} integer, >= 0;

# Define model parameters
param fee;
param profit_per_product{PROD};
param limit{INGR};
param usage{INGR, PROD};

# Define the objective function
maximize total_profit: 
    sum {i in PROD} profit_per_product[i] * make[i] - fee;

# Define the constraints
subject to ingredient_constraints {i in INGR}:
    sum {j in PROD} usage[i,j] * make[j] <= limit[i];
