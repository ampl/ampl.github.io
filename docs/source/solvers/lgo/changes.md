# LGO Changelog

## 20201030.1

-   Fixed a possible problem in the licensing routines for computer with many MAC addresses.

## 20201030

-   Relinked with and updated ASL2, which fixes some more minor problems affecting Hessian computations.

## 20201018

-   Relinked with an updated ASL2, fixing a bug affecting Hessian computations.

## 20190908

-   Relink to ignore any LOGWAIT keywords in the ampl.lic or ampl.netlic file.

## 20190315

-   Relink to fix bugs with “objrep” when several objectives can be adjusted.

## 20190123

-   Add keyword “linwarn” (default 1) to control whether a warning about linear problems is given and whether lgo should exit when the problem is linear or when integer variables are present: sum of
    
    ```
       1 = yes (default)
       2 = abort execution if the problem is purely linear
       4 = abort execution if integer variables are present.
    ```
    

## 20190110

-   Increase internal array sizes to double the problem size allowed. On some platforms (MS Windows, Raspberry Pi), the resulting binaries fault, so they have not been updated.

## 20181120

-   Relink to ignore HEARTBEAT lines in the ampl.lic file.

## 20170803

-   Relink to fix possible trouble with objrep when the last constraint replaces the objective.

## 20170511

-   New keyword “version” (no value) causes version, platfform, and license details to be printed initially.

## 20151208

-   For those who do not have it, add libgfortran.so.3 to Linux bundles.

## 20150630

-   Fix some possible trouble with a single-use license.

## 20150526

-   Adjust solve\_message when interrupted by control-C; add 6 to solve\_result\_num values in this case.

## 20150424

-   Fix a rarely seen licensing glitch.

## 20150316

-   README.lgo (in lgo.doc.\*): minor edits.

## 20150218

-   Update to LGO version 2015-01-17.