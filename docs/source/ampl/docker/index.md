(ampl_docker)=
# AMPL on Docker Containers

AMPL can be easily used on [Docker containers](https://www.docker.com/). 
On Python containers the setup is the easiest
since AMPL and all solvers are now available as [Python Packages](../python/modules.md):

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

You can build and run the container locally as follows:
```bash
$ docker build . --tag ampl-container
$ docker run --rm -it ampl-container bash
root@c240a014dd67:/# python
Python 3.9.16 (main, Jan 23 2023, 23:42:27)
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from amplpy import AMPL, modules, tools
>>> tools.activate_license("<license-uuid>")
>>> modules.load()
>>> ampl = AMPL()
>>>
```

## Docker containers for other languages

We do not provide a base docker image as we give the user total freedom about which base image to use.
In this example, we use the image [`debian:stable-slim`](https://hub.docker.com/_/debian) as base image. We then use `curl` and `tar` for downloading and installing some [modules](https://ampl.com/dl/modules) that you may need.

In the Dockefile below, we install the complete bundle with AMPL and all modules. This is the easiest approach if you are not concerned about image size or if you want to try all solvers we provide. We also install amplpy so that the Python API for AMPL is also ready to be used.

```Dockerfile
# Use any image as base image
FROM debian:stable-slim
# Install curl in order to download the modules necessary
RUN apt-get update && apt-get install -y curl

# Install full bundle (includes AMPL and all solvers)
RUN cd /opt/ && curl -OL https://ampl.com/dl/amplce/ampl.linux64.tgz && \
    tar oxzvf ampl.linux64.tgz && rm ampl.linux64.tgz

# Add installation directory to the environment variable PATH
ENV PATH="/opt/ampl.linux-intel64/:${PATH}"
```

In the Dockerfile example below, we install the modules for AMPL, Gurobi, COPT, COIN-OR solvers, and HiGHS. This is the recommended approach if image size is something is you concerned about.

```Dockerfile
# Use any image as base image
FROM debian:stable-slim
# Install curl in order to download the modules necessary
RUN apt-get update && apt-get install -y curl

# Install individual modules (alternative to installing the full bundle)
ARG MODULES_URL=https://ampl.com/dl/modules
# Download ampl-module.linux64.tgz
RUN cd /opt/ && curl -OL ${MODULES_URL}/ampl-module.linux64.tgz && \
    tar oxzvf ampl-module.linux64.tgz && rm ampl-module.linux64.tgz
# Download gurobi-module.linux64.tgz
RUN cd /opt/ && curl -OL ${MODULES_URL}/gurobi-module.linux64.tgz && \
    tar oxzvf gurobi-module.linux64.tgz && rm gurobi-module.linux64.tgz
# Download copt-module.linux64.tgz
RUN cd /opt/ && curl -OL ${MODULES_URL}/copt-module.linux64.tgz && \
    tar oxzvf copt-module.linux64.tgz && rm copt-module.linux64.tgz
# Download coin-module.linux64.tgz
RUN cd /opt/ && curl -OL ${MODULES_URL}/coin-module.linux64.tgz && \
    tar oxzvf coin-module.linux64.tgz && rm coin-module.linux64.tgz
# Download highs-module.linux64.tgz
RUN cd /opt/ && curl -OL ${MODULES_URL}/highs-module.linux64.tgz && \
    tar oxzvf highs-module.linux64.tgz && rm highs-module.linux64.tgz

# Add installation directory to the environment variable PATH
ENV PATH="/opt/ampl.linux-intel64/:${PATH}"
```

When running the container you need to set the environment variable `AMPLKEY_UUID` with the license UUID of your cloud license (or AMPL CE license), and then run `amplkey activate` before starting
any AMPL session. Alternatively, you can invoke `amplkey activate --uuid xxxxxxxx-xxxx-Mxxx-Nxxx-xxxxxxxxxxxx`.

In order to make the Docker image smaller, you may want to do a [multi-stage build](https://docs.docker.com/develop/develop-images/multistage-build/) so that you can just copy the `ampl.linux-intel64` directory from the first stage. You can do that as follows:

```Dockerfile
# Use any image as base image
FROM debian:stable-slim
# Install curl in order to download the modules necessary
RUN apt-get update && apt-get install -y curl

# Install individual modules (alternative to installing the full bundle)
ARG MODULES_URL=https://ampl.com/dl/modules
# Download ampl-module.linux64.tgz
RUN cd /opt/ && curl -OL ${MODULES_URL}/ampl-module.linux64.tgz && \
    tar oxzvf ampl-module.linux64.tgz && rm ampl-module.linux64.tgz
# Download gurobi-module.linux64.tgz
RUN cd /opt/ && curl -OL ${MODULES_URL}/gurobi-module.linux64.tgz && \
    tar oxzvf gurobi-module.linux64.tgz && rm gurobi-module.linux64.tgz
# Download copt-module.linux64.tgz
RUN cd /opt/ && curl -OL ${MODULES_URL}/copt-module.linux64.tgz && \
    tar oxzvf copt-module.linux64.tgz && rm copt-module.linux64.tgz
# Download coin-module.linux64.tgz
RUN cd /opt/ && curl -OL ${MODULES_URL}/coin-module.linux64.tgz && \
    tar oxzvf coin-module.linux64.tgz && rm coin-module.linux64.tgz
# Download highs-module.linux64.tgz
RUN cd /opt/ && curl -OL ${MODULES_URL}/highs-module.linux64.tgz && \
    tar oxzvf highs-module.linux64.tgz && rm highs-module.linux64.tgz

# Start a second stage copying just ampl.linux-intel64
FROM debian:stable-slim
COPY --from=0 /opt/ampl.linux-intel64 /opt/ampl.linux-intel64

# Add installation directory to the environment variable PATH
ENV PATH="/opt/ampl.linux-intel64/:${PATH}"
```

In case you want to use [non-root containers](https://docs.docker.com/engine/security/rootless/), you need to set the environment variables
`AMPLKEY_RUNTIME_DIR` with a path to a temporary location where `amplkey` temporary files should be written to, and `AMPL_LICFILE` with the location where the short-term licenses will be stored.
This is necessary if the non-root user can't write to `/opt/ampl.linux-intel64`.

```Dockerfile
# Use any image as base image
FROM debian:stable-slim
# Install curl in order to download the modules necessary
RUN apt-get update && apt-get install -y curl

# Install individual modules (alternative to installing the full bundle)
ARG MODULES_URL=https://ampl.com/dl/modules
# Download ampl-module.linux64.tgz
RUN cd /opt/ && curl -OL ${MODULES_URL}/ampl-module.linux64.tgz && \
    tar oxzvf ampl-module.linux64.tgz && rm ampl-module.linux64.tgz
# Download gurobi-module.linux64.tgz
RUN cd /opt/ && curl -OL ${MODULES_URL}/gurobi-module.linux64.tgz && \
    tar oxzvf gurobi-module.linux64.tgz && rm gurobi-module.linux64.tgz
# Download copt-module.linux64.tgz
RUN cd /opt/ && curl -OL ${MODULES_URL}/copt-module.linux64.tgz && \
    tar oxzvf copt-module.linux64.tgz && rm copt-module.linux64.tgz
# Download coin-module.linux64.tgz
RUN cd /opt/ && curl -OL ${MODULES_URL}/coin-module.linux64.tgz && \
    tar oxzvf coin-module.linux64.tgz && rm coin-module.linux64.tgz
# Download highs-module.linux64.tgz
RUN cd /opt/ && curl -OL ${MODULES_URL}/highs-module.linux64.tgz && \
    tar oxzvf highs-module.linux64.tgz && rm highs-module.linux64.tgz

# Start a second stage copying just ampl.linux-intel64
FROM python:3.9-slim-bullseye
COPY --from=0 /opt/ampl.linux-intel64 /opt/ampl.linux-intel64

# Add installation directory to the environment variable PATH
ENV PATH="/opt/ampl.linux-intel64/:${PATH}"

# Add non-root user (optional)
ARG USERNAME=guest
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME
# Change to non-root privilege
USER ${USERNAME}

# Environment variables for amplkey (necessary if the non-root user can't write to /opt/ampl.linux-intel64)
ENV AMPLKEY_RUNTIME_DIR /tmp/ampl/
ENV AMPL_LICFILE /tmp/ampl/ampl.lic
```

You can build this image with `docker build . --tag ampl-container` and you can run it as follows:

```bash
$ docker run --rm -it -e AMPLKEY_UUID=xxxxxxxx-xxxx-Mxxx-Nxxx-xxxxxxxxxxxx ampl-container bash
guest@2b5e38badc9f:/$ amplkey activate
2022/05/12 14:42:08 Wrote 958 bytes to /tmp/ampl/ampl.lic
guest@2b5e38badc9f:/$ ampl
ampl: option version;
option version 'AMPL Version 20220505 (Linux-5.4.0-1077-azure, 64-bit)\
Licensed to AMPL Community Edition License.\
Temporary license expires 20220531.\
Using license file "/tmp/ampl/ampl.lic".\
';
ampl: quit;
```