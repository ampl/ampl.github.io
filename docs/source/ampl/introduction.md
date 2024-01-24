# Quick introduction

AMPL (A Mathematical Programming Language) is a high-level language for expressing optimization models. It is widely used in academia and industry to model and solve linear, nonlinear, and integer optimization problems.

With AMPL you can solve your models with a large variety of solvers, such as [HiGHS](https://ampl.com/products/solvers/open-source-solvers/), [Gurobi](https://ampl.com/products/solvers/solvers-we-sell/gurobi/), [CPLEX](https://ampl.com/products/solvers/solvers-we-sell/cplex/), or [XPRESS](https://ampl.com/products/solvers/solvers-we-sell/xpress/). You can
use AMPL through a command-line interface or via an [API](apis.rst).

## AMPL Syntax

AMPL syntax matches naturally the mathematical description of the traditional algebraic descriptions
of models as you can see in the following example:

- Traditional informal algebraic description of a model:

```{eval-rst}
.. math::
  \def\entity#1{{\color{##7E78D3}{#1}}}
  \def\index#1{{\color{##307090}{#1}}}
  \def\comment#1{: {\color{##7A8596}{\text{#1}}}&}
  \def\statement#1{{\color{##7FA492}{\text{#1}}}}
  \begin{align}
  & \entity{R} \comment{a set of raw materials}\\
  & \entity{P} \comment{a set of products}\\
  & \\
  & \entity{a}_\index{ij}, \index{i} \in \entity{R}, \index{j} \in \entity{P}  \comment{input-output coefficients}\\
  & \entity{b}_\index{i}, \index{i} \in \entity{R}  \comment{units available}\\
  & \entity{c}_\index{j}, \index{j} \in \entity{P}  \comment{profit per unit}\\
  & \entity{u}_\index{j}, \index{j} \in \entity{P}  \comment{production limit}\\
  & \\
  & \entity{x}_\index{j}, \index{j} \in \entity{P}, 0 \leq \entity{x}_\index{j} \leq \entity{u}_\index{j}   \comment{units of j produced}\\
  & \\
  & \statement{maximize  } \sum_{\index{j} \in \entity{P}} \entity{c}_\index{j}\entity{x}_\index{j} \comment{total profit}\\
  & \\
  & \statement{subject to  } \sum_{\index{j} \in \entity{P}} \entity{a}_\index{ij}\entity{x}_\index{j} \leq \entity{b}_\index{i}, \index{i} \in \entity{R}  \comment{limited availability of material}\\
  \end{align}
```

- Corresponding AMPL model:

  ```ampl
  set R; # a set of raw materials
  set P; # a set of products
  
  param a {R, P} >= 0; # input-output coefficients
  param b {R} > 0; # units available
  param c {P} > 0; # profit per unit
  param u {P} > 0; # production limit

  var x {j in P} >= 0, <= u[j]; # units of j produced

  maximize total_profit:
      sum {j in P} c[j] * x[j]; # total profit
  subject to supply {i in R}:
      sum {j in P} a[i,j] * x[j] <= b[i]; # limited availability of material
  ```
  Single-letter names for illustration purposes only! With AMPL you can use meaningful names for better model maintainability!

To get started with AMPL, you will need to learn the syntax of the language. You can find a reference manual and examples on the AMPL website ([https://www.ampl.com/](https://www.ampl.com/)) or in the AMPL book ([https://ampl.com/learn/ampl-book/](https://ampl.com/learn/ampl-book/)). There are also online resources and courses available to help you learn AMPL.

## AMPL Entities

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
- `model model_file.mod;`: specifies the location of the model file
- `data data_file.dat;`: specifies the location of the data file
- `option option_name option_value;`: specifies options for the solver
- `solve;`: solves the optimization model
- `display expression;`: displays the values of the decision variables, objective function, and constraints
- `let name := value;`: assigns a value to a declared parameter or a decision variable

Here is an example of a simple AMPL script:
```ampl
# specify the model and data files
model model_file.mod;
data data_file.dat;

# specify the solver options
option solver highs;

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