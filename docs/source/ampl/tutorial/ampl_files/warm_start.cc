// Include necessary headers
#include <ampl/ampl.h>
// Custom headers
#include "set_n_solve.h"
#include "print_solution.h"

int main() {
    // Initialize AMPL object
    ampl::AMPL ampl;

    // Load model
    ampl.read("mulled_wine.mod");
    
    // Relax integrality and solve the problem as an LP
    ampl.setIntOption("relax_integrality", 1);
    std::cout << "LP solve:";
    set_n_solve(ampl, "highs");
    
    // Print solution
    std::cout << "LP solution:" << std::endl;
    print_solution(ampl);

    // Warm start by assigning rounded values to non-integers
    // getVariables() returns an ampl::EntityMap<Variable>
    // Each element in the EntityMap is an ampl::Variable object
    // Each Variable can be queried for its values via getValues() method
    // Variable values are returned as an ampl::DataFrame
    // DataFrame objects of indexed variables contain an index and a values column
    // DataFrame objects of saclar variables simply contain a value column
    // The DataFrame iterator advances row-by-row
    // A Variable value (i.e. (*iter)[col].dbl()) is a double
    // Values in the DataFrame can be updated via setValue() method
    auto vars = ampl.getVariables();
    for (auto var : vars) { 
        auto value_df = var.getValues();
        std::size_t col{1};
        std::size_t row{0};
        if (var.isScalar()) 
            col = 0; 
        for (auto iter = value_df.begin(); iter != value_df.end(); ++iter, ++row) {
            double value = (*iter)[col].dbl();
            if (value != std::round(value))
                value_df.setValue(row, col, std::round(value));
        }
        var.setValues(value_df);
    }

    // Display updated values
    std::cout << "\nWARM START values:" << std::endl;
    ampl.eval("display _varname, _var;");

    // Enforce integrality and solve the problem as an IP
    ampl.setIntOption("relax_integrality", 0);
    std::cout << "\nIP solve:";
    set_n_solve(ampl, "cbc");

    // Print solution
    std::cout << "IP solution:" << std::endl;
    print_solution(ampl);

    return 0;
}
