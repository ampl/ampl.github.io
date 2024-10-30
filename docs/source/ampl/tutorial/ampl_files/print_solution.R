print_solution <- function(ampl) {
    solver <- ampl$getOption("solver")
    cat("Solution with:", solver, "\n")
    
    vars <- ampl$getData("_varname, _var")
    varnames <- vars$X_varname
    varvals <- vars$X_var
    mapply(function(n, v) cat(n, "=", v, "\n"), varnames, varvals)

    objs <- ampl$getData("_objname, _obj")
    objnames <- objs$X_objname
    objvals <- objs$X_obj
    cat(objnames[1], "=", sprintf("$%.2f", objvals[1]), "\n")
    cat("\n")
}
