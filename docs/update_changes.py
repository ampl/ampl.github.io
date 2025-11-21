import subprocess
import os
import re
import json

SOLVERS = {
    "BARON": "baron",
    "BARONMP": "baronmp",
    "CONOPT": "conopt",
    "CPLEX": "cplex",
    "CPLEXASL": "cplexasl",
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
    "IPOPT": "ipopt",
    "BONMIN": "bonmin",
    "COUENNE": "couenne",
    "MOSEK": "mosek",
    "SCIP": "scip",
    "GCG": "gcg",
    "SCIP-CPX": "scip-cpx",
    "GCG-CPX": "gcg-cpx",
}

import requests


def fetch_url_content(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def filter_changelog(changelog):
    h2_pattern = r"## \d{8}"
    entries = re.split(r"(?=## \d{8})", changelog)
    filtered_entries = [
        entry for entry in entries if re.match(h2_pattern, entry.strip())
    ]
    filtered_changelog = "".join(filtered_entries)
    return filtered_changelog


releases = {}
for label, solver in SOLVERS.items():
    try:
        output = subprocess.check_output([solver, "-="]).decode().strip()
    except:
        print(f"{solver} -= failed")
        continue
    # (errors="ignore")
    # subprocess.check_output(f"{solver} -= || true", shell=True).decode().strip()

    exec_location = subprocess.check_output(["which", solver]).decode()
    if solver in ["lgo"]:
        # handle solvers whose changelog are not being distributed
        changes = f"source/solvers/{solver}/changes.md"
    else:
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
        content = f"# {label} Changelog\n\n" + filter_changelog(content)
        fname = f"solvers/{solver}/changes.md"
        if solver.endswith("asl"):
            fname = f"solvers/{solver[:-3]}/changesasl.md"
        elif solver.endswith("mp"):
            fname = f"solvers/{solver[:-2]}/changesmp.md"
        # Index solver changelog
        releases[solver] = {
            "label": label,
            "file": fname,
            "versions": re.findall(r"^## (\d{8})", content, re.MULTILINE),
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

# Index AMPL changelog
releases["ampl"] = {
    "label": "AMPL",
    "file": "releases/ampl.md",
    "versions": re.findall(r"## (\d{8})", open("source/releases/ampl.md").read()),
}

# Download and index MP changelog
mp_changelog = fetch_url_content(
    "https://raw.githubusercontent.com/ampl/mp/refs/heads/develop/CHANGES.mp.md"
)
mp_changelog = mp_changelog[mp_changelog.find("##") :]
mp_changelog = f"# AMPL MP Library Changelog\n\n{mp_changelog}"
open("source/releases/mp.md", "w").write(mp_changelog)
releases["mp"] = {
    "label": "MP",
    "file": "releases/mp.md",
    "versions": re.findall(r"## (\d{8})", open("source/releases/mp.md").read()),
}

cuopt_changelog = fetch_url_content(
    "https://raw.githubusercontent.com/ampl/mp/refs/heads/develop/solvers/cuoptmp/CHANGES.cuoptmp.md"
)
cuopt_changelog = cuopt_changelog[cuopt_changelog.find("##") :]
cuopt_changelog = f"# CUOPT Changelog\n\n{cuopt_changelog}"
open("source/solvers/cuopt/changes.md", "w").write(cuopt_changelog)
releases["cuopt"] = {
    "label": "cuOpt",
    "file": "solvers/cuopt/changes.md",
    "versions": re.findall(
        r"## (\d{8})", open("source/solvers/cuopt/changes.md").read()
    ),
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
for label, item in sorted(changelogs, key=lambda x: x[0].lower()):
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
mp.md
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
