# Fingerprint instructions for static licenses

Some AMPL licenses require a license file that is tied to a particular computer. Before we can generate this license file, we need you to run our "fingerprint" program on your computer that will host AMPL, and to send us the resulting output.

**To download and run the fingerprint program,** follow the instructions below that correspond to your operating system:

- [Microsoft Windows](get-fingerprint.md#microsoft-windows)
- [Linux](get-fingerprint.md#linux)
- [macOS](get-fingerprint.md#macos)

For more information about this process, see also our fingerprint [frequently asked questions](get-fingerprint.md#faq).

## Microsoft Windows

Download the distribution zipfile, [fingerprint.mswin.zip](https://portal.ampl.com/dl/fp/fingerprint.mswin.zip). Double-click the zipfile icon, or apply an unzip utility, to extract the file `fingerprint.exe` from the zipfile.

Next double-click the `fingerprint.exe` icon. A window will appear stating that “Your system’s fingerprint has been copied to the Clipboard.” Click the “OK” button in this window to close it.

Now return to your trial license form, and use your computer’s paste function to paste the fingerprint into the indicated field on the form. Complete the form and click the Submit button at the bottom; we will reply by email with a license file and instructions for downloading the AMPL and solver software.

**Troubleshooting tip:** If the fingerprint program is provisionally blocked by your version of Windows or by your antivirus software, follow the on-screen instructions to allow the program to run.

## Linux

Download the distribution archive, [fingerprint.linux-intel64.tgz](https://portal.ampl.com/dl/fp/fingerprint.linux-intel64.tgz). Then extract the contents of this archive by typing the command

```bash
$ tar xzf fingerprint.linux-intel32.tgz
```

or

```bash
$ tar xzf fingerprint.linux-intel64.tgz
```

When the extraction is complete you will have an executable file named `fingerprint`. Next invoke the following command in the directory that contains the `fingerprint` file:

```
$ ./fingerprint -s
```

Several lines of letters and numbers will appear in your window, each except the last being 72 characters. These are the “fingerprint” of your computer. Copy all of these lines from your screen.

Finally, return to your trial license form, and paste the copied fingerprint into the indicated field on the form. Complete the form and click the Submit button at the bottom; we will reply by email with a license file and instructions for downloading the AMPL and solver software.

## macOS

Download the distribution archive, [fingerprint.macosx.tgz](https://portal.ampl.com/dl/fp/fingerprint.macosx.tgz). Double-click this file’s icon to extract its contents. When the extraction is complete, you will see an icon named `fingerprint`.

Double-click the `fingerprint` icon. A window will appear stating that, “Your system’s fingerprint has been copied to the Clipboard”. Click the “OK” button in this window to close it.

Now return to your trial license form, and use your computer’s paste function to paste the fingerprint into the indicated field on the form. Complete the form and click the Submit button at the bottom; we will reply by email with a license file and instructions for downloading the AMPL and solver software.

**Troubleshooting tip:** If the fingerprint program is provisionally blocked by your version of MacOSX, then proceed as follows: While holding down the Ctrl key, click on the fingerprint file icon; a small contextual menu will pop up. Select Open in that menu, and you will see a dialog box that asks, “Are you sure you want to open it?” Then click Open again in that dialog box, to run the fingerprint program.

## FAQ

**If I paste the AMPL fingerprint correctly, what will it look like?** An AMPL fingerprint is a long string of characters (mostly letters and numbers), broken into 72-character chunks. Here is a typical example:

```
IyB1c2VyICJSb2JlcnQiCkZpbmdlcnByaW50KDIwMTQwNTIzKSA9IDEtMi0xLTYxM2ZhMWUK
NGVyWW9nYTEzCjAwLTUwLUI2LTBELUEwLTkxCjIwLTE2LUQ4LUE2LUJGLTNCCjM0OEEtRUIz
NQoKIyAyIHNvY2tldHMuCgo=
```

Your computer’s fingerprint will be at least 2 lines, but many are 3 lines or longer.

**What information about my computer is contained in the fingerprint?** The fingerprint records the following items of information:

- Your computer’s name (or hostid) as recorded by your operating system.
- The Ethernet address or addresses (also known as MAC addresses) of your computer.
- For Windows computers only, the 8-character label of your computer’s C: drive.

Additionally the fingerprint includes the name of the user who ran the fingerprint program, and the number of processor sockets detected, but that information is not used for trial licenses.

**How does AMPL use the fingerprint?** The information in the fingerprint is incorporated into your AMPL license file and is checked when AMPL or a solver is run. The check is successful if the computer has the same name, at least one of the same Ethernet addresses, and (for Windows) the same C: drive label. If the check fails then the AMPL license management software displays a detailed error message which you can send to [licensing@ampl.com](mailto:licensing@ampl.com) for help.

**How can I see the information that is in the fingerprint?** The fingerprint is a base64 encoding of a small text file. You can paste the fingerprint string into a [base64 decoder](https://www.base64decode.org/) to see the actual text. For example, the fingerprint shown above decodes to the following:

```
# user "Robert"
Fingerprint(20140523) = 1-2-1-613fa1e
4erYoga13
00-50-B6-0D-A0-91
20-16-D8-A6-BF-3B
348A-EB35
# 2 sockets.
```

Lines beginning with # are ignored for trial license generation. Of the others, the first line is a header that provides information to the license file generator. The computer name appears on the second line, and the C: drive label appears (for Windows only) on the last line; the other lines give the MAC addresses.

**Can I send the required information without using the fingerprint program?** No, the fingerprint also includes a checksum (at the end of the header line) that is required by the AMPL license generator. The only way to get this checksum is to run the fingerprint program.

**Are fingerprints required for other kinds of AMPL installations?** License files generated from fingerprints are used by [trial versions](https://ampl.com/start-free-now/) and [purchased versions](https://ampl.com/licenses-and-pricing/) of AMPL. However fingerprints are not required for the size-limited [demo versions](https://portal.ampl.com/user/ampl/download/demo) or for the full-featured AMPL and solver versions distributed through the [AMPL for Courses](https://ampl.com/licenses-and-pricing/ampl-for-teaching/) program.