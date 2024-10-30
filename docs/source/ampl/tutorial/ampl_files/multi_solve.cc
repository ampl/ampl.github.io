// Include necessary headers
#include <ampl/ampl.h>
// Custom headers
#include "set_n_solve.h"
#include "print_solution.h"

int main() {
    // Initialize AMPL object
    ampl::AMPL ampl;

    std::vector<std::string> model_files = {"lemonade.mod", "mulled_wine_int.mod"};
    std::vector<std::string> solver_names = {"cbc", "highs"};

    for (const auto& file : model_files) {
        // Load model
        ampl.read(file);
        for (const auto& name : solver_names) {
            // Set solver option and solve the problem using the selected solver
            set_n_solve(ampl, name);
            // Print solution using our generic print_solution function
            print_solution(ampl);
        }
        // Reset ampl for next iteration 
        ampl.reset();
    }

    return 0;
}
