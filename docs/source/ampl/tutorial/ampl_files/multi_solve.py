# Import necessary modules
from amplpy import AMPL
# Custom modules
from set_n_solve import set_n_solve
from print_solution import print_solution

# Initialize AMPL object
ampl = AMPL()

model_files = ["lemonade.mod", "mulled_wine.mod"]
solver_names = ["cbc", "highs"]

for file in model_files:
    # Load the model 
    ampl.read(file)
    for name in solver_names:
        # Set solver option and solve the problem using the selected solver
        set_n_solve(ampl, name)
        # Print solution using our generic print_solution function
        print_solution(ampl)
    # Reset ampl for next iteration
    ampl.reset()
