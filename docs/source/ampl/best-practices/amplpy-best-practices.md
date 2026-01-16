# Amplpy Best Practices
## Introduction
`amplpy` is a Python library that acts as an interface to AMPL (A Mathematical Programming Language), allowing users to leverage AMPL’s powerful modeling and optimization features alongside Python’s capabilities for data manipulation, machine learning, and analysis. This integration enhances productivity and enables users to seamlessly work with optimization problems within the Python ecosystem.

AMPL and solvers are available as Python packages for **Windows**, *Linux*, and *macOS*. This guide provides detailed instructions on how to install and set up `amplpy` on both local machines and cloud environments, ensuring you can start optimizing models quickly.

## Section 1: Install AMPL, amplpy, and Set Up the AMPL Environment

1. **Install AMPL through the `amplpy` Library** 
    To install `amplpy`, run the following command in your terminal or command prompt:
    ```python
    python -m pip install amplpy --upgrade 
    ```
    This command installs or upgrades the amplpy package to the latest version.

2. **Get your free license**
    - You can download the AMPL Community Edition from the [Community Edition page](https://ampl.com/ce/). The Community Edition provides free access to AMPL with open-source solvers (e.g., HiGHS, CBC, Couenne, Ipopt, Bonmin) with no size limits in your problems. You can also use commercial solvers via the [NEOS Server](https://www.neos-server.org/). The Community Edition is free for educational, small projects, prototyping and solver testing. There are also commercial licenses for AMPL.

3. **Install Solvers and Activate AMPL License**
    Once you’ve installed `amplpy`, you can install solvers. Run the following command:
    ```python
    python -m amplpy.modules install highs gurobi xpress cplex       # Automatically installs AMPL with any solver
    ```
    Run these commands to activate your AMPL license and verify it:
    ```python
    python -m amplpy.modules activate <license-uuid>    # # Replace <license-uuid> with your unique license key
    python -m amplpy.modules run ampl -vvq              # Verify that the license has been activated successfully
    ```
   This will install solvers such Gurobi and activate AMPL using the provided license key.

4. **Import AMPL in Python**
    Once AMPL is installed and activated, you can start using it in Python. Import the `AMPL class` and initialize it:
    ```python
    from amplpy import AMPL
    ampl = AMPL()                                       # Instantiate the AMPL object
    ```
    Ensure you have the latest version of `pip` installed before installing `amplpy`. Upgrade using the following command:
    ```python
    python -m pip install --upgrade pip
    ```
    For complete documentation on `amplpy.modules`, visit: [AMPL Modules for Python](https://dev.ampl.com/ampl/python/modules.html).

Note: This guide assumes there is no other local AMPL installation (like the stand-alone version or AMPLIDE). If there is already an AMPL version installed, Amplpy will be able to find the license and solvers in the local AMPL installation directory.

### **For Google Colab or Jupyter notebooks:**
Google Colab offers a default [AMPL Community Edition](https://ampl.com/ce/) license, which provides free access to AMPL along with open-source solvers or commercial solvers via the `gokestreal` interface for [NEOS Server](https://www.neos-server.org/).
- **1. Install `amplpy` and Dependencies**
    To install `amplpy` in Google Colab, use the following command:
    ```python
    %pip install -q amplpy
- **2. Integrate AMPL with Google Colab**
    Once `amplpy` is installed, you can initialize AMPL in Google Colab by calling the `ampl_notebook` function, which automatically sets up the necessary solvers and license:
    ```python
    from amplpy import AMPL, ampl_notebook
    ampl = ampl_notebook(
    modules=["coin", "highs", "cplex", "gurobi"],   # Solvers to install
    license_uuid="default"  )                           # Use the default license
    ```
    This command will set up AMPL in the notebook with the required solvers and register magic commands for seamless operation.
- **3. Alternative Setup: Import AMPL Directly in Jupyter Notebooks** 
    ```python
    from amplpy import AMPL
    ampl = AMPL()               # Instantiate AMPL object directly if AMPL is already available
    
### Conclusion

Following this section, you can easily set up amplpy for local development or cloud-based environments like Google Colab or Docker containers. By integrating Python with AMPL, you gain the flexibility to work with powerful solvers and modeling capabilities, while also leveraging Python's data science ecosystem for advanced analysis and optimization tasks.

---

## Section 2: Create or Load an AMPL Model

- ### 2.1 Load model from Files
    To ensure readibility and maintainance of the model, it is a good practice to write the AMPL models in a text file names `model.mod` and save it in your working directory.

    Here's an example of the content you should include in the `model.mod` file, which defines the sets, parameters, variables, objective function, and constraints:
    ```python
    ### SETS
    set NUTR;                           # Set of nutrients
    set FOOD;                           # Set of food items
    set LINKS within NUTR cross FOOD;   # Nutrient-food relationships

    ### PARAMETERS
    param cost {FOOD} > 0;              # Cost of each food item
    param f_min {FOOD} >= 0;            # Minimum amount of each food item
    param f_max {j in FOOD} >= f_min[j];  # Maximum amount of each food item
    param n_min {NUTR} >= 0;            # Minimum nutritional requirement for each nutrient
    param n_max {i in NUTR} >= n_min[i];  # Maximum nutritional requirement for each nutrient
    param amt {LINKS} >= 0;             # Amount of nutrient per food item

    ### VARIABLES
    var Buy {j in FOOD} >= f_min[j], <= f_max[j];  # Amount of each food item to buy

    ### OBJECTIVE FUNCTION
    minimize Total_Cost:  sum {j in FOOD} cost[j] * Buy[j];  # Minimize total cost
    ``` 

    In Google Colab and Jupyter notebooks, you can directly create the `model.mod` file using the `%%writefile` magic command. This command allows you to write the model to a file without needing to leave the notebook environment. Here’s how you can do it:
    ```python
    %%writefile model.mod
    ### Insert Model from 2.1 ###
    ```
    This will create a file named `model.mod` in the working directory of your Google Colab session with the content from the code block above.

- #### **2.1.1 Load the Model**
    Once you've created the `model.mod` file, you can load it into your AMPL session.
    ```python
    ampl.read('model.mod')              # Reads the model file and loads it into the AMPL session
    ```
- ### 2.2 Alternative methods to load small models
    Instead of writing the model to a file, you can define small models (a model with less than 20 lines) directly as a string and pass them to AMPL using one of the following methods.
- #### **2.2.1 Using the `eval()` Method for small models**
    In Python, you can load the model by passing the AMPL code directly as a string using the `ampl.eval()` method. This method allows you to dynamically pass AMPL model code into the session:
    ```python
    ampl.eval(r"""
    ### Insert Model from 2.1 ###
    """)
    ```
- #### **2.2.2 Using %%ampl_eval Cells (Jupyter Notebook Only) for small models**
    In Google Colab and Jupyter Notebooks, you can use `%%ampl_eval` magic at the beginning of the cells to run AMPL code directly from the notebook. This cell magic command is similar to using `ampl.eval("""cell content""")` but could be convenient for interactive notebook environments:
    ```python
    %%ampl_eval
    ### Insert Model from 2.1 ###
    ```
    By using this method, you can insert and run the AMPL model code directly within the notebook cells, allowing for a seamless experience.
    
    Note: Using the `eval()` method or the `%%ampl_eval` magic to write large models is generally considered bad practice in terms of readibility. However, they can be useful in specific cases when working with small models. It is always preferable to use the `ampl.read('model.mod')` statement introduced in the section 2.1.1.
---

## Section 3: Add Data to the Model

- ### **3.1 Use Python Data Structures**

Native data structures in Python can be loaded seamlessly into AMPL through direct assign or 

- #### 3.1.1. Use Lists:
    - **Assigning a List Directly**
        You can directly assign values to AMPL sets using Python lists:
        ```python
        ampl.set["FOOD"] = ['BEEF', 'CHK', 'FISH', 'HAM', 'MCH', 'MTL', 'SPG', 'TUR']  # Set FOOD
        ```
        
    - **Using a Dictionary's Keys** 
        If food items are already stored as keys in a dictionary, extract them and assign them to the `FOOD` set in AMPL:
        ```python
        ampl.set["FOOD"] = list(foods.keys())           # Set the 'FOOD' set in AMPL using the keys from the foods dictionary
        ```
    - **Through set_values** 
        You can also use Set objects and the method `set_values` to load the values. For example, consider the following set in AMPL:
        ```
        set A;
        ```
        In Python, you can dump data from a list to A using `set_values`:
        ```python
        A = ampl.set['A']
        A.set_values([1, 2, 3])
        ```
        
- #### 3.1.2. Use Python Dictionaries
    - ##### Direct Assignment of Values
        For a straightforward approach, you can directly assign values to AMPL parameters using Python dictionaries. Here’s how to do it for food costs, considering there is a "FOOD" set, and a "cost" parameter in AMPL:
        ```ampl
        set FOOD;
        param cost{FOOD};
        ```

        Given the following Python dictionary, we can easily load the data into the model:

        ```python
        # Define the cost parameter for each food item
        cost = {
        "BEEF": 3.59,  # Cost per unit of BEEF
        "CHK":  2.59,  # -//- CHK
        "FISH": 2.29,  # -//- FISH
        "HAM":  2.89,  # -//- HAM
        "MCH":  1.89,  # -//- MCH
        "MTL":  1.99,  # -//- MTL
        "SPG":  1.99,  # -//- SPG
        "TUR":  2.49}  # -//- TUR

        ampl.set["FOOD"] = cost.keys()    # Set the 'FOOD' set in AMPL using the keys from the foods dictionary
        ampl.param["cost"] = cost         # Set the 'cost' param in AMPL using the cost dictionary
        ```

    - ##### Assigning Values from Composite Data
        For more complex data, you can use dictionary comprehensions to assign multiple attributes to AMPL parameters. Considering the following declarations in AMPL:

        ```ampl
        set NUTR;
        set FOOD;
        param cost {FOOD} > 0;
        param f_min {FOOD} >= 0;
        param f_max {j in FOOD} >= f_min[j];
        param n_min {NUTR} >= 0;
        param n_max {i in NUTR} >= n_min[i];      
        param amt {NUTR,FOOD} >= 0;
        ```

        Loading the data in Python for the previous model:

        ```python
        # Define a dictionary with FOOD information for f_min and f_max
        foods = {
        "BEEF": (3.59, 2, 10),                  
        "CHK": (2.59, 2, 10),
        "FISH": (2.29, 2, 10),
        "HAM": (2.89, 2, 10),
        "MCH": (1.89, 2, 10),
        "MTL": (1.99, 2, 10),
        "SPG": (1.99, 2, 10),
        "TUR": (2.49, 2, 10)}
        
        ampl.set['FOOD'] = list(foods.keys())   # Define the cost parameter for each food item
        
        nutrs = {                               # Define nutrient ranges
        "A":    (700, 20000),
        "C":    (700, 20000),
        "B1":   (700, 20000),
        "B2":   (700, 20000),
        "NA":   (0,   50000),
        "CAL":  (16000, 24000),}

        ampl.set['NUTR'] = list(nutrs.keys())
        ampl.param["cost"] = cost
        
        # Map specific attributes to AMPL parameters:
        ampl.param["cost"]  = {food:  cost for food, (cost, _, _)  in foods.items()}# Extract 'cost'
        ampl.param["f_min"] = {food: f_min for food, (_, f_min, _) in foods.items()}# Extract 'f_min'
        ampl.param["f_max"] = {food: f_max for food, (_, _, f_max) in foods.items()}# Extract 'f_max'

        ampl.param["n_min"] = {nutr: n_min for nutr, (n_min, _) in nutrs.items()}   # Extract 'n_min'
        ampl.param["n_max"] = {nutr: n_max for nutr, (_, n_max) in nutrs.items()}   # Extract 'n_max'
        amt = {
            ('A', 'BEEF'):  60, ('C','BEEF'):   20, ('B1','BEEF'):  10, ('B2','BEEF'):  15,
            ('NA','BEEF'):  928, ('CAL','BEEF'): 295, ('A','CHK'):    8, ('B1','CHK'):   20,
            ('B2','CHK'):   20, ('NA','CHK'):   2180, ('CAL','CHK'):  770, ('A','FISH'):   8,
            ('C','FISH'):   10, ('B1','FISH'):  15, ('B2','FISH'):  10, ('NA','FISH'):  945,
            ('CAL','FISH'): 440, ('A','HAM'):    40,('C','HAM'):    40, ('B1','HAM'):   35,
            ('B2','HAM'):   10, ('NA','HAM'):   278, ('CAL','HAM'):  430, ('A','MCH'):    15,
            ('C','MCH'):    35, ('B1','MCH'):   15, ('B2','MCH'):   15, ('NA','MCH'):   1182,
            ('CAL','MCH'):  315, ('A','MTL'):    70, ('C','MTL'):    30, ('B1','MTL'):   15,
            ('B2','MTL'):   15, ('NA','MTL'):   896, ('CAL','MTL'):  400, ('A','SPG'):    25,
            ('C','SPG'):    50, ('B1','SPG'):   25, ('B2','SPG'):   15, ('NA','SPG'):   1329,
            ('CAL','SPG'):  379, ('A','TUR'):    60, ('C','TUR'):    20, ('B1','TUR'):   15,
            ('B2','TUR'):   10, ('NA','TUR'):   1397, ('CAL','TUR'):  450,}
        
        ampl.set['LINKS'] = set(amt.keys())     # Set the 'LINKS' set in AMPL using the keys from the 'amt' dictionary (nutrient-food pairs)
        ampl.param['amt'] = amt                 # Assign the nutrient amounts for each food item in AMPL
        ```
        
- #### 3.1.3 Use Pandas DataFrames
    Pandas is useful for handling data in a tabular format, which can be easily imported into AMPL using [`set_data()`](https://amplpy.ampl.com/en/latest/classes/ampl.html#amplpy.AMPL.set_data) and [`get_parameter()`](https://amplpy.ampl.com/en/latest/classes/ampl.html#amplpy.AMPL.get_parameter). Here's an example for the cost parameter:
    ```python
    import pandas as pd  # For handling data as DataFrames
    import numpy as np   # For matrix operations  
    
    # Create a DataFrame for food items
    food_df = pd.DataFrame([           
    ("BEEF", 3.59, 2, 10),
    ("CHK",  2.59, 2, 10),
    ("FISH", 2.29, 2, 10),
    ("HAM",  2.89, 2, 10),
    ("MCH",  1.89, 2, 10),
    ("MTL",  1.99, 2, 10),
    ("SPG",  1.99, 2, 10),
    ("TUR",  2.49, 2, 10), ],
    columns=["FOOD", "cost", "f_min", "f_max"],).set_index("FOOD")

    # DataFrame for nutrients
    nutr_df = pd.DataFrame([ 
    ("A",   700,    20000),
    ("C",   700,    20000),
    ("B1",  700,    20000),
    ("B2",  700,    20000),
    ("NA",  0,      50000),
    ("CAL", 16000,  24000),],
    columns=["NUTR", "n_min", "n_max"],).set_index("NUTR")
    
    # Nutrient content matrix
    amt_df = pd.DataFrame(
    np.array([                          # np.array: The matrix is defined using NumPy's array function, which takes a nested list as input
    [60, 8, 8, 40, 15, 70, 25, 60],     # Nutrient 1 values for each food
    [20, 0, 10, 40, 35, 30, 50, 20],    # Nutrient 2 values for each food
    [10, 20, 15, 35, 15, 15, 25, 15],   # ...
    [15, 20, 10, 10, 15, 15, 15, 10],
    [928, 2180, 945, 278, 1182, 896, 1329, 1397],
    [295, 770, 440, 430, 315, 400, 379, 450],]),# Nutrient 6 values for each food
    columns=food_df.index.to_list(),    # The columns are labeled using the indices from food_df.
    index=nutr_df.index.to_list(),)     # The rows (index) are labeled using the indices from nutr_df
    
    # Set data in AMPL
    ampl.set_data(food_df, "FOOD")      # Definition of the "FOOD" set and parameters cost, f_min, f_max  
    ampl.set_data(nutr_df, "NUTR")      # Definition of the "NUTR" set and parameters "n_min", "n_max"
    
    # Define LINKS set
    ampl.set['LINKS'] = [(nutrient, food)# Assigns a list of (nutrient, food) pairs to the LINKS
        for nutrient in amt_df.index  # Loops over the rows of amt_df. amt_df.index provides the row labels, which correspond to nutrients
        for food in amt_df.columns    #  Loops over the columns of amt_df. amt_df.columns provides the column labels, corresponding to food items.
        if amt_df.loc[nutrient, food] != 0] # Filters out combinations where the nutrient content for a specific food is 0
    
    # Filter and assign amt values
    filtered_amt = {                                # Creates a dictionary to hold valid (nutrient, food) pairs with their corresponding values from amt_df
    (nutrient, food): amt_df.loc[nutrient, food]    # Fetches the value from amt_df for the (nutrient, food) pair
    for nutrient, food in ampl.set['LINKS'] }       # Loops over each (nutrient, food) pair in the 'LINKS' set
    
    ampl.get_parameter("amt").set_values(filtered_amt) # Set the values for the parameter "amt" using "amt_df"

- #### 3.1.4. Use Matrices with numpy:
    You can use `numpy matrices` or `numpy arrays` to load values into AMPL. Example:
    ```python
    import numpy as np
    import pandas as pd
    amt_df = pd.DataFrame(
            np.array(
                [
                    [60, 8, 8, 40, 15, 70, 25, 60],
                    [20, 0, 10, 40, 35, 30, 50, 20],
                    [10, 20, 15, 35, 15, 15, 25, 15],
                    [15, 20, 10, 10, 15, 15, 15, 10],
                    [928, 2180, 945, 278, 1182, 896, 1329, 1397],
                    [295, 770, 440, 430, 315, 400, 379, 450],
                ]
            ),
            columns=food_df.index.to_list(),
            index=nutr_df.index.to_list(),
        )
    ampl.param['amt'] = amt_df
    
- #### 3.1.5 Use Polars DataFrames
   **Polars** is a **high-performance DataFrame library** for data manipulation and analysis in **Python** (similar to **Pandas**) but optimized for speed and efficiency. It is designed for handling **large datasets efficiently**, both in terms of computation time and memory usage. Polars is excellent for efficient data manipulation, but since AMPL expects Pandas DataFrames, conversion is necessary before setting data in AMPL. That's a smart workflow—leveraging Polars' speed and then converting to Pandas only when interfacing with AMPL.
   ```python   
   import polars as pl

   # Food DataFrame with cost and limits
   food_df = pl.DataFrame({
      "FOOD": ["BEEF", "CHK", "FISH", "HAM", "MCH", "MTL", "SPG", "TUR"],
      "cost": [3.59, 2.59, 2.29, 2.89, 1.89, 1.99, 1.99, 2.49],
      "f_min": [2] * 8,               # Minimum quantity for each food
      "f_max": [10] * 8               # Maximum quantity for each food
   }).to_pandas().set_index("FOOD")    # Convert to Pandas for AMPL compatibility

   # Nutrient DataFrame with limits
   nutr_df = pl.DataFrame({
      "NUTR": ["A", "C", "B1", "B2", "NA", "CAL"],
      "n_min": [700, 700, 700, 700, 0, 16000],            # Minimum nutrient requirement
      "n_max": [20000, 20000, 20000, 20000, 50000, 24000] # Maximum limit
   }).to_pandas().set_index("NUTR")

   # Nutrient content matrix for each food
   amt_df = pl.DataFrame({
      "FOOD": ["BEEF", "CHK", "FISH", "HAM", "MCH", "MTL", "SPG", "TUR"],
      "A": [60, 8, 8, 40, 15, 70, 25, 60],
      "C": [20, 0, 10, 40, 35, 30, 50, 20],
      "B1": [10, 20, 15, 35, 15, 15, 25, 15],
      "B2": [15, 20, 10, 10, 15, 15, 15, 10],
      "NA": [928, 2180, 945, 278, 1182, 896, 1329, 1397],
      "CAL": [295, 770, 440, 430, 315, 400, 379, 450] })

   # Set food and nutrient data in AMPL
   ampl.set_data(food_df, "FOOD")
   ampl.set_data(nutr_df, "NUTR")
   ```

- ### **3.2. Import Data from the External Resources**

It is possible to retrieve data from external files and load them into your AMPL model. Since it is easy to read files using Pandas in Python, and Amplpy can read Pandas directly, we can finally get a flawless connection between AMPL and the most relevant sources of data. 
    
- #### 3.2.1 JSON File
    This approach offers a flexible and efficient method for dynamically loading and indexing tabular data stored in JSON files. It ensures smooth integration by using Pandas DataFrame operations and dynamic variable assignment to handle various datasets.
    This code provides a robust solution for dynamically loading and indexing tabular data from JSON files. By leveraging DataFrame operations and dynamic variable assignment, it offers a flexible approach to handling diverse datasets efficiently.
    ```python
    import pandas as pd
    import json

    # Example JSON data stored in a file
    # data.json:
    # {
    #   "products": [
    #     {"id": 1, "prod": "Unit A", "price": 0.5},
    #     {"id": 2, "prod": "Unit B", "price": 0.3}
    #   ],
    #   "customers": [
    #     {"name": "Alice", "orders": 5},
    #     {"name": "Bob", "orders": 3}
    #   ]
    # }

    # Load the JSON file
    with open("data.json", "r") as file:
        data = json.load(file)

    # Create DataFrames from the JSON data
    products_df = pd.DataFrame(data["products"])  # DataFrame for products
    customers_df = pd.DataFrame(data["customers"])  # DataFrame for customers

    # Set indices
    products_df.set_index("id", inplace=True)  # Use 'id' as the index for products
    customers_df.set_index("name", inplace=True)  # Use 'name' as the index for customers

    ampl.set_data(products_df, "PROD") # Initialize the indexing set "PROD" and send values for parameters indexed by "PROD".
    ampl.set_data(customers_df, "CUSTOMERS") # Initialize the indexing set "CUSTOMERS" and send values for parameters indexed by "CUSTOMERS".
    ```

    This code dynamically loads JSON data and assigns each dataset to a DataFrame, setting appropriate indices and popularing sets PROD and CUSTOMERS in the model, in addition to parameters indexed by PROD and CUSTOMERS.

- #### 3.2.2 CSV Files
    CSV files are a common format for storing data. This code demonstrates how to dynamically read multiple CSV files into Pandas DataFrames, using variable assignment to manage the data efficiently.
    ```python
    # List of DataFrame names (you can modify this if you have more DataFrames)
    df_names = ['food_df', 'nutr_df', 'amt_df']
    # List of indexing sets in AMPL
    ampl_names = ['FOOD', 'NUTR', 'AMT']

    # Generate the corresponding CSV filenames programmatically by appending '.csv'
    csv_files = [f"{name}.csv" for name in df_names]   

    for df_name, ampl_name, csv_file in zip(df_names, ampl_names, csv_files): # Loop through the names and files and read CSV files into DataFrames
        df = pd.read_csv(csv_file)   # Read the CSV into a DataFrame
        ampl.set_data(df, ampl_name) # Send dataframe df to AMPL
    ```
    This snippet demonstrates how to load data from multiple CSV files into Pandas DataFrames and assign them to variable names dynamically, which can then be used for further analysis or optimization tasks ([`pandas.read_csv()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) documentation).
- #### 3.2.3 Excel Files
    When working with Excel files that contain multiple sheets, this code reads all sheets into separate DataFrame variables. This is useful for cases where data is organized into multiple sheets within a single file.
    ```python
    excel_file = "data.xlsx"                            # Define the Excel file path
    dfs = pd.read_excel(excel_file, sheet_name=None)    # Read all sheets into a dictionary of DataFrames

    for sheet_name, df in dfs.items():                  # Dynamically create DataFrame variables from sheet names
        var_name = sheet_name.lower().replace(" ", "_") # Create a valid variable name by converting the sheet names
        ampl.set_values(df, var_name)                   # Load the sheet data into AMPL using the appropriate var_name as one of the indexing sets in the model
    ```
    By reading all sheets from an Excel file and assigning each sheet to a corresponding DataFrame, this approach facilitates the automatic handling of multi-sheet Excel files without the need to manually specify each sheet ([Pandas `read_excel`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) documentation).
- #### 3.2.4 Google Sheets
    Google Sheets can be an efficient way to store and collaborate on data. This Python script enables automatic importing of data from Google Sheets directly into Pandas DataFrames. The script constructs the necessary URLs dynamically based on the sheet names and imports the data.
    ```python
    import pandas as pd

    # Base URL template for reading Google Sheets as CSV
    base_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}"

    spreadsheet_id = "your_spreadsheet_id_here"  # Replace with the actual spreadsheet ID

    sheets = {  # Mapping of sheet names to DataFrame variable names 
        "Food Data": "food_df",
        "Nutrient Data": "nutr_df",
        "Nutrient Content Matrix": "amt_df" }

    for sheet_name, df_name in sheets.items():
        url = base_url.format(spreadsheet_id, sheet_name)
        try:
            # Load the sheet into a Pandas DataFrame
            df = pd.read_csv(url)
            # Load the Pandas DataFrame into AMPL
            ampl.set_data(df, df_name)
        except Exception as e:
            print(f"Failed to load sheet '{sheet_name}': {e}")
    ```
    This code automates the process of importing data from Google Sheets, making it easier to work with datasets stored in the cloud, especially in collaborative environments ([Google Sheets API documentation](https://developers.google.com/sheets/api/guides/values)).
- #### 3.2.5 PostgreSQL
    PostgreSQL is a powerful relational database management system. This example demonstrates how to use SQLAlchemy to read data from PostgreSQL tables directly into Pandas DataFrames. The `psycopg2-binary` library is used to facilitate the connection.
    ```python
    %pip install psycopg2-binary sqlalchemy
    import pandas as pd
    from sqlalchemy import create_engine

    # Define PostgreSQL connection parameters
    db_url = "postgresql://username:password@host:port/database_name"
    engine = create_engine(db_url)  # Create the engine
    table_names = ["food_df", "nutr_df", "amt_df"]  # Table names in PostgreSQL

    # Read data from PostgreSQL into DataFrames dynamically
    with engine.connect() as conn:
        dfs = {table: pd.read_sql(f"SELECT * FROM {table}", conn) for table in table_names}

    # Assign to variables explicitly
    food_df, nutr_df, amt_df = dfs.values()
    # Load them into AMPL
    ampl.set_data(food_df, "FOOD")
    ampl.set_data(nutr_df, "NUTR")
    ampl.param['amt'] = amt_df
    ```
    Using SQLAlchemy, this script reads tables from a PostgreSQL database into Pandas DataFrames. This is particularly useful when the data is stored in a relational database and needs to be integrated into analysis workflows ([SQLAlchemy documentation](https://www.sqlalchemy.org/), [psycopg2-binary documentation](https://pypi.org/project/psycopg2-binary/)).
- #### 3.2.6 MS PowerBI
    Power BI is a widely used business analytics tool. Through its API, developers can interact with Power BI reports, datasets, and tables programmatically. This section highlights resources and tools available to integrate Power BI data with Python workflows.

    For more details on how to interact with Power BI data using Python, check the [PowerBI REST API Python Library](https://github.com/AntoineDW/powerbi-rest-api-python), [Power BI Jupyter Notebook Integration](https://github.com/microsoft/powerbi-jupyter), or this example on [Oil refinary production optimization](https://colab.ampl.com/notebooks/oil-refinery-production-optimization-powerbi.html).

- #### 3.2.7 Note on large datasets
    For very large datasets (e.g., over 10 million rows), consider table handlers (e.g., [amplcsv](https://plugins.ampl.com/amplcsv.html?_gl=1*az5jj*_ga*NzYxMTM1OTIyLjE3MzczODAyNjg.*_ga_FY84K2YRRE*MTczNzc3MjQ3MC41LjEuMTczNzc3MjQ4MC4wLjAuMA..), [amplxl](https://plugins.ampl.com/amplxl.html?_gl=1*vmneu2*_ga*NzYxMTM1OTIyLjE3MzczODAyNjg.*_ga_FY84K2YRRE*MTczNzc3MjQ3MC41LjEuMTczNzc3MjQ4MC4wLjAuMA..), [eodbc](https://plugins.ampl.com/ampltabl.html?_gl=1*1fhbiwe*_ga*NzYxMTM1OTIyLjE3MzczODAyNjg.*_ga_FY84K2YRRE*MTczNzc3MjQ3MC41LjEuMTczNzc3MjQ4MC4wLjAuMA..)) to load data directly into AMPL for better performance. You can still use `amplpy` to update data and retrieve solutions.

- ### **3.3 Use a Data File**
    - You can still read a `data.dat` file from your working directory. This file will contain essential data like the values for sets and parameters in your model. You can read a data file through the `read_data(filename)` function in Amplpy. Example:
    ```python
    ampl.read_data('data.dat')
    ```
    For better maintainance of your application, consider first Section 3.2 rather than using AMPL ".dat" files directly.
    
## Section 4: Modify model data
In an optimization model, input data is typically stored in **parameters**, which can be either scalar (single values) or vectorial (arrays, lists of values, matrices). Modifying the values of vectorial parameters is a common task in optimization modeling. There are two primary ways to modify the values of vectorial parameters:
**1. Change Specific Values**: Modify the values for particular indices or entries of the parameter.
**2. Change All Values**: Update all entries in the parameter at once, either by providing a complete list or array of values.

Below are two examples demonstrating how to modify the values of the cost parameter using both methods. After making the changes, the model is solved, and the new objective value is retrieved.
- #### Example 1: Modify All Values
    If you need to update **all** values in a vectorial parameter at once, you can pass a list of new values to the `set_values()` method. The order of the values in the list should correspond to the order of indices in the parameter as defined in AMPL.
    ```python
    cost.set_values([3, 5, 5, 6, 1, 2, 5.01, 4.55])     # Update all costs in order
    print("Updated all costs.")
    ampl.solve()                                        # Solve the model
    print("New objective value:", totalcost.value())    # Get the updated objective value

**Explanation:**
- The list `[3, 5, 5, 6, 1, 2, 5.01, 4.55]` assigns new values to all entries in the `cost` parameter.
- The values are assigned in the order the `cost` parameter's indices are defined in AMPL.

    This also applies to sets: 
    ```python
    ampl.set['TIME'] = list(range(10))        # Populate TIME set in AMPL with a list
    # Or alternatively
    time = ampl.get_set('TIME')
    time.set_values(range(10))
    ```

>The function `amplpy.Parameter.set_values() `is versatile and supports both specific updates (using a dictionary) and complete updates (using a list). When updating all values, ensure the order matches the indexing in AMPL to avoid unintended results. For a complete list of available methods and more detailed documentation, refer to the [amplpy.Parameter.set_values()](https://amplpy.ampl.com/en/latest/classes/parameter.html#amplpy.Parameter.set_values) documentation.

- #### Example 2: Modify Specific Values
    In this approach, you modify the values of specific entries in the parameter, leaving other values unchanged. One option is to access the parameter directly through the model.param:
    ```python
    ampl.param['cost'] = {"BEEF": 5.01, "HAM": 4.55}        # Modify costs for BEEF and HAM
    print("Increased costs of beef and ham.")
    ampl.solve()                                        # Solve the model
    print("New objective value:", ampl.obj['Total_Cost'].value())    # Get the updated objective value
    ```
    Another clean alternative is to use `set_values()` method from the [`amplpy.Parameter`](https://amplpy.ampl.com/en/latest/classes/parameter.html#amplpy.Parameter.set_values) class. You provide a dictionary where the keys are the indices (e.g., the names or identifiers of items), and the values are the new values you want to assign.
    ```python
    cost = ampl.get_parameter("cost")                   
    cost.set_values({"BEEF": 5.01, "HAM": 4.55})        # Modify costs for BEEF and HAM
    print("Increased costs of beef and ham.")
    ampl.solve()                                        # Solve the model
    print("New objective value:", ampl.obj['Total_Cost'].value())    # Get the updated objective value
    ```
    **Explanation:** The code assigns 5.01 to `BEEF` and 4.55 to `HAM`. Other values in the `cost` parameter remain unchanged.    
---

## Section 5. Set Options
- ### 5.1. AMPL Options
    AMPL provides a comprehensive set of options that allow users to customize the behavior of their models in various ways. These options can be divided into several categories, each focusing on a different aspect of model setup, solution process, and solver options. Here's how to access and change these options through Amplpy within Python. First option is to directly assign the value of an option through an option name. 
    **Example Python code to configure solver-related options:**
    ```python
    ampl.option['solver'] = 'highs'  # Configure mp-solvers options (output level and time limit)
    ampl.option['mp_options'] = 'outlev=0 lim:time=20'  # Configure mp-solvers options (output level and time limit)
    ```
    To increase the number of presolve iterations in AMPL or to turn if off, use the "presolve" option (by default 10):
    ```python
    ampl.option['presolve'] = 90 # Set 90 Presolve iterations
    ```
    As an alternative syntax, it is possible to use the `set_option(option_name, value)` method:
    ```python
    ampl.set_option('solver', 'highs')  # Set 90 Presolve iterations
    ampl.set_option('presolve', 90)  # Set 90 Presolve iterations
    ampl.set_option('mp_options', 'outlev=0 lim:time=20')  # Configure mp-solvers options (output level and time limit)
    ```
    To get the value of an option, use the `get_option(option_name)` method or directly access `ampl.option[option_name]`.

    These options allow for a high degree of flexibility, ensuring that AMPL can be tailored to meet the specific needs of various optimization tasks. Users can control aspects such as statistical displays, solver behavior, time limits, and how zero values are handled in output, making AMPL a powerful and adaptable tool for optimization modeling.

    To explore all available options in detail and learn more about their specific applications, you can consult the [full list of AMPL options](https://dev.ampl.com/ampl/options.html).
    
- ### 5.2. Solver Options
    Solver options provide users with control over the configuration of the solvers that AMPL uses to find solutions. These options allow you to fine-tune solver behavior, such as adjusting the level of verbosity in solver messages, setting time limits for solver execution, and defining solver-specific parameters that influence the performance and accuracy of the solution.

    By modifying solver options, you can strike a balance between performance (such as speed) and accuracy (such as precision of the solution). These options are crucial for optimizing the solution process and ensuring that the solver operates efficiently within the time constraints specified by the user.

    For a comprehensive guide on the solver options available in AMPL, including their specific usage and settings, refer to the [solver guide](https://dev.ampl.com/solvers/index.html).

    As a special case, solver options can be modified in a [`solve(solver='', verbose=True, **kwargs)`](https://amplpy.ampl.com/en/latest/classes/ampl.html#amplpy.AMPL.solve) call. **Example updating solver options in Amplpy**.
    ```python
    # Solve the problem with Highs, with outlev=0 and time limit of 30 seconds
    ampl.solve(solver='highs', mp_options='outlev=0 lim:time=30')
    # Solve the problem with Gurobi, with mipfocus=1 and time limit of 180 seconds
    ampl.solve(solver='gurobi', mp_options='mipfocus=1 lim:time=180')
    ```
    Notice that `mp_options` are options common to AMPL solvers built by the MP framework, but `gurobi_options` and `highs_options` would be accepted too.
---

## Section 6. Solve the Optimization Problem
To solve the current optimization problem instance using AMPL in Python, follow the commands below. These examples illustrate different ways to set and execute a solver.
   
**1a. Set Solver and Solve**
   ```python
   ampl.solve(solver='highs')  # Solve the optimization problem using highs solver
   ```
- Uses `ampl.solve() `with the solver explicitly passed as an argument.

**1b. Specify and Solve with a Solver Option**
   ```python
   # Specify the Solver and Solve
   ampl.option["solver"] = "highs"           # Specify the solver to use (e.g., HiGHS)
   ampl.solve(verbose=False)                 # Solve the problem
   ```
- Sets the solver globally for the current AMPL model instance.
- Executes the optimization using the specified solver
- `verbose=False` suppresses detailed solver output.

**2. Verify if the Model is Solved**
   ```python
   assert ampl.solve_result == "solved"      # Stop if the model was not solved
   ```
- Checks whether the model was solved successfully by comparing ampl.solve_result to "solved".
- If the assertion fails, it raises an error indicating the model was not solved. See the full list of codes for Amplpy here:

| Number  | String     | Interpretation                                          |
| ------- | ---------- | ------------------------------------------------------- |
| 0-99    | solved     | Optimal solution found                                  |
| 100-199 | solved?    | Optimal solution indicated, but error likely            |
| 200-299 | infeasible | Constraints cannot be satisfied                         |
| 300-399 | unbounded  | Objective can be improved without limit                 |
| 400-499 | limit      | Stopped by a limit that you set (such as on iterations) |
| 500-599 | failure    | Stopped by an error condition in the solver routines    |

**2.1. Debugging an infeasible model**
Some solvers like Gurobi can return the Irreducible Infeasible Subsystem (IIS):
```python
ampl.solve(solver="gurobi", gurobi_options="outlev=1 iis=1")
if ampl.solve_result == "infeasible":
    print("Infeasible problem!")
    var_iis, con_iis = ampl.get_iis()
    print(var_iis, con_iis)
```

**Important Notes:**
- **Error Handling**: Use assertions or conditional checks to handle unsolved models gracefully.
- **Performance**: For large models, consider setting solver-specific options for enhanced performance, as a reference, see specific solver features in this [MP Solvers advanced features](https://mp.ampl.com/features-guide.html).

---

## Section 7. Retrieve Results and Export Data
- ### 7.1. Retrieve Results
    The `ampl.get_solution(flat=False, zeros=False)` should be used in order to get the solution. The `zeros` option controls whether variables with zero value are retrieved or not. The result is a nested dictionary where variable names are indexes to access the dictionary with the values for each variable family (each key is an index for the variable, and the value the optimal value after solve).
  
- ### 7.2 Save as Python Dictionary
    Simply use the method `get_solution`.
    ```python
    solution = ampl.get_solution(flat=False, zeros=False)
    ```
- ### 7.3 Save as Pandas DataFrame
    Use `get_solution` to get a Python Dict and later generate Pandas DataFrame from dict.
    ```python
    import pandas as pd
    solution_df = pd.DataFrame.from_dict(ampl.get_solution(flat=False))
    print(solution_df)
    ```
    Consider using filters in the DataFrame such as get the elements greater than a certain threshold (1e-9), or rounding for integer decision variables in the DataFrame.
- ### 7.4 Save as Polars DataFrame
    TThis section provides an optimized approach for Polars integration.
    ```python
    import polars as pl
    solution_df = pl.from_dict(ampl.get_solution(flat=False))
    print(solution_df)
    ```
- ### 7.5 Save to JSON File
    Save as Python Dict and send to a json file.
    ```python
    import json
    solution_dict = ampl.get_solution(flat=False, zeros=False)
    with open("data.json", "w") as file:
        json.dump(solution_dict, file, indent=4)
- ### 7.6 Save to CSV Files
    This stores each variable's DataFrame as a separate CSV file.
    ```python
    import pandas as pd
    # Get the solution as a Pandas DataFrame
    solution_df = pd.DataFrame.from_dict(ampl.get_solution(flat=False))
    # Output file
    output_path = "ampl_results/results.csv"
    solution_df.to_csv(output_path, index=False)
- ### 7.7 Save to Excel File
    Saves each variable to a separate Excel sheet. 
    ```python
    import pandas as pd
    # Get the solution as a Pandas DataFrame
    solution_df = pd.DataFrame.from_dict(ampl.get_solution(flat=False))

    # Initialize an Excel writer
    with pd.ExcelWriter("ampl_results.xlsx") as writer:
        # Save each DataFrame to a separate sheet
        solution_df.to_excel(writer, sheet_name=key_ampl, index=False)          
- ### 7.8 Save to Google Sheets
    This section writes the combined DataFrame to a Google Sheet.
    
    **1. Set Up Google Sheets API:**
    - Go to the Google Cloud Console.
    - Create a new project (or use an existing one).
    - Enable the **Google Sheets API** and **Google Drive API**.
    - Create credentials for a service account, and download the JSON key file.
    - Share your Google Sheet with the service account's email.
    
    **2. Save Output to Google Sheets:**
    ```python
    pip install gspread gspread-dataframe oauth2client
    import gspread
    from gspread_dataframe import set_with_dataframe
    import pandas as pd
    # Get the solution as a Pandas DataFrame
    solution_df = pd.DataFrame.from_dict(ampl.get_solution(flat=False))

    # Authenticate using the service account key file
    gc = gspread.service_account(filename='path_to_your_service_account.json')
    sh = gc.open("YourGoogleSheetName")                 # Open Google Sheet by name or URL
    worksheet = sh.sheet1                               # Select the first worksheet
    set_with_dataframe(worksheet, solution_df)             # Write DataFrame to Google Sheets
- ### 7.9 Save to PostgreSQL
    This section saves variable data to a PostgreSQL table.
    ```python
    pip install psycopg2 sqlalchemy
    from sqlalchemy import create_engine

    # Replace the placeholders with your actual database details
    db_url = "postgresql://username:password@host:port/dbname"
    engine = create_engine(db_url)
    from sqlalchemy import create_engine

    # PostgreSQL connection details
    db_url = "postgresql://username:password@host:port/dbname"
    engine = create_engine(db_url)
    import pandas as pd
    solution_df = pd.DataFrame.from_dict(ampl.get_solution(flat=False))
    for variable, index_value in ampl.get_solution(flat=False, zeros=True).items():
        # Save to PostgreSQL
        table_name = f"ampl_results_{variable}"         # Optional: customize table naming
        var_df = pd.DataFrame.from_dict(index_value)
        var_df.to_sql(
            table_name,
            engine,
            if_exists="replace",                        # Options: 'fail', 'replace', 'append'
            index=False)
---

## Section 8. Get arbitrary values via ampl expressions
When working with optimization models, there are often cases where we require specific outputs beyond the complete set of results. Instead of cluttering the AMPL environment with additional entities (like variables or constraints), AMPL provides a clean and efficient way to directly fetch values using arbitrary expressions. This keeps the workspace organized while leveraging AMPL's powerful expression capabilities.

### 8.1. Accessing the values of a decision variable
* We can access the value of a variable and save it into a DataFrame easily with `ampl.var['Buy'].to_pandas()` or to a dictionary with `ampl.var['Buy'].to_dict()`, in this case, to access the values of variable `Buy`:
    ```python
    buy_df = ampl.var['Buy'].to_pandas()
    buy_dict = ampl.var['Buy'].to_dict()
    ```
    or using the `get_data` method.
    ```python
    buy_df = ampl.get_data('Buy').to_pandas()
    buy_dict = ampl.get_data('Buy').to_dict()
    ```
### 8.2. Example: Evaluating Decision Variables Against Their Upper Bounds
In this example, we aim to determine how close each decision variable (`Buy[j]`) is to its upper bound (`Buy[j].ub`) as a percentage. This insight helps identify variables that are tightly constrained by their upper limits, which can inform further optimization or model adjustments. We can achieve this by using the function [`amplpy.AMPL.get_data()`](https://amplpy.ampl.com/en/latest/classes/ampl.html#amplpy.AMPL.get_data). This function retrieves data based on a given AMPL expression and converts it into a Python-friendly format, such as a pandas DataFrame.
- Here’s the Code Example:
    ```python
    # Get the values of an expression into a pandas.DataFrame object
    df = ampl.get_data("{j in FOOD} 100*Buy[j]/Buy[j].ub").to_pandas()
    print(df)
    ```
#### **Code Breakdown**
**1. Expression**: `{j in FOOD} 100 * Buy[j] / Buy[j].ub`:
- Iterates efficiently over all items in the set FOOD.
- For each item j, calculates the percentage of Buy[j] relative to its upper bound (Buy[j].ub).
- Multiplies by 100 to express the result as a percentage.

**2. `ampl.get_data()` Function**:
- Fetches computed values from the model based on the given AMPL expression.
- Provides a clean interface to extract specific model information without needing additional AMPL variables or constraints.

**3. `.to_pandas()` Method:**
- Converts the data returned by ampl.get_data() into a pandas DataFrame, making it easy to analyze and visualize results in Python.

The `get_data()` method is the best way to retrieve difficult expressions from AMPL, by using AMPL syntax, and returning the result values as a pandas DataFrame.

## Section 9. Sensitivity Analysis
   This section performs a **sensitivity analysis** on parameters in an AMPL optimization model to assess how changes in parameter values affect both the **objective function** and **decision variables**. This function analyzes the sensitivity of parameters based on the provided list of percentage changes (deltas). Results are stored in a nested dictionary structure.
```python
# Function to perform sensitivity analysis for parameters
def sensitivity_analysis_parameter(ampl, param_name, deltas):
    results_dict = {}
    original_value = ampl.param[param_name].value()
    for delta in deltas:
        ampl.param[param_name] = original_value*(1 + delta)
        ampl.solve()
        results_dict[delta] = ampl.obj['Profit'].value()
    return results_dict

# Define deltas
deltas = [-0.3, -0.25, -0.2, -0.15, -0.1, -0.05, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3]  # Percentage changes
# Analyze profit for different budgets by updating the parameter ampl.param['budget'] for every delta
results_dict = sensitivity_analysis_parameters(ampl, "budget", deltas)
```
