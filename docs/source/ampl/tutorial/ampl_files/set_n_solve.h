// Include necessary headers
#include <iostream>
#include "ampl/ampl.h"

void set_n_solve(ampl::AMPL &ampl, const std::string &solver_name) 
{
    std::cout << std::endl; // Add space for output formatting
    // Set option solver to solver_name
    ampl.setOption("solver", solver_name);
    // Solve
    ampl.solve();
    std::cout << std::endl; // Add space for output formatting
}
