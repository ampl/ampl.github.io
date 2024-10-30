# Import necessary modules
from amplpy import AMPL
# Custom modules
from set_n_solve import set_n_solve
from print_solution import print_solution

# Initialize AMPL object
ampl = AMPL()

# Load the model 
ampl.read("production.mod")

# Data files for each instance of a proudction model
data_files = ["lemonade.dat", "mulled_wine.dat"]
# Solver names
solver_names = ["cbc", "highs"]

for file, name in zip(data_files, solver_names):
    # Load data file
    ampl.read_data(file)
    # Set solver option and solve the problem using the selected solver
    set_n_solve(ampl, name)
    # Print solution using our generic print_solution function
    print_solution(ampl)
    # Reset data for next iteration
    ampl.eval("reset data;")
