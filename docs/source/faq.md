# FAQs

## How do cloud licenses work?

Instead of using long term licenses that require static hardware we use short-term leases which give the flexibility of moving the license between different machines or containers.

These leases are stored in a `ampl.lic` file that is replaced every time the lease is renewed. Each lease lasts 5 minutes and it is automatically renewed.

In order to renew a lease, the current license file and a fingerprint are sent to one of our REST API endpoints hosted across multiple cloud providers such as AWS and Azure.

If everything is ok with the request, a new lease is returned in the response and the ampl.lic file is replaced. There is no automatic enforcement of license limits as we just log the renewal.

Even though this mechanism was designed with Docker containers in mind, it also works natively on Windows and macOS virtual and physical machines too. The only requirement is an internet connection.

### Which information is collected?

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

## How to use AMPL with Docker containers?

We do not provide a base docker image as we give the user total freedom about which base image to use.
In this example, we use the image [`python:3.9-slim-bullseye`](https://hub.docker.com/_/python) as base image. We then use `curl` and `tar` for downloading and installing some [modules](https://ampl.com/dl/modules) that you may need.

In the Dockerfile example below, we install AMPL, Gurobi, and COIN-OR solvers. We also install amplpy so that the Python API for AMPL is also ready to be used.

```Dockerfile
# Use any image as base image
FROM python:3.9-slim-bullseye
# Install curl in order to download the modules necessary
RUN apt-get update && apt-get install -y curl
# Build arguments
ARG MODULES_URL=https://ampl.com/dl/modules
# Download ampl-module.linux64.tgz
RUN cd /opt/ && curl -O ${MODULES_URL}/ampl-module.linux64.tgz && \
    tar oxzvf ampl-module.linux64.tgz && rm ampl-module.linux64.tgz
# Download gurobi-module.linux64.tgz
RUN cd /opt/ && curl -O ${MODULES_URL}/gurobi-module.linux64.tgz && \
    tar oxzvf gurobi-module.linux64.tgz && rm gurobi-module.linux64.tgz
# Download coin-module.linux64.tgz
RUN cd /opt/ && curl -O ${MODULES_URL}/coin-module.linux64.tgz && \
    tar oxzvf coin-module.linux64.tgz && rm coin-module.linux64.tgz

# Add installation directory to the environment variable PATH
ENV PATH="/opt/ampl.linux-intel64/:${PATH}"

# Install amplpy
RUN pip3 install amplpy --no-cache-dir
```

When running the container you need to set the environment variable `AMPLKEY_UUID` with the license UUID of your cloud license (or AMPL CE license), and then run `amplkey activate` before starting
any AMPL session. Alternatively, you can invoke `amplkey activate --uuid xxxxxxxx-xxxx-Mxxx-Nxxx-xxxxxxxxxxxx`.

In order to make the Docker image smaller, you may want to do a [multi-stage build](https://docs.docker.com/develop/develop-images/multistage-build/) so that you can just copy the `ampl.linux-intel64` directory from the first stage. You can do that as follows:

```Dockerfile
# Use any image as base image
FROM python:3.9-slim-bullseye
# Install curl in order to download the modules necessary
RUN apt-get update && apt-get install -y curl
# Build arguments
ARG MODULES_URL=https://ampl.com/dl/modules
# Download ampl-module.linux64.tgz
RUN cd /opt/ && curl -O ${MODULES_URL}/ampl-module.linux64.tgz && \
    tar oxzvf ampl-module.linux64.tgz && rm ampl-module.linux64.tgz
# Download gurobi-module.linux64.tgz
RUN cd /opt/ && curl -O ${MODULES_URL}/gurobi-module.linux64.tgz && \
    tar oxzvf gurobi-module.linux64.tgz && rm gurobi-module.linux64.tgz
# Download coin-module.linux64.tgz
RUN cd /opt/ && curl -O ${MODULES_URL}/coin-module.linux64.tgz && \
    tar oxzvf coin-module.linux64.tgz && rm coin-module.linux64.tgz

# Start a second stage copying just ampl.linux-intel64
FROM python:3.9-slim-bullseye
COPY --from=0 /opt/ampl.linux-intel64 /opt/ampl.linux-intel64

# Add installation directory to the environment variable PATH
ENV PATH="/opt/ampl.linux-intel64/:${PATH}"

# Install amplpy
RUN pip3 install amplpy --no-cache-dir
```

In case you want to use [non-root containers](https://docs.docker.com/engine/security/rootless/), you need to set the environment variables
`AMPLKEY_RUNTIME_DIR` with a path to a temporary location where `amplkey` temporary files should be written to, and `AMPL_LICFILE` with the location where the short-term licenses will be stored.
This is necessary if the non-root user can't write to `/opt/ampl.linux-intel64`.

```Dockerfile
# Use any image as base image
FROM python:3.9-slim-bullseye
# Install curl in order to download the modules necessary
RUN apt-get update && apt-get install -y curl
# Build arguments
ARG MODULES_URL=https://ampl.com/dl/modules
# Download ampl-module.linux64.tgz
RUN cd /opt/ && curl -O ${MODULES_URL}/ampl-module.linux64.tgz && \
    tar oxzvf ampl-module.linux64.tgz && rm ampl-module.linux64.tgz
# Download gurobi-module.linux64.tgz
RUN cd /opt/ && curl -O ${MODULES_URL}/gurobi-module.linux64.tgz && \
    tar oxzvf gurobi-module.linux64.tgz && rm gurobi-module.linux64.tgz
# Download coin-module.linux64.tgz
RUN cd /opt/ && curl -O ${MODULES_URL}/coin-module.linux64.tgz && \
    tar oxzvf coin-module.linux64.tgz && rm coin-module.linux64.tgz

# Start a second stage copying just ampl.linux-intel64
FROM python:3.9-slim-bullseye
COPY --from=0 /opt/ampl.linux-intel64 /opt/ampl.linux-intel64

# Add installation directory to the environment variable PATH
ENV PATH="/opt/ampl.linux-intel64/:${PATH}"

# Install amplpy
RUN pip3 install amplpy --no-cache-dir

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
Licensed to Trial amplkey licgen.\
Temporary license expires 20220531.\
Using license file "/tmp/ampl/ampl.lic".\
';
ampl: quit;
guest@2b5e38badc9f:/$ python
Python 3.9.12 (main, May 11 2022, 08:03:15)
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from amplpy import AMPL
>>> ampl = AMPL()
>>> ampl.eval('option version;')
option version 'AMPL Version 20220505 (Linux-5.4.0-1077-azure, 64-bit)\
Licensed to Trial amplkey licgen.\
Temporary license expires 20220531.\
Using license file "/tmp/ampl/ampl.lic".\
';
>>>
```



