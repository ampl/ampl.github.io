# AMPL on Streamlit Cloud

Since AMPL and all Solvers are now available as [Python Packages](modules.md). To use them in [streamlit](https://streamlit.io) you just need to list the modules in the [requirements.txt](https://github.com/fdabrandao/streamlit-nqueens/blob/master/requirements.txt) file as follows:

```
--index-url https://pypi.ampl.com # AMPL's Python Package Index
--extra-index-url https://pypi.org/simple
ampl_module_base # AMPL
ampl_module_highs # HiGHS solver
ampl_module_gurobi # Gurobi solver
amplpy # Python API for AMPL
```

and load them in [streamlit_app.py](https://github.com/fdabrandao/streamlit-nqueens/blob/master/streamlit_app.py):
```python
from amplpy import AMPL
ampl = AMPL()
```

- [Python API documentation](https://amplpy.ampl.com)
- [Python modules documentation](modules.md)

## N-Queens Using AMPL and HiGHS

- Running on Streamlit Cloud: [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/fdabrandao/streamlit-nqueens/)
- Project GitHub: <https://github.com/fdabrandao/streamlit-nqueens>


<a href="https://share.streamlit.io/fdabrandao/streamlit-nqueens/" target="_blank">
    <video width="100%" autoplay loop muted poster="https://ampl.com/upload/videos/nqueens_streamlit_poster.jpg">
        <source src="https://ampl.com/upload/videos/nqueens_streamlit.mp4" type="video/mp4" />
    </video>
</a>

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
