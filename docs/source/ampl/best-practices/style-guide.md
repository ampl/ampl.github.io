# AMPL Style Guide

Creating clear, consistent, and scalable AMPL models is critical for managing complex optimization workflows. The best practices identified in this guide provide actionable guidelines for naming, organizing, and formatting AMPL models to ensure readability, maintainability, and professional-quality output.

## 1. Model Structure
### 1.1. Divide the model into clear sections: 
  - Sets
  - Parameters
  - Variables
  - Constraints
  - Objective Functions

### 1.2. Use Indentation and Formatting
AMPL supports spaces, indentation and line breaks, so use them to guarantee the readability and understanding of the model.

- **Indent Blocks:** Use consistent indentation for readability.
  ```ampl
  param unit_cost >= 0;                   # Unit cost of the product
  param n_step integer > 0;               # Number of steps in the piecewise linear price function
  ```
- **Align Declarations:** Align similar constructs for clarity.
    ```ampl
    param unit_cost >= 0;                   # Unit cost of the product
    param n_step integer > 0;               # Number of steps in the piecewise linear price function
    param demand {1..n_step} >= 0;          # Demand values at each price step
    param price {1..n_step} >= 0;           # Price values for each demand step
  
    ### VARIABLES
    ...
    ```
- **Line Breaks:** Break long lines logically.
  ```ampl
  maximize TotalProfit: 
    sum {p in PRODUCTS, w in WAREHOUSES}
      profit[p, w] * Shipment[p, w];
  ```

### 1.3. Comments

Single line (`#`) and multi-line C-style comments (`/*...*/`) are allowed in the model. This is helpful to provide explanations of some pieces of the model.

- **Inline Comments:** Use inline comments sparingly for clarification within a line of code.
  ```ampl
  var Shipment {PRODUCTS, WAREHOUSES} >= 0; # Units shipped of a certain product to an specific warehouse
  ```
- **Section & Document comments:** Use comments to describe additional information or key assumptions in the model.
  ```ampl
  # Input parameters defining unit_cost and price steps
  # Assumption: demand is always non-negative
  param unit_cost >= 0;                   
  param n_step integer > 0;
  ```

- **Header comment block:** Use header comments to describe the current version of the model, if many updates are expected to happen.
  ```ampl
  # Model Name: Point Selection for Profit Maximization
  # Purpose: Select one point from a set of options to maximize total profit
  # Version: 2.7
  # Last Updated: 11 April 2025
  ```

### 1.4. Check for infeasibility

Help ensure that the model's requirements can indeed be met given the available resources and constraints.
  ```ampl
  check: sum{p in PRODUCTS} demand[p] <= total_capacity;
  ```
This check can also be performed on the `API` side, before loading the data.

## 2. Naming

The most important rule for scalable models is to write descriptive and significant names for the entities in the model, rather than the usual short names used in Maths and Programming (`x`, `i`, `j`, `p`, `q`...). This depends on the context, because short names can help reading some complex expression, specially when using short names for index variables.

### 2.1. General Naming Principles
- **Readable Names:** Use meaningful, descriptive names for `sets`, `parameters`, `variables`, and `constraints`.    
  ```ampl
  warehouse_capacity, transport_cost  # Good practice
  cap, tc                             ! Not recommended
  ```
- **Use Domain Terms:** Align sets, parameters, variables, and constraints names with the terminology of your domain (e.g., logistics, finance).  
  ```ampl
  Shipment_volume                     # Good practice
  volume                              ! Not recommended
  ```
- **Use Snake Case:** For multi-word names of `sets`, `parameters`, and `variables`, use underscores (`_`) to combine words and improve readability.  
  ```ampl
  param cost_per_unit{PROD} >= 0 ;    # Good practice              
  param costPerUnit{PROD} >= 0 ;      ! Not recommended
  ```
- **Use Snake Case at the End** of computed `sets`, `parameters` and `variables` to denote computed model objects.
  ```ampl
  var Storage_Fraction_{p in PROD, t in 1..nPeriod} =          # Amount of each product in Storage each period
    sum{tt in 1..t} (sum{(i,p) in BLENDING} Blending[i,p,tt]
    - sum{s in STAT, n in 1..nStep} Demand[p,s,tt,n]) * (1-storage_Waste[p]/100) ;  
  ```

  # Compute remaining capacity in warehouses
  var Remaining_Capacity_{w in WAREHOUSES} = capacity[w] - sum{p in PRODUCTS}Shipment[p,w];
