import subprocess
import os
import re
import json

SOLVERS = {
    "BARON": "baron",
    "CONOPT": "conopt",
    "CPLEX": "cplex",
    "CPLEXMP": "cplexmp",
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
    "MOSEK": "mosek",
    "SCIP": "scip",
    "GCG": "gcg",
    "SCIP-CPX": "scip-cpx",
    "GCG-CPX": "gcg-cpx",
}

releases = {}
for label, solver in SOLVERS.items():
    output = subprocess.check_output([solver, "-="]).decode()  # (errors="ignore")

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
        fname = f"solvers/{solver}/changes.md"
        if solver.endswith("asl"):
            fname = f"solvers/{solver[:-3]}/changesasl.md"
        elif solver.endswith("mp"):
            fname = f"solvers/{solver[:-2]}/changesmp.md"
        releases[solver] = {
            "label": label,
            "file": fname,
            "versions": re.findall(r"## (\d{8})", content),
        }
        open(f"source/{fname}", "w").write(content)
    else:
        print(f"No changelog for {solver}.")

    if solver.endswith("asl"):
        fname = f"source/solvers/{solver.replace('asl', '')}/{solver}.md"
    elif solver.endswith("mp"):
        fname = f"source/solvers/{solver.replace('mp', '')}/{solver}.md"
    elif solver.endswith("-cpx"):
        fname = f"source/solvers/{solver.replace('-cpx', '')}/{solver}.md"
    else:
        fname = f"source/solvers/{solver}/options.md"

    with open(fname, "w") as f:
        print(
            f"""
# {label} Options

```ampl
ampl: option solver {solver}; # change the solver
ampl: option {solver.replace('-cpx', '')}_options 'option1=value1 option2=value2'; # specify options
ampl: solve; # solve the problem
```

Solver options obtained with `$ {solver} -=`.

```
{output}
```
""",
            file=f,
        )

releases["ampl"] = {
    "label": "AMPL",
    "file": "releases/ampl.md",
    "versions": re.findall(r"## (\d{8})", open("source/releases/ampl.md").read()),
}


released_on = {}
for item in releases:
    for date in releases[item]["versions"]:
        if date not in released_on:
            released_on[date] = []
        released_on[date].append(item)


changes = open("source/releases/index.md", "w")
print(
    """(releases)=

# Release History

""",
    file=changes,
)

changelogs = {
    (releases[item]["label"], item): releases[item]["file"] for item in releases
}
for label, item in sorted(changelogs):
    latest = max(releases[item]["versions"])
    fname = changelogs[label, item]
    print(
        f"- [**{label}** Changelog (latest: **{latest}**)](../{fname})",
        file=changes,
    )

print(
    """
```{toctree}
:hidden:
:glob:
ampl.md
```

""",
    file=changes,
)

for date in sorted(released_on, reverse=True):
    print(f"## {date}", file=changes)
    if len(released_on[date]) != len(set(released_on[date])):
        print(date, released_on[date])
    for item in sorted(set(released_on[date])):
        label, fname = releases[item]["label"], releases[item]["file"]
        print(f"- [{label}](../{fname}#{date})", file=changes)
