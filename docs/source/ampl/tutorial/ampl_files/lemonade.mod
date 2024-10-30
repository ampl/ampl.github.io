# Define the decision variables
var lemonade integer, >= 0;
var iced_tea integer, >= 0;

# Define the parameter(s)
param fee = 2;

# Define the objective function
maximize profit: 1.5*lemonade + iced_tea - fee;

# Define the constraints
subject to lemon_constraint: lemonade <= 10;
subject to tea_bag_constraint: iced_tea <= 8;
subject to sugar_constraint: 2*lemonade + iced_tea <= 20;
