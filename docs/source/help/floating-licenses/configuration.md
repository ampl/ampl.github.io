# Floating license configuration guide

```{note}
This page explains how to change the default configuration of the AMPL floating license manager, to handle various special situations.

Need help with a floating license that has already been installed?\
To install a floating license for the first time, see our [Installation Guide](installation.md).\
To start and operate the floating license manager, see our [Manager Guide](manager.md).\
To interpret and fix error conditions, consult our [Troubleshooting Guide](troubleshooting.md).
```

## Introduction

You can configure various options of the AMPL floating license manager as needed for your particular installation. Options are specified by editing the license files `ampl.netlic` and `ampl.lic`, using a plain-text editor to insure that no nonprinting special characters are added.

All `ampl.netlic` and `ampl.lic` files begin with a “MGR\_IP line” of the form

```text
MGR_IP = ip-address
```

where ip-address is the IP address of the license server. Usually this is an IPv4 address such as `70.38.71.71`, though it may also be an IPv6 address (like `2001:0db8:85a3:0000:0000:8a2e:0370:7334`), or a quoted symbolic name (like `"server.ampl.com"`) that resolves to an IP address.

Options are specified by adding one or more “option lines” immediate after the MGR\_IP line of `ampl.netlic` (for servers only) or `ampl.lic`. The formats of the option lines are described in the following sections below:

