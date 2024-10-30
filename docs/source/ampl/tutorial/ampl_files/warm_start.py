# Import necessary modules
from amplpy import AMPL, DataFrame
# Custom modules
from set_n_solve import set_n_solve
from print_solution import print_solution

# Initialize AMPL object
ampl = AMPL()

# Load model
ampl.read('mulled_wine.mod')

# Relax integrality and solve the problem as an LP
ampl.set_option("relax_integrality", 1)
print("LP solve:", end="")
set_n_solve(ampl, "highs")

# Print solution
print("LP solution:")
print_solution(ampl)

# Warm start by assigning rounded values to non-integers
# get_variables() returns an EntityMap
# Each element in the EntityMap is a tuple
# The first element of the tupel is a string (the name) 
# The second elment is a variable object 
# i.e. ('name', Variable object)
# A variable object could hold multiple values if the variable is indexed
vars = ampl.get_variables()
for var in vars:
    for v in var[1]:
        val = v[1].value()
        if val != round(val):
            v[1].set_value(round(val))

# Display updated values
print("\nWARM START values:")
ampl.eval("display _varname, _var;")

# Enforce integrality and solve the problem as an IP
ampl.set_option("relax_integrality", 0)
print("\nIP solve:", end="")
set_n_solve(ampl, "cbc")

# Print solution
print("IP solution:")
print_solution(ampl)
