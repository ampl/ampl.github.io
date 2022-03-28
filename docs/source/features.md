# What's new?

## Using AMPL in Google Colab, Kaggle, and similar platforms

We have a set of Jupyter Notebooks available on our [Model Colaboratory](https://colab.ampl.com).

You can use our template (<https://colab.ampl.com/en/latest/tag-template.html>)
as a starting point. Our cloud licenses, include AMPL CE licenses, work on all cloud platforms.

## Snapshot feature (save and restore AMPL sessions)

In your AMPL bundle you should find `x-ampl`, the development version of AMPL where experimental features are enabled. One of such features is the snapshot command which allows saving the AMPL session in such a way that you can restore the state of AMPL using it.

### Example using it with amplpy

You need to be using at least amplpy 0.8.0 (you can install it with `python -m pip install amplpy==0.8.0`). With this version of  amplpy it is possible to pass an additional argument to [Environment](https://amplpy.readthedocs.io/en/stable/classes/environment.html) that allows specifing the executable name as follows:

```python
ampl = AMPL(Environment('', 'x-ampl'))
```

You can then use `AMPL.get_output` to retrieve the output of the new command "snapshot;" as a string. The string returned is a compact representation of the AMPL state (model declaration, data, solution loaded, options, etc.)
```python
snapshot = ampl.get_output('snapshot;')
print(snapshot)
```
This string can then be passed to another AMPL object using `AMPL.eval`. The following example produces the output below:
```python
from amplpy import AMPL, Environment

print('First object:')
ampl = AMPL(Environment('', 'x-ampl'))
ampl.read('diet.mod')
ampl.read_data('diet.dat')
ampl.option['solver'] = 'gurobi'
ampl.solve()

print('Second object:')
ampl2 = AMPL(Environment('', 'x-ampl'))
snapshot = ampl.get_output('snapshot;')
print(snapshot, file=open('snapshot.run', 'w'))
ampl2.eval(snapshot)
ampl2.display('Buy')

print('Third object:')
ampl3 = AMPL(Environment('', 'x-ampl'))
ampl3.eval(ampl2.get_output('snapshot;'))
ampl3.display('_VARS;')
ampl3.eval('option solver;')

```


```
First object:
Gurobi 9.1.2: optimal solution; objective 88.2
1 simplex iterations
Second object:
Buy [*] :=
BEEF   0
 CHK   0
FISH   0
 HAM   0
 MCH  46.6667
 MTL   0
 SPG   0
 TUR   0
;

Third object:
set _VARS := Buy;

option solver gurobi;
```

One thing that may also be useful: In the example, there is the line `print(snapshot, file=open('snapshot.run', 'w'))` that writes the snapshot to a file called `snapshot.run`. This file can be loaded into AMPL (e.g., for debugging) as follows:
```
$ ampl
ampl: include "snapshot.run";
ampl: display Buy;
Buy [*] :=
BEEF   0
 CHK   0
FISH   0
 HAM   0
 MCH  46.6667
 MTL   0
 SPG   0
 TUR   0
;
```
The snapshot feature is not finished and it is still being perfected. If you encounter any issues, please let us know.

## Enhanced Gurobi driver (x-gurobi)

We have released `x-gurobi`, the beta version of our enhanced AMPL-Gurobi interface.
It has the following features:

- Full support of logical expressions and constraints, as described in the AMPL page on Logic and Constraint Programming Extensions.
- Algebraic expressions beyond linear and quadratic.
- Choice between conversions in the driver vs. native solver support.

[[Modeling Guide](https://amplmp.readthedocs.io/en/latest/rst/model-guide.html)] [[x-gurobi options](solver_options/x-gurobi_options.md)]

## Using AMPL in docker containers

We do not provide a base docker image as we give the user total freedom about which base image to use.

We provide a set of commands for downloading and installing all the modules that the user may need.

In the Dockerfile example below, we install AMPL, Gurobi, and COIN-OR solvers.

The license is also installed so that the container is ready to use after being built.

In this example we also install amplpy so that the Python API for AMPL is also ready to be used.

```Dockerfile
# Use any image as base image
FROM python:3.9-slim-buster
# Install curl in order to download the modules necessary
RUN apt-get update && apt-get install -y curl
# Build arguments
ARG LICENSE_UUID=f9758f88-b0a3-11eb-9e10-c75c7742e3ae
ARG MODULES_URL=https://ampl.com/dl/modules
# Download ampl-module.linux64.tgz
RUN cd /opt/ && curl -O ${MODULES_URL}/ampl-module.linux64.tgz && \
    tar xzvf ampl-module.linux64.tgz && rm ampl-module.linux64.tgz
# Download gurobi-module.linux64.tgz
RUN cd /opt/ && curl -O ${MODULES_URL}/gurobi-module.linux64.tgz && \
    tar xzvf gurobi-module.linux64.tgz && rm gurobi-module.linux64.tgz
# Download coin-module.linux64.tgz
RUN cd /opt/ && curl -O ${MODULES_URL}/coin-module.linux64.tgz && \
    tar xzvf coin-module.linux64.tgz && rm coin-module.linux64.tgz
# Download ampl.lic file
RUN cd /opt/ampl.linux-intel64/ && \
    curl -O https://portal.ampl.com/download/license/${LICENSE_UUID}/ampl.lic
# Add installation directory to the environment variable PATH
ENV PATH="/opt/ampl.linux-intel64/:${PATH}"

# RUN pip3 install -r requirements.txt
RUN pip3 install amplpy
```

## Cloud licensing

We have a new licensing mechanism for deployment in virtual environments such as cloud services and containers.

Instead of using long term licenses that require static hardware we use short-term leases which give the flexibility of moving the license between different machines or containers.

These leases are stored in a `ampl.lic` file that is replaced every time the lease is renewed. Each lease lasts 5 minutes and it is automatically renewed.

In order to renew a lease, the current license file and a fingerprint are sent to one of our REST API endpoints hosted across multiple cloud providers such as AWS and Azure.

If everything is ok with the request, a new lease is returned in the response and the ampl.lic file is replaced. There is no automatic enforcement of license limits as we just log the renewal.

The fingerprint information sent in each request includes among other details the following: 
  - number of CPU cores on the underlying machine
  - number of CPU threads available (e.g., Docker containers may be running restricted to a subset of CPU threads)
  
With the information obtained in the fingerprint we are able to count for any given moment:
  - Total number of concurrent active leases
  - Total number of CPU threads available across all concurrent active leases
  - Total number of different underlying machines with concurrent active leases
  - Total number of CPU cores across all machines with concurrent active leases

If a license is exceeding its limitations for long periods of time users are then contacted to figure out what happened and eventually upgrade the license limits to the customer needs. Since we just log the lease request and each lease lasts 5 minutes, exceeding license limits for short-periods of time is expected for instance when containers are being created and destroyed quickly.

Even though this mechanism was designed with Docker containers in mind, it also works natively on Windows and macOS virtual and physical machines too. The only requirement is an internet connection.

## Using remote solvers from NEOS with gokestrel

To simplify the work of comparing and testing solvers, we have made AMPL and solver resources available online in collaboration with the [NEOS Server](http://www.neos-server.org/) project, under the auspices of the [Wisconsin Institutes for Discovery](http://www.discovery.wisc.edu/) at the University of Wisconsin, Madison. 

Thanks to [gokestrel](https://github.com/ampl/gokestrel), our new Kestrel driver, instead of specifying a solver installed on your computer or local network, you invoke Kestrel, a "client" program that sends your problem to a solver running on one of the NEOS Server's remote computers. The results from the NEOS Server are eventually returned through Kestrel to AMPL, where you can view and manipulate them locally in the usual way.

Important options:
- `email`: your e-mail address (it is required by NEOS).
- `kestrel_options`: allows you to specify among other things, the solver to use

As an example, here is how you might invoke Kestrel from a local AMPL session, using CPLEX as your remote solver:
```
ampl: model diet.mod;
ampl: data diet.dat;
ampl: option solver kestrel;
ampl: option email "***@***.***";
ampl: option kestrel_options "solver=cplex";
ampl: option cplex_options "display=2";
ampl: solve;
Connecting to: neos-server.org:3333
Job XXXX submitted to NEOS, password='xxxx'
Check the following URL for progress report:
https://neos-server.org/neos/cgi-bin/nph-neos-solver.cgi?admin=results&jobnumber=XXXX&pass=xxxx
Job XXXX dispatched
password: xxxx
---------- Begin Solver Output -----------
Condor submit: 'neos.submit'
Condor submit: 'watchdog.submit'
Job submitted to NEOS HTCondor pool.
CPLEX 20.1.0.0: optimal solution; objective 88.2
1 dual simplex iterations (0 in phase I)
```