# Load necessary libraries
from amplpy import AMPL
import pandas as pd

# Initialize AMPL object
ampl = AMPL()

# Load the model 
ampl.read("lemonade.mod")

# Set solver option 
ampl.set_option("solver", "highs")

# Solve the problem
ampl.solve()

# Retrieve the results and convert to a Pandas dataframe
solution_df = ampl.get_data("lemonade, iced_tea, profit")
pandas_df = solution_df.to_pandas()

# Perform formatting before printing
pandas_df = pandas_df.T.reset_index() # Transpose and reset indexing
pandas_df.columns = ['item', 'value'] # Provide column names
pandas_df = pandas_df.set_index('item') # Use column 'item' as index

# Print solution
print(pandas_df)
