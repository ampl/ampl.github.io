# Floating license manager guide

```{note}
This page explains how to run the floating license manager `ampl_lic` and related programs, to start serving floating licenses and to manage their use.

Need help with a floating license that has already been installed?\
To install a floating license for the first time, see our [Installation Guide](installation.md).\
To set options of the floating license manager, consult our [Configuration Guide](configuration.md).\
To interpret and fix error conditions, consult our [Troubleshooting Guide](troubleshooting.md).
```

## Introduction

AMPL’s floating license mechanism is implemented by `ampl_lic`, a program that functions as a license manager for both servers and clients. This page is guide to using the `ampl_lic` command to start and stop the license manager and to monitor the status of floating licenses. The general form of the command is

```
ampl_lic keyword [arguments]
```

The presentation on this page is organized according to the possible values of _keyword_, as follows:

- [start](#start): start the license manager process and keep it running
- [stop](#stop): stop the license manager process
- [restart](#restart): stop and then start the license manager process
- [checkout](#checkout-return) (and return): manually check out and return licenses for offline use
- [status](#status-netstatus) (and netstatus): query the state of the license manager and the licenses in use
- [licshow](#licshow-ipranges) (and ipranges): view the license file in use, and its IP address restrictions

These keywords can be used with `ampl_lic` either on the computer designated as the license server, or on a client computer, except for a few cases indicated in our descriptions.

## start

To make floating licenses available, the AMPL floating license manager, `ampl_lic`, needs to be started on the computer that acts as a license server. The same `ampl_lic` program must also be started on each client computer where a floating license will be used. Once started on any particular computer, `ampl_lic` will continue to run until it is terminated, usually by a logout or shutdown. Thus it normally only needs to be started when the computer is restarted or a new user logs in.

This section gives instructions for starting the floating license manager by explicitly invoking the `ampl_lic` program. Notes on starting the license manager automatically on startup or login are also provided, with instructions for getting more information. Separate instructions are provided for Windows, Linux, and macOS.

_Starting AMPL or a licensed solver should also cause the license manager to be started if it is not already running._ In that case an explicit invocation of `ampl_lic` is not needed.

**_Windows._** For security reasons, the floating license manager must be invoked with a full pathname:

```
full-pathname\ampl_lic [start]
```

For example in a Windows command-prompt window you might type `C:\Users\Smith\Desktop\AMPL\ampl_lic`. (The `start` keyword is optional.)

The command window in which `ampl_lic` is started must remain open to keep `ampl_lic` running. As an alternative, to avoid keeping a command window active, you can invoke the auxiliary program `alic_run` by typing it in a command window (and then closing the window) or double-clicking the `alic_run.exe` icon. An icon labeled `alic_run`: running `ampl_lic` will then appear in the taskbar at the bottom of the Windows screen; you can click on it to bring up a message window that may contain some diagnostic information.

We also offer an `ampl_lic_service` that invokes `ampl_lic.exe` when Windows is started up, so that the `ampl_lic` program will be run by the LocalService account rather than by any logged-in user. This can be desirable when the machine hosting the AMPL floating license server is centrally managed. Contact licensing@ampl.com for installation details.

**_Linux._** For security reasons, the floating license manager must be invoked with a full pathname:

```
full-pathname/ampl_lic [start]
```

For example in a Linux command window you might type `/home/Smith/AMPL/ampl_lic`. (The `start` argument is optional.) If the `ampl_lic` program is in the current directory, then you can use the shorter form

```
$(pwd)/ampl_lic
```

(An equivalent form `` `pwd`/ampl_lic `` is required by some Linux shells.) After the startup is completed, control returns to the command window and `ampl_lic` continues running in the background.

To automate the process of starting the license manager, `ampl_lic` can be started by a simple shell script in one of the directories of scripts that get run when the system boots. Details depend on specifics of the Linux installation; contact licensing@ampl.com for assistance.

**_macOS._** For security reasons, the floating license manager must be invoked with a full pathname:

```
full-pathname/ampl_lic [start]
```

For example in a macOS Terminal window you might type `/Users/smith/Desktop/AMPL/ampl_lic`. (The `start` argument is optional.) If the current directory contains the `ampl_lic` program, then you can use the shorter form

```
$(pwd)/ampl_lic
```

After the startup is completed, control returns to the command window and `ampl_lic` continues running in the background.

The process of starting the license manager can be automated by placing an appropriate startup file in the folder /Library/LaunchDaemons. Contact licensing@ampl.com to request detailed instructions for this option.

## stop

When a floating license server or client is logged out or shut down, the `ampl_lic` process normally catches an appropriate shutdown signal and udpates current license information to a state file before terminating. The process can also be stopped manually with the command

```
ampl_lic stop
```

If `ampl_lic` is manually stopped on a client computer, licensed programs continue to run. When `ampl_lic` is subsequently restarted, it reads its saved state file, checks for licensed processes that are still running, and updates its state accordingly. It then checks in with the license manager on the server, which returns (among other things) a checksum of what it thinks is the local manager’s state. The client license manager then corrects the server’s view if necessary.

## restart

After any change to an AMPL floating license file (ampl.netlic or ampl.lic), the license manager must be restarted on the computer where the change has been made. This can be conveniently done by issuing the command

```
ampl_lic restart
```

which has an effect similar to stopping and then starting `ampl_lic`, except that the port does not have to be rebound (which can take several minutes on some systems).

## checkout, return

Normally floating licenses are automatically checked out when a licensed programs starts, and are automatically returned after termination of a licensed program. There is an option to check out a license manually, however, in which case it remains on the client computer until it is manually returned. This can be useful when the client computer will be temporarily moved to a location where it does not have access to the license server, such as for a demo at a customer site.

Floating licenses are manually checked out by a command of the form

```
ampl_lic checkout program [count] [program [count]] ...
```

where _program_ is the name of a licensed program and optionally _count_ is the number of floating licenses to be checked out. In the most common situation, only one license of AMPL and of some solvers needs to be checked out, and _count_ can be omitted. For example, you might specify `ampl_lic checkout ampl minos knitro` to check out one license each for AMPL and the MINOS and Knitro solvers.

A similar command requests that checked-out licenses be returned:

```
ampl_lic return program [count] [program [count]] ...
```

Licenses are not actually returned until all processes using them have ended. An `ampl_lic return` statement may specify only some of the licenses that have been manually checked out, in which case the remaining licenses remain with the client until returned by a subsequent `ampl_lic return` statement.

## status, netstatus

A summary of all floating licenses in use can be requested with the command

```
ampl_lic netstatus
```

issued on the server or on any client. This command communicates directly with the server, and hence can be used on a client even where the `ampl_lic` program is not currently running.

Any computer can request a summary of its local floating license activity with the command

```
ampl_lic status
```

If an `ampl_lic` process is running, this command first tries to return any licenses held as specified by the current [LIC\_HOLD](https://old.ampl.com/resources/floating-licenses/configuration/#lic_hold) setting. It then displays a report of the licensed processes currently running on the computer and of licenses that the computer is holding for other reasons, such as previous use of `ampl_lic checkout` or failure to communicate with the server to return licenses.

If there is no `ampl_lic` process running, `ampl_lic status` displays an error message. Thus, invoking `ampl_lic status` is a way to check whether the local license manager is running.

The local (client) license manager may hold licenses because it cannot communicate with the network (server) license manager to return them, perhaps because the network license manager has been stopped or because the network has gone down. In this case, the local manager tries periodically to reestablish contact with the network license manager. The period between tries starts at 15 seconds and increases by 15 second increments up to 15 minutes. If you know that the network manager has just become available again, invoking `ampl_lic status` will cause the local manager to return licenses immediately.

If you kill a licensed process or the process faults, the network license manager may still think the process is running. Invoking `ampl_lic status`will cause the manager to check which processes are still running and to return any licenses that are no longer in use.

## licshow, ipranges

If `ampl_lic` is running locally, the output from

```
ampl_lic licshow
```

reports the full pathname by which `ampl_lic` was invoked and the full pathname and contents of the ampl.netlic or ampl.lic file that it read.

The ampl.netlic file on the server may be configured to accept checkout requests only from certain IP addresses. A list of allowable IP addresses and/or address ranges can be included in the license file when it is generated, and may also be modified by the user through [IPRANGE](https://old.ampl.com/resources/floating-licenses/configuration/#iprange) and [ADDRANGE](https://old.ampl.com/resources/floating-licenses/configuration/#iprange) settings. The current list of valid IP addresses can be seen by invoking

```
ampl_lic ipranges
```

on the server or any client.