# AMPL Style Guide

Creating clear, consistent, and scalable AMPL models is critical for managing complex optimization workflows. These best practices provide actionable guidelines for naming, organizing, and formatting AMPL models to ensure readability, maintainability, and professional-quality output.

## 1. Organizing Structure
### 1.1. Divide your model into clear sections: 
  - Parameters
  - Sets
  - Variables
  - Constraints
  - Objective Functions
  - Solve Statements
### 1.2. Use Indentation and Formatting
- **Indent Blocks:** Use consistent indentation for readability.
- **Align Declarations:** Align similar constructs for clarity.
    ```ampl
    # Define sets 
    set PRODUCTS;                           # All products 
    set WAREHOUSES;                         # All warehouses
- **Line Breaks:** Break long lines logically.
  ```ampl
  maximize TotalProfit: 
    sum {p in PRODUCTS, w in WAREHOUSES} 
      profit[p, w] * shipment[p, w];
### 1.3. Comments
- **Inline Comments:** Use inline comments sparingly for clarification within a line of code.
  ```ampl
  var shipment {PRODUCTS, WAREHOUSES} >= 0; # Units shipped
- **Section comments:** Briefly describe the purpose of each section or block of code.
  ```ampl
  # Define the set of products and warehouses 
  set PRODUCTS; 
  set WAREHOUSES;
- **Document comments:** Use comments or documentation about key assumptions in the model for future reference.
  ```ampl
  # Assumption: Demand is always non-negative and met in full. 
  param demand {PRODUCTS} >= 0;
- **Header comment block:** Use header comments.
  ```ampl
  # Model Name: Point Selection for Profit Maximization
  # Purpose: Select one point from a set of options to maximize total profit
  # Version: 1.0
  # Last Updated: Jan 2025
### 1.4. Checks infeasibility
- Help ensure that the model's requirements can indeed be met given the available resources and constraints.
  ```ampl
  check: sum{p in PRODUCTS} demand[p] <= total_capacity;
## 2. Naming
### 2.1. General Naming Principles
- **Readable Names:** Use meaningful, descriptive names for `sets`, `parameters`, `variables`, and `constraints`.    
  ```ampl
  warehouse_capacity, transport_cost  # Good practice
  cap, tc                             ! Avoid practice
- **Use Domain Terms:** Align sets, parameters, variables, and constraints names with the terminology of your domain (e.g., logistics, finance).  
  ```ampl
  shipment_volume                     # Good practice
  volume                              ! Avoid practice
- **Use Snake Case:** For multi-word names of `parameters`, and `variables`, use underscores (`_`) to improve readability.  
  ```ampl
  # Good practice
  param cost_per_unit{PROD} >= 0 ; 
  var Shipment{PROD} >= 0 ;               
  
  ! Avoid practice
  param costPerUnit{PROD} >= 0 ; 
  var InventoryLevel{PROD} >= 0 ;                             
- **Consistency:** Maintain consistent patterns for similar items.  
  ```ampl
  # Good practice
  set PRODUCTS;
  set WAREHOUSES;
  
  ! Avoid practice  
  set Routes
- **! Avoid:**
  - **Abbreviations:** Minimize abbreviations unless they are commonly understood in your domain.
  - **Overloading:** Do not use the same name across different types (e.g., avoid using cost for both a parameter and a variable).
### 2.2. Sets
- **Set names are specified using uppercase letters**. Name sets using plural nouns to indicate they represent collections. Ensure the name specifies what the set contains.  
  ```ampl
  set PRODUCTS;
  set WAREHOUSES;
  set CUSTOMERS;
- **Calculated Sets:** Computed sets have the `_` sign at the end. Name calculated sets to indicate their derivation or filtering. (Use words like `valid`, `available`, `filtered`, or `active` to signify calculated sets).  
  ```ampl 
  set ACTIVE_ROUTES_ within ROUTES;                 # Routes that are currently operational.
### 2.3. Parameters
- **Parameter names are specified using lowercase letters**. Use singular nouns for individual parameters. Provide context about what the parameter represents.  
  ```ampl
  param cost_per_unit{PROD} >= 0 ;
  param demand_per_product{PROD} >= 0 ;
