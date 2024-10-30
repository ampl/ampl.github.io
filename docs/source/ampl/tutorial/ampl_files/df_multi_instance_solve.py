# Import necessary modules
from amplpy import AMPL
# Custom modules
from set_n_solve import set_n_solve
from print_solution import print_solution
from set_data import set_data

# Initialize AMPL object
ampl = AMPL()

# Load the model 
ampl.read("production.mod")

# Data names for each instance of a proudction model
data_names = ["lemonade", "mulled_wine"]
# Solver names
solver_names = ["cbc", "highs"]

for data, solver in zip(data_names, solver_names):
    # Set data using the 'set_data()' method without the need for a `.dat` file
    set_data(ampl, data)
    # Set solver option and solve the problem using the selected solver  
    set_n_solve(ampl, solver)
    # Print solution using our generic print_solution function
    print_solution(ampl)
    # Reset data for next iteration
    ampl.eval("reset data;")
