# Load necessary libraries
from amplpy import AMPL

# Initialize AMPL object
ampl = AMPL()

# Evaluate AMPL statements
ampl.eval("""
    param begin = 1;
    param end = 6;
    param ones{begin..end} := 1;
    """)

# Get data for parameter ones
# get_data() returns both the indexing set and values of parameter ones
# Column 'index0' contains the values of the indexing set
# Column 'ones' contains the values of the ones array
ones = ampl.get_data("ones")

# For each element of ones print value
for v in ones.get_column("ones"):
    print(int(v))
