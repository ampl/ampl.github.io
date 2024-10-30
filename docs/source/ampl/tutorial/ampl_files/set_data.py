# Import necessary modules
from amplpy import DataFrame
import pandas as pd

def set_data(ampl, data_name):

    # Decide, which data to load
    # Then prepare lists that hold values to be loaded into AMPL
    if data_name == "lemonade":
        # Create Python lists for AMPL sets
        PROD = ['lemonade', 'iced_tea']
        INGR = ['lemon', 'tea_bag', 'sugar']
        # Create Python lists for AMPL params
        profit_per_product_data = [1.5, 1.0]
        limit_data = [10, 8, 20]
        usage_data = [1.0, 0.0,
                      0.0, 1.0,
                      2.0, 1.0]
    elif data_name == "mulled_wine":
        # Create Python lists for AMPL sets
        PROD = ["mulled_wine", "hot_tea"]
        INGR = ["spice", "tea_bag", "sugar", "wine"]
        # Create Python lists for AMPL params
        profit_per_product_data = [2.0, 1.5]
        limit_data = [12, 8, 30, 15]
        usage_data = [2.0, 0.0,
                      0.0, 1.0,
                      4.0, 2.0,
                      2.0, 0.0]
    else:
        raise ValueError("Invalid data_name. Data cannot be set.")


    # For simple data it is convenient to use AMPL object properties such as
    # 'set' (i.e. ampl.set), or 'param' (i.e. ampl.param) 
    # to assign data directly from lists.
    # However, for large amounts of data with custom indexing 
    # we recommend using the 'set_data()' method, 
    # which is illustrated below for loading parameter data.

    # Set scalar parameter fee (independent of data type (lemonade or mulled_wine))
    ampl.param["fee"] = 2.0

    # Assign members to AMPL's set PROD
    ampl.set["PROD"] = PROD

    # Assign members to AMPL's set INGR
    ampl.set["INGR"] = INGR


    # When using Pandas DataFrames to load AMPL data we need to keep the following in mind:
    # 1. The column names correspond to the AMPL entities' names (e.g. parameter names)
    # 2. The Pandas index values need to be equivalent to the values of the AMPL indexing set.
    # 3. We can load data into multiple AMPL entites simulatneously using 'set_data()', 
    #    as long as those entities are indexed over the same set.

    # Create Pandas DataFrame containing
    # param data: profit_per_product_data
    # indexing: PROD
    # and column (aka AMPL entity) name: profit_per_product
    profit_per_product = pd.DataFrame(  profit_per_product_data, 
                                        index=PROD, 
                                        columns=["profit_per_product"] )
    # Load data into AMPL
    ampl.set_data(profit_per_product)
    
    # Create Pandas DataFrame containing param data, indexing, and AMPL entity name
    # With a more compact Pandas DataFrame declaration, 
    # where the column name is inferred from the dictionary key.
    limit = pd.DataFrame( { 'limit': limit_data },
                            index=INGR )
    # Load data into AMPL
    ampl.set_data(limit) 

    # usage_data is a 1D represnentation of the constraint coefficient matrix.
    # This is needed because each Pandas DataFrame column
    # corresponds to an entity and thus values for 2D (or 3D, etc.) entities 
    # are also stored in one column.
    # Because 'param usage' is indexed over both INGR and PROD it is a 2D parameter.
    # Therefore we need to add tuples to the Pandas DataFrame index column.
    # These tuples can be created using:
    # pd.MultiIndex.from_tuples([(i,j) for i in INGR for j in PROD])
    # As usual the column name needs to correspond to the AMPL entity name 
    usage = pd.DataFrame( { 'usage': usage_data }, 
                            index=pd.MultiIndex.from_tuples([(i,j) for i in INGR for j in PROD]) )
    # Load data into AMPL
    ampl.set_data(usage)
