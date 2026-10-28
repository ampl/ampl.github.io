"""Update the solver pages and the release index from the installed solvers.

For each solver in SOLVERS found on PATH, writes
- source/solvers/<page>/options.md from `<solver> -=`,
- source/solvers/<page>/solve_results.inc from `<solver> -!`, or, for drivers
  without `-!` (classic ASL drivers), AMPL's generic solve result table,
- source/solvers/<page>/changes.md from CHANGES.<solver>.md next to `ampl`
  (in <ampl dir>/docs), when that file exists.
Then downloads the MP, amplpy, GSL, AMPLS and cuOpt changelogs and rewrites
source/releases/index.md.
"""
import argparse
import subprocess
import os
import re
from generate_activity_chart import activity_chart_block

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
    "MP2NL": "mp2nl",
    "Kestrel": "kestrel",
    "PATH": "path",
    "CP-SAT": "cpsat",
    "Gecode": "gecode",
}

# AMPL's default option solve_result_table, for drivers without `-!`
GENERIC_SOLVE_RESULTS = """\
Solve result table (AMPL default ranges)
          0- 99 solved: optimal for an optimization problem, feasible for a satisfaction problem
        100-199 solved? solution candidate returned but error likely
        200-299 infeasible
        300-399 unbounded
        400-499 limit
        500-999 failure, no solution returned
"""

parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog="""Examples:
  # full update from the AMPL bundle on PATH (as for a release):
  python update_changes.py
  # only CP-SAT and Gecode, keep the downloaded changelogs as they are:
  PATH=~/solvers/bin:$PATH python update_changes.py --solvers cpsat,gecode --no-fetch
""",
)
parser.add_argument(
    "--solvers",
    help="comma-separated driver names (values of SOLVERS) to update; the others "
    "keep their pages and are indexed from their existing changes.md. "
    "Default: all. Example: --solvers gurobi,highs,cpsat",
)
parser.add_argument(
    "--no-fetch",
    action="store_true",
    help="do not download the MP, amplpy, GSL, AMPLS and cuOpt changelogs; index "
    "the copies already in source/ instead. Example: --no-fetch",
)
parser.add_argument(
    "--no-changes",
    action="store_true",
    help="do not rewrite solver changes.md files, only options and solve results; "
    "the release index is built from the existing changes.md files. "
    "Example: --no-changes",
)
args = parser.parse_args()
selected = set(args.solvers.split(",")) if args.solvers else set(SOLVERS.values())
unknown = selected - set(SOLVERS.values())
if unknown:
    parser.error(f"unknown solver(s): {', '.join(sorted(unknown))}")

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


