# Academic License Troubleshooting

This guide covers some common issues when activating or using Academic licenses, Course Bundle licenses, and other trial licenses such as Community Edition for industry practitioners.

## General Licensing Notes

* To **activate your license** in Python, run:

  ```bash
  python -m amplpy.modules activate <license-uuid>
  ```

* Or, in a **Jupyter notebook**:

  ```python
  from amplpy import AMPL, ampl_notebook
  ampl = ampl_notebook(
      modules=["gurobi", "xpress", "highs"],  # modules to install
      license_uuid=<license-uuid>          # license to use
  )
  ```

* **Academic licenses** require an **active internet connection** to periodically renew its short-term lease.

* Install AMPL in your **user home directory**, typically (on Windows):

  ```
  C:\Users\<YOUR_USERNAME>\AMPL\
  ```

* **Do not install** Academic licenses in read-only locations (e.g., `C:\Program Files\AMPL\`).

---

## Common Issues & Fixes

### 1. License Renewal Error

**Example error:**

```
Please make sure your internet connection is working in order to renew the license
C:\Users\USER\AMPL\ampl.lic: Short term lease expired.
```

**Explanation:**

* The short-term license lease couldn’t be renewed due to:

  * No active internet connection, or
  * Installation in a **read-only directory** that prevents license updates. This is a typical Windows issue when AMPL is installed in `C:\Program Files\AMPL\`.

**Fix:**

1. Ensure you have a **stable internet connection**.
2. Restart AMPL.
3. If AMPL is installed in a protected directory (e.g., `C:\Program Files\AMPL\`), reinstall it under:

   ```
   C:\Users\<YOUR_USERNAME>\AMPL\
   ```
---

### 2. "Bundle Expired" Message

**Example error:**

```
# Bundle #2837.7303 expiring 20250215
No ampl license for this machine.
```

**Explanation:**

* Your **AMPL bundle license has expired**.

**Fix:**

1. Log in to your account on [portal.ampl.com](https://portal.ampl.com) to check active bundles.
2. If none are active, request a new one:
    - [Request a new academic bundle](https://portal.ampl.com/user/ampl/request/ampl-for-courses/new)
3. If you already had one:
    - [Download your bundle](https://portal.ampl.com/download/ampl/bundle/<your-bundle-uuid>)
4. Activate your new license bundle following the [installation instructions](https://dev.ampl.com/ampl/install.html).

---

### 3. Showing demo license after full license activation

**Example symptoms:**

* License activation appears to succeed (no errors) using a command such as:

  ```
  ampl: shell "amplkey activate --uuid <license-uuid>";
  ```

* However, when running a model, AMPL still displays a demo limitation message:

  ```
  Sorry, a demo license is limited to 2000 variables and 2000 constraints and objectives for linear problems.
  You have <N> variables and <M> constraints.
  ```

**Explanation:**

The most common cause is that AMPL was activated in **one installation**, but the user later runs AMPL from a **different installation or executable**.

This can happen when:

* Multiple AMPL installations exist on the system (e.g., in different folders or environments, Amplpy and a previous AMPL-standalone version).
* The activation was performed using one method (e.g., inside AMPL or via amplkey), but AMPL is later invoked from a different location, like from Amplpy. The other way around is true, activating with `` won't ensure that an independent previous installation will find the license.

**Fix / Diagnostic Steps:**

1. When using Python, you don't need to run the `amplkey` command. Ensure activation is done in the same environment and installation:

   ```bash
   python -m amplpy.modules install base --upgrade # update ampl version
   python -m amplpy.modules activate <license-uuid>
   ```

2. For standalone installations of AMPL, **identify which AMPL executable is being used** when running the model.
   For example:

   ```bash
   which ampl
   ```

   or on Windows:

   ```
   where ampl
   ```

* Confirm that this is the same AMPL installation where the license was activated, or activate it again:

  ```
  ampl: shell "amplkey activate --uuid <license-uuid>";
  ```

**Reference:**

Installation and activation workflow details:
[https://dev.ampl.com/ampl/install.html]()

---

### 4. "No AMPL License for This Machine" in Synced Folders (e.g., OneDrive)

**Example error:**

```
No ampl license for this machine.
AMPL path:
C:\Users\user\OneDrive - <University>\ampl_mswin64\ampl.exe
```

**Explanation:**

* AMPL was installed in a **OneDrive-synced folder**.
* OneDrive may overwrite or lock the license file during synchronization.

**Fix:**

1. Move your AMPL installation to a **non-synced local directory**, such as:

   ```
   C:\Users\<YOUR_USERNAME>\AMPL\
   ```
2. Activate your new license using the uuid following the [installation instructions](https://dev.ampl.com/ampl/install.html).

---

## Extending Solver Trials

If your **trial license for commercial solvers** (e.g., Gurobi, CPLEX) has expired, you can request an extension through the AMPL Portal:
   
   * [AMPL Community Edition Trial Extension](https://ampl.com/trial)

AMPL will review your request and grant an extension where eligible.

---

## Contact Support

If your issue remains unresolved, please include the following when contacting support:

   * The **full error message**
   * The **log file** (if available, find it with `ampl: shell "amplkey show log";`):
     ```
     C:\Users\<YOUR_USERNAME>\AMPL\amplkey.log
     ```
   * Send it to **[licensing@ampl.com](mailto:licensing@ampl.com)**.

---

## 🔗 Useful Links

* [AMPL Installation Instructions](https://dev.ampl.com/ampl/install.html)
* [Static Fingerprint Guide](https://dev.ampl.com/help/get-fingerprint.html)
* [Amplpy documentation](https://amplpy.ampl.com/en/latest/index.html)

