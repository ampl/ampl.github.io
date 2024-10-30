set_n_solve <- function(ampl, solver_name) {
    cat("\n") # Add space for output formatting
    # Set option solver to solver_name
    ampl$setOption("solver", solver_name)
    # Solve
    ampl$solve()
    cat("\n") # Add space for output formatting
}