- **Group related parameters:**  
  ```ampl
  param production_cost{PRODUCTS} >= 0;             # Cost of producing each product  
  param transport_cost{PRODUCTS, WAREHOUSES} >= 0;  # Transportation cost per unit
- **Calculated Parameters:** Computed parameters have the `_` sign at the end. Use names that reflect how the parameter is derived.
  ```ampl
  # Calculate adjusted demand based on a scaling factor (e.g., demand increased by 20%)
  param adjusted_demand_{p in PROD} = 1.2 * demand[p];

  # Calculate the average cost per unit by dividing total cost by total quantity
  param average_cost_{p in PROD} = total_cost[p] / total_quantity[p];
### 2.4. Variables
- **Variables names begin with uppercase letters**. Use names that reflect the decision being modeled and avoid generic names like `x` or `y` unless absolutely necessary.
  ```ampl
  var Shipment{PROD} >= 0;          # Quantity of items to be shipped for each product
  var Inventory_Level{PROD} >= 0;   # Inventory level for each product
- **Suffixes for Binary or Integer Variables**: Is, Num
  ```ampl
  var IsOpen{WAREHOUSES} binary;    # Binary variable: 1 if warehouse is open, 0 otherwise
  var NumTruck_Count >= 0 integer;  # Integer variable: Number of trucks to be used
- **Calculated Variables**: Computed variables have the `_` sign at the end.
  ```ampl
  # Calculate remaining capacity in warehouses
  var remaining_capacity_[w in WAREHOUSES] = capacity[w] - sum{p in PRODUCTS} shipment[p,w];
### 2.5. Constraints
- **Constraints names begin with** ***uppercase letters*** with combining words. Combine the constraint’s purpose with the entity it applies to.
  ```ampl
  subject to CapacityLimit{w in WAREHOUSES}: 
    sum{p in PRODUCTS} Shipment[p,w] <= capacity[w]; 
  subject to DemandSatisfaction{p in PRODUCTS}: 
    sum{w in WAREHOUSES} Shipment[p,w] = demand[p];
- **Use a shared prefix** for related constraints like Limit, Balance, Level, etc., to denote various constraints.
  ```ampl
  # Supply constraints for each warehouse ensuring supply doesn't exceed capacity
  subject to SupplyLimit{w in WAREHOUSES}:        # Limit on supply per warehouse
    sum {p in PRODUCTS} shipment[p, w] <= capacity[w];        

  # Balance constraints for inventory levels at each warehouse
  subject to InventoryBalance{w in WAREHOUSES}:   # Inventory balance at each warehouse
      sum {p in PRODUCTS} shipment[p, w] - inventory[w] = 0;

  # Level constraints for production to avoid exceeding maximum production levels
  subject to ProductionLevel{p in PRODUCTS}:      # Maximum production level per product
      production[p] <= max_production[p];                     
### 2.6. Objective Functions
- **Action-Oriented:** Use verbs or action-oriented phrases to describe the goal.
- **Single Purpose:** Ensure the name reflects the exact purpose of the objective.
  ```ampl
  maximize TotalProfit
  minimize TotalCost
- **Multi-objective models** should use clearly named weighted components.
  ```ampl
  maximize WeightedObjective: 
    weight_profit * TotalProfit - weight_cost * TotalCost;
## Benefits
- ***Readability:*** Clear visual separation between different model elements.
- ***Debugging:*** Easier to identify computed vs. input elements.
- ***Maintainability:*** Facilitates collaboration and future updates.
- ***Scalability:*** Works well even as models grow in complexity.

Adopting these best practices ensures clarity, consistency, and scalability in AMPL models. By following these guidelines, your models will be easier to read, maintain, and scale, achieving professional-quality optimization workflows. This structured approach enhances collaboration, simplifies debugging, and supports long-term usability, making your models highly effective and user-friendly.


## How To Use It

Just ask ChatGPT:
- ***Please use these rules:***  [Link_To_This_Page]
- ***For changes in the model:*** [Insert_Code_Of_Your_Model]
and you will receive the model taking into account the Best practice rules.