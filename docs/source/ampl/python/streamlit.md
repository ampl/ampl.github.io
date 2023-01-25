# AMPL on Streamlit

Since AMPL and all Solvers are now available as [Python Packages](modules.md). To use them in [streamlit](https://streamlit.io) you just need to list the modules in the requirements.txt file as follows:

```
--index-url https://pypi.ampl.com # AMPL's Python Package Index
--extra-index-url https://pypi.org/simple
ampl_module_base # AMPL and base tools
ampl_module_highs # HiGHS solver
ampl_module_gurobi # Gurobi solver
amplpy # Python API for AMPL
```

and load them in [streamlit_app.py](streamlit_app.py):
```python
from amplpy import AMPL, modules
modules.load()
```

- [Python API documentation](https://amplpy.readthedocs.io)
- [Python modules documentation](modules.md)

## N-Queens using AMPL and HiGHS

Running on [Streamlit Cloud](https://share.streamlit.io/fdabrandao/streamlit-nqueens/).
Project GitHub: <https://github.com/fdabrandao/streamlit-nqueens>

Run it locally:
```bash
$ git clone https://github.com/fdabrandao/streamlit-nqueens.git
$ cd streamlit-nqueens
$ python -m venv venv
$ sournce venv/bin/activate
$ python -m install -r requirements.txt --upgrade
$ streamlit run streamlit_app.py
```

Deploy to [Streamlit Cloud](https://streamlit.io/) for free!

