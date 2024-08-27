(amplpy.modules)=
# AMPL Modules for Python

AMPL and all Solvers are now available as Python Packages:

```bash
# Install Python API for AMPL
$ python -m pip install amplpy --upgrade

# Install solvers (e.g., HiGHS and Gurobi)
$ python -m amplpy.modules install highs gurobi 

# Activate your license (e.g., free https://ampl.com/ce license)
$ python -m amplpy.modules activate <license-uuid>

# Import in Python
$ python
>>> from amplpy import AMPL
>>> ampl = AMPL() # instantiate AMPL object
```

[Python API (amplpy) Documentation](https://amplpy.ampl.com/)

## Modules available

List of modules available:

- [Open-source solvers](https://ampl.com/products/solvers/open-source-solvers/): `highs`, `cbc`, `coin` (includes: CBC, Couenne, Ipopt, Bonmin), `open` (includes all open-source solvers)

-  [NEOS Server](https://www.neos-server.org/): `gokestrel` ([kestrel client](https://dev.ampl.com/solvers/kestrel.html))

-   Commercial solvers: [`baron`](https://ampl.com/products/solvers/solvers-we-sell/baron/), [`conopt`](https://ampl.com/products/solvers/solvers-we-sell/conopt/), [`copt`](https://ampl.com/products/solvers/solvers-we-sell/copt/), [`cplex`](https://ampl.com/products/solvers/solvers-we-sell/cplex/), [`gurobi`](https://ampl.com/products/solvers/solvers-we-sell/gurobi/), [`knitro`](https://ampl.com/products/solvers/solvers-we-sell/knitro/), [`lgo`](https://ampl.com/products/solvers/solvers-we-sell/lgo/), [`lindoglobal`](https://ampl.com/products/solvers/solvers-we-sell/lindoglobal/), [`loqo`](https://ampl.com/products/solvers/solvers-we-sell/loqo/), [`minos`](https://ampl.com/products/solvers/solvers-we-sell/minos/), [`mosek`](https://ampl.com/products/solvers/solvers-we-sell/mosek/), [`octeract`](https://ampl.com/products/solvers/solvers-we-sell/octeract/), [`snopt`](https://ampl.com/products/solvers/solvers-we-sell/snopt/), [`xpress`](https://ampl.com/products/solvers/solvers-we-sell/xpress/)

-   AMPL Plugins: `amplgsl` ([amplgsl docs](https://gsl.ampl.com/)), `plugins` ([amplplugins docs](https://plugins.ampl.com/))

## Commands

### usage

List usage instructions:
```
$ python -m amplpy.modules usage
```

### install

Install modules:
```bash
$ python -m amplpy.modules install <solver 1> <solver 2> ...
```
Example:
```bash
$ python -m amplpy.modules install highs gurobi
```

### activate

Activate a license (e.g., free <https://ampl.com/ce> license):
```bash
$ python -m amplpy.modules activate <license-uuid>
```

### uninstall

Uninstall modules:
```bash
$ python -m amplpy.modules uninstall <solver 1> <solver 2> ...
```
Example:
```bash
$ python -m amplpy.modules uninstall gurobi highs
```

### installed
List installed modules:
```bash
$ python -m amplpy.modules installed
```
Example:
```bash
$ python -m amplpy.modules installed
You have the following modules installed:
	base
	gurobi
	highs
```

### available
List modules available to be installed:
```bash
$ python -m amplpy.modules available
You can install any of the following modules:
	amplgsl
	baron
	base
	cbc
	coin
	conopt
	copt
	cplex
	gcg
	gecode
	gokestrel
	gurobi
	highs
	ilogcp
	knitro
	lgo
	lindoglobal
	loqo
	minos
	mosek
	octeract
	open
	plugins
	scip
	snopt
	xpress
```

### path
Value to append to the environment variable PATH to access modules:
```bash
$ python -m amplpy.modules path
```
Example: 
```bash
export PATH=$PATH:`python -m amplpy.modules path`
```

### find
Find the path to a file in any module:
```bash
$ python -m amplpy.modules find <file name>
```
Example:
```bash
$ python -m amplpy.modules find gurobi
```

### requirements
Generate `requirements.txt` for the modules currently installed:
```bash    
$ python -m amplpy.modules requirements
--index-url https://pypi.ampl.com
--extra-index-url https://pypi.org/simple
ampl_module_base==20221226
ampl_module_gurobi==20221228
ampl_module_highs==20221228
```

### run
Run command in the same environment as the modules
```bash
$ python -m amplpy.modules run <command>
```
Example:
```bash
$ python -m amplpy.modules run ampl -v
AMPL Version 20221013 (Darwin-20.6.0, 64-bit)
Demo license with maintenance expiring 20240131.
ampl:
```

## Programmatically

All of this is also available from Python programmatically:

```python
>>> from amplpy import modules
>>> modules.installed()
['base', 'gurobi', 'highs']
>>> modules.available()
['baron', 'cbc', 'lindoglobal', 'xpress', 'gurobi', 'lgo', 'open', 'minos', 'octeract', 'copt', 'plugins', 'amplgsl', 'loqo', 'conopt', 'base', 'cplex', 'snopt', 'coin', 'knitro', 'highs', 'gokestrel']
>>> modules.install('cplex')
>>> modules.installed()
['base', 'cplex', 'gurobi', 'highs']
>>> modules.uninstall('cplex')
>>> modules.installed()
['base', 'gurobi', 'highs']
```

## How to use modules

### Install modules

```bash
# Install Python API for AMPL
$ python -m pip install amplpy --upgrade

# Install solvers (e.g., HiGHS, Gurobi, COIN-OR)
$ python -m amplpy.modules install highs gurobi coin

# Activate your license (e.g., free https://ampl.com/ce license)
$ python -m amplpy.modules activate <license-uuid>
```

### Using from AMPL

Installed modules are loaded by default when [amplpy](https://amplpy.ampl.com) is loaded.

```python
from amplpy import AMPL
ampl = AMPL()  # instantiate AMPL object
ampl.option["solver"] = "highs"  # use the solver highs
```

In case you have another AMPL installation and want to ensure that modules
are used, you can do that as follows:

```python
from amplpy import AMPL, modules
modules.load()  # load all modules
ampl = AMPL()  # instantiate AMPL object
```

### Using from Pyomo

Even though the [NL format](https://en.wikipedia.org/wiki/Nl_(format))
was invented for connecting solvers to AMPL, it has been adopted by other systems
such as Pyomo. [Pyomo](https://www.pyomo.org/) is an open-source modeling tool written in Python
that is compatible with solvers that read .nl files, which means it works with all
[AMPL solvers](solvers). You can use AMPL solvers with Pyomo as follows:

Install modules for HiGHS, CBC, Couenne, Bonmin, Ipopt, SCIP, and GCG:
```bash
!pip install amplpy pyomo -q
!python -m amplpy.modules install coin highs scip gcg -q  # Install HiGHS, CBC, Couenne, Bonmin, Ipopt, SCIP, and GCG
```

Use the solver modules from Pyomo:
```python
from amplpy import modules
import pyomo.environ as pyo
solver_name = "highs"  # "highs", "cbc",  "couenne", "bonmin", "ipopt", "scip", or "gcg".
solver = pyo.SolverFactory(solver_name+"nl", executable=modules.find(solver_name), solve_io="nl")

model = pyo.ConcreteModel()
model.x = pyo.Var([1,2], domain=pyo.NonNegativeReals)
model.OBJ = pyo.Objective(expr = 2*model.x[1] + 3*model.x[2])
model.Constraint1 = pyo.Constraint(expr = 3*model.x[1] + 4*model.x[2] >= 1)
solver.solve(model, tee=True)
```

Note that Pyomo is typically substantially slower than AMPL
due to being written completely in Python (e.g., not performing the model instantiation using heavily optimized C code like AMPL does), and that it may also not be able to take advantage
of all functionalities of our solver drivers (especially the ones built with the new [MP interface](https://mp.ampl.com/)); the solver performance when used from AMPL also tends to be superior
due to AMPL's presolver that is typically able to reduce model sizes substantially.
Nevertheless, feel free to use any of our solvers with other modeling tools.

```{note}
**Pyomo is an independent open-source project. It is not developed or maintained by AMPL.** We can just provide support related to deployment using our [solver drivers](solvers). For any Pyomo issues not related to our solvers
please check the support channels at <https://www.pyomo.org/>.
```

