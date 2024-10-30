def print_solution(ampl):
    solver = ampl.get_option("solver")
    print(f"Solution with: {solver}")

    vars = ampl.get_data("_varname, _var")
    varnames = vars.get_column("_varname")
    varvals = vars.get_column("_var")
    for n, v in zip(varnames, varvals) :
        print(f"{n} = {v}")

    objs = ampl.get_data("_objname, _obj")
    objnames = objs.get_column("_objname")
    objvals = objs.get_column("_obj")
    print(f"{next(iter(objnames))} = ${next(iter(objvals)):.2f}")
    print()
