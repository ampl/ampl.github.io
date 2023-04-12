(ampl_cicd)=
# Continuous Integration (CI/CD)

AMPL can be easily used in [Continuous Integration/Continuous Delivery (CI/CD)](https://en.wikipedia.org/wiki/CI/CD) platforms in order to test your optimization applications before deploying to production.

The most convenient way is by using the [Python modules](../python/modules.md), even if your optimization application is built using another [AMPL API](../apis).
Since AMPL and all solvers are now available as [Python Packages](../python/modules.md). It is only necessary to have a step which installs [amplpy](https://amplpy.readthedocs.io) and the modules needed by your application:

```bash
python -m pip install amplpy
python -m amplpy.modules install <solver1> <solver2> # install the solvers you need
python -m amplpy.activate <license-uuid> # activate your license
```

In order to then be able to access AMPL and solvers when using
[AMPL APIs](../apis) other than [amplpy](https://amplpy.readthedocs.io) the
only additional step is to add to the environment variable path the paths to the modules installed:

```bash
export PATH=$PATH:$(python -m amplpy.modules path)
```

Below we have examples for two popular CI/CD platforms: [GitHub Actions](https://github.com/features/actions) and [Azure Pipelines](https://azure.microsoft.com/en-us/products/devops/pipelines). The setup is very similar for others.

```{note}
 **Contact us at <support@ampl.com> for free support setting up AMPL in your CI/CD platform.** You can also any questions you have on our [Discourse Forum](https://discuss.ampl.com).
```

## GitHub Actions

[Example configuration for GitHub Actions](https://github.com/ampl/amplpyfinance/blob/master/.github/workflows/test.yaml) used in the example project [amplpyfinance](https://github.com/ampl/amplpyfinance).

File `".github/workflows/test.yaml"`:
```yaml
name: Test
run-name: ${{ github.actor }} is building "${{ github.ref_name }}"
on: [push]

jobs:
  Test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.10"]

    steps:
      - uses: actions/checkout@v3
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install dependencies
        run: |
          set -ex
          python -m pip install -r requirements.txt
          python -m pip install amplpy
          python -m amplpy.modules install <solver1> <solver2>
          python -m amplpy.activate <license-uuid>
      - name: Install package
        run: |
          python -m pip install .
      - name: Test package
        run: |
          python -m <package-name>.tests
```

## Azure Pipelines

[Example configuration for Azure Pipelines](https://github.com/ampl/amplpyfinance/blob/master/azure-pipelines.yml) used in the example project [amplpyfinance](https://github.com/ampl/amplpyfinance).

File `"azure-pipelines.yml"`:
```yaml
jobs:
- job: Test
  pool: {vmImage: 'ubuntu-latest'}
  strategy:
    matrix:
      Python 3.10:
        PYTHON_VERSION: 3.10
  steps:
    - task: UsePythonVersion@0
      inputs:
        versionSpec: $(PYTHON_VERSION)
    - bash: python --version
      displayName: Check python version
    - bash: |
        set -ex
        python -m pip install -r requirements.txt
        python -m pip install amplpy
        python -m amplpy.modules install <solver1> <solver2>
        python -m amplpy.activate <license-uuid>
      displayName: Install dependencies
    - bash: |
        python -m pip install .
      displayName: Install package
    - bash: |
        python -m <package-name>.tests
      displayName: Test package
```
