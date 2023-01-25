# AMPL on Docker Containers

Since AMPL and all Solvers are now available as [Python Packages](modules.md). 
This makes AMPL really simple to use with [Docker containers](https://www.docker.com/):

```Dockerfile
# Use any image as base image
FROM python:3.9-slim-bullseye
RUN python -m pip install amplpy # Install amplpy
RUN python -m amplpy.modules install highs gurobi  # Install modules
```

You can build and run the container as follows:
```bash
$ docker build . --tag ampl-container
$ docker run --rm -it ampl-container bash
root@c240a014dd67:/# python
Python 3.9.16 (main, Jan 23 2023, 23:42:27)
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from amplpy import AMPL, modules
>>> modules.load()
>>> ampl = AMPL()
>>>
```
