# Load necessary libraries
library(rAMPL)

# Initialize AMPL object
ampl <- new(AMPL)

# Evaluate AMPL statements
ampl$eval(paste("param begin = 1;",
                "param end = 6;",
                "param ones{begin..end} := 1;"))

# Get data for parameter ones
# getData() returns both the indexing set and values of parameter ones
# Column 'index0' contains the values of the indexing set
# Column 'ones' contains the values of the ones array
ones <- ampl$getData("ones")

# For each element of ones print value
for (v in ones$ones) {
    cat(v, "\n")
}
