# Floating license troubleshooting guide

```{note}
This page explains how to interpret the AMPL floating license manager’s informational and error messages, and how to request additional help with configuration and connection problems.

Need help with a floating license that has already been installed?\
To install a floating license for the first time, see our [Installation Guide](installation.md).\
To start and operate the floating license manager, see our [Manager Guide](manager.md).\
To set options of the floating license manager, consult our [Configuration Guide](configuration.md).
```

## Introduction

If your computer cannot successfully check out a floating license, consult the listing of common warning and error messages below. For each message, we describe the cause and give instructions for fixing the problem.

If you continue to have difficulties after following our instructions, see [How to Ask for Help](#how-to-ask-for-help) at the bottom of this page.

## Common Messages

Other detailed error listings may appear along with these messages. When writing to us about an error, be sure to include all message lines.  
 

```text
Could not connect with local license manager.
```

The requested operation cannot be performed, because the floating license manager program, `ampl_lic`, is not currently running on the computer where this message appears. See the floating license [Manager Guide](manager.md) for instructions on starting `ampl_lic`.  
 

```text
Could not connect with network license manager.
```

```text
Failed to connect with netmgr in StartMgr.
```

The client computer where this message appears is unable to make a connection to the floating license server. The most common causes of this error are are as follows:

-   The client cannot reach the server’s IP address over the network. To test this possibility, you can use a system command of the form `ping _a.b.c.d_` where a.b.c.d is replaced by the IP address given in the client’s ampl.lic file.
-   The communication port that `ampl_lic` uses on the client and/or server is not open. The chosen port can be changed by inserting a [PORT](configuration.md#port) line into the appropriate license file.
-   The floating license manager program, `ampl_lic`, is not currently running on the server. To check, run the `ampl_lic` [status](manager.md#status-netstatus) command _on the server;_ a `Could not connect` message indicates that `ampl_lic` is not running.

In rare cases, a firewall setting may be preventing communication between the client and server, and you will need to consult the firewall settings or instructions to resolve the problem.  
 

```text
License failure: ip address(es) rejected.
```

_(clients only)_ The client that is trying to check out a floating license is not on the network at one of the allowed IP addresses. To see a list of the allowed IP addresses, use the command `ampl_lic ipranges`. To add to the allowed IP address ranges, insert [IPRANGE](configuration.md#iprange-addrange) or [ADDRANGE](configuration.md#iprange-addrange) lines in the server’s ampl.netlic file, or contact [licensing@ampl.com](mailto:licensing@ampl.com) to have the updated IP addresses encoded into ampl.netlic.  
 

```text
License file ampl.lic not found anywhere in $PATH.
```

The file ampl.lic, which begins with a line of the form `MGR_IP = _ip-address_`, could not be found by AMPL; as a result, the AMPL program could not contact the server to check out a floating license. AMPL looks for ampl.lic in the same folder/directory as the AMPL program file, and also in the locations specified by the system search path. If necessary, create a new ampl.lic file that contains just the first line of the server’s ampl.netlic file.  
 

```text
MGR_IP = "ip-address" is not attached to this machine.
Starting ampl_lic, but only serving licenses to this machine.
```

_(server only)_  The IP address specified in the first line of the ampl.netlic file is not one of the server’s IP addresses. The floating licenses can be used on the server, but they cannot be checked out by client computers until the IP address discrepancy is corrected.  
 

```text
MGR_IP = "ip-address" is on this machine,
but license file = "license-file-name"
does not have a valid license for this machine.
```

_(server only)_  The ampl.netlic file listed in this message has been found, but it is not a valid license file for the server. An incorrect license file may have been installed on the server. Or the server’s license file may have become invalid, because there has been a change in the server’s hostname, MAC addresses, or (for Windows) C drive label. Contact [licensing@ampl.com](mailto:licensing@ampl.com) for help getting a valid license file.  
 

```text
No licenses available for ampl.
No licenses available for solver-name.
```

All available floating licenses for AMPL or for the indicated solver have been checked out by other users. Use the command `ampl_lic netstatus` to get a listing of users who have checked out the licenses.  
 

```text
No licenses in use on this machine.
```

On the computer where this message appears, no AMPL or solver licenses are currently checked out by any users. Floating licenses may be available, however; use the command `ampl_lic netstatus` to get a summary of current license users and status.  
 

```text
Trying to start license manager ampl_lic.
Invoking "alic_run.exe".
CreateProcess("alic_run.exe") failure!
```

_(Windows)_  When AMPL was started up, it found that the floating license manager was not running; it tried to start the floating license manager, but its attempt failed. Check that the files `ampl_lic.exe` and `alic_run.exe` were downloaded and moved to the same folder as ampl.exe. If the problem persists, see [How to Ask for Help](#how-to-ask-for-help) on this page.  
 

```text
Temporary license expired yyyymmdd.
```

The license manager `ampl_lic` is not running on the server, because the expiration date in its license file ampl.netlic has passed. Contact [licensing@ampl.com](mailto:licensing@ampl.com) for help getting a renewed license file.  
 

```text
Too much clock skew.
```

A client’s request for a floating license was refused by the server, because the time on the client differed by more than 24 hours from the time on the server. After the clocks are reset to current time, requests will again be accepted.

## How to Ask for Help

If you have consulted the above information and still have trouble getting your floating license installation to work, follow the instructions below to request further help.

**Microsoft Windows.** On the computer where the error appears, find the application sw.exe in the AMPL folder, and double-click it to bring up a command window with an `sw:` prompt in the upper left. Type each of the following 7 commands at the prompt,

```
ping a.b.c.d
ampl_lic stop
alic_run
ampl_lic status
ampl_lic netstatus
ampl_lic licshow
ampl
```

where a.b.c.d is the IP address shown in the first line of your ampl.lic or ampl.netlic file (for example, 73.73.125.205). Then send us a complete transcript of the commands and the messages that result. **_Also_** in the taskbar at the bottom of the Windows screen, look for an `alic_run` icon like this:

![alic_run icon](alic_run.png)

If you see this icon, wait about 5 minutes (to allow for any timeouts), click the icon to open the alic\_run window, and send us the messages (if any) that appear there. You can paste into your email either copies of the text from the sw.exe and `ampl_lic` windows, or screenshots of the windows. Add any other information that you think may be helpful, and then send everything to [licensing@ampl.com](mailto:licensing@ampl.com).

We will analyze this information and will respond with instructions for fixing the problem or for further troubleshooting.

**Linux** or **macOS.** On the computer where the error appears, open a Linux console window or macOS Terminal window. Use the `cd` command to set your AMPL directory or folder as current. Then type each of the following 7 commands at the command prompt in the window,

```
ping a.b.c.d
./ampl_lic stop
$(pwd)/ampl_lic
./ampl_lic status
./ampl_lic netstatus
./ampl_lic licshow
./ampl
```

where a.b.c.d is the IP address shown in the first line of your ampl.lic or ampl.netlic file (for example, 73.73.125.205). Then send us a complete transcript of the commands and the messages that result. You can paste into your email either copies of the text from the console or terminal window, or a screenshot of the window. Add any other information that you think may be helpful, and then send everything to [licensing@ampl.com](mailto:licensing@ampl.com).

We will analyze this information and will respond with instructions for fixing the problem or for further troubleshooting.