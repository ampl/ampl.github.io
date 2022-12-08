import subprocess

SOLVERS = {
    "BARON": "baron",
    "CONOPT": "conopt",
    "CPLEX": "cplex",
    "GUROBI": "gurobi",
    "KNITRO": "knitro",
    "Lindo Global": "lindoglobal",
    "LOQO": "loqo",
    "LGO": "lgo",
    "MINOS": "minos",
    "SNOPT": "snopt",
    "XPRESS": "xpress",
    "COPT": "copt",
    "GUROBIASL": "gurobiasl",
    "XPRESSASL": "xpressasl",
    "HiGHS": "highs",
    "CBC": "cbc",
}


for label, solver in SOLVERS.items():
    output = subprocess.check_output([solver, "-="]).decode()

    with open(f"source/solvers/options/{solver}.md", "w") as f:
        print(
            f"""
# {label} Options

```ampl
ampl: option solver {solver}; # change the solver
ampl: option {solver}_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

Solver options obtained with `$ {solver} -=`.

```
{output}
```
""",
            file=f,
        )
