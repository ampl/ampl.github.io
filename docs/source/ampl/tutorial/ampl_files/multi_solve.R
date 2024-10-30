# Load necessary libraries
library(rAMPL)
# Custom function definitions
source("set_n_solve.R")
source("print_solution.R")

# Initialize AMPL object
ampl <- new(AMPL)

model_files <- c("lemonade.mod", "mulled_wine_int.mod")
solver_names <- c("cbc", "highs")

for (file in model_files) {
    # Load the model
    ampl$read(file)  
    for (name in solver_names) {
        # Set solver option and solve the problem using the selected solver
        set_n_solve(ampl, name)
        # Print solution using our generic print_solution function
        print_solution(ampl)
    }
    # Reset ampl for next iteration
    ampl$reset()
}
