import subprocess

SOLVERS = {
    "BARON": "baron",
    "CONOPT": "conopt",
    "CPLEX": "cplex",
    "GUROBI": "gurobi",
    "KNITRO": "knitro",
    "Lindo Global": "lindoglobal",
    "LOQO": "loqo",
    "MINOS": "minos",
    "SNOPT": "snopt",
    "XPRESS": "xpress",
    "COPT": "copt",
    "x-GUROBI": "x-gurobi",
}


for label, solver in SOLVERS.items():
    output = subprocess.check_output([solver, "-="]).decode()

    with open(f"source/solver_options/{solver}_options.md", "w") as f:
        print(
            f"""
# {label} Options

Obtained with `$ {solver} -=`.

```
{output}
```
""",
            file=f,
        )
