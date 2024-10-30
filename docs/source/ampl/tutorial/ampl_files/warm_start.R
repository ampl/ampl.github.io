# Load necessary libraries
library(rAMPL)
# Custom function definitions
source("set_n_solve.R")
source("print_solution.R")

# Initialize AMPL object
ampl <- new(AMPL)

# Load model
ampl$read("mulled_wine.mod")

# Relax integrality and solve the problem as an LP
ampl$setOption("relax_integrality", 1)
cat("LP solve:")
set_n_solve(ampl, "highs")

# Print solution
cat("LP solution:\n")
print_solution(ampl)

# Warm start by assigning rounded values to non-integers
# getVariables() returns a list of Rcpp_Variable references
# Each Rcpp_Variable reference can be queried for its values via getValues() method
# Variable values are returned as a data.frame
# data.frame objects of indexed variables contain an index and a values column
# data.frame objects of saclar variables simply contain a value column
# Value column (i.e. value_df[[idx]]) is a numeric vector that can be updated via mapply() 
vars <- ampl$getVariables()
for (var in vars) {
    idx = 2
    if(var$isScalar()) {
        idx = 1
    } 
    value_df <- var$getValues()
    value_df[[idx]] <- mapply(function(val) if(val != round(val)) round(val) else val, value_df[[idx]])
    var$setValues(value_df)
}

# Display updated values
cat("\nWARM START values:\n")
ampl$eval("display _varname, _var;")

# Enforce integrality and solve the problem as an IP
ampl$setOption("relax_integrality", 0)
cat("\nIP solve:")
set_n_solve(ampl, "cbc")

# Print solution
cat("IP solution:\n")
print_solution(ampl)
