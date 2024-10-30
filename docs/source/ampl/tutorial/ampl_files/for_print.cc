// Include necessary headers
#include <iostream>
#include "ampl/ampl.h"

int main(int argc, char *argv[]) 
{
    // Initialize AMPL object
    ampl::AMPL ampl;

    // Evaluate AMPL statements
    ampl.eval(R"(param begin = 1;
             param end = 6;
             param ones{begin..end} := 1;)");

    // Get data for parameter ones
    // getData() returns both the indexing set and values of parameter ones
    // Column 'index0' contains the values of the indexing set
    // Column 'ones' contains the values of the ones array
    ampl::DataFrame ones = ampl.getData("ones");
    
    // For each element of ones print value
    for (const auto &v : ones.getColumn("ones"))
        std::cout << v.dbl() << std::endl;

    return 0;
}
