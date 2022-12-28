# Quick introduction

AMPL (A Mathematical Programming Language) is a high-level language for expressing optimization models. It is widely used in academia and industry to model and solve linear, nonlinear, and integer optimization problems.

To use AMPL, you will need to install a solver, such as CPLEX, Gurobi, or XPRESS. You can
use AMPL through a command-line interface or via an [API](apis.md).

## AMPL Syntax

To get started with AMPL, you will need to learn the syntax of the language. You can find a reference manual and examples on the AMPL website ([http://www.ampl.com/](http://www.ampl.com/)) or in the AMPL book ([https://ampl.com/learn/ampl-book/](https://ampl.com/learn/ampl-book/)). There are also online resources and courses available to help you learn AMPL.

Here are some simple examples of the basic elements of an AMPL model:

### Sets

Sets are used to define the sets of decision variables and constraints. For example, you might define a set of cities, a set of products, or a set of time periods.

```ampl
# define a set of cities
set CITIES;

# define a set of products
set PRODUCTS;

# define a set of time periods
set PERIODS;
```

### Parameters

Parameters are used to define the data for your model. For example, you might define the cost of each product, the demand for each product, or the capacity of each facility.

```ampl
# define the cost of each product
param cost{PRODUCTS};

# define the demand for each product
param demand{PRODUCTS};

# define the capacity of each facility
param capacity{CITIES};
```

### Decision variables

Decision variables represent the decisions you need to make in your model. For example, you might define a binary variable to represent whether a product is produced at a particular facility, or a continuous variable to represent the amount of a product that is produced.

```ampl
# define a binary variable to represent whether a product is produced at a facility
var x{PRODUCTS, CITIES} binary;

# define a continuous variable to represent the amount of a product that is produced
var y{PRODUCTS, PERIODS} >= 0;
```

### Objective function

The objective function defines the goal of your optimization model. For example, you might want to maximize profit, minimize cost, or maximize customer satisfaction.

```ampl
# maximize profit
maximize total_profit:
  sum{p in PRODUCTS, c in CITIES} (x[p,c] * (demand[p] - cost[p]));

# minimize cost
minimize total_cost:
  sum{p in PRODUCTS, c in CITIES} (x[p,c] * cost[p]);
```

### Constraints

Constraints define the limitations of your model. For example, you might have a capacity constraint that limits the amount of a product that can be produced at a facility, or a budget constraint that limits the amount of money you can spend.

```ampl
# capacity constraint
subject to capacity_constraint{c in CITIES}:
  sum{p in PRODUCTS} x[p,c] <= capacity[c];

# budget constraint
param budget;
subject to budget_constraint:
  sum{p in PRODUCTS, c in CITIES} (x[p,c] * cost[p]) <= budget;
```

## AMPL Scripting

Here are some examples of the most important AMPL scripting commands:
- `model model.mod;`: specifies the location of the model file
- `data data.dat;`: specifies the location of the data file
- `option option_name option_value;`: specifies options for the solver
- `solve;`: solves the optimization model
- `display expression;`: displays the values of the decision variables, objective function, and constraints
- `let name := value;`: assigns a value to a parameter or a decision variable

Here is an example of a simple AMPL script:
```ampl
# specify the model and data files
model model.mod;
data data.dat;

# specify the solver options
option solver cplex;

# solve the model
solve;

# display the values of the decision variables, objective function, and constraints
display x, y, total_profit, capacity_constraint, budget_constraint;

# assign a new value to a parameter
let budget := 100;

# re-solve the model
solve;

# display the new values of the decision variables and objective function
display x, y, total_profit;
```