def solver_output(solver, flag):
    """Output of `solver flag`, or None if the driver is missing or rejects the flag."""
    try:
        r = subprocess.run(
            [solver, flag],
            capture_output=True,
            text=True,
            timeout=60,
            stdin=subprocess.DEVNULL,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    if r.returncode != 0:
        return None
    return r.stdout.strip()


def solve_results(solver):
    """`solver -!` when the driver lists its codes, else AMPL's generic table."""
    output = solver_output(solver, "-!")
    if output and output.startswith("Solve result table"):
        return output.expandtabs(8) + "\n"
    return GENERIC_SOLVE_RESULTS


def page_file(solver, name):
    """Path of a generated file for a driver; variants go to the main page."""
    for suffix in ("asl", "mp", "-cpx"):
        if solver.endswith(suffix):
            page = solver[: -len(suffix)]
            stem, ext = os.path.splitext(name)
            return f"source/solvers/{page}/{stem}_{solver}{ext}"
    return f"source/solvers/{solver}/{name}"


def changes_file(solver):
    if solver.endswith("asl"):
        return f"solvers/{solver[:-3]}/changesasl.md"
    if solver.endswith("mp"):
        return f"solvers/{solver[:-2]}/changesmp.md"
    return f"solvers/{solver}/changes.md"


def index_entry(label, fname):
    return {
        "label": label,
        "file": fname,
        "versions": re.findall(
            r"^## (\d{8})", open(f"source/{fname}").read(), re.MULTILINE
        ),
    }


releases = {}
ampl_location = subprocess.check_output(["which", "ampl"]).decode()
for label, solver in SOLVERS.items():
    fname = changes_file(solver)
    if solver not in selected:
        if os.path.exists(f"source/{fname}"):
            releases[solver] = index_entry(label, fname)
        continue

    output = solver_output(solver, "-=")
    if output is None:
        print(f"{solver} -= failed")
        output = ""

    if solver in ["lgo"]:
        # handle solvers whose changelog are not being distributed
        changes = f"source/solvers/{solver}/changes.md"
    else:
        changes = os.path.join(
            os.path.dirname(ampl_location), "docs", f"CHANGES.{solver}.md"
        )

    if not args.no_changes and os.path.exists(changes):
        content = open(changes, "r").read().strip()
        if content.startswith("#"):
            content = content[content.find("#") :]
            content = content[content.find("\n") + 1 :]
        else:
            content = content[content.find("==") :]
            content = content[content.find("\n") + 1 :]
        content = re.sub(r"###+ (\d+)", r"## \g<1>", content)
        content = f"# {label} Changelog\n\n" + filter_changelog(content)
        open(f"source/{fname}", "w").write(content)
    elif not args.no_changes:
        print(f"No changelog for {solver}.")
    if os.path.exists(f"source/{fname}"):
        releases[solver] = index_entry(label, fname)

    if output == "":
        print(f"No options for {solver}.")
        continue

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

    with open(page_file(solver, "solve_results.inc"), "w") as f:
        f.write(solve_results(solver))

# Index AMPL changelog
releases["ampl"] = index_entry("AMPL", "releases/ampl.md")

# Download (unless --no-fetch) and index the other changelogs
REMOTE = [
    (
        "mp",
        "AMPL MP",
        "releases/mp.md",
        "# AMPL MP Library Changelog",
        "https://raw.githubusercontent.com/ampl/mp/refs/heads/develop/CHANGES.mp.md",
    ),
    (
        "amplpy",
        "AMPLPY",
        "releases/amplpy.md",
        "# amplpy Changelog",
        "https://raw.githubusercontent.com/ampl/amplpy/refs/heads/master/CHANGELOG.md",
    ),
    (
        "amplgsl",
        "GSL",
        "releases/amplgsl.md",
        "# AMPL GSL Library Changelog",
        "https://raw.githubusercontent.com/ampl/gsl/cf180cd7fbd06039a577f9c9ff0b428784765ac1/ampl/CHANGES.amplgsl.md",
    ),
    (
        "ampls",
        "AMPLS",
        "releases/ampls.md",
        "# AMPLS Libraries Changelog",
        "https://raw.githubusercontent.com/ampl/ampls-api/refs/heads/master/changes.md",
    ),
    (
        "cuopt",
        "cuOpt",
        "solvers/cuopt/changes.md",
        "# CUOPT Changelog",
        "https://raw.githubusercontent.com/ampl/mp/refs/heads/develop/solvers/cuoptmp/CHANGES.cuoptmp.md",
    ),
]
for item, label, fname, title, url in REMOTE:
    if not args.no_fetch:
        text = fetch_url_content(url)
        text = text[text.find("##") :]
        open(f"source/{fname}", "w").write(f"{title}\n\n{text}")
    releases[item] = {
        "label": label,
        "file": fname,
        "versions": re.findall(r"## (\d{8})", open(f"source/{fname}").read()),
    }

released_on = {}
for item in releases:
    for date in releases[item]["versions"]:
        if date not in released_on:
            released_on[date] = []
        released_on[date].append(item)


def anchor(fname, date):
    """Anchor of the heading for date in fname: '## <date>' if there is one,
    else the first heading that starts with it, e.g. '## 20190605, 20190606'
    has the anchor 20190605-20190606."""
    headings = [l[3:].strip() for l in open(f"source/{fname}") if l.startswith("## ")]
    if date in headings:
        return date
    for text in headings:
        if text.startswith(date):
            return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return date


changes = open("source/releases/index.md", "w")
print(
    """(releases)=

# Product Updates

""",
    file=changes,
)
print(activity_chart_block(released_on), file=changes, end="")

print("## Changelogs", file=changes)
changelogs = {
    (releases[item]["label"], item): releases[item]["file"] for item in releases
}
md_list = []
for label, item in sorted(changelogs, key=lambda x: x[0].lower()):
    latest = max(releases[item]["versions"])
    fname = changelogs[label, item]
    md_list.append(f"../{fname}")
    print(
        f"- [**{label}** Changelog (latest: **{latest}**)](../{fname})",
        file=changes,
    )


print(
    f"""
```{{toctree}}
:hidden:
:glob:
{'\n'.join(md_list)}
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
        print(f"- [{label}](../{fname}#{anchor(fname, date)})", file=changes)
