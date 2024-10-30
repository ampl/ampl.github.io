# Load necessary libraries
library(rAMPL)

# Initialize AMPL object
ampl <- new(AMPL)

# Load the model
ampl$read("lemonade.mod")

# Set solver option
ampl$setOption("solver", "highs")

# Solve the model
ampl$solve()

# Retrieve the results
solution_df <- ampl$getData("lemonade, iced_tea, profit")

# Perform formatting before printing
solution_df <- as.data.frame(t(solution_df))  # Transpose 
names(solution_df) <- c("value")  # Provide column names

# Print solution
print(solution_df)
