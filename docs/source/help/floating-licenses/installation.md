# Floating License Installation Guide

```{note}
This page introduces AMPL floating licenses and gives instructions for initial installation.

Need help with a floating license that has already been installed?\
To start and operate the floating license manager, see our [Manager Guide](manager.md).\
To set options of the floating license manager, consult our [Configuration Guide](configuration.md).\
To interpret and fix error conditions, consult our [Troubleshooting Guide](troubleshooting.md).

```

## Introduction

_Floating licenses_ let you run an application on any computer, subject to a limit on the number of application sessions that can be active at the same time. You can purchase one or more floating licenses for AMPL and also for any of the solvers that we sell; the number of purchased floating licenses determines the number of simultaneous sessions allowed. Optionally you make your floating licenses available only to computers at specified network addresses.

To install floating licenses, you must choose one computer to be your AMPL _floating license server._ The server will need to be running and connected to the network whenever the floating licenses are being used. Additionally, the following machine characteristics of the server must be static (not changing):

- at least one IP address
- at least one MAC address
- the hostname
- the C drive label (Windows only)

The other computers that use the floating licenses are called _clients._ Each client computer must have a network connection to the server, but a client computer does _not_ need to have a static IP address or other static machine characteristics.

One _application session_ for a floating license can be defined in any of several ways. The following configurations are available on our price lists:

- one user on one computer, running any number of simultaneous processes; for commercial licenses for AMPL and for the BARON, CONOPT, LGO, LOQO, MINOS, and SNOPT solvers
- one user on one computer, running one process; for commercial licenses for CPLEX, Gurobi, Knitro, and Xpress.
- any number of users on one computer, each running any number of simultaneous processes; for academic licenses

Other configurations may be available; contact our [sales team](mailto:sales@ampl.com) for details.

