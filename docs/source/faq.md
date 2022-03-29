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
