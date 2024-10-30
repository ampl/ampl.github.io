def set_n_solve(ampl, solver_name):
    print() # Add space for output formatting
    # Set option solver to solver_name
    ampl.set_option("solver", solver_name)
    # Solve
    ampl.solve()
    print() # Add space for output formatting