The following sections give basic download and installation instructions for servers and clients under [Microsoft Windows](installation.md#windows-installation), [Linux](installation.md#linux-installation), and [macOS](installation.md#macos-installation). We recommend first creating a basic installation on your chosen server, and then creating and testing your client installations. If you encounter error conditions or special situations, consult our additional documentation:

- The [Floating License Manager Guide](manager.md) explains the use of the program `ampl_lic` to manage client-server communication and to monitor the status of floating licenses.
- The [Floating License Configuration Guide](configuration.md) explains additional settings that can be added to floating license files, for example to change the communication port or state-file location.
- The [Floating License Troubleshooting Guide](troubleshooting.md) gives instructions for interpreting common error messages and requesting technical support.

Client computers do not need to run the same operating system as the server. When installing a client, follow the download and installation instructions for the client’s operating system.

## Windows Installation

**_Download files._** On the computer that you have chosen as your AMPL license server, create a new Windows folder to hold your AMPL files; we will refer to this as your _AMPL folder._ Then go to the [AMPL software download site](https://portal.ampl.com) and log in to your personalized download page by following the instructions that we have previously emailed to you. (If you have not logged in before or forgot your password, click on Login and then click on the password reset link.) Download the needed files as follows:

-   Click on `My Licenses` and then click on the ID number of your floating license. Scroll down to the box marked `Download ampl.netlic` where you will see a link ending in .netlic; click this link to download your server license file. _Rename this file_ to ampl.netlic and move it into your AMPL folder.
-   Create a client license file: Make a copy of the ampl.netlic file in your AMPL folder, rename the copy to ampl.lic, and then edit the ampl.lic file to delete all but the first line.
-   Click on `My Downloads` scroll down to the `ampl_lic` link next to `mswin`, and click the link to download a zipfile of all the AMPL floating license manager files. Double-click the zipfile icon, or apply an unzip utility, to extract the contents of the zipfile, and move all of the contained files into your AMPL folder.
-   Go to [Download AMPL](https://ampl.com/download/ampl). Under "2. Download individual AMPL solver module" click on Windows and then on "Download AMPL module for Windows" download a zipfile of all the AMPL program files. Double-click the zipfile icon, or apply an unzip utility, to extract the contents of the zipfile, and move all of the contained files into your AMPL folder.
-   If you will be using this computer to run solvers provided as part of your AMPL setup, use the solver links on the same page to download solver zipfiles. Again, unzip them and move the contents into your AMPL folder.

**_Set up the server._** In your AMPL folder, find the file sw.exe (or sw if filename extensions have been turned off). Double-click this file to bring up a command window with an `sw:` prompt in the upper left. Type each of the following 4 commands at the prompt:

```
alic_run
ampl_lic status
ampl_lic netstatus
ampl
```

These commands will start the program `ampl_lic`, which manages the floating licenses; will display some floating license status information; and will start the AMPL program. At the end, the contents of your window should look something like this:

```
sw: alic_run
sw: ampl_lic status
20181114 15:38:27: No licenses in use on this machine.
sw: ampl_lic netstatus
20181114 15:38:33:  No licenses in use.
Available licenses:
ampl    3 machines
cplex   2 machines
gurobi  2 machines
knitro  1 machine
sw: ampl
ampl:
```

The `ampl:` prompt indicates that AMPL has successfully started up and checked out a floating license. If the `Available licenses` message shows that you have floating licenses for solvers, download a sample [model](steelT.mod) and [data](steelT.dat) file into your AMPL folder, and give AMPL commands as follows to check that each solver runs and reports an optimal solution:

```
ampl: reset;
ampl: model steelT.mod;
ampl: data steelT.dat;
ampl: option solver minos;
ampl: solve;
MINOS 5.51: optimal solution found.
15 iterations, objective 515033
ampl:
```

Enter `quit` to end the AMPL session and return its license.

After the above steps are completed, the floating license manager `ampl_lic` will be running as a background process on your computer. This program will handle all requests to check out and to return floating licenses, and thus it _must be running whenever you want the licenses to be available to users._ If `ampl_lic` is stopped — such as by a restart of the computer — its state will be saved, and you can start it up again by repeating the above instructions.

_If you see error messages instead of the messages shown above,_ consult our [Troubleshooting Guide](troubleshooting.md) which provides advice on fixing common errors and requesting further help.

If you have special requirements for your installation, such as a particular communication port or folder for temporary files, see our [Configuration Guide](configuration.md) for instructions. If you need to automatically start `ampl_lic` when the server starts up, consult our `ampl_lic` [start](manager.md#start) instructions.

**_Set up a client._** Setting up a floating license client to run under Microsoft Windows is almost the same as setting up a floating license server under Windows:

-   Follow the download instructions for the server as given above;  
    _or,_ if you have set up your server under Windows, copy your entire server AMPL folder to the client.
-   Keep the ampl.lic file for use by the client,  
    but _delete the ampl.netlic file_ which is only needed for the server.

Then follow the instructions given above for the server, to run the floating license manager, AMPL, and solvers, and to confirm that they are operating properly. Because you are running on a remote client, requests to check out AMPL and solver licenses will be handled through communications between the `ampl_lic` program on the client and the `ampl_lic` program that you previously started on the server.

Once you have confirmed that AMPL is successfully checking out floating licenses on a client, you can use AMPL on the client just like on any other computer. When you start AMPL, it will automatically start up `ampl_lic` (if necessary) and check out a license.

## Linux Installation

**_Download files._** On the computer that you have chosen as your AMPL license server, create a new Linux directory to hold your AMPL files; we will refer to this as your _AMPL directory._ Then go to the [AMPL software download site](https://portal.ampl.com) and log in to your personalized download page by following the instructions that we have previously emailed to you. (If you have not logged in before or forgot your password, please click on Login and then click on the password reset link.) Download the needed files as follows:

-   Click on `My Licenses` and then click on the ID number of your floating license. Scroll down to the box marked `Download ampl.netlic` where you will see a link ending in `.netlic`; click this link to download your server license file. _Rename this file_ to ampl.netlic and move it into your AMPL directory.
-   Create a client license file: Make a copy of the ampl.netlic file in your AMPL folder, rename the copy to ampl.lic, and then edit the ampl.lic file to delete all but the first line.
-   Click on `My Downloads` scroll down to the `ampl_lic` link next to `linux-intel64`, and click the link to download a compressed archive of all the AMPL floating license manager files. Unpack the archive with a command of the form  
       `gzip -dc ???.tgz | tar xf -`  
    where ??? is replaced by the name of the archive file you downloaded; the name will begin with `ampl_lic`.linux-intel64. and end with an 8-digit date identifier. Move all of the unpacked files into your AMPL directory.
-   Go to [Download AMPL](https://ampl.com/download/ampl). Under "2. Download individual AMPL solver module" click on Linux and then on "Download AMPL module for Linux" download a compressed archive of all the AMPL program files. Unpack the archive as in the previous step, and move all of the unpacked files into your AMPL directory.
-   If you will be using this computer to run solvers provided as part of your AMPL setup, use the solver links on the same page to download solver archives. Again, extract them and move the contents into your AMPL directory.

**_Set up the server._** Go to your AMPL directory and test your installation as follows:

(1) Use the `cd` command to set the current directory to be your AMPL directory.

(2) Execute the command

```
$(pwd)/ampl_lic
```

to start the `ampl_lic` program, which manages the floating licenses. (An equivalent form `` `pwd`/ampl_lic `` is required by some Unix shells.)

(3) Enter each of the following three commands:

```
./ampl_lic status
./ampl_lic netstatus
./ampl
```

These commands will display some floating license status information, and will then start the AMPL program. At the end, the contents of your window should look something like this:

```
4er@atest:~$ cd /usr/local/bin/ampl
4er@atest:~/ampl$ $(pwd)/ampl_lic
4er@atest:~/ampl$ ampl_lic status
20181220 15:52:30: No licenses in use on this machine.
4er@atest:~/ampl$ ampl_lic netstatus
20181220 15:53:22: No licenses in use.
Available licenses:
        ampl    1 machine
        cplex   1 machine
        gurobi  1 machine
4er@atest:~/ampl$ ./ampl
ampl:
```

The `ampl:` prompt indicates that AMPL has successfully started up and checked out a floating license. If you have installed solvers, download a sample [model](steelT.mod) and [data](steelT.dat) file into your AMPL folder, and give AMPL commands as follows to check that each solver runs and reports an optimal solution:

```
ampl: reset;
ampl: model steelT.mod;
ampl: data steelT.dat;
ampl: option solver minos;
ampl: solve;
MINOS 5.51: optimal solution found.
15 iterations, objective 515033
ampl:
```

Enter `quit` to end the AMPL session and return its license.

After the above steps are completed, the floating license manager `ampl_lic` will be running as a background process on your computer. This program will handle all requests to check out and to return floating licenses, and thus it _must be running whenever you want the licenses to be available to users._ If `ampl_lic` is stopped — such as by a restart of the computer — its state will be saved, and you can start it up again by repeating the above instructions.

_If you see error messages instead of the messages shown above,_ consult our [Troubleshooting Guide](troubleshooting.md) which provides advice on fixing common errors and requesting further help.

If you have special requirements for your installation, such as a particular communication port or folder for temporary files, see our [Configuration Guide](configuration.md) for instructions. If you need to automatically start `ampl_lic` when the server starts up, consult our `ampl_lic` [start](manager.md#start) instructions.

**_Set up a client._** Setting up a floating license client to run under Linux is almost the same as setting up a floating license server under Linux. To get the needed files, you can proceed in either of the following ways:

-   Follow the download instructions for the server as given above;  
    _or,_ if you have set up your server under Linux, copy your entire server AMPL folder to the client.
-   Keep the ampl.lic file for use by the client,  
    but _delete the ampl.netlic file_ which is only needed for the server.

Then follow the instructions given above for the server, to run the floating license manager, AMPL, and solvers, and to confirm that they are operating properly. Because you are running on a remote client, requests to check out AMPL and solver licenses will be handled through communications between the `ampl_lic` program on the client and the `ampl_lic` program that you previously started on the server.

Once you have confirmed that AMPL is successfully checking out floating licenses on a client, you can use AMPL on the client just like on any other computer. When you start AMPL, it will automatically start up `ampl_lic` (if necessary) and check out a license.

## macOS Installation

Floating licenses are installed through the macOS Darwin operating system, which is similar to Linux. Thus, the instructions are much the same as given for Linux above. Contact [licensing@ampl.com](mailto:licensing@ampl.com) for additional assistance.