-   [HEARTBEAT](#heartbeat): set timing for the server to check that clients are active
-   [IGNORE\_CLIENT\_FP](#ignore_client_fp): for floating per-machine licenses, distinguish clients only by hostname
-   [IPRANGE](#iprange-addrange) (and ADDRANGE): list valid IP addresses
-   [LIC\_HOLD](#lic_hold): delay return of licenses
-   [LOGFILE](#logfile-logwait-verbose) (and LOGWAIT, VERBOSE): log floating license status to a file
-   [PORT](#port): choose a port for license manager communications
-   [PROC\_CHK](#proc_chk): set timing for a client to check that licensed software is still running
-   [SAVE\_WAIT](#save_wait): interval between saves of the state file
-   [STATEFILE](#statefile): choose the name and location of state and lock files

## HEARTBEAT

When a floating license client is a node in a computational cluster, or is a virtual machine created by a cloud service, the client may be shut down before the floating license can be returned. To prevent licenses from being “lost” in these situations, you can specify

```text
HEARTBEAT = nnn
```

in the `ampl.netlic` file for the network license server, where nnn is a positive integer (such as 10 or 60). The license server will then expect to receive a communication every nnn seconds from clients that have currently checked out floating licenses. When the server does not hear from a client within a few seconds of the expected time, the server will assume the client has been shut down, and any licenses that were held by the client will be made available again.

A client may exclude itself from this heartbeat mechanism by specifying `HEARTBEAT = 0` in its `ampl.lic` file. This option can be used by clients that are not cluster or cloud machines, to avoid unnecessary communication.

The `ampl_lic` program on both server and clients must be version 20181120 or later for this heartbeat mechanism to work. (The command `ampl_lic -v` displays the `ampl_lic` version.)

## IGNORE\_CLIENT\_FP

When floating per-machine licenses are provided (usually for academic use), each floating license is checked out by a computer rather than by a particular user. Since there may be more than one client computer than has the same name, `ampl_lic` distinguishes clients by their _fingerprints_ which include hostname, MAC address, and (for Windows only) C drive label.

In rare cases, a client can disconnect from the network and then (without shutting down) reconnect with a new MAC addresses. Then the license server by default will regard the client as a different computer and will not release licenses that the client may have been holding under its old fingerprint. If this situation cannot be avoided, it may be addressed by adding the option line

```text
IGNORE_CLIENT_FP = 1
```

to the license server’s ampl.netlic file. When this option is specified, client computers are distinguished only by their hostnames, and it is your responsibility to assure that the hostnames of all clients are distinct.

## IPRANGE, ADDRANGE

A list of valid IP address ranges is encoded into your `ampl.netlic` file. You can replace these builtin ranges by inserting a line of the form

```text
IPRANGE = range_pat [ range_pat ... ]
```

and can augment the ranges by adding lines of the form

```text
ADDRANGE = range_pat [ range_pat ... ]
```

to the ampl.netlic file (following the IPRANGE line, if given). For conventional IPv4 addresses, each range\_pat has the form

```text
range_list1.range_list2.range_list3.range_list4
```

— that is, four range\_lists separated by periods, in which each range\_list is a comma-separated list of single decimal integers d with 0 <= d <= 255, and individual ranges of the form m-n, where m and n are decimal integers with 0 <= m <= n <= 255. If m = 0, m can be omitted, and if n = 255, n can be omitted. The last range may be followed by a `/mask` notation in which mask is a decimal integer specifying the number of initial bits in a range that are fixed; all the remaining bits can vary. For example,

```text
192.168.1.0-255
192.168.1.-255
192.168.1.0-
192.168.1.-
192.168.1.0/24
```

all specify the same IP address range. No spaces may appear in a range\_pat, but range\_pats are separated by one or more spaces. Each range\_pat specifies a range that includes all IP address w.x.y.z with w in range\_list1, x in range\_list2, y in range\_list3, and z in range\_list4.

For IPv6 addresses, each range\_pat involves up to 8 range\_lists of up to four hexadecimal digits, with range\_lists separated by colons rather than periods. When two or more ranges would just be 0, they may be replaced by a pair of colons. At most one such pair may appear, and if none appears, there must be 8 range\_lists. For example,

```text
fdd8:ed91:f4fe:c1a4:0-ffff:0-ffff:0-ffff:0-ffff
fdd8:ed91:f4fe:c1a4:-:-:-:-
fdd8:ed91:f4fe:c1a4::/64
```

all have the same meaning.

## LIC\_HOLD

To reduce network traffic when AMPL or solvers are invoked frequently, a client can be configured to briefly retain floating licenses before they are returned to the server. An option line of the form

```text
LIC_HOLD = nnn
```

(where nnn is an integer) causes a delay of nnn seconds before the license is returned. Hence the license is immediately available if needed again within nnn seconds. The default nnn is 0: no such delay.

## LOGFILE, LOGWAIT, VERBOSE

Adding an option line of the form

```text
LOGFILE = logfilename
```

or

```text
LOGFILE = "logfilename"
```

to ampl.lic will cause `ampl_lic` to write some lines to the indicated file. The special setting `LOGFILE = -` causes logging to the standard output, or to the alic\_run window when the alic\_run application is used under Windows.

In `ampl_lic` versions dated 20190910 and later, flushing of the log file’s buffer can be regulated by adding an option line of the form

```text
LOGWAIT = n
```

When n is at its default setting of 0, the log file buffer is flushed immediately, so that the log is up to date whenever it is viewed. When n is 1, or in earlier `ampl_lic` versions, the log file buffer is only flushed when the state file is written, or when `ampl_lic status` is invoked.

By default, only start-up, disaster, and shut-down messages will appear in the log file. The starting and stopping of licensed processes and changes of license state can also be recorded in the log file, by adding an option line of the form

```text
VERBOSE = nnn
```

with nnn being the sum of 1 to log local processes, 2 to log network (remote) licenses, 4 to include user IDs in log entries for new processes, and 8 to augment user IDs with user names (on non-Windows systems).

## PORT

The floating license mechanism uses a dedicated TCP port, which by default is port 5195, but which can be specified by an option line of the form

```text
PORT = nnnn
```

where nnnn is an integer. You may need to adjust your firewall settings to permit use of the specified TCP port.

## PROC\_CHK

When a license is in use, the local `ampl_lic` process checks periodically whether the programs that requested the license are still running. By default this happens every 10 minutes, but you can specify a different interval by adding to `ampl.lic` a line of the form

```text
PROC_CHK = nnn
```

where nnn is the number of seconds to wait before checking again. Values of nnn less than 20 are treated as 20.

## SAVE\_WAIT

Each `ampl_lic` process (on the server or on a client) periodically updates a “state” file that records the status of licenses in use. By default the state file is updated every 5 minutes, but you can specify a different interval by adding to `ampl.netlic` or `ampl.lic` a line of the form

```text
SAVE_WAIT = nnn
```

where nnn is the number of seconds between updates. The value of nnn must be at least 5 and at most 600.

## STATEFILE

Each `ampl_lic` process (on the server or on a client) periodically updates a “state” file, and always updates it (or removes it if it would be empty) when shutting down. By default, the state file appears in the same directory as the license file and has a name formed by the machine’s hostname followed by `.ampl_state` (for example, scherzo.ampl\_state). An alternative state file can be specified by an option line of the form

```text
STATEFILE = "statefileloc"
```

in `ampl.netlic` (server) or `ampl.lic` (client). If statefileloc is a filename (such as `/home/4er/ampl/state1`) then that file will be used as the state file. If statefileloc is a directory or folder name (such as `/home/4er/ampl/`) then the statefile will be written to that directory with the default name described above.

The `ampl_lic` process also writes a “lock” file in the directory of the state file, with a standard name formed by the machine’s hostname followed by `.ampl_lock` (for example, scherzo.ampl\_lock).

The location of the lock and state files must of course be writable by `ampl_lic`. The directory where these files appear need not be on the system search path, and it can be on a cross-mounted file system such that all clients use the same directory — provided the clients have distinct hostnames.