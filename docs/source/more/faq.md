(faq)=
# FAQs

## What is AMPL

1. AMPL is a modelling language for describing production, distribution, blending, scheduling and many other kinds of problems known generally as large-scale optimization or mathematical programming.

2. AMPL's familiar algebraic notation and interactive command environment are designed to help formulate models, **communicate with a wide variety of solvers (e.g., Gurobi, CPLEX, etc.)**, and examine solutions. **AMPL connects to most open-source and commercial solvers and allows you to switch easily between them.**

3. **AMPL has [APIs](../ampl/apis.rst) for several popular programming languages (e.g., Python, R, etc.)** and it allows you to only model once in AMPL and interact with it using an API for a language you are familiar with, and possibly deploy to a completely different language with minimal effort since the model remains the same.

4. If you are in Academia: students, researchers, professors teaching optimization, or just graduated, **you can use AMPL and commercial solvers for free** with an [Academic License](https://ampl.com/academia/).

5. **You can use AMPL for free** with open-source solvers with a [Community Edition License](https://ampl.com/ce/) for personal, or commercial prototyping purposes using [AMPL APIs](../ampl/apis.rst). You can also start 30-day trials for individual commercial solvers. We also offer a few other free licenses for you to [start for free now](https://ampl.com/start-free-now/).

## How to Install AMPL

Sign up into the [AMPL Portal](https://portal.ampl.com) to get an account. Then,
please follow the instructions below:
- [Installation guide](https://dev.ampl.com/ampl/install.html)

(cloud_licenses)=
## How do Cloud Licenses Work

Instead of using long term licenses that require static hardware we use short-term leases which give the flexibility of moving the license between different machines or containers.

These leases are stored in a `ampl.lic` file that is replaced every time the lease is renewed. Each lease lasts 5 minutes and it is automatically renewed.

In order to renew a lease, the current license file and a fingerprint are sent to one of our REST API endpoints hosted across multiple cloud providers such as AWS and Azure.

If everything is ok with the request, a new lease is returned in the response and AMPL.lic file is replaced. There is no automatic enforcement of license limits as we just log the renewal.

Even though this mechanism was designed with Docker containers in mind, it also works natively on Windows and macOS virtual and physical machines too. The only requirement is an internet connection.

### Which Information is Collected?

The fingerprint information sent in each request includes among other details the following: 
  - number of CPU cores on the underlying machine
  - number of CPU threads available (e.g., Docker containers may be running restricted to a subset of CPU threads)
  
With the information obtained in the fingerprint we are able to count for any given moment:
  - Total number of concurrent active leases
  - Total number of CPU threads available across all concurrent active leases
  - Total number of different underlying machines with concurrent active leases
  - Total number of CPU cores across all machines with concurrent active leases

### What happens if the limits are exceeded?

If a license is exceeding its limitations for long periods of time users are then contacted to figure out what happened and eventually upgrade the license limits to the customer needs. Since we just log the lease request and each lease lasts 5 minutes, exceeding license limits for short-periods of time is expected for instance when containers are being created and destroyed quickly.

### How to check the status of AMPL cloud services?

You can check the status of AMPL cloud services at <https://status.ampl.com/>.

## How to Use AMPL with Docker Containers

AMPL can be easily used on [Docker containers](https://www.docker.com/):

```Dockerfile
# Use any image as base image with python installed
FROM python:3.9-slim-bullseye
RUN python -m pip install amplpy --no-cache-dir # Install amplpy
RUN python -m amplpy.modules install highs gurobi --no-cache-dir # Install modules
# Environment variables for amplkey (only necessary for non-root containers)
ENV AMPLKEY_RUNTIME_DIR /tmp/ampl/
ENV AMPL_LICFILE /tmp/ampl/ampl.lic
```
We do not provide a base docker image as we give the user total freedom about which base image to use.
In this example, we use the image [`python:3.9-slim-bullseye`](https://hub.docker.com/_/python) as base image.

In the example above we used a Python container, for other options see [AMPL on Docker Containers](ampl_docker).

## What is amplbot?

Amplbot is a specialized AI companion for optimization that helps you learn AMPL, formulate models from natural language, and generate ready-to-run Amplpy code. It streamlines the entire modeling workflow. [Amplbot FAQ](../help/faq_amplbot.md).

You can access it for free in [Amplbot ChatGPT](https://chatgpt.com/g/g-68c00de8b030819185be6db190ad7bce-amplbot).

## How to Add AMPL Installation Directory to PATH/Path?

### Python

On any python script you can add the path to AMPL installation directory to the environment variable `PATH`/`Path` as follows:

```python
import os
os.environ["PATH"] += os.pathsep + "/complete/path/to/ampl/installation/directory/"
```

Note: on Windows you should replace `"PATH"` by `"Path"`.

### Windows

On Windows, you can add the path to AMPL installation directory (e.g., `"C:\ampl.mswin64\"`)
to the environment variable `Path` as described in
<https://www.computerhope.com/issues/ch000549.htm>.

### Linux

On Linux, you can add the path to AMPL installation directory (e.g., `"/opt/ampl.linux-intel64/"`) to the environment variable `PATH` with:
```bash
export PATH="/complete/path/to/ampl.linux-intel64/":$PATH
```
You can add this line to `~/.profile` or `~/.bashrc`.

### macOS

On macOS, you can add the path to AMPL installation directory (e.g., `"/Users/username/bin/ampl.macos64/"`) to the environment variable `PATH` with:
```bash
export PATH="/complete/path/to/ampl.macos64/":$PATH
```
You can add this line to `~/.zshrc`.

## Other Help Resources

```{toctree}
../help/index
```