- **Consistency:** Maintain consistent patterns for similar items.  
  ```ampl
  # Good practice
  set PRODUCTS;
  set WAREHOUSES;
  
  ! Not recommended  
  set Routes; # rather than ROUTES
  ```
- **! Avoid:**
  - **Abbreviations:** Minimize abbreviations unless they are commonly understood in your domain.
  - **Overloading:** Do not use the same name across different types (e.g., avoid using `cost` for both a parameter and a variable).

### 2.2. Sets
- **Set names are often specified using uppercase letters**. Name sets using plural nouns to indicate they represent collections. Ensure the name specifies what the set contains.
  ```ampl
  set WAREHOUSES;
  set CUSTOMERS;
  set WAREHOUSES {CUSTOMERS};
  ```
### 2.3. Parameters
- **Parameter names are often specified using lowercase letters**. Provide context about what the parameter represents.  
  ```ampl
  param cost_per_unit{PRODUCTS};
  param demand_per_product{PRODUCTS};
  ```
- **Group related parameters:** indexes can be useful to identify parameters related to the same group (like costs). 
  - Instead of:
    ```ampl
    param production_cost{PRODUCTS} >= 0;         # Cost of producing each product
    param transport_cost{PRODUCTS} >= 0;          # Transportation cost per unit
    ```
  - It makes sense to use:
    ```ampl
    set COST_TYPES = {'production', 'transport'}; # Define cost types
    param cost{COST_TYPES, PRODUCTS} >= 0;        # Define a parameter for costs, indexed by products and cost types

    # Use grouped parameter in constraints
    subject to TotalCostConstraint:
      sum{c in COST_TYPES, p in PRODUCTS} cost[c,p] <= budget;
    ```
### 2.4. Variables
- **Variables names are often begin with uppercase letters**. Use names that reflect the decision being modeled and avoid generic names like `x` or `y`.
  ```ampl
  var Shipment{PRODUCTS, WAREHOUSES} >= 0;
  var Inventory_Level{PRODUCTS} >= 0;
  ```
- **Use Prefixes for Binary & Integer Variables:**
  ```ampl
  var IsOpen{WAREHOUSES} binary;    # Binary variable: 1 if warehouse is open, 0 otherwise
  var NumTruck_Count >= 0 integer;  # Integer variable: Number of trucks to be used
  ```
### 2.5. Constraints
- **Constraints names are often begin with** ***uppercase letters*** with combining words. Use descriptive names for constraints that actually describe the logic or restriction being modeled. For example, words such as: Limit, Balance, Level can be implemented in the name of restrictions.
  ```ampl
  subject to CapacityLimit{w in WAREHOUSES}: 
    sum{p in PRODUCTS} Shipment[p,w] <= capacity[w];
  ```
- Remember that in AMPL you can include logical rules directly in the model. Try to use logical constraints to model business rules or problematic constraints whenever possible.
  ```ampl
  subject to Shipment{p in PRODUCTS}: 
    Shipment[p,w] == 0 or Shipment[p,w] >= min_shipment[w];
  ```

See more expressive modeling examples here: [Modeling guide](https://mp.ampl.com/model-guide.html)

### 2.6. Objective Functions
- **Action-Oriented:** Use verbs or action-oriented phrases to describe the goal.
- **Single Purpose:** Ensure the name reflects the exact purpose of the objective.
  ```ampl
  maximize TotalProfit: sum{p in PROD} Assign[p] * (fixed_profit[p] + variable_profit[p]) ;
  minimize TotalCost: sum{p in PROD} cost[i] * Assign[p];
  ```

** Remember that AMPL also supports [Multiple, Blended and Lexicographical objectives](https://mp.ampl.com/modeling-mo.html). 

## Benefits
- ***Readability:*** Clear visual separation between different model elements.
- ***Debugging:*** Easier to identify computed vs input elements.
- ***Maintainability:*** Facilitates collaboration and future updates.
- ***Scalability:*** Works well even as models grow in complexity, or more variables and constraints are added.

Adopting these best practices ensures clarity, consistency, and scalability in AMPL models. By following these guidelines, your models will be easier to read, maintain, and scale, achieving professional-quality optimization workflows. This structured approach enhances collaboration, simplifies debugging, and supports long-term usability, making your models highly effective and user-friendly.

## How To Use It

Just ask ChatGPT:
- ***Please use these rules:*** https://dev.ampl.com/ampl/best-practices/style-guide.html
- ***For changes in the model:*** [Insert_Code_Of_Your_Model]

and you will receive the model taking into account the Best practice rules.