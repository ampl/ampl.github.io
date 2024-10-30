#include "MyDataFrame.h"
#include "transpose.h"
#include "ampl/ampl.h"

int main(int argc, char *argv[]) 
{
    // Initialize AMPL object
    ampl::AMPL ampl;

    // Load the model (file has to be in the working directory)
    ampl.read("lemonade.mod");

    // Set solver option
    ampl.setOption("solver", "highs");

    // Solve the problem
    ampl.solve();

    // Retrieve the results
    ampl::DataFrame solution_df = ampl.getData("lemonade, iced_tea, profit");

    // Convert data from ampl::DataFrame into a custom made MyDataFrame
    std::unique_ptr<MyDataFrame> my_df_ptr = transpose1D(solution_df);
    MyDataFrame& my_df = *my_df_ptr;

    // Use a special print function to print the solution stored in MyDataFrame
    printMyDataFrame(my_df);

    return 0;
}
