// Include necessary headers
#include <iostream>
#include <iomanip> // For std::setprecision
#include "ampl/ampl.h"

void print_solution(ampl::AMPL &ampl) 
{
    std::string solver = ampl.getOption("solver").value();
    std::cout << "Solution with: " << solver << std::endl;

    ampl::DataFrame vars = ampl.getData("_varname, _var");
    auto numRows = vars.getNumRows();
    auto varnames = vars.getColumn("_varname");
    auto varvals = vars.getColumn("_var");
    for (auto i = 0; i < numRows; ++i) 
        std::cout << varnames[i].str() << " = " << varvals[i].dbl() << std::endl;
  
    ampl::DataFrame objs = ampl.getData("_objname, _obj");
    auto objnames = objs.getColumn("_objname");
    auto objvals = objs.getColumn("_obj");
    std::cout << objnames[0].str() << " = $" << std::fixed << std::setprecision(2) << objvals[0].dbl() << std::endl;
    std::cout << std::endl;
}
