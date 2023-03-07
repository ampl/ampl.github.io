import subprocess
import os
import re

SOLVERS = {
    "BARON": "baron",
    "CONOPT": "conopt",
    "CPLEX": "cplex",
    "ILOGCP": "ilogcp",
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

    exec_location = subprocess.check_output(["which", solver]).decode()
    changes = os.path.join(
        os.path.dirname(exec_location), "docs", f"CHANGES.{solver}.md"
    )
    if os.path.exists(changes):
        content = open(changes, "r").read().strip()
        if content.startswith("#"):
            content = content[content.find("#") :]
            content = content[content.find("\n") + 1 :]
        else:
            content = content[content.find("==") :]
            content = content[content.find("\n") + 1 :]
        content = re.sub(r"###+ (\d+)", r"## \g<1>", content)
        content = f"# {label} Changelog\n" + content
        dst = f"source/solvers/{solver}/changes.md"
        if solver.endswith("asl"):
            dst = f"source/solvers/{solver[:-3]}/changesasl.md"
        open(dst, "w").write(content)
    else:
        print(f"No changelog for {solver}.")

    fname = f"source/solvers/{solver}/options.md"
    if solver.endswith("asl"):
        fname = f"source/solvers/{solver.replace('asl', '')}/{solver}.md"
    with open(fname, "w") as f:
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
