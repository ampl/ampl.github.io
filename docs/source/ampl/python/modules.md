# AMPL Modules for Python

AMPL and all Solvers are now available as Python Packages:

```bash
# Install Python API for AMPL:
$ python -m pip install amplpy --upgrade

# Install solvers (e.g., HiGHS and Gurobi)
$ python -m amplpy.modules install highs gurobi 

# Activate your license (e.g., free https://ampl.com/ce license):
$ python -m amplpy.modules activate <license-uuid>

# Import, load, and instantiate in Python:
$ python
>>> from amplpy import AMPL
>>> ampl = AMPL() # instantiate AMPL object
```

[Python API (amplpy) Documentation](https://amplpy.readthedocs.io/)

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
	gokestrel
	gurobi
	highs
	knitro
	lgo
	lindoglobal
	loqo
	minos
	octeract
	open
	plugins
	snopt
	xpress
```

### path
Value to append to the environment variable PATH to access modules:
```bash
$ python -m amplpy.modules path
```
Example: 
```
export PATH=$PATH:`python -m amplpy.modules path`
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
