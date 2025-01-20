# AMPL Style Guide

Creating clear, consistent, and scalable AMPL models is critical for managing complex optimization workflows. The best practices identified in this guide provide actionable guidelines for naming, organizing, and formatting AMPL models to ensure readability, maintainability, and professional-quality output.

## 1. Model Structure

### 1.1. Divide the model into clear sections

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
  # Assumption: unit_cost is always non-negative
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

```{note}
This check could also be performed before loading the data on the [API](#apis) side (specially when using [Python](#python_integration)).
```

## 2. Naming

The most important rule for scalable models is to write descriptive and significant names for the entities in the model, rather than the usual short names used in Maths and Programming (`x`, `i`, `j`, `p`, `q`...). This depends on the context, because short names can help reading some complex expression, specially when using short names for index variables.

### 2.1. General Naming Principles

- **Readable Names:** Use meaningful, descriptive names for `sets`, `parameters`, `variables`, `constraints`, and `objectives`.    
  ```ampl
  warehouse_capacity, transport_cost  # Good practice
  cap, tc                             ! Not recommended
  ```
- **Use Domain Terms:** Align sets, parameters, variables, and constraints names with the terminology of your domain (e.g., logistics, finance).  
  ```ampl
  shipment_volume                     # Good practice
  volume                              ! Not recommended
  ```
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

- Name sets using uppercase letters.
- Name sets using plural nouns to indicate they represent collections.
- Ensure the name specifies what the set contains.
- For multi-word names of sets use underscores (`_`) to combine words and improve readability.
  ```ampl
  set WAREHOUSES;
  set CUSTOMERS;
  set WAREHOUSES {CUSTOMERS};
  set COST_TYPES = {'production', 'transport'};
  ```

### 2.3. Parameters

- Name parameters using lowercase letters.
- Provide context about what the parameter represents.
- For multi-word names of parameters use underscores (`_`) to combine words and improve readability.
  ```ampl
  param cost_per_unit{PRODUCTS};
  param demand_per_product{PRODUCTS};
  ```

### 2.4. Variables

- Name variables starting each word with uppercase letters.
- Use names that reflect the decision being modeled and avoid generic names like `x` or `y`.
  ```ampl
  var Shipment{PRODUCTS, WAREHOUSES} >= 0;
  var InventoryLevel{PRODUCTS} >= 0;
  ```

### 2.5. Constraints

- Name constraints starting each word with uppercase letters.
- Use descriptive names for constraints that actually describe the logic or restriction being modeled. For example, words such as: Limit, Balance, Level can be implemented in the name of restrictions.
  ```ampl
  subject to CapacityLimit{w in WAREHOUSES}: 
    sum{p in PRODUCTS} Shipment[p,w] <= capacity[w];
  ```

```{eval-rst}
.. note::

    Remember that in AMPL you can include logical rules directly in the model. Try to use logical constraints to model business rules or problematic constraints whenever possible.

    .. code-block:: ampl
        
        subject to Shipment{p in PRODUCTS}: 
            Shipment[p,w] == 0 or Shipment[p,w] >= min_shipment[w];
        subject to AlreadyFinished{container in CONTAINERS, t in T}:
            ContainerFinish[c,t] = 1 ==> ContainerMove[c,t+1] = 0;

    See more expressive modeling examples here: `Modeling guide <https://mp.ampl.com/model-guide.html>`_
```

### 2.6. Objective Functions

- Name objectives starting each word with uppercase letters.
- Action-Oriented: Use verbs or action-oriented phrases to describe the goal.
- Single Purpose: Ensure the name reflects the exact purpose of the objective.
  ```ampl
  maximize TotalProfit: sum{p in PROD} Assign[p] * (fixed_profit[p] + variable_profit[p]) ;
  minimize TotalCost: sum{p in PROD} cost[i] * Assign[p];
  ```

```{note}
Remember that AMPL also supports [Multiple, Blended and Lexicographical objectives](https://mp.ampl.com/modeling-mo.html).
``` 

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
