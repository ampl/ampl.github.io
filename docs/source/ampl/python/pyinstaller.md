(amplpy.bundle)=
# PyInstaller Bundles

[PyInstaller](https://pyinstaller.org/) is a popular tool in the Python ecosystem used to convert Python applications into standalone executables. It's beneficial when you want to distribute your Python code as a single package, making it easier for users who might not have Python or the required dependencies installed.

We provide an easy way to use PyInstaller to bundle
optimization applications for distribution with
all dependencies including solvers. You can bundle your optimization application using
`python -m amplpy.bundle script_name.py` where `script_name.py` is the main Python script of your application for distribution. In the dist folder you will find the bundled app ready to distribute to your users. This works on Windows, Linux, and macOS.

In case `amplpy.bundle` is not available, please upgrade amplpy to the latest version with `python -m pip install amplpy --upgrade`.

## Quick Example

1) Create and enable a new virtual environment.
  
	```bash
	$ python -m venv venv # Create a new virtual environment

	$ source venv/bin/activate # On Linux and macOS

	$ venvironment\Scripts\activate # On Windows
	```

	```{note}
	The use of a clean virtual environment is important to reduce the dependencies
	included in the bundled app.
	```

2) Install any dependencies you may need on the new virtual environment.

	```bash
	$ python -m pip install -r requirements.txt
	```

3) Install `amplpy` and the solver modules you need.

	```bash
	# Install Python API for AMPL
	$ python -m pip install amplpy --upgrade

	# Install solvers (e.g., HiGHS, Gurobi, COIN-OR)
	$ python -m amplpy.modules install highs gurobi coin
	```

4) Create your main python script.

	For instance `script_name.py`:
	```python
	from amplpy import AMPL
	ampl = AMPL()
	ampl.eval(r"""
	param n integer > 0; # N-queens
	var Row {1..n} integer >= 1 <= n;
	s.t. row_attacks: alldiff ({j in 1..n} Row[j]);
	s.t. diag_attacks: alldiff ({j in 1..n} Row[j]+j);
	s.t. rdiag_attacks: alldiff ({j in 1..n} Row[j]-j);
	""")
	n = 10
	ampl.param["n"] = n
	ampl.solve(solver="highs")
	solution = ampl.get_data("Row").to_dict()
	queens = set((int(r) - 1, int(c) - 1) for c, r in solution.items())
	print("Solution")
	for r in range(n):
		print("".join([" Q " if (r, c) in queens else " + " for c in range(n)]))
	```

5) Install PyInstaller.

	```bash
	python -m pip install pyinstaller
	```
	On Windows, we encountered issues with the latest version, but version 5.1 worked.
	You can install it with `python -m pip install pyinstaller==5.1`. On Linux and macOS,
	the latest version worked without issues.

6) Bundle your application.

	```bash
	python -m amplpy.bundle script_name.py
	...
	Your executable is at ".../dist/script_name/script_name".
	```

	By default the license file will be excluded from the bundle. You can include
	the license file with:
	```bash
	python -m amplpy.bundle script_name.py --keep-license
	```

7) Test your executable.

	```bash
	$ dist/script_name/script_name
	HiGHS 1.6.0: optimal solution
	155 simplex iterations
	1 branching nodes

	Objective = find a feasible point.
	Solution
	Q  +  +  +  +  +  +  +  +  +
	+  +  +  +  +  +  +  Q  +  +
	+  +  +  +  +  Q  +  +  +  +
	+  Q  +  +  +  +  +  +  +  +
	+  +  +  +  +  +  Q  +  +  +
	+  +  +  +  +  +  +  +  +  Q
	+  +  +  Q  +  +  +  +  +  +
	+  +  +  +  +  +  +  +  Q  +
	+  +  +  +  Q  +  +  +  +  +
	+  +  Q  +  +  +  +  +  +  +
	```

8) Distribute your bundled application.

	Distribute the folder `dist/script_name`.

## Licensing

In most situations you will not want to include your own AMPL license in the bundle
for distribution. There are two recommend ways of dealing with that:

- a) Specify the location of the license file for instance in the user home directory:

	Start your script with:
	```python
	import os
	from amplpy import AMPL

	os.environ["AMPL_LICFILE"] = os.path.join(os.path.expanduser("~"), "ampl.lic")

	...
	```
	The person using your bundled app will just need to have the `ampl.lic` file
	in the home directory.

- b) Use an environment variable to pass the license UUID to the application:

	Start your script with:
	```python
	import os
	from amplpy import AMPL, modules

	modules.activate(os.environ["AMPLKEY_UUID"])

	...
	```
	The person using your bundled app will just need to set the environment variable
	`AMPLKEY_UUID` with the license UUID to use.
